#!/usr/bin/env python3
"""YouTube 자동화 스튜디오 - 영상 제작 엔진 (Claude Code가 직접 실행)

사용법:
  python3 studio/tools/studio.py check
  python3 studio/tools/studio.py long   studio/projects/<slug>/project.json
  python3 studio/tools/studio.py shorts studio/projects/<slug>/project.json
  python3 studio/tools/studio.py thumb  studio/projects/<slug>/project.json
  python3 studio/tools/studio.py all    studio/projects/<slug>/project.json

필요: ffmpeg, Pillow, edge-tts (pip install pillow edge-tts)
TTS(edge-tts)가 안 되면 무음 + 자막 영상으로 대체되며 경고를 출력합니다.
"""
import argparse, asyncio, json, os, re, shutil, subprocess, sys
from pathlib import Path

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


async def _tts(text, voice, rate, out):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate=rate).save(str(out))


def make_audio(text, voice, rate, out):
    """TTS 성공 시 mp3, 실패 시 글자수 기반 길이의 무음 mp3"""
    try:
        asyncio.run(_tts(text, voice, rate, out))
        if out.exists() and out.stat().st_size > 1000:
            return True
    except Exception as e:  # 네트워크/모듈 문제
        print(f"  ! TTS 실패({type(e).__name__}) → 무음 대체", file=sys.stderr)
    secs = max(2.0, len(text) / 5.5)
    sh(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", f"{secs:.2f}",
        "-q:a", "9", str(out)])
    return False


def load(path):
    path = Path(path).resolve()
    proj = json.loads(path.read_text(encoding="utf-8"))
    return proj, path.parent


def build_audio(proj, root):
    work = root / "work"
    work.mkdir(exist_ok=True)
    voice = proj.get("voice", "ko-KR-SunHiNeural")
    rate = proj.get("rate", "+0%")
    timeline = []
    for i, sc in enumerate(proj["scenes"]):
        mp3 = work / f"scene_{i:02d}.mp3"
        flag = mp3.with_suffix(".silent")  # 무음 대체본은 캐시하지 않고 다음 실행에 재시도
        if not mp3.exists() or flag.exists():
            print(f"[음성] 장면 {i + 1}/{len(proj['scenes'])}")
            if make_audio(sc["narration"], voice, rate, mp3):
                flag.unlink(missing_ok=True)
            else:
                flag.touch()
        timeline.append({"scene": i, "audio": str(mp3), "dur": dur(mp3)})
    return timeline


def render_video(proj, root, scene_ids, size, out, hook=None, theme_shift=0, font=None):
    w, h = size
    font_path = find_font(font)
    work = root / ("work_" + out.stem)
    shutil.rmtree(work, ignore_errors=True)
    work.mkdir()
    timeline = build_audio(proj, root)
    frames, audios = [], []  # frames: (png, seconds)
    total = len(scene_ids)
    for k, si in enumerate(scene_ids):
        sc, tl = proj["scenes"][si], timeline[si]
        theme = THEMES[(si + theme_shift) % len(THEMES)]
        subs = split_subs(sc["narration"])
        weights = [max(len(s), 4) for s in subs]
        for j, s in enumerate(subs):
            png = work / f"f_{k:02d}_{j:02d}.png"
            render_frame(w, h, sc, s, theme, font_path, k, total, root,
                         hook=hook if k == 0 or hook else None).save(png)
            frames.append((png, tl["dur"] * weights[j] / sum(weights)))
        audios.append(tl["audio"])
    lst = work / "frames.txt"
    with open(lst, "w") as f:
        for png, secs in frames:
            f.write(f"file '{png.name}'\nduration {secs:.3f}\n")
        f.write(f"file '{frames[-1][0].name}'\n")
    alst = work / "audio.txt"
    alst.write_text("".join(f"file '{a}'\n" for a in audios))
    print(f"[인코딩] {out.name}")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst),
        "-f", "concat", "-safe", "0", "-i", str(alst),
        "-vf", f"fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
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
        print("! edge-tts 없음 → 무음 영상으로 대체 (pip install edge-tts)")
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
