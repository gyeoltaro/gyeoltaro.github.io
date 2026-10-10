"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 1부 아래층 남자의 이야기 → 2부 같은 석 달을 위층 할머니 목소리로 → 3부 함께"""
import json
T, G, M, O, D, X, N = "taeho", "grandma", "manager", "mom", "daeun", "doctor", "narrator"


def L(w, t, e="normal", r=None):
    d = {"who": w, "text": t}
    if w != N:
        d["emotion"] = e
    if r:
        d["react"] = r
    return d


def NG(t):  # 2부 해설: 할머니 목소리
    return dict(L(N, t), voice=G)


S = []


def scene(title, bg, cast, lines=None, **kw):
    S.append(dict(title=title, bg=bg, cast=cast, lines=lines, **kw))
    return len(S) - 1


# ───────── 1부: 아래층 남자의 이야기 ─────────
s_open = scene("새벽 다섯 시의 쿵쿵", "hallway", [T], mood="tense", lines=[
    L(N, "새벽 다섯 시. 오늘도 천장에서 쿵, 쿵 소리가 났습니다."),
    dict(L(T, "할머니! 지금 몇 시인 줄 아세요? 석 달째예요, 석 달!", "angry"), sfx="thud"),
    L(N, "석 달을 참다 결국 위층 문을 두드렸어요. 그리고 문이 열렸을 때, 저는 아무 말도 할 수 없었습니다."),
    L(T, "할머니… 이게 다 뭐예요?", "shock"),
    L(N, "이 이야기는 두 사람의 이야기입니다. 먼저, 아래층에 사는 제 이야기부터 할게요."),
])
scene("재택근무자의 새벽", "room_night", [T], mood="calm", when="석 달 전", lines=[
    L(N, "저는 집에서 일하는 프로그래머예요. 밤늦게 일하고, 아침 아홉 시쯤 일어나죠."),
    L(N, "그런데 석 달 전부터, 매일 새벽 다섯 시면 천장이 울리기 시작했어요."),
    dict(L(T, "쿵… 드르륵… 쿵… 대체 새벽에 뭘 하는 거야.", "angry"), sfx="thud"),
    L(T, "가구를 옮기나? 아니면 운동이라도 하나?", "think"),
    L(N, "소리는 딱 한 시간. 다섯 시부터 여섯 시까지, 하루도 빠지지 않았어요."),
    L(T, "이어폰을 끼고 자도 소용이 없네. 진동이 머리로 바로 울려.", "angry"),
    L(T, "이러다 내가 먼저 쓰러지겠다. 오늘은 말을 해야겠어.", "angry"),
])
s_note = scene("문에 붙인 쪽지", "hallway", [T], mood="tense", lines=[
    L(N, "처음엔 점잖게 쪽지를 붙였어요."),
    L(T, "새벽 소음 자제 부탁드립니다. 아래층 1203호. 이 정도면 알아듣겠지.", "think"),
    L(N, "다음 날 아침, 제 현관문 앞에 떡 한 팩과 쪽지 한 장이 놓여 있었어요."),
    L(T, "떡? 떡으로 때우겠다는 거야? 소음은 그대로면서.", "angry"),
    dict(L(N, "저는 쪽지를 펼쳐 보지도 않고, 떡이랑 같이 분리수거함에 넣어 버렸습니다."), sfx="ding"),
    L(N, "그 쪽지에 무엇이 적혀 있었는지는, 한참 뒤에야 알게 됐어요."),
])
scene("관리사무소", "office", [T, M], mood="calm", lines=[
    L(T, "소장님, 1303호 좀 어떻게 해 주세요. 새벽마다 쿵쿵거려서 잠을 못 자요.", "angry", {M: "think"}),
    L(M, "1303호요? 거기 여든 되신 할머니 혼자 사세요.", "surprised"),
    L(T, "혼자 사시는 할머니가 무슨 소리를 그렇게 내요?", "think"),
    L(M, "글쎄요. 요즘 새벽마다 뭘 연습하신다고는 들었는데…", "think", {T: "angry"}),
    L(T, "연습이요? 새벽 다섯 시에요? 방송 한 번만 해 주세요.", "angry"),
    L(M, "알겠습니다. 근데 너무 몰아세우진 마세요. 사정이 있으신 것 같던데.", "sad"),
])
scene("엄마의 전화", "room_night", [T, O], mood="calm", lines=[
    L(O, "태호야, 이번 주말에 외할머니 생신인데 올 수 있지?", "happy", {T: "think"}),
    L(T, "엄마, 나 요즘 잠도 못 자고 일도 밀렸어. 다음에 갈게.", "angry"),
    L(O, "할머니가 너 보고 싶다고 매일 그러셔. 일 년째 얼굴을 못 봤다고.", "sad", {T: "sad"}),
    L(T, "알았어, 알았어. 나 바빠. 끊을게.", "angry", {O: "sad"}),
    L(N, "그때 저는 몰랐어요. 그 짜증이, 위층에도 똑같이 향하고 있었다는 걸."),
])
s_broom = scene("천장을 두드리다", "room", [T], mood="tense", lines=[
    L(N, "방송이 나간 다음 날에도 소리는 계속됐어요. 조금 작아졌을 뿐."),
    dict(L(T, "진짜 너무하네. 나도 할 만큼 했어.", "angry"), sfx="thud"),
    L(N, "저는 빗자루로 천장을 쾅쾅 두드렸어요. 위층 소리가 잠깐 멈췄다가, 다시 아주 작게 이어졌죠."),
    L(T, "할머니, 제발요! 저도 잠은 자야 사는 사람이에요!", "angry"),
    L(T, "끝까지 해 보자는 거지? 좋아. 내일은 직접 올라간다.", "angry"),
])

