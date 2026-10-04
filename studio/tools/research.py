#!/usr/bin/env python3
"""유튜브 리서치·분석 도구 (YouTube Data API v3, 공개 데이터)

사용법:
  python3 studio/tools/research.py topic "습관 만들기" [--days 90] [--n 50] [--shorts|--long]
  python3 studio/tools/research.py video https://youtu.be/VIDEO_ID [--peers 30]
  python3 studio/tools/research.py channel @핸들 또는 UC... [--n 30]

결과: studio/research/<이름>/report.md (사람·Claude 가 읽는 리포트) + data.json (원자료)
API 키: 환경변수 YOUTUBE_API_KEY → GOOGLE_API_KEY → GOOGLE_TTS_API_KEY 순으로 사용
할당량(하루 10,000): 검색 1회 100, 영상·채널·댓글 조회 1회 1
"""
import argparse, json, os, re, statistics, sys, urllib.error, urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://www.googleapis.com/youtube/v3/"
KST = timezone(timedelta(hours=9))
DAYS = "월화수목금토일"
STOP = set("그리고 그래서 하는 있는 없는 이런 저런 그런 하면 해서 그냥 진짜 너무 정말 the a of to and in for is on with 이 그 저 것 수 등 및 더 왜 뭐".split())
ROOT = Path(__file__).resolve().parents[1] / "research"


def key():
    for k in ("YOUTUBE_API_KEY", "GOOGLE_API_KEY", "GOOGLE_TTS_API_KEY"):
        if os.environ.get(k):
            return os.environ[k]
    sys.exit("API 키가 없습니다. 환경변수 YOUTUBE_API_KEY (또는 GOOGLE_TTS_API_KEY)를 설정하세요.")


def call(endpoint, **params):
    params["key"] = key()
    url = API + endpoint + "?" + urllib.parse.urlencode(params, doseq=True)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        err = json.loads(e.read() or b"{}").get("error", {})
        reason = ",".join(d.get("reason", "") for d in err.get("details", []) + err.get("errors", []) if d.get("reason"))
        hint = {
            "SERVICE_DISABLED": "Google Cloud 콘솔에서 'YouTube Data API v3' 를 사용 설정하세요.",
            "API_KEY_SERVICE_BLOCKED": "API 키 제한사항에 'YouTube Data API v3' 를 추가로 체크하세요.",
            "quotaExceeded": "오늘 할당량을 다 썼습니다. 내일(태평양 시간 자정) 초기화됩니다.",
            "commentsDisabled": None,
        }
        for r_, h in hint.items():
            if r_ in reason or r_ in err.get("status", ""):
                if h is None:
                    return {"items": []}
                sys.exit(f"YouTube API 오류 {e.code}: {h}")
        sys.exit(f"YouTube API 오류 {e.code}: {err.get('message', '')[:200]}")


def chunks(xs, n=50):
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def iso_dur(s):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return 0
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + se


def fmt_dur(sec):
    return f"{sec // 60}:{sec % 60:02d}" if sec < 3600 else f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def human(n):
    n = float(n)
    if n >= 1e8:
        return f"{n / 1e8:.1f}억"
    if n >= 1e4:
        return f"{n / 1e4:.1f}만"
    if n >= 1e3:
        return f"{n / 1e3:.1f}천"
    return f"{int(n)}"


def videos_detail(ids):
    out = []
    for c in chunks(ids):
        out += call("videos", part="snippet,statistics,contentDetails", id=",".join(c)).get("items", [])
    return out


def channels_subs(ch_ids):
    subs = {}
    for c in chunks(list(set(ch_ids))):
        for it in call("channels", part="statistics,snippet", id=",".join(c)).get("items", []):
            st = it.get("statistics", {})
            subs[it["id"]] = None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0))
    return subs


def top_comments(vid, n=20):
    items = call("commentThreads", part="snippet", videoId=vid, order="relevance", maxResults=n,
                 textFormat="plainText").get("items", [])
    out = []
    for it in items:
        s = it["snippet"]["topLevelComment"]["snippet"]
        out.append({"text": s.get("textDisplay", "")[:300], "likes": int(s.get("likeCount", 0))})
    return out


