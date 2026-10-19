"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 비 오는 교문 앞에서 치매 엄마를 찾는 장면(앞당김) → 30년 전 비 오는 날의 원망 → 비만 오면 사라지는 엄마
→ 요양원 갈등 → 엄마 옛 동료가 밝힌 그날의 사고(엄마 시점 회상) → 옷장 속 노란 우산 → 같은 교문에서 30년 만의 마중"""
import json
J, M, YM, JK, H, Y, YY, DR, FM, N = "jiwon", "mom", "mom_young", "jiwon_kid", "sanghun", "youngsook", "youngsook_young", "doctor", "minjimom", "narrator"


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


s_open = scene("비 오는 교문", "schoolgate", [J, M], mood="tense", when="현재", weather="rain", lines=[
    L(N, "치매를 앓는 엄마가 또 사라졌어요. 그날도 하늘에서 비가 쏟아지고 있었습니다."),
    dict(L(J, "엄마! 여기서 뭐 해! 온 동네를 다 뒤졌잖아!", "shock", {M: "surprised"}), sfx="thud"),
    L(M, "쉿, 조용히 해요. 우리 딸 곧 나와요. 비 오잖아요.", "happy"),
    L(J, "엄마, 내가 지원이야. 나 마흔둘이야.", "cry", {M: "think"}),
    L(M, "우리 지원이는 아홉 살이에요. 우산 없이 기다리면 감기 걸려요.", "sad", {J: "cry"}),
    L(N, "엄마 손에는 처음 보는 낡은 노란 우산이 꼭 쥐여 있었어요."),
    L(N, "그 우산이 삼십 년 전 어느 비 오는 날에 멈춰 있었다는 걸, 저는 그때 몰랐습니다."),
])
scene("진단", "hospital", [J, M, DR], mood="calm", when="1년 전", lines=[
    L(N, "엄마가 치매 진단을 받은 건 일 년 전이었어요."),
    L(DR, "최근 기억부터 사라지실 거예요. 오래된 기억은 오히려 더 선명해지기도 합니다.", "normal", {J: "sad"}),
    L(DR, "날씨나 소리 같은 게 옛 기억을 깨우기도 해요. 잘 지켜봐 주세요.", "think", {J: "think"}),
    L(J, "오래된 기억이요? 엄마는 옛날 얘기를 거의 안 하시는 분인데요.", "think"),
    L(M, "지원아, 오늘 비 온다더라. 우산 챙겼니?", "happy", {J: "think"}),
    L(J, "엄마는 또 우산 타령이야. 하늘 맑잖아.", "angry", {M: "sad"}),
    L(N, "엄마는 평생 비 소식만 들리면 저한테 전화를 했어요. 그게 저는 늘 이상하게 거슬렸죠."),
])
s_kidgate = scene("기다린 아이", "schoolgate", [JK, FM], mood="sad", when="30년 전", flashback=True, weather="rain", lines=[
    L(N, "초등학교 3학년, 갑자기 소나기가 쏟아진 날이었어요."),
    L(FM, "지원아, 아줌마 우산 같이 쓰고 갈래? 민지랑 같이 가자.", "happy", {JK: "sad"}),
    L(JK, "괜찮아요. 우리 엄마도 올 거예요. 꼭 온다고 했어요.", "happy"),
    L(N, "친구 엄마들이 하나둘 우산을 펼쳐 들고 떠났어요. 교문 앞에는 저 혼자 남았죠."),
    L(JK, "엄마… 왜 안 와. 벌써 깜깜해졌어.", "cry"),
    L(N, "결국 저는 두 시간을 기다리다, 비를 쫄딱 맞고 혼자 집까지 걸어갔어요."),
])
s_lie = scene("깜빡했어", "kitchen", [JK, YM], mood="tense", when="30년 전 · 그날 밤", flashback=True, lines=[
    L(N, "엄마는 밤 열 시가 넘어서야 들어왔어요. 저는 열이 펄펄 끓고 있었죠."),
    L(JK, "엄마 왜 안 왔어! 다른 엄마들은 다 왔단 말이야!", "angry", {YM: "sad"}),
    dict(L(YM, "미안해, 지원아. 엄마가… 깜빡했어.", "sad", {JK: "shock"}), sfx="thud"),
    L(JK, "깜빡했다고? 나 두 시간이나 기다렸어. 엄마 미워!", "cry", {YM: "cry"}),
    L(YM, "다음엔 꼭 갈게. 엄마가 정말 미안해.", "cry"),
    L(N, "그날 엄마가 왜 벽을 짚고 걸었는지, 저는 열에 들떠서 보지 못했어요."),
    L(N, "그 뒤로 엄마는 한 번도 교문에 오지 않았고, 저도 다시는 기다리지 않았습니다."),
])
scene("운동회", "park", [JK, YM], mood="calm", when="29년 전", flashback=True, lines=[
    L(N, "이듬해 가을 운동회. 엄마는 그날만큼은 일찍 와서 맨 앞에 앉아 있었어요."),
    L(JK, "엄마! 다음이 엄마랑 손잡고 달리기야. 빨리 나와!", "happy", {YM: "sad"}),
    L(YM, "지원아, 엄마는… 달리기는 못 해. 이모랑 뛰고 와.", "sad"),
    dict(L(JK, "왜? 다른 엄마들은 다 뛰잖아. 엄마는 맨날 못 한대!", "angry", {YM: "sad"}), sfx="thud"),
    L(YM, "미안해. 대신 엄마가 여기서 제일 크게 응원할게.", "sad"),
    L(JK, "필요 없어. 엄마는 맨날 미안하대.", "cry", {YM: "cry"}),
    L(N, "그날 엄마는 혼자 돗자리에 앉아, 무릎을 오래 주무르고 있었어요."),
    L(N, "저는 그게 부끄러워서, 끝날 때까지 한 번도 엄마 쪽을 보지 않았습니다."),
])
scene("비 소식 전화", "office", [J], mood="calm", when="5년 전", lines=[
    L(N, "어른이 되고 나서도, 비 소식이 있는 날이면 어김없이 엄마 전화가 왔어요."),
    L(M, "지원아, 오후에 비 온대. 우산 챙겼어?", "happy"),
    L(J, "엄마, 나 서른일곱이야. 회의 중이니까 끊어.", "angry"),
    L(M, "그래, 그래. 비 맞지 말고. 감기 걸려.", "sad"),
    L(J, "어릴 땐 한 번도 안 와 놓고, 이제 와서 왜 그러는지 모르겠어.", "think"),
    L(N, "저는 엄마의 그 전화가, 늦게 와서 하는 생색 같았어요."),
])
scene("한집에 살기", "living", [J, H, M], mood="calm", when="1년 전", lines=[
    L(N, "진단을 받고, 저는 남편과 상의해서 엄마를 우리 집으로 모셨어요."),
    L(H, "어머니, 이 방 쓰세요. 창문 쪽이라 해가 잘 들어요.", "happy", {M: "happy"}),
    L(M, "고마워요. 그런데 우산은 어디 둬요? 현관에 있어야 하는데.", "think", {J: "think"}),
    L(J, "엄마, 짐 정리하는데 우산 얘기부터 해?", "angry"),
    L(H, "괜찮아. 현관에 우산꽂이 하나 두자. 어머니 편하시게.", "happy", {M: "happy"}),
    L(N, "그때만 해도 엄마는 대부분의 날을 또렷하게 보냈어요. 비 오는 날만 빼고요."),
])
scene("비만 오면", "room_night", [J, M], mood="tense", when="현재", weather="rain", lines=[
    L(N, "그런데 올여름 장마가 시작되자, 엄마가 변하기 시작했어요."),
    dict(L(M, "몇 시예요? 네 시 넘었어요? 우리 딸 학교 끝날 시간인데!", "shock", {J: "surprised"}), sfx="ding"),
    L(J, "엄마, 지금 새벽 두 시야. 어디 가려고 그래.", "surprised"),
    L(M, "놔요! 비 오잖아요. 우리 지원이 우산이 없어요.", "angry", {J: "cry"}),
    L(J, "엄마, 내가 지원이라니까. 나 여기 있잖아!", "cry"),
    L(M, "아줌마는 누군데 자꾸 우리 딸 이름을 불러요?", "think", {J: "cry"}),
    L(N, "비만 오면 엄마는 신발도 신지 않고 문을 열고 나가려 했어요."),
])
scene("요양원 상담", "cafe", [J, H], mood="tense", lines=[
    L(H, "여보, 요양원 상담 다녀왔어? 너무 혼자 다 하려고 하지 마.", "sad", {J: "sad"}),
    L(J, "보내야 할 것 같아. 나도 이제 한계야.", "cry"),
    L(J, "웃기지? 엄마는 나 기다릴 때 한 번도 안 왔는데, 나는 매일 엄마를 찾으러 다녀.", "angry", {H: "sad"}),
    L(H, "어머니가 그날 왜 못 오셨는지, 한 번이라도 물어본 적 있어?", "think", {J: "surprised"}),
    L(J, "깜빡했대. 그게 다야. 삼십 년 동안 그 말뿐이었어.", "angry"),
    L(H, "깜빡한 사람이 삼십 년 동안 비 오는 날마다 전화를 해?", "think", {J: "think"}),
    L(J, "…생각해 보니 그날 이후로, 엄마는 한 번도 이유를 말한 적이 없어.", "think", {H: "sad"}),
])
s_aunt = scene("영숙 이모", "street", [J, Y], mood="sad", lines=[
    L(N, "며칠 뒤, 엄마가 옛날에 일하던 시장에 들렀다가 영숙 이모를 만났어요."),
    L(Y, "어머, 지원이 아니니? 엄마는 좀 어떠시고?", "surprised", {J: "sad"}),
    L(J, "요즘은 비만 오면 저를 데리러 학교에 가겠대요. 아홉 살 저를요.", "sad"),
    L(Y, "아이고… 그날 일을 아직도 못 놓았구나.", "cry", {J: "think"}),
    L(J, "그날이요? 이모, 그날 엄마가 깜빡했다고 했는데요.", "think"),
    dict(L(Y, "깜빡하긴! 네 엄마 그날 오토바이에 치였어. 너 우산 갖다주러 가다가.", "angry", {J: "shock"}), sfx="thud"),
    L(J, "치였다고요? 엄마가요?", "shock"),
])
s_truth = scene("엄마의 거짓말", "hospital", [YM, YY], mood="sad", when="30년 전 · 엄마의 그날", flashback=True, lying=[YM], lines=[
    L(N, "그날 엄마는 생선 가게 사장님 몰래 가게를 빠져나와, 우산 두 개를 들고 뛰었대요."),
    L(YY, "언니, 다리 뼈에 금이 갔대. 지원이한테 연락할까?", "cry", {YM: "sad"}),
    L(YM, "안 돼. 지원이한텐 절대 말하지 마.", "sad"),
    L(YM, "자기 우산 때문에 엄마가 다쳤다고 생각하면, 그 애 평생 비 오는 날이 무서울 거야.", "cry", {YY: "cry"}),
    L(YY, "그럼 뭐라고 해. 애가 두 시간이나 기다렸다며.", "sad"),
    L(YM, "깜빡했다고 해야지. 나쁜 엄마 하는 게 낫지.", "cry"),
    L(N, "엄마는 그날 깁스를 하고 가게를 잘렸고, 그 뒤로 평생 다리를 조금씩 절었어요."),
])
s_closet = scene("옷장 속 우산", "room", [J, H], mood="sad", lines=[
    L(N, "집에 오자마자 저는 엄마 옷장을 열었어요. 맨 안쪽에 비닐에 싸인 게 있었어요."),
    dict(L(J, "노란 우산… 이름표에 3학년 2반 강지원.", "shock", {H: "surprised"}), sfx="ding"),
    L(H, "살이 다 휘었네. 그날 들고 가셨던 우산인가 봐.", "sad"),
    L(J, "엄마는 이걸 삼십 년 동안 버리지도 못하고 갖고 있었던 거야.", "cry", {H: "sad"}),
    L(J, "다리를 절던 것도 나는 나이 들어서 그런 줄만 알았어.", "cry"),
    L(J, "비 오는 날마다 전화한 것도… 그날 못 온 게 미안해서였어.", "cry", {H: "cry"}),
])
scene("또 사라진 엄마", "night", [J, H], mood="tense", weather="rain", lines=[
    L(N, "그날 밤, 다시 비가 내렸고 엄마 방은 비어 있었어요."),
    L(H, "여보! 어머니가 안 계셔. 현관에 노란 우산도 없어!", "shock", {J: "surprised"}),
    L(J, "괜찮아. 어디 계신지 알아.", "sad"),
    L(N, "저는 현관에 남은 제 우산 하나만 들고, 빗속으로 뛰어나갔어요."),
    L(H, "경찰에 신고부터 해야 하는 거 아니야?", "surprised"),
    L(J, "아니. 이번엔 내가 마중 나갈게. 엄마가 삼십 년 동안 가려던 데로.", "cry", {H: "sad"}),
])
s_meet = scene("늦어서 미안해", "schoolgate", [J, M], mood="hope", weather="rain", lines=[
    L(N, "엄마는 역시, 그 교문 앞에 서 있었어요. 다리를 절면서 우산 두 개를 꼭 쥐고서요."),
    L(M, "지원아! 우리 지원이 맞지? 늦어서 미안해. 엄마가 우산 가져왔어.", "cry", {J: "cry"}),
    L(J, "엄마… 안 늦었어. 딱 맞춰 왔어.", "cry"),
    L(M, "다리가 좀 아파서 천천히 왔어. 많이 기다렸지?", "sad", {J: "cry"}),
    L(J, "아니야. 하나도 안 기다렸어. 엄마 오는 거 알았어.", "happy", {M: "happy"}),
    dict(L(M, "착하다, 우리 딸. 자, 노란 우산. 감기 걸리면 안 돼.", "happy", {J: "cry"}), sfx="ding"),
    L(J, "엄마, 이번엔 내가 씌워 줄게. 같이 집에 가자.", "happy", {M: "happy"}),
    L(N, "삼십 년 만에, 저는 엄마와 한 우산을 쓰고 그 길을 걸어서 돌아왔어요."),
])
scene("비 오는 날 네 시", "park", [J, M], mood="warm", when="한 달 뒤", lines=[
    L(N, "저는 요양원 상담을 취소하고, 낮에는 엄마를 주간보호센터에 모셔다 드려요."),
    L(J, "엄마, 오늘 오후에 비 온대. 네 시에 나랑 산책 갈까?", "happy", {M: "happy"}),
    L(M, "좋아요. 근데 아가씨, 우산은 챙겼어요?", "happy"),
    L(J, "응, 챙겼어. 엄마 거랑 내 거, 노란 우산까지 세 개.", "happy", {M: "happy"}),
    L(M, "아가씨는 우리 지원이를 많이 닮았네. 웃는 게 꼭 똑같아.", "happy", {J: "cry"}),
    L(N, "엄마는 이제 저를 자주 못 알아봐요. 그래도 비 오는 날 네 시만큼은 꼭 같이 걸어요."),
])
scene("여러분께", "living", [J, M], mood="warm", lines=[
    L(N, "그날 엄마의 '깜빡했어'는, 제 평생 들은 말 중에 가장 다정한 거짓말이었어요."),
    L(N, "혹시 여러분도, 이유를 묻지 않은 채 오래 미워한 사람이 있나요?"),
    L(J, "여러분이라면 교문 앞의 엄마에게 무슨 말을 하셨을까요? 댓글로 들려주세요.", "happy", {M: "happy"}),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "비 오는 날 한 번도 안 온 엄마, 치매에 걸린 뒤 매일 교문 앞에 서 있는 이유"
proj = {
    "title": TITLE,
    "slug": "rain-umbrella",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Callirrhoe",
    "cast": {
        J: {"name": "지원", "gvoice": "ko-KR-Chirp3-HD-Callirrhoe", "color": "#7e57c2", "hair": "long", "hair_color": "#2e2420", "skin": "#fbd9bd"},
        M: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#8d6e63", "hair": "bun", "hair_color": "#b5aea8", "skin": "#efc9a6"},
        YM: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Achernar", "color": "#a1887f", "hair": "bun", "hair_color": "#2e2420", "skin": "#f6cfae"},
        JK: {"name": "어린 지원", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#ffca28", "hair": "long", "hair_color": "#2e2420", "skin": "#ffe0c8", "accessory": "bow", "scale": 0.7},
        H: {"name": "상훈", "gvoice": "ko-KR-Chirp3-HD-Orus", "color": "#3f7cac", "hair": "short", "hair_color": "#1f1a18", "accessory": "glasses"},
        Y: {"name": "영숙 이모", "gvoice": "ko-KR-Chirp3-HD-Pulcherrima", "color": "#43a047", "hair": "bun", "hair_color": "#9e958d"},
        YY: {"name": "영숙 이모", "gvoice": "ko-KR-Chirp3-HD-Zephyr", "color": "#66bb6a", "hair": "short", "hair_color": "#3a2c22"},
        DR: {"name": "의사", "gvoice": "ko-KR-Chirp3-HD-Schedar", "color": "#eceff1", "hair": "short", "hair_color": "#2a2a2a", "accessory": "glasses"},
        FM: {"name": "민지 엄마", "gvoice": "ko-KR-Chirp3-HD-Sulafat", "color": "#ef6c00", "hair": "long", "hair_color": "#4a3020"},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (교문 마중 결말은 숨김)
    "teaser": [[s_lie, 1, 3], [s_aunt, 5, 7], [s_truth, 3, 4]],
    "shorts_speed": 1.25,
    "shorts": [
        {"clips": [[s_kidgate, 4, 6], [s_lie, 1, 5]], "hook": "비 오는 날\n끝내 안 온 엄마",
         "hook_who": JK, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "umbrella", "text": "3학년 2반"},
         "end_text": "엄마가 못 온 이유는 본편에서 ▶"},
        {"clips": [[s_open, 1, 7]], "hook": "치매 엄마가\n매일 서 있는 곳",
         "hook_who": M, "hook_emotion": "sad", "hook_tone": "red", "hook_prop": {"type": "umbrella", "text": "지원이 우산"},
         "end_text": "노란 우산의 비밀은 본편에서 ▶"},
        {"clips": [[s_truth, 1, 7]], "hook": "엄마의\n'깜빡했어'의 진실",
         "hook_who": J, "hook_emotion": "shock", "hook_tone": "gold", "hook_prop": {"type": "letter", "text": "깜빡했어"},
         "end_text": "그날의 진실은 본편에서 ▶"},
        {"clips": [[s_aunt, 5, 7], [s_closet, 1, 6]], "hook": "엄마 옷장 속\n휘어진 노란 우산",
         "hook_who": J, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "umbrella", "text": "3학년 2반"},
         "end_text": "두 사람의 마지막은 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "안 온 엄마\n교문의 비밀",
        "highlight": "교문의 비밀",
        "badge": "30년 오해",
        "variants": [
            {"style": "story", "tone": "blue", "face": [M, "cry"], "prop": {"type": "umbrella", "text": "3학년 2반"}},
            {"style": "story", "tone": "red", "face": [J, "shock"], "text": "엄마의 거짓말\n'깜빡했어'", "highlight": "'깜빡했어'",
             "badge": "눈물 주의", "prop": {"type": "letter", "text": "깜빡했어"}},
            {"style": "story", "tone": "gold", "face": [J, "cry"], "text": "30년 늦은\n엄마의 마중", "highlight": "엄마의 마중",
             "badge": "끝까지 보세요", "prop": {"type": "umbrella", "text": "지원이 우산"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“엄마가 깜빡했어”… 30년 전 비 오는 날, 엄마가 끝내 교문에 못 온 진짜 이유",
                           "치매 엄마가 비만 오면 사라졌다, 교문 앞에서 노란 우산을 들고"],
        "description": "“엄마가… 깜빡했어.” 초등학교 3학년 비 오는 날, 두 시간을 기다려도 오지 않은 엄마. 삼십 년 뒤 치매에 걸린 엄마는 비만 오면 노란 우산을 들고 그 교문 앞으로 사라집니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 교문 앞의 엄마에게 무슨 말을 하셨을까요? 이유를 묻지 못하고 오래 미워했던 가족 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #엄마 #감동사연",
        "tags": ["사연", "엄마", "감동 사연", "가족 사연", "치매", "치매 엄마", "엄마 사연", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "모녀", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-20T18:00:00+09:00",
        "pinned_comment": "이유를 모른 채 오래 서운했던 가족이 있으신가요? 나중에 알게 된 진심이 있다면 들려주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-21T12:00:00+09:00", "2026-10-21T19:00:00+09:00", "2026-10-22T12:00:00+09:00", "2026-10-22T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #엄마"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
