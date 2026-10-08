"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)"""
import json
W_, D, K, E, B, G, R, N = "seoyeon", "doyun", "jihu", "eunbi", "banjang", "guard", "realtor", "narrator"


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


s_open = scene("이혼 서류", "living", [W_, D], mood="tense", when="이혼 7일 전", lines=[
    L(N, "결혼 10주년을 일주일 앞둔 밤, 저는 남편 앞에 이혼 서류를 내밀었습니다."),
    L(W_, "도윤 씨, 여기 도장 찍어. 다음 주 금요일에 법원 가자.", "angry", {D: "surprised"}),
    L(D, "…이유는 안 물어볼게. 대신 일주일만 시간 줘.", "sad", {W_: "angry"}),
    L(W_, "일주일 동안 뭐 할 건데? 또 새벽에 들어오게?", "angry"),
    dict(L(N, "그리고 이혼 전날 밤, 몰래 남편을 따라갔다가 저는 그 자리에 주저앉았습니다."), sfx="thud"),
    L(N, "모든 건 여섯 달 전부터 시작됐어요."),
])
scene("달라진 남편", "kitchen", [W_, D, K], mood="calm", when="여섯 달 전", lines=[
    L(N, "여섯 달 전부터 남편이 이상해졌어요. 새벽 두세 시에 들어와서, 해가 뜨기 전에 나갔죠."),
    L(W_, "요즘 왜 이렇게 늦어? 지후가 아빠 얼굴 본 지 일주일 됐어.", "think", {D: "sad", K: "sad"}),
    L(D, "회사에 일이 좀 많아. 조금만 참아 줘.", "sad"),
    L(K, "아빠, 오늘은 같이 저녁 먹어?", "happy", {D: "sad"}),
    L(D, "미안해, 지후야. 아빠 또 나가 봐야 해.", "sad", {K: "sad", W_: "angry"}),
    L(N, "남편은 휴대폰을 늘 뒤집어 놓았고, 잠금 비밀번호도 바꿨어요."),
])
s_money = scene("사라진 200만 원", "room_night", [W_], mood="tense", lines=[
    L(N, "그러다 은행 앱을 열어 본 날, 손이 떨렸어요."),
    dict(L(W_, "매달 200만 원씩… 김정숙? 이 사람이 누군데?", "shock"), sfx="thud"),
    L(N, "다섯 달 동안, 한 번도 빠지지 않고 같은 이름으로 돈이 빠져나가고 있었어요."),
    L(W_, "우리 지후 학원비 아끼자고 할 땐 언제고… 이 돈은 다 어디로 간 거야.", "cry"),
    L(W_, "물어볼까… 아니야. 또 회사 일이라고 하겠지. 증거부터 찾자.", "think"),
    L(N, "그날 밤, 저는 처음으로 이혼이라는 단어를 검색했습니다."),
])
scene("친구의 조언", "cafe", [W_, E], mood="tense", lines=[
    L(E, "새벽에 들어오고, 폰 뒤집어 놓고, 매달 모르는 사람한테 송금? 그거 백 퍼센트야.", "angry", {W_: "sad"}),
    L(W_, "도윤 씨가 그럴 사람이 아닌데… 십 년을 살았는데.", "sad"),
    L(E, "다들 그렇게 말해. 증거 모아. 감정 말고 증거.", "think"),
    L(W_, "물어보면 맨날 회사 일이래. 얼굴이 너무 피곤해 보여서 더 못 묻겠어.", "think", {E: "angry"}),
    L(E, "서연아, 정신 차려. 너 혼자 지후 키울 준비부터 해.", "angry"),
])
s_phone = scene("잠든 남편의 휴대폰", "living", [W_, D], mood="tense", lines=[
    L(N, "그날 밤, 소파에서 쓰러지듯 잠든 남편의 휴대폰에 메시지가 왔어요."),
    dict(L(W_, "새벽 네 시까지 와요, 기다릴게… 이게 뭐야?", "shock", {D: "sad"}), sfx="thud"),
    L(N, "보낸 사람은 '반장님'. 저는 그 이름 뒤에 누가 있는지 상상하느라 밤을 꼬박 새웠어요."),
    L(W_, "무슨 반장이길래 새벽 네 시에 만나자는 건데.", "angry"),
    L(D, "…조금만 더… 금요일까지만…", "sad", {W_: "angry"}),
    L(N, "잠꼬대마저 금요일이었어요. 저는 남편이 그날만 기다리는 줄 알았습니다."),
])
scene("아들의 질문", "room", [W_, K], mood="sad", lines=[
    L(K, "엄마, 엄마랑 아빠 헤어져?", "sad", {W_: "surprised"}),
    L(W_, "누가 그래? 그런 거 아니야.", "surprised"),
    L(K, "어제 아빠가 차 안에서 울고 있었어. 쓰레기 버리러 나갔다가 봤어.", "sad", {W_: "shock"}),
    L(W_, "아빠가… 울었어?", "shock"),
    L(K, "응. 핸들에 머리 대고 한참 있었어. 내가 창문 두드리니까 하품하는 척했어.", "sad"),
    L(N, "그날 처음으로, 남편이 숨기는 게 바람이 아닐 수도 있겠다는 생각이 들었어요."),
])
s_promise = scene("10년 전의 약속", "park", [W_, D], mood="warm", when="10년 전", flashback=True, lines=[
    L(N, "십 년 전, 우리는 이 공원에서 결혼을 약속했어요."),
    L(W_, "나 언젠가 내 이름 건 빵집 할 거야. 아침마다 갓 구운 빵 냄새 나는 가게.", "happy", {D: "happy"}),
    L(D, "좋다. 그럼 결혼 10주년엔 내가 꼭 열어 줄게. 서연 베이커리.", "happy"),
    L(D, "간판은 내가 직접 달 거야. 동네에서 제일 크게.", "happy", {W_: "happy"}),
    L(W_, "말만 들어도 배부르다. 약속했어?", "happy"),
    L(N, "하지만 지후가 태어나고, 저는 제빵 학원을 그만뒀어요. 그 꿈은 그렇게 잊혀졌습니다."),
])
scene("다친 손", "living", [W_, D], mood="tense", when="이혼 5일 전", lines=[
    L(N, "이혼 닷새 전, 새벽 다섯 시에 들어온 남편의 손에 붕대가 감겨 있었어요."),
    L(W_, "손은 또 왜 그래?", "think", {D: "surprised"}),
    L(D, "아, 회사 계단에서 넘어졌어. 별거 아니야.", "normal"),
    L(W_, "거짓말도 성의 있게 해. 옷에서 먼지 냄새가 나.", "angry", {D: "sad"}),
    L(D, "서연아… 금요일까지만. 금요일까지만 기다려 줘.", "sad"),
    L(N, "그날 남편 차 뒷좌석에는 낡은 담요 한 장과 컵라면 상자가 있었어요."),
    L(N, "금요일. 우리가 법원에 가기로 한 날이자, 결혼 10주년이었어요."),
])
s_company = scene("남편의 회사", "street", [W_, G], mood="tense", when="이혼 3일 전", lines=[
    L(N, "사흘 전, 저는 도시락을 싸 들고 남편 회사로 찾아갔어요. 직접 확인하고 싶었거든요."),
    L(W_, "저기요, 7층 한빛물산에 남편이 다니는데요. 잠깐 올라가도 될까요?", "normal", {G: "think"}),
    dict(L(G, "한빛물산이요? 거기 여섯 달 전에 부도나서 문 닫았는데요.", "surprised", {W_: "shock"}), sfx="thud"),
    L(W_, "네? 그럴 리가요. 남편은 매일 출근하는데요.", "shock"),
    L(G, "아이고, 그 회사 직원들 그때 월급도 못 받고 다 나갔어요.", "sad", {W_: "cry"}),
    L(G, "사장은 해외로 떠났다던데, 남은 직원들만 불쌍하지.", "sad"),
    L(N, "그럼 남편은 여섯 달 동안, 매일 어디로 출근한 걸까요?"),
])
scene("미행을 결심하다", "night", [W_, E], mood="tense", lines=[
    L(W_, "은비야, 도윤 씨 회사 여섯 달 전에 망했대.", "cry", {E: "shock"}),
    L(E, "뭐? 그럼 그동안 매일 어디 간 거야?", "shock"),
    L(W_, "모르겠어. 근데 이제는 무서워. 바람보다 더 나쁜 일이면 어떡해.", "cry"),
    L(E, "그럼 직접 봐. 내일 밤에 따라가 보자. 나도 같이 갈게.", "think", {W_: "sad"}),
    L(E, "지후는 우리 엄마한테 맡기자. 무슨 일이 있어도 애가 보면 안 되니까.", "think"),
    L(W_, "응… 어쩌면 이게 우리 부부의 마지막 밤일지도 모르겠다.", "sad"),
    L(N, "이혼 전날 밤, 저는 친구 차를 빌려 남편의 차를 따라갔습니다."),
])
s_drive = scene("이혼 전날 밤", "street", [W_, E], mood="tense", when="이혼 전날", lines=[  # 몰래 지켜보는 장면: 남편은 화면 밖 목소리만
    L(N, "남편이 차를 세운 곳은 번화가 술집 앞이었어요. 그리고 남의 차 운전석에 올라탔죠."),
    L(W_, "대리운전…? 저 사람이 왜 대리운전을…", "shock"),
    L(N, "취한 손님은 남편에게 반말로 소리를 질렀고, 남편은 몇 번이고 고개를 숙였어요."),
    L(D, "네, 사장님. 죄송합니다. 안전하게 모셔다드리겠습니다.", "sad", {W_: "cry", E: "sad"}),
    L(W_, "은비야, 저 사람 좀 봐. 어떻게 사람한테 저렇게 막 대해…", "cry", {E: "sad"}),
    L(E, "서연아, 저게 바람피우는 사람 얼굴이야? 저건… 버티는 사람 얼굴이야.", "sad", {W_: "cry"}),
    L(N, "그렇게 밤 열두 시부터 새벽 세 시까지, 남편은 세 번의 대리를 뛰었어요."),
])
s_wh = scene("새벽 네 시, 물류센터", "warehouse", [D, B, W_], mood="sad", lines=[
    L(N, "새벽 네 시. 남편의 차가 멈춘 곳은 도시 외곽의 물류센터였어요."),
    L(B, "도윤 씨, 손 다 터졌는데 오늘은 좀 쉬어. 내가 대신 넣어 줄게.", "sad", {D: "normal"}),
    L(D, "괜찮아요, 반장님. 이번 주만 채우면 돼요. 금요일까지만요.", "happy"),
    L(N, "숨어서 지켜보던 저를, 반장님이 먼저 발견했어요."),
    L(B, "혹시 사모님이세요? 도윤 씨가 여섯 달째 하루도 안 빠지고 나와요.", "surprised", {W_: "cry"}),
    dict(L(B, "낮엔 일자리 구하러 다니고, 밤엔 대리, 새벽엔 여기. 잠은 차에서 자고요.", "sad", {W_: "cry"}), sfx="ding"),
])
s_dawn = scene("들켜 버린 남편", "night", [W_, D], mood="sad", lines=[
    L(D, "서연아… 여기 어떻게…", "shock", {W_: "cry"}),
    L(W_, "왜 말 안 했어? 회사 망한 거, 왜 혼자 다 짊어졌어!", "cry"),
    L(W_, "당신 손 좀 봐. 이렇게 될 때까지 왜 아무 말도…", "cry", {D: "sad"}),
    L(D, "지후 학원비는 이번 달 것까지 미리 넣어 놨어. 그건 걱정하지 마.", "sad"),
    L(D, "말하면 당신이 또 다 포기할 거잖아. 지후 낳고 빵 학원 그만둔 것처럼.", "sad", {W_: "surprised"}),
    L(W_, "그게 지금 무슨 상관인데…", "cry"),
    L(D, "내일 법원 가기 전에, 한 군데만 같이 가 줘. 도장은 그다음에 찍을게.", "sad"),
])
s_bakery = scene("법원 대신 간 곳", "bakery", [W_, D, R], mood="hope", when="이혼 당일", lines=[
    L(N, "결혼 10주년이자, 이혼하기로 한 날 아침. 남편이 저를 데려간 곳은 작은 빵집이었어요."),
    L(R, "아, 오셨어요? 제가 김정숙이에요. 이 가게 건물주예요.", "happy", {W_: "surprised"}),
    L(R, "남편분이 다섯 달 동안 보증금을 매달 이백씩 나눠서 내셨어요. 오늘로 다 채우셨고요.", "happy", {W_: "shock"}),
    dict(L(D, "서연 베이커리. 10주년에 열어 준다고 했잖아. 많이 늦어서 미안해.", "sad", {W_: "cry"}), sfx="ding"),
    L(W_, "바보야… 회사도 없으면서 무슨 빵집이야. 손이 이게 뭐야…", "cry"),
    L(D, "회사는 또 구하면 돼. 근데 당신 꿈은, 더 미루면 영영 못 열 것 같았어.", "sad", {W_: "cry"}),
])
scene("찢어 버린 서류", "living", [W_, D, K], mood="hope", lines=[
    L(N, "그날 밤, 저는 남편 앞에서 이혼 서류를 반으로 찢었어요."),
    L(W_, "의심해서 미안해. 혼자 아프게 둬서 미안해.", "cry", {D: "sad"}),
    L(D, "내가 미안하지. 말 안 해서, 무섭게 해서.", "sad", {W_: "cry"}),
    L(W_, "그 큰돈을, 손이 다 터지도록 여섯 달 만에 모은 거야?", "sad"),
    L(D, "당신이 접어 둔 십 년에 비하면, 여섯 달은 아무것도 아니야.", "happy", {W_: "cry"}),
    L(K, "엄마 아빠, 이제 안 헤어져?", "happy", {W_: "happy", D: "happy"}),
    L(D, "응. 대신 우리 지후, 이제 빵 많이 먹어야 된다.", "happy", {K: "happy"}),
])
scene("서연 베이커리", "bakery", [W_, D, B, E], mood="warm", when="두 달 뒤", lines=[
    L(N, "두 달 뒤, 서연 베이커리가 문을 열었어요."),
    L(E, "서연아, 미안해. 내가 바람이라고 막 몰아붙였잖아.", "sad", {W_: "happy"}),
    L(W_, "아니야. 네 덕분에 따라갔고, 그래서 알았어.", "happy"),
    L(B, "도윤 씨, 우리 센터 관리직 자리 났어. 이번엔 정규직이야.", "happy", {D: "surprised"}),
    L(D, "반장님, 정말요? 이제 밤에 자도 되는 거예요?", "happy"),
    L(N, "남편은 이제 새벽 다섯 시가 아니라, 저녁 여섯 시에 집에 들어옵니다."),
    L(W_, "오늘 첫 빵은 당신 거야. 십 년 묵은 내 꿈, 지켜 줘서 고마워.", "happy", {D: "happy"}),
])
scene("여러분께", "park", [W_], mood="warm", lines=[
    L(N, "혹시 여러분 곁에도, 힘든 걸 혼자 짊어지고 웃는 사람이 있나요?"),
    L(N, "의심하기 전에, 오늘은 먼저 물어봐 주세요. 요즘 많이 힘들지 않냐고."),
    L(W_, "여러분이라면 그날 이혼 서류를 찢으셨을까요? 댓글로 들려주세요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "결혼 10주년에 이혼 서류를 내민 날, 전날 밤 남편을 따라갔다가 주저앉았습니다"
proj = {
    "title": TITLE,
    "slug": "divorce-eve",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Achernar",
    "cast": {
        W_: {"name": "서연", "gvoice": "ko-KR-Chirp3-HD-Achernar", "color": "#ec407a", "hair": "long", "hair_color": "#2e1f18", "skin": "#ffdcc0"},
        D: {"name": "도윤", "gvoice": "ko-KR-Chirp3-HD-Iapetus", "color": "#3f6fb5", "hair": "short", "hair_color": "#1e1a1a", "skin": "#f2c9a6"},
        K: {"name": "지후", "gvoice": "ko-KR-Chirp3-HD-Laomedeia", "color": "#66bb6a", "hair": "spiky", "hair_color": "#1e1a1a", "skin": "#ffe0c8", "scale": 0.7},
        E: {"name": "은비", "gvoice": "ko-KR-Chirp3-HD-Pulcherrima", "color": "#ffa726", "hair": "bun", "hair_color": "#6a3d2a"},
        B: {"name": "반장", "gvoice": "ko-KR-Chirp3-HD-Rasalgethi", "color": "#8d6e63", "hair": "short", "hair_color": "#9e9e9e", "skin": "#e8b892"},
        G: {"name": "경비원", "gvoice": "ko-KR-Chirp3-HD-Umbriel", "color": "#455a64", "hair": "short", "hair_color": "#e0e0e0", "skin": "#efc6a2", "accessory": "glasses"},
        R: {"name": "건물주", "gvoice": "ko-KR-Chirp3-HD-Erinome", "color": "#ab47bc", "hair": "long", "hair_color": "#b0aaa4", "skin": "#f2cba8"},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (빵집 결말은 숨김)
    "teaser": [[s_company, 2, 3], [s_wh, 4, 6], [s_dawn, 1, 2]],
    "shorts_speed": 1.25,
    "shorts": [
        {"clips": [[s_open, 1, 4], [s_phone, 1, 5]], "hook": "결혼 10주년에\n이혼 서류를 내밀었다",
         "hook_who": W_, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "letter", "text": "이혼 서류"},
         "end_text": "남편의 비밀은 본편에서 ▶"},
        {"clips": [[s_company, 1, 6]], "hook": "남편 회사에 갔더니\n6개월 전 부도",
         "hook_who": W_, "hook_emotion": "shock", "hook_tone": "gold", "hook_prop": {"type": "phone", "text": "한빛물산"},
         "end_text": "남편이 간 곳은 본편에서 ▶"},
        {"clips": [[s_wh, 1, 6]], "hook": "새벽 4시\n물류센터의 남편",
         "hook_who": D, "hook_emotion": "sad", "hook_tone": "blue", "hook_prop": {"type": "money", "text": "월 200만 원"},
         "end_text": "200만 원의 정체는 본편에서 ▶"},
        {"clips": [[s_bakery, 1, 6]], "hook": "이혼 당일\n남편이 건넨 열쇠",
         "hook_who": W_, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "key", "text": "서연 베이커리"},
         "end_text": "전체 이야기는 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "이혼 전날\n남편 미행",
        "highlight": "남편 미행",
        "badge": "결혼 10주년",
        "variants": [
            {"style": "story", "tone": "red", "face": [W_, "shock"], "prop": {"type": "letter", "text": "이혼 서류"}},
            {"style": "story", "tone": "blue", "face": [D, "sad"], "text": "매달 사라진\n200만 원", "highlight": "200만 원",
             "badge": "끝까지 보세요", "prop": {"type": "money", "text": "월 200만 원"}},
            {"style": "story", "tone": "gold", "face": [W_, "cry"], "text": "이혼 당일\n남편의 열쇠", "highlight": "남편의 열쇠",
             "badge": "눈물 주의", "prop": {"type": "key", "text": "서연 베이커리"}},
        ],
    },
    "publish": {
        "url": "https://youtu.be/aYcg16WBE28",  # 업로드된 롱폼 (쇼츠 설명·고정 댓글 링크)
        "title": TITLE,
        "title_variants": ["“회사 일이야” 매달 200만 원씩 사라지던 남편, 이혼 전날 밤 따라가 봤습니다",
                           "여섯 달 전 망한 회사에 매일 출근하던 남편, 새벽 4시 물류센터에 있었습니다"],
        "description": "“도윤 씨, 여기 도장 찍어.” 새벽에 들어오고, 휴대폰을 숨기고, 매달 200만 원씩 모르는 사람에게 돈을 보내던 남편. 결혼 10주년을 일주일 앞두고 이혼 서류를 내민 아내는, 이혼 전날 밤 남편을 몰래 따라갑니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 그날 이혼 서류를 찢으셨을까요? 여러분의 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #부부사연 #감동사연",
        "tags": ["사연", "부부 사연", "감동 사연", "이혼", "이혼 서류", "남편", "결혼 10주년", "실직", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-30T18:00:00+09:00",
        "pinned_comment": "힘든 걸 말 못 하고 혼자 버틴 적 있으신가요? 그때 듣고 싶었던 한마디를 댓글로 남겨 주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-31T12:00:00+09:00", "2026-11-01T19:00:00+09:00", "2026-11-02T12:00:00+09:00", "2026-11-03T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #부부"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
