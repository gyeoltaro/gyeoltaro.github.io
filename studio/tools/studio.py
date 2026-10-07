#!/usr/bin/env python3
"""YouTube 자동화 스튜디오 - 영상 제작 엔진 (Claude Code가 직접 실행)

사용법:
  python3 studio/tools/studio.py check
  python3 studio/tools/studio.py long   studio/projects/<slug>/project.json
  python3 studio/tools/studio.py shorts studio/projects/<slug>/project.json
  python3 studio/tools/studio.py thumb  studio/projects/<slug>/project.json
  python3 studio/tools/studio.py kit    studio/projects/<slug>/project.json   # 휴대폰 업로드 키트
  python3 studio/tools/studio.py all    studio/projects/<slug>/project.json

필요: ffmpeg, Pillow, edge-tts (pip install pillow edge-tts)
음성: Google Cloud TTS(GOOGLE_TTS_API_KEY) → edge-tts → 구글 번역 음성 → espeak-ng(오프라인) → 무음 순으로 대체됩니다.
"""
import argparse, asyncio, hashlib, json, os, random, re, shutil, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cartoon  # noqa: E402
import sound  # noqa: E402

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
except ImportError:
    sys.exit("Pillow 가 필요합니다: pip install pillow")

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/nanum/NanumGothicBold.ttf",
    "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
    "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    "C:/Windows/Fonts/malgunbd.ttf",
]
THEMES = [  # (배경 위, 배경 아래, 강조색)
    ((18, 24, 48), (52, 28, 88), (255, 213, 79)),
    ((10, 40, 52), (16, 18, 40), (102, 240, 200)),
    ((46, 16, 28), (20, 20, 44), (255, 138, 128)),
]


def sh(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw).stdout


def dur(path):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "csv=p=0", str(path)]).strip())


def find_font(user_font=None):
    for p in ([user_font] if user_font else []) + FONT_CANDIDATES:
        if p and os.path.exists(p):
            return p
    sys.exit("한글 폰트를 찾지 못했습니다. --font 로 .ttf 경로를 지정하세요 (예: NanumGothic).")


def wrap(draw, text, font, max_w):
    lines, cur = [], ""
    for ch in text:
        if draw.textlength(cur + ch, font=font) > max_w and cur:
            lines.append(cur)
            cur = ch.lstrip()
        else:
            cur += ch
    if cur:
        lines.append(cur)
    return lines


