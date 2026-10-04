#!/usr/bin/env python3
"""YouTube 자동 업로드 (YouTube Data API v3, OAuth 2.0)

사용법:
  python3 studio/tools/upload.py auth                      # 최초 1회: 구글 계정 연결 → 리프레시 토큰 발급
  python3 studio/tools/upload.py auth --manual             # 기기 코드 방식이 막힐 때: 주소창 URL 복사 방식
  python3 studio/tools/upload.py upload studio/projects/<slug>/project.json --dry-run   # 보낼 내용만 확인
  python3 studio/tools/upload.py upload studio/projects/<slug>/project.json [--only long|shorts]

필요한 환경변수 (클라우드 환경 설정의 환경 변수 칸에 저장):
  YT_CLIENT_ID, YT_CLIENT_SECRET   Google Cloud 콘솔 → 사용자 인증 정보 → OAuth 클라이언트 ID
  YT_REFRESH_TOKEN                 auth 명령으로 발급
  YT_AUDITED=1                     YouTube API 심사 통과 후 설정 (그 전에는 업로드 영상이 비공개로 잠김)

업로드 정보는 studio.py kit 과 같은 publish_info()(project.json 의 publish, shorts[])를 씁니다.
이미 올린 파일은 output/uploaded.json 에 기록되어 다시 올리지 않습니다.
할당량: 영상 업로드는 1회에 많은 할당량을 씁니다(하루 기본 10,000 중 상당 부분). 하루 몇 편으로 나눠 올리세요.
"""
import argparse, io, json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import studio  # noqa: E402

SCOPES = "https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube"
TOKEN_URL = "https://oauth2.googleapis.com/token"
DEVICE_URL = "https://oauth2.googleapis.com/device/code"
API = "https://www.googleapis.com/youtube/v3/"
UPLOAD = "https://www.googleapis.com/upload/youtube/v3/"


def env(name, required=True):
    v = os.environ.get(name, "").strip()
    if required and not v:
        sys.exit(f"환경변수 {name} 이(가) 없습니다. studio/api-audit/README.md 의 '연결 준비'를 따라 설정하세요.")
    return v


def post_form(url, data):
    req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(),
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return json.loads(e.read() or b"{}") | {"_status": e.code}


def show_token(tok):
    rt = tok.get("refresh_token")
    if not rt:
        sys.exit(f"리프레시 토큰을 받지 못했습니다: {tok}")
    print("\n✔ 연결 완료. 아래 한 줄을 클라우드 환경 설정의 '환경 변수'에 추가하세요 (다른 사람에게 보여주지 마세요):")
    print(f"YT_REFRESH_TOKEN={rt}")
    print("\n※ OAuth 동의 화면이 '테스트' 상태면 이 토큰은 7일 뒤 만료됩니다. 만료되면 auth 를 다시 실행하세요.")


def cmd_auth(a):
    cid, secret = env("YT_CLIENT_ID"), env("YT_CLIENT_SECRET")
    if a.manual:
        url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
            "client_id": cid, "redirect_uri": "http://localhost", "response_type": "code",
            "scope": SCOPES, "access_type": "offline", "prompt": "consent"})
        print("1) 아래 주소를 휴대폰/PC 브라우저에서 열고 YouTube 채널 계정으로 허용하세요.\n" + url)
        print("2) 허용 후 '연결할 수 없음' 페이지가 떠도 정상입니다. 그 페이지의 주소창 URL 전체를 복사해 붙여넣으세요.")
        got = input("URL: ").strip()
        code = urllib.parse.parse_qs(urllib.parse.urlparse(got).query).get("code", [got])[0]
        tok = post_form(TOKEN_URL, {"code": code, "client_id": cid, "client_secret": secret,
                                    "redirect_uri": "http://localhost", "grant_type": "authorization_code"})
        return show_token(tok)
    dev = post_form(DEVICE_URL, {"client_id": cid, "scope": SCOPES})
    if "device_code" not in dev:
        sys.exit(f"기기 코드 발급 실패: {dev.get('error')} {dev.get('error_description', '')}\n"
                 "→ OAuth 클라이언트 유형이 'TV 및 입력 제한 기기'인지 확인하거나, auth --manual 을 쓰세요.")
    print(f"1) 휴대폰에서 {dev['verification_url']} 을 열고\n2) 코드 {dev['user_code']} 를 입력한 뒤 YouTube 채널 계정으로 허용하세요.")
    print("   (허용할 때까지 기다립니다…)")
    interval = int(dev.get("interval", 5))
    deadline = time.time() + int(dev.get("expires_in", 1800))
    while time.time() < deadline:
        time.sleep(interval)
        tok = post_form(TOKEN_URL, {"client_id": cid, "client_secret": secret, "device_code": dev["device_code"],
                                    "grant_type": "urn:ietf:params:oauth:grant-type:device_code"})
        err = tok.get("error")
        if err == "authorization_pending":
            continue
        if err == "slow_down":
            interval += 5
            continue
        if err:
            sys.exit(f"연결 실패: {err} {tok.get('error_description', '')}")
        return show_token(tok)
    sys.exit("시간이 초과되었습니다. 다시 실행하세요.")