def enrich(items, subs):
    now = datetime.now(timezone.utc)
    rows = []
    for it in items:
        sn, st, cd = it["snippet"], it.get("statistics", {}), it.get("contentDetails", {})
        pub = datetime.fromisoformat(sn["publishedAt"].replace("Z", "+00:00"))
        views = int(st.get("viewCount", 0))
        likes = int(st.get("likeCount", 0)) if "likeCount" in st else None
        comments = int(st.get("commentCount", 0)) if "commentCount" in st else None
        age = max((now - pub).total_seconds() / 86400, 0.5)
        sub = subs.get(sn["channelId"])
        dur = iso_dur(cd.get("duration"))
        title = sn.get("title", "")
        kst = pub.astimezone(KST)
        rows.append({
            "id": it["id"], "url": f"https://youtu.be/{it['id']}", "title": title,
            "channel": sn.get("channelTitle", ""), "channel_id": sn["channelId"], "subs": sub,
            "published": kst.strftime("%Y-%m-%d %H:%M"), "weekday": DAYS[kst.weekday()], "hour": kst.hour,
            "age_days": round(age, 1), "views": views, "likes": likes, "comments": comments,
            "views_per_day": round(views / age), "duration": dur, "is_short": dur <= 180,
            "outlier": round(views / sub, 2) if sub else None,
            "engagement": round(((likes or 0) + (comments or 0)) / views * 100, 2) if views else 0,
            "tags": sn.get("tags", []), "description": sn.get("description", "")[:600],
            "title_len": len(title), "has_number": bool(re.search(r"\d", title)),
            "has_question": "?" in title, "has_exclaim": "!" in title,
            "has_bracket": bool(re.search(r"[\[\]【】()〈〉<>]", title)),
            "thumb": sn.get("thumbnails", {}).get("high", {}).get("url", ""),
        })
    return rows


def words(texts):
    c = Counter()
    for t in texts:
        for w in re.findall(r"[가-힣A-Za-z0-9]{2,}", t):
            w = w.lower()
            if w not in STOP and not w.isdigit():
                c[w] += 1
    return c


def pct(xs):
    return f"{sum(xs) / len(xs) * 100:.0f}%" if xs else "-"


