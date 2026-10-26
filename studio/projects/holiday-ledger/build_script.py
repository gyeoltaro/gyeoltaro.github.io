"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 맏며느리(화자) 시점. 차례상 앞에서 장부를 내미는 순간(앞당김) → 첫 명절 → 장부를 쓰기 시작한 밤 → 동서가 들어온 날
→ 혼자 부친 전 300장 → 시어머니 수술비(비밀) → 은행에서 본 보증금 → 올해 추석 → 장부 공개 → 5천만 원 → 남편과 시아버지
→ 장부 맨 뒷장(시어머니 시점) → 사과 → 다음 설날
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 30초~3분, 가장 센 대사로 시작) + 예고형 1개"""
import json
SY, MIL, FIL, HU, DS, SIL, N = "sunyoung", "mother", "father", "jeongwoo", "jieun", "jeonghee", "narrator"


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


s_open = scene("차례상 앞", "jesa", [SY, MIL, DS], mood="tense", when="올해 추석", lines=[
    L(MIL, "올해 차례비는 네가 다 내라. 동서는 형편이 어렵다잖니.", "angry", {SY: "sad", DS: "happy"}),
    L(N, "그 말을 하는 시어머니 옆에서, 동서는 새로 산 명품 가방을 만지작거리고 있었어요."),
    dict(L(SY, "어머님, 이 장부 한번 보세요.", "angry", {MIL: "shock", DS: "surprised"}), sfx="thud"),
    L(N, "십 년 동안 한 번도 말대꾸하지 않던 맏며느리가, 차례상 앞에 낡은 장부 한 권을 내려놓았습니다."),
    L(N, "그 장부에는 시댁 식구 누구도 몰랐던 숫자들이 적혀 있었어요."),
    L(N, "이 이야기를 하려면, 제가 처음 이 집에서 명절을 보낸 날로 돌아가야 해요."),
])
scene("첫 명절", "kitchen", [SY, MIL, HU], mood="calm", when="10년 전", flashback=True, lines=[
    L(N, "결혼하고 첫 추석. 새벽 다섯 시에 일어나 부엌에 섰어요."),
    L(MIL, "맏며느리는 원래 이런 거다. 전은 삼백 장, 나물은 다섯 가지.", "normal", {SY: "surprised"}),
    L(SY, "네, 어머님. 근데 어머님, 다른 식구들은 언제 와요?", "think"),
    L(MIL, "다들 바쁘지. 오후에 와서 먹기만 하면 돼.", "normal", {SY: "sad"}),
    L(HU, "엄마 말대로 해. 우리 집은 원래 그래.", "normal", {SY: "sad"}),
    L(N, "그날 저는 열두 시간을 서서 전을 부쳤고, 저녁상에서는 '간이 좀 싱겁다'는 말을 들었어요."),
])
scene("장부를 쓴 밤", "room_night", [SY], mood="sad", when="9년 전", flashback=True, lines=[
    L(N, "두 번째 명절이 끝난 밤, 저는 문구점에서 초록색 장부 한 권을 샀어요."),
    L(SY, "추석 장보기 사십삼만 원. 일한 시간 열네 시간. 어머님 용돈 이십만 원.", "sad"),
    L(SY, "누구한테 보여 주려는 게 아니야. 내가 버틴 걸 내가 잊지 않으려고.", "cry"),
    L(N, "그날부터 십 년 동안, 영수증 한 장도 버리지 않고 장부에 붙였어요."),
])
scene("동서가 들어온 날", "living", [SY, MIL, DS], mood="tense", when="8년 전", lines=[
    L(N, "결혼 이 년째, 시동생이 장가를 갔어요. 동서 지은이가 들어왔죠."),
    L(MIL, "지은이는 직장 다니니까 명절엔 쉬어라. 피곤할 텐데.", "happy", {DS: "happy", SY: "surprised"}),
    L(SY, "어머님, 저도 직장 다니는데요.", "surprised"),
    L(MIL, "너는 맏이잖니. 맏이가 그런 것까지 따지면 집안이 어떻게 되겠어.", "angry", {SY: "sad"}),
    L(DS, "형님, 죄송해요. 그럼 저는 설거지만 할게요.", "happy"),
    L(N, "동서는 그 뒤로 팔 년 동안, 설거지를 한 번도 하지 않았어요."),
])
scene("혼자 부친 전", "kitchen", [SY, HU], mood="sad", when="5년 전 · 설날", lines=[
    L(N, "명절이면 거실에서는 웃음소리가, 부엌에서는 기름 튀는 소리만 났어요."),
    L(SIL, "새언니, 식혜는 아직이야? 목말라.", "normal", {SY: "sad"}),
    L(DS, "형님, 동그랑땡 좀 많이 해 주세요. 애들이 좋아해요.", "happy"),
    L(HU, "여보, 나 친구들 잠깐 보고 올게. 쉬엄쉬엄 해.", "happy", {SY: "angry"}),
    L(SY, "정우 씨, 잠깐만. 나도 좀 앉고 싶어.", "sad"),
    L(HU, "명절에 다 그렇지 뭐. 금방 올게.", "normal"),
    L(N, "그날 장부에는 '설날, 일한 시간 열여섯 시간, 손등 화상'이라고 적었어요."),
])
s_surgery = scene("어머님 수술비", "hospital", [SY, MIL], mood="sad", when="3년 전", flashback=True, lying=[MIL], lines=[
    L(N, "삼 년 전, 시어머니가 쓰러지셔서 급히 수술을 하셨어요."),
    L(N, "시동생네는 형편이 어렵다고 했고, 시누이는 전화를 받지 않았어요."),
    L(MIL, "선영아, 병원비는… 걱정 마라. 애들이 알아서 하겠지.", "sad", {SY: "sad"}),
    L(SY, "네, 어머님. 걱정 마시고 푹 주무세요.", "happy"),
    dict(L(N, "저는 그날 원무과에서, 결혼 전부터 모은 적금을 깨서 팔백만 원을 냈어요."), sfx="ding"),
    L(SY, "어머님 수술비 팔백만 원. 어머님께는 비밀.", "cry"),
])
s_bank = scene("은행 창구", "street", [SY], mood="tense", when="2년 전", lines=[
    L(N, "이 년 전 봄, 은행에 갔다가 창구 앞에서 걸음을 멈췄어요."),
    L(MIL, "지은아, 보증금 오천이면 되지? 형님네는 모르게 해라.", "normal", {SY: "shock"}),
    L(DS, "어머님, 고마워요. 형님은 알면 서운해하실 거예요.", "happy"),
    dict(L(SY, "오천만 원… 수술비 낼 땐 형편이 어렵다더니.", "shock"), sfx="thud"),
    L(N, "그날 저는 집에 와서 장부에 날짜를 적었어요. 삼월 십사일, 동서네 보증금 오천만 원."),
])
scene("남편과의 다툼", "room_night", [SY, HU], mood="tense", when="1년 전", lines=[
    L(N, "작년 설날이 끝난 밤, 처음으로 남편에게 장부 얘기를 꺼냈어요."),
    L(SY, "정우 씨, 나 십 년 동안 명절마다 혼자 일했어. 당신은 알아?", "sad", {HU: "think"}),
    L(HU, "알지. 근데 엄마한테 그 정도는 해 드려야지. 맏며느리잖아.", "normal", {SY: "angry"}),
    L(SY, "맏며느리는 사람 아니야? 동서는 설거지 한 번 안 했어.", "angry"),
    L(HU, "명절에 싸우지 말자. 그냥 넘어가.", "angry", {SY: "cry"}),
    L(N, "그날 장부에는 처음으로 숫자가 아닌 말을 적었어요. '그냥 넘어가라는 말, 열 번째.'"),
])
scene("추석 전날 장보기", "mart", [SY], mood="calm", when="올해 추석 전날", lines=[
    L(N, "그리고 올해 추석 전날, 저는 또 혼자 마트에서 카트 두 대를 밀고 있었어요."),
    L(DS, "형님, 저 오늘 좀 늦어요. 네일 예약이 있어서요.", "happy", {SY: "sad"}),
    L(SY, "응, 그래. 내일 아침엔 와서 좀 도와줘.", "sad"),
    L(N, "계산대에서 찍힌 금액은 오십팔만 원. 저는 그 영수증도 장부에 붙였어요."),
])
s_notice = scene("차례비 통보", "kitchen", [SY, MIL, DS], mood="tense", when="추석 당일", lines=[
    L(MIL, "선영아, 올해 차례비는 네가 다 내라. 동서는 형편이 어렵다잖니.", "angry", {SY: "sad"}),
    L(DS, "형님, 죄송해요. 요즘 저희가 좀 빠듯해서요.", "sad", {SY: "think"}),
    L(N, "그 말을 하는 동서의 팔에는, 백만 원이 넘는다는 새 가방이 걸려 있었어요."),
    L(SIL, "새언니, 맏며느리가 그 정도는 해야지. 우리 엄마 힘든 거 안 보여?", "angry", {SY: "sad"}),
    L(SY, "…알겠어요, 어머님. 그 전에 하나만 보여 드릴게요.", "angry", {MIL: "surprised"}),
])
s_ledger = scene("장부", "jesa", [SY, MIL, DS, SIL], mood="tense", lines=[
    dict(L(SY, "어머님, 이 장부 한번 보세요.", "angry", {MIL: "shock", DS: "surprised"}), sfx="thud"),
    L(SY, "십 년 동안 명절 장보기 영수증이에요. 일한 시간, 어머님 용돈, 제사비까지 다 있어요.", "normal"),
    L(SY, "첫 추석, 사십삼만 원에 열네 시간. 오 년 전 설날, 열여섯 시간에 손등 화상.", "sad", {MIL: "think"}),
    L(DS, "형님… 그 화상, 저 그날 거실에서 봤어요. 그냥 모른 척했어요.", "sad", {SY: "sad"}),
    L(SY, "합계 천팔백만 원. 일한 시간은 이백팔십 시간이에요.", "sad", {SIL: "shock"}),
    L(SIL, "새언니, 이걸 다 적었어? 무섭다, 진짜.", "angry", {SY: "sad"}),
    L(MIL, "며느리가 시집 살림을 계산해? 내가 너를 그렇게 가르쳤니?", "angry", {SY: "sad"}),
    L(SY, "계산하려고 쓴 거 아니에요. 제가 버틴 걸 잊지 않으려고 쓴 거예요.", "cry"),
])
s_deposit = scene("오천만 원", "living", [SY, MIL, DS, SIL], mood="tense", lines=[
    L(SY, "그리고 여기, 이 년 전 삼월 십사일.", "angry", {DS: "shock"}),
    dict(L(SY, "동서네 아파트 보증금 오천만 원. 어머님이 몰래 보태 주셨죠?", "angry", {MIL: "shock", DS: "shock"}), sfx="thud"),
    L(SIL, "엄마, 그거 진짜야? 나한텐 돈 없다고 했잖아!", "angry", {MIL: "shock"}),
    L(DS, "형님, 그건… 어머님이 먼저 주신다고 하셔서요.", "sad"),
    L(MIL, "그건… 지은이네가 집도 없이 사는 게 안쓰러워서 그랬다.", "sad", {SY: "cry"}),
    L(SY, "어머님, 저희도 전세 살아요. 그래도 저는 한 번도 손 벌린 적 없어요.", "cry", {MIL: "sad"}),
    L(SY, "형편이 어려운 동서가 보증금을 받는 동안, 저는 차례비를 다 냈어요.", "cry", {MIL: "sad"}),
    L(N, "거실에 있던 누구도, 한참 동안 말을 하지 못했어요."),
])
s_husband = scene("남편의 첫마디", "yard", [HU, FIL, MIL], mood="hope", lines=[
    L(N, "그때, 마당에서 담배를 피우던 남편이 들어왔어요."),
    L(HU, "엄마, 이건 아니에요. 십 년 동안 저도 모른 척했어요. 제가 제일 나빴어요.", "angry", {MIL: "shock"}),
    L(FIL, "그만들 해라. 장부는 내가 다 봤다.", "angry", {MIL: "surprised", HU: "surprised"}),
    L(FIL, "앞으로 명절은 세 집이 돌아가며 지내고, 비용은 삼 등분이다. 이의 있는 사람?", "normal"),
    L(MIL, "여보, 당신까지 왜 그래요. 며느리 앞에서 내 체면은요.", "angry", {FIL: "angry"}),
    L(FIL, "체면? 십 년 동안 며느리 손등이 데는 동안 당신 체면은 어디 있었소.", "angry", {MIL: "sad"}),
    L(HU, "없어요, 아버지. 선영아, 미안하다. 진짜 미안해.", "cry"),
    L(N, "결혼하고 처음으로, 남편이 제 편에 섰어요."),
])
s_back = scene("장부 맨 뒷장", "room", [MIL], mood="sad", when="그날 밤 · 시어머니", lines=[
    L(N, "그날 밤, 시어머니는 혼자 방에서 그 장부를 끝까지 넘겨 보셨대요."),
    L(MIL, "맨 뒷장에 이건 뭐냐… 어머님 수술비 팔백만 원?", "surprised"),
    dict(L(MIL, "어머님께는 비밀… 선영이가 냈던 거야? 나는 정민이가 낸 줄 알았는데.", "shock"), sfx="ding"),
    L(MIL, "내가 형편 어렵다고 감싸던 애들은 한 푼도 안 냈는데…", "cry"),
    L(MIL, "이 바보 같은 애가, 그걸 삼 년이나 말을 안 했어.", "cry"),
    L(N, "장부 맨 마지막 줄에는, 제가 그날 밤 써 둔 한 줄이 있었어요."),
    L(SY, "어머님, 저는 어머님 미워서 이걸 쓴 게 아니에요. 언젠가 제 편이 되어 주실까 봐 썼어요.", "sad"),
])
s_sorry = scene("어머님의 앞치마", "kitchen", [SY, MIL, DS], mood="hope", when="다음 날 아침", lines=[
    L(N, "다음 날 새벽, 부엌에 나가 보니 시어머니가 앞치마를 두르고 계셨어요."),
    L(MIL, "선영아, 오늘 아침은 내가 한다. 너는 앉아 있어.", "sad", {SY: "surprised"}),
    L(MIL, "수술비… 왜 말 안 했니. 내가 너한테 십 년 동안 무슨 짓을 한 거냐.", "cry", {SY: "cry"}),
    L(SY, "어머님, 저는 그냥 어머님이 빨리 나으시길 바랐어요.", "cry"),
    L(DS, "형님, 저도 죄송해요. 보증금은 조금씩이라도 갚을게요.", "sad", {SY: "sad"}),
    L(MIL, "미안하다, 선영아. 내가 정말 미안하다.", "cry", {SY: "cry"}),
    L(SY, "어머님, 장부 맨 마지막 줄 읽으셨어요?", "cry", {MIL: "cry"}),
    L(MIL, "그래. 이제부터는 내가 네 편이다. 늦어서 미안하다.", "cry", {SY: "cry"}),
])
scene("다음 설날", "jesa", [SY, MIL, DS, HU], mood="warm", when="다음 해 설날", lines=[
    L(N, "다음 해 설날은 동서네에서 지냈어요. 처음으로, 저는 손님이었죠."),
    L(DS, "형님, 앉아 계세요. 오늘은 제가 다 할게요.", "happy", {SY: "happy"}),
    L(MIL, "선영아, 이 전 좀 먹어 봐라. 내가 부친 거다. 간 맞냐?", "happy", {SY: "happy"}),
    L(SY, "네, 어머님. 딱 맞아요.", "happy"),
    L(HU, "올해 장부엔 뭐라고 적을 거야?", "happy", {SY: "happy"}),
    L(SY, "일한 시간 영 시간. 웃은 시간은… 다 못 셀 것 같아.", "happy"),
])
scene("여러분께", "room_night", [SY], mood="warm", lines=[
    L(N, "그 초록색 장부는 지금 장롱 맨 위에 있어요. 다시 꺼낼 일은 없을 것 같아요."),
    L(N, "여러분이라면 이 장부를 꺼내셨을까요? 아니면 끝까지 참으셨을까요?"),
    L(SY, "명절마다 혼자 부엌에 계신 분이 있다면, 오늘은 꼭 옆에 서 주세요.", "happy"),
    L(N, "여러분의 생각을 댓글로 들려주세요. 이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "명절마다 며느리만 일 시킨 시어머니, 이번 추석에 며느리가 내민 10년 치 장부 한 권"
DESC_SHORT = "10년 동안 명절마다 혼자 부엌을 지킨 맏며느리. 차례비까지 다 내라는 시어머니 앞에 며느리가 장부 한 권을 내밀었습니다. 그 안에는 동서네 보증금과, 아무도 몰랐던 수술비 기록이 있었습니다.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #사이다사연 #감동사연 #며느리 #시어머니 #명절 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "holiday-ledger",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Leda",
    "cast": {
        SY: {"name": "맏며느리 선영", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#00897b", "hair": "bun", "hair_color": "#2e2420", "skin": "#f8d6ba"},
        MIL: {"name": "시어머니", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#8d6e63", "hair": "bun", "hair_color": "#bdb5ad", "skin": "#eec4a2"},
        FIL: {"name": "시아버지", "gvoice": "ko-KR-Chirp3-HD-Rasalgethi", "color": "#546e7a", "hair": "short", "hair_color": "#d6d0ca", "accessory": "glasses"},
        HU: {"name": "남편 정우", "gvoice": "ko-KR-Chirp3-HD-Achird", "color": "#3949ab", "hair": "short", "hair_color": "#1f1a18"},
        DS: {"name": "동서 지은", "gvoice": "ko-KR-Chirp3-HD-Zephyr", "color": "#ec407a", "hair": "long", "hair_color": "#6d4c41", "accessory": "bow"},
        SIL: {"name": "시누이 정희", "gvoice": "ko-KR-Chirp3-HD-Pulcherrima", "color": "#ffa000", "hair": "short", "hair_color": "#3b2a20", "accessory": "glasses"},
    },
    "scenes": S,
    # 0:00 하이라이트: 장부를 내미는 순간과 5천만 원 (수술비 반전은 숨김)
    "teaser": [[s_open, 0, 1], [s_ledger, 0, 1], [s_deposit, 1, 3]],
    "shorts_speed": 1.25,
    "shorts": [
        # 완결형 1: 장부를 내미는 순간 → 십 년 → 공개 → 5천만 원 → 남편·시아버지 → 수술비 → 사과
        {"format": "full", "speed": 1.0,
         "clips": [[s_ledger, 0, 1], [s_open, 0, 2], [s_notice, 2, 4], [s_ledger, 1, 8], [s_deposit, 1, 8], [s_husband, 1, 7], [s_back, 1, 4], [s_sorry, 2, 4], [s_sorry, 5, 8]],
         "hook": "어머님, 이 장부\n한번 보세요",
         "hook_who": SY, "hook_emotion": "angry", "hook_tone": "red", "hook_prop": {"type": "ledger", "text": "합계 1,800만 원"},
         "cta_line": "며느리의 십 년, 더 긴 이야기는 아래 본편에서 들려 드릴게요.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"어머님, 이 장부 한번 보세요\" #시니어사연 #사이다사연 #며느리 #시어머니 #명절 #인생이야기",
         "description": DESC_SHORT},
        # 완결형 2: 보증금 폭로로 시작 → 은행 창구 → 차례비 통보 → 공개 → 남편 → 사과
        {"format": "full", "speed": 1.0,
         "clips": [[s_deposit, 1, 2], [s_bank, 0, 5], [s_notice, 0, 5], [s_ledger, 0, 3], [s_deposit, 2, 8], [s_husband, 1, 8], [s_back, 2, 5], [s_sorry, 2, 3], [s_sorry, 5, 8]],
         "hook": "동서네 보증금\n오천만 원",
         "hook_who": DS, "hook_emotion": "shock", "hook_tone": "gold", "hook_prop": {"type": "ledger", "text": "보증금 5천만"},
         "cta_line": "이 가족의 이야기 전체는 아래 본편에서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"동서네 보증금 오천, 어머님이 보태 주셨죠?\" #시니어사연 #사이다사연 #며느리 #동서 #시어머니",
         "description": DESC_SHORT},
        # 완결형 3: 감동형 — 수술비 비밀로 시작 → 첫 명절 → 장부 쓴 밤 → 공개 → 맨 뒷장 → 앞치마 → 설날
        {"format": "full", "speed": 1.0,
         "clips": [[s_back, 2, 5], [s_surgery, 0, 6], [s_open, 0, 3], [s_ledger, 1, 5], [s_ledger, 7, 8], [s_husband, 1, 2], [s_husband, 5, 7], [s_back, 5, 7], [s_sorry, 0, 8]],
         "hook": "어머님 수술비\n팔백만 원의 비밀",
         "hook_who": MIL, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "ledger", "text": "어머님께는 비밀"},
         "cta_line": "며느리가 십 년 동안 쓴 장부, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"이 바보 같은 애가 그걸 삼 년이나 말을 안 했어\" #시니어사연 #감동사연 #며느리 #시어머니 #눈물주의",
         "description": DESC_SHORT},
        # 예고형: 장부를 내미는 순간까지
        {"clips": [[s_notice, 0, 5], [s_ledger, 0, 1]], "hook": "차례비 다 내라는\n시어머니",
         "hook_who": MIL, "hook_emotion": "angry", "hook_tone": "red", "hook_prop": {"type": "ledger", "text": "10년 치 장부"},
         "end_text": "장부에 적힌 비밀은 본편에서 ▶",
         "title": "\"올해 차례비는 네가 다 내라\" #시니어사연 #사이다사연 #며느리"},
    ],
    "thumbnail": {
        "text": "며느리가 내민\n10년 치 장부",
        "highlight": "10년 치 장부",
        "badge": "명절 사이다",
        "variants": [
            {"style": "story", "tone": "red", "face": [MIL, "shock"], "prop": {"type": "ledger", "text": "합계 1,800만 원"}},
            {"style": "story", "tone": "gold", "face": [DS, "shock"], "text": "동서네 보증금\n오천만 원", "highlight": "오천만 원",
             "badge": "들통", "prop": {"type": "ledger", "text": "보증금 5천만"}},
            {"style": "story", "tone": "blue", "face": [MIL, "cry"], "text": "장부 맨 뒷장의\n비밀", "highlight": "비밀",
             "badge": "눈물 주의", "prop": {"type": "ledger", "text": "어머님께는 비밀"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“어머님, 이 장부 한번 보세요”… 10년 명절 혼자 일한 며느리가 차례상 앞에 내민 것",
                           "차례비까지 며느리에게 떠넘긴 시어머니, 장부 맨 뒷장을 보고 무너졌다"],
        "description": "“올해 차례비는 네가 다 내라. 동서는 형편이 어렵다잖니.” 10년 동안 명절마다 혼자 부엌을 지킨 맏며느리 선영. 새 명품 가방을 든 동서 앞에서 차례비까지 떠넘겨진 날, 선영은 차례상 앞에 낡은 장부 한 권을 내려놓습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 이 장부를 꺼내셨을까요? 아니면 끝까지 참으셨을까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #사이다사연",
        "tags": ["사연", "시니어사연", "사이다 사연", "감동 사연", "며느리", "시어머니", "동서", "명절", "차례", "장부", "고부갈등", "인생이야기", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-27T18:00:00+09:00",
        "pinned_comment": "여러분이라면 이 장부를 꺼내셨을까요? 아니면 끝까지 참으셨을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-27T18:10:00+09:00", "2026-10-28T12:00:00+09:00", "2026-10-29T12:00:00+09:00", "2026-10-29T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