def access_token():
    tok = post_form(TOKEN_URL, {"client_id": env("YT_CLIENT_ID"), "client_secret": env("YT_CLIENT_SECRET"),
                                "refresh_token": env("YT_REFRESH_TOKEN"), "grant_type": "refresh_token"})
    if "access_token" not in tok:
        sys.exit(f"토큰 갱신 실패({tok.get('error')}). 7일 만료일 수 있습니다 → upload.py auth 를 다시 실행하세요.")
    return tok["access_token"]


def api(method, url, token, body=None, data=None, headers=None, want_headers=False):
    h = {"Authorization": f"Bearer {token}"} | (headers or {})
    if body is not None:
        data = json.dumps(body).encode()
        h["Content-Type"] = "application/json; charset=UTF-8"
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                raw = r.read()
                res = json.loads(raw) if raw else {}
                return (res, r.headers) if want_headers else res
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="ignore")[:400]
            if e.code in (500, 502, 503, 504) and attempt < 3:
                time.sleep(2 ** attempt * 3)
                continue
            hint = ""
            if "quotaExceeded" in msg:
                hint = " → 오늘 할당량 초과. 내일 이어서 실행하면 올린 것은 건너뜁니다."
            elif "youtubeSignupRequired" in msg:
                hint = " → 이 계정에 YouTube 채널이 없습니다."
            elif e.code == 403 and "thumbnails" in url:
                hint = " → 맞춤 썸네일은 휴대폰 인증된 채널만 가능합니다 (YouTube 스튜디오 → 설정 → 채널 → 기능 사용 자격)."
            raise RuntimeError(f"YouTube API {e.code}: {msg}{hint}")


def to_utc(s):
    if not s:
        return None
    d = datetime.fromisoformat(s)
    if d.tzinfo is None:
        d = d.replace(tzinfo=studio_kst())
    if d <= datetime.now(timezone.utc):
        return None  # 지난 시각이면 예약하지 않음
    return d.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def studio_kst():
    from datetime import timedelta
    return timezone(timedelta(hours=9))


def video_body(meta, pub):
    at = to_utc(meta.get("publish_at"))
    status = {"privacyStatus": "private" if at else meta.get("privacy", "private"),
              "selfDeclaredMadeForKids": bool(pub.get("made_for_kids", False)),
              "containsSyntheticMedia": bool(pub.get("synthetic_media", True))}
    if at:
        status["publishAt"] = at
    return {"snippet": {"title": meta["title"][:100], "description": meta["description"][:5000],
                        "tags": meta.get("tags", [])[:30], "categoryId": str(pub.get("category", 1)),
                        "defaultLanguage": "ko", "defaultAudioLanguage": "ko"},
            "status": status}


