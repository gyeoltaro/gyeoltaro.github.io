#!/usr/bin/env python3
"""YouTube 자동화 스튜디오 - 영상 제작 엔진 (Claude Code가 직접 실행)

사용법:
  python3 studio/tools/studio.py check
  python3 studio/tools/studio.py long   studio/projects/<slug>/project.json
  python3 studio/tools/studio.py shorts studio/projects/<slug>/project.json
  python3 studio/tools/studio.py thumb  studio/projects/<slug>/project.json
  python3 studio/tools/studio.py all    studio/projects/<slug>/project.json

필요: ffmpeg, Pillow, edge-tts (pip install pillow edge-tts)
음성: edge-tts → 구글 번역 음성 → espeak-ng(오프라인) → 무음 순으로 대체됩니다.
"""
import argparse, asyncio, hashlib, json, os, random, re, shutil, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cartoon  # noqa: E402

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


async def _tts(text, voice, rate, pitch, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(str(out))


_warned = set()


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


def make_audio(text, voice, rate, pitch, out):
    """True=edge-tts 고품질 음성. False=대체본(구글/espeak-ng/무음, 다음 실행에 edge-tts 재시도)"""
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


def speak(proj, root, who, text):
    """화자별 목소리로 한 줄 음성 생성(캐시). 반환: (mp3 경로, 길이)"""
    c = proj.get("cast", {}).get(who or "", {})
    voice = c.get("voice") or proj.get("voice", "ko-KR-SunHiNeural")
    rate = c.get("rate") or proj.get("rate", "+0%")
    pitch = c.get("pitch", "+0Hz")
    work = root / "work"
    work.mkdir(exist_ok=True)
    key = hashlib.md5(f"{voice}|{rate}|{pitch}|{text}".encode()).hexdigest()[:12]
    mp3 = work / f"{key}.mp3"
    flag = mp3.with_suffix(".silent")  # 무음 대체본은 캐시하지 않고 다음 실행에 재시도
    if not mp3.exists() or flag.exists():
        if make_audio(text, voice, rate, pitch, mp3):
            flag.unlink(missing_ok=True)
        else:
            flag.touch()
    return str(mp3), dur(mp3)


def scene_lines(sc):
    """장면의 대사 목록. lines 가 없으면 narration 한 줄(해설)로 취급"""
    if sc.get("lines"):
        return sc["lines"]
    return [{"who": "narrator", "text": sc["narration"]}]


def is_cartoon(proj, sc):
    return bool(sc.get("lines")) or bool(proj.get("cast")) or sc.get("style") == "cartoon"


def cast_color(spec):
    return tuple(int(spec.get("color", cartoon.DEFAULT_LOOK["color"]).lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))


def cartoon_segments(proj, sc, root, rdr, size, k, total, hook, chip):
    """만화 장면 → [(png, 초)], [mp3]. 입모양/눈깜빡임 상태별 PNG 를 재사용"""
    w, h = size
    cast = proj.get("cast", {})
    lines = scene_lines(sc)
    ids = sc.get("cast") or []
    if not ids:
        for ln in lines:
            if ln.get("who") in cast and ln["who"] not in ids:
                ids.append(ln["who"])
    chars = [(i, cast[i]) for i in ids if i in cast] or [("_mascot", proj.get("mascot", cartoon.DEFAULT_LOOK))]
    frames, audios = [], []
    sil = None
    for li, ln in enumerate(lines):
        who = ln.get("who", "narrator")
        mp3, secs = speak(proj, root, who, ln["text"])
        audios.append(mp3)
        speaker = who if who in dict(chars) else ("_mascot" if who == "narrator" and chars[0][0] == "_mascot" else None)
        emo = ln.get("emotion", "normal")
        emos = {cid: ln.get("react", {}).get(cid, "normal") for cid, _ in chars}
        if speaker:
            emos[speaker] = emo
        spec = dict(cast.get(who, {}))
        name = spec.get("name") if who != "narrator" else None
        ncol = cast_color(spec) if spec else (200, 200, 220)
        prog = (k + 1) / total
        states = {}
        for st, (m, bl) in {"o": (True, False), "c": (False, False), "b": (False, True)}.items():
            png = root / f"work_{size[0]}x{size[1]}" / f"{k:02d}_{li:02d}_{st}.png"
            png.parent.mkdir(exist_ok=True)
            rdr.frame(w, h, bg=sc.get("bg", "plain"), chars=chars, speaker=speaker, emotions=emos,
                      mouth=m, blink=bl, text=ln["text"], name=name, name_color=ncol,
                      chip=chip, hook=hook, progress=prog).save(png)
            states[st] = png
        rnd = random.Random(li * 31 + k)
        t, step, pattern = 0.0, 0.16, []
        while t < secs:
            r = rnd.random()
            st = "b" if (r < .07 and pattern and pattern[-1] == "c") else ("o" if rnd.random() < .62 else "c")
            if not speaker:
                st = "c" if st == "o" else st
            d_ = min(step, secs - t)
            pattern.append(st)
            frames.append((states[st], d_))
            t += d_
        gap = 0.18  # 대사 사이 여백
        sil = sil or root / "work" / "gap.mp3"
        if not sil.exists():
            sh(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", f"{gap}", "-q:a", "9", str(sil)])
        frames.append((states["c"], gap))
        audios.append(str(sil))
    return frames, audios


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
    return frames, [mp3]


def render_video(proj, root, scene_ids, size, out, hook=None, theme_shift=0, font=None):
    w, h = size
    font_path = find_font(font)
    work = root / f"work_{w}x{h}"
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir()
    rdr = cartoon.Renderer(font_path)
    frames, audios = [], []
    total = len(scene_ids)
    for k, si in enumerate(scene_ids):
        sc = proj["scenes"][si]
        print(f"[장면] {k + 1}/{total} {sc.get('title', '')}")
        chip = sc.get("title")
        if is_cartoon(proj, sc):
            f, a = cartoon_segments(proj, sc, root, rdr, size, k, total, hook if k == 0 else hook, chip)
        else:
            f, a = slide_segments(proj, sc, root, size, k, total, THEMES[(si + theme_shift) % len(THEMES)], font_path, hook)
        frames += f
        audios += a
    lst = work / "frames.txt"
    with open(lst, "w") as fh:
        for png, secs in frames:
            fh.write(f"file '{png.name if png.parent == work else png}'\nduration {secs:.3f}\n")
        fh.write(f"file '{frames[-1][0]}'\n")
    alst = work / "audio.txt"
    alst.write_text("".join(f"file '{a}'\n" for a in audios))
    print(f"[인코딩] {out.name}")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
        "-f", "concat", "-safe", "0", "-i", str(alst),
        "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(out)])
    shutil.rmtree(work, ignore_errors=True)
    total_s = sum(s for _, s in frames)
    print(f"  ✔ {out}  ({total_s / 60:.1f}분)")
    return total_s


def cmd_long(proj, root, font):
    out = root / "output"
    out.mkdir(exist_ok=True)
    ids = list(range(len(proj["scenes"])))
    secs = render_video(proj, root, ids, (1920, 1080), out / "longform.mp4", font=font)
    if secs < 8 * 60:
        print("  ! 8분 미만: 미드롤 광고를 위해선 8분 이상 권장 (장면/대본 확장 필요)")


def cmd_shorts(proj, root, font):
    out = root / "output"
    out.mkdir(exist_ok=True)
    for n, sh_ in enumerate(proj.get("shorts", []), 1):
        secs = render_video(proj, root, sh_["scenes"], (1080, 1920), out / f"short_{n:02d}.mp4",
                            hook=sh_.get("hook", ""), theme_shift=n, font=font)
        if secs > 180:
            print("  ! 쇼츠는 3분 이내여야 합니다 (60초 이내 권장)")


def cmd_thumb(proj, root, font):
    out = root / "output"
    out.mkdir(exist_ok=True)
    font_path = find_font(font)
    t = proj.get("thumbnail", {})
    text = t.get("text") or proj["title"]
    w, h = 1280, 720
    img = gradient(w, h, (20, 20, 60), (120, 30, 90))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(font_path, 130)
    y = 130
    for ln in wrap(d, text, f, w - 140)[:3]:
        for dx, dy in [(-4, -4), (4, 4), (-4, 4), (4, -4)]:
            d.text((70 + dx, y + dy), ln, font=f, fill="black")
        d.text((70, y), ln, font=f, fill=(255, 224, 70) if y == 130 else "white")
        y += 165
    img.save(out / "thumbnail.png")
    print(f"  ✔ {out / 'thumbnail.png'}")


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
    print(("✔" if shutil.which("espeak-ng") else "!"), "espeak-ng (오프라인 대체 음성)")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["check", "long", "shorts", "thumb", "all"])
    ap.add_argument("project", nargs="?")
    ap.add_argument("--font")
    a = ap.parse_args()
    if a.cmd == "check":
        cmd_check()
    if not a.project:
        sys.exit("project.json 경로가 필요합니다")
    proj, root = load(a.project)
    if a.cmd in ("long", "all"):
        cmd_long(proj, root, a.font)
    if a.cmd in ("shorts", "all"):
        cmd_shorts(proj, root, a.font)
    if a.cmd in ("thumb", "all"):
        cmd_thumb(proj, root, a.font)