def gradient(w, h, top, bot):
    img = Image.new("RGB", (w, h))
    px = ImageDraw.Draw(img)
    for y in range(h):
        t = y / (h - 1)
        px.line([(0, y), (w, y)], fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    return img


def background(w, h, scene, theme, root):
    img_path = scene.get("image")
    if img_path:
        p = (root / img_path)
        if p.exists():
            im = Image.open(p).convert("RGB")
            s = max(w / im.width, h / im.height)
            im = im.resize((int(im.width * s), int(im.height * s)))
            l, t = (im.width - w) // 2, (im.height - h) // 2
            im = im.crop((l, t, l + w, t + h)).filter(ImageFilter.GaussianBlur(2))
            return Image.blend(im, Image.new("RGB", (w, h), (0, 0, 0)), 0.55)
    return gradient(w, h, theme[0], theme[1])


def render_frame(w, h, scene, sub, theme, font_path, idx, total, root, hook=None):
    vertical = h > w
    img = background(w, h, scene, theme, root)
    d = ImageDraw.Draw(img)
    u = w / 1080 if vertical else w / 1920  # 해상도 단위
    f_title = ImageFont.truetype(font_path, int((78 if vertical else 76) * u))
    f_body = ImageFont.truetype(font_path, int((54 if vertical else 46) * u))
    f_sub = ImageFont.truetype(font_path, int((58 if vertical else 50) * u))
    f_small = ImageFont.truetype(font_path, int(34 * u))
    pad = int(90 * u)
    accent = theme[2]
    y = int((300 if vertical else 110) * u)

    if hook and vertical:  # 숏폼 상단 후크 문구
        hy = int(150 * u)
        for ln in wrap(d, hook, f_title, w - pad * 2)[:3]:
            d.text((pad, hy), ln, font=f_title, fill=accent)
            hy += int(f_title.size * 1.25)
        y = max(y, hy + int(60 * u))

    d.rectangle([pad, y - int(26 * u), pad + int(140 * u), y - int(18 * u)], fill=accent)
    if scene.get("title"):
        for ln in wrap(d, scene["title"], f_title, w - pad * 2):
            d.text((pad, y), ln, font=f_title, fill="white")
            y += int(f_title.size * 1.3)
        y += int(30 * u)
    for b in scene.get("bullets", [])[:5]:
        lines = wrap(d, b, f_body, w - pad * 2 - int(50 * u))
        d.ellipse([pad, y + int(18 * u), pad + int(18 * u), y + int(36 * u)], fill=accent)
        for ln in lines:
            d.text((pad + int(50 * u), y), ln, font=f_body, fill=(235, 235, 245))
            y += int(f_body.size * 1.35)
        y += int(14 * u)

    if sub:  # 하단 자막
        lines = wrap(d, sub, f_sub, w - pad * 2)
        lh = int(f_sub.size * 1.35)
        by = h - int((380 if vertical else 90) * u) - lh * len(lines)
        box_h = lh * len(lines) + int(36 * u)
        ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(ov).rounded_rectangle(
            [pad // 2, by - int(18 * u), w - pad // 2, by - int(18 * u) + box_h],
            radius=int(24 * u), fill=(0, 0, 0, 165))
        img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
        d = ImageDraw.Draw(img)
        for ln in lines:
            tw = d.textlength(ln, font=f_sub)
            d.text(((w - tw) / 2, by), ln, font=f_sub, fill="white")
            by += lh
    d.rectangle([0, h - int(8 * u), int(w * (idx + 1) / total), h], fill=accent)  # 진행바
    return img


def split_subs(text, max_chars=26):
    parts = [p.strip() for p in re.split(r"(?<=[.!?。])\s+|\n+", text) if p.strip()]
    out = []
    for p in parts:
        while len(p) > max_chars * 1.5:
            cut = p.rfind(" ", 0, max_chars + 6)
            cut = cut if cut > 8 else max_chars
            out.append(p[:cut].strip())
            p = p[cut:].strip()
        out.append(p)
    return out or [text]


def _trust_extra_ca():
    """프록시/회사망 환경: SSL_CERT_FILE 등에 지정된 CA 를 edge-tts 에도 신뢰시키기"""
    import edge_tts.communicate as ec
    for k in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE"):
        path = os.environ.get(k)
        if path and os.path.exists(path):
            try:
                ec._SSL_CTX.load_verify_locations(cafile=path)
            except Exception:
                pass


async def _tts(text, voice, rate, pitch, out):
    import edge_tts
    _trust_extra_ca()
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(str(out))


_warned = set()
CHARS_PER_MIN = 430  # 실측(4편): Google 음성 + 대사 간 여백 기준 분당 410~433자 → 짧게 추정되도록 430
FAST = False  # --fast: 가변 프레임레이트(VFR)로 인코딩 2배 빠름 (미리보기용)


def warn_once(msg):
    if msg not in _warned:
        _warned.add(msg)
        print(msg, file=sys.stderr)


def espeak_audio(text, voice, pitch, out):
    """오프라인 대체 음성(espeak-ng, 로봇 느낌). 성공 시 True"""
    if not shutil.which("espeak-ng"):
        return False
    male = any(k in voice for k in ("InJoon", "Hyunsu", "Male"))
    m = re.match(r"([+-]?\d+)Hz", pitch or "")
    p = max(0, min(99, 50 + (int(m.group(1)) * 2 if m else 0) + (-12 if male else 8)))
    wav = out.with_suffix(".wav")
    try:
        sh(["espeak-ng", "-v", "ko+" + ("m3" if male else "f3"), "-s", "150", "-p", str(p), "-w", str(wav), text])
        sh(["ffmpeg", "-y", "-i", str(wav), "-af", "volume=1.3,highpass=f=80", "-ar", "24000", "-ac", "1",
            "-q:a", "4", str(out)])
        return out.exists() and out.stat().st_size > 1000
    except Exception:
        return False
    finally:
        wav.unlink(missing_ok=True)


def google_audio(text, voice, pitch, out):
    """구글 번역 음성(네트워크 필요, 자연스러운 한국어 1종). 남성/피치는 음높이 변환으로 구분"""
    import urllib.parse, urllib.request
    chunks, cur = [], ""
    for part in re.split(r"(?<=[.!?,])\s+", text):
        if len(cur) + len(part) > 180 and cur:
            chunks.append(cur)
            cur = part
        else:
            cur = (cur + " " + part).strip()
    if cur:
        chunks.append(cur)
    raw = out.with_suffix(".raw.mp3")
    try:
        with open(raw, "wb") as fh:
            for i, c in enumerate(chunks):
                q = urllib.parse.urlencode({"client": "gtx", "ie": "UTF-8", "tl": "ko", "q": c,
                                            "total": len(chunks), "idx": i, "textlen": len(c)})
                req = urllib.request.Request("https://translate.googleapis.com/translate_tts?" + q,
                                             headers={"User-Agent": "Mozilla/5.0"})
                with urllib.request.urlopen(req, timeout=20) as r:
                    fh.write(r.read())
        male = any(k in voice for k in ("InJoon", "Hyunsu", "Male"))
        m = re.match(r"([+-]?\d+)Hz", pitch or "")
        semi = (-4.0 if male else 0.0) + (int(m.group(1)) / 6 if m else 0)
        k = 2 ** (semi / 12)
        af = f"asetrate=24000*{k:.4f},aresample=24000,atempo={1.12 / k:.4f}"  # 음높이만 변경 + 약간 빠르게
        sh(["ffmpeg", "-y", "-i", str(raw), "-af", af, "-ac", "1", "-q:a", "3", str(out)])
        return out.exists() and out.stat().st_size > 1000
    except Exception:
        return False
    finally:
        raw.unlink(missing_ok=True)


GCLOUD_VOICES = {"male": "ko-KR-Neural2-C", "female": "ko-KR-Neural2-A"}


def gcloud_audio(text, voice, rate, pitch, out, gvoice=None):
    """Google Cloud Text-to-Speech (환경변수 GOOGLE_TTS_API_KEY 필요). 성공 시 True"""
    import base64, urllib.request
    key = os.environ.get("GOOGLE_TTS_API_KEY")
    if not key:
        return False
    male = any(k in voice for k in ("InJoon", "Hyunsu", "Male"))
    name = gvoice or GCLOUD_VOICES["male" if male else "female"]
    m = re.match(r"([+-]?\d+)Hz", pitch or "")
    r = re.match(r"([+-]?\d+)%", rate or "")
    body = {"input": {"text": text},
            "voice": {"languageCode": "ko-KR", "name": name},
            "audioConfig": {"audioEncoding": "MP3", "sampleRateHertz": 24000,
                            "speakingRate": round(1 + (int(r.group(1)) / 100 if r else 0), 2),
                            "pitch": max(-20, min(20, int(m.group(1)) / 6 if m else 0))}}
    if "Chirp" in name:  # Chirp3-HD 음성은 pitch 미지원
        body["audioConfig"].pop("pitch")
    req = urllib.request.Request("https://texttospeech.googleapis.com/v1/text:synthesize?key=" + key,
                                 data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            out.write_bytes(base64.b64decode(json.loads(resp.read())["audioContent"]))
        return out.stat().st_size > 1000
    except urllib.error.HTTPError as e:
        warn_once(f"  ! Google Cloud TTS 오류 {e.code}: {e.read()[:200].decode(errors='ignore')}")
    except Exception as e:
        warn_once(f"  ! Google Cloud TTS 실패({type(e).__name__})")
    return False


def make_audio(text, voice, rate, pitch, out, gvoice=None):
    """True=고품질 음성(Google Cloud/edge-tts). False=대체본(구글 번역/espeak-ng/무음, 다음 실행에 재시도)"""
    if gcloud_audio(text, voice, rate, pitch, out, gvoice):
        warn_once("  · 음성: Google Cloud TTS")
        return True
    try:
        asyncio.run(_tts(text, voice, rate, pitch, out))
        if out.exists() and out.stat().st_size > 1000:
            return True
    except Exception as e:  # 네트워크/모듈 문제
        warn_once(f"  ! edge-tts 사용 불가({type(e).__name__}) → 대체 음성 사용")
    if google_audio(text, voice, pitch, out):
        warn_once("  · 대체 음성: 구글 번역 음성")
        return False
    if espeak_audio(text, voice, pitch, out):
        warn_once("  · 대체 음성: espeak-ng (로봇 음성)")
        return False
    warn_once("  ! 사용 가능한 음성 없음 → 무음 (sudo apt install espeak-ng)")
    secs = max(1.6, len(text) / 5.5)
    sh(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", f"{secs:.2f}",
        "-q:a", "9", str(out)])
    return False


def load(path):
    path = Path(path).resolve()
    proj = json.loads(path.read_text(encoding="utf-8"))
    return proj, path.parent


def audio_path(proj, root, who, text):
    """대사 음성 캐시 파일 경로 (화자 목소리·대사로 결정)"""
    c = proj.get("cast", {}).get(who or "", {})
    voice = c.get("voice") or proj.get("voice", "ko-KR-SunHiNeural")
    rate = c.get("rate") or proj.get("rate", "+0%")
    pitch = c.get("pitch", "+0Hz")
    gvoice = c.get("gvoice") or (proj.get("narrator_gvoice") if (who or "narrator") == "narrator" else None)
    work = root / "work"
    work.mkdir(exist_ok=True)
    return work / f"{hashlib.md5(f'{voice}|{gvoice}|{rate}|{pitch}|{text}'.encode()).hexdigest()[:12]}.mp3"


def speak(proj, root, who, text):
    """화자별 목소리로 한 줄 음성 생성(캐시). 반환: (mp3 경로, 길이)"""
    c = proj.get("cast", {}).get(who or "", {})
    voice = c.get("voice") or proj.get("voice", "ko-KR-SunHiNeural")
    rate = c.get("rate") or proj.get("rate", "+0%")
    pitch = c.get("pitch", "+0Hz")
    gvoice = c.get("gvoice") or (proj.get("narrator_gvoice") if (who or "narrator") == "narrator" else None)  # Google Cloud 음성 이름 (예: ko-KR-Chirp3-HD-Aoede)
    mp3 = audio_path(proj, root, who, text)
    flag = mp3.with_suffix(".silent")  # 무음 대체본은 캐시하지 않고 다음 실행에 재시도
    if not mp3.exists() or flag.exists():
        if make_audio(text, voice, rate, pitch, mp3, gvoice):
            flag.unlink(missing_ok=True)
        else:
            flag.touch()
    return str(mp3), dur(mp3)


def scene_lines(sc):
    """장면의 대사 목록. lines 가 없으면 narration 한 줄(해설)로 취급 (쇼츠 표지는 대사 없음)"""
    if sc.get("_cover"):
        return []
    if sc.get("lines"):
        return sc["lines"]
    return [{"who": "narrator", "text": sc["narration"]}]


def is_cartoon(proj, sc):
    return bool(sc.get("lines")) or bool(sc.get("_cover")) or bool(proj.get("cast")) or sc.get("style") == "cartoon"


def cast_color(spec):
    return tuple(int(spec.get("color", cartoon.DEFAULT_LOOK["color"]).lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


_RDR = None


def _init_worker(font_path):
    global _RDR
    _RDR = cartoon.Renderer(font_path)


def _render_job(job):
    png, kw = job
    if "_hook" in kw:  # 숏폼 첫 화면(후크 카드)
        cartoon.render_hook_card(font_path=_RDR.font_path, **kw["_hook"]).save(png, compress_level=1)
    else:
        _RDR.frame(**kw).save(png, compress_level=1)


def prefetch_audio(proj, root, scene_ids):
    """모든 대사 음성을 동시에 미리 생성(캐시에 저장). 이후 speak() 는 캐시만 읽음"""
    todo = []
    for si in scene_ids:
        sc = proj["scenes"][si]
        if is_cartoon(proj, sc):
            todo += [(ln.get("who", "narrator"), ln["text"]) for ln in scene_lines(sc)]
        else:
            todo.append(("narrator", sc["narration"]))
    t0 = time.time()
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(lambda a: speak(proj, root, *a), todo))
    print(f"[음성] {len(todo)}줄 {time.time() - t0:.0f}초")


def pick_shot(sc, li, ln, speaker, vertical=False):
    """카메라: 장면 첫 대사·해설은 전체 샷, 감정이 큰 대사는 말하는 사람 클로즈업, 나머지는 번갈아
    쇼츠(세로)는 인물이 작아 보이지 않게 클로즈업 위주 (홀수 대사만 전체 샷)"""
    if sc.get("shots") == "wide" or sc.get("_hook_card") or not speaker or speaker in sc.get("lying", ()):
        return "wide"
    if ln.get("shot"):
        return ln["shot"]
    if vertical:
        return "wide" if (li % 2 and ln.get("emotion") not in ("sad", "surprised", "angry", "cry", "shock")) else "close"
    if li == 0:
        return "wide"
    if ln.get("emotion") in ("sad", "surprised", "angry", "cry", "shock"):
        return "close"
    return "close" if li % 2 else "wide"


def phrases(text, max_chars=12):
    """쇼츠 자막: 문장을 짧은 구절로 나눔 (공백 기준, 구절당 max_chars 내외)"""
    words, out, cur = text.split(), [], ""
    for wd in words:
        if cur and len(cur) + 1 + len(wd) > max_chars:
            out.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        out.append(cur)
    if len(out) > 1 and len(out[-1]) <= 3:  # 꼬리 한두 글자는 앞 구절에 붙임
        tail = out.pop()  # (out[-2] += out.pop() 은 pop 전에 위치를 잡아 구절이 2개일 때 IndexError)
        out[-1] += " " + tail
    return out or [text]


def silence(root, secs):
    sil = root / "work" / f"sil{int(secs * 1000)}.mp3"
    sil.parent.mkdir(exist_ok=True)
    if not sil.exists():
        sh(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", f"{secs}", "-q:a", "9", str(sil)])
    return str(sil)


def cartoon_segments(proj, sc, root, jobs, size, k, total, hook, chip):
    """만화 장면 → [(png, 초)], [mp3], [(시각, 효과음)]. 입모양/눈깜빡임 상태별 PNG 는 jobs 에 모아 병렬 렌더링
    세로(쇼츠)는 큰 구절 자막이 말에 맞춰 바뀌고, 롱폼은 하단 자막 상자"""
    w, h = size
    vertical = h > w
    wd = root / f"work_{size[0]}x{size[1]}"
    wd.mkdir(exist_ok=True)
    cast = proj.get("cast", {})
    lines = scene_lines(sc)
    ids = sc.get("cast") or []
    if not ids:
        for ln in lines:
            if ln.get("who") in cast and ln["who"] not in ids:
                ids.append(ln["who"])
    chars = [(i, cast[i]) for i in ids if i in cast] or [("_mascot", proj.get("mascot", cartoon.DEFAULT_LOOK))]
    frames, audios, events = [], [], []
    prog = (k + 1) / total

    if sc.get("_cover"):  # 쇼츠 표지: 0.35초 — 첫 프레임은 온전한 표지, 이어서 펀치 줌, 소리는 '쿵'만
        hk = dict(w=w, h=h, spec=sc["_cover"]["spec"], emo=sc["_cover"]["emo"], text=hook or "",
                  prop=sc["_cover"].get("prop"), tone=sc["_cover"].get("tone", "red"),
                  progress=1 / total if sc["_cover"].get("loop") else prog)  # 반복용 끝 표지는 첫 프레임과 똑같이
        if sc["_cover"].get("loop"):  # 쇼츠 끝: 첫 프레임(표지)으로 돌아가 반복 재생이 끊김 없이 이어지게
            png = wd / f"{k:02d}_loop.png"
            jobs.append((str(png), {"_hook": dict(hk, mouth=False, blink=False, zoom=1.0)}))
            return [(png, .45)], [silence(root, .45)], []
        for zi, (z, d_) in enumerate(((1.0, .12), (1.12, .07), (1.07, .07), (1.03, .09))):
            png = wd / f"{k:02d}_cover{zi}.png"
            jobs.append((str(png), {"_hook": dict(hk, mouth=False, blink=False, zoom=z)}))
            frames.append((png, d_))
        return frames, [silence(root, .35)], [(0.0, "thud")]

    t_scene = 0.0
    for li, ln in enumerate(lines):
        who = ln.get("who", "narrator")
        mp3, secs = speak(proj, root, who, ln["text"])
        if ln.get("sfx"):
            events.append((t_scene, ln["sfx"]))
        audios.append(mp3)
        speaker = who if who in dict(chars) else ("_mascot" if who == "narrator" and chars[0][0] == "_mascot" else None)
        emo = ln.get("emotion", "normal")
        listen = {"sad": "sad", "tense": "think"}.get(sc.get("mood"), "normal")  # 슬픈·긴장 장면에서 듣는 사람이 웃고 있지 않게
        emos = {cid: ln.get("react", {}).get(cid, listen) for cid, _ in chars}
        if speaker:
            emos[speaker] = emo
        spec = dict(cast.get(who, {}))
        name = spec.get("name") if who != "narrator" else None
        ncol = cast_color(spec) if spec else (200, 200, 220)
        shot = pick_shot(sc, li, ln, speaker, vertical)
        # 자막 조각: 쇼츠는 구절 단위로 넘어감, 롱폼은 문장 통째
        chunks = phrases(ln["text"]) if vertical else [ln["text"]]
        weights = [max(len(c), 3) for c in chunks]
        rnd = random.Random(li * 31 + k)
        for ci, chunk in enumerate(chunks):
            cdur = secs * weights[ci] / sum(weights)
            states = {}
            for st, (m, bl) in {"o": (True, False), "c": (False, False), "b": (False, True)}.items():
                png = wd / f"{k:02d}_{li:02d}_{ci:02d}_{st}.png"
                jobs.append((str(png), dict(w=w, h=h, bg=sc.get("bg", "plain"), chars=chars, speaker=speaker,
                                            emotions=emos, mouth=m, blink=bl, text=chunk, name=name,
                                            name_color=ncol, chip=chip, hook=hook, progress=prog,
                                            lying=tuple(sc.get("lying", ())), shot=shot,
                                            caption="pop" if vertical else "box",
                                            hook_overlay=bool(ln.get("_hook_overlay")),
                                            end_text=ln.get("_end_text"),
                                            tint="flashback" if sc.get("flashback") else None,
                                            badge=sc.get("when"))))
                states[st] = png
            t, step, pattern = 0.0, 0.16, []
            while t < cdur - 1e-6:
                r = rnd.random()
                st = "b" if (r < .07 and pattern and pattern[-1] == "c") else ("o" if rnd.random() < .62 else "c")
                if not speaker:
                    st = "c" if st == "o" else st
                d_ = min(step, cdur - t)
                pattern.append(st)
                frames.append((states[st], d_))
                t += d_
        gap = 0.06 if vertical else 0.18  # 대사 사이 여백 (쇼츠는 촘촘하게)
        frames.append((states["c"], gap))
        audios.append(silence(root, gap))
        t_scene += secs + gap
    return frames, audios, events


def slide_segments(proj, sc, root, size, k, total, theme, font_path, hook):
    w, h = size
    mp3, secs = speak(proj, root, "narrator", sc["narration"])
    subs = split_subs(sc["narration"])
    weights = [max(len(s), 4) for s in subs]
    frames = []
    for j, s in enumerate(subs):
        png = root / f"work_{w}x{h}" / f"{k:02d}_{j:02d}.png"
        png.parent.mkdir(exist_ok=True)
        render_frame(w, h, sc, s, theme, font_path, k, total, root, hook=hook).save(png)
        frames.append((png, secs * weights[j] / sum(weights)))
    return frames, [mp3], []


def render_video(proj, root, scene_ids, size, out, hook=None, theme_shift=0, font=None, speed=1.0):
    w, h = size
    font_path = find_font(font)
    work = root / f"work_{w}x{h}"
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir()
    prefetch_audio(proj, root, scene_ids)
    jobs = []
    frames, audios = [], []
    sections, events = [], []  # 배경음악 구간(시작, 끝, 분위기), 효과음(시각, 종류) — 원래 속도 기준
    total = len(scene_ids)
    for k, si in enumerate(scene_ids):
        sc = proj["scenes"][si]
        print(f"[장면] {k + 1}/{total} {sc.get('title', '')}")
        chip = None if sc.get("_teaser") else sc.get("title")  # 하이라이트는 오른쪽 위 빨간 표시로 대신
        start = sum(s for _, s in frames)
        if is_cartoon(proj, sc):
            f, a, ev = cartoon_segments(proj, sc, root, jobs, size, k, total, hook, chip)
        else:
            f, a, ev = slide_segments(proj, sc, root, size, k, total, THEMES[(si + theme_shift) % len(THEMES)], font_path, hook)
        frames += f
        audios += a
        end = sum(s for _, s in frames)
        mood = sc.get("mood") or ("tense" if sc.get("_hook_card") else sound.auto_mood(scene_lines(sc) if sc.get("lines") or sc.get("narration") else []))
        sections.append((start, end, mood))
        events += [(start + o, kind) for o, kind in ev]
        if k > 0 and not sc.get("_hook_card") and not sc.get("_cover") and not proj["scenes"][scene_ids[k - 1]].get("_hook_card") \
                and not proj["scenes"][scene_ids[k - 1]].get("_cover"):
            events.append((max(0, start - .25), "whoosh"))
    if jobs:
        t0 = time.time()
        workers = max(1, (os.cpu_count() or 2))
        with ProcessPoolExecutor(workers, initializer=_init_worker, initargs=(font_path,)) as ex:
            list(ex.map(_render_job, jobs, chunksize=4))
        print(f"[프레임] {len(jobs)}장 {time.time() - t0:.0f}초 (병렬 {workers})")
    if speed != 1.0:  # 배속: 화면 길이는 줄이고 음성은 atempo(음높이 유지)로 빠르게
        frames = [(png, secs / speed) for png, secs in frames]
    lst = work / "frames.txt"
    with open(lst, "w") as fh:
        for png, secs in frames:
            fh.write(f"file '{png.name if png.parent == work else png}'\nduration {secs:.3f}\n")
        fh.write(f"file '{frames[-1][0]}'\n")
    alst = work / "audio.txt"
    alst.write_text("".join(f"file '{a}'\n" for a in audios))
    if FAST:
        vflags = ["-vf", "format=yuv420p", "-fps_mode", "vfr"]
    elif proj.get("drift", False):  # 천천히 떠다니는 카메라 (기본 꺼짐 — 켜려면 project.json 에 "drift": true)
        zf = 1.07 if h > w else 1.04
        sw, sh_ = int(w * zf) // 2 * 2, int(h * zf) // 2 * 2
        vflags = ["-vf", f"fps=30,scale={sw}:{sh_},crop={w}:{h}:x='(iw-ow)/2*(1+0.85*sin(t*0.55))':"
                         f"y='(ih-oh)/2*(1+0.85*cos(t*0.41))',format=yuv420p"]
    else:
        vflags = ["-vf", "format=yuv420p,fps=30"]
    venc = ["-c:v", "libx264", "-preset", "veryfast", "-tune", "animation", "-crf", "20" if h > w else "25"]  # 롱폼 9분 ≈ 25~30MB
    print(f"[인코딩] {out.name}")
    if proj.get("music", True):
        dur_final = sum(s for _, s in frames)  # 배속 반영된 최종 길이
        sec_f = [(s / speed, e / speed, m) for s, e, m in sections]
        ev_f = [(a / speed, kd) for a, kd in events]
        music, fx = sound.build(dur_final, sec_f, ev_f, float(proj.get("music_volume", 1.0)))
        sound.write_wav(work / "music.wav", music)
        sound.write_wav(work / "fx.wav", fx)
        tempo = f",atempo={speed}" if speed != 1.0 else ""
        fc = (f"[1:a]aresample=44100{tempo},asplit=2[va][vb];[2:a]aresample=44100[m];"
              "[m][va]sidechaincompress=threshold=0.015:ratio=10:attack=15:release=450[md];"
              "[3:a]aresample=44100[fx];[vb][md][fx]amix=inputs=3:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[aout]")  # 유튜브 기준 음량
        sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
            "-f", "concat", "-safe", "0", "-i", str(alst), "-i", str(work / "music.wav"), "-i", str(work / "fx.wav"),
            "-filter_complex", fc, "-map", "0:v", "-map", "[aout]", *vflags, *venc,
            "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", str(out)])
    else:
        sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
            "-f", "concat", "-safe", "0", "-i", str(alst), *vflags, *venc,
            "-af", (f"atempo={speed}," if speed != 1.0 else "") + "loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100",
            "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out)])
    if not os.environ.get("STUDIO_KEEP_WORK"):
        shutil.rmtree(work, ignore_errors=True)
    total_s = sum(s for _, s in frames)
    print(f"  ✔ {out}  ({total_s / 60:.1f}분)")
    return total_s


def clip_scenes(proj, clips, **extra):
    """[[장면, 시작줄, 끝줄(제외)], ...] → 잘라 낸 장면 dict 목록"""
    out = []
    for clip in clips:
        sc = proj["scenes"][clip[0]]
        a_, b_ = (clip[1] if len(clip) > 1 else 0), (clip[2] if len(clip) > 2 else None)
        out.append(dict(sc, lines=[dict(x) for x in scene_lines(sc)[a_:b_]], **extra))
    return out


def long_plan(proj):
    """롱폼 장면 순서: (하이라이트 미리보기) + 본편. 하이라이트 = project.json 의 teaser 구간을 맨 앞에 붙임"""
    p2 = dict(proj, scenes=list(proj["scenes"]))
    ids = [i for i, sc in enumerate(proj["scenes"]) if not sc.get("shorts_only")]  # 숏폼 전용 장면 제외
    if proj.get("teaser"):
        tz = clip_scenes(proj, proj["teaser"], title="하이라이트", when="▶ 하이라이트", flashback=False, _teaser=True)
        p2["scenes"] += tz
        ids = list(range(len(proj["scenes"]), len(p2["scenes"]))) + ids
    return p2, ids


def cmd_long(proj, root, font):
    out = root / "output"
    out.mkdir(exist_ok=True)
    p2, ids = long_plan(proj)
    secs = render_video(p2, root, ids, (1920, 1080), out / "longform.mp4", font=font)
    if secs < 8 * 60:
        need = int((480 - secs) / 60 * CHARS_PER_MIN) + 1
        print(f"  ! 8분 미만: 미드롤 광고를 위해선 8분 이상 필요 → 대사 약 {need:,}자(≈{need // 25 + 1}줄) 더 추가하세요")


def cmd_shorts(proj, root, font):
    """쇼츠: 0.35초 표지(후크 카드) → 곧바로 이야기의 결정적 대사부터 시작(clips 로 장면 일부만) → 끝 안내는 화면에 겹쳐 표시
    shorts[]: clips=[[장면, 시작줄, 끝줄(제외, 생략 시 끝까지)], ...] 또는 scenes=[장면, ...]
              hook(표지·첫 대사 위 큰 문구), hook_who/hook_emotion/hook_tone/hook_prop(표지), end_text, speed"""
    out = root / "output"
    out.mkdir(exist_ok=True)
    cast = proj.get("cast", {})
    for n, sh_ in enumerate(proj.get("shorts", []), 1):
        p2 = dict(proj, scenes=list(proj["scenes"]))
        clips = sh_.get("clips") or [[i] for i in sh_["scenes"]]
        p2["scenes"] += clip_scenes(proj, clips)
        ids = list(range(len(proj["scenes"]), len(p2["scenes"])))
        first, last = p2["scenes"][ids[0]], p2["scenes"][ids[-1]]
        hook = sh_.get("hook", "")
        if hook:
            first["lines"][0]["_hook_overlay"] = True
        last["lines"][-1]["_end_text"] = sh_.get("end_text", "결말은 본편에서 ▶")
        if sh_.get("cover", True) and is_cartoon(proj, first):
            who = sh_.get("hook_who") or next((x for x in (first.get("cast") or []) if x in cast), None)
            spec = cast.get(who) or cartoon.DEFAULT_LOOK
            cover = {"spec": spec, "emo": sh_.get("hook_emotion", "shock"),
                     "prop": sh_.get("hook_prop"), "tone": sh_.get("hook_tone", "red")}
            p2["scenes"].append({"title": "", "bg": first.get("bg"), "mood": "tense", "lines": [], "_cover": cover})
            ids = [len(p2["scenes"]) - 1] + ids
            if sh_.get("loop", proj.get("shorts_loop", True)):  # 끝에 표지를 다시 붙여 반복 재생이 자연스럽게
                p2["scenes"].append({"title": "", "bg": first.get("bg"), "mood": last.get("mood", "tense"), "lines": [],
                                     "_cover": dict(cover, loop=True)})
                ids.append(len(p2["scenes"]) - 1)
        speed = float(sh_.get("speed", proj.get("shorts_speed", 1.25)))
        secs = render_video(p2, root, ids, (1080, 1920), out / f"short_{n:02d}.mp4",
                            hook=hook, theme_shift=n, font=font, speed=speed)
        print(f"    {speed}배속 · 표지 0.35초 · {len(clips)}개 구간")
        if secs > 40:
            print("  ! 40초 초과: 감동 사연 쇼츠 상위 25% 길이 중앙값은 약 24초(2026-10 조사)입니다. 구간을 줄여 보세요")


def cmd_thumb(proj, root, font):
    """썸네일 A/B/C 3종 (유튜브 '테스트 및 비교'용). thumbnail.png 가 기본(A)"""
    out = root / "output"
    out.mkdir(exist_ok=True)
    font_path = find_font(font)
    t = proj.get("thumbnail", {})
    text = t.get("text") or proj["title"]
    cast = proj.get("cast", {}) or {"_mascot": proj.get("mascot", cartoon.DEFAULT_LOOK)}
    ids = list(cast)
    variants = t.get("variants") or [
        {"palette": "yellow", "chars": [[ids[0], "surprised"]] + ([[ids[1], "happy"]] if len(ids) > 1 else [])},
        {"palette": "blue", "chars": ([[ids[1], "happy"]] if len(ids) > 1 else []) + [[ids[0], "think"]]},
        {"palette": "red", "chars": [[ids[0], "sad"]] + ([[ids[1], "angry"]] if len(ids) > 1 else [])},
    ]
    for i, v in enumerate(variants[:3]):
        if v.get("style") == "story":
            fc, fe = v.get("face", [ids[0], "cry"])
            img = cartoon.render_story_thumbnail(v.get("text", text), (cast[fc], fe), font_path, tone=v.get("tone", "red"),
                                                 highlight=v.get("highlight", t.get("highlight")),
                                                 badge=v.get("badge", t.get("badge")), prop=v.get("prop", t.get("prop")))
            name = "thumbnail.png" if i == 0 else f"thumbnail_{'abc'[i]}.png"
            img.save(out / name)
            print(f"  ✔ {out / name}")
            continue
        chars = [(cast[c], e) for c, e in v["chars"] if c in cast]
        img = cartoon.render_thumbnail(v.get("text", text), chars, font_path, palette=v.get("palette", "yellow"),
                                       highlight=v.get("highlight", t.get("highlight")),
                                       badge=v.get("badge", t.get("badge")))
        name = "thumbnail.png" if i == 0 else f"thumbnail_{'abc'[i]}.png"
        img.save(out / name)
        print(f"  ✔ {out / name}")


def timeline(proj, root):
    """롱폼 장면별 (시작 초, 장면 dict) 목록과 전체 길이 (실제 음성 길이 + 대사 간 여백 기준, 하이라이트 포함)"""
    p2, ids = long_plan(proj)
    t, rows = 0.0, []
    for si in ids:
        sc = p2["scenes"][si]
        rows.append((t, sc))
        if is_cartoon(p2, sc):
            for ln in scene_lines(sc):
                t += speak(p2, root, ln.get("who", "narrator"), ln["text"])[1] + 0.18
        else:
            t += speak(p2, root, "narrator", sc["narration"])[1]
    return rows, t


def mmss(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


def chapters_text(proj, root):
    """롱폼 챕터 타임스탬프. 하이라이트 구간(여러 개)은 0:00 '하이라이트' 하나로 묶음"""
    out = []
    for t, sc in timeline(proj, root)[0]:
        if sc.get("_teaser") and out:
            continue
        out.append(f"{mmss(t)} {sc.get('title', '')}".rstrip())
    return "\n".join(out)


def midroll_points(proj, root):
    """중간광고 수동 위치 추천: 장면 경계 중 약 2분 30초 간격, 2분 이후·끝나기 1분 전까지.
    반전(효과음) 직후보다 직전, 즉 긴장이 걸린 장면 경계를 우선 (광고 뒤에도 계속 보게)"""
    rows, total = timeline(proj, root)
    cands = [(t, sc) for t, sc in rows if 120 <= t <= total - 60 and not sc.get("_teaser")]
    picks, target = [], 150.0
    while cands and target <= total - 60:
        t, sc = min(cands, key=lambda x: abs(x[0] - target) - (8 if any(l.get("sfx") for l in scene_lines(x[1])[:2]) else 0))
        if not picks or t - picks[-1][0] >= 120:
            picks.append((t, sc))
        target = max(target, t) + 150
    return picks


def publish_info(proj, root):
    """업로드 메타데이터 정리: project.json 의 publish(롱폼)·shorts[](숏폼) + 기본값"""
    pub = dict(proj.get("publish", {}))
    pub.setdefault("title", proj["title"])
    desc = pub.get("description", "")
    ch = chapters_text(proj, root)
    pub["description"] = desc.replace("{chapters}", ch) if "{chapters}" in desc else (desc + "\n\n⏱ 챕터\n" + ch).strip()
    pub.setdefault("tags", [])
    pub.setdefault("category", 1)  # 1 영화/애니메이션, 24 엔터테인먼트, 27 교육
    pub.setdefault("made_for_kids", False)
    pub.setdefault("synthetic_media", True)  # 합성 음성 사용
    shorts = []
    for n, s in enumerate(proj.get("shorts", []), 1):
        title = s.get("title") or s.get("hook") or f"{proj['title']} #{n}"
        d = s.get("description") or f"{title}\n전체 영상 👉 「{pub['title']}」\n#Shorts " + " ".join(
            "#" + x.replace(" ", "") for x in pub["tags"][:3])
        shorts.append({"file": f"short_{n:02d}.mp4", "title": title[:100], "description": d,
                       "publish_at": s.get("publish_at", ""), "tags": s.get("tags", pub["tags"][:10])})
    return pub, shorts


def _thumb_b64(path):
    import base64, io
    if not path.exists():
        return None
    buf = io.BytesIO()
    Image.open(path).convert("RGB").save(buf, "JPEG", quality=86)
    return base64.b64encode(buf.getvalue()).decode()


def when_ko(s):
    """ISO 시각 → '10월 9일(금) 18:00'"""
    from datetime import datetime
    try:
        d = datetime.fromisoformat(s)
        return f"{d.month}월 {d.day}일({'월화수목금토일'[d.weekday()]}) {d:%H:%M}"
    except (TypeError, ValueError):
        return s


def cmd_kit(proj, root, font):
    """휴대폰 업로드 키트: 항목별 복사 버튼 + 썸네일 + 업로드 순서가 담긴 output/upload.html"""
    import html as H
    out = root / "output"
    out.mkdir(exist_ok=True)
    pub, shorts = publish_info(proj, root)
    cats = {1: "영화/애니메이션", 22: "인물/블로그", 24: "엔터테인먼트", 27: "교육"}
    (out / "upload.json").write_text(json.dumps({"long": dict(pub, file="longform.mp4"), "shorts": shorts},
                                                ensure_ascii=False, indent=1), encoding="utf-8")

    def field(label, value, rows=1):
        v = H.escape(value)
        box = f'<textarea readonly rows="{rows}">{v}</textarea>' if rows > 1 else f'<input readonly value="{v}">'
        return f'<div class="field"><div class="fl"><span>{H.escape(label)}</span><button type="button" class="cp">복사</button></div>{box}</div>'

    thumbs = ""
    for name in ("thumbnail.png", "thumbnail_b.png", "thumbnail_c.png"):
        b = _thumb_b64(out / name)
        if b:
            thumbs += f'<figure><img alt="{name}" src="data:image/jpeg;base64,{b}"><figcaption>{name}</figcaption></figure>'
    when = when_ko(pub.get("publish_at")) or "직접 선택 (권장: 저녁 6~7시)"
    variants = [v for v in pub.get("title_variants", []) if v != pub["title"]][:2]
    mids = midroll_points(proj, root)
    mid_html = ("<li>중간광고: <b>자동 배치 켜기</b> + 수동 추가 " + ", ".join(f"<b>{mmss(t)}</b>" for t, _ in mids)
                + " (장면이 바뀌는 지점)</li>") if mids else ""
    long_block = (
        f'<section><h2>롱폼 <small>longform.mp4</small></h2>'
        + field("제목 A (기본)", pub["title"])
        + "".join(field(f"제목 {'BC'[i]} (테스트 및 비교용)", v) for i, v in enumerate(variants))
        + field("설명", pub["description"], 10)
        + field("태그 (쉼표 구분)", ", ".join(pub["tags"]), 3)
        + (field("고정 댓글", pub["pinned_comment"], 3) if pub.get("pinned_comment") else "")
        + f'<ul class="set"><li>공개 상태: <b>예약</b> · {H.escape(when)}</li>'
        f'<li>시청자층: <b>아동용 아님</b></li>'
        f'<li>변경되었거나 합성된 콘텐츠: <b>{"예" if pub["synthetic_media"] else "아니요"}</b> (합성 음성 사용)</li>'
        f'<li>카테고리: <b>{cats.get(pub["category"], pub["category"])}</b></li>'
        + (f'<li>재생목록: <b>{H.escape(pub["playlist"])}</b></li>' if pub.get("playlist") else "")
        + mid_html
        + '<li>최종 화면(마지막 20초): <b>지난 영상 1개 + 구독 버튼</b></li>'
        + f'</ul><div class="thumbs">{thumbs}</div>'
        '<p class="hint">썸네일 3장은 길게 눌러 저장한 뒤, YouTube 스튜디오(웹)의 <b>테스트 및 비교</b>에 등록하세요. '
        '제목 B·C도 함께 넣으면 제목×썸네일 조합을 시청 시간 기준으로 비교해 줍니다. 휴대폰 앱에서는 1개만 고를 수 있습니다.</p></section>')
    short_blocks = "".join(
        f'<section><h2>숏폼 {i} <small>{s["file"]}</small></h2>' + field("제목", s["title"])
        + field("설명", s["description"], 4)
        + f'<ul class="set"><li>공개: <b>예약</b> · {H.escape(when_ko(s["publish_at"]) or "롱폼 다음 날부터 하루 1개")}</li><li>시청자층: <b>아동용 아님</b> · 합성 콘텐츠: <b>예</b></li>'
        f'<li><b>관련 동영상</b>: 롱폼을 연결 (쇼츠 → 본편 유입)</li><li>표지: <b>첫 프레임(0초)</b> 그대로</li></ul></section>'
        for i, s in enumerate(shorts, 1))
    page = f"""<title>업로드 키트 · {H.escape(pub['title'][:30])}</title>
<style>
:root{{--bg:#f4f5f7;--card:#fff;--fg:#17191e;--mu:#606674;--ln:#dcdfe5;--ac:#d8402a;--ok:#1f7a63}}
@media (prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#121418;--card:#1b1e24;--fg:#eceef2;--mu:#a2a8b4;--ln:#2c3038;--ac:#ff7a5c;--ok:#5fd1ad;color-scheme:dark}}}}
:root[data-theme=dark]{{--bg:#121418;--card:#1b1e24;--fg:#eceef2;--mu:#a2a8b4;--ln:#2c3038;--ac:#ff7a5c;--ok:#5fd1ad;color-scheme:dark}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.6 -apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;word-break:keep-all}}
.w{{max-width:680px;margin:0 auto;padding-inline:16px;padding-block:20px 60px;display:grid;gap:18px}}
h1{{font-size:21px;margin:0}}h2{{font-size:17px;margin:0 0 10px}}h2 small{{color:var(--mu);font-weight:400;font-size:12px;margin-left:6px}}
section{{background:var(--card);border:1px solid var(--ln);border-radius:12px;padding:14px;display:grid;gap:10px}}
ol{{margin:0;padding-left:20px;display:grid;gap:4px}}.field{{display:grid;gap:4px}}
.fl{{display:flex;justify-content:space-between;align-items:center;font-size:12.5px;color:var(--mu)}}
input,textarea{{width:100%;font:inherit;font-size:14px;color:var(--fg);background:var(--bg);border:1px solid var(--ln);border-radius:8px;padding:8px 10px;resize:vertical}}
button.cp{{font:inherit;font-size:13px;font-weight:600;background:var(--ac);color:#fff;border:0;border-radius:99px;padding:4px 14px;cursor:pointer}}
button.cp.done{{background:var(--ok)}}button:focus-visible{{outline:2px solid var(--fg);outline-offset:2px}}
.set{{margin:0;padding-left:18px;font-size:14px}}.thumbs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:8px}}
figure{{margin:0}}img{{width:100%;border-radius:8px;display:block}}figcaption,.hint{{font-size:12px;color:var(--mu);margin:0}}
</style>
<div class="w">
<h1>업로드 키트</h1>
<section><h2>휴대폰 YouTube 앱으로 올리는 순서</h2><ol>
<li>앱 아래 <b>+</b> → <b>동영상 업로드</b> → 영상 파일 선택</li>
<li><b>세부정보 추가</b>: 아래 제목·설명을 복사해서 붙여넣기</li>
<li><b>공개 상태 → 예약</b>, <b>시청자층 → 아동용 아님</b></li>
<li><b>추가 설정</b>에서 태그 붙여넣기, 변경되었거나 합성된 콘텐츠 <b>예</b></li>
<li>업로드 후 고정 댓글 달기, 썸네일 등록</li></ol></section>
{long_block}{short_blocks}
<p class="hint">project.json 의 publish 정보로 자동 생성 · 챕터는 실제 음성 길이로 계산했습니다.</p>
</div>
<script>
document.querySelectorAll('button.cp').forEach(function(b){{b.addEventListener('click',function(){{
 var el=b.closest('.field').querySelector('input,textarea');
 function ok(){{b.textContent='복사됨';b.classList.add('done');setTimeout(function(){{b.textContent='복사';b.classList.remove('done')}},1500)}}
 function fb(){{el.focus();el.select();try{{document.execCommand('copy');ok()}}catch(e){{b.textContent='길게 눌러 복사'}}}}
 if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(el.value).then(ok,fb)}}else fb();
}})}});
</script>
"""
    (out / "upload.html").write_text(page, encoding="utf-8")
    print(f"  ✔ {out / 'upload.html'}  (+ upload.json)")


BEAT_EMO = ("shock", "surprised", "angry", "cry")


def cmd_lint(proj, root, font=None):
    """대본 점검 (렌더링 전에 실행): 잘 되는 사연 영상들의 공통 요소가 빠졌는지 확인. 음성 없이 글자 수로 길이 추정
    기준 출처: studio/KNOWHOW.md (2026-10 유튜브 사연 상위 영상 분석)"""
    def est(txt, who=None):  # 이미 만든 음성이 있으면 실제 길이, 없으면 글자 수로 추정
        if who is not None:
            p_ = audio_path(proj, root, who, txt)
            if p_.exists() and not p_.with_suffix(".silent").exists():
                return dur(p_) + .18
        return len(txt) * 60 / CHARS_PER_MIN
    probs, oks = [], []
    ck = lambda cond, ok, bad: (oks.append(ok) if cond else probs.append(bad))
    scenes = [(i, sc) for i, sc in enumerate(proj["scenes"]) if not sc.get("shorts_only")]
    lines = [ln for _, sc in scenes for ln in scene_lines(sc)]
    total = sum(est(ln["text"], ln.get("who", "narrator")) for ln in lines)
    tz = clip_scenes(proj, proj.get("teaser", []))
    tz_secs = sum(est(ln["text"], ln.get("who", "narrator")) for sc in tz for ln in scene_lines(sc))
    total_all = total + tz_secs
    # 1) 길이·구조
    ck(total_all >= 8 * 60 + 10, f"길이 약 {mmss(total_all)} (8분 이상: 중간광고 가능)",
       f"길이 약 {mmss(total_all)} — 8분 10초 이상 권장 (8분 미만이면 중간광고 불가, 추정 오차 여유 10초)")
    ck(10 <= tz_secs <= 35, f"0:00 하이라이트 {tz_secs:.0f}초", "0:00 하이라이트 없음/길이 부적절 — teaser 로 절정 대사 15~30초를 맨 앞에 (챕터 '0:00 하이라이트')")
    t, first_beat = 0.0, None
    for _, sc in scenes:
        for ln in scene_lines(sc):
            if first_beat is None and (ln.get("sfx") or ln.get("emotion") in BEAT_EMO):
                first_beat = t
            t += est(ln["text"], ln.get("who", "narrator"))
    ck(tz_secs >= 10 or (first_beat is not None and first_beat <= 20), "첫 20초 안에 충격 장면(하이라이트 또는 본편)",
       "첫 20초 안에 충격·반전(효과음 또는 shock/surprised) 대사가 없음")
    # 2) 리듬: 감정 비트 간격·장면 길이·배경 반복
    t, last, gaps = 0.0, 0.0, []
    for _, sc in scenes[:-1]:  # 마지막 맺음 장면은 잔잔해도 됨
        for ln in scene_lines(sc):
            if ln.get("sfx") or ln.get("emotion") in BEAT_EMO:
                gaps.append((t - last, sc.get("title")))
                last = t
            t += est(ln["text"], ln.get("who", "narrator"))
    gaps.append((t - last, "끝"))
    worst = max(gaps, key=lambda g: g[0])
    ck(worst[0] <= 90, f"감정 비트 최대 간격 {worst[0]:.0f}초", f"{worst[0]:.0f}초 동안 감정 비트 없음('{worst[1]}' 앞) — 60~90초마다 반전·질문·효과음으로 주의 환기")
    long_sc = [(sc.get("title"), sum(est(l["text"], l.get("who", "narrator")) for l in scene_lines(sc))) for _, sc in scenes]
    long_sc = [(n, d) for n, d in long_sc if d > 75]
    ck(not long_sc, "장면 길이 모두 75초 이하", "75초 넘는 장면: " + ", ".join(f"{n}({d:.0f}초)" for n, d in long_sc) + " — 나누거나 배경을 바꾸세요")
    same = [scenes[k][1].get("title") for k in range(1, len(scenes)) if scenes[k][1].get("bg") == scenes[k - 1][1].get("bg")]
    ck(not same, "연속 장면 배경 모두 다름", "앞 장면과 배경이 같음: " + ", ".join(map(str, same)))
    nar = sum(len(l["text"]) for l in lines if l.get("who", "narrator") == "narrator") / max(1, sum(len(l["text"]) for l in lines))
    ck(nar <= .45, f"해설 비중 {nar:.0%}", f"해설 비중 {nar:.0%} — 45% 넘으면 슬라이드쇼처럼 보임(비진정성 정책 위험). 대사로 바꾸세요")
    crowd = [sc.get("title") for _, sc in scenes if len(sc.get("cast") or []) > 4]
    ck(not crowd, "장면당 인물 4명 이하", "인물 5명 이상 장면: " + ", ".join(map(str, crowd)))
    longl = [l["text"] for l in lines if len(l["text"]) > 60]
    ck(not longl, "대사 한 줄 60자 이하", f"60자 넘는 대사 {len(longl)}줄 — 두 줄로 나누면 자막이 읽기 쉬움: " + " / ".join(x[:20] + "…" for x in longl[:3]))
    flash = [sc for _, sc in scenes if sc.get("when") or sc.get("flashback")]
    ck(bool(flash), f"시점 표시 {len(flash)}장면 (when/flashback)", "회상·시간 이동 장면에 when(예: '20년 전') 또는 flashback 표시가 없음")
    # 3) 끝맺음·정책
    end = " ".join(l["text"] for l in scene_lines(scenes[-1][1]))
    ck("?" in end, "마지막에 댓글 유도 질문", "마지막 장면에 시청자에게 던지는 질문(?)이 없음 — 댓글 유도")
    ck(any(k in end for k in ("창작 사연", "실화")), "끝에 창작/실화 표시", "마지막 장면에 '창작 사연' 또는 '실화' 표시가 없음")
    ck(sum(est(l["text"], l.get("who", "narrator")) for l in scene_lines(scenes[-1][1])) >= 20, "마지막 장면 20초 이상(최종 화면 자리)", "마지막 장면이 20초 미만 — 최종 화면(다음 영상·구독) 넣을 시간이 부족")
    # 4) 제목·설명
    pub = proj.get("publish", {})
    title = pub.get("title", proj.get("title", ""))
    ck(20 <= len(title) <= 50, f"제목 {len(title)}자", f"제목 {len(title)}자 — 상위 사연 영상은 28~41자")
    ck(len(pub.get("title_variants", [])) >= 2, "제목 B·C 준비(테스트 및 비교)", "publish.title_variants 에 제목 2개 더 — 하나는 “대사”… 형식 추천")
    desc = pub.get("description", "")
    ck("?" in desc, "설명에 질문", "설명에 '여러분이라면 어떻게 하셨을까요?' 같은 질문이 없음")
    ck("{chapters}" in desc, "설명에 챕터 자리", "설명에 {chapters} 가 없음 (챕터 자동 삽입)")
    # 5) 쇼츠
    speed = float(proj.get("shorts_speed", 1.25))
    for n, sh_ in enumerate(proj.get("shorts", []), 1):
        ls = [l for sc in clip_scenes(proj, sh_.get("clips") or [[i] for i in sh_.get("scenes", [])]) for l in scene_lines(sc)]
        secs = sum(est(l["text"], l.get("who", "narrator")) for l in ls) / speed * .93 + .8
        hook = sh_.get("hook", "")
        hl = hook.split("\n")
        ck(15 <= secs <= 35, f"쇼츠{n} 약 {secs:.0f}초", f"쇼츠{n} 약 {secs:.0f}초 — 15~35초 권장(감동 사연 상위권 중앙값 24초)")
        ck(hook and len(hl) <= 2 and max(len(x) for x in hl) <= 13, f"쇼츠{n} 후크 2줄", f"쇼츠{n} 후크는 2줄·줄당 13자 이하로: {hook!r}")
        ck(bool(ls) and (ls[0].get("emotion") in BEAT_EMO + ("sad",) or ls[0].get("sfx") or "?" in ls[0]["text"]),
           f"쇼츠{n} 첫 대사 감정 강함", f"쇼츠{n} 첫 대사가 밋밋함 — 갈등·충격 대사로 시작하세요")
    print(f"[대본 점검] {proj.get('title', '')}")
    for o in oks:
        print("  ✔", o)
    for b in probs:
        print("  !", b)
    print(f"  → 통과 {len(oks)} · 보완 {len(probs)}")
    return probs


def cmd_check():
    ok = True
    for tool in ("ffmpeg", "ffprobe"):
        p = shutil.which(tool)
        print(("✔" if p else "✘"), tool, p or "(없음)")
        ok &= bool(p)
    try:
        print("✔ 폰트", find_font())
    except SystemExit as e:
        print("✘", e); ok = False
    try:
        import edge_tts  # noqa
        print("✔ edge-tts")
    except ImportError:
        print("! edge-tts 없음 → 대체 음성 사용 (pip install edge-tts)")
    print(("✔" if os.environ.get("GOOGLE_TTS_API_KEY") else "!"), "GOOGLE_TTS_API_KEY (Google Cloud TTS 고품질 음성)")
    print(("✔" if shutil.which("espeak-ng") else "!"), "espeak-ng (오프라인 대체 음성)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["check", "lint", "long", "shorts", "thumb", "kit", "all"])
    ap.add_argument("project", nargs="?")
    ap.add_argument("--font")
    ap.add_argument("--fast", action="store_true", help="미리보기용 빠른 인코딩(가변 프레임레이트)")
    a = ap.parse_args()
    FAST = a.fast
    if a.cmd == "check":
        cmd_check()
    if not a.project:
        sys.exit("project.json 경로가 필요합니다")
    proj, root = load(a.project)
    if a.cmd in ("lint", "all"):
        cmd_lint(proj, root)
    if a.cmd in ("long", "all"):
        cmd_long(proj, root, a.font)
    if a.cmd in ("shorts", "all"):
        cmd_shorts(proj, root, a.font)
    if a.cmd in ("thumb", "all"):
        cmd_thumb(proj, root, a.font)
    if a.cmd in ("kit", "all"):
        cmd_kit(proj, root, a.font)
