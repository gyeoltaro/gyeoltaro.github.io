"""만화 렌더러 - 캐릭터/배경을 코드로 직접 그리는 자막 만화 프레임 생성기 (Pillow)

외부 이미지 없이 동작합니다. 모든 도형을 2배 해상도로 그린 뒤 축소해 선이 매끄럽습니다.
"""
import random
from PIL import Image, ImageDraw, ImageFont

SS = 2                    # 슈퍼샘플링 배율
OUT = (43, 34, 51)        # 외곽선 색
EMOTIONS = ("normal", "happy", "sad", "angry", "surprised", "think")
BG_ALIAS = {"home": "room", "house": "room", "bedroom": "room", "school": "office", "classroom": "office",
            "company": "office", "bar": "cafe", "restaurant": "cafe", "outside": "park", "city": "street",
            "road": "street", "evening": "night"}
DEFAULT_LOOK = {"color": "#ff8a65", "skin": "#ffdcb8", "hair": "short", "hair_color": "#3b2a20"}


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def mix(c, t, k):
    return tuple(int(c[i] + (t[i] - c[i]) * k) for i in range(3))


def grad(d, W, H, y0, y1, c0, c1):
    for y in range(y0, y1):
        d.line([(0, y), (W, y)], fill=mix(c0, c1, (y - y0) / max(1, y1 - y0 - 1)))


