"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 옥탑방 상자에서 시작(앞당긴 장면) → 형제의 어린 시절·장례식·절연 → 이름 없는 도움 두 번(복선)
→ 형이 쓰러짐 → 상자 속 영수증과 수첩(형의 목소리) → 형수의 고백 → 병실 → 마지막 상환"""
import json
T, B, E, W_, F, TK, BK, K, N = "taeo", "taesung", "eunjeong", "sujin", "dad", "taeo_kid", "taesung_kid", "keeper", "narrator"


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


s_open = scene("형의 옥탑방", "rooftop", [T, E], mood="tense", when="현재", lines=[
    L(N, "십 년 동안 연락을 끊었던 형의 옥탑방. 저는 형수님 부탁으로 상자 하나를 가지러 갔습니다."),
    L(E, "서방님, 저 상자예요. 무슨 일 생기면 꼭 서방님 드리라고 했어요.", "sad", {T: "angry"}),
    L(T, "형이 저한테 줄 게 뭐가 있어요. 집 판 돈이라도 들었나 보죠.", "angry", {E: "sad"}),
    dict(L(N, "테이프를 뜯자, 누렇게 바랜 영수증 수백 장이 바닥으로 쏟아졌어요."), sfx="thud"),
    L(T, "상환 영수증… 백이십 회? 형수님, 이게 다 뭐예요?", "shock", {E: "cry"}),
    L(N, "그날 저는, 십 년 동안 미워했던 형이 혼자 무엇을 지고 있었는지 알게 됐습니다."),
    L(N, "이 이야기를 하려면, 우리 형제가 아직 한 방을 쓰던 시절로 돌아가야 해요."),
])
scene("형의 운동화", "room", [TK, BK], mood="warm", when="25년 전", flashback=True, lines=[
    L(N, "아버지는 작은 부품 공장을 했고, 우리 집은 늘 넉넉하지 않았어요."),
    L(TK, "형, 나 내일 소풍인데 운동화 앞이 다 터졌어. 애들이 놀릴 거야.", "cry", {BK: "think"}),
    L(BK, "울지 마. 형이 다 생각이 있어. 잠깐만 기다려 봐.", "happy"),
    L(N, "형은 신문 배달로 모은 돈을 들고 시장으로 뛰어갔어요. 자기 운동화를 사려고 모은 돈이었죠."),
    L(BK, "자, 새 운동화. 사이즈 크게 샀어. 오래 신어야 하니까.", "happy", {TK: "surprised"}),
    L(TK, "우와! 근데 형 운동화는? 형 것도 구멍 났잖아.", "surprised"),
    L(BK, "형은 발 다 컸어. 너는 아직 커야 하잖아.", "happy", {TK: "happy"}),
])
s_factory = scene("아버지의 공장", "warehouse", [F, B, T], mood="calm", when="12년 전", flashback=True, lines=[
    L(N, "형은 고등학교를 졸업하자마자 아버지 공장에서 일했어요. 저는 대학에 갔고요."),
    L(F, "태오야, 공부 열심히 해라. 우리 집에서 대학 간 사람은 네가 처음이다.", "happy", {T: "happy"}),
    L(F, "이 집이랑 공장은 나중에 너희 둘 거다. 반반이야. 싸우지 말고.", "happy"),
    L(N, "그런데 그해 겨울부터, 아버지는 밤마다 누군가와 낮은 목소리로 통화를 했어요."),
    L(F, "김 사장, 보증 얘기는 애들 앞에서 하지 말자고 했잖나.", "think", {B: "think"}),
    L(B, "아버지, 무슨 일 있으세요? 요즘 공장에 빨간 우편물이 자꾸 와요.", "think"),
    L(F, "아무 일 없다. 태오한테는 쓸데없는 소리 하지 마라.", "sad", {B: "sad"}),
])
s_funeral = scene("아버지 장례식", "memorial", [T, B], mood="tense", when="10년 전", lines=[
    L(N, "아버지는 그다음 해 봄에 갑자기 쓰러지셨어요. 장례식 사흘째 밤이었습니다."),
    L(B, "태오야, 집 내놨다. 공장도 정리할 거야.", "sad", {T: "surprised"}),
    L(T, "집을 팔아? 아버지 돌아가신 지 사흘밖에 안 됐어.", "shock", {B: "sad"}),
    L(B, "내가 다 알아서 정리할게. 넌 신경 쓰지 말고 학교나 다녀.", "sad"),
    L(T, "아버지가 반반이라고 했잖아. 그럼 내 몫은?", "angry", {B: "sad"}),
    dict(L(B, "네 몫 같은 거 없어. 더 묻지 마.", "angry", {T: "shock"}), sfx="thud"),
    L(T, "형 혼자 다 가져가겠다는 거지? 그거였구나.", "angry"),
])
s_night = scene("갈라선 밤", "night", [T, B], mood="sad", when="10년 전", lines=[
    L(T, "오늘부터 나한테 형 없어. 찾아오지도 마.", "angry", {B: "sad"}),
    L(B, "태오야… 밥은 굶지 말고 다녀.", "sad"),
    L(T, "그 말 하지 마. 형이 그런 말 할 자격 없어.", "cry", {B: "cry"}),
    L(N, "그날 이후로 저는 형 번호를 지웠어요. 명절에도, 아버지 기일에도 따로 갔죠."),
    L(N, "형은 집 판 돈으로 잘 살고 있을 거라고, 저는 그렇게 믿었습니다."),
])
s_scholar = scene("이름 없는 장학금", "classroom", [T, W_], mood="hope", when="9년 전", lines=[
    L(N, "다음 학기, 저는 등록금이 없어서 휴학 신청서를 들고 학과 사무실에 갔어요."),
    L(W_, "태오야! 휴학하지 마. 너 장학금 됐대. 등록금 전액이래!", "surprised", {T: "shock"}),
    L(T, "내가? 성적도 그저 그런데? 어디서 주는 건데?", "surprised"),
    L(W_, "이름이 좀 특이해. '두 형제 장학회'래. 졸업할 때까지 매 학기 준대.", "happy", {T: "think"}),
    L(T, "두 형제… 처음 듣는 데네. 아무튼 살았다.", "happy", {W_: "happy"}),
    L(N, "그때 저는 그 이름을 한 번도 깊이 생각해 보지 않았어요."),
])
s_hall = scene("문 앞의 쌀 포대", "hallway", [T, W_], mood="calm", when="6년 전", lines=[
    L(N, "졸업하고 취직해서, 그때 그 사무실 동기 수진이와 결혼했어요. 신혼집으로 이사한 날이었죠."),
    L(W_, "여보, 현관 앞에 쌀 포대가 있어. 봉투도 같이 있고.", "surprised", {T: "think"}),
    L(T, "봉투에 이름이 없네. 안에… 삼백만 원?", "shock", {W_: "surprised"}),
    L(W_, "쪽지가 있어. '밥은 굶지 말고 살아라.' 이게 누구야?", "think"),
    L(T, "…회사 사장님이 보내셨나 보다. 그분이 좀 그런 스타일이야.", "think", {W_: "think"}),
    L(N, "그 말투를 어디서 들었는지, 저는 끝내 떠올리지 않았어요. 떠올리기 싫었던 거겠죠."),
])
scene("기일의 국화", "memorial", [T, K], mood="calm", when="3년 전", lines=[
    L(N, "아버지 기일이면 저는 늘 혼자, 형이 오지 않을 시간에 맞춰 납골당에 갔어요."),
    L(T, "어? 국화가 벌써 있네. 꽃이 아직 싱싱한데.", "surprised", {K: "happy"}),
    L(K, "큰아드님이 아침 일찍 다녀가셨어요. 그분은 기일 말고도 매달 오세요.", "happy"),
    L(T, "매달이요? 형이 그렇게 한가한 사람이 아닐 텐데요.", "think"),
    L(K, "늘 흙 묻은 작업복 차림이에요. 일 가기 전에 들른다고 하시더라고요.", "normal", {T: "think"}),
    L(K, "올 때마다 아버님 앞에서 뭘 한참 읽으세요. 영수증 같은 걸요.", "think", {T: "surprised"}),
    L(T, "작업복이요? 집 판 돈으로 장사한다고 들었는데…", "think"),
    L(N, "그 이상한 기분을, 저는 그날도 애써 모른 척했습니다."),
])
s_call = scene("형수의 전화", "office", [T], mood="tense", when="현재", lines=[
    L(N, "그리고 올해 가을, 회사에서 모르는 번호로 전화가 왔어요."),
    dict(L(E, "서방님, 저 은정이에요. 형이… 공사장에서 쓰러졌어요.", "cry", {T: "shock"}), sfx="ding"),
    L(T, "공사장이요? 형이 왜 공사장에서 일을 해요? 집 판 돈은요?", "shock"),
    L(E, "의식이 아직 없어요. 서방님, 한 번만 와 주세요.", "cry"),
    L(T, "형수님, 저는 형이랑 끝난 사이예요. 죄송해요.", "angry"),
    L(E, "그럼 옥탑방에 있는 상자만이라도 가져가 주세요. 그이가 그것만은 꼭 전하라고 했어요.", "sad", {T: "think"}),
])
scene("아내의 한마디", "living", [T, W_], mood="calm", lines=[
    L(W_, "여보, 아주버님 쓰러지셨다며. 안 가 볼 거야?", "sad", {T: "angry"}),
    L(T, "십 년 동안 연락 한 번 없던 사람이야. 이제 와서 뭘.", "angry"),
    L(W_, "연락은 당신이 끊었잖아. 아주버님은 기다린 걸 수도 있어.", "think", {T: "think"}),
    L(W_, "미워하는 것도 십 년이면 충분해. 상자만 가지고 와. 같이 열어 보자.", "sad"),
    L(T, "…그래. 상자만 가지고 올게. 그게 끝이야.", "sad", {W_: "happy"}),
])
s_box = scene("상자 속 영수증", "rooftop", [T, E], mood="sad", lines=[
    L(N, "그렇게 저는 처음으로 형의 옥탑방에 올라갔어요. 그리고 그 상자를 열었죠."),
    L(T, "채무자 강병철… 이거 아버지 이름이잖아요. 보증 채무 상환?", "shock", {E: "cry"}),
    L(E, "아버님이 친구분 보증을 서셨대요. 공장이 넘어가고도 빚이 삼억이 남았어요.", "cry"),
    L(T, "그럼 집을 판 게… 빚 갚으려고요?", "surprised", {E: "sad"}),
    L(E, "집 판 돈으로도 모자라서, 그이가 십 년 동안 매달 이백만 원씩 갚았어요.", "sad"),
    dict(L(T, "이건 등록금 납부 영수증이잖아. 납부자… 강태성?", "shock", {E: "cry"}), sfx="thud"),
    L(T, "두 형제 장학회가… 형이었어?", "cry"),
])
s_diary = scene("형의 수첩", "room_night", [T, B], mood="sad", lines=[
    L(N, "상자 맨 밑에는 낡은 수첩이 한 권 있었어요. 형의 글씨였습니다."),
    L(B, "태오가 오늘 나를 버렸다. 잘됐다. 미워할 사람이 있어야 버틴다.", "sad"),
    L(B, "등록금 냈다. 장학회 이름은 두 형제. 태오는 눈치 못 챌 거다.", "happy"),
    L(B, "태오 졸업식. 강당 맨 뒤에서 봤다. 학사모가 아버지 닮았다.", "cry"),
    L(B, "태오 결혼한다. 쌀 한 포대 문 앞에 두고 왔다. 밥은 굶지 마라, 태오야.", "cry"),
    L(B, "남은 빚 이천만 원. 한 번만 더 내면 아버지 이름이 깨끗해진다.", "happy"),
    L(T, "바보 같은 형… 운동화 때랑 똑같잖아.", "cry"),
])
s_conf = scene("형수의 고백", "kitchen", [T, E], mood="sad", lines=[
    L(T, "형수님, 왜 저한테 한 번도 말 안 하셨어요?", "cry", {E: "sad"}),
    L(E, "그이가 그랬어요. 태오까지 빚쟁이 아들이 되면 안 된다고.", "sad"),
    L(E, "서방님이 알면 학교 그만두고 같이 갚겠다고 할 거라고요.", "sad", {T: "cry"}),
    L(E, "그래서 장례식 날, 일부러 나쁜 형이 됐대요. 그래야 서방님이 떠날 수 있으니까.", "cry"),
    L(T, "저는 그것도 모르고 십 년 동안 형을 욕했어요.", "cry", {E: "cry"}),
    L(E, "그이는 다 알고 있었어요. 그래도 서방님 얘기만 나오면 웃었어요.", "happy"),
])
s_hosp = scene("병실", "hospital", [T, B], mood="hope", lying=[B], lines=[
    L(N, "그날 밤, 저는 병원으로 달려갔어요. 사흘 만에 형이 눈을 떴습니다."),
    L(B, "…태오냐? 왔냐. 밥은 먹었고?", "surprised", {T: "cry"}),
    L(T, "지금 밥이 문제야? 왜 말 안 했어. 왜 혼자 다 갚았어!", "cry", {B: "sad"}),
    L(B, "말하면 네가 학교 그만뒀을 거잖아. 너라도 앞으로 가야지.", "sad"),
    L(T, "나쁜 형이라고 십 년을 미워했어. 아버지 집 혼자 챙긴 사람이라고.", "cry"),
    L(B, "알아. 그래도 된다. 그 덕에 너는 뒤도 안 보고 갔잖아.", "happy", {T: "cry"}),
    dict(L(T, "이제 내가 갚을게. 마지막 한 번은 내가 낼 거야.", "cry", {B: "surprised"}), sfx="ding"),
    L(B, "그래… 그럼 그건 같이 내자. 두 형제니까.", "happy", {T: "happy"}),
])
s_last = scene("마지막 영수증", "park", [T, B], mood="hope", when="한 달 뒤", lines=[
    L(N, "한 달 뒤, 퇴원한 형과 은행에 다녀오는 길이었어요."),
    L(T, "형, 이거 봐. 완납. 백이십 회 끝.", "happy", {B: "cry"}),
    L(B, "아버지… 이제 깨끗해졌습니다.", "cry"),
    L(T, "형, 나 이거 하나 사 왔어. 형 운동화. 사이즈 크게 샀어.", "happy", {B: "surprised"}),
    L(B, "형은 발 다 컸다니까. 이 녀석이.", "cry", {T: "happy"}),
    L(T, "오래 신으라고. 이제 형도 좀 앞으로 가야지.", "happy", {B: "happy"}),
])
scene("여러분께", "rooftop", [T, B], mood="warm", lines=[
    L(N, "요즘 우리 형제는 일요일마다 형 옥탑방 평상에서 고기를 구워요."),
    L(B, "태오야, 많이 먹어. 밥은 굶지 말고.", "happy", {T: "happy"}),
    L(N, "혹시 여러분에게도, 오해한 채 멀어진 가족이 있나요?"),
    L(N, "그 사람이 왜 그랬는지, 한 번만 먼저 물어봐 주세요. 너무 늦기 전에요."),
    L(T, "여러분이라면 십 년 만에 형 앞에서 무슨 말부터 하셨을까요? 댓글로 들려주세요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "아버지 집 팔아 혼자 챙긴 형과 10년 절연… 형 옥탑방 상자를 열고 말을 잃었습니다"
proj = {
    "title": TITLE,
    "slug": "brother-receipts",
    "voice": "ko-KR-InJoonNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Alnilam",
    "cast": {
        T: {"name": "태오", "gvoice": "ko-KR-Chirp3-HD-Alnilam", "color": "#26a69a", "hair": "short", "hair_color": "#231c18", "skin": "#f8d4b4"},
        B: {"name": "태성", "gvoice": "ko-KR-Chirp3-HD-Algenib", "color": "#6d4c41", "hair": "spiky", "hair_color": "#1a1614", "skin": "#e8b994"},
        E: {"name": "형수 은정", "gvoice": "ko-KR-Chirp3-HD-Sulafat", "color": "#f06292", "hair": "bun", "hair_color": "#3e2a20"},
        W_: {"name": "수진", "gvoice": "ko-KR-Chirp3-HD-Kore", "color": "#ffca28", "hair": "long", "hair_color": "#5a3a24", "accessory": "bow"},
        F: {"name": "아버지", "gvoice": "ko-KR-Chirp3-HD-Sadachbia", "color": "#546e7a", "hair": "short", "hair_color": "#9e9a96", "skin": "#eec29e", "accessory": "glasses"},
        TK: {"name": "어린 태오", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#4dd0e1", "hair": "short", "hair_color": "#231c18", "skin": "#ffe0c8", "scale": 0.7},
        K: {"name": "관리인", "gvoice": "ko-KR-Chirp3-HD-Iapetus", "color": "#78909c", "hair": "none", "skin": "#eec29e"},
        BK: {"name": "어린 태성", "gvoice": "ko-KR-Chirp3-HD-Puck", "color": "#a1887f", "hair": "spiky", "hair_color": "#1a1614", "skin": "#f2cba8", "scale": 0.8},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (병실 화해·완납 결말은 숨김)
    "teaser": [[s_funeral, 5, 7], [s_box, 5, 7], [s_conf, 3, 4]],
    "shorts_speed": 1.25,
    "shorts": [
        {"clips": [[s_funeral, 1, 7], [s_night, 0, 2]], "hook": "아버지 집 팔고\n혼자 챙긴 형",
         "hook_who": T, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "key", "text": "아버지 집"},
         "end_text": "형이 숨긴 진실은 본편에서 ▶"},
        {"clips": [[s_scholar, 1, 5], [s_hall, 2, 5]], "hook": "이름 없는\n장학금의 정체",
         "hook_who": T, "hook_emotion": "surprised", "hook_tone": "gold", "hook_prop": {"type": "envelope", "text": "삼백만 원"},
         "end_text": "보낸 사람은 본편에서 ▶"},
        {"clips": [[s_box, 1, 7], [s_diary, 1, 2]], "hook": "형 옥탑방\n상자 속 영수증",
         "hook_who": T, "hook_emotion": "shock", "hook_tone": "blue", "hook_prop": {"type": "receipt", "text": "120회"},
         "end_text": "형의 수첩은 본편에서 ▶"},
        {"clips": [[s_hosp, 1, 8]], "hook": "십 년 만에\n형을 찾아간 날",
         "hook_who": B, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "receipt", "text": "완납"},
         "end_text": "두 형제의 결말은 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "유산 챙긴 형\n상자의 비밀",
        "highlight": "상자의 비밀",
        "badge": "10년 절연",
        "variants": [
            {"style": "story", "tone": "red", "face": [T, "shock"], "prop": {"type": "receipt", "text": "120회"}},
            {"style": "story", "tone": "blue", "face": [B, "cry"], "text": "이름 없는\n장학금의 정체", "highlight": "장학금의 정체",
             "badge": "눈물 주의", "prop": {"type": "envelope", "text": "삼백만 원"}},
            {"style": "story", "tone": "gold", "face": [T, "cry"], "text": "형이 10년 동안\n갚은 것", "highlight": "갚은 것",
             "badge": "끝까지 보세요", "prop": {"type": "receipt", "text": "완납"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“네 몫 같은 거 없어”… 아버지 장례식 날 집을 팔아 버린 형의 진짜 이유",
                           "유산 혼자 챙긴 줄 알았던 형, 옥탑방 영수증 120장에 적힌 이름"],
        "description": "“네 몫 같은 거 없어. 더 묻지 마.” 아버지 장례식 사흘째 밤, 집을 팔겠다는 형과 연을 끊은 태오. 십 년 뒤 형이 공사장에서 쓰러졌다는 전화를 받고, 형의 옥탑방에서 상자 하나를 열게 됩니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 십 년 만에 형 앞에서 무슨 말부터 하셨을까요? 오해로 멀어졌던 가족 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #형제 #감동사연",
        "tags": ["사연", "형제", "감동 사연", "가족 사연", "유산", "형제 갈등", "보증 빚", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "형 사연", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-13T18:00:00+09:00",
        "pinned_comment": "오해로 멀어졌다가 나중에 진심을 알게 된 가족이 있으신가요? 여러분의 이야기를 들려주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-14T12:00:00+09:00", "2026-10-14T19:00:00+09:00", "2026-10-15T12:00:00+09:00", "2026-10-15T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #형제"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
