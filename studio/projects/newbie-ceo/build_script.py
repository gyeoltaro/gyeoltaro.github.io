"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)"""
import json
M, S_, B, C, J, H, N = "minji", "sujeong", "bujang", "ceo", "junhyuk", "harin", "narrator"


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


s_open = scene("회식 자리의 침묵", "hoesik", [M, S_, B, C], mood="tense", lines=[
    L(N, "입사 석 달째 첫 회식. 부장님은 오늘도 수정 씨에게 술을 따르라고 했습니다."),
    L(B, "어이, 늦깎이 신입. 부장 잔 비었잖아. 눈치가 없어, 눈치가.", "angry", {S_: "sad", M: "think", C: "normal"}),
    L(S_, "네, 부장님. 따라 드리겠습니다.", "sad"),
    L(N, "그때 고깃집 문이 열리고, 사장님이 들어오셨어요."),
    dict(L(C, "한 선생님? 여기 계셨군요. 그동안 정말 감사했습니다.", "surprised", {B: "shock", M: "shock", S_: "surprised"}), sfx="thud"),
    L(B, "사, 사장님… 지금 신입한테 뭐라고 하신 겁니까?", "shock"),
    L(N, "그날 저는 알게 됐습니다. 우리가 석 달 동안 무시해 온 신입이 누구였는지."),
])
scene("서른일곱 살 신입", "office", [M, S_, J, B], mood="calm", when="석 달 전", lines=[
    L(N, "석 달 전, 우리 해외영업팀에 신입 한 명이 들어왔어요."),
    L(S_, "안녕하세요. 한수정입니다. 많이 가르쳐 주세요.", "normal", {B: "think"}),
    L(B, "서른일곱? 신입이 나랑 열 살 차이네. 그 나이 먹도록 뭐 했어요?", "angry", {S_: "sad", J: "surprised"}),
    L(S_, "혼자 아이를 키우느라 몇 년 쉬었습니다.", "sad"),
    L(J, "부장님, 첫날부터 너무 세게 가시는데요?", "think", {B: "happy"}),
    L(B, "농담이야, 농담. 신입이 그것도 못 받아?", "happy", {S_: "sad"}),
    L(N, "저는 그때 웃기만 했어요. 솔직히 저도 같은 생각이었거든요."),
])
s_coffee = scene("탕비실의 커피", "kitchen", [S_, B, M], mood="calm", lines=[
    L(B, "수정 씨, 아메리카노 말고 믹스커피. 설탕 반 스푼. 몇 번을 말해.", "angry", {S_: "sad"}),
    L(S_, "죄송합니다. 다시 타 오겠습니다.", "sad"),
    L(M, "수정 씨, 부장님 커피는 원래 막내가 타요. 그냥 외워 두세요.", "normal", {S_: "normal"}),
    L(N, "수정 씨는 매일 여덟 시에 출근해서, 팀원 다섯 명의 커피 취향을 수첩에 적어 두었어요."),
    dict(L(B, "그리고 이 보고서, 내 이름으로 올린다. 신입 이름이면 위에서 안 읽어.", "think", {S_: "surprised", M: "surprised"}), sfx="ding"),
    L(S_, "…네, 알겠습니다.", "sad"),
    L(N, "보고서는 부장님 이름으로 올라갔고, 그 주에 부장님은 칭찬을 받았습니다."),
])
scene("혼자 먹는 도시락", "park", [M, S_, J], mood="calm", lines=[
    L(N, "점심시간이면 수정 씨는 혼자 회사 앞 벤치에서 도시락을 먹었어요."),
    L(M, "아, 수정 씨 여기 있었네요. 저희 먼저 국밥 먹으러 갈게요.", "normal", {S_: "happy"}),
    L(S_, "네, 맛있게 드세요.", "happy"),
    L(N, "도시락 옆에는 늘 두꺼운 일본어 책이 펼쳐져 있었어요."),
    L(J, "민지 씨, 저 책 봤어요? 나이 먹고 무슨 일본어 공부래.", "think", {M: "think"}),
    L(M, "자격증 따려나 보죠. 우리랑은 별로 안 친해지고 싶은가 봐요.", "normal"),
])
scene("거래처 앞에서", "cafe", [B, S_, M], mood="tense", lines=[
    L(N, "한 달쯤 지났을 때, 거래처 미팅에서 납품 날짜가 잘못 전달된 일이 있었어요."),
    L(B, "죄송합니다, 사장님. 우리 신입이 날짜를 잘못 적어서요. 아직 일을 몰라서 그래요.", "sad", {S_: "surprised", M: "surprised"}),
    L(M, "그거 부장님이 전화로 받으신 날짜였는데…", "think"),
    dict(L(B, "수정 씨, 뭐 해요? 얼른 거래처 사장님께 사과드려야지.", "angry", {S_: "sad", M: "angry"}), sfx="thud"),
    L(S_, "…제 실수입니다. 정말 죄송합니다.", "sad"),
    L(N, "수정 씨는 한마디 변명도 없이 고개를 숙였어요. 그날 처음으로, 부장님이 무서운 사람이라는 걸 알았습니다."),
])
s_six = scene("여섯 시 정각", "office", [S_, B, M], mood="tense", lines=[
    L(N, "그리고 수정 씨는 매일 여섯 시 정각에 퇴근했어요."),
    L(B, "벌써 가요? 다들 야근하는데 신입이 제일 먼저 가네?", "angry", {S_: "sad", M: "think"}),
    L(S_, "죄송합니다. 어린이집이 일곱 시에 문을 닫아서요.", "sad"),
    dict(L(B, "애 핑계 대면 다야? 회사가 놀이터야?", "angry", {S_: "sad", M: "surprised"}), sfx="thud"),
    L(N, "수정 씨는 고개를 숙이고 나갔고, 사무실엔 부장님 웃음소리만 남았어요."),
])
scene("어린이집 앞에서", "street", [M, S_, H], mood="warm", lines=[
    L(N, "그날 퇴근길, 저는 우연히 어린이집 앞에서 수정 씨를 봤어요."),
    L(H, "엄마! 오늘도 일등으로 왔다!", "happy", {S_: "happy", M: "surprised"}),
    L(S_, "그럼. 엄마는 하린이한테는 절대 안 늦어.", "happy"),
    L(H, "엄마 회사 사람들 좋아? 엄마 안 힘들어?", "think", {S_: "sad"}),
    L(S_, "응, 다들 좋아. 엄마 회사 진짜 좋은 곳이야.", "happy", {M: "sad"}),
    L(H, "그럼 엄마도 회사에서 일등이야?", "happy"),
    L(S_, "음… 엄마는 아직 꼴찌야. 그래도 열심히 하고 있어.", "sad", {M: "sad"}),
    L(N, "그 말을 듣는데, 이상하게 가슴 한쪽이 따끔했어요."),
])
s_crisis = scene("삼십억 계약이 날아간다", "office", [B, M, J], mood="tense", lines=[
    dict(L(B, "큰일 났다. 오사카 거래처가 계약을 해지하겠대!", "shock", {M: "shock", J: "shock"}), sfx="thud"),
    L(J, "삼십억짜리요? 갑자기 왜요?", "surprised"),
    L(J, "오사카 공장장님은 한국어를 한마디도 못 하시잖아요. 누가 통화를 해요?", "think", {B: "angry"}),
    L(B, "우리가 보낸 사양서 숫자가 틀렸대. 번역 누가 한 거야!", "angry", {J: "sad", M: "think"}),
    L(M, "그거… 부장님이 번역기 돌려서 보내신 거잖아요.", "think", {B: "angry"}),
    L(B, "조용히 해! 내일 아침까지 해결 못 하면 우리 팀 다 끝이야.", "angry"),
    L(N, "그날 밤, 부장님은 제일 먼저 퇴근했어요. 수정 씨는 말없이 그 사양서를 출력해 갔고요."),
])
s_roof = scene("밤 열한 시의 옥상", "night", [M, S_], mood="calm", lines=[
    L(N, "밤 열한 시. 휴대폰을 두고 와서 회사에 다시 들렀는데, 옥상에서 목소리가 들렸어요."),
    L(S_, "다나카 공장장님, 정말 죄송합니다. 틀린 숫자는 제가 하나하나 다시 확인했습니다.", "sad", {M: "surprised"}),
    L(N, "수정 씨가 유창한 일본어로 통화하고 있었어요. 손에는 빨간 펜으로 고친 사양서가 들려 있었고요."),
    L(M, "수정 씨… 일본어를 그렇게 잘했어요?", "surprised", {S_: "surprised"}),
    L(S_, "아, 민지 씨. 예전에 일본에서 통역 일을 조금 했어요.", "normal"),
    L(S_, "부장님께는 비밀로 해 주세요. 제가 했다고 하면 부장님이 곤란해지시잖아요.", "sad", {M: "think"}),
    dict(L(N, "그 사람은, 자기를 무시하는 상사의 체면까지 지켜 주고 있었습니다."), sfx="ding"),
])
s_credit = scene("가로챈 공", "office", [B, M, S_, J], mood="tense", lines=[
    L(N, "다음 날 아침, 오사카에서 계약을 그대로 유지하겠다는 연락이 왔어요."),
    L(B, "다들 들었지? 내가 밤새 사과하고 사양서 다 고쳤다. 위에도 그렇게 보고했어.", "happy", {M: "think", S_: "normal"}),
    L(J, "역시 부장님! 이번 성과급은 부장님 거네요.", "happy"),
    L(M, "부장님, 그거 사실은…", "think", {B: "angry", S_: "surprised"}),
    L(S_, "민지 씨, 괜찮아요.", "normal", {M: "sad"}),
    dict(L(B, "사실은 뭐? 신입은 신입답게 커피나 타 와.", "angry", {S_: "sad", M: "angry"}), sfx="thud"),
    L(N, "그날 아무 말도 하지 못한 제가, 부장님보다 더 부끄러웠어요."),
])
s_reveal = scene("다시, 회식 자리", "hoesik", [M, S_, B, C], mood="tense", when="다시, 회식 자리", lines=[
    L(N, "그리고 다시, 그날의 회식 자리."),
    L(C, "다나카 회장님이 어제 저한테 직접 전화를 하셨어요.", "normal", {B: "surprised"}),
    L(C, "그 사과 전화, 한수정 씨가 한 거 맞냐고. 십오 년 전 그 학생 맞냐고.", "normal", {S_: "surprised", M: "surprised"}),
    dict(L(B, "네? 그, 그건 제가 밤새…", "shock", {C: "angry"}), sfx="thud"),
    L(C, "김 부장, 보고서에 본인이 다 했다고 썼죠? 통화 기록까지 다 확인했습니다.", "angry", {B: "shock"}),
    L(N, "고깃집 안이 쥐 죽은 듯 조용해졌어요."),
])
scene("십오 년 전, 오사카", "street", [S_, C], mood="hope", when="15년 전", flashback=True, lines=[
    L(N, "십오 년 전, 우리 회사는 부도 직전이었다고 해요. 마지막 희망이 오사카 거래처였죠."),
    L(C, "통역사 쓸 돈도 없습니다. 이 계약 못 따면 직원 백 명이 거리에 나앉아요.", "sad", {S_: "think"}),
    L(S_, "제가 해 볼게요. 통역비는 계약되면 주세요.", "happy", {C: "surprised"}),
    L(N, "일본 유학 중이던 스물두 살 학생이, 사흘 밤을 새워 계약서를 번역했대요."),
    L(C, "학생, 이름이라도 알려 주세요. 이 은혜는 꼭 갚겠습니다.", "cry", {S_: "happy"}),
    L(S_, "그럼 나중에 회사가 커지면, 저 같은 사람도 받아 주세요.", "happy"),
    L(N, "그 계약으로 회사는 살아났어요. 그런데 그 학생은 끝내 통역비를 받지 않고 사라졌습니다."),
])
s_why = scene("신입으로 온 이유", "hoesik", [C, S_, M, B], mood="sad", lines=[
    L(C, "왜 말씀 안 하셨어요. 우리 회사에 오셨다고 한마디만 하셨으면…", "sad", {S_: "sad", B: "sad"}),
    L(S_, "혼자 아이를 키우느라 팔 년을 쉬었어요. 경력이 끊긴 사람은 아무 데서도 안 받아 주더라고요.", "sad"),
    L(S_, "그래서 신입으로 지원했어요. 옛날 일로 특혜를 받고 싶진 않았어요.", "normal", {C: "sad", M: "cry"}),
    dict(L(C, "특혜가 아니라 빚입니다. 우리 회사는 십오 년 동안 한 선생님께 빚을 지고 있었어요.", "cry", {M: "cry", S_: "cry"}), sfx="ding"),
    L(N, "그 순간, 부장님 얼굴이 하얗게 질렸어요."),
])
scene("부장님의 사과", "office", [B, S_, M, J], mood="hope", lines=[
    L(N, "다음 날 아침, 부장님이 수정 씨 자리 앞에 섰어요."),
    L(B, "수정 씨… 아니, 한 선생님. 내가 정말 면목이 없습니다.", "sad", {S_: "normal", M: "think"}),
    L(B, "나도 신입 때 나이 많다고 무시당한 게 한이었는데, 똑같은 짓을 하고 있었네요.", "sad"),
    L(S_, "부장님, 저는 선생님 아니고 신입이에요. 그냥 수정 씨라고 부르세요.", "normal"),
    L(S_, "대신 커피는 앞으로 각자 타 드시는 걸로 해요.", "happy", {M: "happy", B: "sad", J: "happy"}),
    dict(L(N, "부장님은 그 주에 지방 지사로 발령이 났고, 보고서 이름은 모두 원래 주인을 찾았습니다."), sfx="ding"),
    L(J, "수정 씨, 아니 선배님! 저 일본어 좀 가르쳐 주세요!", "happy", {S_: "happy"}),
])
scene("함께 먹는 도시락", "park", [M, S_], mood="warm", lines=[
    L(N, "한 달 뒤, 수정 씨는 새로 생긴 일본 사업팀의 팀장이 됐어요."),
    L(M, "팀장님, 오늘 점심 같이 드셔도 돼요? 저도 도시락 싸 왔어요.", "happy", {S_: "surprised"}),
    L(S_, "민지 씨가 도시락을? 무슨 바람이에요?", "happy"),
    L(M, "그동안 혼자 드시게 해서 죄송했어요. 저도 부장님이랑 다를 게 없었어요.", "sad", {S_: "normal"}),
    L(S_, "아니에요. 그날 밤 옥상에 와 준 사람, 민지 씨뿐이었어요.", "happy", {M: "cry"}),
    L(M, "팀장님 수첩에, 아직도 커피 취향 적혀 있어요?", "happy"),
    L(S_, "그럼요. 이제는 우리 팀원들 생일도 적혀 있어요.", "happy"),
    L(S_, "그리고 우리 팀은 여섯 시 퇴근이에요. 팀장 명령입니다.", "happy", {M: "happy"}),
])
scene("다시, 여섯 시", "street", [S_, H], mood="hope", lines=[
    L(N, "그리고 오늘도 여섯 시 정각, 수정 팀장님은 어린이집으로 달려갑니다."),
    L(H, "엄마! 오늘도 일등!", "happy", {S_: "happy"}),
    L(S_, "그럼. 엄마 회사 사람들이 일찍 보내 줬어.", "happy"),
    L(H, "엄마 회사 사람들, 이제 진짜 좋아?", "think"),
    L(S_, "응. 이제는 진짜야.", "happy"),
])
scene("여러분께", "office", [M], mood="warm", lines=[
    L(N, "혹시 여러분 회사에도, 조용히 남의 몫까지 해내는 수정 씨가 있나요?"),
    L(N, "오늘은 그 사람에게 커피 한 잔 대신, 고맙다는 말 한마디를 건네 보세요."),
    L(M, "여러분이라면 부장님을 용서하실 건가요? 댓글로 들려주세요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "서른일곱 늦깎이 신입을 무시하던 부장, 회식 자리에 사장님이 들어오자 얼어붙었습니다"
proj = {
    "title": TITLE,
    "slug": "newbie-ceo",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Kore",
    "cast": {
        M: {"name": "민지", "gvoice": "ko-KR-Chirp3-HD-Kore", "color": "#7e57c2", "hair": "long", "hair_color": "#5a3b26", "skin": "#ffdcc0"},
        S_: {"name": "수정", "gvoice": "ko-KR-Chirp3-HD-Vindemiatrix", "color": "#4f86c6", "hair": "bun", "hair_color": "#231c1c", "skin": "#f6d2b4", "accessory": "glasses"},
        B: {"name": "김 부장", "gvoice": "ko-KR-Chirp3-HD-Schedar", "color": "#55606e", "hair": "none", "skin": "#f0c4a0", "accessory": "glasses"},
        C: {"name": "사장", "gvoice": "ko-KR-Chirp3-HD-Sadaltager", "color": "#2f3b52", "hair": "short", "hair_color": "#c9c9c9", "skin": "#efc6a2"},
        J: {"name": "준혁", "gvoice": "ko-KR-Chirp3-HD-Puck", "color": "#ef6c00", "hair": "spiky", "hair_color": "#2a2626"},
        H: {"name": "하린", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#ffd54f", "hair": "long", "hair_color": "#231c1c", "skin": "#ffe0c8", "accessory": "bow", "scale": 0.7},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (15년 전 비밀은 숨김)
    "teaser": [[s_reveal, 2, 5], [s_credit, 5, 6]],
    "shorts_speed": 1.25,
    "shorts": [
        {"clips": [[s_open, 1, 6], [s_reveal, 1, 3]], "hook": "무시하던 신입에게\n사장이 고개 숙였다",
         "hook_who": B, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "money", "text": "30억"},
         "end_text": "신입의 정체는 본편에서 ▶"},
        {"clips": [[s_credit, 1, 7]], "hook": "신입 공을 가로챈\n부장의 최후",
         "hook_who": B, "hook_emotion": "angry", "hook_tone": "gold", "hook_prop": {"type": "letter", "text": "보고서"},
         "end_text": "부장의 최후는 본편에서 ▶"},
        {"clips": [[s_roof, 1, 7]], "hook": "밤 11시 옥상에서\n들려온 일본어",
         "hook_who": M, "hook_emotion": "shock", "hook_tone": "blue", "hook_prop": {"type": "phone", "text": "오사카"},
         "end_text": "그녀의 과거는 본편에서 ▶"},
        {"clips": [[s_why, 0, 4]], "hook": "37살 신입이\n숨겨 온 15년",
         "hook_who": S_, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "photo", "text": "15년 전"},
         "end_text": "전체 이야기는 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "신입에게\n고개 숙인 사장",
        "highlight": "고개 숙인 사장",
        "badge": "회식 자리 대반전",
        "variants": [
            {"style": "story", "tone": "red", "face": [B, "shock"], "prop": {"type": "money", "text": "30억"}},
            {"style": "story", "tone": "blue", "face": [S_, "sad"], "text": "37살 신입의\n숨겨진 정체", "highlight": "숨겨진 정체",
             "badge": "끝까지 보세요", "prop": {"type": "photo", "text": "15년 전"}},
            {"style": "story", "tone": "gold", "face": [M, "shock"], "text": "밤 11시 옥상\n일본어 통화", "highlight": "일본어 통화",
             "badge": "부장만 몰랐다", "prop": {"type": "phone", "text": "오사카"}},
        ],
    },
    "publish": {
        "url": "https://youtu.be/M1D-P2WdFNE",  # 업로드된 롱폼 (쇼츠 설명·고정 댓글 링크)
        "title": TITLE,
        "title_variants": ["“신입은 커피나 타 와” 무시당하던 37살 신입의 정체가 밝혀진 회식 날",
                           "30억 계약을 살린 건 부장이 아니라, 모두가 무시하던 신입이었습니다"],
        "description": "“신입은 신입답게 커피나 타 와.” 서른일곱 살에 신입으로 들어온 수정 씨는 석 달 동안 무시를 당했습니다. 그런데 첫 회식 날, 고깃집 문을 열고 들어온 사장님이 수정 씨에게 고개를 숙입니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 부장님을 용서하시겠어요? 여러분 회사의 '수정 씨' 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #사이다사연 #직장사연",
        "tags": ["사연", "사이다 사연", "직장 사연", "회사 사연", "참교육", "갑질", "늦깎이 신입", "회식", "반전 사연", "사연 만화", "사연 애니메이션", "감동 사연", "창작 사연"],
        "category": 1,
        "playlist": "사이다 직장 사연",
        "publish_at": "2026-10-23T18:00:00+09:00",
        "pinned_comment": "여러분 회사에도 조용히 남의 몫까지 해내는 사람이 있나요? 그분께 하고 싶은 말을 댓글로 남겨 주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-24T12:00:00+09:00", "2026-10-25T19:00:00+09:00", "2026-10-26T12:00:00+09:00", "2026-10-27T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #사이다사연 #직장"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