# ───────────────────────── 배경 ─────────────────────────
def draw_bg(w, h, kind, horizon):
    kind = BG_ALIAS.get(kind, kind)
    W, H = w * SS, h * SS
    hz = int(H * horizon)
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    lw = max(3, int(min(W, H) * 0.004))
    rnd = random.Random(7)

    def window(x0, y0, x1, y1, sky=(150, 205, 245), frame=(255, 255, 255)):
        d.rectangle([x0, y0, x1, y1], fill=sky, outline=OUT, width=lw)
        d.line([((x0 + x1) // 2, y0), ((x0 + x1) // 2, y1)], fill=frame, width=lw * 2)
        d.line([(x0, (y0 + y1) // 2), (x1, (y0 + y1) // 2)], fill=frame, width=lw * 2)

    if kind == "room":
        grad(d, W, H, 0, hz, (255, 238, 214), (246, 218, 184))
        d.rectangle([0, hz, W, H], fill=(205, 158, 112))
        for i in range(1, 9):
            d.line([(0, hz + (H - hz) * i // 9), (W, hz + (H - hz) * i // 9)], fill=(184, 138, 94), width=lw)
        d.rectangle([0, hz - lw * 3, W, hz], fill=(255, 255, 255))
        window(int(W * .07), int(hz * .18), int(W * .27), int(hz * .66))
        d.rectangle([int(W * .05), int(hz * .12), int(W * .09), int(hz * .72)], fill=(255, 160, 160))
        d.rectangle([int(W * .25), int(hz * .12), int(W * .29), int(hz * .72)], fill=(255, 160, 160))
        d.rectangle([int(W * .72), int(hz * .2), int(W * .9), int(hz * .55)], fill=(255, 255, 255), outline=OUT, width=lw * 2)
        d.ellipse([int(W * .77), int(hz * .27), int(W * .85), int(hz * .48)], fill=(140, 200, 150))
    elif kind == "street":
        grad(d, W, H, 0, hz, (170, 220, 250), (225, 242, 252))
        x = 0
        while x < W:
            bw = rnd.randint(int(W * .07), int(W * .13))
            bh = rnd.randint(int(hz * .35), int(hz * .85))
            col = rnd.choice([(255, 196, 160), (190, 205, 235), (240, 220, 160), (200, 230, 210)])
            d.rectangle([x, hz - bh, x + bw, hz], fill=col, outline=OUT, width=lw)
            for wy in range(hz - bh + int(H * .03), hz - int(H * .03), int(H * .06)):
                for wx in range(x + int(bw * .15), x + bw - int(bw * .2), int(bw * .3)):
                    d.rectangle([wx, wy, wx + int(bw * .15), wy + int(H * .03)], fill=(255, 250, 200))
            x += bw
        d.rectangle([0, hz, W, hz + int((H - hz) * .25)], fill=(220, 220, 225))
        d.rectangle([0, hz + int((H - hz) * .25), W, H], fill=(96, 100, 112))
        for x in range(0, W, int(W * .12)):
            d.rectangle([x, hz + int((H - hz) * .65), x + int(W * .06), hz + int((H - hz) * .7)], fill=(250, 240, 180))
    elif kind == "office":
        grad(d, W, H, 0, hz, (232, 238, 246), (212, 222, 236))
        d.rectangle([0, hz, W, H], fill=(150, 156, 170))
        for i in range(1, 6):
            d.line([(W * i // 6, hz), (W * i // 6 - (W // 12 - W * i // 6 // 6 * 0), H)], fill=(132, 138, 152), width=lw)
        window(int(W * .12), int(hz * .12), int(W * .5), int(hz * .72), sky=(170, 215, 245))
        x = int(W * .13)
        while x < int(W * .49):
            bh = rnd.randint(int(hz * .15), int(hz * .35))
            d.rectangle([x, int(hz * .72) - bh, x + int(W * .03), int(hz * .72)], fill=(120, 150, 190))
            x += int(W * .035)
        d.ellipse([int(W * .72), int(hz * .12), int(W * .82), int(hz * .12) + int(W * .1)], fill=(255, 255, 255), outline=OUT, width=lw * 2)
        cx, cy = int(W * .77), int(hz * .12) + int(W * .05)
        d.line([(cx, cy), (cx, cy - int(W * .035))], fill=OUT, width=lw * 2)
        d.line([(cx, cy), (cx + int(W * .025), cy)], fill=OUT, width=lw * 2)
        d.rectangle([int(W * .86), int(hz * .62), int(W * .91), hz], fill=(176, 120, 80))
        d.ellipse([int(W * .83), int(hz * .3), int(W * .94), int(hz * .66)], fill=(110, 190, 120), outline=OUT, width=lw)
    elif kind == "cafe":
        grad(d, W, H, 0, hz, (196, 148, 104), (170, 122, 84))
        d.rectangle([0, hz, W, H], fill=(124, 86, 58))
        for i in range(1, 8):
            d.line([(0, hz + (H - hz) * i // 8), (W, hz + (H - hz) * i // 8)], fill=(104, 70, 48), width=lw)
        d.rectangle([0, int(hz * .62), W, int(hz * .78)], fill=(96, 64, 44), outline=OUT, width=lw)
        for fx in (.18, .5, .82):
            x = int(W * fx)
            d.line([(x, 0), (x, int(hz * .22))], fill=OUT, width=lw)
            d.pieslice([x - int(W * .04), int(hz * .12), x + int(W * .04), int(hz * .42)], 180, 360, fill=(255, 214, 120), outline=OUT, width=lw)
        d.rectangle([int(W * .66), int(hz * .26), int(W * .9), int(hz * .58)], fill=(48, 56, 56), outline=(220, 200, 160), width=lw * 2)
        for k in range(3):
            d.line([(int(W * .69), int(hz * (.34 + k * .08))), (int(W * (.78 + k * .03)), int(hz * (.34 + k * .08)))], fill=(235, 235, 235), width=lw)
        window(int(W * .08), int(hz * .12), int(W * .3), int(hz * .55), sky=(255, 224, 170))
    elif kind == "park":
        grad(d, W, H, 0, hz, (150, 214, 250), (226, 246, 255))
        d.ellipse([int(W * .78), int(H * .06), int(W * .78) + int(H * .13), int(H * .06) + int(H * .13)], fill=(255, 236, 130), outline=OUT, width=lw)
        d.ellipse([-int(W * .1), int(hz * .78), int(W * .5), hz + int(H * .25)], fill=(140, 208, 120), outline=OUT, width=lw)
        d.ellipse([int(W * .3), int(hz * .85), int(W * 1.1), hz + int(H * .3)], fill=(120, 196, 110), outline=OUT, width=lw)
        d.rectangle([0, hz + int(H * .02), W, H], fill=(112, 188, 100))
        for fx, sc in ((.1, 1), (.88, 1.2), (.64, .8)):
            x = int(W * fx)
            tw = int(W * .02 * sc)
            d.rectangle([x - tw, hz - int(H * .12 * sc), x + tw, hz + int(H * .02)], fill=(146, 98, 64), outline=OUT, width=lw)
            d.ellipse([x - int(W * .07 * sc), hz - int(H * .38 * sc), x + int(W * .07 * sc), hz - int(H * .08 * sc)], fill=(96, 176, 96), outline=OUT, width=lw)
    elif kind == "night":
        grad(d, W, H, 0, hz, (16, 20, 52), (60, 52, 110))
        for _ in range(70):
            x, y, r = rnd.randint(0, W), rnd.randint(0, int(hz * .8)), rnd.randint(2, 5)
            d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 250, 210))
        d.ellipse([int(W * .78), int(H * .08), int(W * .78) + int(H * .14), int(H * .08) + int(H * .14)], fill=(255, 245, 200))
        x = 0
        while x < W:
            bw = rnd.randint(int(W * .06), int(W * .12))
            bh = rnd.randint(int(hz * .3), int(hz * .75))
            d.rectangle([x, hz - bh, x + bw, hz], fill=(26, 28, 62), outline=(10, 10, 30), width=lw)
            for wy in range(hz - bh + int(H * .03), hz - int(H * .03), int(H * .06)):
                for wx in range(x + int(bw * .15), x + bw - int(bw * .2), int(bw * .3)):
                    if rnd.random() < .55:
                        d.rectangle([wx, wy, wx + int(bw * .15), wy + int(H * .03)], fill=(255, 224, 130))
            x += bw
        d.rectangle([0, hz, W, H], fill=(34, 36, 70))
    else:
        grad(d, W, H, 0, hz, (210, 200, 255), (250, 232, 245))
        d.rectangle([0, hz, W, H], fill=(214, 200, 232))
        d.line([(0, hz), (W, hz)], fill=(190, 176, 214), width=lw * 2)
    return im


# ───────────────────────── 캐릭터 ─────────────────────────
def draw_char(d, cx, base, s, spec, emo, mouth, blink, bounce, fnt):
    skin = rgb(spec.get("skin", DEFAULT_LOOK["skin"]))
    shirt = rgb(spec.get("color", DEFAULT_LOOK["color"]))
    hair = rgb(spec.get("hair_color", DEFAULT_LOOK["hair_color"]))
    style = spec.get("hair", "short")
    lw = max(3, int(s * 0.016))
    pants = mix(shirt, (30, 36, 70), .72)

    def ell(x0, y0, x1, y1, fill):
        d.ellipse([x0, y0, x1, y1], fill=fill, outline=OUT, width=lw)

    def thick(p0, p1, wd, fill):
        for col, ww in ((OUT, wd + lw * 2), (fill, wd)):
            d.line([p0, p1], fill=col, width=int(ww))
            for p in (p0, p1):
                d.ellipse([p[0] - ww / 2, p[1] - ww / 2, p[0] + ww / 2, p[1] + ww / 2], fill=col)

    by = base - bounce
    top = by - .42 * s
    hy = top - .24 * s
    # 그림자
    d.ellipse([cx - .26 * s, base - .02 * s, cx + .26 * s, base + .04 * s], fill=(0, 0, 0, 55))
    # 다리
    for sx in (-1, 1):
        d.rounded_rectangle([cx + sx * .075 * s - .05 * s, by - .16 * s, cx + sx * .075 * s + .05 * s, base - .01 * s],
                            radius=int(.03 * s), fill=pants, outline=OUT, width=lw)
        ell(cx + sx * .075 * s - .07 * s, base - .045 * s, cx + sx * .075 * s + .07 * s, base + .02 * s, (250, 250, 250))
    # 긴 머리(뒤)
    if style == "long":
        d.rounded_rectangle([cx - .34 * s, hy - .2 * s, cx + .34 * s, hy + .46 * s], radius=int(.16 * s), fill=hair, outline=OUT, width=lw)
    # 몸
    d.rounded_rectangle([cx - .17 * s, top, cx + .17 * s, by - .08 * s], radius=int(.07 * s), fill=shirt, outline=OUT, width=lw)
    # 팔
    arms = {"happy": ((-.28, -.10), (.28, -.10)), "surprised": ((-.32, -.02), (.32, -.02)),
            "angry": ((-.2, .22), (.2, .22)), "sad": ((-.17, .3), (.17, .3)),
            "think": ((-.24, .26), (.12, -.14)), "normal": ((-.25, .28), (.25, .28))}[emo]
    for sx, (hx, hy_) in zip((-1, 1), arms):
        thick((cx + sx * .15 * s, top + .06 * s), (cx + hx * s, top + .06 * s + (hy_ + .02) * s if hy_ < 0 else top + hy_ * s), .06 * s, shirt)
        px, py = cx + hx * s, (top + .06 * s + (hy_ + .02) * s if hy_ < 0 else top + hy_ * s)
        ell(px - .035 * s, py - .035 * s, px + .035 * s, py + .035 * s, skin)
    # 머리
    ell(cx - .32 * s, hy - .29 * s, cx + .32 * s, hy + .29 * s, skin)
    # 앞머리
    if style in ("short", "long", "bun", "spiky"):
        d.pieslice([cx - .335 * s, hy - .43 * s, cx + .335 * s, hy + .09 * s], 180, 360, fill=hair, outline=OUT, width=lw)
        pts = [(cx - .325 * s, hy - .17 * s), (cx - .2 * s, hy - .085 * s), (cx - .08 * s, hy - .16 * s),
               (cx + .05 * s, hy - .085 * s), (cx + .18 * s, hy - .16 * s), (cx + .325 * s, hy - .17 * s)]
        d.polygon(pts, fill=hair)
        d.line(pts, fill=OUT, width=lw)
    if style == "bun":
        ell(cx - .1 * s, hy - .5 * s, cx + .1 * s, hy - .3 * s, hair)
    if style == "spiky":
        for k in range(-2, 3):
            x = cx + k * .12 * s
            d.polygon([(x - .07 * s, hy - .3 * s), (x, hy - .5 * s), (x + .07 * s, hy - .3 * s)], fill=hair)
            d.line([(x - .07 * s, hy - .3 * s), (x, hy - .5 * s), (x + .07 * s, hy - .3 * s)], fill=OUT, width=lw)
    if spec.get("accessory") == "bow":
        ell(cx + .14 * s, hy - .34 * s, cx + .26 * s, hy - .24 * s, (255, 90, 120))
    # 눈/눈썹
    ey = hy + .04 * s
    for sx in (-1, 1):
        ex = cx + sx * .115 * s
        by_ = ey - .095 * s
        if emo == "sad":
            d.line([(ex - sx * .06 * s, by_ + .02 * s), (ex + sx * .06 * s, by_ - .03 * s)], fill=OUT, width=int(lw * 1.4))
        elif emo == "angry":
            d.line([(ex - sx * .06 * s, by_ - .02 * s), (ex + sx * .06 * s, by_ + .03 * s)], fill=OUT, width=int(lw * 1.6))
        elif emo == "think" and sx == 1:
            d.line([(ex - .06 * s, by_ - .02 * s), (ex + .06 * s, by_ - .06 * s)], fill=OUT, width=int(lw * 1.3))
        else:
            d.line([(ex - .055 * s, by_ + (0 if emo != "happy" else -.02 * s)), (ex + .055 * s, by_ + (0 if emo != "happy" else -.02 * s))], fill=OUT, width=int(lw * 1.2))
        if blink and emo != "happy":
            d.line([(ex - .055 * s, ey), (ex + .055 * s, ey)], fill=OUT, width=int(lw * 1.4))
        elif emo == "happy":
            d.arc([ex - .06 * s, ey - .045 * s, ex + .06 * s, ey + .075 * s], 200, 340, fill=OUT, width=int(lw * 1.6))
        else:
            rx, ry, pr = .06, .072, .034
            if emo == "angry":
                ry = .05
            if emo == "surprised":
                rx, ry, pr = .07, .092, .02
            ell(ex - rx * s, ey - ry * s, ex + rx * s, ey + ry * s, (255, 255, 255))
            ox, oy = 0, 0
            if emo == "sad":
                oy = .02
            if emo == "think":
                ox, oy = .02 * sx + .015, -.03
            px, py = ex + ox * s, ey + oy * s
            d.ellipse([px - pr * s, py - pr * s, px + pr * s, py + pr * s], fill=OUT)
            d.ellipse([px - pr * .4 * s + pr * .3 * s, py - pr * .8 * s, px + pr * .2 * s + pr * .3 * s, py - pr * .2 * s], fill=(255, 255, 255))
        # 볼
        cheek = (255, 150, 165) if emo != "angry" else (255, 110, 110)
        d.ellipse([cx + sx * .21 * s - .05 * s, hy + .13 * s, cx + sx * .21 * s + .05 * s, hy + .19 * s], fill=cheek)
    # 입
    my = hy + .19 * s
    dark = (96, 32, 44)
    tongue = (255, 130, 140)
    if emo == "surprised":
        k = 1 if mouth else .6
        ell(cx - .04 * s * k, my - .04 * s * k, cx + .04 * s * k, my + .06 * s * k, dark)
    elif mouth:
        if emo == "happy":
            d.pieslice([cx - .09 * s, my - .08 * s, cx + .09 * s, my + .1 * s], 0, 180, fill=dark, outline=OUT, width=lw)
            d.ellipse([cx - .045 * s, my + .03 * s, cx + .045 * s, my + .085 * s], fill=tongue)
        elif emo == "angry":
            d.rounded_rectangle([cx - .065 * s, my - .02 * s, cx + .065 * s, my + .05 * s], radius=int(.02 * s), fill=dark, outline=OUT, width=lw)
        else:
            ell(cx - .05 * s, my - .03 * s, cx + .05 * s, my + .05 * s, dark)
            d.ellipse([cx - .03 * s, my + .015 * s, cx + .03 * s, my + .048 * s], fill=tongue)
    else:
        if emo == "happy":
            d.arc([cx - .08 * s, my - .08 * s, cx + .08 * s, my + .04 * s], 15, 165, fill=OUT, width=int(lw * 1.4))
        elif emo == "sad":
            d.arc([cx - .05 * s, my, cx + .05 * s, my + .08 * s], 200, 340, fill=OUT, width=int(lw * 1.4))
        elif emo == "angry" or emo == "think":
            d.line([(cx - .045 * s, my + .02 * s), (cx + .045 * s, my + .02 * s)], fill=OUT, width=int(lw * 1.4))
        else:
            d.arc([cx - .05 * s, my - .05 * s, cx + .05 * s, my + .04 * s], 20, 160, fill=OUT, width=int(lw * 1.4))
    # 안경
    if spec.get("accessory") == "glasses":
        for sx in (-1, 1):
            ex = cx + sx * .115 * s
            d.ellipse([ex - .085 * s, ey - .09 * s, ex + .085 * s, ey + .09 * s], outline=OUT, width=int(lw * 1.2))
        d.line([(cx - .03 * s, ey - .01 * s), (cx + .03 * s, ey - .01 * s)], fill=OUT, width=int(lw * 1.2))
    # 감정 이펙트
    ex_, ey_ = cx + .27 * s, hy - .32 * s
    if emo == "surprised":
        d.rounded_rectangle([ex_ - .02 * s, ey_ - .14 * s, ex_ + .02 * s, ey_ - .03 * s], radius=int(.02 * s), fill=(255, 70, 70))
        d.ellipse([ex_ - .022 * s, ey_, ex_ + .022 * s, ey_ + .044 * s], fill=(255, 70, 70))
    elif emo == "think":
        f = fnt(int(.26 * s))
        d.text((ex_ - .05 * s, ey_ - .22 * s), "?", font=f, fill=(255, 255, 255), stroke_width=lw, stroke_fill=OUT)
    elif emo == "angry":
        for dx, dy in ((-1, -1), (1, 1)):
            d.line([(ex_ - .05 * s * dx, ey_ - .02 * s * dy), (ex_ + .05 * s * dx, ey_ + .02 * s * dy)], fill=(255, 60, 60), width=int(lw * 1.6))
            d.line([(ex_ - .02 * s * dy, ey_ + .05 * s * dx), (ex_ + .02 * s * dy, ey_ - .05 * s * dx)], fill=(255, 60, 60), width=int(lw * 1.6))
    elif emo == "sad":
        x, y = cx - .2 * s, hy + .12 * s
        d.polygon([(x, y - .05 * s), (x - .035 * s, y + .02 * s), (x, y + .06 * s), (x + .035 * s, y + .02 * s)], fill=(120, 190, 255), outline=OUT)
    elif emo == "happy":
        for x, y, r in ((cx - .3 * s, hy - .3 * s, .06), (cx + .32 * s, hy - .1 * s, .045)):
            d.polygon([(x, y - r * s), (x + r * .3 * s, y - r * .3 * s), (x + r * s, y), (x + r * .3 * s, y + r * .3 * s),
                       (x, y + r * s), (x - r * .3 * s, y + r * .3 * s), (x - r * s, y), (x - r * .3 * s, y - r * .3 * s)],
                      fill=(255, 224, 80), outline=OUT)


# ───────────────────────── 프레임 합성 ─────────────────────────
def wrap(d, text, font, max_w):
    """공백 위치를 우선해 줄바꿈 (한 글자만 남는 줄 방지)"""
    lines, cur = [], ""
    for ch in text:
        cur += ch
        if d.textlength(cur, font=font) > max_w:
            cut = cur.rfind(" ")
            if cut > len(cur) * .4:
                lines.append(cur[:cut])
                cur = cur[cut + 1:]
            else:
                lines.append(cur[:-1])
                cur = ch
    if cur.strip():
        lines.append(cur)
    return lines


class Renderer:
    def __init__(self, font_path):
        self.font_path = font_path
        self._bg = {}
        self._fonts = {}

    def font(self, size):
        size = max(8, int(size))
        if size not in self._fonts:
            self._fonts[size] = ImageFont.truetype(self.font_path, size)
        return self._fonts[size]

    def bg(self, w, h, kind, horizon):
        key = (w, h, kind, horizon)
        if key not in self._bg:
            self._bg[key] = draw_bg(w, h, kind, horizon)
        return self._bg[key]

    def frame(self, w, h, *, bg, chars, speaker, emotions, mouth, blink, text, name, name_color,
              chip=None, hook=None, progress=0.0, accent=(255, 213, 79)):
        """chars: [(id, spec)] / emotions: {id: emo}"""
        vertical = h > w
        horizon = .54 if vertical else .70
        n = max(1, len(chars))
        if vertical:
            s = min(w * .86 / n, h * .34)
            base = h * .60
        else:
            s = min(h * .66, w * .9 / n)
            base = h * .86
        layer = self.bg(w, h, bg, horizon).copy().convert("RGBA")
        ch = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        d = ImageDraw.Draw(ch)
        for i, (cid, spec) in enumerate(chars):
            cx = w * (i + 1) / (n + 1) * SS
            talking = cid == speaker
            bounce = (.025 * s * SS) if talking and mouth else 0
            draw_char(d, cx, base * SS, s * SS, spec, emotions.get(cid, "normal"),
                      talking and mouth, blink, bounce, lambda z: self.font(z))
        layer = Image.alpha_composite(layer, ch).reduce(SS).convert("RGB")  # 2배→1배 박스 축소(빠름)
        d = ImageDraw.Draw(layer)

        u = w / 1080 if vertical else w / 1920
        pad = int(70 * u)
        if chip and not vertical:
            f = self.font(40 * u)
            tw = d.textlength(chip, font=f)
            d.rounded_rectangle([pad, int(46 * u), pad + tw + int(50 * u), int(46 * u) + int(66 * u)], radius=int(33 * u), fill=(20, 20, 40))
            d.text((pad + int(25 * u), int(46 * u) + int(10 * u)), chip, font=f, fill=accent)
        if hook and vertical:
            f = self.font(68 * u)
            y = int(130 * u)
            hl = wrap(d, hook, f, w - pad * 2)
            if len(hl) == 2 and " " in hook:  # 두 줄이면 가운데 가까운 공백에서 균형 있게 나눔
                sp = [i for i, ch in enumerate(hook) if ch == " "]
                cut = min(sp, key=lambda i: abs(i - len(hook) / 2))
                hl = [hook[:cut], hook[cut + 1:]]
            for ln in hl[:3]:
                tw = d.textlength(ln, font=f)
                d.text(((w - tw) / 2, y), ln, font=f, fill=accent, stroke_width=int(7 * u), stroke_fill=OUT)
                y += int(f.size * 1.25)
        if text:
            f = self.font((56 if vertical else 50) * u)
            lines = wrap(d, text, f, w - pad * 2 - int(40 * u))
            lh = int(f.size * 1.36)
            box_h = lh * len(lines) + int(34 * u)
            bottom = h * .90 if vertical else h - int(40 * u)
            bottom = int(bottom) - (int(240 * u) if vertical else 0)
            top = bottom - box_h
            ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
            od = ImageDraw.Draw(ov)
            od.rounded_rectangle([pad // 2, top, w - pad // 2, bottom], radius=int(26 * u), fill=(10, 10, 24, 205))
            layer = Image.alpha_composite(layer.convert("RGBA"), ov).convert("RGB")
            d = ImageDraw.Draw(layer)
            ty = top + int(17 * u)
            for ln in lines:
                tw = d.textlength(ln, font=f)
                d.text(((w - tw) / 2, ty), ln, font=f, fill="white", stroke_width=max(1, int(2 * u)), stroke_fill=(0, 0, 0))
                ty += lh
            if name:
                nf = self.font(36 * u)
                nw = d.textlength(name, font=nf) + int(44 * u)
                d.rounded_rectangle([pad // 2 + int(20 * u), top - int(30 * u), pad // 2 + int(20 * u) + nw, top + int(22 * u)],
                                    radius=int(26 * u), fill=name_color, outline=OUT, width=max(2, int(3 * u)))
                lum = .3 * name_color[0] + .59 * name_color[1] + .11 * name_color[2]
                d.text((pad // 2 + int(42 * u), top - int(27 * u)), name, font=nf, fill=(20, 20, 30) if lum > 150 else "white")
        d.rectangle([0, h - int(8 * u), int(w * progress), h], fill=accent)
        return layer
