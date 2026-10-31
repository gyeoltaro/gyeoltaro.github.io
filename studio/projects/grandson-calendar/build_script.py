"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연, 14편)
구성: 딸(화자) 시점. 용돈 줄이자는 말(앞당김) → 3년 전 부탁 → 새벽 출근 → 놀이터 → 용돈 봉투 → 어린이집 첫날
→ 부부의 계산 → 용돈 줄이자 → 달력 한 장 → 병원(회상) → 엄마의 서러움 → 달력 뒷장 → 수술 날 → 일요일 공원
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 20초~2분 45초, 가장 센 대사로 시작) + 예고형 1개"""
import json
EJ, SJ, JH, HJ, DR, N = "eunji", "sunja", "junho", "hajun", "doctor", "narrator"


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


s_open = scene("용돈 줄이자", "living", [EJ, SJ, JH], mood="tense", when="올가을", lines=[
    L(N, "그날 저는 3년 동안 손주를 키워 준 친정엄마한테, 입에 담으면 안 되는 말을 하고 말았어요."),
    dict(L(EJ, "엄마, 이제 하준이 어린이집 가니까 용돈도 줄이자. 오십에서 삼십으로.", "normal", {SJ: "sad", JH: "think"}), sfx="thud"),
    L(SJ, "…그래. 그러자. 애 안 봐도 되니까.", "sad"),
    L(N, "엄마는 웃으며 대답했지만, 손에 든 찻잔이 가늘게 떨리고 있었어요."),
    L(N, "저는 그 떨림이 무슨 뜻인지 그때는 몰랐어요. 이 이야기를 하려면, 3년 전으로 돌아가야 해요."),
])
s_ask = scene("엄마한테 부탁한 날", "room", [EJ, SJ], mood="warm", when="3년 전", flashback=True, lines=[
    L(N, "3년 전, 하준이가 태어나고 제 육아휴직이 끝나갈 때였어요."),
    L(EJ, "엄마, 나 복직해야 해. 어린이집은 대기만 백 명이래. 엄마가 조금만 봐 주면 안 될까?", "sad", {SJ: "think"}),
    L(SJ, "내가 퇴직하고 이제 좀 쉬려던 참인데, 그래도 내 새끼가 부탁하는데 어쩌겠니.", "happy"),
    L(EJ, "진짜? 엄마 고마워. 대신 내가 매달 용돈 꼭 드릴게.", "happy", {SJ: "happy"}),
    L(SJ, "용돈은 무슨. 엄마가 하는 일에 값을 매기는 게 어디 있니.", "happy"),
    L(EJ, "그래도 받아. 안 받으면 나 부탁 못 해.", "sad"),
    dict(L(SJ, "그래, 알았다. 그럼 오십만 원만 받으마. 그 이상은 안 된다.", "happy"), sfx="ding"),
    L(N, "그렇게 엄마의 새로운 하루가 시작됐어요. 쉬려던 은퇴가 육아로 바뀐 날이었죠."),
])
scene("새벽 출근길", "street", [SJ, JH], mood="calm", when="3년 전 겨울", lines=[
    L(N, "엄마는 매일 아침 6시 반, 첫 지하철을 타고 우리 집으로 왔어요."),
    L(N, "저와 남편은 7시에 나가야 했거든요. 엄마는 우리가 나가기 전에 도착해야 했어요."),
    L(SJ, "에고, 새벽 공기가 차네. 우리 하준이 일어났으려나.", "happy"),
    L(N, "엄마는 오는 길에 항상 편의점 호빵이나 하준이 좋아하는 바나나우유를 샀어요."),
    dict(L(SJ, "이 바나나우유는 하준이 거니까 내 돈으로 사자. 용돈은 따로 모아야지.", "think"), sfx="ding"),
    L(JH, "장모님, 이렇게 일찍 오시면 힘드시잖아요. 저희가 하준이 데려다 드릴까요?", "sad", {SJ: "happy"}),
    L(SJ, "아니야. 애는 제 집에서 자야 잘 커. 내가 오는 게 낫지.", "happy"),
    L(N, "그때는 엄마가 왜 용돈을 따로 모은다고 했는지, 그냥 흘려들었어요."),
])
s_play = scene("놀이터의 할미", "park", [SJ, HJ], mood="warm", when="2년 전 봄", lines=[
    L(N, "엄마는 하준이를 업고 안고, 하루도 빠짐없이 놀이터에 나갔어요."),
    L(HJ, "할미! 할미! 미끄럼틀 또!", "happy", {SJ: "happy"}),
    L(SJ, "아이고 우리 강아지, 할미 무릎이 좀 아픈데… 그래도 한 번 더 타자.", "happy"),
    L(N, "엄마는 쪼그려 앉을 때마다 무릎을 한 번씩 짚고 일어났지만, 하준이 앞에서는 한 번도 내색하지 않았어요."),
    dict(L(HJ, "할미, 나 할미 제일 좋아. 엄마보다 더.", "happy", {SJ: "surprised"}), sfx="ding"),
    L(SJ, "에이, 그런 말 하면 엄마가 서운해하지. 엄마는 하준이 위해서 일하러 가는 거야.", "happy"),
    L(N, "그날 엄마의 일기장에는 이렇게 적혀 있었다고 해요. 오늘 하준이가 나를 제일 좋아한대. 이 맛에 산다."),
])
scene("용돈 봉투", "kitchen", [EJ, SJ, JH], mood="calm", when="2년 전", lines=[
    L(N, "매달 25일은 엄마한테 용돈 봉투를 드리는 날이었어요."),
    L(EJ, "엄마, 이거 이번 달 용돈. 항상 고마워.", "happy", {SJ: "happy"}),
    L(SJ, "그래, 고맙다. 근데 은지야, 이 돈 내가 쓸 데가 없어. 그냥 네가 가져가도 되는데.", "normal"),
    L(JH, "장모님, 받으세요. 저희가 그나마 이거라도 해야 마음이 편해요.", "happy", {SJ: "happy"}),
    L(SJ, "알았네, 알았어. 이 사람들이 하도 우겨서.", "happy"),
    L(N, "엄마는 봉투를 받자마자 가방 깊숙이 넣었어요. 저는 엄마가 그 돈으로 맛있는 걸 사 드시길 바랐죠."),
    L(N, "하지만 엄마는 한 번도 새 옷을 사 입지 않았어요. 늘 같은 점퍼였죠."),
    L(JH, "장모님, 요즘도 그 점퍼 입으시네요. 바꾸셔도 되는데.", "happy"),
    dict(L(SJ, "이게 얼마나 따뜻한데. 사람이 따뜻하면 됐지.", "happy"), sfx="ding"),
])
scene("어린이집 첫날", "schoolgate", [EJ, SJ, HJ], mood="hope", when="올가을", lines=[
    L(N, "그러던 올가을, 기다리던 어린이집 입소 연락이 왔어요."),
    L(EJ, "엄마! 드디어 하준이 어린이집 붙었어! 이제 엄마 쉬셔도 돼!", "happy", {SJ: "surprised"}),
    L(SJ, "…그래? 잘됐네. 잘됐다, 정말.", "happy"),
    L(HJ, "할미, 나 어린이집 가. 형아 됐어.", "happy", {SJ: "sad"}),
    L(SJ, "그래, 우리 하준이 이제 의젓한 형아네. 선생님 말씀 잘 듣고.", "happy"),
    L(N, "저는 신이 나서 하준이 가방을 챙기느라 엄마 표정을 못 봤어요."),
    dict(L(SJ, "이제 내가 할 일이 끝났네. 허, 이렇게 빨리 오다니.", "cry"), sfx="thud"),
    L(N, "제 눈에는 엄마가 홀가분해 보였는데, 지금 생각하면 엄마는 길을 잃은 사람 같았어요."),
])
scene("부부의 계산", "room_night", [EJ, JH], mood="tense", when="그날 밤", lines=[
    L(N, "그날 밤, 저와 남편은 가계부를 펴 놓고 앉았어요."),
    L(EJ, "자기야, 어린이집비에 학원 적금에, 우리 요즘 너무 빠듯하지 않아?", "sad", {JH: "think"}),
    L(JH, "그렇긴 한데, 장모님 용돈을 줄이는 건 좀 그렇지 않아?", "think"),
    L(EJ, "이제 하준이 안 봐 주시잖아. 엄마도 용돈 부담스러워하셨고, 오십은 너무 많았어.", "normal", {JH: "think"}),
    dict(L(JH, "그래도 3년을 해 주셨는데. 갑자기 줄이면 서운해하실 수도 있어.", "shock"), sfx="thud"),
    L(EJ, "엄마가 그런 걸로 서운해하겠어? 우리 엄마 쿨하잖아.", "normal"),
    L(JH, "…그럼 은지가 잘 말씀드려. 나는 옆에서 가만히 있을게.", "sad"),
    L(N, "저는 그 말에 쉽게 고개를 끄덕였어요. 그게 제일 부끄러운 일이 될 줄도 모르고요."),
])
s_say = scene("거실의 한마디", "living", [EJ, SJ, JH], mood="tense", when="다음 주 일요일", lines=[
    L(N, "그리고 일요일, 엄마를 집으로 모셔서 말을 꺼냈어요."),
    dict(L(EJ, "엄마, 이제 하준이 어린이집 가니까 용돈도 줄이자. 오십에서 삼십으로.", "normal", {SJ: "sad", JH: "think"}), sfx="thud"),
    L(SJ, "그래. 그게 맞지. 내가 할 일도 없는데 돈만 받으면 되겠니.", "sad"),
    L(EJ, "엄마가 그렇게 이해해 주니까 고마워. 우리도 살림이 빠듯해서.", "happy", {SJ: "sad"}),
    L(SJ, "그럼. 알지, 알아. 근데 은지야, 엄마가 잠깐 집에 같이 가자. 보여 줄 게 있다.", "sad"),
    L(EJ, "보여 줄 거? 뭔데?", "think", {SJ: "sad"}),
    L(SJ, "가 보면 안다. 오래 안 걸려. 사위도 같이 가자.", "sad", {JH: "surprised"}),
    L(N, "엄마의 목소리가 평소와 달랐어요. 화난 것도, 우는 것도 아닌, 아주 조용한 목소리였죠."),
])
s_cal = scene("달력 한 장", "room", [EJ, SJ, JH], mood="tense", when="엄마 집", lines=[
    L(N, "엄마 집에 도착하자, 엄마는 장롱 깊은 곳에서 낡은 종이 한 장을 꺼냈어요."),
    L(N, "엄마가 3년 동안 쓴 달력을 한 장에 옮겨 그린 연력이었어요. 칸마다 빨간 동그라미가 가득했죠."),
    dict(L(SJ, "빨간 동그라미는 하준이 본 날이야. 세어 보니까 천백 스물한 개더라.", "sad", {EJ: "shock"}), sfx="ding"),
    dict(L(EJ, "천백 스물한 개…? 엄마, 이걸 다 세었어?", "shock", {SJ: "sad"}), sfx="thud"),
    L(SJ, "그리고 이 파란 X 보이니? 이건 병원 예약한 날이야.", "sad"),
    L(JH, "병원이요? 장모님, 어디 편찮으셨어요?", "surprised", {SJ: "sad"}),
    L(SJ, "무릎이 안 좋아서 수술하라고 했는데, 날짜를 잡을 때마다 하준이 맡길 데가 없었어.", "sad"),
    L(N, "파란 X는 모두 열두 개였어요. 저는 그 열두 개가 몇 번 미룬 수술인지 헤아릴 수가 없었어요."),
    L(EJ, "엄마, 나한테는 한 번도 그런 말…", "cry", {SJ: "sad"}),
])
s_hosp = scene("엄마의 병원", "hospital", [SJ, DR], mood="sad", when="작년 가을 · 엄마의 기억", flashback=True, lines=[
    L(DR, "어머니, 무릎 연골이 거의 없습니다. 이대로 두시면 걷기 힘들어지세요. 수술 날짜 잡으시죠.", "normal", {SJ: "sad"}),
    L(SJ, "선생님, 제가 손주를 봐 주고 있어서요. 딸이 직장에 다니거든요.", "sad"),
    L(DR, "수술하면 최소 한 달은 안 움직이셔야 해요. 맡기실 곳은 없으세요?", "think"),
    L(SJ, "…없어요. 괜찮아요. 아직은 참을 만합니다. 하준이 어린이집 갈 때까지만요.", "sad"),
    L(N, "엄마는 그날 세 번째로 수술 날짜를 취소하고 병원 계단을 내려왔어요."),
    L(SJ, "은지한테 말하면 걱정할 텐데. 그냥 내가 참으면 되지.", "cry"),
    L(N, "엄마는 계단참에 앉아 무릎을 한참 주무르다, 다시 일어나 하준이를 데리러 갔다고 해요."),
])
s_yard = scene("서러웠던 마음", "yard", [EJ, SJ], mood="sad", when="엄마 집 마당", lines=[
    L(N, "저는 엄마를 따라 마당으로 나갔어요. 엄마는 뒷짐을 지고 한참 하늘을 올려다봤어요."),
    L(EJ, "엄마, 내가 잘못했어. 용돈이 적어서 서운하셨죠?", "cry", {SJ: "sad"}),
    L(SJ, "은지야, 엄마는 돈 때문에 서운한 게 아니야.", "sad"),
    L(SJ, "하준이 어린이집 간다는 말 듣는 순간, 이제 나는 쓸모없어졌구나 싶었어.", "cry", {EJ: "shock"}),
    L(SJ, "3년을 매일 새벽에 나서서 살았는데, 하루아침에 할 일이 없어지니까 마음이 텅 비더라.", "cry"),
    L(SJ, "거기다 용돈까지 줄이자는 말을 들으니, 내가 한 일이 오십만 원짜리였나 싶었다.", "sad", {EJ: "cry"}),
    dict(L(EJ, "엄마, 아니야. 그런 뜻이 아니었어. 정말 아니야.", "cry", {SJ: "sad"}), sfx="ding"),
    L(N, "저는 그제야 알았어요. 제가 한 말이 엄마의 3년을 얼마짜리로 매긴 말이었다는 걸요."),
])
s_back = scene("달력 뒷장", "kitchen", [EJ, SJ, JH], mood="hope", when="그날 저녁", lines=[
    L(N, "엄마는 저를 부엌으로 데리고 가더니, 달력을 뒤집어 보여 줬어요."),
    L(N, "뒷장에는 통장 사본이 붙어 있었고, 이름란에는 하준이의 이름이 또박또박 적혀 있었어요."),
    L(SJ, "네가 준 용돈, 한 푼도 안 썼다. 3년 동안 매달 오십씩 넣었어.", "happy", {EJ: "shock"}),
    L(EJ, "엄마… 이게 무슨 돈이야? 엄마 쓰라고 드린 건데.", "cry"),
    L(SJ, "하준이 대학 갈 때 보태라고 모았지. 엄마가 쓰기엔 너무 미안한 돈이었어.", "happy", {EJ: "cry"}),
    L(N, "통장 옆에는 엄마 글씨로 쓴 메모가 붙어 있었어요. 수술은 하준이 입학식 보고 하자."),
    L(JH, "장모님… 정말 죄송합니다. 저희가 너무 짧게 생각했어요.", "cry"),
    L(N, "남편이 먼저 일어나 엄마 손을 잡았어요. 저는 그 옆에서 소리 내어 울어 버렸어요."),
    L(SJ, "울긴 왜 울어. 내가 너희 마음 아는데. 다 컸어도 내 새끼들이다.", "happy", {EJ: "cry", JH: "cry"}),
])
s_op = scene("수술 날", "hospital", [EJ, SJ, JH], mood="hope", when="2주 뒤", lines=[
    L(N, "저는 다음 날 바로 병원에 전화해서 가장 빠른 수술 날짜를 잡았어요."),
    L(SJ, "얘, 입학식 보고 한다니까. 아직 한참 남았어.", "sad", {EJ: "sad"}),
    L(EJ, "엄마 무릎이 먼저야. 하준이 입학식에는 휠체어 타고 가면 되지. 내가 밀어 줄게.", "happy", {SJ: "happy"}),
    L(JH, "저희가 한 달 동안 교대로 휴가를 낼게요. 장모님은 아무 걱정 마세요.", "happy"),
    L(SJ, "참 나. 이런 일이 있나. 내가 사위한테 신세를 지게 생겼네.", "happy", {JH: "happy"}),
    L(N, "수술은 잘 끝났어요. 엄마는 마취에서 깨자마자 제일 먼저 하준이가 밥은 먹었냐고 물었죠."),
    L(N, "저는 그 말에 웃다가 또 울었어요. 우리 엄마는 끝까지 우리 엄마였어요."),
    L(EJ, "엄마, 용돈은 그대로 오십 드릴 거야. 아니, 육십 드릴게.", "happy", {SJ: "happy"}),
    L(SJ, "허, 이 아이가. 일은 안 하는데 월급 올려 주는 직장도 다 있네.", "happy"),
])
s_fin = scene("여러분께", "park", [EJ, SJ, HJ], mood="warm", when="한 달 뒤 일요일", lines=[
    L(N, "한 달 뒤 일요일, 엄마는 지팡이를 짚고 하준이와 놀이터에 나왔어요."),
    L(HJ, "할미! 이제 안 아파? 나랑 달리기하자!", "happy", {SJ: "happy"}),
    L(SJ, "이 녀석아, 아직은 걸어서 가야지. 할미 금방 낫는다.", "happy"),
    L(N, "저는 그 뒤로 일요일마다 엄마를 모시고 하준이와 함께 공원에 나와요."),
    L(N, "용돈은 그대로 드리고 있고, 엄마는 그 돈을 또 하준이 통장에 넣겠죠."),
    L(N, "저는 이제 압니다. 엄마가 한 일에는 값을 매길 수 없다는 것을요."),
    L(N, "여러분이라면 그날 엄마에게 어떻게 말씀하셨을까요? 댓글로 들려주세요."),
    L(N, "※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다."),
])

TITLE = "3년 동안 손주 봐 준 엄마에게 '이제 용돈 줄이자'던 딸, 엄마가 꺼낸 달력 한 장"
DESC_SHORT = "손주를 3년 동안 키워 준 엄마에게 '이제 용돈 줄이자'고 말한 딸. 엄마는 말없이 달력 한 장을 꺼냈습니다. 빨간 동그라미와 파란 X의 정체.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #감동사연 #엄마 #손주 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "grandson-calendar",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Aoede",
    "cast": {
        EJ: {"name": "은지", "gvoice": "ko-KR-Chirp3-HD-Aoede", "color": "#ec7b9b", "hair": "long", "hair_color": "#2f2118", "skin": "#fbdcc4"},
        SJ: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Sulafat", "color": "#7e8c6a", "hair": "bun", "hair_color": "#8a8582", "skin": "#eec4a2"},
        JH: {"name": "준호", "gvoice": "ko-KR-Chirp3-HD-Charon", "color": "#5c7cbf", "hair": "short", "hair_color": "#222222", "accessory": "glasses"},
        HJ: {"name": "하준", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#ffca28", "hair": "short", "hair_color": "#3a2618", "skin": "#ffe0c8", "scale": 0.6},
        DR: {"name": "의사", "gvoice": "ko-KR-Chirp3-HD-Iapetus", "color": "#e3f2fd", "hair": "short", "hair_color": "#333333", "accessory": "glasses"},
    },
    "scenes": S,
    "teaser": [[s_open, 1, 2], [s_cal, 3, 5], [s_cal, 7, 8]],
    "shorts_speed": 1.25,
    "shorts": [
        {"format": "full", "speed": 1.0,
         "clips": [[s_open, 1, 4], [s_ask, 2, 6], [s_play, 1, 5], [s_say, 1, 5], [s_cal, 2, 8], [s_hosp, 0, 6], [s_yard, 2, 5]],
         "hook": "엄마, 이제\n용돈 줄이자",
         "hook_who": EJ, "hook_emotion": "normal", "hook_tone": "red", "hook_prop": {"type": "calendar", "text": "3년 치 달력"},
         "cta_line": "엄마가 꺼낸 달력의 뒷이야기, 아래 본편에서 이어집니다.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"엄마, 이제 용돈 줄이자\" 3년 키워 준 엄마에게 건넨 한마디 #시니어사연 #감동사연 #엄마",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_cal, 2, 5], [s_hosp, 0, 6], [s_say, 1, 4], [s_yard, 1, 7], [s_back, 0, 8], [s_op, 5, 8]],
         "hook": "파란 X는\n병원 예약일",
         "hook_who": SJ, "hook_emotion": "sad", "hook_tone": "blue", "hook_prop": {"type": "calendar", "text": "천백 스물한 번"},
         "cta_line": "엄마의 3년, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"내가 한 일이 오십만 원짜리였나\" 엄마가 마당에서 한 말 #감동사연 #엄마 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_back, 3, 8], [s_op, 0, 8], [s_fin, 0, 4], [s_cal, 2, 5], [s_hosp, 2, 6], [s_yard, 3, 7]],
         "hook": "수술은 하준이\n입학식 보고 하자",
         "hook_who": SJ, "hook_emotion": "happy", "hook_tone": "gold", "hook_prop": {"type": "bankbook", "text": "하준이 통장"},
         "cta_line": "3년 치 용돈의 사연, 본편에서 이어서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"수술은 하준이 입학식 보고 하자\" 달력 뒷장에 붙은 통장 #감동사연 #엄마 #손주 #눈물주의",
         "description": DESC_SHORT},
        {"clips": [[s_say, 1, 3], [s_cal, 2, 5]], "hook": "용돈 줄이자는 말에\n엄마가 꺼낸 것",
         "hook_who": SJ, "hook_emotion": "sad", "hook_tone": "red", "hook_prop": {"type": "calendar", "text": "3년 치 달력"},
         "end_text": "달력의 정체는 본편에서 ▶",
         "title": "\"엄마, 이제 용돈 줄이자\" #시니어사연 #감동사연 #엄마"},
    ],
    "thumbnail": {
        "text": "엄마가 꺼낸\n달력 한 장",
        "highlight": "달력 한 장",
        "badge": "감동 사연",
        "variants": [
            {"style": "story", "tone": "red", "face": [SJ, "sad"], "prop": {"type": "calendar", "text": "3년 치 달력"}},
            {"style": "story", "tone": "gold", "face": [EJ, "cry"], "text": "용돈 줄이자던\n딸의 눈물", "highlight": "딸의 눈물",
             "badge": "눈물 주의", "prop": {"type": "calendar", "text": "천백 스물한 번"}},
            {"style": "story", "tone": "blue", "face": [SJ, "cry"], "text": "파란 X는\n병원 예약일", "highlight": "병원 예약일",
             "badge": "엄마의 3년", "prop": {"type": "bankbook", "text": "하준이 통장"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“엄마, 이제 용돈 줄이자”… 3년 키워 준 엄마가 말없이 꺼낸 달력에는 파란 X가 가득했다",
                           "손주 봐 준 엄마에게 용돈을 줄이자고 한 날, 달력 뒷장에 붙은 통장을 보고 딸은 주저앉았다"],
        "description": "“엄마, 이제 하준이 어린이집 가니까 용돈도 줄이자.” 3년 동안 매일 새벽 손주를 돌봐 준 엄마에게 딸이 건넨 말. 엄마는 아무 말 없이 낡은 달력 한 장을 꺼냈습니다. 빨간 동그라미 천백 스물한 개, 그리고 파란 X 열두 개.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 그날 엄마에게 어떻게 말씀하셨을까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #감동사연",
        "tags": ["사연", "시니어사연", "감동 사연", "엄마", "손주", "용돈", "육아", "친정엄마", "인생이야기", "사연 만화", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-11-04T18:00:00+09:00",
        "pinned_comment": "여러분이라면 그날 엄마에게 어떻게 말씀하셨을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-11-04T18:10:00+09:00", "2026-11-05T12:00:00+09:00", "2026-11-06T12:00:00+09:00", "2026-11-06T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
