"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)"""
import json
S_, J, G, F, H, Y, C, N = "sujin", "junho", "mil", "fil", "haeun", "miyoung", "hyerin", "narrator"


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


s_open = scene("마지막 반찬통", "kitchen", [S_, J], mood="calm", lines=[
    L(N, "시어머니가 돌아가시고 한 달 뒤, 냉장고 맨 안쪽에서 반찬통 하나를 꺼냈습니다."),
    L(J, "여보, 그거 엄마가 마지막으로 보낸 김치 아니야?", "sad", {S_: "think"}),
    L(S_, "응. 아까워서 못 먹고 있었어. 이제 정리해야지.", "sad"),
    L(N, "통을 비우고 뒤집은 순간, 바닥에 테이프로 붙여 둔 비닐봉지가 보였어요."),
    dict(L(S_, "여보… 이거 어머니 글씨야.", "surprised", {J: "surprised"}), sfx="thud"),
    L(N, "그 쪽지를 읽고 나서야 알았습니다. 열 달 동안 매주 오던 반찬통이 무엇이었는지."),
])
scene("삼 년 전, 첫인사", "living", [S_, J, G, F], mood="warm", lines=[
    L(N, "시어머니를 처음 뵌 건 삼 년 전, 결혼 허락을 받으러 간 날이었어요."),
    L(G, "아이고, 우리 집에 딸이 하나 더 생겼네. 손이 왜 이렇게 차니.", "happy", {S_: "surprised", J: "happy"}),
    L(S_, "안녕하세요, 어머니. 수진이라고 합니다.", "normal"),
    L(F, "편하게 해라. 이 사람이 며칠 전부터 반찬만 열 가지를 했다.", "happy", {G: "happy"}),
    L(G, "수진이는 친정엄마 음식 중에 뭐가 제일 그립니?", "normal", {S_: "think"}),
    L(S_, "김치요. 근데 엄마 김치 맛이… 이제 잘 기억이 안 나요.", "sad", {G: "sad"}),
    L(N, "그때 어머니가 제 손을 오래 잡고 계셨던 게, 이상하게 지금도 생각나요."),
])
scene("매주 금요일의 택배", "living", [S_, J, H], mood="warm", lines=[
    L(N, "결혼하고 이 년쯤 지났을 무렵부터, 시어머니는 매주 금요일마다 아이스박스에 반찬을 꽉꽉 채워 보내셨어요."),
    L(H, "엄마! 할머니 택배 왔어! 엄청 무거워!", "happy", {S_: "think"}),
    L(S_, "또 왔어? 지난주 거도 아직 그대로인데.", "think"),
    L(J, "엄마가 우리 생각해서 보내는 거잖아. 고맙다고 해.", "normal", {S_: "angry"}),
    L(S_, "고맙지. 근데 냉장고 문이 안 닫혀, 준호 씨.", "angry"),
    L(N, "김치, 멸치볶음, 장조림, 나물 세 가지. 맞벌이 세 식구가 일주일에 다 먹을 수 있는 양이 아니었어요."),
])
s_trash = scene("버려지는 반찬", "kitchen", [S_, H], mood="calm", lines=[
    L(N, "새 반찬이 오는 날이면, 저는 지난주 반찬을 몰래 음식물 쓰레기통에 버렸습니다."),
    L(H, "엄마, 할머니 멸치볶음 왜 버려? 나 그거 좋아하는데.", "surprised", {S_: "surprised"}),
    L(S_, "요즘 할머니 반찬이 너무 짜. 하은이 몸에 안 좋아.", "think"),
    L(H, "그래도 할머니가 하은이 거라고 했잖아.", "sad", {S_: "sad"}),
    L(N, "정말 짰어요. 예전엔 안 그랬는데, 어느 순간부터 간이 점점 세졌거든요."),
    L(N, "빈 통은 돌려보내기도 귀찮아서 베란다 수납장에 차곡차곡 쌓아 두었습니다."),
])
scene("동료의 한마디", "cafe", [S_, C], mood="calm", lines=[
    L(C, "시어머니가 반찬 보내 주시면 좋은 거 아니야? 난 부럽기만 한데.", "happy", {S_: "think"}),
    L(S_, "매주 전화 와. 잘 먹었냐고, 통 바닥은 봤냐고. 검사받는 기분이야.", "angry"),
    L(C, "통 바닥? 그건 왜?", "think"),
    L(S_, "몰라. 깨끗이 먹었는지 보라는 거겠지.", "think"),
    L(C, "수진 씨는 친정엄마가 반찬 해 주신 적 없어?", "normal", {S_: "sad"}),
    L(S_, "우리 엄마는 나 열 살 때 돌아가셨어. 그래서 그런가, 이런 게 그냥 부담스러워.", "sad", {C: "sad"}),
    L(N, "엄마 없이 자란 저는, 누가 챙겨 주는 마음을 받는 법을 몰랐던 것 같아요."),
])
scene("추석에 본 어머니", "living", [S_, G, J], mood="calm", lines=[
    L(N, "그해 추석, 오랜만에 시댁에 갔을 때 어머니는 털모자를 쓰고 계셨어요."),
    L(S_, "어머니, 집 안에서 웬 모자세요? 살도 많이 빠지신 것 같은데.", "think", {G: "happy"}),
    L(G, "다이어트 좀 했다. 이 나이에 날씬해지니 좋더라.", "happy", {J: "think"}),
    L(J, "엄마, 어디 아픈 거 아니지? 얼굴이 너무 핼쑥해.", "think"),
    L(G, "아프긴. 수진아, 반찬통 바닥은 봤니?", "happy", {S_: "think"}),
    L(S_, "아… 네, 네. 잘 먹고 있어요.", "normal"),
    L(N, "저는 거짓말을 했어요. 통 바닥 같은 건 한 번도 들여다본 적이 없었으니까요."),
])
s_call = scene("반찬 그만 보내세요", "room_night", [S_, G], mood="tense", lines=[
    L(G, "수진아, 이번 김치는 어땠니? 간이 좀 셌지?", "happy", {S_: "think"}),
    L(S_, "어머니, 그 얘기 좀 드리려고요.", "think"),
    L(S_, "이제 반찬 그만 보내셔도 돼요. 저희 바빠서 다 못 먹고 버려요.", "angry", {G: "surprised"}),
    L(G, "…버린다고?", "surprised"),
    L(S_, "네. 솔직히 너무 짜서 하은이도 못 먹어요.", "angry", {G: "sad"}),
    L(G, "…그래. 알았다. 엄마가 눈치가 없었구나. 미안하다.", "sad"),
    dict(L(G, "그래도 수진아… 통 바닥, 한 번만 봐 다오.", "sad", {S_: "think"}), sfx="ding"),
    L(N, "저는 대답도 하지 않고 전화를 끊었어요. 그게 어머니와 나눈 마지막 통화가 될 줄은 몰랐습니다."),
])
scene("끊긴 택배", "living", [S_, J], mood="sad", lines=[
    L(N, "그 뒤로 금요일 택배가 오지 않았어요. 한 주, 두 주."),
    L(J, "엄마가 요즘 전화도 금방 끊어. 목소리에 힘도 없고.", "think", {S_: "think"}),
    L(S_, "내가 반찬 그만 보내시라고 했어. 서운하셨나 봐.", "sad"),
    L(J, "뭐? 그 말을 엄마한테 직접 했어?", "angry", {S_: "sad"}),
    L(S_, "그럼 계속 버려? 그게 더 죄송한 거잖아.", "angry"),
    L(N, "그리고 삼 주째 되던 금요일, 마지막 택배가 도착했어요. 김치 한 통뿐이었습니다."),
])
s_news = scene("시누이의 전화", "night", [S_, Y], mood="tense", lines=[
    dict(L(Y, "언니, 엄마가 쓰러졌어. 지금 응급실이야.", "sad", {S_: "surprised"}), sfx="thud"),
    L(S_, "어머니가? 왜? 어디가 편찮으셨어?", "surprised"),
    L(Y, "췌장암이래. 열 달 전에 이미 알았대. 우리한테만 말을 안 한 거야.", "sad", {S_: "shock"}),
    L(S_, "열 달 전에? 그럼 그 반찬은… 그동안 계속…", "shock"),
    L(Y, "항암 치료 받으면서도 금요일만 되면 부엌에 서 있었대. 아빠가 말려도 소용없었고.", "cry"),
    L(Y, "약 때문에 입맛을 다 잃어서 간을 못 봤대. 그래서 반찬이 짰던 거야.", "cry", {S_: "cry"}),
])
s_hosp = scene("병실에서", "hospital", [S_, G, J], mood="sad", lines=[
    L(N, "병실의 어머니는, 제가 알던 사람이 맞나 싶을 만큼 작아져 있었어요."),
    L(S_, "어머니, 왜 말씀 안 하셨어요. 그 몸으로 왜 반찬을…", "cry", {J: "sad"}),
    L(G, "왔니… 우리 며느리. 미안하다, 짜게 해서.", "sad", {S_: "cry"}),
    L(S_, "아니에요. 제가 죄송해요. 제가 정말 못된 말을…", "cry"),
    L(G, "수진아… 통 바닥… 봤니?", "sad", {S_: "think"}),
    L(S_, "통 바닥이요? 아직… 못 봤어요.", "sad"),
    L(G, "괜찮다… 천천히 봐라. 하나씩, 천천히.", "happy"),
    L(N, "어머니는 그 주를 넘기지 못하셨어요. 저는 끝내 그 말의 뜻을 여쭤보지 못했습니다."),
], lying=[G])
scene("장례식장", "memorial", [Y, S_, F], mood="sad", lines=[
    L(Y, "언니, 엄마가 언니 얘기를 제일 많이 했어.", "sad", {S_: "surprised"}),
    L(Y, "엄마 없이 큰 애라서, 자기가 엄마 노릇 해 줘야 한다고.", "sad"),
    L(F, "네 시어머니가 반찬통 들고 늘 그러더라. 우리 수진이 이거 먹고 힘내라고.", "sad", {S_: "sad"}),
    L(S_, "저는 그 반찬을… 버렸어요, 아버님.", "cry", {F: "sad"}),
    L(F, "괜찮다. 그 사람은 다 알고도 보냈을 거다.", "sad"),
])
s_note = scene("바닥의 쪽지", "kitchen", [S_, J], mood="calm", lines=[
    L(N, "그리고 다시, 그날 부엌."),
    dict(L(S_, "수진아, 네가 그립다던 엄마 김치, 내 식대로 흉내 내 본다…", "surprised", {J: "surprised"}), sfx="ding"),
    L(S_, "배추 절일 때 소금은 두 줌, 찹쌀풀은 묽게…", "sad"),
    L(S_, "레시피야. 여보, 어머니가 김치 담그는 법을 적어 놓으셨어.", "surprised", {J: "sad"}),
    L(J, "잠깐만. 베란다에 쌓아 둔 통들… 거기도 혹시?", "surprised"),
    L(N, "베란다 수납장으로 달려갔어요. 쌓여 있던 반찬통은 서른일곱 개."),
])
s_stack = scene("서른일곱 개의 반찬통", "living", [S_, J, H], mood="sad", lines=[
    dict(L(S_, "있어… 하나도 빠짐없이 다 있어.", "shock", {J: "shock", H: "surprised"}), sfx="thud"),
    L(J, "준호 감기 걸리면 콩나물국, 고춧가루는 빼고…", "cry", {S_: "cry"}),
    L(H, "엄마, 여기 내 이름 있어! 하은이 멸치볶음은 물엿 반 숟가락.", "surprised", {S_: "cry"}),
    L(S_, "수진이 입덧할 때 먹었다던 오이소박이…", "cry"),
    L(N, "열 달 동안, 매주 한 장씩. 어머니는 반찬통 바닥에 부엌을 통째로 옮겨 놓고 계셨어요."),
    L(S_, "통 바닥 봤냐고… 그걸 매주 물어보셨던 거야.", "cry", {J: "cry"}),
])
s_letter = scene("첫 번째 쪽지", "room_night", [S_, G], mood="sad", lines=[
    L(N, "가장 오래된 통 바닥에는, 레시피가 아닌 편지가 있었습니다."),
    dict(L(G, "수진아. 엄마가 할 줄 아는 게 반찬밖에 없어서, 이렇게 마음을 전한다.", "sad", {S_: "cry"}), sfx="ding"),
    L(G, "너는 엄마 손맛을 배울 시간이 없었다고 했지. 그 말이 자꾸 마음에 걸렸다.", "sad"),
    L(G, "엄마가 아프단다. 그래서 내가 아는 걸 다 적어 두려고 한다.", "sad"),
    L(G, "나중에 내가 없어도, 네 부엌에 엄마 하나는 남아 있으라고.", "sad"),
    L(G, "시어머니 말고, 그냥 엄마라고 생각해 주면 고맙겠다. 사랑한다, 우리 딸.", "happy", {S_: "cry"}),
    L(S_, "어머니… 아니, 엄마. 미안해요. 정말 미안해요.", "cry"),
])
scene("엄마의 맛", "kitchen", [S_, H, J], mood="hope", lines=[
    L(N, "그 주말, 저는 처음으로 쪽지를 보며 멸치볶음을 만들었어요."),
    L(S_, "물엿 반 숟가락… 불은 약하게, 마지막에 참깨.", "think", {H: "happy"}),
    L(H, "엄마! 이거 할머니 맛이야! 진짜 똑같아!", "happy", {S_: "cry", J: "cry"}),
    L(J, "엄마 맛이네. 여보, 고마워.", "cry"),
    L(S_, "고마운 건 어머니지. 나는 이제야 받은 거야.", "sad"),
    L(N, "서른일곱 장의 쪽지는, 지금 우리 집 냉장고에 한 장씩 붙어 있습니다."),
])
s_fri = scene("다시, 금요일", "living", [S_, F], mood="hope", lines=[
    L(N, "그리고 요즘, 금요일마다 아이스박스를 싸는 사람은 저예요."),
    L(F, "아이고, 또 이렇게 많이 보냈냐. 나 혼자 다 못 먹는다.", "happy", {S_: "happy"}),
    L(S_, "아버님, 다 못 드셔도 괜찮아요. 그리고 꼭, 통 바닥 보세요.", "happy", {F: "surprised"}),
    L(F, "통 바닥? 허허, 니 시어머니랑 똑같은 소리를 하는구나.", "happy"),
    L(N, "통 바닥에는 이렇게 적었어요. 아버님, 오늘도 맛있게 드세요. 엄마 레시피예요."),
])
scene("여러분께", "park", [S_], mood="warm", lines=[
    L(N, "혹시 여러분 냉장고에도, 귀찮아서 미뤄 둔 누군가의 반찬통이 있나요?"),
    L(N, "오늘은 그 통 바닥을 한번 들여다봐 주세요. 그리고 잘 먹었다고 전화 한 통 드려 보세요."),
    L(S_, "여러분의 엄마 반찬 이야기도 댓글로 들려주세요. 하나하나 다 읽을게요.", "happy"),
    L(N, "이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다. 구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

proj = {
    "title": "매주 반찬 보내는 시어머니가 귀찮았는데, 반찬통 바닥을 보고 무너졌습니다",
    "slug": "mil-sidedish",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Sulafat",
    "cast": {
        S_: {"name": "수진", "gvoice": "ko-KR-Chirp3-HD-Sulafat", "color": "#e57373", "hair": "long", "hair_color": "#4a3222", "skin": "#ffdcc0"},
        J: {"name": "준호", "gvoice": "ko-KR-Chirp3-HD-Orus", "color": "#5c7cfa", "hair": "short", "hair_color": "#1f1b1b"},
        G: {"name": "시어머니", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#c08457", "hair": "bun", "hair_color": "#b8b4ae", "skin": "#f2cba8", "accessory": "glasses"},
        F: {"name": "시아버지", "gvoice": "ko-KR-Chirp3-HD-Algieba", "color": "#607d6b", "hair": "short", "hair_color": "#d0d0d0", "skin": "#efc6a2"},
        H: {"name": "하은", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#f8bbd0", "hair": "long", "hair_color": "#3b2a20", "skin": "#ffe0c8", "accessory": "bow", "scale": 0.72},
        Y: {"name": "미영", "gvoice": "ko-KR-Chirp3-HD-Zephyr", "color": "#26a69a", "hair": "bun", "hair_color": "#2a2020"},
        C: {"name": "혜린", "gvoice": "ko-KR-Chirp3-HD-Despina", "color": "#ffb300", "hair": "long", "hair_color": "#6b4a2b", "accessory": "glasses"},
    },
    "scenes": S,
    "shorts_speed": 1.25,
    "shorts": [
        # clips: [장면, 시작줄, 끝줄(제외)] — 느린 해설은 빼고 결정적인 대사부터
        {"clips": [[s_open, 1, 5], [s_stack, 0, 4]], "hook": "시어머니 반찬통 바닥에\n쪽지가 붙어 있었다",
         "hook_who": S_, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "sidedish", "text": "쪽지"},
         "end_text": "쪽지의 내용은 본편에서 ▶"},
        {"clips": [[s_call, 0, 7]], "hook": "반찬 그만 보내라고\n말해 버린 며느리",
         "hook_who": G, "hook_emotion": "sad", "hook_tone": "blue", "hook_prop": {"type": "phone", "text": "어머니"},
         "end_text": "통 바닥의 비밀은 본편에서 ▶"},
        {"clips": [[s_news, 0, 6]], "hook": "반찬이 짰던 이유를\n알고 무너졌다",
         "hook_who": S_, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "sidedish", "text": "10개월"},
         "end_text": "전체 이야기는 본편에서 ▶"},
        {"clips": [[s_letter, 1, 7]], "hook": "시어머니가 남긴\n첫 번째 쪽지",
         "hook_who": S_, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "letter", "text": "우리 딸"},
         "end_text": "서른일곱 장의 쪽지는 본편에서 ▶"},
    ],
    "thumbnail": {
        "text": "귀찮던 반찬통\n바닥을 보니",
        "highlight": "바닥을 보니",
        "badge": "시어머니의 열 달",
        "variants": [
            {"style": "story", "tone": "red", "face": [S_, "cry"], "prop": {"type": "sidedish", "text": "쪽지"}},
            {"style": "story", "tone": "blue", "face": [G, "sad"], "text": "시어머니가 남긴\n쪽지 37장", "highlight": "쪽지 37장", "badge": "눈물 주의",
             "prop": {"type": "letter", "text": "우리 딸"}},
            {"style": "story", "tone": "gold", "face": [S_, "shock"], "text": "반찬이 짰던\n진짜 이유", "highlight": "진짜 이유",
             "badge": "며느리만 몰랐다", "prop": {"type": "sidedish", "text": "10개월"}},
        ],
    },
    "publish": {
        "title": "매주 반찬 보내는 시어머니가 귀찮았는데, 반찬통 바닥을 보고 무너졌습니다",
        "description": "매주 금요일 도착하던 시어머니의 반찬 택배. 냉장고 자리만 차지한다고 버리던 며느리가, 반찬통 바닥에서 쪽지를 발견합니다.\n\n⏱ 챕터\n{chapters}\n\n여러분의 엄마 반찬 이야기도 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ 합성 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #감동사연 #시어머니",
        "tags": ["사연", "감동 사연", "가족 사연", "시어머니", "며느리", "시어머니 반찬", "반찬통", "고부 사연", "반전 사연", "사연 만화", "사연 애니메이션", "눈물 사연", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-16T18:00:00+09:00",
        "pinned_comment": "여러분이 가장 그리운 엄마 반찬은 무엇인가요? 그 맛에 담긴 이야기를 댓글로 나눠 주세요 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-17T12:00:00+09:00", "2026-10-18T19:00:00+09:00", "2026-10-19T12:00:00+09:00", "2026-10-20T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["title"] = s["hook"].replace("\n", " ") + " #감동사연 #시어머니"
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines))
for i, sh in enumerate(proj["shorts"], 1):
    print("short", i, sum(len(l["text"]) for c in sh["clips"] for l in S[c[0]]["lines"][c[1]:c[2]]), "chars")
print("40자 초과:", [l["text"] for l in lines if len(l["text"]) > 45])