def upload_video(token, path, body):
    size = path.stat().st_size
    _, headers = api("POST", UPLOAD + "videos?uploadType=resumable&part=snippet,status", token, body=body,
                     headers={"X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)},
                     want_headers=True)
    loc = headers["Location"]
    with open(path, "rb") as fh:
        res = api("PUT", loc, token, data=fh, headers={"Content-Type": "video/mp4", "Content-Length": str(size)})
    return res["id"]


def set_thumbnail(token, vid, png):
    from PIL import Image
    buf = io.BytesIO()
    Image.open(png).convert("RGB").save(buf, "JPEG", quality=90)
    api("POST", UPLOAD + f"thumbnails/set?videoId={vid}", token, data=buf.getvalue(),
        headers={"Content-Type": "image/jpeg"})


def add_to_playlist(token, vid, title):
    pls = api("GET", API + "playlists?part=snippet&mine=true&maxResults=50", token).get("items", [])
    pid = next((p["id"] for p in pls if p["snippet"]["title"] == title), None)
    if not pid:
        pid = api("POST", API + "playlists?part=snippet,status", token,
                  body={"snippet": {"title": title, "defaultLanguage": "ko"}, "status": {"privacyStatus": "public"}})["id"]
    api("POST", API + "playlistItems?part=snippet", token,
        body={"snippet": {"playlistId": pid, "resourceId": {"kind": "youtube#video", "videoId": vid}}})


def cmd_upload(a):
    proj, root = studio.load(a.project)
    out = root / "output"
    pub, shorts = studio.publish_info(proj, root)
    jobs = []
    if a.only in (None, "long"):
        jobs.append(("longform.mp4", dict(pub), out / "thumbnail.png"))
    if a.only in (None, "shorts"):
        jobs += [(s["file"], s, None) for s in shorts]
    log_path = out / "uploaded.json"
    done = json.loads(log_path.read_text()) if log_path.exists() else {}
    if a.dry_run:
        for f, meta, thumb in jobs:
            print(f"── {f} {'(이미 업로드됨: ' + done[f] + ')' if f in done else ''}")
            print(json.dumps(video_body(meta, pub), ensure_ascii=False, indent=1)[:1500])
            print(f"   썸네일: {thumb.name if thumb and thumb.exists() else '-'} · 재생목록: {pub.get('playlist', '-')}")
        print("\n(--dry-run: 실제로 올리지 않았습니다)")
        return
    if os.environ.get("YT_AUDITED") != "1":
        print("⚠ YouTube API 심사 전입니다. 지금 올리는 영상은 '비공개'로 잠기고 공개로 바꿀 수 없습니다.\n"
              "  테스트 목적이면 계속, 아니면 업로드 키트(output/upload.html)로 직접 올리세요.")
        if input("계속할까요? (yes 입력): ").strip() != "yes":
            sys.exit("중단했습니다.")
    token = access_token()
    for f, meta, thumb in jobs:
        if f in done:
            print(f"· {f} 건너뜀 (이미 업로드: https://youtu.be/{done[f]})")
            continue
        path = out / f
        if not path.exists():
            print(f"! {f} 없음 — 먼저 렌더링하세요")
            continue
        print(f"[업로드] {f} …")
        vid = upload_video(token, path, video_body(meta, pub))
        done[f] = vid
        log_path.write_text(json.dumps(done, ensure_ascii=False, indent=1))
        print(f"  ✔ https://youtu.be/{vid}")
        if thumb and thumb.exists():
            try:
                set_thumbnail(token, vid, thumb)
                print("  ✔ 썸네일")
            except RuntimeError as e:
                print(f"  ! 썸네일 실패: {e}")
        if pub.get("playlist") and f == "longform.mp4":
            try:
                add_to_playlist(token, vid, pub["playlist"])
                print(f"  ✔ 재생목록: {pub['playlist']}")
            except RuntimeError as e:
                print(f"  ! 재생목록 실패: {e}")
    print("\n남은 수동 작업: 고정 댓글 고정, 썸네일 '테스트 및 비교'(YouTube 스튜디오 웹)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="YouTube 자동 업로드")
    sp = ap.add_subparsers(dest="cmd", required=True)
    au = sp.add_parser("auth", help="구글 계정 연결 (리프레시 토큰 발급)")
    au.add_argument("--manual", action="store_true", help="주소창 URL 복사 방식")
    up = sp.add_parser("upload", help="렌더링된 영상 업로드")
    up.add_argument("project")
    up.add_argument("--only", choices=["long", "shorts"])
    up.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    {"auth": cmd_auth, "upload": cmd_upload}[a.cmd](a)
