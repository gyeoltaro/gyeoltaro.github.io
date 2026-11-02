"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연, 17편)
구성: 영식(화자) 시점. 장례식장 조문 줄(앞당김) → 30년 전 연탄 스무 장 → 엄마의 자존심 → 서울 → 부고 → 빈소
→ 골목 끝까지 이어진 줄 → 사람들의 사연 → 연탄 가게 사장의 말 → 할아버지의 겨울 → 다음 해 겨울 → 마무리
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 20초~2분 45초, 가장 센 대사로 시작) + 예고형 1개(롱폼으로 데려오는 입구)"""
import json
YS, KD, MOM, CH, AJ, SH, NB, N = "youngsik", "youngsik_kid", "mom", "choi", "ajumma", "shopkeeper", "neighbor", "narrator"


def L(w, t, e="normal", r=None):
    d = {"who": w, "text": t}
    if w != N:
        d["emotion"] = e
    if r:
        d["react"] = r
    return d


S = []


def scene(title, bg, cast, lines=None, **kw):
    S.append(dict(title=title, bg=bg, cast=cast, lines=lines, **kw))
    return len(S) - 1


s_open = scene("골목 끝까지", "memorial", [YS, AJ, MOM], mood="sad", when="장례식 날", lines=[
    L(N, "장례식 이튿날, 조문 줄이 골목 끝까지 이어져 있었어요. 모두 손에 연탄 한 장씩을 들고 있었죠."),
    dict(L(AJ, "저희 집도 해마다 연탄 스무 장을 받았어요. 영감님은 늘 연탄이 남아서라고 하셨죠.", "cry", {YS: "shock", MOM: "cry"}), sfx="thud"),
    L(YS, "우리 집에도 해마다 그러셨어요. 연탄이 남아서라고요.", "cry", {AJ: "cry"}),
    L(MOM, "영식아, 이 줄 좀 봐라. 영감님이 이 모든 집에 그렇게 하셨구나.", "cry", {YS: "cry"}),
    L(N, "저는 영정 앞에서 한참을 일어나지 못했어요. 30년이 걸려서야 알게 된 일이었으니까요."),
    L(N, "이 이야기를 하려면, 달동네 세 들어 살던 제 어린 시절부터 말씀드려야 해요."),
])
s_first = scene("첫눈 오는 날", "yard", [KD, MOM, CH], mood="warm", when="30년 전", flashback=True, lines=[
    L(N, "저는 어릴 때 달동네 비탈길 끝, 낡은 세방에서 엄마와 단둘이 살았어요."),
    L(CH, "어, 영식이 어머니. 우리 집 연탄이 또 남았네. 이걸 어떡하나.", "normal", {MOM: "surprised"}),
    L(MOM, "영감님, 저희가 다음 달에 형편이 되면 사 놓을게요. 괜찮습니다.", "sad"),
    L(CH, "아이고, 연탄은 쌓아 두면 습기 먹어서 못 쓰는데. 버리긴 아깝고. 좀 가져가 줘.", "normal", {KD: "happy"}),
    L(KD, "엄마, 할아버지가 연탄이 남아서 그러시대. 가져가자!", "happy", {MOM: "think"}),
    L(MOM, "…남는 거라고 하시니 받겠습니다. 정말 고맙습니다, 영감님.", "sad", {CH: "happy"}),
    L(CH, "고맙긴. 내가 외려 고맙지. 치워 줘서.", "happy"),
    L(N, "할아버지는 지게에 연탄 스무 장을 얹어 우리 연탄 창고에 쌓아 주고 가셨어요."),
])
s_room = scene("엄마의 자존심", "room", [KD, MOM], mood="sad", when="그날 밤", lines=[
    L(N, "그날 밤, 연탄불이 방을 따뜻하게 데웠어요. 저는 이불 속에서 엄마한테 물었죠."),
    L(KD, "엄마, 할아버지는 왜 맨날 연탄이 남아? 우리는 모자라는데.", "think", {MOM: "surprised"}),
    L(MOM, "…영식아, 어른들 사정은 그냥 고맙다고 받으면 되는 거야.", "sad"),
    L(KD, "근데 엄마, 연탄이 남으면 할아버지도 추우실까 봐 걱정돼.", "sad"),
    L(MOM, "그러게. 우리 아들이 어른이 되면 꼭 갚아 드려야지. 약속하자.", "sad", {KD: "happy"}),
    L(KD, "응, 약속!", "happy"),
    dict(L(N, "엄마는 제 머리를 쓰다듬으며 아주 오래 창밖을 쳐다보셨어요. 눈이 펑펑 내리고 있었죠."), sfx="ding"),
    L(N, "해마다 첫눈이 오는 날이면 할아버지는 어김없이 지게를 지고 우리 집 앞에 나타났어요."),
])
s_years = scene("서울살이", "street", [YS, MOM], mood="calm", when="20년 뒤", lines=[
    L(N, "세월이 흘러 저는 서울에 취직했고, 달동네를 떠나 아파트로 이사했어요. 엄마를 모시고요."),
    L(MOM, "영식아, 요즘 최 영감님 안부 좀 알아봐라. 그분 연세가 얼만데.", "sad"),
    L(YS, "엄마, 저 요즘 정말 바빠요. 다음에 한번 가요.", "normal", {MOM: "sad"}),
    L(MOM, "그래, 그래. 너 바쁜 건 안다.", "sad"),
    L(N, "저는 그 말을 몇 해 동안 흘려들었어요. 일이 바쁘다는 핑계가 제일 쉬웠거든요."),
    L(N, "엄마는 한 번도 서운하다는 말을 안 하셨어요. 그냥 해마다 11월이 되면 창가에 앉아 계셨죠."),
    L(MOM, "이제 곧 첫눈이 오겠구나. 영감님은 지게 지고 오시려나.", "think"),
])
scene("부고", "living", [YS, MOM], mood="sad", when="그해 겨울", lines=[
    L(N, "그해 겨울, 달동네 이장님에게서 전화 한 통이 걸려 왔어요."),
    L(YS, "네, 이장님. 오랜만입니다. 무슨 일이세요?", "normal"),
    dict(L(N, "최 영감님이 어제 새벽에 돌아가셨다는 소식이었어요. 향년 여든일곱이셨죠."), sfx="thud"),
    L(YS, "엄마, 최 할아버지가… 돌아가셨대요.", "sad", {MOM: "shock"}),
    L(MOM, "뭐라고? 영감님이? 내가 얼른 찾아뵀어야 했는데…", "cry", {YS: "cry"}),
    L(YS, "엄마, 지금 바로 가요. 제가 모셔다 드릴게요.", "cry"),
    L(N, "저는 그제야 엄마의 오랜 부탁이 하나도 지켜지지 않았다는 걸 깨달았어요."),
])
s_hall = scene("조용한 빈소", "memorial", [YS, MOM, NB], mood="sad", when="장례식 첫날", lines=[
    L(N, "장례식장에 도착해 보니 빈소가 쓸쓸할 만큼 조용했어요."),
    L(NB, "자식도 없이 혼자 사셨으니, 누가 조문을 오겠어. 이장님이랑 우리 몇 사람뿐이겠지.", "sad", {MOM: "sad"}),
    L(MOM, "영감님, 저 영식이 엄마예요. 너무 늦게 왔습니다. 용서하세요.", "cry"),
    L(YS, "할아버지, 저 영식이에요. 연탄… 한 번도 갚지 못해서 죄송합니다.", "cry", {MOM: "cry"}),
    L(N, "영정 속 할아버지는 낡은 털모자를 쓰고 환하게 웃고 계셨어요. 우리 집에 연탄을 쌓아 주던 그날처럼요."),
    L(N, "그날 밤, 저는 엄마와 둘이 빈소를 지켰어요. 더는 올 사람이 없을 거라고 생각했죠."),
])
scene("줄이 시작됐다", "street", [YS, AJ, NB], mood="hope", when="장례식 둘째 날 아침", lines=[
    L(N, "그런데 이튿날 아침, 장례식장 앞 골목이 웅성거리기 시작했어요."),
    L(AJ, "영감님 빈소가 여기 맞나요? 저 비탈길 맨 윗집 아줌마예요. 연탄 때문에 왔어요.", "sad", {YS: "surprised"}),
    L(YS, "연탄이요? 그게 무슨…", "surprised"),
    L(AJ, "영감님이 해마다 우리 집에 연탄을 쌓아 주셨어요. 남는다고 하시면서요.", "cry", {NB: "cry"}),
    L(NB, "나도 받았어. 우리 집도, 아랫집도, 그 아랫집도…", "cry", {YS: "shock"}),
    dict(L(N, "한 사람이 연탄 한 장을 영정 앞에 놓고 울며 절했어요. 그리고 또 한 사람, 또 한 사람."), sfx="ding"),
    L(N, "점심때가 되자 줄은 골목 끝까지 이어졌어요. 모두 연탄 한 장씩을 들고 있었죠."),
])
s_story = scene("사람들의 사연", "hallway", [YS, AJ, NB], mood="sad", when="장례식 둘째 날", lines=[
    L(N, "저는 줄 서 있는 사람들에게 하나둘 사연을 물어봤어요."),
    L(AJ, "남편이 일찍 가서 혼자 애 셋을 키웠어요. 겨울마다 연탄이 걱정이었는데 영감님이 쌓아 주셨죠.", "cry"),
    L(NB, "우리 아들 중풍 걸린 해에도 영감님이 연탄 마흔 장을 쌓아 주고 가셨어요.", "sad", {YS: "surprised"}),
    L(YS, "마흔 장이요? 저희는 스무 장이었는데…", "surprised", {NB: "sad"}),
    L(AJ, "형편이 더 어려운 집은 마흔 장, 그보다 더한 집은 쉰 장까지도 쌓아 주셨대요.", "sad"),
    L(NB, "그런데 영감님이 뭐라고 하신 줄 알아? 자기는 연탄이 남아서 어쩔 수 없대.", "happy", {AJ: "cry"}),
    L(AJ, "그 말씀 한 번도 틀린 적이 없었어요. 해마다 똑같이 남는다고 하셨지.", "cry"),
    L(N, "저는 그 말을 듣고 가슴이 먹먹했어요. 남는 연탄이 해마다 몇 집을 살렸는지 아무도 몰랐으니까요."),
])
s_shop = scene("연탄 가게 사장님", "warehouse", [YS, SH], mood="sad", when="그날 오후", lines=[
    L(N, "그날 오후, 동네 연탄 가게 사장님이 저를 찾아왔어요."),
    L(SH, "자네가 영식이인가. 영감님이 자주 자네 얘기를 하셨어. 서울 가서 잘 사는 아이라고.", "happy", {YS: "surprised"}),
    L(YS, "사장님, 할아버지가 연탄이 정말 해마다 남으셨던 건가요?", "think"),
    dict(L(SH, "남기는 무슨. 영감님은 해마다 가을이면 내 가게에 와서 연탄을 주문하셨어. 몇백 장씩.", "sad", {YS: "shock"}), sfx="thud"),
    L(SH, "내가 이만큼이나 때실 거냐고 물으면 매번 그러셨지. 남는 건 이웃 줄 거라고.", "sad"),
    L(SH, "그런데 영감님 방은 가 본 적 있나? 연탄을 두 장만 때고 지내셨어. 겨울 내내.", "cry", {YS: "cry"}),
    L(YS, "두 장이요? 이 추운 겨울에 두 장으로요?", "cry"),
    L(SH, "자기 몫은 아껴서 이웃 거 먼저 챙기셨던 거야. 영감님이 연탄이 남는 해는 한 번도 없었어.", "cry"),
    L(N, "저는 그 자리에서 소리 내어 울어 버렸어요."),
    L(N, "30년 동안 받은 연탄이 누구의 겨울이었는지 이제야 알았으니까요."),
])
scene("할아버지의 겨울", "room", [CH, SH], mood="warm", when="어느 해 겨울 · 사장님의 기억", flashback=True, lines=[
    L(SH, "영감님, 올해도 연탄 이렇게 많이 주문하시게요? 영감님 몫은 안 챙기세요?", "sad", {CH: "happy"}),
    L(CH, "내 방은 두 장이면 돼. 저 위 집 애들은 열 장은 있어야 하고.", "happy"),
    L(SH, "영감님이 그렇게까지 하시면 몸도 안 좋으신데 어떻게 하세요.", "sad"),
    L(CH, "나는 혼자잖나. 혼자 사는 사람이 추위 좀 타는 건 괜찮아.", "happy"),
    L(CH, "그런데 아이들 있는 집은 달라. 애들이 춥게 자면 그게 평생 가거든.", "normal", {SH: "cry"}),
    L(SH, "그럼 남는다고 말씀하세요? 그냥 드린다고 하셔도 되는데.", "sad"),
    L(CH, "그냥 드린다고 하면 받는 사람이 미안해하지. 남는다고 하면 고맙다고만 하면 돼.", "happy"),
    dict(L(CH, "받는 사람 마음 편한 게 더 큰 선물이야.", "happy", {SH: "cry"}), sfx="ding"),
])
s_next = scene("다음 해 겨울", "yard", [YS, MOM, AJ], mood="warm", when="다음 해 첫눈", lines=[
    L(N, "장례를 마친 다음 해 첫눈이 오던 날, 저는 달동네로 돌아왔어요."),
    L(YS, "엄마, 나 이제 할아버지가 하던 일 해 볼래요. 이번엔 우리가 쌓아 드릴 차례예요.", "happy", {MOM: "cry"}),
    L(MOM, "그래, 영식아. 약속 지켜 줘서 고맙다. 영감님도 하늘에서 웃으시겠다.", "cry"),
    L(N, "저는 할아버지 집 앞에서부터 연탄을 쌓기 시작했어요. 지게는 없어서 손수레로요."),
    L(AJ, "영식 씨, 우리도 거들게. 연탄은 같이 날라야 빠르잖아.", "happy", {YS: "happy"}),
    L(N, "골목 사람들이 하나둘 나와 연탄을 날랐어요. 어느새 줄은 골목 끝까지 이어졌어요."),
    L(YS, "연탄이 남아서요. 이거 좀 쓰세요.", "happy", {AJ: "happy"}),
    L(AJ, "그래요, 남는다고 하면 받아야지. 고맙습니다.", "happy"),
])
scene("여러분께", "street", [YS, MOM], mood="warm", when="그날 저녁", lines=[
    L(N, "그날 저녁, 저는 엄마와 할아버지 집 앞에 나란히 서서 첫눈을 바라봤어요."),
    L(MOM, "영식아, 사람이 죽으면 뭘 남기는지 아니? 돈도 이름도 아니고 마음이란다.", "happy", {YS: "cry"}),
    L(YS, "맞아요 엄마. 그 마음이 이 골목 모든 집 연탄불에 아직 타고 있어요.", "happy"),
    L(N, "저는 이제 압니다. 우리가 받은 건 연탄이 아니라, 받는 사람이 미안하지 않게 하려는 마음이었다는 걸요."),
    L(N, "여러분이라면 이웃에게 무엇을 남기고 싶으세요? 댓글로 들려주세요."),
    L(N, "※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다."),
])

TITLE = "해마다 \"연탄이 남아서\" 옆집에 쌓아 주던 할아버지, 장례식 날 골목 끝까지 줄이 이어졌다"
DESC_SHORT = "해마다 \"연탄이 남아서\"라며 이웃에게 연탄을 쌓아 주던 할아버지. 장례식 날, 조문 줄이 골목 끝까지 이어졌습니다. 연탄 가게 사장님이 들려준 진짜 이유.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #감동사연 #연탄 #이웃 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "briquette-line",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Alnilam",
    "cast": {
        YS: {"name": "영식", "gvoice": "ko-KR-Chirp3-HD-Alnilam", "color": "#546e7a", "hair": "short", "hair_color": "#222222", "skin": "#fbdcc4"},
        KD: {"name": "어린 영식", "gvoice": "ko-KR-Chirp3-HD-Zephyr", "color": "#ffb74d", "hair": "short", "hair_color": "#222222", "skin": "#ffe0c8", "scale": 0.6},
        MOM: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#9e8a7d", "hair": "bun", "hair_color": "#6d625a", "skin": "#eec4a2"},
        CH: {"name": "최 할아버지", "gvoice": "ko-KR-Chirp3-HD-Rasalgethi", "color": "#455a64", "hair": "none", "hair_color": "#b7b2ad", "skin": "#e8b994", "accessory": "glasses"},
        AJ: {"name": "아주머니", "gvoice": "ko-KR-Chirp3-HD-Despina", "color": "#ba68c8", "hair": "bun", "hair_color": "#3a2618"},
        SH: {"name": "연탄 가게 사장", "gvoice": "ko-KR-Chirp3-HD-Fenrir", "color": "#6d4c41", "hair": "short", "hair_color": "#3a3a3a", "skin": "#e8b994"},
        NB: {"name": "이웃 아주머니", "gvoice": "ko-KR-Chirp3-HD-Vindemiatrix", "color": "#81a58a", "hair": "bun", "hair_color": "#9e9a96", "skin": "#e8b994"},
    },
    "scenes": S,
    "teaser": [[s_open, 1, 3], [s_shop, 3, 5], [s_shop, 7, 8]],
    "shorts_speed": 1.25,
    "shorts": [
        {"format": "full", "speed": 1.0,
         "clips": [[s_open, 1, 4], [s_first, 1, 7], [s_room, 1, 6], [s_story, 1, 7], [s_hall, 1, 5], [s_shop, 1, 6], [s_shop, 6, 9]],
         "hook": "연탄이 남아서\n그러시대요",
         "hook_who": AJ, "hook_emotion": "cry", "hook_tone": "red", "hook_prop": {"type": "receipt", "text": "연탄 주문서"},
         "cta_line": "연탄 가게 사장님이 들려준 이야기, 아래 본편에서 이어집니다.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"연탄이 남아서라고 하시더라고요\" 장례식 날 골목 끝까지 이어진 줄 #시니어사연 #감동사연 #연탄",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_shop, 3, 9], [s_story, 1, 8], [s_hall, 1, 5], [s_open, 1, 4], [s_next, 1, 8]],
         "hook": "영감님 방은\n연탄 두 장이었어",
         "hook_who": SH, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "receipt", "text": "연탄 주문서"},
         "cta_line": "할아버지의 겨울, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"영감님 방은 연탄 두 장만 때셨어\" 연탄 가게 사장님의 말 #감동사연 #연탄 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_open, 1, 3], [s_first, 1, 8], [s_room, 1, 6], [s_years, 1, 6], [s_hall, 1, 5], [s_next, 1, 8]],
         "hook": "남는다고 하면\n고맙다고만 하면 돼",
         "hook_who": CH, "hook_emotion": "happy", "hook_tone": "blue", "hook_prop": {"type": "receipt", "text": "연탄 스무 장"},
         "cta_line": "할아버지가 연탄을 쌓은 진짜 이유, 본편에서 이어서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"남는다고 하면 받는 사람이 편해\" 할아버지의 마지막 한마디 #감동사연 #이웃 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"clips": [[s_open, 1, 3], [s_shop, 3, 5]], "hook": "연탄이 남아서라던\n할아버지의 진짜 이유",
         "hook_who": SH, "hook_emotion": "sad", "hook_tone": "red", "hook_prop": {"type": "receipt", "text": "연탄 주문서"},
         "end_text": "진짜 이유는 본편에서 ▶",
         "title": "\"연탄이 남아서라고 하시더라고요\" #시니어사연 #감동사연 #연탄"},
    ],
    "thumbnail": {
        "text": "연탄이 남아서\n그러시대요",
        "highlight": "연탄이 남아서",
        "badge": "감동 사연",
        "variants": [
            {"style": "story", "tone": "red", "face": [AJ, "cry"], "prop": {"type": "receipt", "text": "연탄 스무 장"}},
            {"style": "story", "tone": "gold", "face": [SH, "sad"], "text": "영감님 방은\n연탄 두 장", "highlight": "연탄 두 장",
             "badge": "눈물 주의", "prop": {"type": "receipt", "text": "연탄 주문서"}},
            {"style": "story", "tone": "blue", "face": [YS, "cry"], "text": "골목 끝까지\n이어진 줄", "highlight": "이어진 줄",
             "badge": "장례식 날", "prop": {"type": "receipt", "text": "연탄 한 장"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“연탄이 남아서라고 하시더라고요”… 이웃에게 연탄을 쌓아 주던 할아버지의 장례식 날",
                           "30년 동안 우리 집에 연탄을 쌓아 주던 옆집 할아버지, 연탄 가게 사장님의 말에 무너졌다"],
        "description": "해마다 첫눈이 오면 “연탄이 남아서”라며 이웃 집 연탄 창고를 채워 주던 최 할아버지. 장례식 날 조문 줄은 골목 끝까지 이어졌고, 연탄 가게 사장님이 진짜 이유를 들려줬습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 이웃에게 무엇을 남기고 싶으세요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #감동사연",
        "tags": ["사연", "시니어사연", "감동 사연", "연탄", "이웃", "달동네", "할아버지", "겨울", "인생이야기", "사연 만화", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-11-09T18:00:00+09:00",
        "pinned_comment": "여러분이라면 이웃에게 무엇을 남기고 싶으세요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-11-09T18:10:00+09:00", "2026-11-10T12:00:00+09:00", "2026-11-11T12:00:00+09:00", "2026-11-11T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