def med(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else 0


def pattern_table(top, rest):
    def col(rows):
        return [
            f"{med([r['title_len'] for r in rows]):.0f}자",
            pct([r["has_number"] for r in rows]), pct([r["has_question"] for r in rows]),
            pct([r["has_exclaim"] for r in rows]), pct([r["has_bracket"] for r in rows]),
            fmt_dur(int(med([r["duration"] for r in rows]))),
            f"{med([r['engagement'] for r in rows]):.2f}%",
        ]
    names = ["제목 길이(중앙값)", "제목에 숫자", "질문형(?)", "느낌표(!)", "괄호·대괄호", "영상 길이(중앙값)", "참여율(좋아요+댓글/조회)"]
    a, b = col(top), col(rest) if rest else ["-"] * len(names)
    lines = ["| 항목 | 상위 25% | 나머지 |", "|---|---|---|"]
    lines += [f"| {n} | {x} | {y} |" for n, x, y in zip(names, a, b)]
    return "\n".join(lines)


def timing(rows):
    if not rows:
        return "-"
    wd = Counter(r["weekday"] for r in rows).most_common(3)
    hr = Counter(f"{r['hour']:02d}시" for r in rows).most_common(3)
    return f"요일: {', '.join(f'{d}({n})' for d, n in wd)} / 시간(KST): {', '.join(f'{h}({n})' for h, n in hr)}"


def video_line(r, i=None):
    sub = f"구독 {human(r['subs'])}" if r["subs"] else "구독 비공개"
    ol = f" · **구독자 대비 {r['outlier']}배**" if r["outlier"] else ""
    return (f"{'' if i is None else f'{i}. '}[{r['title']}]({r['url']}) — {r['channel']} ({sub})  \n"
            f"   조회 {human(r['views'])} · 하루 {human(r['views_per_day'])}회{ol} · {fmt_dur(r['duration'])} · "
            f"참여율 {r['engagement']}% · {r['published']}({r['weekday']})")


def comments_block(rows, n_videos=5):
    out = []
    for r in rows[:n_videos]:
        cs = top_comments(r["id"], 15)
        r["top_comments"] = cs
        if cs:
            out.append(f"**{r['title']}**")
            out += [f"- ({c['likes']}👍) {' '.join(c['text'].split())[:140]}" for c in sorted(cs, key=lambda c: -c["likes"])[:6]]
            out.append("")
    return "\n".join(out) or "(댓글 없음/비활성)"


GUIDE = """## Claude 분석 가이드
이 리포트를 읽은 Claude 는 아래 질문에 답해 `insights.md` 로 정리합니다.
1. **떡상 공식**: 구독자 대비 배수 상위 영상들의 공통점(주제 각도·제목 구조·길이·타이밍)은?
2. **제목 패턴**: 상위 25% 와 나머지의 차이에서 우리 제목에 적용할 규칙 3가지
3. **시청자 욕구**: 댓글에서 반복되는 질문·불만·요청 → 다음 영상 소재 5개
4. **빈틈**: 수요(조회수)는 큰데 공급(영상 수·품질)이 부족해 보이는 하위 주제
5. **우리 채널 적용**: 만화 대화극 형식으로 바꿨을 때의 제목 5개 / 썸네일 문구 3개 / 첫 3초 후크 대사 3개
"""


def save(name, report, data):
    d = ROOT / re.sub(r"[^\w가-힣-]+", "-", name).strip("-")[:60]
    d.mkdir(parents=True, exist_ok=True)
    (d / "report.md").write_text(report, encoding="utf-8")
    (d / "data.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"✔ {d / 'report.md'}")
    return d


def cmd_topic(a):
    after = (datetime.now(timezone.utc) - timedelta(days=a.days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    params = dict(part="id", q=a.keyword, type="video", order="viewCount", publishedAfter=after,
                  regionCode=a.region, relevanceLanguage="ko", maxResults=min(a.n, 50))
    if a.shorts:
        params["videoDuration"] = "short"
    elif a.long:
        params["videoDuration"] = "medium"  # 4~20분
    ids = [it["id"]["videoId"] for it in call("search", **params).get("items", [])]
    if not ids:
        sys.exit("검색 결과가 없습니다. 키워드나 --days 를 바꿔 보세요.")
    items = videos_detail(ids)
    rows = enrich(items, channels_subs([it["snippet"]["channelId"] for it in items]))
    rows.sort(key=lambda r: -(r["outlier"] or 0))
    by_views = sorted(rows, key=lambda r: -r["views"])
    q = max(1, len(rows) // 4)
    top, rest = by_views[:q], by_views[q:]
    out = [f"# 주제 리서치: {a.keyword}",
           f"최근 {a.days}일 · 조회수 상위 {len(rows)}개 · 지역 {a.region}"
           + (" · 숏폼" if a.shorts else " · 롱폼(4~20분)" if a.long else "") + f" · 생성 {datetime.now(KST):%Y-%m-%d %H:%M}",
           "", "## 한눈에 보기",
           f"- 조회수 중앙값 {human(med([r['views'] for r in rows]))} · 하루 조회 중앙값 {human(med([r['views_per_day'] for r in rows]))}",
           f"- 숏폼 비율 {pct([r['is_short'] for r in rows])} · 영상 길이 중앙값 {fmt_dur(int(med([r['duration'] for r in rows])))}",
           f"- 상위 25% 업로드 타이밍 — {timing(top)}",
           "", "## 떡상 영상 (구독자 대비 조회수 배수 순)",
           "작은 채널인데 크게 터진 영상 = 주제·제목·썸네일의 힘이 컸다는 신호", ""]
    min_v = max(med([r["views"] for r in rows]), 3000)  # 너무 작은 영상·채널의 착시 배수 제외
    hits = [r for r in rows if r["outlier"] and r["views"] >= min_v and (r["subs"] or 0) >= 100]
    out.append(f"(조회수 {human(min_v)} 이상 · 구독자 100명 이상만)")
    out.append("")
    out += [video_line(r, i) for i, r in enumerate(hits[:10], 1)] or ["(조건에 맞는 영상 없음)"]
    out += ["", "## 조회수 Top 10", ""] + [video_line(r, i) for i, r in enumerate(by_views[:10], 1)]
    out += ["", "## 제목·형식 패턴 (조회수 상위 25% vs 나머지)", "", pattern_table(top, rest)]
    tw = words(r["title"] for r in top).most_common(20)
    tg = Counter(t.lower() for r in rows for t in r["tags"]).most_common(25)
    out += ["", "## 자주 쓰인 단어", f"- 상위 영상 제목: {', '.join(f'{w}({n})' for w, n in tw)}",
            f"- 태그: {', '.join(f'{w}({n})' for w, n in tg) or '(태그 비공개)'}"]
    out += ["", "## 시청자 댓글 (떡상 상위 5개 영상)", "", comments_block(hits or by_views), GUIDE]
    save(f"topic-{a.keyword}", "\n".join(out), {"keyword": a.keyword, "days": a.days, "videos": rows})


def parse_vid(s):
    m = re.search(r"(?:v=|youtu\.be/|shorts/|embed/)([\w-]{11})", s)
    return m.group(1) if m else s


def cmd_video(a):
    vid = parse_vid(a.url)
    items = videos_detail([vid])
    if not items:
        sys.exit("영상을 찾을 수 없습니다 (비공개/삭제/잘못된 링크).")
    me = enrich(items, channels_subs([items[0]["snippet"]["channelId"]]))[0]
    # 비교군: 같은 주제(태그/제목 핵심어)로 검색한 최근 영상들
    kw = " ".join((me["tags"][:3] if me["tags"] else [w for w, _ in words([me["title"]]).most_common(3)]))
    ids = [it["id"]["videoId"] for it in call("search", part="id", q=kw, type="video", order="relevance",
                                              regionCode="KR", relevanceLanguage="ko", maxResults=a.peers).get("items", [])]
    ids = [i for i in ids if i != vid]
    pitems = videos_detail(ids)
    peers = enrich(pitems, channels_subs([it["snippet"]["channelId"] for it in pitems]))
    peers = [p for p in peers if p["is_short"] == me["is_short"]] or peers
    rank = sorted(peers + [me], key=lambda r: -r["views_per_day"]).index(me) + 1

    def cmp(label, mine, others, f=lambda x: x):
        m = med(others)
        mark = "▲" if mine > m else ("▼" if mine < m else "=")
        return f"| {label} | {f(mine)} | {f(m)} | {mark} |"

    out = [f"# 영상 분석: {me['title']}", f"{me['url']} · {me['channel']} · 생성 {datetime.now(KST):%Y-%m-%d %H:%M}", "",
           "## 성과", video_line(me), "",
           f"- 비교군 {len(peers)}개 중 **하루 조회수 {rank}위** (비교 키워드: `{kw}`)", "",
           "## 비교군 대비", "| 항목 | 이 영상 | 비교군 중앙값 | |", "|---|---|---|---|",
           cmp("하루 조회수", me["views_per_day"], [p["views_per_day"] for p in peers], human),
           cmp("구독자 대비 배수", me["outlier"] or 0, [p["outlier"] for p in peers if p["outlier"]], lambda x: f"{x:.2f}배"),
           cmp("참여율", me["engagement"], [p["engagement"] for p in peers], lambda x: f"{x:.2f}%"),
           cmp("제목 길이", me["title_len"], [p["title_len"] for p in peers], lambda x: f"{x:.0f}자"),
           cmp("영상 길이", me["duration"], [p["duration"] for p in peers], lambda x: fmt_dur(int(x))),
           "", "## 제목·설명·태그",
           f"- 제목 특징: 숫자 {'O' if me['has_number'] else 'X'} · 질문형 {'O' if me['has_question'] else 'X'} · "
           f"느낌표 {'O' if me['has_exclaim'] else 'X'} · 괄호 {'O' if me['has_bracket'] else 'X'}",
           f"- 태그({len(me['tags'])}개): {', '.join(me['tags'][:20]) or '(없음/비공개)'}",
           f"- 설명 첫 부분: {me['description'][:200].replace(chr(10), ' ')}",
           f"- 업로드: {me['published']} ({me['weekday']})", "",
           "## 비교군 상위 5 (하루 조회수)", ""]
    out += [video_line(p, i) for i, p in enumerate(sorted(peers, key=lambda r: -r["views_per_day"])[:5], 1)]
    out += ["", "## 이 영상의 시청자 댓글", "", comments_block([me], 1),
            "## Claude 분석 가이드",
            "1. 비교군 대비 ▲/▼ 항목으로 '왜 잘 됐나/안 됐나' 가설 3개 (제목 각도·썸네일 문구·길이·타이밍·주제 수요)",
            "2. 댓글 반응에서 드러난 시청 동기와 아쉬운 점",
            "3. 다음 영상에서 그대로 유지할 것 / 바꿀 것 각 3가지",
            "4. 같은 주제로 다시 만든다면: 제목 3개, 썸네일 문구 3개, 첫 3초 후크 대사 3개"]
    save(f"video-{vid}", "\n".join(out), {"video": me, "peers": peers, "keyword": kw})


def cmd_channel(a):
    s = a.channel.strip()
    if s.startswith("@") or "youtube.com/@" in s:
        handle = "@" + s.split("@", 1)[1].split("/")[0]
        res = call("channels", part="snippet,statistics,contentDetails", forHandle=handle)
    else:
        cid = re.search(r"(UC[\w-]{22})", s)
        res = call("channels", part="snippet,statistics,contentDetails", id=cid.group(1) if cid else s)
    if not res.get("items"):
        sys.exit("채널을 찾을 수 없습니다. @핸들 또는 UC로 시작하는 채널 ID 를 넣으세요.")
    ch = res["items"][0]
    st = ch["statistics"]
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    ids, token = [], None
    while len(ids) < a.n:
        r = call("playlistItems", part="contentDetails", playlistId=uploads, maxResults=50,
                 **({"pageToken": token} if token else {}))
        ids += [it["contentDetails"]["videoId"] for it in r.get("items", [])]
        token = r.get("nextPageToken")
        if not token:
            break
    ids = ids[:a.n]
    subs = None if st.get("hiddenSubscriberCount") else int(st.get("subscriberCount", 0))
    rows = enrich(videos_detail(ids), {ch["id"]: subs})
    longs = [r for r in rows if not r["is_short"]]
    shorts = [r for r in rows if r["is_short"]]
    est_hours = sum(r["views"] * min(r["duration"], 600) * .35 for r in longs) / 3600  # 추정치
    by = sorted(rows, key=lambda r: -r["views_per_day"])
    out = [f"# 채널 분석: {ch['snippet']['title']}",
           f"구독자 {human(subs) if subs else '비공개'} · 총 조회 {human(st.get('viewCount', 0))} · 영상 {st.get('videoCount')}개 · 생성 {datetime.now(KST):%Y-%m-%d %H:%M}",
           "", "## 최근 영상 요약",
           f"- 분석 {len(rows)}개 (롱폼 {len(longs)} / 숏폼 {len(shorts)})",
           f"- 롱폼 조회 중앙값 {human(med([r['views'] for r in longs]))} · 숏폼 조회 중앙값 {human(med([r['views'] for r in shorts]))}",
           f"- 롱폼 시청시간 **대략** {human(est_hours)}시간 (평균 시청률 35% 가정 추정치, 정확한 값은 YouTube 스튜디오)",
           f"- 숏폼 조회 합계 {human(sum(r['views'] for r in shorts))}회",
           "", "## 잘 된 영상 Top 5 (하루 조회수)", ""] + [video_line(r, i) for i, r in enumerate(by[:5], 1)]
    out += ["", "## 부진한 영상 Bottom 5", ""] + [video_line(r, i) for i, r in enumerate(by[-5:][::-1], 1)]
    out += ["", "## 잘 된 영상 vs 나머지", "", pattern_table(by[:max(1, len(by) // 4)], by[max(1, len(by) // 4):]),
            "", "## Claude 분석 가이드",
            "1. Top 5 와 Bottom 5 의 차이(주제·제목·썸네일 문구·길이·업로드 시간) → 성공 공식 3가지",
            "2. 롱폼↔숏폼 연계: 숏폼이 잘 된 주제를 롱폼으로 확장할 후보",
            "3. 다음 2주 업로드 계획 (주제·제목·형식) 제안"]
    save(f"channel-{ch['snippet']['title']}", "\n".join(out), {"channel": ch, "videos": rows})


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="유튜브 리서치·분석 (YouTube Data API v3)")
    sp = ap.add_subparsers(dest="cmd", required=True)
    t = sp.add_parser("topic", help="키워드 주제 리서치")
    t.add_argument("keyword")
    t.add_argument("--days", type=int, default=90)
    t.add_argument("--n", type=int, default=50)
    t.add_argument("--region", default="KR")
    g = t.add_mutually_exclusive_group()
    g.add_argument("--shorts", action="store_true")
    g.add_argument("--long", action="store_true")
    v = sp.add_parser("video", help="영상 하나 '왜 잘 됐나' 분석")
    v.add_argument("url")
    v.add_argument("--peers", type=int, default=30)
    c = sp.add_parser("channel", help="채널 성과 분석")
    c.add_argument("channel")
    c.add_argument("--n", type=int, default=30)
    a = ap.parse_args()
    {"topic": cmd_topic, "video": cmd_video, "channel": cmd_channel}[a.cmd](a)