# ───────── 2부: 위층 할머니의 이야기 ─────────
s_fall = scene("넘어진 날", "hospital", [G, D, X], mood="sad", when="위층 이야기 · 석 달 전", flashback=True, lying=[G], lines=[
    NG("이번엔 위층 이야기를 해 볼게요. 석 달 전, 나는 화장실 앞에서 미끄러져 엉덩이뼈가 부러졌어요."),
    L(X, "수술은 잘 됐습니다. 그런데 연세가 있으셔서, 다시 걷기는 어려우실 수도 있어요.", "sad", {D: "sad"}),
    L(D, "할머니, 걱정하지 마. 휠체어 타면 되지.", "sad", {G: "sad"}),
    L(D, "근데 할머니… 나 석 달 뒤에 결혼해. 할머니 꼭 와야 돼.", "cry"),
    L(G, "다은아, 할머니는 네 결혼식에 휠체어 말고, 내 발로 걸어 들어갈 거다.", "happy", {D: "cry"}),
    NG("의사 선생님은 고개를 저었지만, 나는 그날 마음을 먹었어요."),
])
s_practice = scene("새벽 다섯 시의 연습", "living", [G], mood="sad", when="위층 이야기", lines=[
    NG("새벽 다섯 시. 아무도 안 보는 시간이라야, 넘어져도 덜 부끄러웠어요."),
    L(G, "하나… 둘… 셋… 오늘은 스무 걸음만 더 가 보자.", "sad"),
    L(G, "다리야, 조금만 버텨 다오. 우리 다은이 손 한 번만 잡게.", "sad"),
    NG("보행기를 밀 때마다 바닥이 드르륵 울렸고, 다리가 풀리면 쿵 하고 주저앉았어요."),
    dict(L(G, "아이고… 괜찮다, 괜찮아. 다시 일어나면 되지.", "cry"), sfx="thud"),
    L(G, "다은아, 할머니 오늘 스물세 걸음 걸었다.", "happy"),
    NG("벽에 붙인 달력에 매일 동그라미를 쳤어요. 결혼식까지 남은 날을 세면서요."),
])
s_reply = scene("아래층 총각의 쪽지", "kitchen", [G], mood="sad", when="위층 이야기", lines=[
    NG("어느 날 현관문에 아래층 총각의 쪽지가 붙어 있었어요. 얼마나 시끄러웠으면 그랬을까."),
    L(G, "아이고, 총각도 출근해야 할 텐데. 내가 염치가 없었네.", "sad"),
    NG("떡 한 팩을 사서, 삐뚤빼뚤한 글씨로 답장을 썼어요."),
    L(G, "시끄러워서 정말 미안해요. 손녀 결혼식까지 딱 3주만 참아 주면, 그날 잔치떡 꼭 갖다 드릴게요.", "sad"),
    dict(NG("다음 날 아침, 분리수거함에 그 떡이 버려져 있었어요. 쪽지는 펴 보지도 않은 채로."), sfx="ding"),
    L(G, "그래… 내가 미웠겠지. 미울 만하지.", "cry"),
])
s_bang = scene("천장이 울리던 날", "room_night", [G, D], mood="sad", when="위층 이야기", lines=[
    NG("그리고 그날 새벽, 발밑에서 쾅쾅 소리가 났어요. 아래층에서 천장을 두드리는 소리였죠."),
    L(G, "미안해요, 총각. 미안해요…", "cry"),
    NG("이불을 세 겹으로 깔고, 보행기 바퀴에 양말을 씌웠어요. 그래도 소리가 다 안 막아지더라고요."),
    L(G, "그만둘까… 휠체어 타고 가도 다은이는 좋아할 텐데.", "sad"),
    L(D, "할머니, 전화 받았어? 연습 너무 무리하지 마. 그냥 휠체어 타고 와도 돼.", "sad", {G: "sad"}),
    L(G, "다은아, 할머니 요즘 서른 걸음도 넘게 걷는다. 걱정하지 마라.", "happy"),
    L(G, "내가 약속했잖아. 내 발로 간다고.", "think"),
    NG("다음 날 새벽 다섯 시, 누군가 우리 집 문을 세게 두드렸어요."),
])

