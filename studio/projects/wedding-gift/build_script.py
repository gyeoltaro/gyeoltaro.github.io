"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 축의금 장부의 한 줄에서 시작 → 20년 우정을 연도별로 거슬러 올라감 → 오해 → 진실 → 다시 만남"""
import json
H, S_, J, O, SO, HK, SK, N = "hayun", "sora", "minjae", "mom", "soramom", "hayun_kid", "sora_kid", "narrator"


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


s_open = scene("축의금 장부", "living", [H, J], mood="tense", when="결혼식 다음 날", lines=[
    L(N, "결혼식 다음 날, 남편과 축의금 장부를 정리하다가 한 줄에서 손이 멈췄습니다."),
    dict(L(H, "이소라… 오만 원?", "shock", {J: "surprised"}), sfx="thud"),
    L(J, "소라 씨면 자기 제일 친한 친구잖아. 잘못 적힌 거 아니야?", "think"),
    L(H, "삼 년 전 소라 결혼식 때, 나는 오십만 원 냈어. 대학생 때 알바비 모아서.", "angry", {J: "surprised"}),
    L(N, "이십 년 친구였어요. 그날 저는, 그 친구와 연을 끊기로 마음먹었습니다."),
    L(N, "그런데 그 오만 원짜리 봉투에는, 제가 끝까지 몰랐던 이야기가 담겨 있었어요."),
])
s_kid = scene("짝꿍", "classroom", [HK, SK], mood="warm", when="20년 전", flashback=True, lines=[
    L(N, "소라를 처음 만난 건 중학교 1학년 때였어요. 우리는 짝꿍이었죠."),
    L(SK, "너 도시락 안 싸 왔어? 내 거 반 먹어. 엄마가 계란말이 많이 넣어 줬어.", "happy", {HK: "surprised"}),
    L(HK, "진짜? 고마워. 나 사실 아침도 못 먹었어.", "happy"),
    L(N, "그해 우리 집은 가게가 망해서 엄마가 새벽부터 일을 나갔어요. 도시락을 쌀 사람이 없었죠."),
    L(SK, "그럼 내일부터 내가 두 개 싸 올게. 우리 엄마 손 엄청 크거든.", "happy", {HK: "cry"}),
    L(HK, "소라야, 나중에 내가 꼭 갚을게.", "cry", {SK: "happy"}),
    L(SK, "갚긴 뭘 갚아. 대신 평생 내 짝꿍 해.", "happy"),
    L(N, "소라는 그 뒤로 일 년 동안, 매일 도시락 두 개를 들고 왔습니다."),
])
scene("수능 날", "street", [H, S_], mood="warm", when="17년 전", flashback=True, lines=[
    L(N, "고3 수능 날, 저는 긴장해서 시험을 완전히 망쳤어요."),
    L(H, "소라야, 나 끝났어. 수학 시간에 머리가 하얘졌어.", "cry", {S_: "sad"}),
    L(S_, "괜찮아. 일단 이거 마셔. 꿀물이야. 너 시험 끝날 때까지 기다렸어.", "happy", {H: "cry"}),
    L(H, "너도 시험 봤잖아. 너 시험장은 여기서 한 시간 거리인데?", "surprised"),
    L(S_, "택시 타고 왔지. 너 울 것 같아서. 내 예감 맞았네.", "happy", {H: "cry"}),
    L(N, "그날 소라는 택시비로 한 달 용돈을 다 썼다는 걸, 저는 한참 뒤에야 알았어요."),
])
scene("스무 살의 약속", "park", [H, S_], mood="warm", when="15년 전", flashback=True, lines=[
    L(N, "스무 살, 우리는 공원 벤치에서 서로의 결혼식 얘기를 했어요."),
    L(S_, "하윤아, 우리 나중에 결혼하면 축의금은 무조건 백만 원이다.", "happy", {H: "happy"}),
    L(H, "백만 원? 그럼 우리 둘 다 부자 돼야겠네.", "happy"),
    L(S_, "부자 못 되면? 그럼 몸으로 때우지 뭐. 내가 네 드레스 자락 들어 줄게.", "happy"),
    L(S_, "그리고 네 결혼식 축사는 내가 한다. 너 펑펑 울리는 걸로.", "happy"),
    L(H, "약속했다? 꼭 내 결혼식 맨 앞줄에 앉아야 돼.", "happy", {S_: "happy"}),
])
s_sorawed = scene("소라의 결혼식", "wedding", [S_, H], mood="warm", when="3년 전", lines=[
    L(N, "삼 년 전, 소라가 먼저 결혼했어요. 저는 석 달 동안 아르바이트 비를 모아 오십만 원을 넣었죠."),
    L(S_, "하윤아, 이게 뭐야. 너 이거 무리했잖아.", "surprised", {H: "happy"}),
    L(H, "무리는 무슨. 너 나 중학교 때 도시락 일 년 싸 줬잖아. 이걸로도 모자라.", "happy", {S_: "cry"}),
    L(S_, "바보. 그건 그냥 우리 엄마가 싸 준 거야.", "cry"),
    L(S_, "다음은 네 차례야. 그때는 내가 제일 먼저 달려갈게.", "happy", {H: "happy"}),
    L(N, "그날 소라는 하루 종일 제 손을 놓지 않았어요."),
])
scene("뜸해진 연락", "room_night", [H], mood="calm", when="2년 전", lines=[
    L(N, "그런데 소라가 결혼하고 일 년쯤 지나면서, 연락이 점점 뜸해졌어요."),
    L(H, "소라야, 이번 주말에 밥 먹자. 내가 살게.", "happy"),
    L(N, "답장은 늘 짧았어요. 미안, 요즘 너무 바빠. 다음에 꼭."),
    L(H, "다음에, 다음에… 결혼하더니 사람이 변했네.", "think"),
    L(N, "전화를 걸면 소라는 늘 어딘가 시끄러운 곳에 있었어요. 기계 소리, 계산대 삑삑 소리 같은 게 들렸죠."),
])
scene("취소된 돌잔치", "living", [H, S_], mood="tense", when="1년 전", lines=[
    L(H, "소라야, 다음 달에 도진이 돌잔치지? 나 반지 맞춰 놨어.", "happy", {S_: "sad"}),
    L(S_, "아… 돌잔치 안 하기로 했어. 그냥 가족끼리 밥 먹으려고.", "sad"),
    L(H, "왜? 너 결혼할 때부터 돌잔치는 꼭 크게 한다며.", "surprised"),
    L(S_, "그냥… 요즘은 다들 안 해. 반지는 마음만 받을게. 진짜 고마워.", "sad", {H: "think"}),
    L(N, "그때 소라 목소리가 떨렸다는 걸, 저는 그냥 서운함으로만 들었어요."),
])
s_myday = scene("나의 결혼식", "wedding", [H, J, S_], mood="tense", when="결혼식 당일", lines=[
    L(N, "그리고 제 결혼식 날. 소라는 식이 시작하기 직전에야 헐레벌떡 들어왔어요."),
    L(S_, "하윤아, 너무 예쁘다. 진짜 너무 예뻐.", "cry", {H: "happy"}),
    L(H, "왜 이렇게 늦었어. 맨 앞줄 앉기로 했잖아.", "think"),
    L(S_, "미안해. 버스가 좀 막혔어. 식 끝나고 얘기하자.", "sad", {H: "think"}),
    L(N, "식 내내 소라는 맨 앞줄 끝자리에 앉아, 손수건으로 눈가를 계속 닦고 있었어요."),
    L(N, "그런데 식이 끝나고 사진을 찍을 때, 소라는 보이지 않았어요."),
    L(J, "소라 씨 먼저 갔나 봐. 식당에도 안 왔던데.", "think", {H: "angry"}),
])
s_sns = scene("끊어 버린 연락", "room", [H, J], mood="tense", lines=[
    L(H, "오만 원 내고, 밥도 안 먹고, 인사도 없이 가? 내가 그 정도였나 봐.", "angry", {J: "sad"}),
    L(J, "사정이 있었겠지. 전화라도 한번 해 봐.", "sad"),
    L(J, "그리고 그런 글은 올리지 마. 소라 씨도 볼 텐데.", "sad", {H: "angry"}),
    L(H, "싫어. 이십 년 동안 나만 친구였던 거야.", "cry"),
    dict(L(N, "저는 소라 번호를 차단하고, SNS에 짧은 글을 올렸어요. 사람은 축의금으로 알 수 있다고."), sfx="thud"),
    L(N, "그 글에 '좋아요'가 쌓일수록, 이상하게 마음은 더 허전했습니다."),
])
scene("엄마의 한마디", "kitchen", [H, O], mood="calm", lines=[
    L(O, "하윤아, 축의금 정리는 다 했니? 소라는 왔었고?", "normal", {H: "angry"}),
    L(H, "왔다 갔어. 오만 원 내고, 밥도 안 먹고.", "angry"),
    L(O, "소라가? 그 애가 그럴 애가 아닌데. 너 중학교 때 일 년 동안 도시락 싸 준 애야.", "surprised", {H: "think"}),
    L(H, "엄마는 맨날 소라 편이야. 사람은 변해.", "angry"),
    L(O, "사람이 변하면 다 이유가 있는 거야. 무슨 일 있는 거 아니니?", "sad", {H: "sad"}),
])
scene("식당의 밤", "hoesik", [S_], mood="sad", when="같은 날 밤, 소라", lines=[
    L(N, "같은 날 밤, 소라는 식당 주방에서 설거지를 하고 있었어요."),
    L(S_, "하윤이 글이네… 사람은 축의금으로 알 수 있다.", "cry"),
    L(S_, "그래, 맞는 말이지. 오만 원밖에 못 냈으니까.", "cry"),
    L(N, "고무장갑을 낀 채, 소라는 한참 동안 휴대폰 화면만 보고 있었대요."),
    L(S_, "그래도 우리 하윤이 드레스 입은 건 봤으니까. 그거면 됐어.", "sad"),
])
s_ticket = scene("남은 식권 한 장", "living", [H, J], mood="calm", when="일주일 뒤", lines=[
    L(N, "일주일 뒤, 웨딩홀에서 정산서와 함께 작은 봉투 하나를 보내왔어요."),
    L(J, "하객 한 분이 식권을 반납하고 가셨대. 이건 그분이 두고 간 거래.", "surprised", {H: "think"}),
    dict(L(H, "식권… 반납? 밥값 아끼라고 일부러 안 먹고 간 거야?", "shock", {J: "sad"}), sfx="ding"),
    L(N, "봉투 안에는 삐뚤삐뚤한 손글씨 쪽지가 들어 있었어요."),
    L(H, "하윤아, 축의금이 너무 작아서 밥까지 먹으면 너한테 빚지는 것 같았어. 미안해. 소라가.", "cry", {J: "sad"}),
    L(H, "이 바보… 내 결혼식 밥값 아끼려고 굶고 간 거야?", "cry"),
])
s_call = scene("소라 엄마의 전화", "kitchen", [H, SO], mood="sad", lines=[
    L(N, "저는 떨리는 손으로 소라 어머니께 전화를 걸었어요."),
    L(SO, "하윤이구나. 우리 소라가 결혼식 잘 다녀왔다고 하던데.", "happy", {H: "sad"}),
    L(H, "어머니, 소라… 요즘 무슨 일 있어요?", "sad"),
    dict(L(SO, "소라가 말 안 했구나. 사위 사업이 망해서, 빚이 몇억이야. 집도 넘어갔고.", "sad", {H: "shock"}), sfx="thud"),
    L(SO, "낮에는 마트 계산대, 밤에는 식당 설거지. 애 키우면서 일 년째 그렇게 살아.", "cry"),
    L(SO, "그 오만 원도, 일당 받은 거 그대로 넣었을 거야. 너한테는 절대 말하지 말라고 했는데.", "cry", {H: "cry"}),
    L(H, "어머니, 저 소라한테 정말 못된 글을 올렸어요.", "cry"),
    L(SO, "그 애는 그것도 다 봤어. 그래도 너 원망 한마디 안 하더라.", "sad", {H: "cry"}),
])
s_mart = scene("마트 계산대", "mart", [S_, H], mood="sad", lines=[
    L(N, "그날 저녁, 저는 소라가 일한다는 마트로 갔어요."),
    L(S_, "어서 오세요, 고객님. 봉투 필요하세요?", "normal", {H: "cry"}),
    L(S_, "…하윤아?", "shock", {H: "cry"}),
    L(H, "왜 말 안 했어. 왜 혼자 다 버텼어, 바보야.", "cry", {S_: "cry"}),
    L(S_, "말하면 네가 결혼식 망칠까 봐. 너 그날 제일 행복해야 했잖아.", "cry"),
    dict(L(S_, "오만 원밖에 못 넣어서 미안해. 백만 원 약속했는데.", "cry", {H: "cry"}), sfx="ding"),
    L(H, "백만 원이 뭐가 중요해. 맨 앞줄에 앉기로 한 약속은 지켰잖아.", "cry", {S_: "cry"}),
    L(S_, "점장님 보면 혼나. 끝나고 저기 벤치에서 기다려 줄래?", "sad", {H: "happy"}),
])
scene("도시락 두 개", "park", [H, S_], mood="hope", lines=[
    L(N, "다음 날 아침, 저는 도시락 두 개를 싸서 소라네 동네 공원으로 갔어요."),
    L(H, "이번엔 내가 싸 왔어. 계란말이 많이 넣었어.", "happy", {S_: "surprised"}),
    L(S_, "하윤아… 이거 중학교 때 내가 했던 말이잖아.", "cry"),
    L(H, "소라야, 축의금은 오만 원이었지만, 너는 나한테 이십 년 치 도시락을 줬어.", "happy", {S_: "cry"}),
    L(H, "이번엔 내가 갚을 차례야. 일 구하는 거, 우리 남편 회사 쪽으로 같이 알아보자.", "happy"),
    L(S_, "근데 하윤아, 그 글은 지워 줘. 설거지하다가 그거 생각나서 몇 번을 울었어.", "sad", {H: "sad"}),
    L(H, "벌써 지웠어. 대신 새 글 쓸 거야.", "happy"),
    L(S_, "너는 진짜… 옛날이나 지금이나 손이 너무 커.", "happy", {H: "happy"}),
])
scene("다시 쓴 글", "room", [H, J], mood="warm", when="한 달 뒤", lines=[
    L(N, "저는 SNS의 그 글을 지우고, 새 글을 올렸어요."),
    L(H, "사람은 축의금으로 알 수 없다. 내 친구는 오만 원과 함께, 밥 한 끼까지 아껴서 왔다.", "sad", {J: "happy"}),
    L(J, "이제 좀 후련해?", "happy"),
    L(H, "응. 그리고 소라, 다음 달부터 우리 회사 경리팀 나가. 면접 붙었대.", "happy", {J: "surprised"}),
    L(N, "소라는 요즘 퇴근하고, 아이 손을 잡고 우리 집에 밥을 먹으러 와요. 식권 없이요."),
])
scene("여러분께", "living", [H], mood="warm", lines=[
    L(N, "혹시 여러분도 축의금 액수 때문에 서운했던 친구가 있나요?"),
    L(N, "그 봉투 뒤에 어떤 하루가 있었는지, 한 번만 먼저 물어봐 주세요."),
    L(H, "여러분이라면 그날 소라에게 먼저 연락하셨을까요? 댓글로 들려주세요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "50만 원 냈던 친구가 내 결혼식에 5만 원… 식권도 안 받고 돌아간 이유"
proj = {
    "title": TITLE,
    "slug": "wedding-gift",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Despina",
    "cast": {
        H: {"name": "하윤", "gvoice": "ko-KR-Chirp3-HD-Despina", "color": "#5c6bc0", "hair": "long", "hair_color": "#3a2618", "skin": "#ffdcc0"},
        S_: {"name": "소라", "gvoice": "ko-KR-Chirp3-HD-Erinome", "color": "#ef8a3c", "hair": "bun", "hair_color": "#2b1f1a", "skin": "#f6d0b0"},
        J: {"name": "민재", "gvoice": "ko-KR-Chirp3-HD-Enceladus", "color": "#455a64", "hair": "short", "hair_color": "#1e1a1a"},
        O: {"name": "엄마", "gvoice": "ko-KR-Chirp3-HD-Autonoe", "color": "#ba68c8", "hair": "bun", "hair_color": "#4a3a32"},
        SO: {"name": "소라 엄마", "gvoice": "ko-KR-Chirp3-HD-Vindemiatrix", "color": "#8d6e63", "hair": "bun", "hair_color": "#a8a29c", "skin": "#f2cba8", "accessory": "glasses"},
        HK: {"name": "어린 하윤", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#7986cb", "hair": "long", "hair_color": "#3a2618", "skin": "#ffe0c8", "accessory": "bow", "scale": 0.74},
        SK: {"name": "어린 소라", "gvoice": "ko-KR-Chirp3-HD-Laomedeia", "color": "#ffb74d", "hair": "bun", "hair_color": "#2b1f1a", "skin": "#ffe0c8", "scale": 0.74},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 보여 주고 본편 시작 (마트 재회 결말은 숨김)
    "teaser": [[s_open, 1, 2], [s_ticket, 2, 3], [s_call, 3, 4]],
    "shorts_speed": 1.25,
    "shorts": [
        {"clips": [[s_open, 1, 4], [s_myday, 4, 6]], "hook": "50만 원 받고\n5만 원 낸 친구",
         "hook_who": H, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "envelope", "text": "5만 원"},
         "end_text": "봉투의 비밀은 본편에서 ▶"},
        {"clips": [[s_ticket, 1, 5]], "hook": "식권도 안 받고\n돌아간 친구",
         "hook_who": H, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "letter", "text": "미안해"},
         "end_text": "친구의 사정은 본편에서 ▶"},
        {"clips": [[s_call, 2, 6]], "hook": "친구 엄마의\n전화 한 통",
         "hook_who": SO, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "phone", "text": "소라 엄마"},
         "end_text": "두 사람의 결말은 본편에서 ▶"},
        {"clips": [[s_mart, 1, 8]], "hook": "마트 계산대에서\n다시 만난 친구",
         "hook_who": S_, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "envelope", "text": "5만 원"},
         "end_text": "전체 이야기는 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "축의금\n5만 원 친구",
        "highlight": "5만 원 친구",
        "badge": "20년 우정",
        "variants": [
            {"style": "story", "tone": "red", "face": [H, "shock"], "prop": {"type": "envelope", "text": "5만 원"}},
            {"style": "story", "tone": "blue", "face": [S_, "cry"], "text": "식권도 안 받고\n돌아간 이유", "highlight": "돌아간 이유",
             "badge": "눈물 주의", "prop": {"type": "letter", "text": "미안해"}},
            {"style": "story", "tone": "gold", "face": [H, "cry"], "text": "축의금 5만 원\n봉투의 진실", "highlight": "봉투의 진실",
             "badge": "끝까지 보세요", "prop": {"type": "envelope", "text": "5만 원"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“이소라… 오만 원?” 20년 친구와 연을 끊으려던 날 알게 된 진실",
                           "축의금 5만 원 낸 친구, 결혼식 날 밥도 안 먹고 돌아간 진짜 이유"],
        "description": "“이소라… 오만 원?” 삼 년 전 친구 결혼식에 오십만 원을 냈던 하윤. 그런데 자기 결혼식 축의금 장부에 적힌 20년 지기 친구의 이름 옆에는 오만 원. 게다가 친구는 밥도 먹지 않고 인사도 없이 돌아갔습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 그날 친구에게 먼저 연락하셨을까요? 축의금 때문에 서운했던 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #축의금 #감동사연",
        "tags": ["사연", "축의금", "감동 사연", "친구 사연", "우정", "결혼식", "축의금 5만원", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "인간관계", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-11T07:00:00+09:00",
        "pinned_comment": "축의금 액수 때문에 서운했다가 나중에 사정을 알게 된 적 있으신가요? 여러분의 이야기를 들려주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-11T07:10:00+09:00", "2026-10-11T19:00:00+09:00", "2026-10-12T12:00:00+09:00", "2026-10-12T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #축의금"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
