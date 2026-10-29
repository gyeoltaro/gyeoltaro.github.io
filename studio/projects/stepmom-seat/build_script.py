"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 딸(화자) 시점. 친엄마의 전화(앞당김) → 새엄마가 온 날 → 운동회 도시락 → 사춘기 → 상견례 → 친엄마와의 만남
→ 한복 취소 → 아빠의 한마디 → 복도에서 받은 상자 → 20년 치 편지 → 결혼식 아침 → 혼주석 → 집들이
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 20초~2분 40초, 가장 센 대사로 시작) + 예고형 1개"""
import json
SY, SM, BM, DAD, SK, GR, N = "seoyeon", "stepmom", "birthmom", "dad", "seoyeon_kid", "junho", "narrator"


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


s_open = scene("친엄마의 전화", "living", [SY, SM], mood="tense", when="결혼 한 달 전", lines=[
    L(N, "결혼식을 한 달 앞둔 밤, 이십 년 동안 연락이 없던 사람에게서 전화가 왔어요."),
    dict(L(BM, "서연아, 엄마야. 네 결혼식 혼주석에… 엄마가 앉고 싶어.", "sad", {SY: "shock", SM: "surprised"}), sfx="thud"),
    L(SY, "…친엄마요? 이제 와서요?", "shock"),
    L(N, "그 통화를 부엌에서 듣던 새엄마는, 아무 말 없이 행주만 접고 있었어요."),
    L(SY, "아줌마, 들었어요? 친엄마가 혼주석에 앉고 싶대요.", "think", {SM: "sad"}),
    L(SM, "…그래. 그럴 수 있지. 낳아 주신 분이잖아.", "sad"),
    L(N, "그리고 그 주에, 새엄마가 맞춰 두었던 한복을 조용히 취소했다는 걸 알게 됐습니다."),
    L(N, "이 이야기를 하려면, 제가 여덟 살이던 봄으로 돌아가야 해요."),
])
scene("새엄마가 온 날", "room", [SK, SM], mood="tense", when="22년 전", flashback=True, lines=[
    L(N, "여덟 살 봄, 아빠가 낯선 아줌마를 데려왔어요."),
    L(SM, "서연아, 안녕. 오늘부터 같이 살게 됐어. 정숙이라고 해.", "happy", {SK: "angry"}),
    L(SK, "아줌마는 우리 엄마 아니야! 엄마라고 안 부를 거야!", "angry", {SM: "sad"}),
    L(SM, "그래, 그럼 아줌마라고 불러. 대신 밥은 꼭 같이 먹자.", "happy"),
    L(SK, "…싫어. 아줌마 밥 안 먹어.", "sad", {SM: "sad"}),
    L(N, "그날 밤, 방문 앞에는 계란말이를 올린 밥상이 놓여 있었어요. 저는 몰래 다 먹었죠."),
])
scene("운동회 도시락", "park", [SK, SM], mood="calm", when="18년 전", flashback=True, lines=[
    L(N, "초등학교 마지막 운동회 날, 새엄마는 새벽부터 김밥을 쌌어요."),
    L(SM, "서연아, 김밥 먹자. 네가 좋아하는 햄 많이 넣었어.", "happy", {SK: "sad"}),
    L(SK, "애들 앞에서 크게 부르지 마. 그냥 우리 집 아줌마라고 했단 말이야.", "angry", {SM: "sad"}),
    L(SM, "그래, 알았어. 아줌마는 저기 나무 밑에 있을게.", "happy"),
    L(N, "새엄마는 운동회가 끝날 때까지 나무 밑에 혼자 앉아, 제 달리기를 보며 박수만 쳤어요."),
    L(SK, "…아줌마, 나 일등 했어. 봤어?", "happy", {SM: "happy"}),
    L(SM, "그럼, 봤지. 아줌마가 제일 크게 박수 쳤어.", "happy"),
])
scene("사춘기", "room_night", [SY, SM], mood="tense", when="14년 전", lines=[
    L(N, "중학생이 되고, 저는 더 날카로워졌어요."),
    L(SY, "아줌마가 뭔데 내 일에 간섭해? 진짜 엄마도 아니면서!", "angry", {SM: "sad"}),
    L(SM, "그래, 진짜 엄마는 아니지. 그래도 밥은 먹고 자.", "sad"),
    L(SY, "우리 진짜 엄마는 나를 보고 싶어 하지도 않는데, 아줌마가 왜 이래!", "cry", {SM: "cry"}),
    L(N, "그날 밤 새엄마 방에는 늦게까지 불이 켜져 있었어요. 누군가에게 편지를 쓰고 있었죠."),
    L(N, "저는 그 편지가 누구에게 가는 건지, 이십 년 동안 몰랐습니다."),
])
scene("졸업식", "classroom", [SY, SM], mood="sad", when="11년 전", flashback=True, lines=[
    L(N, "고등학교 졸업식 날, 아빠는 출장이었어요. 새엄마가 꽃다발을 들고 왔죠."),
    L(SM, "서연아, 졸업 축하해. 꽃 사 왔어.", "happy", {SY: "sad"}),
    L(SY, "친구들이 누구냐고 물어보잖아요. 그냥 저기 계세요.", "angry", {SM: "sad"}),
    L(SM, "그래. 그럼 사진만 한 장 찍을게. 멀리서.", "happy"),
    L(N, "새엄마는 강당 맨 뒤에서 까치발을 들고, 제 사진을 몇 장이나 찍었어요."),
    L(N, "그 사진들이 어디로 갔는지, 저는 결혼식 전날에야 알게 됐어요."),
])
scene("상견례", "cafe", [SY, SM, GR], mood="calm", when="두 달 전", lines=[
    L(N, "서른 살, 저는 결혼을 앞두고 상견례 자리에 앉았어요."),
    L(GR, "어머님, 처음 뵙겠습니다. 서연이한테 얘기 많이 들었어요.", "happy", {SM: "happy", SY: "think"}),
    L(SY, "아… 저희 새어머니세요.", "think", {SM: "sad"}),
    L(SM, "네, 서연이가 어릴 때부터 같이 살았어요. 잘 부탁드려요.", "happy"),
    L(N, "식사 내내, 새엄마는 웃으며 제 접시에 고기를 올려 줬어요. 저는 그 웃음이 왜 쓸쓸해 보였는지 몰랐어요."),
])
s_meet = scene("친엄마와의 만남", "street", [SY, BM], mood="tense", when="결혼 한 달 전", lines=[
    L(N, "전화를 받은 다음 날, 저는 이십 년 만에 친엄마를 만났어요."),
    L(BM, "서연아, 이렇게 컸구나. 엄마가… 미안하다.", "cry", {SY: "angry"}),
    L(SY, "이십 년 동안 연락 한 번 없다가, 왜 이제 와서요?", "angry"),
    L(BM, "엄마가 너무 아팠어. 빚도 많았고. 너를 데려갈 수가 없었어.", "sad", {SY: "think"}),
    L(SY, "아프셨으면 연락이라도 하시지. 저는 엄마가 저를 버린 줄 알았어요.", "cry", {BM: "cry"}),
    L(BM, "버린 게 아니야. 매일 생각했어. 그런데 너한테는 이미 좋은 사람이 있다고 들었어.", "sad", {SY: "surprised"}),
    L(BM, "결혼식 날 혼주석에 한 번만 앉고 싶어. 엄마로서 마지막 부탁이야.", "cry"),
    L(N, "저는 대답하지 못했어요. 그런데 이상하게, 새엄마 얼굴이 먼저 떠올랐어요."),
])
s_hanbok = scene("한복 취소", "living", [SY, SM], mood="tense", lines=[
    L(SM, "서연아, 혼주석은 친엄마 드려라. 낳아 주신 분이잖니.", "sad", {SY: "surprised"}),
    L(SY, "…아줌마 한복은요? 석 달 전에 맞췄잖아요.", "think"),
    dict(L(SM, "취소했어. 괜찮아. 나는 하객석에서 보면 돼.", "happy", {SY: "shock"}), sfx="thud"),
    L(SY, "아줌마는 끝까지 남이네요. 이럴 때도 그냥 비켜 주고.", "angry", {SM: "sad"}),
    L(SM, "남이라서 비켜 주는 게 아니야. 네 마음 편하라고 그러는 거야.", "sad"),
    L(SY, "내 마음이 왜 편해요? 이십 년을 같이 살았는데, 결혼식 날 하객석이라니.", "cry", {SM: "cry"}),
    L(SM, "서연아, 엄마는… 아니, 아줌마는 괜찮아. 정말이야.", "cry"),
    L(N, "저는 그 말에 대답도 안 하고 방문을 닫아 버렸어요. 서운한 건 저였는데, 왜 서운한지도 몰랐어요."),
])
scene("아빠의 한마디", "kitchen", [SY, DAD], mood="calm", when="그날 밤", lines=[
    L(DAD, "서연아, 아빠가 하나만 말할게.", "sad", {SY: "think"}),
    L(DAD, "정숙 씨가 그 한복 석 달 전에 맞춘 이유, 너 아니?", "think"),
    L(SY, "결혼식이니까 입으려고 맞춘 거겠죠.", "think"),
    L(DAD, "네 결혼식 날, 이십 년 만에 엄마 소리 한 번 들을까 해서 맞춘 거다. 저 사람이 그러더라.", "sad", {SY: "shock"}),
    L(DAD, "그래도 네 친엄마가 오고 싶어 하면, 자기는 빠지겠다고. 너 힘들지 않게.", "sad", {SY: "cry"}),
    L(SY, "아빠, 아줌마는 왜 한 번도 서운하다고 안 했어요?", "cry", {DAD: "sad"}),
    L(DAD, "서운한 걸 말하면 네가 미안해할까 봐. 그 사람은 이십 년 내내 그랬다.", "sad"),
])
s_box = scene("복도의 상자", "hallway", [SY, BM], mood="sad", when="결혼식 전날", lines=[
    L(N, "결혼식 전날 밤, 친엄마가 우리 아파트 복도까지 찾아왔어요."),
    L(BM, "서연아, 이거 받아. 엄마가 이십 년 동안 받은 거야.", "sad", {SY: "surprised"}),
    L(SY, "이게 뭐예요? 편지… 사진…?", "surprised"),
    dict(L(BM, "네 새엄마가 매년 보낸 편지야. 내가 어디 사는지 수소문해서, 한 해도 안 빠지고.", "cry", {SY: "shock"}), sfx="ding"),
    L(BM, "나는 이 사람 덕분에 너를 다 봤어. 운동회도, 졸업식도.", "cry"),
    L(SY, "졸업식 사진도… 이거 아줌마가 강당 뒤에서 찍은 거예요.", "cry", {BM: "sad"}),
    L(BM, "그래. 이 사람이 매년 편지 끝에 썼어. 언제든 보러 오셔도 된다고.", "cry"),
    L(BM, "그리고 서연이는 엄마를 미워하지 않게 키우겠다고.", "cry", {SY: "cry"}),
    L(BM, "그 자리는 내 자리가 아니야. 혼주석은 이 사람 거야.", "cry", {SY: "cry"}),
])
s_letters = scene("20년 치 편지", "room_night", [SY], mood="sad", when="그날 밤", lines=[
    L(N, "그날 밤, 저는 상자 속 편지를 하나씩 읽었어요."),
    L(SM, "서연이가 오늘 자전거를 처음 탔어요. 넘어져도 울지 않더라고요. 어머님 닮았나 봐요.", "happy"),
    L(SM, "서연이가 저를 아줌마라고 불러요. 괜찮아요. 언젠가 어머님을 만나도 미워하지 않게 키울게요.", "sad"),
    L(SM, "서연이가 대학에 붙었어요. 사진 보내 드려요. 언제든 보고 싶으시면 연락하세요.", "happy"),
    L(SM, "서연이가 오늘 저한테 진짜 엄마도 아니면서, 라고 했어요. 맞는 말이라 아무 말도 못 했어요.", "sad"),
    L(SM, "서연이 졸업식이었어요. 맨 뒤에서 찍어서 사진이 흐려요. 그래도 많이 컸죠.", "happy"),
    L(SY, "아줌마… 이걸 이십 년 동안 혼자…", "cry"),
    L(N, "편지 맨 마지막 장은, 석 달 전 날짜였어요. 서연이가 결혼해요. 혼주석은 어머님 자리로 비워 둘게요."),
])
s_morning = scene("결혼식 아침", "bridalroom", [SY, SM], mood="hope", when="결혼식 날", lines=[
    L(N, "결혼식 날 아침, 저는 신부 대기실에서 전화를 걸었어요."),
    L(SY, "아줌마… 한복 다시 입고 와 주세요. 대여점에 제가 다 말해 놨어요.", "cry", {SM: "surprised"}),
    L(SM, "서연아, 그래도 되니? 친엄마가…", "surprised"),
    L(SY, "친엄마가 그러셨어요. 그 자리는 아줌마 거라고.", "cry", {SM: "cry"}),
    L(SM, "…알았어. 금방 갈게. 울지 마, 화장 번진다.", "cry"),
    L(GR, "서연아, 장모님 오셨어. 한복 입으셨어.", "happy", {SY: "cry"}),
])
s_seat = scene("혼주석", "wedding", [SY, SM, BM], mood="warm", lines=[
    L(N, "식이 시작되기 직전, 한복을 입은 새엄마가 하객석 맨 뒤에 조용히 섰어요."),
    L(SY, "잠깐만요.", "normal", {SM: "surprised"}),
    dict(L(SY, "엄마, 여기 앉으세요. 여기가 엄마 자리예요.", "cry", {SM: "cry", BM: "cry"}), sfx="ding"),
    L(SM, "서연아… 지금 엄마라고 했니?", "cry"),
    L(SY, "이십 년 동안 못 한 말이에요. 엄마, 키워 줘서 고마워요.", "cry", {SM: "cry"}),
    L(SM, "아이고, 이 녀석. 이십 년 기다린 보람이 있네.", "cry", {SY: "cry"}),
    L(N, "하객석 한쪽에서, 친엄마가 눈물을 닦으며 가장 크게 박수를 쳐 주었어요."),
    L(BM, "고마워요, 정숙 씨. 우리 서연이 이렇게 키워 줘서.", "cry", {SM: "cry"}),
])
scene("집들이", "living", [SY, SM, BM], mood="warm", when="두 달 뒤", lines=[
    L(N, "신혼집 집들이에는 엄마가 두 분 오셨어요."),
    L(BM, "정숙 씨, 이 잡채 비법 좀 알려 줘요. 서연이가 이게 제일 맛있대요.", "happy", {SM: "happy"}),
    L(SM, "비법은 무슨요. 서연이가 어릴 때 시금치를 안 먹어서 조금만 넣었어요.", "happy"),
    L(SY, "엄마들, 둘이서 제 흉보는 거 다 들려요.", "happy", {SM: "happy", BM: "happy"}),
    L(SM, "서연아, 이번 주말엔 김밥 싸 갈게. 햄 많이 넣어서.", "happy", {SY: "happy"}),
    L(N, "저는 이제 두 분을 다 엄마라고 불러요. 한 분은 저를 낳아 주셨고, 한 분은 저를 키워 주셨어요."),
])
scene("여러분께", "park", [SY], mood="warm", lines=[
    L(N, "이십 년 동안 아줌마라고 불렀던 사람이, 이십 년 동안 저를 지켜 주고 있었어요."),
    L(N, "여러분이라면 혼주석에 누구를 앉히셨을까요? 낳아 준 엄마, 키워 준 엄마?"),
    L(SY, "곁에서 묵묵히 키워 준 분이 있다면, 오늘은 꼭 고맙다고 말해 주세요.", "happy"),
    L(N, "여러분의 생각을 댓글로 들려주세요. 이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "20년 동안 '아줌마'라 부른 새엄마, 결혼식 전날 친엄마가 건넨 상자를 열고 울었습니다"
DESC_SHORT = "여덟 살 때부터 20년 동안 새엄마를 '아줌마'라고만 불렀던 딸. 결혼식을 앞두고 친엄마가 혼주석에 앉고 싶다며 나타났고, 새엄마는 조용히 한복을 취소했습니다. 그리고 결혼식 전날, 친엄마가 상자 하나를 건넸습니다.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#감동사연 #시니어사연 #새엄마 #결혼식 #가족사연 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "stepmom-seat",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Kore",
    "cast": {
        SY: {"name": "서연", "gvoice": "ko-KR-Chirp3-HD-Kore", "color": "#fafafa", "hair": "long", "hair_color": "#3a2618", "skin": "#fbdcc4"},
        SM: {"name": "새엄마 정숙", "gvoice": "ko-KR-Chirp3-HD-Despina", "color": "#8e7cc3", "hair": "bun", "hair_color": "#4a3a32", "skin": "#f2cba8"},
        BM: {"name": "친엄마", "gvoice": "ko-KR-Chirp3-HD-Vindemiatrix", "color": "#90a4ae", "hair": "short", "hair_color": "#6d625a", "skin": "#eec4a2"},
        DAD: {"name": "아빠", "gvoice": "ko-KR-Chirp3-HD-Charon", "color": "#5d4037", "hair": "short", "hair_color": "#9e9a96", "accessory": "glasses"},
        SK: {"name": "어린 서연", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#f48fb1", "hair": "long", "hair_color": "#3a2618", "skin": "#ffe0c8", "accessory": "bow", "scale": 0.7},
        GR: {"name": "예비신랑 준호", "gvoice": "ko-KR-Chirp3-HD-Puck", "color": "#1e88e5", "hair": "short", "hair_color": "#222222"},
    },
    "scenes": S,
    # 0:00 하이라이트: 혼주석 요구와 한복 취소, 상자 (혼주석 결말은 숨김)
    "teaser": [[s_open, 1, 2], [s_hanbok, 2, 3], [s_box, 3, 4]],
    "shorts_speed": 1.25,
    "shorts": [
        # 완결형 1: 혼주석 장면으로 시작 → 20년 → 친엄마 → 한복 취소 → 상자 → 편지 → 혼주석
        {"format": "full", "speed": 1.0,
         "clips": [[s_seat, 2, 3], [s_open, 1, 5], [s_hanbok, 0, 7], [s_box, 1, 8], [s_letters, 1, 3], [s_letters, 6, 8], [s_morning, 1, 5], [s_seat, 2, 8]],
         "hook": "엄마, 여기가\n엄마 자리예요",
         "hook_who": SY, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "box", "text": "20년 치 편지"},
         "cta_line": "새엄마와 딸의 이십 년, 더 긴 이야기는 아래 본편에서 들려 드릴게요.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"엄마, 여기가 엄마 자리예요\" 20년 만에 처음 부른 이름 #감동사연 #새엄마 #결혼식 #가족사연 #인생이야기",
         "description": DESC_SHORT},
        # 완결형 2: 친엄마의 혼주석 요구로 시작 → 만남 → 한복 → 아빠 → 상자 → 혼주석
        {"format": "full", "speed": 1.0,
         "clips": [[s_open, 1, 3], [s_meet, 1, 8], [s_hanbok, 0, 4], [s_hanbok, 4, 7], [s_box, 1, 8], [s_morning, 1, 4], [s_seat, 1, 8]],
         "hook": "혼주석에 앉고 싶다는\n친엄마",
         "hook_who": BM, "hook_emotion": "sad", "hook_tone": "red", "hook_prop": {"type": "box", "text": "20년 치 편지"},
         "cta_line": "이 가족의 이야기 전체는 아래 본편에서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"혼주석에 엄마가 앉고 싶어\" 20년 만에 나타난 친엄마 #감동사연 #시니어사연 #친엄마 #새엄마 #결혼식",
         "description": DESC_SHORT},
        # 완결형 3: 편지로 시작하는 감동형 → 새엄마가 온 날 → 운동회 → 사춘기 → 상자 → 혼주석
        {"format": "full", "speed": 1.0,
         "clips": [[s_letters, 2, 3], [1, 1, 6], [2, 2, 5], [3, 1, 6], [4, 1, 5], [s_box, 3, 8], [s_letters, 1, 8], [s_seat, 2, 6]],
         "hook": "아줌마라고 불러도\n괜찮아요",
         "hook_who": SM, "hook_emotion": "sad", "hook_tone": "blue", "hook_prop": {"type": "letter", "text": "괜찮아요"},
         "cta_line": "새엄마가 보낸 이십 년 치 편지, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"아줌마라고 불러도 괜찮아요\" 새엄마가 20년 동안 몰래 쓴 편지 #감동사연 #새엄마 #가족사연 #눈물주의",
         "description": DESC_SHORT},
        # 예고형: 한복 취소까지
        {"clips": [[s_open, 1, 3], [s_open, 3, 5], [s_hanbok, 0, 3]], "hook": "말없이 한복을\n취소한 새엄마",
         "hook_who": SM, "hook_emotion": "sad", "hook_tone": "red", "hook_prop": {"type": "box", "text": "20년 치 편지"},
         "end_text": "상자 속 비밀은 본편에서 ▶",
         "title": "\"혼주석은 친엄마 드려라\" #감동사연 #새엄마 #결혼식"},
    ],
    "thumbnail": {
        "text": "20년 '아줌마'\n상자의 비밀",
        "highlight": "상자의 비밀",
        "badge": "눈물 주의",
        "variants": [
            {"style": "story", "tone": "gold", "face": [SY, "cry"], "prop": {"type": "box", "text": "20년 치 편지"}},
            {"style": "story", "tone": "red", "face": [BM, "sad"], "text": "혼주석에 앉겠다는\n친엄마", "highlight": "친엄마",
             "badge": "20년 만에", "prop": {"type": "box", "text": "20년 치 편지"}},
            {"style": "story", "tone": "blue", "face": [SM, "cry"], "text": "말없이 한복을\n취소한 새엄마", "highlight": "새엄마",
             "badge": "끝까지 보세요", "prop": {"type": "letter", "text": "괜찮아요"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“혼주석에 엄마가 앉고 싶어”… 20년 만에 나타난 친엄마, 새엄마는 말없이 한복을 취소했다",
                           "새엄마가 20년 동안 몰래 쓴 편지, 결혼식 전날 친엄마가 건넨 상자 속에 있었다"],
        "description": "“서연아, 엄마야. 네 결혼식 혼주석에 엄마가 앉고 싶어.” 여덟 살 때부터 20년 동안 새엄마를 '아줌마'라고만 불렀던 서연. 결혼식을 앞두고 연락이 끊겼던 친엄마가 나타나자, 새엄마는 석 달 전에 맞춘 한복을 조용히 취소합니다. 그리고 결혼식 전날, 친엄마가 상자 하나를 건넵니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 혼주석에 누구를 앉히셨을까요? 낳아 준 엄마, 키워 준 엄마? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #감동사연 #새엄마",
        "tags": ["사연", "감동 사연", "시니어사연", "새엄마", "친엄마", "결혼식", "혼주석", "가족 사연", "기른 정", "인생이야기", "사연 만화", "눈물 사연", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-31T18:00:00+09:00",
        "pinned_comment": "여러분이라면 혼주석에 누구를 앉히셨을까요? 낳아 준 엄마, 키워 준 엄마? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-31T18:10:00+09:00", "2026-11-01T12:00:00+09:00", "2026-11-02T12:00:00+09:00", "2026-11-02T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