# ───────── 3부: 함께 ─────────
s_door = scene("열린 문", "hallway", [T, G], mood="sad", when="다시, 그날 새벽", lines=[
    L(N, "다시, 그날 새벽. 문을 연 할머니는 땀에 흠뻑 젖은 채 보행기를 붙잡고 있었어요."),
    dict(L(G, "총각이구나. 또 시끄러웠지요? 미안해요. 정말 미안해요.", "sad", {T: "shock"}), sfx="thud"),
    L(N, "거실 바닥엔 테이프로 붙인 줄이 있었어요. 열 걸음, 스무 걸음, 서른 걸음."),
    L(T, "다은이 결혼식, D-21… 할머니, 이거 걷는 연습이에요?", "shock", {G: "sad"}),
    L(G, "손녀 결혼식에 내 발로 들어가고 싶어서. 늙은이 욕심이 총각 잠을 다 뺏었네.", "sad", {T: "cry"}),
])
s_sorry = scene("버려진 쪽지", "living", [T, G], mood="sad", lines=[
    L(T, "할머니, 그 쪽지… 저 안 읽고 버렸어요. 떡도요. 죄송합니다.", "cry", {G: "surprised"}),
    L(G, "괜찮아요. 내가 총각이었어도 화났을 거야.", "happy"),
    L(T, "아니에요. 우리 외할머니도 여든이세요. 일 년째 찾아뵙지도 못했는데…", "cry", {G: "sad"}),
    dict(L(T, "할머니, 내일부터는 저랑 같이 공원에서 걸어요. 거긴 아무리 쿵쿵거려도 아무도 뭐라 안 해요.", "happy", {G: "surprised"}), sfx="ding"),
    L(G, "총각이 그 새벽에? 일은 어쩌고?", "surprised"),
    L(T, "저 재택근무예요. 출근 시간이 없어요.", "happy", {G: "happy"}),
])
scene("새벽 공원", "park", [T, G], mood="hope", when="결혼식 14일 전", lines=[
    L(N, "그날부터 새벽 다섯 시면, 저는 할머니 옆에서 같이 걸었어요."),
    L(T, "마흔여덟, 마흔아홉, 쉰! 할머니, 오늘 쉰 걸음이에요!", "happy", {G: "happy"}),
    L(G, "아이고, 총각 덕분이다. 혼자 할 땐 서른 걸음이 끝이었는데.", "happy"),
    L(G, "총각은 할머니 안 계셔?", "think", {T: "sad"}),
    L(T, "계세요. 근데 바쁘다는 핑계로 일 년째 못 갔어요.", "sad"),
    L(G, "가 봐요. 늙으면 손주 얼굴 한 번이 보약이야.", "happy", {T: "sad"}),
    L(T, "할머니, 결혼식에 저도 가도 돼요? 할머니 걷는 거 제 눈으로 보고 싶어요.", "happy", {G: "surprised"}),
    L(G, "그럼. 총각이 우리 집 일등 하객이지.", "happy", {T: "happy"}),
])
scene("엄마에게 건 전화", "room", [T, O], mood="warm", lines=[
    L(T, "엄마, 이번 주말에 외할머니 댁 가자. 내가 운전할게.", "normal", {O: "surprised"}),
    L(O, "태호야, 갑자기 웬일이야? 바쁘다며.", "surprised"),
    L(T, "위층 할머니가 그러시더라. 늙으면 손주 얼굴이 보약이래.", "happy", {O: "happy"}),
    L(O, "위층 할머니? 너 층간소음 때문에 싸운다며.", "think"),
    L(T, "응. 이제는 같이 걷는 사이야.", "happy"),
    L(O, "그래, 외할머니가 얼마나 좋아하시겠니. 엄마가 미역국 끓여 놓을게.", "happy", {T: "happy"}),
])
s_wed = scene("결혼식 날", "wedding", [D, G, T], mood="hope", when="결혼식 당일", lines=[
    L(N, "그리고 결혼식 날. 신부 입장 전, 할머니가 먼저 식장에 들어섰어요. 휠체어 없이, 지팡이 하나만 짚고."),
    dict(L(D, "할머니! 할머니 걸어서 왔어?", "cry", {G: "happy", T: "cry"}), sfx="ding"),
    L(G, "내 발로 왔다, 우리 다은이. 약속 지켰지?", "happy", {D: "cry"}),
    L(N, "하객석에서 박수가 터졌어요. 저도 모르게 일어나서 손뼉을 쳤습니다."),
    L(D, "아저씨가 아래층 분이시죠? 할머니가 새벽마다 같이 걸어 준 총각 꼭 데려오라고 하셨어요.", "happy", {T: "surprised"}),
    L(G, "총각, 약속한 잔치떡이야. 이번엔 버리지 마요.", "happy", {T: "cry"}),
])
scene("아래층 남자의 지금", "park", [T, G], mood="warm", lines=[
    L(N, "층간소음은 이제 없어요. 할머니는 보행기 없이도 집 안을 걸으시거든요."),
    L(N, "대신 매일 새벽 다섯 시면, 우리 집 문을 두드리는 소리가 들려요."),
    L(G, "총각, 걸으러 가자!", "happy", {T: "happy"}),
    L(T, "네, 할머니. 오늘은 공원 두 바퀴 가요.", "happy"),
    L(T, "가면서 우리 외할머니 얘기 해 드릴게요. 할머니랑 똑같이 고집이 세세요.", "happy", {G: "happy"}),
    L(G, "고집 센 할머니들이 오래 사는 법이야.", "happy"),
    L(N, "그리고 지난 주말엔, 일 년 만에 우리 외할머니 손을 잡고 같이 걸었습니다."),
])
scene("여러분께", "living", [T], mood="warm", lines=[
    L(N, "혹시 여러분 위층에서도, 이유를 모르는 소리가 들려오나요?"),
    L(N, "화내기 전에 쪽지 한 장, 아니 문 한 번 두드려서 안부를 물어봐 주세요."),
    L(T, "여러분이라면 그 새벽, 위층 문을 두드렸을까요? 댓글로 들려주세요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "석 달 참은 층간소음, 새벽 5시에 위층 문을 두드렸다가 할 말을 잃었습니다"
proj = {
    "title": TITLE,
    "slug": "upstairs-grandma",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Achird",
    "cast": {
        T: {"name": "태호", "gvoice": "ko-KR-Chirp3-HD-Achird", "color": "#26a69a", "hair": "short", "hair_color": "#2b2220", "skin": "#f4cfae", "accessory": "glasses"},
        G: {"name": "위층 할머니", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#a1887f", "hair": "bun", "hair_color": "#dedad4", "skin": "#f2cba8"},
        M: {"name": "관리소장", "gvoice": "ko-KR-Chirp3-HD-Umbriel", "color": "#5d6d7e", "hair": "short", "hair_color": "#7a7a7a"},
        O: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Autonoe", "color": "#ce93d8", "hair": "bun", "hair_color": "#4a3a32", "skin": "#f7d4b8"},
        D: {"name": "다은", "gvoice": "ko-KR-Chirp3-HD-Callirrhoe", "color": "#fafafa", "hair": "long", "hair_color": "#3a2a20", "skin": "#ffdcc0", "accessory": "bow"},
        X: {"name": "의사", "gvoice": "ko-KR-Chirp3-HD-Zubenelgenubi", "color": "#eceff1", "hair": "short", "hair_color": "#1e1a1a", "accessory": "glasses"},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (결혼식 결말은 숨김)
    "teaser": [[s_open, 1, 2], [s_door, 1, 2], [s_door, 3, 5]],
    "shorts_speed": 1.25,
    "shorts": [
        {"clips": [[s_open, 1, 2], [s_door, 1, 5]], "hook": "층간소음 항의하러\n갔다가 얼어붙었다",
         "hook_who": T, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "calendar", "text": "결혼식 D-21"},
         "end_text": "D-21의 비밀은 본편에서 ▶"},
        {"clips": [[s_practice, 1, 7]], "hook": "여든 살 할머니의\n새벽 5시 비밀",
         "hook_who": G, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "calendar", "text": "오늘 23걸음"},
         "end_text": "할머니의 약속은 본편에서 ▶"},
        {"clips": [[s_note, 3, 5], [s_reply, 3, 6]], "hook": "읽지도 않고\n버려진 쪽지",
         "hook_who": G, "hook_emotion": "sad", "hook_tone": "gold", "hook_prop": {"type": "letter", "text": "미안해요"},
         "end_text": "아래층 남자의 선택은 본편에서 ▶"},
        {"clips": [[s_wed, 1, 6]], "hook": "휠체어 대신\n내 발로 걸어서",
         "hook_who": D, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "photo", "text": "결혼식"},
         "end_text": "전체 이야기는 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "층간소음 범인\n80세 할머니",
        "highlight": "80세 할머니",
        "badge": "새벽 5시의 쿵쿵",
        "variants": [
            {"style": "story", "tone": "red", "face": [T, "shock"], "prop": {"type": "calendar", "text": "결혼식 D-21"}},
            {"style": "story", "tone": "blue", "face": [G, "sad"], "text": "읽지도 않고\n버린 쪽지", "highlight": "버린 쪽지",
             "badge": "눈물 주의", "prop": {"type": "letter", "text": "미안해요"}},
            {"style": "story", "tone": "gold", "face": [T, "cry"], "text": "위층 벽에 붙은\nD-21", "highlight": "D-21",
             "badge": "끝까지 보세요", "prop": {"type": "calendar", "text": "결혼식 D-21"}},
        ],
    },
    "publish": {
        "url": "https://youtu.be/ps3Sdkd-bMg",  # 업로드된 롱폼 (쇼츠 설명·고정 댓글 링크)
        "title": TITLE,
        "title_variants": ["“할머니, 지금 몇 시인 줄 아세요?” 석 달 층간소음의 진짜 이유",
                           "읽지도 않고 버린 위층 할머니의 쪽지, 거기엔 이렇게 적혀 있었습니다"],
        "description": "“할머니, 지금 몇 시인 줄 아세요?” 석 달 동안 매일 새벽 다섯 시면 울리던 천장. 참다못해 위층 문을 두드린 날, 문을 연 건 땀에 젖은 여든 살 할머니였습니다. 아래층 남자와 위층 할머니, 두 사람의 석 달을 차례로 들려드립니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 그 새벽, 위층 문을 두드리셨을까요? 여러분의 이웃 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #층간소음 #감동사연",
        "tags": ["사연", "층간소음", "감동 사연", "이웃 사연", "할머니", "손녀 결혼식", "아파트", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "가족 사연", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-11-06T18:00:00+09:00",
        "pinned_comment": "이웃 때문에 화났다가 사정을 알고 마음이 바뀐 적 있으신가요? 여러분의 이웃 이야기를 들려주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-11-07T12:00:00+09:00", "2026-11-08T19:00:00+09:00", "2026-11-09T12:00:00+09:00", "2026-11-10T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #층간소음"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
