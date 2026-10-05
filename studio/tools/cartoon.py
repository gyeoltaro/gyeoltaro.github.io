"""만화 렌더러 - 캐릭터/배경을 코드로 직접 그리는 자막 만화 프레임 생성기 (Pillow)

외부 이미지 없이 동작합니다. 모든 도형을 2배 해상도로 그린 뒤 축소해 선이 매끄럽습니다.
"""
import math
import random
from PIL import Image, ImageDraw, ImageFont

SS = 2                    # 슈퍼샘플링 배율
OUT = (43, 34, 51)        # 외곽선 색
EMOTIONS = ("normal", "happy", "sad", "angry", "surprised", "think", "cry", "shock")
BG_ALIAS = {"livingroom": "living", "night_room": "room_night", "bedroom_night": "room_night", "funeral": "memorial", "hospital_room": "hospital", "bank": "office", "home": "room", "house": "room", "bedroom": "room", "school": "office", "classroom": "office",
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
    elif kind in ("living", "room_night"):
        night = kind == "room_night"
        grad(d, W, H, 0, hz, (70, 74, 110) if night else (236, 228, 214), (52, 54, 88) if night else (222, 210, 192))
        d.rectangle([0, hz, W, H], fill=(96, 78, 70) if night else (184, 146, 108))
        for i in range(1, 8):
            d.line([(0, hz + (H - hz) * i // 8), (W, hz + (H - hz) * i // 8)], fill=(84, 68, 60) if night else (166, 130, 96), width=lw)
        window(int(W * .06), int(hz * .14), int(W * .24), int(hz * .6), sky=(30, 36, 80) if night else (160, 210, 245))
        if night:
            d.ellipse([int(W * .17), int(hz * .2), int(W * .21), int(hz * .2) + int(W * .04)], fill=(255, 245, 200))
            d.polygon([(int(W * .84), int(hz * .32)), (int(W * .92), int(hz * .32)), (int(W * .9), int(hz * .18)), (int(W * .86), int(hz * .18))], fill=(255, 220, 140), outline=OUT)  # 스탠드
            d.line([(int(W * .88), int(hz * .32)), (int(W * .88), hz)], fill=OUT, width=lw * 2)
            d.pieslice([int(W * .76), int(hz * .1), int(W * 1.0), int(hz * .9)], 60, 120, fill=(255, 230, 160))
        else:
            d.rounded_rectangle([int(W * .64), int(hz * .48), int(W * .97), int(hz * .86)], radius=int(W * .02), fill=(120, 140, 170), outline=OUT, width=lw)  # 소파
            d.rounded_rectangle([int(W * .66), int(hz * .32), int(W * .95), int(hz * .58)], radius=int(W * .02), fill=(132, 152, 182), outline=OUT, width=lw)
            d.rectangle([int(W * .32), int(hz * .2), int(W * .52), int(hz * .5)], fill=(30, 32, 40), outline=OUT, width=lw * 2)  # TV
            d.rectangle([int(W * .3), int(hz * .5), int(W * .54), int(hz * .58)], fill=(150, 110, 80), outline=OUT, width=lw)
        d.ellipse([int(W * .25), hz + int((H - hz) * .2), int(W * .75), hz + int((H - hz) * .7)], fill=(150, 90, 90) if night else (200, 120, 110))  # 러그
    elif kind == "kitchen":
        grad(d, W, H, 0, hz, (244, 240, 230), (230, 224, 210))
        for x in range(0, W, int(W * .03)):  # 타일
            d.line([(x, int(hz * .45)), (x, int(hz * .72))], fill=(214, 206, 192), width=lw)
        for y in range(int(hz * .45), int(hz * .72), int(W * .03)):
            d.line([(0, y), (W, y)], fill=(214, 206, 192), width=lw)
        d.rectangle([0, int(hz * .06), W, int(hz * .4)], fill=(170, 196, 170), outline=OUT, width=lw)  # 상부장
        for x in range(int(W * .1), W, int(W * .18)):
            d.line([(x, int(hz * .06)), (x, int(hz * .4))], fill=OUT, width=lw)
        d.rectangle([0, int(hz * .72), W, hz], fill=(150, 176, 150), outline=OUT, width=lw)  # 하부장·조리대
        d.rectangle([0, int(hz * .7), W, int(hz * .76)], fill=(236, 236, 236), outline=OUT, width=lw)
        d.rectangle([int(W * .86), int(hz * .1), int(W * .98), hz], fill=(225, 230, 235), outline=OUT, width=lw * 2)  # 냉장고
        d.line([(int(W * .86), int(hz * .45)), (int(W * .98), int(hz * .45))], fill=OUT, width=lw)
        d.rectangle([0, hz, W, H], fill=(206, 196, 180))
        for i in range(1, 6):
            d.line([(W * i // 6, hz), (W * i // 6, H)], fill=(190, 180, 164), width=lw)
    elif kind == "hospital":
        grad(d, W, H, 0, hz, (232, 246, 244), (214, 236, 234))
        d.rectangle([0, hz, W, H], fill=(196, 214, 218))
        for i in range(1, 7):
            d.line([(W * i // 7, hz), (W * i // 7, H)], fill=(182, 200, 204), width=lw)
        window(int(W * .06), int(hz * .14), int(W * .26), int(hz * .6), sky=(190, 225, 250))
        d.rectangle([int(W * .60), int(hz * .80), int(W * .98), int(hz * 1.04)], fill=(255, 255, 255), outline=OUT, width=lw)  # 침대
        d.rectangle([int(W * .58), int(hz * .58), int(W * .61), int(hz * 1.04)], fill=(170, 180, 190), outline=OUT, width=lw)
        d.line([(int(W * .55), int(hz * .12)), (int(W * .55), hz)], fill=(150, 160, 170), width=lw * 2)  # 링거대
        d.rounded_rectangle([int(W * .525), int(hz * .14), int(W * .575), int(hz * .3)], radius=lw * 3, fill=(220, 240, 255), outline=OUT, width=lw)
        d.rounded_rectangle([int(W * .4), int(hz * .12), int(W * .5), int(hz * .24)], radius=lw * 2, fill=(40, 60, 60), outline=OUT, width=lw)  # 모니터
        d.line([(int(W * .41), int(hz * .19)), (int(W * .44), int(hz * .19)), (int(W * .45), int(hz * .15)),
                (int(W * .46), int(hz * .22)), (int(W * .47), int(hz * .19)), (int(W * .49), int(hz * .19))], fill=(110, 255, 160), width=lw)
    elif kind == "memorial":
        grad(d, W, H, 0, hz, (226, 222, 214), (206, 200, 190))
        d.rectangle([0, hz, W, H], fill=(150, 140, 128))
        cx = W // 2
        fy0, fy1 = int(hz * .04), int(hz * .40)
        d.rectangle([cx - int(W * .06), fy0, cx + int(W * .06), fy1], fill=(250, 248, 242), outline=(40, 34, 30), width=lw * 3)  # 영정 액자
        d.ellipse([cx - int(W * .03), fy0 + int(hz * .07), cx + int(W * .03), fy0 + int(hz * .21)], fill=(200, 196, 188))
        d.pieslice([cx - int(W * .045), fy0 + int(hz * .2), cx + int(W * .045), fy1 + int(hz * .1)], 180, 360, fill=(200, 196, 188))
        d.line([(cx - int(W * .06), fy0), (cx - int(W * .025), fy0)], fill=(30, 30, 30), width=lw * 4)  # 검은 리본
        for fx in (-.17, -.12, .12, .17):  # 국화
            x = cx + int(W * fx)
            d.line([(x, int(hz * .55)), (x, hz)], fill=(90, 130, 80), width=lw * 2)
            for k in range(6):
                a = k * math.pi / 3
                d.ellipse([x + math.cos(a) * W * .012 - W * .012, int(hz * .55) + math.sin(a) * W * .012 - W * .012,
                           x + math.cos(a) * W * .012 + W * .012, int(hz * .55) + math.sin(a) * W * .012 + W * .012], fill=(255, 255, 250), outline=OUT)
        d.rectangle([cx - int(W * .2), int(hz * .72), cx + int(W * .2), hz], fill=(120, 90, 66), outline=OUT, width=lw)
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
            "think": ((-.24, .26), (.12, -.14)), "normal": ((-.25, .28), (.25, .28)),
            "cry": ((-.21, -.22), (.21, -.22)), "shock": ((-.34, -.16), (.34, -.16))}.get(emo, ((-.25, .28), (.25, .28)))
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
        if emo in ("sad", "cry"):
            d.line([(ex - sx * .06 * s, by_ - .03 * s), (ex + sx * .06 * s, by_ + .02 * s)], fill=OUT, width=int(lw * 1.4))  # 안쪽 끝이 올라감
        elif emo == "angry":
            d.line([(ex - sx * .06 * s, by_ + .03 * s), (ex + sx * .06 * s, by_ - .02 * s)], fill=OUT, width=int(lw * 1.6))  # 안쪽 끝이 내려감
        elif emo == "think" and sx == 1:
            d.line([(ex - .06 * s, by_ - .02 * s), (ex + .06 * s, by_ - .06 * s)], fill=OUT, width=int(lw * 1.3))
        else:
            lift = {"happy": -.02, "shock": -.045}.get(emo, 0) * s
            d.line([(ex - .055 * s, by_ + lift), (ex + .055 * s, by_ + lift)], fill=OUT, width=int(lw * 1.2))
        if emo == "cry":  # ㅠㅠ: 꼭 감은 눈 + 흘러내리는 눈물 줄기
            d.line([(ex - .065 * s, ey), (ex + .065 * s, ey)], fill=OUT, width=int(lw * 1.8))
            for tx in (ex - .03 * s, ex + .03 * s):
                d.rounded_rectangle([tx - .016 * s, ey + .01 * s, tx + .016 * s, hy + .3 * s], radius=int(.016 * s), fill=(120, 190, 255), outline=OUT, width=max(2, lw // 2))
        elif blink and emo != "happy":
            d.line([(ex - .055 * s, ey), (ex + .055 * s, ey)], fill=OUT, width=int(lw * 1.4))
        elif emo == "happy":
            d.arc([ex - .06 * s, ey - .045 * s, ex + .06 * s, ey + .075 * s], 200, 340, fill=OUT, width=int(lw * 1.6))
        else:
            rx, ry, pr = .06, .072, .034
            if emo == "angry":
                ry = .05
            if emo == "surprised":
                rx, ry, pr = .07, .092, .02
            if emo == "shock":
                rx, ry, pr = .085, .1, .015
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
    if emo == "cry":  # 엉엉 우는 입
        if mouth:
            ell(cx - .085 * s, my - .03 * s, cx + .085 * s, my + .08 * s, dark)
            d.ellipse([cx - .045 * s, my + .03 * s, cx + .045 * s, my + .075 * s], fill=tongue)
        else:
            pts = [(cx - .07 * s + i * .028 * s, my + (.01 if i % 2 else .04) * s) for i in range(6)]
            d.line(pts, fill=OUT, width=int(lw * 1.4))
    elif emo == "shock":
        k = 1 if mouth else .75
        ell(cx - .05 * s * k, my - .05 * s * k, cx + .05 * s * k, my + .09 * s * k, dark)
    elif emo == "surprised":
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
    elif emo == "shock":  # 이마의 파란 그늘선 + 느낌표 두 개
        for k in range(-2, 3):
            x = cx + k * .07 * s
            d.line([(x, hy - .16 * s), (x, hy - .04 * s)], fill=(80, 100, 210), width=int(lw * 1.2))
        for j in (0, 1):
            x = ex_ + j * .07 * s
            d.rounded_rectangle([x - .02 * s, ey_ - .14 * s, x + .02 * s, ey_ - .03 * s], radius=int(.02 * s), fill=(255, 70, 70))
            d.ellipse([x - .022 * s, ey_, x + .022 * s, ey_ + .044 * s], fill=(255, 70, 70))
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
        self.font_path = font_path  # 굵은 글씨(heavy_font)의 대체 폰트로도 사용
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
              chip=None, hook=None, progress=0.0, accent=(255, 213, 79), hook_big=False, lying=(), shot="wide",
              caption="box", hook_overlay=False, end_text=None):
        """chars: [(id, spec)] / emotions: {id: emo} / hook_big: 숏폼 첫 3초 후크 카드(큰 글씨+폭발 배경)
        lying: 병원 침대에 누운 캐릭터 id 목록 (hospital 배경의 침대 위에 머리+이불로 그림)"""
        vertical = h > w
        horizon = .54 if vertical else .70
        hook_raw = hook  # 큰 후크 문구는 지정한 줄바꿈 그대로
        hook = hook.replace("\n", " ") if hook else hook  # 상단 작은 문구는 한 덩어리로
        lie = [(cid, spec) for cid, spec in chars if cid in lying]
        chars = [(cid, spec) for cid, spec in chars if cid not in lying]
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
        if hook_big and vertical:  # 캐릭터 뒤 폭발(집중선) 배경
            bx, by_, W2 = w / 2 * SS, h * .21 * SS, w * SS
            pts = []
            for k in range(36):
                a = math.pi * 2 * k / 36
                r = W2 * (.62 if k % 2 == 0 else .44)
                pts.append((bx + math.cos(a) * r, by_ + math.sin(a) * r * .85))
            d.polygon(pts, fill=(255, 72, 72, 255))
            d.line(pts + [pts[0]], fill=OUT + (255,), width=int(6 * SS))
        span = .54 if lie else 1.0  # 누운 사람이 있으면 침대 왼쪽에만 섬
        if lie:
            s = min(s, w * span * .9 / n) if not vertical else min(w * span * .9 / n, h * .34)
        focus = None
        for i, (cid, spec) in enumerate(chars):
            cx = w * span * (i + 1) / (n + 1) * SS
            si = s * float(spec.get("scale", 1))  # 어린이 등은 scale < 1
            talking = cid == speaker
            bounce = (.025 * si * SS) if talking and mouth else 0
            draw_char(d, cx, base * SS, si * SS, spec, emotions.get(cid, "normal"),
                      talking and mouth, blink, bounce, lambda z: self.font(z))
            if talking:
                focus = (cx, (base - .66 * si) * SS, si * SS)  # 클로즈업 중심(머리)
        for cid, spec in lie:  # 침대에 누운 캐릭터: 머리만 그려 90도 눕히고 이불을 덮음
            hz = h * horizon
            bx0, bx1, top = w * .60, w * .98, hz * .80
            hs = (bx1 - bx0) * .78 * SS
            tmp = Image.new("RGBA", (int(hs * 1.2), int(hs * 1.4)), (0, 0, 0, 0))
            talking = cid == speaker
            draw_char(ImageDraw.Draw(tmp), tmp.width / 2, tmp.height * .98, hs, spec, emotions.get(cid, "normal"),
                      talking and mouth, blink, 0, lambda z: self.font(z))
            hy = tmp.height * .98 - .66 * hs
            head = tmp.crop((int(tmp.width / 2 - .37 * hs), int(hy - .45 * hs), int(tmp.width / 2 + .37 * hs), int(hy + .31 * hs)))
            head = head.rotate(90, expand=True)
            hx, hy2 = int(bx0 * SS - head.width * .15), int(top * SS - head.height * .62)
            ch.alpha_composite(head, (max(0, hx), max(0, hy2)))
            d.rounded_rectangle([hx + head.width * .93, top * SS - hs * .2, bx1 * SS, top * SS + hs * .08],
                                radius=int(hs * .08), fill=(170, 205, 235, 255), outline=OUT + (255,), width=max(3, int(hs * .012)))
        layer = Image.alpha_composite(layer, ch)
        if shot == "close" and focus:  # 말하는 사람 클로즈업 (2배 해상도에서 잘라 선명함 유지)
            fx, fy, fs = focus
            z = 1.6 if vertical else 1.5
            cw, chh = layer.width / z, layer.height / z
            cy = fy + (.05 if vertical else -.07) * fs  # 머리 위(올림머리 포함)가 잘리지 않게
            x0 = min(max(0, fx - cw / 2), layer.width - cw)
            y0 = min(max(0, cy - chh / 2), layer.height - chh)
            layer = layer.crop((int(x0), int(y0), int(x0 + cw), int(y0 + chh))).resize((w, h), Image.LANCZOS).convert("RGB")
        else:
            layer = layer.reduce(SS).convert("RGB")  # 2배→1배 박스 축소(빠름)
        d = ImageDraw.Draw(layer)

        u = w / 1080 if vertical else w / 1920
        pad = int(70 * u)
        if chip and not vertical:
            f = self.font(40 * u)
            tw = d.textlength(chip, font=f)
            d.rounded_rectangle([pad, int(46 * u), pad + tw + int(50 * u), int(46 * u) + int(66 * u)], radius=int(33 * u), fill=(20, 20, 40))
            d.text((pad + int(25 * u), int(46 * u) + int(10 * u)), chip, font=f, fill=accent)
        if hook and vertical and hook_overlay:  # 쇼츠 첫 대사: 화면 위쪽에 큰 후크 문구 (영상은 움직이는 채로)
            hl = _split_balanced(hook_raw)[:3]
            hs = 104 * u
            while hs > 30 and max(d.textlength(x, font=heavy_font(hs, self.font_path)) for x in hl) > w * .9:
                hs *= .93
            hf = heavy_font(hs, self.font_path)
            y = int(120 * u)
            for i, ln in enumerate(hl):
                tw = d.textlength(ln, font=hf)
                d.text(((w - tw) / 2, y), ln, font=hf, fill=(255, 226, 60) if i == len(hl) - 1 else (255, 255, 255),
                       stroke_width=int(hs * .1), stroke_fill=OUT)
                y += int(hs * 1.15)
        elif hook and vertical:
            f = self.font((104 if hook_big else 68) * u)
            y = int((150 if hook_big else 130) * u)
            hl = wrap(d, hook, f, w - pad * 2)
            if len(hl) == 2 and " " in hook:  # 두 줄이면 가운데 가까운 공백에서 균형 있게 나눔
                sp = [i for i, ch in enumerate(hook) if ch == " "]
                cut = min(sp, key=lambda i: abs(i - len(hook) / 2))
                hl = [hook[:cut], hook[cut + 1:]]
            for ln in hl[:3]:
                tw = d.textlength(ln, font=f)
                d.text(((w - tw) / 2, y), ln, font=f, fill=(255, 240, 90) if hook_big else accent,
                       stroke_width=int((10 if hook_big else 7) * u), stroke_fill=OUT)
                y += int(f.size * 1.25)
        if end_text and vertical:  # 쇼츠 마지막: 본편 안내
            ef = heavy_font(58 * u, self.font_path)
            ew = d.textlength(end_text, font=ef)
            ey = int(h * .3)
            d.rounded_rectangle([(w - ew) / 2 - 36 * u, ey - 16 * u, (w + ew) / 2 + 36 * u, ey + 92 * u], radius=int(26 * u),
                                fill=(255, 213, 60), outline=OUT, width=max(3, int(5 * u)))
            d.text(((w - ew) / 2, ey), end_text, font=ef, fill=(20, 20, 28))
        if text and vertical and caption == "pop":  # 쇼츠 자막: 크고 굵은 구절, 상자 없이 테두리, 숫자는 노랑
            cf = heavy_font(80 * u, self.font_path)
            words = text.split()
            lines_, cur = [], []
            for wd_ in words:
                if cur and d.textlength(" ".join(cur + [wd_]), font=cf) > w * .78:
                    lines_.append(cur)
                    cur = [wd_]
                else:
                    cur.append(wd_)
            if cur:
                lines_.append(cur)
            y = int(h * .655)
            if name:
                nf = self.font(34 * u)
                nw = d.textlength(name, font=nf) + int(40 * u)
                d.rounded_rectangle([(w - nw) / 2, y - int(62 * u), (w + nw) / 2, y - int(14 * u)], radius=int(24 * u),
                                    fill=name_color, outline=OUT, width=max(2, int(3 * u)))
                lum = .3 * name_color[0] + .59 * name_color[1] + .11 * name_color[2]
                d.text(((w - nw) / 2 + int(20 * u), y - int(60 * u)), name, font=nf, fill=(20, 20, 30) if lum > 150 else "white")
            for ws in lines_[:3]:
                line = " ".join(ws)
                x = (w - d.textlength(line, font=cf)) / 2
                for wd_ in ws:
                    col = (255, 226, 60) if any(ch.isdigit() for ch in wd_) else (255, 255, 255)
                    d.text((x, y), wd_, font=cf, fill=col, stroke_width=int(9 * u), stroke_fill=OUT)
                    x += d.textlength(wd_ + " ", font=cf)
                y += int(cf.size * 1.18)
            text = None
        if text and not (hook_big and vertical):  # 후크 카드는 큰 글씨가 자막 역할
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


# ───────────────────────── 썸네일 ─────────────────────────
HEAVY_FONTS = [  # (경로, ttc 인덱스) — 썸네일은 두꺼운 글씨가 핵심
    ("/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc", 1),
    ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 1),
    ("/usr/share/fonts/truetype/nanum/NanumGothicExtraBold.ttf", 0),
    ("/usr/share/fonts/truetype/nanum/NanumSquareEB.ttf", 0),
    ("/System/Library/Fonts/AppleSDGothicNeo.ttc", 8),
    ("C:/Windows/Fonts/malgunbd.ttf", 0),
]
PALETTES = {  # 집중선 배경 2색, 강조 박스 색, 배지 글자색
    "yellow": ((255, 214, 64), (255, 178, 0), (232, 36, 52), (255, 214, 64)),
    "blue": ((92, 200, 255), (30, 150, 240), (232, 36, 52), (255, 230, 80)),
    "red": ((255, 92, 92), (220, 30, 50), (20, 20, 30), (255, 230, 80)),
    "green": ((120, 230, 140), (40, 180, 90), (232, 36, 52), (255, 230, 80)),
    "purple": ((190, 140, 255), (130, 80, 230), (232, 36, 52), (255, 230, 80)),
}


def heavy_font(size, fallback):
    for path, idx in HEAVY_FONTS:
        try:
            return ImageFont.truetype(path, int(size), index=idx)
        except OSError:
            continue
    return ImageFont.truetype(fallback, int(size))


def _split_balanced(text):
    if "\n" in text:
        return [t.strip() for t in text.split("\n") if t.strip()]
    if " " not in text or len(text) <= 6:
        return [text]
    sp = [i for i, ch in enumerate(text) if ch == " "]
    cut = min(sp, key=lambda i: abs(i - len(text) / 2))
    return [text[:cut], text[cut + 1:]]


def render_thumbnail(text, chars, font_path, *, palette="yellow", highlight=None, badge=None, w=1280, h=720):
    """유튜브 썸네일: 집중선 배경 + 확대한 캐릭터(스티커 테두리) + 초대형 글씨 + 강조 박스 + 배지
    chars: [(spec, emotion)] — 첫 번째가 주인공(앞, 크게)"""
    from PIL import ImageFilter
    c1, c2, box, badge_fg = PALETTES.get(palette, PALETTES["yellow"])
    W, H = w * SS, h * SS
    img = Image.new("RGB", (W, H), c1)
    d = ImageDraw.Draw(img)
    ox, oy = W * .70, H * .45  # 집중선 중심 = 캐릭터 쪽
    n = 28
    for k in range(n):
        if k % 2:
            continue
        a0, a1 = 2 * math.pi * k / n, 2 * math.pi * (k + 1) / n
        R = W * 1.5
        d.polygon([(ox, oy), (ox + math.cos(a0) * R, oy + math.sin(a0) * R),
                   (ox + math.cos(a1) * R, oy + math.sin(a1) * R)], fill=c2)

    # 캐릭터 (뒤 → 앞 순서로)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    slots = [(.70, .80, 1.03), (.90, .70, 1.01)]  # (x비율, 크기 배율, 바닥 위치)
    fnt = lambda z: ImageFont.truetype(font_path, max(8, int(z)))
    for (spec, emo), (fx, sc, fb) in reversed(list(zip(chars[:2], slots))):
        draw_char(ld, W * fx, H * fb, H * sc, spec, emo, emo in ("surprised", "happy", "angry"), False, 0, fnt)
    # 스티커 테두리(흰색) + 그림자
    alpha = layer.split()[3]
    small = alpha.resize((w // 2, h // 2))
    halo = small.filter(ImageFilter.MaxFilter(9)).resize((W, H))
    shadow = small.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(6)).resize((W, H))
    img.paste((0, 0, 0), (int(10 * SS), int(10 * SS)), shadow.point(lambda v: int(v * .35)))
    img.paste((255, 255, 255), (0, 0), halo)
    img.paste(layer, (0, 0), layer)

    img = img.reduce(SS)
    d = ImageDraw.Draw(img)
    pad = int(w * .045)
    top = int(h * .07)
    if badge:  # 좌상단 배지
        bf = heavy_font(h * .075, font_path)
        bw = d.textlength(badge, font=bf)
        d.rounded_rectangle([pad, top, pad + bw + h * .06, top + h * .115], radius=int(h * .03), fill=(20, 20, 28))
        d.text((pad + h * .03, top + h * .012), badge, font=bf, fill=badge_fg)
        top += int(h * .16)
    lines = _split_balanced(text)[:3]
    max_w = w * .58
    size = h * (.24 if len(lines) <= 2 else .18)
    while size > 20:
        tf = heavy_font(size, font_path)
        if max(d.textlength(ln, font=tf) for ln in lines) <= max_w:
            break
        size *= .93
    lh = int(size * 1.18)
    y = max(top, int((h - lh * len(lines)) / 2 + h * .06))
    sw = max(4, int(size * .085))
    for ln in lines:
        is_hl = highlight and highlight in ln
        tw = d.textlength(ln, font=tf)
        if is_hl:  # 강조 줄: 색 박스 + 살짝 기울인 느낌의 그림자
            d.rounded_rectangle([pad - int(size * .12) + 8, y + int(size * .08) + 8, pad + tw + int(size * .12) + 8, y + lh + 8],
                                radius=int(size * .12), fill=(0, 0, 0))
            d.rounded_rectangle([pad - int(size * .12), y + int(size * .08), pad + tw + int(size * .12), y + lh],
                                radius=int(size * .12), fill=box, outline=(0, 0, 0), width=max(3, sw // 2))
        d.text((pad + 6, y + 6), ln, font=tf, fill=(0, 0, 0), stroke_width=sw, stroke_fill=(0, 0, 0))
        d.text((pad, y), ln, font=tf, fill=(255, 255, 255) if (is_hl or palette != "yellow") else (255, 255, 255),
               stroke_width=sw, stroke_fill=(0, 0, 0))
        y += lh
    return img


# ───────────────────────── 소품 · 강조 표시 (썸네일·후크 카드용) ─────────────────────────
def _fit_font(d, text, max_w, size, font_path):
    while size > 10:
        f = heavy_font(size, font_path)
        if d.textlength(text, font=f) <= max_w:
            return f
        size *= .92
    return heavy_font(size, font_path)


def prop_image(kind, size, text, font_path):
    """소품 그림(RGBA). size = 소품 가로 길이(px). kind: bankbook/letter/money/phone/photo/sidedish"""
    W, H = int(size), int(size * .72)
    im = Image.new("RGBA", (W + 20, H + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    lw = max(3, int(size * .018))
    o = 10
    if kind == "bankbook":
        d.rounded_rectangle([o, o, o + W, o + H], radius=int(size * .05), fill=(36, 112, 86), outline=OUT, width=lw)
        d.rounded_rectangle([o + W * .06, o + H * .26, o + W * .94, o + H * .92], radius=int(size * .02), fill=(255, 255, 250), outline=OUT, width=max(2, lw // 2))
        hf = _fit_font(d, "통장", W * .3, H * .17, font_path)
        d.text((o + W * .07, o + H * .04), "통장", font=hf, fill=(255, 255, 255))
        for k in range(3):
            y = o + H * (.42 + k * .15)
            d.line([(o + W * .1, y), (o + W * .9, y)], fill=(200, 205, 210), width=max(2, lw // 2))
        if text:
            f = _fit_font(d, text, W * .8, H * .24, font_path)
            tw = d.textlength(text, font=f)
            d.text((o + (W - tw) / 2, o + H * .5), text, font=f, fill=(220, 30, 40), stroke_width=max(1, lw // 3), stroke_fill=(255, 255, 255))
    elif kind == "letter":
        d.polygon([(o, o + H * .08), (o + W * .9, o), (o + W, o + H * .9), (o + W * .08, o + H)], fill=(250, 244, 222), outline=OUT)
        d.line([(o, o + H * .08), (o + W * .9, o), (o + W, o + H * .9), (o + W * .08, o + H), (o, o + H * .08)], fill=OUT, width=lw)
        for k in range(4):
            y = o + H * (.55 + k * .1)
            d.line([(o + W * .14, y + k * 2), (o + W * .84, y - H * .06 + k * 2)], fill=(180, 160, 130), width=max(2, lw // 2))
        if text:
            f = _fit_font(d, text, W * .72, H * .26, font_path)
            d.text((o + W * .14, o + H * .18), text, font=f, fill=(90, 50, 30))
    elif kind == "money":
        for k in range(3):
            y = o + H * (.12 + k * .2)
            d.rounded_rectangle([o + k * W * .03, y, o + W * .9 + k * W * .03, y + H * .5], radius=int(size * .02), fill=(150, 196, 120), outline=OUT, width=lw)
            d.ellipse([o + W * .38 + k * W * .03, y + H * .1, o + W * .52 + k * W * .03, y + H * .4], outline=(60, 110, 60), width=lw)
        d.rectangle([o + W * .62, o + H * .5, o + W * .72, o + H * .98], fill=(255, 250, 240), outline=OUT, width=max(2, lw // 2))
        if text:
            f = _fit_font(d, text, W * .9, H * .26, font_path)
            tw = d.textlength(text, font=f)
            d.text((o + (W - tw) / 2, o + H * .02), text, font=f, fill=(255, 255, 255), stroke_width=lw, stroke_fill=OUT)
    elif kind == "phone":
        pw = W * .5
        d.rounded_rectangle([o + (W - pw) / 2, o, o + (W + pw) / 2, o + H], radius=int(size * .06), fill=(30, 30, 36), outline=OUT, width=lw)
        d.rounded_rectangle([o + (W - pw) / 2 + lw * 2, o + H * .08, o + (W + pw) / 2 - lw * 2, o + H * .9], radius=int(size * .03), fill=(235, 240, 250))
        if text:
            f = _fit_font(d, text, pw * .8, H * .14, font_path)
            tw = d.textlength(text, font=f)
            d.text((o + (W - tw) / 2, o + H * .42), text, font=f, fill=(220, 30, 40))
    elif kind == "sidedish":  # 투명 반찬통 + 바닥에 붙은 쪽지
        bx0, by0, bx1, by1 = o + W * .04, o + H * .24, o + W * .96, o + H * .9
        d.rounded_rectangle([bx0, by0, bx1, by1], radius=int(size * .05), fill=(222, 236, 240), outline=OUT, width=lw)
        d.rounded_rectangle([bx0 + W * .05, by0 + H * .14, bx1 - W * .05, by1 - H * .1], radius=int(size * .03), fill=(196, 62, 40))
        for k in range(7):  # 김치 결
            x = bx0 + W * (.1 + k * .11)
            d.line([(x, by0 + H * .2), (x + W * .05, by1 - H * .16)], fill=(236, 120, 70), width=max(2, lw // 2))
        d.rounded_rectangle([o, o + H * .08, o + W, o + H * .27], radius=int(size * .04), fill=(70, 140, 220), outline=OUT, width=lw)
        nx0, ny0 = o + W * .46, o + H * .58  # 바닥에 붙은 쪽지 (비스듬히 삐져나옴)
        d.polygon([(nx0, ny0), (o + W * .97, ny0 - H * .06), (o + W * .99, o + H * .98), (nx0 + W * .02, o + H * 1.02)], fill=(255, 246, 170), outline=OUT)
        d.line([(nx0, ny0), (o + W * .97, ny0 - H * .06), (o + W * .99, o + H * .98), (nx0 + W * .02, o + H * 1.02), (nx0, ny0)], fill=OUT, width=lw)
        if text:
            f = _fit_font(d, text, W * .48, H * .2, font_path)
            d.text((nx0 + W * .04, ny0 + H * .1), text, font=f, fill=(150, 40, 30))
    else:  # photo
        d.rectangle([o, o, o + W, o + H], fill=(255, 255, 255), outline=OUT, width=lw)
        d.rectangle([o + W * .06, o + H * .08, o + W * .94, o + H * .78], fill=(190, 210, 230))
        if text:
            f = _fit_font(d, text, W * .86, H * .16, font_path)
            d.text((o + W * .07, o + H * .8), text, font=f, fill=OUT)
    return im


def draw_mark(d, box, src, scale=1.0):
    """빨간 원(소품 주위) + 빨간 화살표(src → 원)"""
    x0, y0, x1, y1 = box
    px, py = (x1 - x0) * .14, (y1 - y0) * .18
    lw = int(max(6, (x1 - x0) * .035) * scale)
    d.ellipse([x0 - px, y0 - py, x1 + px, y1 + py], outline=(235, 30, 40), width=lw)
    tx, ty = (x0 + x1) / 2, (y0 + y1) / 2
    ang = math.atan2(ty - src[1], tx - src[0])
    rx, ry = (x1 - x0) / 2 + px, (y1 - y0) / 2 + py
    ex, ey = tx - math.cos(ang) * rx * 1.08, ty - math.sin(ang) * ry * 1.08
    d.line([src, (ex, ey)], fill=(235, 30, 40), width=int(lw * 1.4))
    hl = lw * 3.2
    d.polygon([(ex + math.cos(ang) * hl * .4, ey + math.sin(ang) * hl * .4),
               (ex - math.cos(ang - .5) * hl, ey - math.sin(ang - .5) * hl),
               (ex - math.cos(ang + .5) * hl, ey - math.sin(ang + .5) * hl)], fill=(235, 30, 40))


def drama_bg(w, h, tone="red"):
    """어두운 드라마 배경: 가운데 붉은(또는 푸른) 빛 + 옅은 집중선 + 가장자리 어둡게"""
    from PIL import ImageFilter
    core = {"red": (120, 26, 34), "blue": (34, 52, 120), "gold": (130, 90, 20)}.get(tone, (120, 26, 34))
    img = Image.new("RGB", (w, h), (12, 10, 16))
    glow = Image.new("L", (w, h), 0)
    ImageDraw.Draw(glow).ellipse([w * .3, h * .05, w * 1.15, h * 1.1], fill=255)
    glow = glow.filter(ImageFilter.GaussianBlur(min(w, h) * .18))
    img = Image.composite(Image.new("RGB", (w, h), core), img, glow)
    rays = Image.new("L", (w, h), 0)
    rd = ImageDraw.Draw(rays)
    ox, oy, n = w * .7, h * .45, 30
    for k in range(0, n, 2):
        a0, a1 = 2 * math.pi * k / n, 2 * math.pi * (k + 1) / n
        R = max(w, h) * 1.5
        rd.polygon([(ox, oy), (ox + math.cos(a0) * R, oy + math.sin(a0) * R), (ox + math.cos(a1) * R, oy + math.sin(a1) * R)], fill=26)
    img = Image.composite(Image.new("RGB", (w, h), tuple(min(255, c + 60) for c in core)), img, rays)
    return img


def big_face(spec, emo, mouth, blink, s, font_path):
    """캐릭터를 크게 그려 흰 스티커 테두리를 두른 RGBA (머리 중심 좌표도 반환)"""
    from PIL import ImageFilter
    W, H = int(s * 1.2), int(s * 1.25)
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    base = H * .98
    draw_char(ImageDraw.Draw(layer), W / 2, base, s, spec, emo, mouth, blink, 0, lambda z: ImageFont.truetype(font_path, max(8, int(z))))
    a = layer.split()[3]
    halo = a.filter(ImageFilter.MaxFilter(15))
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    out.paste((255, 255, 255, 255), (0, 0), halo)
    out.alpha_composite(layer)
    return out, (W / 2, base - .66 * s)


def render_story_thumbnail(text, main, font_path, *, tone="red", highlight=None, badge=None, prop=None, w=1280, h=720):
    """사연형 썸네일: 어두운 드라마 배경 + 감정 폭발 얼굴 클로즈업 + 소품(빨간 원·화살표) + 초대형 2줄 문구"""
    W, H = w * SS, h * SS
    img = drama_bg(W, H, tone).convert("RGBA")
    spec, emo = main
    s = H * 1.2
    face, (fx, fy) = big_face(spec, emo, True, False, s, font_path)
    img.alpha_composite(face, (int(W * .74 - fx), int(H * .52 - fy)))
    d = ImageDraw.Draw(img)
    pad = W * .045
    y = H * .07
    if badge:
        bf = heavy_font(H * .062, font_path)
        bw = d.textlength(badge, font=bf)
        d.rounded_rectangle([pad, y, pad + bw + H * .05, y + H * .095], radius=int(H * .025), fill=(235, 30, 40))
        d.text((pad + H * .025, y + H * .008), badge, font=bf, fill=(255, 255, 255))
        y += H * .13
    lines = _split_balanced(text)[:2]
    size = H * .165
    while size > 20:
        tf = heavy_font(size, font_path)
        if max(d.textlength(ln, font=tf) for ln in lines) <= W * .6:
            break
        size *= .93
    for ln in lines:
        hl = bool(highlight and highlight in ln)
        d.text((pad + 10, y + 10), ln, font=tf, fill=(0, 0, 0), stroke_width=int(size * .1), stroke_fill=(0, 0, 0))
        d.text((pad, y), ln, font=tf, fill=(255, 226, 60) if hl else (255, 255, 255), stroke_width=int(size * .09), stroke_fill=(0, 0, 0))
        y += size * 1.12
    if prop:
        top, bottom = y + H * .02, H * .97  # 빨간 원(소품 위아래 18% 여백)까지 화면 안에 들어오도록 크기 조정
        ps = H * .38
        for _ in range(8):
            pim = prop_image(prop.get("type", "bankbook"), ps, prop.get("text", ""), font_path).rotate(-8, expand=True, resample=Image.BICUBIC)
            if pim.height * 1.36 <= bottom - top or ps < H * .22:
                break
            ps *= .9
        px = int(W * .21 - pim.width / 2)
        py = int(max(top + pim.height * .18, bottom - pim.height * 1.18))
        img.alpha_composite(pim, (px, py))
        draw_mark(ImageDraw.Draw(img), (px, py, px + pim.width, py + pim.height), (W * .5, py + pim.height * .45), 1.4)  # 화살표는 글자를 가리지 않게 옆에서
    return img.convert("RGB").resize((w, h), Image.LANCZOS)


def render_hook_card(w, h, spec, emo, mouth, blink, text, font_path, prop=None, zoom=1.0, tone="red", progress=0.0):
    """숏폼 첫 화면: 어두운 드라마 배경 + 화면 아래 절반을 채우는 감정 얼굴 + 소품 + 초대형 후크 문구 (zoom>1 이면 확대된 상태)"""
    img = drama_bg(w, h, tone).convert("RGBA")
    s = w * 1.22
    face, (fx, fy) = big_face(spec, emo, mouth, blink, s, font_path)
    img.alpha_composite(face, (int(w * .5 - fx), int(h * .7 - fy)))
    d = ImageDraw.Draw(img)
    if prop:
        pim = prop_image(prop.get("type", "bankbook"), w * .5, prop.get("text", ""), font_path).rotate(-7, expand=True, resample=Image.BICUBIC)
        px, py = int(w * .5 - pim.width / 2), int(h * .425 - pim.height / 2)
        img.alpha_composite(pim, (px, py))
        draw_mark(ImageDraw.Draw(img), (px, py, px + pim.width, py + pim.height), (w * .97, h * .29), 1.0)
    lines = _split_balanced(text)[:3]
    size = w * .115
    while size > 20:
        tf = heavy_font(size, font_path)
        if max(d.textlength(ln, font=tf) for ln in lines) <= w * .9:
            break
        size *= .93
    y = h * .085
    for i, ln in enumerate(lines):
        tw = d.textlength(ln, font=tf)
        col = (255, 226, 60) if i == len(lines) - 1 else (255, 255, 255)
        d.text(((w - tw) / 2, y), ln, font=tf, fill=col, stroke_width=int(size * .1), stroke_fill=(0, 0, 0))
        y += size * 1.15
    out = img.convert("RGB")
    if zoom > 1.0:
        cw, ch = w / zoom, h / zoom
        out = out.crop((int((w - cw) / 2), int((h - ch) / 2), int((w + cw) / 2), int((h + ch) / 2))).resize((w, h), Image.LANCZOS)
    ImageDraw.Draw(out).rectangle([0, h - max(4, int(h * .004)), int(w * progress), h], fill=(255, 213, 79))
    return out
