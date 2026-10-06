"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)"""
import json
J, M, D, O, B, N = "jieun", "minho", "dad", "mom", "banker", "narrator"
K = "jieun_kid"  # 회상 속 어린 지은


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


s_open = scene("아빠의 서랍", "room", [J, M, O], mood="calm", lines=[
    L(N, "아빠가 돌아가시고 일주일 뒤, 우리는 아빠 방을 정리하고 있었습니다."),
    L(M, "누나, 이거 좀 봐. 서랍 맨 밑에 이런 게 있어.", "surprised", {J: "think", O: "sad"}),
    L(J, "통장? 아빠가 무슨 통장을 이렇게 꼭꼭 숨겨 놨어?", "think"),
    L(N, "낡은 고무줄로 묶인 통장 세 개. 그걸 열어 본 순간, 저는 그 자리에 주저앉았습니다."),
    dict(L(J, "이게… 이게 다 뭐야?", "surprised", {M: "surprised", O: "sad"}), sfx="thud"),
    L(N, "이 이야기를 하려면, 우리 아빠가 얼마나 지독한 짠돌이였는지부터 말씀드려야 할 것 같아요."),
])
scene("우리 아빠는 짠돌이", "living", [K, D, O], mood="warm", when="20여 년 전", flashback=True, lines=[
    L(N, "아빠는 삼십 년 동안 택시를 몰았습니다. 그리고 동네에서 소문난 짠돌이였어요."),
    L(D, "누가 방에 불 켜 놨어? 사람 없는 방에 불 켜면 전기세가 얼만데.", "angry", {K: "sad"}),
    L(K, "아빠, 나 숙제하다 잠깐 화장실 간 거야.", "sad"),
    L(D, "그래도 끄고 가. 습관이 돼야 돈이 모이는 거야.", "normal"),
    L(N, "한여름에도 에어컨은 손님이 올 때만 켰어요."),
    L(N, "아빠 점퍼는 제가 초등학생 때부터 대학생이 될 때까지 똑같은 거였고요."),
    L(O, "여보, 점퍼 소매 다 해졌어요. 이번엔 하나 사요.", "think", {D: "think"}),
    L(D, "아직 멀쩡해. 바느질하면 몇 년은 더 입어.", "happy"),
    L(N, "그때는 몰랐어요. 왜 아빠는 그렇게까지 아껴야 했는지."),
])
scene("생일 케이크 대신 붕어빵", "street", [K, D], mood="warm", when="열 살 생일", flashback=True, lines=[
    L(N, "제 열 살 생일이었어요. 친구들은 생일마다 큰 케이크에 초를 꽂았거든요."),
    L(K, "아빠, 오늘 내 생일인데 케이크 사 오는 거지?", "happy", {D: "think"}),
    L(D, "케이크는 금방 상해. 아빠가 더 맛있는 거 사 왔다.", "happy"),
    L(K, "이거… 붕어빵이잖아.", "sad", {D: "happy"}),
    L(D, "팥 많이 든 걸로 골랐어. 따뜻할 때 먹어.", "happy"),
    L(N, "저는 그날 붕어빵을 한 입도 안 먹고 방에 들어가 울었어요. 그 뒤로 매년 제 생일엔 붕어빵이 왔습니다."),
    L(K, "다른 애들 아빠는 케이크 사 주는데, 우리 아빠는 왜 맨날 이래.", "angry"),
])
scene("수학여행", "kitchen", [J, D, O], mood="calm", when="중학생 때", flashback=True, lines=[
    L(J, "엄마, 나 수학여행비 내야 돼. 제주도 간대.", "happy", {O: "think", D: "think"}),
    L(D, "제주도? 거기 꼭 가야 하는 거냐?", "think"),
    L(J, "반 애들 다 가! 나만 안 가면 왕따 당한단 말이야!", "angry", {D: "surprised"}),
    L(O, "여보, 이건 보내 줍시다. 애가 얼마나 기다렸는데.", "sad"),
    L(D, "…알았다. 대신 용돈은 만 원이다.", "normal", {J: "surprised"}),
    L(N, "다른 친구들은 십만 원씩 들고 와서 기념품을 샀어요. 저는 만 원으로 귤 초콜릿 하나를 샀습니다."),
    L(N, "그 초콜릿을 아빠한테 내밀었을 때, 아빠가 웃었던 것 같기도 해요. 그땐 그것도 짜증이 났지만요."),
])
scene("핸드폰 전쟁", "room_night", [J, D, M], mood="tense", when="고등학생 때", flashback=True, lines=[
    L(J, "아빠, 우리 반에서 핸드폰 없는 사람 나밖에 없어.", "sad", {D: "think"}),
    L(D, "학생이 핸드폰이 왜 필요해. 공부할 시간에 문자만 하지.", "angry"),
    L(M, "누나 진짜 불쌍해. 친구들 단톡방에도 못 들어간대.", "sad", {J: "sad"}),
    L(J, "아빠는 내가 창피한 거 몰라? 진짜 짠돌이야!", "angry", {D: "sad", M: "surprised"}),
    L(N, "그날 아빠는 아무 말도 안 했어요. 그냥 해진 점퍼를 입고 밤 운행을 나갔습니다."),
    L(N, "저는 고등학교를 졸업할 때까지 핸드폰을 갖지 못했어요."),
])
scene("등록금은 내가 번다", "cafe", [J, M], mood="sad", when="대학 입학", lines=[
    L(N, "대학에 붙었을 때, 아빠가 처음 한 말은 축하가 아니었어요."),
    L(J, "아빠가 그러더라. 장학금 받으라고. 등록금은 반만 내 준대.", "sad", {M: "surprised"}),
    L(M, "반만? 누나 그럼 나머지는 어떡해?", "surprised"),
    L(J, "어떡하긴. 알바 세 개 뛰어야지.", "angry"),
    L(N, "카페, 편의점, 과외. 하루에 네 시간 자면서 학교를 다녔습니다."),
    L(J, "민호야, 너는 나처럼 살지 마. 빨리 돈 벌어서 이 집에서 나가.", "sad", {M: "sad"}),
    L(N, "그때부터 저는 아빠를 미워하기로 마음먹었던 것 같아요."),
])
s_wed = scene("결혼자금 100만 원", "living", [J, D, O], mood="tense", when="3년 전", lines=[
    L(N, "그리고 몇 년 뒤, 제가 결혼을 하게 됐어요."),
    L(J, "아빠, 다음 달에 상견례 해요. 결혼 준비하려면 돈이 좀 필요해.", "normal", {D: "think", O: "sad"}),
    L(D, "…여기 있다.", "sad"),
    L(J, "100만 원? 아빠, 이게 다야?", "surprised", {D: "sad", O: "sad"}),
    L(J, "다른 집은 전셋값 보태 준다는데, 아빠는 딸 시집가는데 100만 원이 다야?", "angry"),
    L(O, "지은아, 아빠한테 그러는 거 아니야.", "sad"),
    L(J, "엄마는 맨날 아빠 편이야! 나 진짜 이 집 딸 맞아?", "angry", {D: "sad"}),
    L(D, "미안하다. 아빠가… 지금은 이것밖에 없다.", "sad"),
    L(N, "저는 그 봉투를 식탁에 던져 놓고 나와 버렸어요."),
    L(N, "그게 아빠 얼굴을 제대로 본 마지막 날이 될 줄도 모르고요."),
])
scene("멀어진 우리", "night", [J], mood="sad", lines=[
    L(N, "결혼하고 삼 년 동안, 저는 명절에만 잠깐 집에 들렀어요."),
    L(N, "아빠는 가끔 밤늦게 전화를 했지만, 저는 바쁘다는 핑계로 받지 않았습니다."),
    L(J, "또 아빠네. 받으면 또 잔소리하겠지.", "think"),
    L(N, "그 부재중 전화들이, 아빠가 할 수 있는 최선의 표현이었다는 걸 그땐 몰랐어요."),
])
scene("엄마의 전화", "room_night", [J, O], mood="tense", lines=[
    dict(L(O, "지은아… 아빠가 쓰러지셨어. 빨리 병원으로 와.", "sad", {J: "surprised"}), sfx="thud"),
    L(J, "뭐? 엄마, 무슨 소리야. 아빠 어디 아팠어?", "surprised"),
    L(O, "작년부터 심장이 안 좋으셨어. 너희한테는 절대 말하지 말라고 하셔서…", "sad", {J: "sad"}),
    L(J, "왜? 왜 말을 안 했어! 수술은? 수술은 했어?", "angry"),
    L(O, "수술비 아깝다고, 조금만 더 버티면 된다고 미루셨어.", "sad"),
])
scene("병실에서", "hospital", [J, O, D], mood="sad", lines=[
    L(N, "병원에 도착했을 때, 아빠는 이미 말을 잘 하지 못했어요."),
    L(J, "아빠, 나 왔어. 지은이 왔어. 눈 좀 떠 봐.", "sad", {O: "sad"}),
    L(D, "지은아… 미안하다… 서랍…", "sad", {J: "surprised"}),
    L(J, "서랍? 무슨 서랍? 아빠, 그런 거 말고 일어나기만 해.", "sad"),
    L(D, "…우리 딸… 고맙다…", "sad"),
    L(N, "그게 아빠의 마지막 말이었습니다. 저는 끝내 고맙다는 말도, 미안하다는 말도 하지 못했어요."),
], lying=[D])
scene("장례식장", "memorial", [M, J, O], mood="sad", lines=[
    L(N, "장례식장에는 생각보다 많은 사람이 찾아왔어요. 대부분 처음 보는 얼굴이었습니다."),
    L(M, "누나, 저분들 다 아빠 택시 단골이래. 아빠가 새벽마다 공짜로 병원 태워 드렸대.", "surprised", {J: "surprised"}),
    L(J, "공짜로? 우리한테는 만 원 한 장도 벌벌 떨던 사람이?", "think"),
    L(O, "너희 아빠는 원래 그런 사람이야. 말을 잘 못 해서 그렇지.", "sad", {J: "sad"}),
])
s_book = scene("서랍 속 통장", "room", [J, M, O], mood="calm", when="다시, 현재", lines=[
    L(N, "그리고 다시, 그날 아빠 방."),
    L(M, "누나, 이거 누나 이름이야. 이건 내 이름이고, 이건 엄마 거.", "surprised", {J: "surprised"}),
    L(J, "첫 입금이… 내가 태어난 해야. 매달 삼십만 원씩…", "surprised"),
    L(J, "한 달도 안 빠졌어. 삼십 년 동안 한 달도.", "sad", {M: "sad", O: "sad"}),
    dict(L(M, "누나 통장 잔액… 일억 이천만 원이야.", "surprised", {J: "surprised"}), sfx="ding"),
    L(N, "통장 사이사이에는 아빠의 삐뚤삐뚤한 글씨로 메모가 붙어 있었어요."),
    L(J, "지은이 대학… 지은이 시집… 지은이 집…", "sad"),
    L(N, "등록금 반만 내 준다던 아빠. 결혼할 때 100만 원만 주던 아빠. 그 아빠의 통장이었어요."),
])
s_bank = scene("은행에서", "bank", [J, B], mood="hope", lines=[
    L(N, "믿기지 않아서, 다음 날 통장을 들고 은행에 갔어요."),
    L(B, "아, 이 통장… 혹시 택시 하시던 아버님 따님이세요?", "surprised", {J: "surprised"}),
    L(J, "아빠를 아세요?", "surprised"),
    L(B, "그럼요. 매달 첫째 주 월요일 아침이면 꼭 직접 오셨어요. 십 년 넘게 제가 맡았거든요.", "sad"),
    L(B, "자동이체 하시면 편하다고 해도, 직접 넣어야 마음이 놓인다고 하셨어요.", "normal"),
    L(B, "그리고 늘 그러셨어요. 이 돈은 절대 손대면 안 된다고. 우리 애들 힘들 때 줄 거라고.", "sad", {J: "sad"}),
    L(J, "아빠가… 그런 말을 했어요?", "sad"),
    L(B, "딸 자랑을 정말 많이 하셨어요. 혼자 알바해서 대학 다닌 장한 딸이라고.", "happy", {J: "sad"}),
    L(N, "저는 은행 창구 앞에서, 다 큰 어른이 아이처럼 엉엉 울었어요."),
])
s_mom = scene("엄마의 고백", "kitchen", [J, M, O], mood="sad", lines=[
    L(J, "엄마, 하나만 물어볼게. 나 결혼할 때, 아빠 진짜 100만 원밖에 없었어?", "sad", {O: "sad"}),
    dict(L(O, "…그해에 아빠 택시 회사가 망했어. 월급을 반년이나 못 받았지.", "sad", {J: "surprised", M: "surprised"}), sfx="thud"),
    L(O, "그 100만 원도, 아빠가 새벽마다 대리운전해서 모은 돈이야.", "sad"),
    L(J, "그럼 통장에서 꺼내 주면 됐잖아!", "angry"),
    L(O, "아빠가 그러더라. 이건 애들이 진짜 무너질 때 주는 돈이라고. 결혼은 웃으면서 하는 거니까 괜찮다고.", "sad"),
    L(M, "아빠가 수술 안 한 것도… 설마 이 통장 때문이야?", "surprised", {O: "sad"}),
    L(O, "수술하려면 통장을 깨야 했거든. 아빠는 끝까지 그건 안 된다고 했어.", "sad", {J: "sad", M: "sad"}),
    L(J, "바보 같아. 진짜 바보 같아, 아빠.", "sad"),
])
s_letter = scene("통장 사이의 편지", "room_night", [J, D], mood="sad", lines=[
    L(N, "제 통장 맨 뒤에는, 접힌 편지 한 장이 끼워져 있었어요."),
    dict(L(D, "지은아. 아빠가 말을 잘 못 해서, 이렇게 글로 쓴다.", "sad", {J: "sad"}), sfx="ding"),
    L(D, "생일마다 케이크 하나 못 사 줘서 미안하다. 붕어빵 사 들고 오는 길에 아빠도 많이 창피했다.", "sad"),
    L(D, "핸드폰 사 달라고 울던 날, 아빠는 밤새 운전하면서 너한테 미안해서 혼났다.", "sad"),
    L(D, "그래도 이 통장만큼은 지키고 싶었다. 아빠가 없어도, 우리 딸이 힘들 때 기댈 곳 하나는 있어야 하니까.", "sad"),
    L(D, "짠돌이 아빠라서 미안하다. 그래도 아빠는 우리 딸이 세상에서 제일 자랑스럽다.", "happy", {J: "sad"}),
    L(J, "아빠… 나 이제야 알았어. 미안해. 정말 미안해.", "sad"),
])
s_bday = scene("아빠 생일", "memorial", [M, J, O], mood="hope", lines=[
    L(N, "그리고 올해, 아빠 생일."),
    L(J, "아빠, 오늘은 내가 붕어빵 사 왔어. 팥 많이 든 걸로.", "sad", {O: "sad", M: "sad"}),
    L(M, "아빠, 나도 이제 짠돌이 될게. 아빠처럼 우리 가족 지키는 짠돌이.", "sad"),
    L(O, "여보, 애들이 이제야 당신 마음 알았나 봐요.", "sad", {J: "sad"}),
    L(J, "아빠 통장은 엄마한테 다 드리기로 했어. 엄마가 아빠 대신 오래오래 행복하게 쓰시라고.", "happy", {O: "surprised"}),
    L(N, "아빠가 평생 아껴서 남긴 건, 돈이 아니라 우리를 향한 마음이었어요."),
])
scene("여러분께", "park", [J], mood="warm", lines=[
    L(N, "혹시 여러분 곁에도, 말 대신 행동으로 사랑을 표현하는 짠돌이 아빠가 있나요?"),
    L(N, "오늘은 전화 한 통 걸어서, 고맙다고 한마디만 해 보세요. 생각보다 시간이 많지 않을지도 몰라요."),
    L(J, "여러분의 부모님 이야기도 댓글로 들려주세요. 하나하나 다 읽을게요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])
s_cta = scene("본편 안내", "room", [J], mood="calm", lines=[
    L(J, "이 이야기의 진짜 결말은 채널 본편에서 확인하세요.", "sad"),
], shorts_only=True)

proj = {
    "title": "평생 짠돌이라 원망했던 아빠, 통장을 열어 본 날 주저앉았습니다",
    "slug": "dad-bankbook",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Aoede",
    "cast": {
        J: {"name": "지은", "gvoice": "ko-KR-Chirp3-HD-Aoede", "color": "#ff8a65", "hair": "long", "hair_color": "#3b2a20", "skin": "#ffdcc0"},
        K: {"name": "어린 지은", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#ffb74d", "hair": "long", "hair_color": "#3b2a20", "skin": "#ffdcc0", "accessory": "bow", "scale": 0.72},
        M: {"name": "민호", "gvoice": "ko-KR-Chirp3-HD-Puck", "color": "#4caf7a", "hair": "spiky", "hair_color": "#2a2626"},
        D: {"name": "아빠", "gvoice": "ko-KR-Chirp3-HD-Charon", "color": "#8a6a4a", "hair": "short", "hair_color": "#9a9a9a", "skin": "#f2c9a6"},
        O: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#9c7bd0", "hair": "bun", "hair_color": "#5c4a42", "skin": "#f7d4b8"},
        B: {"name": "은행 직원", "gvoice": "ko-KR-Chirp3-HD-Kore", "color": "#3f5fbf", "hair": "bun", "hair_color": "#1f1a1a", "accessory": "glasses"},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (결말은 숨김)
    "teaser": [[s_wed, 3, 5], [s_book, 4, 5], [s_letter, 5, 6]],
    "shorts_speed": 1.25,
    "shorts": [
        # clips: [장면, 시작줄, 끝줄(제외)] — 느린 해설은 빼고 결정적인 대사부터
        {"clips": [[s_open, 1, 5], [s_book, 2, 7]], "hook": "아빠 통장 열어보고\n주저앉았습니다",
         "hook_who": J, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "bankbook", "text": "1억 2천만 원"},
         "end_text": "통장의 비밀은 본편에서 ▶"},
        {"clips": [[s_bank, 1, 8]], "hook": "은행 직원의 한마디에\n눈물이 터졌다",
         "hook_who": J, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "bankbook", "text": "매달 30만 원"},
         "end_text": "전체 이야기는 본편에서 ▶"},
        {"clips": [[s_wed, 2, 8]], "hook": "딸 결혼에\n100만 원만 준 아빠",
         "hook_who": J, "hook_emotion": "shock", "hook_tone": "gold", "hook_prop": {"type": "money", "text": "100만 원"},
         "end_text": "100만 원의 진실은 본편에서 ▶"},
        {"clips": [[s_letter, 1, 7]], "hook": "통장 맨 뒤에\n숨겨진 편지",
         "hook_who": J, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "letter", "text": "미안하다"},
         "end_text": "아빠의 30년은 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "짠돌이 아빠\n통장 열어보니",
        "highlight": "통장 열어보니",
        "badge": "30년 동안 숨긴 비밀",
        "variants": [
            {"style": "story", "tone": "red", "face": [J, "cry"], "prop": {"type": "bankbook", "text": "1억 2천만 원"}},
            {"style": "story", "tone": "blue", "face": [D, "sad"], "text": "아빠가 숨긴\n편지 한 장", "highlight": "편지 한 장", "badge": "눈물 주의",
             "prop": {"type": "letter", "text": "미안하다"}},
            {"style": "story", "tone": "gold", "face": [J, "shock"], "text": "결혼자금\n100만 원의 진실", "highlight": "100만 원의 진실",
             "badge": "딸만 몰랐던 이유", "prop": {"type": "money", "text": "100만 원"}},
        ],
    },
    "publish": {
        "title": "평생 짠돌이라 원망했던 아빠, 통장을 열어 본 날 주저앉았습니다",
        "title_variants": ["“아빠, 이게 다야?” 결혼자금 100만 원 준 아빠의 통장을 열어 봤습니다",
                           "짠돌이 아빠가 30년 동안 숨긴 통장 세 개, 잔액을 보고 무너졌습니다"],
        "description": "케이크 대신 붕어빵, 결혼자금 100만 원. 평생 짠돌이라고 원망했던 아빠가 떠난 뒤, 서랍 속에서 통장 세 개가 나왔습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 끝까지 통장을 지킨 아빠의 선택을 이해하실 수 있나요? 여러분의 부모님 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #감동사연 #아빠",
        "tags": ["사연", "감동 사연", "가족 사연", "아빠", "짠돌이 아빠", "통장", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "부모님", "효도", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-09T18:00:00+09:00",
        "pinned_comment": "여러분의 아버지는 어떤 분이셨나요? 말 대신 행동으로 사랑을 보여 주셨던 순간을 댓글로 나눠 주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-10T12:00:00+09:00", "2026-10-11T19:00:00+09:00", "2026-10-12T12:00:00+09:00", "2026-10-13T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #가족"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines))
for i, sh in enumerate(proj["shorts"], 1):
    print("short", i, sum(len(l["text"]) for c in sh["clips"] for l in S[c[0]]["lines"][c[1]:c[2]]), "chars")
print("40자 초과:", [l["text"] for l in lines if len(l["text"]) > 45])
