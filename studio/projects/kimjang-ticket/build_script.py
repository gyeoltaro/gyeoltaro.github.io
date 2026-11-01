"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연, 16편)
구성: 며느리(화자) 시점. 시어머니가 기차표를 내미는 순간(앞당김) → 10년째 김장 → 마당의 수육 → 일기장 → 전화
→ 새벽 4시의 시어머니 → 이미 끝난 김장 → 부산행 KTX 표와 일기장 → 남편의 배웅 → 친정 마당 → 엄마와 김장 → 마무리
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 20초~2분 45초, 가장 센 대사로 시작) + 예고형 1개"""
import json
SJ, MIL, HB, NJ, MOM, NB, N = "sujin", "mil", "husband", "sister", "mom", "neighbor", "narrator"


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


s_open = scene("기차표", "yard", [SJ, MIL, NJ], mood="tense", when="올해 김장 날", lines=[
    L(N, "올해 김장 날, 시어머니가 제 앞에 봉투를 내밀었어요. 김치통이 아니라 기차표였어요."),
    dict(L(MIL, "올해는 네 친정엄마 김장 도와드려라. 사돈이 혼자 하신다고 들었다.", "normal", {SJ: "shock", NJ: "surprised"}), sfx="thud"),
    L(NJ, "엄마, 무슨 소리야! 김장은 언니가 해야 하는 거잖아!", "angry", {MIL: "angry"}),
    L(MIL, "10년을 혼자 한 애한테 올해는 내가 하고 싶었다. 너는 거들떠도 안 봤잖니.", "angry", {NJ: "shock"}),
    L(N, "저는 그 자리에서 아무 말도 못 하고 서 있었어요. 눈물이 먼저 나왔거든요."),
    L(N, "이 이야기를 하려면, 10년 전 첫 김장부터 말씀드려야 해요."),
])
s_ten = scene("10년째 김장", "kitchen", [SJ, MIL], mood="sad", when="10년 전부터", flashback=True, lines=[
    L(N, "결혼 첫해 11월, 시어머니는 저에게 앞치마를 내밀었어요. 배추 백 포기가 마당에 쌓여 있었죠."),
    L(MIL, "새아기야, 김장은 며느리가 해야 맛이 나는 거다. 열심히 배워라.", "normal", {SJ: "surprised"}),
    L(SJ, "네, 어머님. 열심히 할게요.", "happy"),
    L(N, "그해에는 일이 서툰 줄 알고 참았어요. 둘째 해에도, 셋째 해에도요."),
    L(MIL, "간이 싱겁구나. 올해도 영 별로네. 이래서 쓰겠니?", "normal", {SJ: "sad"}),
    L(SJ, "죄송해요, 어머님. 다음엔 더 잘할게요.", "sad"),
    L(N, "열 번의 김장 동안 칭찬은 한 번도 들어 보지 못했어요. 손톱 밑이 빨갛게 물들어도 괜찮다고 했죠."),
    L(N, "저는 그냥 며느리는 원래 이런 거라고 생각했어요."),
])
s_suyuk = scene("마당의 수육", "yard", [SJ, HB, NJ], mood="tense", when="작년 김장", lines=[
    L(N, "작년 김장 날이었어요. 저는 새벽 다섯 시부터 열 시간째 배추를 버무리고 있었죠."),
    L(NJ, "오빠, 수육 맛있다. 언니가 해 준 김치랑 먹으니까 더 맛있네.", "happy", {HB: "happy"}),
    L(HB, "그치? 역시 김장은 수진이 손이 제일이야. 수진아, 우리 먹고 있을게!", "happy"),
    L(SJ, "…응, 천천히 먹어. 나는 좀 더 하고 갈게.", "sad", {HB: "happy"}),
    dict(L(NJ, "언니, 이거 좀 짜다. 다음엔 간 좀 신경 써 줘요. 엄마 입맛에 맞춰야지.", "normal", {SJ: "shock"}), sfx="thud"),
    L(N, "그 순간 손에 든 고무장갑이 갑자기 너무 무겁게 느껴졌어요."),
    L(N, "저는 속으로 다짐했어요. 올해가 마지막이라고."),
])
scene("일기장 속 한 줄", "room_night", [SJ, HB], mood="sad", when="올해 가을", lines=[
    L(N, "저는 매년 김장 날 밤마다 몰래 일기장을 썼어요. 남편은 그걸 몰랐죠."),
    L(SJ, "엄마 보고 싶다. 올해도 엄마 김장 못 도와드렸네. 엄마 혼자 얼마나 힘드실까.", "cry"),
    L(N, "친정은 부산이라 멀기도 했지만, 시댁 김장 때문에 한 번도 갈 수가 없었어요."),
    L(HB, "수진아, 올해 김장 날짜 잡혔어. 11월 셋째 주 토요일이래.", "happy", {SJ: "sad"}),
    L(SJ, "자기야, 올해는 나 정말 힘들 것 같아. 열 번이야, 열 번.", "sad", {HB: "surprised"}),
    L(HB, "에이, 어머니가 서운해하셔. 한 번만 더 해 줘. 부탁이야.", "normal", {SJ: "cry"}),
    dict(L(SJ, "…그럼 내가 어머님께 직접 말씀드릴게.", "sad"), sfx="ding"),
    L(N, "그렇게 저는 처음으로 시어머니께 거절의 말을 꺼내기로 했어요."),
])
scene("전화 한 통", "living", [SJ, MIL], mood="tense", when="김장 일주일 전", lines=[
    L(N, "김장 일주일 전, 저는 떨리는 손으로 시어머니께 전화를 걸었어요."),
    L(SJ, "어머님, 저 수진이에요. 올해는 제가 몸이 안 좋아서 일찍 못 갈 것 같아요.", "sad"),
    L(MIL, "…몸이 안 좋다고? 어디가?", "think"),
    L(SJ, "그냥 좀… 요즘 많이 지쳐서요. 죄송합니다, 어머님.", "sad"),
    L(MIL, "…그래. 알았다.", "sad"),
    L(N, "시어머니는 한참 말이 없다가, 그 한마디만 하고 전화를 끊었어요."),
    L(N, "저는 수화기를 든 채로 한참 서 있었어요. 야단을 맞을 줄 알았는데 이상하게 더 무서웠죠."),
    L(SJ, "어머님이 단단히 서운하셨나 봐. 어떡하지.", "cry"),
])
scene("새벽 네 시", "kitchen", [MIL, NB], mood="sad", when="김장 날 새벽 · 시어머니의 기억", flashback=True, lines=[
    L(N, "그날 새벽 네 시, 시댁 부엌에는 불이 켜져 있었다고 해요."),
    L(NB, "아이고 형님, 이 새벽에 뭐 하세요. 배추 백 포기를 혼자 하시려고요?", "surprised", {MIL: "sad"}),
    L(MIL, "응. 이번엔 내가 하려고. 우리 며느리가 몸이 안 좋다잖아.", "happy"),
    L(NB, "형님 허리도 안 좋으신데. 며느리가 안 하면 딸한테 시키세요.", "sad"),
    L(MIL, "우리 며느리가 10년 동안 얼마나 힘들었는지, 나는 이제야 알겠어.", "sad", {NB: "think"}),
    L(MIL, "작년에 김장 끝나고 보니까, 그 애 손가락이 퉁퉁 부어 있더라. 그걸 보고도 내가 입을 닫았어.", "cry"),
    dict(L(NB, "형님…", "sad", {MIL: "cry"}), sfx="ding"),
    L(N, "시어머니는 얼음장 같은 물에 배추를 씻으며, 혼자 그렇게 중얼거리셨대요."),
])
s_arrive = scene("이미 끝난 김장", "yard", [SJ, MIL, NJ], mood="hope", when="김장 날 오전", lines=[
    L(N, "저는 눈치를 보며 시댁에 갔어요. 안 가면 더 마음이 불편할 것 같았거든요."),
    L(SJ, "어머님, 저 왔어요. 몸은 좀 괜찮아져서…", "sad"),
    L(N, "그런데 마당에는 이미 절임 배추와 양념이 다 끝나 있었어요. 동네 할머니들이 김칫독을 채우고 계셨죠."),
    dict(L(SJ, "어머님, 이게 다 뭐예요? 설마 혼자 다 하신 거예요?", "shock", {MIL: "happy"}), sfx="thud"),
    L(NJ, "엄마, 왜 이렇게 무리를 해! 언니가 하면 되잖아!", "angry", {MIL: "angry"}),
    L(MIL, "10년을 혼자 한 애한테 올해는 내가 하고 싶었다. 너희는 거들떠도 안 봤잖니.", "angry", {NJ: "shock"}),
    L(NJ, "엄마…", "sad"),
    L(N, "시누이는 그제야 고개를 숙였어요. 마당이 쥐 죽은 듯 조용해졌죠."),
])
s_ticket = scene("봉투와 일기장", "room", [SJ, MIL], mood="warm", when="그날 오후", lines=[
    L(MIL, "수진아, 이리 와서 앉아 봐라. 줄 게 있다.", "happy", {SJ: "surprised"}),
    L(MIL, "여기, 부산 가는 KTX 표다. 내일 아침 첫 열차야. 두 장 샀다.", "happy"),
    L(SJ, "어머님, 이게 무슨…", "surprised"),
    L(MIL, "올해는 네 친정엄마 김장 도와드려라. 사돈이 혼자 하신다고 들었다. 이 어미 대신 인사도 드리고.", "happy", {SJ: "cry"}),
    L(SJ, "어머님, 저는 친정 김장 이야기 한 번도 안 했는데, 어떻게 아셨어요?", "cry"),
    dict(L(MIL, "작년에 네 방 청소하다가 일기장을 봤다. 훔쳐보려던 건 아닌데… 엄마 보고 싶다는 글이 있더라.", "sad", {SJ: "shock"}), sfx="thud"),
    L(MIL, "10년 동안 시댁 김장 때문에 친정 한 번을 못 간 거, 이 어미가 모르고 있었다.", "sad"),
    L(SJ, "어머님… 죄송해요, 제가 말씀드렸어야 했는데.", "cry"),
    L(MIL, "죄송할 사람은 너가 아니라 나다. 열 번이나 김장을 시켜 놓고 칭찬 한마디 안 했어.", "cry", {SJ: "cry"}),
    L(N, "저는 그 자리에서 무릎을 꿇고 소리 내어 울었어요. 시어머니도 제 손을 꼭 잡고 우셨죠."),
])
scene("남편의 배웅", "street", [SJ, HB], mood="warm", when="다음 날 아침", lines=[
    L(N, "다음 날 새벽, 남편이 저를 역까지 데려다 줬어요."),
    L(HB, "수진아, 내가 정말 미안해. 10년 동안 너 혼자 그렇게 힘들었는데 눈치도 못 챘어.", "sad", {SJ: "surprised"}),
    L(SJ, "자기 잘못만은 아니야. 나도 말을 못 했으니까.", "sad"),
    L(HB, "아니야. 이제 김장은 우리 둘이 같이 하자. 어머니랑 여동생까지 다 같이.", "normal"),
    L(HB, "그리고 장모님 뵈면 내가 큰절 올리러 못 가서 죄송하다고 꼭 전해 줘.", "sad"),
    L(SJ, "…응, 전할게. 자기도 몸 챙기고.", "happy", {HB: "happy"}),
    L(N, "기차가 출발하자 남편이 플랫폼에서 한참 손을 흔들었어요. 저는 창밖을 보며 또 울었죠."),
])
s_mom = scene("친정 마당", "yard", [SJ, MOM], mood="sad", when="그날 오전", lines=[
    L(N, "열 번의 겨울을 건너뛴 끝에, 저는 친정 마당에 들어섰어요."),
    L(SJ, "엄마, 나 왔어. 수진이 왔어.", "cry", {MOM: "surprised"}),
    L(MOM, "아이고 내 새끼야! 연락도 없이 이게 웬일이니!", "surprised"),
    L(SJ, "엄마, 미안해. 10년 동안 한 번도 못 와서. 김장도 못 도와드리고.", "cry"),
    L(MOM, "무슨 소리야, 이 사람아. 시집간 딸이 얼마나 바쁜 줄 내가 다 알아.", "cry", {SJ: "cry"}),
    L(MOM, "그런데 사돈이 보내신 이 김치 좀 봐라. 어제 택배로 왔다.", "happy"),
    L(N, "엄마 손에는 시어머니가 보낸 김치 한 통과 손 편지 한 장이 들려 있었어요."),
])
s_letter = scene("사돈의 편지", "living", [SJ, MOM], mood="hope", when="그날 오후", lines=[
    L(N, "엄마는 안경을 쓰고 편지를 천천히 읽어 주었어요."),
    L(MOM, "사돈, 우리 수진이 곱게 키워 주셔서 고맙습니다. 저희 집에서 10년 동안 너무 고생을 시켰습니다.", "cry"),
    L(MOM, "올해는 사돈 댁에서 김장을 도와 드리라고 보냅니다. 이 어미가 대신 인사드립니다.", "cry", {SJ: "cry"}),
    dict(L(SJ, "엄마… 어머님이 이런 편지를…", "cry"), sfx="ding"),
    L(MOM, "수진아, 네 시어머니가 참 좋은 분이시다. 딸이 이런 집에 가서 얼마나 다행인지 몰라.", "happy"),
    L(SJ, "맞아 엄마. 나 처음으로 시어머니께 인사드리고 싶은 마음이 들었어.", "happy", {MOM: "happy"}),
    L(N, "그날 저는 엄마와 나란히 앉아, 10년 치 이야기를 쏟아 놓았어요."),
])
s_kimchi = scene("엄마와 함께", "kitchen", [SJ, MOM], mood="warm", when="그날 저녁", lines=[
    L(N, "그날 저녁, 저는 엄마와 나란히 서서 김장 양념을 버무렸어요."),
    L(MOM, "수진아, 간은 이만하면 됐다. 어쩜 이렇게 솜씨가 늘었니.", "happy", {SJ: "happy"}),
    L(SJ, "시어머니께 10년 배웠거든요. 엄마 입맛에 맞을지는 모르겠지만.", "happy"),
    L(MOM, "맛있다. 정말 맛있어. 우리 딸 손이 이렇게 컸구나.", "cry"),
    L(N, "엄마의 한마디가 열 번의 김장 칭찬보다 더 오래 마음에 남았어요."),
    L(N, "그때 시어머니에게서 전화가 걸려 왔어요."),
    L(MIL, "수진아, 잘 도착했니? 사돈 모시고 맛있는 거 많이 먹어라. 김치는 우리가 잘 챙겨 놓을게.", "happy", {SJ: "cry"}),
    L(SJ, "어머님, 고맙습니다. 올해는 저도 어머님께 갚을 차례예요.", "cry"),
])
s_fin_idx = scene("여러분께", "park", [SJ, MIL], mood="warm", when="한 달 뒤", lines=[
    L(N, "한 달 뒤, 저는 시어머니 손을 잡고 시장에 갔어요. 김장 속에 넣을 굴을 사러요."),
    L(MIL, "수진아, 올해 김치는 어땠니? 사돈이 맛있다고 하시더구나.", "happy", {SJ: "happy"}),
    L(SJ, "어머님 김치가 제일이에요. 내년엔 제가 어머님 옆에서 배울게요.", "happy"),
    L(MIL, "내년엔 같이 하자. 이젠 며느리가 아니라 우리 딸이다.", "cry", {SJ: "cry"}),
    L(N, "저는 이제 압니다. 10년의 서운함은 한마디 말에 녹을 수 있다는 걸요."),
    L(N, "여러분이라면 시어머니께 어떻게 인사드리셨을까요? 댓글로 들려주세요."),
    L(N, "※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다."),
])

TITLE = "10년 동안 김장을 혼자 떠맡은 며느리, 올해 시어머니가 김치통 대신 기차표를 내밀었다"
DESC_SHORT = "10년 동안 시댁 김장을 혼자 해 온 며느리에게 올해 시어머니가 내민 것은 김치통이 아니라 부산행 기차표였습니다.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #감동사연 #김장 #시어머니 #며느리 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "kimjang-ticket",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Callirrhoe",
    "cast": {
        SJ: {"name": "수진", "gvoice": "ko-KR-Chirp3-HD-Callirrhoe", "color": "#e57373", "hair": "long", "hair_color": "#2f2118", "skin": "#fbdcc4"},
        MIL: {"name": "시어머니", "gvoice": "ko-KR-Chirp3-HD-Achernar", "color": "#6d4c6f", "hair": "bun", "hair_color": "#8e8985", "skin": "#e8b994"},
        HB: {"name": "남편", "gvoice": "ko-KR-Chirp3-HD-Puck", "color": "#5c7cbf", "hair": "short", "hair_color": "#222222"},
        NJ: {"name": "시누이", "gvoice": "ko-KR-Chirp3-HD-Despina", "color": "#f06292", "hair": "long", "hair_color": "#4a3020"},
        MOM: {"name": "친정엄마", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#a1887f", "hair": "bun", "hair_color": "#6d625a", "skin": "#eec4a2"},
        NB: {"name": "이웃 할머니", "gvoice": "ko-KR-Chirp3-HD-Vindemiatrix", "color": "#81a58a", "hair": "bun", "hair_color": "#b7b2ad", "skin": "#e8b994"},
    },
    "scenes": S,
    "teaser": [[s_open, 1, 3], [s_ticket, 5, 6], [s_letter, 3, 4]],
    "shorts_speed": 1.25,
    "shorts": [
        {"format": "full", "speed": 1.0,
         "clips": [[s_open, 1, 5], [s_ten, 1, 8], [s_suyuk, 1, 7], [s_arrive, 1, 8], [s_ticket, 2, 9], [s_mom, 1, 4]],
         "hook": "올해는 네 친정엄마\n김장 도와드려라",
         "hook_who": MIL, "hook_emotion": "happy", "hook_tone": "red", "hook_prop": {"type": "envelope", "text": "부산행 KTX 표"},
         "cta_line": "시어머니가 건넨 기차표의 사연, 아래 본편에서 이어집니다.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"올해는 네 친정엄마 김장 도와드려라\" 시어머니가 내민 기차표 #시니어사연 #감동사연 #김장",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_arrive, 3, 8], [s_suyuk, 1, 7], [s_ten, 4, 8], [s_ticket, 5, 10], [s_letter, 1, 6], [s_mom, 3, 7]],
         "hook": "10년을 혼자 한 애한테\n올해는 내가",
         "hook_who": MIL, "hook_emotion": "angry", "hook_tone": "gold", "hook_prop": {"type": "envelope", "text": "10년 치 김장"},
         "cta_line": "며느리의 10년, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"10년을 혼자 한 애한테 올해는 내가 하고 싶었다\" 시어머니의 마당 호통 #감동사연 #김장 #시어머니 #눈물주의",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_ticket, 5, 10], [s_mom, 1, 7], [s_letter, 0, 7], [s_kimchi, 1, 8], [s_fin_idx, 1, 4]],
         "hook": "일기장 속\n엄마 보고 싶다",
         "hook_who": SJ, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "envelope", "text": "시어머니의 편지"},
         "cta_line": "일기장 속 한 줄의 비밀, 본편에서 이어서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"작년에 네 일기장을 봤다\" 시어머니가 알고 있던 한 줄 #감동사연 #시어머니 #친정엄마 #눈물주의",
         "description": DESC_SHORT},
        {"clips": [[s_open, 1, 4], [s_ticket, 3, 5]], "hook": "시어머니가 내민 건\n김치통이 아니었다",
         "hook_who": MIL, "hook_emotion": "happy", "hook_tone": "red", "hook_prop": {"type": "envelope", "text": "부산행 KTX 표"},
         "end_text": "기차표의 사연은 본편에서 ▶",
         "title": "\"올해는 네 친정엄마 김장 도와드려라\" #시니어사연 #감동사연 #김장"},
    ],
    "thumbnail": {
        "text": "김치통 대신\n기차표",
        "highlight": "기차표",
        "badge": "감동 사연",
        "variants": [
            {"style": "story", "tone": "red", "face": [SJ, "shock"], "prop": {"type": "envelope", "text": "부산행 KTX 표"}},
            {"style": "story", "tone": "gold", "face": [MIL, "cry"], "text": "10년을 혼자 한 애한테\n올해는 내가", "highlight": "올해는 내가",
             "badge": "눈물 주의", "prop": {"type": "envelope", "text": "10년 치 김장"}},
            {"style": "story", "tone": "blue", "face": [SJ, "cry"], "text": "일기장 속\n엄마 보고 싶다", "highlight": "엄마 보고 싶다",
             "badge": "며느리의 10년", "prop": {"type": "envelope", "text": "시어머니의 편지"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“올해는 네 친정엄마 김장 도와드려라”… 10년 김장을 혼자 한 며느리에게 시어머니가 내민 것",
                           "10년 동안 시댁 김장을 혼자 한 며느리, 김장 날 마당에서 시어머니의 호통을 듣고 무너졌다"],
        "description": "“올해는 네 친정엄마 김장 도와드려라. 사돈이 혼자 하신다고 들었다.” 10년 동안 시댁 김장을 혼자 해 온 며느리에게 시어머니가 김치통 대신 기차표를 내밀었습니다. 시어머니가 알고 있던 일기장 속 한 줄은 무엇이었을까요.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 시어머니께 어떻게 인사드리셨을까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #감동사연",
        "tags": ["사연", "시니어사연", "감동 사연", "김장", "시어머니", "며느리", "친정엄마", "고부", "인생이야기", "사연 만화", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-11-08T18:00:00+09:00",
        "pinned_comment": "여러분이라면 시어머니께 어떻게 인사드리셨을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-11-08T18:10:00+09:00", "2026-11-09T12:00:00+09:00", "2026-11-10T12:00:00+09:00", "2026-11-10T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
