"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연, 15편)
구성: 알바생(화자) 시점. 점장이 도둑으로 모는 순간(앞당김) → 새벽의 폐지 할머니 → 몰래 건넨 우유 → 도윤의 사정 → 점장의 갑질
→ 영수증 → 사라진 할머니 → 병실의 봉투 → 건물 등기부 → 20년 전 급식실 → 장부 첫 장 → 점장의 사과 → 공원
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 20초~2분 45초, 가장 센 대사로 시작) + 예고형 1개"""
import json
DY, MR, MG, KD, TC, N = "doyun", "maryae", "manager", "doyun_kid", "teacher", "narrator"


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


s_open = scene("도둑 취급", "mart", [DY, MG, MR], mood="tense", when="어느 새벽", lines=[
    L(N, "그날 새벽, 저는 편의점에서 도둑으로 몰렸어요. 폐지 줍는 할머니께 우유 하나를 건넸다는 이유로요."),
    dict(L(MG, "재고 빼돌려서 거지한테 퍼 주냐? 너 지금 도둑질한 거야, 알아?", "angry", {DY: "shock", MR: "sad"}), sfx="thud"),
    L(DY, "점장님, 그게 아니라… 저는 그냥…", "sad", {MG: "angry"}),
    L(MG, "그냥은 무슨 그냥이야! 변상하고 내일부터 나오지 마!", "angry", {DY: "cry"}),
    L(N, "창밖에서 할머니가 손수레 손잡이를 꼭 쥐고 서 있었어요. 할머니는 아무 말도 하지 못했죠."),
    L(N, "이 이야기를 하려면, 석 달 전 어느 새벽부터 말씀드려야 해요."),
])
s_first = scene("새벽의 수레", "street", [DY, MR], mood="calm", when="석 달 전", flashback=True, lines=[
    L(N, "저는 서른 살을 앞둔 취업 준비생이에요. 야간 편의점 알바로 학원비를 벌었죠."),
    L(N, "새벽 네 시쯤이면 가게 앞에 폐지 가득한 수레가 멈춰 섰어요."),
    L(MR, "학생, 미안한데 잠깐만 수레 좀 세워 놓을게. 금방 갈 거야.", "sad"),
    L(DY, "괜찮아요 할머니, 천천히 하세요. 추운데 안에서 좀 쉬다 가셔도 돼요.", "happy", {MR: "surprised"}),
    L(MR, "아이고, 고마워라. 근데 내가 이 꼴로 들어가면 손님들이 싫어해.", "sad"),
    L(DY, "손님 한 명도 없어요. 그리고 있어도 괜찮아요.", "happy"),
    L(MR, "…그래. 학생은 말이 참 곱네. 이름이 뭐야?", "happy", {DY: "happy"}),
    L(DY, "도윤이요. 김도윤.", "happy"),
    L(MR, "도윤이… 그래, 이름 좋다. 고마워요, 도윤 학생.", "happy"),
])
s_milk = scene("몰래 건넨 우유", "mart", [DY, MR], mood="warm", when="석 달 전", lines=[
    L(N, "다음 날 새벽에도 할머니는 오셨어요. 손이 빨갛게 얼어 있었죠."),
    L(N, "저는 냉장고에서 따뜻한 우유 하나를 꺼내 계산대에 찍었어요. 제 돈으로요."),
    L(DY, "할머니, 이거 유통기한 지난 거라 버릴 건데 드시겠어요?", "happy", {MR: "think"}),
    L(MR, "유통기한이 지났다고? 날짜 보니까 아직 한참 남았는데.", "think", {DY: "surprised"}),
    L(DY, "…들켰네요. 사실 제가 계산했어요. 추우시니까 따뜻한 거 한 잔 드시라고요.", "happy"),
    L(MR, "아이고 이 학생이. 내가 이런 걸 받을 처지가 못 되는데.", "cry", {DY: "sad"}),
    L(DY, "처지가 어디 있어요. 그냥 제가 드리고 싶어서 그래요.", "happy"),
    dict(L(MR, "…고마워. 평생 못 잊을 거야.", "cry", {DY: "happy"}), sfx="ding"),
    L(N, "그날부터 저는 매일 새벽 우유 하나를 자기 월급으로 계산해서 몰래 건넸어요."),
    L(N, "할머니는 한 번도 공짜로 받는 척하지 않았어요. 늘 두 손으로, 고개를 숙이고 받으셨죠."),
])
s_room = scene("도윤의 사정", "room", [DY], mood="sad", when="그 무렵", lines=[
    L(N, "솔직히 저도 넉넉해서 그런 건 아니었어요. 자취방 월세도 밀려 있었으니까요."),
    L(DY, "서류 탈락이 열여섯 번째네. 이번 달 월세는 또 어떻게 내지.", "sad"),
    L(N, "저는 컵라면을 먹으며 가계부를 쓰던 날이 많았어요. 우유값 천오백 원이 아쉬운 날도 있었죠."),
    L(DY, "그래도 할머니 우유 값은 아끼면 안 돼. 이건 이상하게 아깝지가 않아.", "happy"),
    L(N, "어릴 때 저도 누군가에게서 이런 도움을 받았던 것 같은 기분이 들었어요."),
    L(N, "그게 정확히 누구였는지, 그때는 기억나지 않았지만요."),
])
s_bully = scene("가게 앞의 점장", "street", [DY, MG, MR], mood="tense", when="어느 새벽", lines=[
    L(N, "그러던 어느 날 새벽, 점장이 예고 없이 가게에 나타났어요."),
    L(MG, "저기요, 할머니! 수레 좀 치우세요. 가게 앞에 이런 거 세워 두면 장사 방해돼요.", "angry", {MR: "sad"}),
    L(MR, "미안해요. 금방 치울게요. 잠깐 쉬고 있었어요.", "sad"),
    L(MG, "여기가 쉼터예요? 냄새나는 폐지 쌓아 두고 손님 다 쫓아내는 게 보이지도 않아요?", "angry", {DY: "shock"}),
    L(DY, "점장님, 새벽엔 손님이 거의 없어요. 그리고 할머니는 잠깐…", "sad", {MG: "angry"}),
    dict(L(MG, "넌 입 다물어. CCTV 다 봤으니까.", "angry", {DY: "shock"}), sfx="thud"),
    L(MG, "도윤 씨, 재고 빼돌려서 저런 사람한테 퍼 준 거 내가 모를 줄 알았어?", "angry"),
    L(N, "수레를 끄는 할머니의 뒷모습이 그날따라 한없이 작아 보였어요."),
])
s_receipt = scene("영수증", "mart", [DY, MG], mood="hope", when="그날 아침", lines=[
    L(N, "저는 숨을 한 번 깊게 쉬고, 가방에서 클리어파일 하나를 꺼냈어요."),
    L(DY, "점장님, 이거 한번 보세요. 지난 석 달 치 영수증이에요.", "normal", {MG: "surprised"}),
    L(MG, "뭐야 이게… 우유? 매일 하나씩, 정가로 계산했네?", "surprised"),
    L(DY, "재고를 빼돌린 적은 없습니다. 전부 제 월급으로 계산했어요. 전표 번호도 맞춰 보세요.", "normal"),
    L(MG, "그, 그래도 이런 걸 왜 네 돈으로…", "think", {DY: "happy"}),
    L(DY, "추운 날 따뜻한 우유 한 잔 드리는 게 그렇게 잘못된 일인가요?", "sad"),
    dict(L(MG, "…쯧. 아무튼 다음부터는 가게 앞에 수레 못 세우게 해. 알겠지?", "think"), sfx="ding"),
    L(N, "점장은 말을 돌렸지만, 제 손에 들린 영수증을 한참 쳐다보고 있었어요."),
])
s_gone = scene("비어 있는 가게 앞", "night", [DY], mood="sad", when="일주일 뒤", lines=[
    L(N, "그런데 그날 이후 할머니가 보이지 않았어요. 하루, 이틀, 사흘, 그리고 일주일."),
    L(DY, "할머니가 점장님 말 때문에 안 오시는 걸까. 내가 괜히 영수증을 꺼내서…", "cry"),
    L(N, "저는 새벽마다 가게 앞을 내다보며 따뜻한 우유를 하나씩 계산했어요. 주인 없는 우유가 냉장고에 쌓여 갔죠."),
    L(DY, "내일 폐지 수거장 쪽으로 가 봐야겠다. 무슨 일 있으신 건 아닐까.", "sad"),
    L(N, "다음 날 오전, 저는 골목 끝 폐지 수거장 사장님을 찾아갔어요."),
    L(N, "사장님은 제 얼굴을 보더니 뜻밖의 말을 했어요. 막례 할머니, 열흘 전에 쓰러져서 병원에 입원했다고요."),
])
s_hosp = scene("병실의 봉투", "hospital", [DY, MR], mood="sad", when="그날 오후", lines=[
    L(N, "저는 사장님이 알려 준 병원으로 달려갔어요. 병실 문을 열자 할머니가 힘없이 웃고 계셨어요."),
    L(MR, "아이고, 도윤 학생이네. 여기가 어떻게 알고 왔어.", "happy", {DY: "sad"}),
    L(DY, "할머니, 왜 말씀 안 하셨어요. 우유 하나 못 드린 게 얼마나 마음에 걸렸는데요.", "cry"),
    L(MR, "나 때문에 학생이 점장한테 얼마나 혼났을까 싶어서, 일부러 안 갔지.", "sad", {DY: "cry"}),
    L(DY, "저는 괜찮아요. 그것보다 할머니 몸이 더 걱정이에요.", "sad"),
    L(MR, "내가 학생한테 부탁이 하나 있어. 이 봉투, 점장한테 좀 전해 줘.", "normal"),
    L(MR, "단, 학생은 열어 보면 안 돼. 꼭 점장이 직접 열어야 해.", "normal", {DY: "surprised"}),
    L(DY, "알겠어요 할머니. 꼭 전해 드릴게요. 얼른 나으셔야 해요.", "sad"),
    L(N, "저는 낡은 서류 봉투를 가슴에 안고 병원을 나섰어요. 그 안에 뭐가 들었는지 상상도 못 했죠."),
])
s_env = scene("건물의 주인", "mart", [DY, MG], mood="tense", when="그날 저녁", lines=[
    L(N, "저는 출근하자마자 점장에게 봉투를 건넸어요."),
    L(DY, "점장님, 폐지 할머니께서 이걸 전해 달라고 하셨어요. 점장님이 직접 열어 보시래요.", "normal", {MG: "think"}),
    L(MG, "거지 할머니가 나한테 뭘 줘? 설마 사정하는 편지겠지.", "normal"),
    L(N, "점장이 비웃으며 봉투를 열었어요. 그런데 안에서 나온 서류를 보자 점장의 얼굴이 하얗게 변했어요."),
    dict(L(MG, "이, 이게 뭐야… 이 건물 등기부등본…? 소유자 이름이… 김막례?", "shock", {DY: "surprised"}), sfx="thud"),
    L(DY, "네? 이 건물이 할머니 거라고요?", "surprised", {MG: "shock"}),
    L(MG, "우리 가게 임대인이… 할머니였다고? 내가 지금까지 월세를 낸 사람이 저 할머니였다고?", "shock"),
    L(N, "점장은 휘청거리며 의자에 주저앉았어요. 서류 맨 뒤에는 할머니의 짧은 편지도 한 장 붙어 있었죠."),
])
s_past = scene("20년 전 급식실", "schoolgate", [KD, TC, MR], mood="sad", when="20년 전", flashback=True, lines=[
    L(TC, "도윤아, 급식비 아직 못 냈지? 이번 달까지 안 내면 점심을 못 먹어.", "sad", {KD: "cry"}),
    L(KD, "선생님, 엄마가 이번 주 안에 꼭 낸대요. 저 점심 안 먹어도 괜찮아요.", "cry"),
    L(TC, "배고픈 아이를 굶길 수는 없지. 선생님이 알아볼게.", "sad"),
    L(MR, "선생님, 저 폐지 판 돈이 조금 있는데요. 이걸로 급식비 못 내는 아이 좀 도와줄 수 있을까요?", "sad", {TC: "surprised"}),
    L(TC, "어머니, 이 돈은 쉽게 모은 돈이 아니잖아요. 정말 괜찮으세요?", "surprised"),
    L(MR, "우리 아들도 어릴 때 밥 한 끼 못 먹고 학교 다녔어요. 밥은 굶기면 안 돼요.", "sad"),
    L(TC, "…알겠습니다. 이 아이에게는 후원자가 있다고만 전하겠습니다.", "cry"),
    L(N, "그날 이후 저는 졸업할 때까지 점심을 굶은 적이 없었어요. 누가 내 줬는지는 끝내 몰랐죠."),
])
s_ledger = scene("장부의 첫 장", "hospital", [DY, MR, MG], mood="hope", when="그날 밤", lines=[
    L(N, "점장이 편지를 읽다 말고 저를 데리고 병원으로 달려갔어요. 병실에서 할머니가 장부 한 권을 펼쳐 보였죠."),
    L(MR, "점장님, 놀라게 해서 미안해요. 나는 그냥 가게 앞에서 쉬고 싶었을 뿐이에요.", "sad", {MG: "cry"}),
    L(MG, "할머니… 아니, 사장님. 제가 죄송합니다. 정말 몰랐습니다.", "cry"),
    L(MR, "이 장부 좀 봐요. 우리 남편 죽고 나서 폐지 줍기 시작한 지 20년이에요.", "normal", {DY: "surprised"}),
    L(MR, "이 돈으로 동네 아이들 급식비를 내 줬어요. 한 명 한 명 이름을 다 적어 뒀지.", "happy"),
    dict(L(MR, "맨 앞 장 이름 좀 봐요. 도윤이. 초등학교 때 급식비 못 내던 도윤이.", "happy", {DY: "shock"}), sfx="ding"),
    L(DY, "제 이름이요? 설마 그 후원자가… 할머니였어요?", "shock", {MR: "happy"}),
    L(MR, "처음 가게에서 얼굴 봤을 때 바로 알아봤어. 눈매가 그대로더라.", "cry", {DY: "cry"}),
    L(MR, "그래서 학생이 주는 우유를 받았어. 한 번쯤은 내가 받아도 되지 싶어서.", "happy"),
    L(N, "저는 그 자리에서 소리 내어 울어 버렸어요. 20년 전의 은혜가 우유 한 잔으로 돌아온 거였으니까요."),
])
s_end = scene("점장의 사과", "street", [DY, MG, MR], mood="warm", when="일주일 뒤", lines=[
    L(N, "일주일 뒤, 할머니가 퇴원하던 날이에요. 점장이 병원 앞까지 찾아왔어요."),
    L(MG, "사장님, 제가 그동안 큰 잘못을 했습니다. 월세도 올려 주시고 싶은 대로 하세요.", "cry", {MR: "sad"}),
    L(MR, "월세는 그대로 둬요. 점장님이 월세 때문에 가게 접으면 도윤이 같은 학생은 어디서 일하누.", "happy"),
    L(MR, "대신 부탁 하나만 해요. 도윤이 같은 사람은 쓰다듬어 주고 일하게 해 줘요.", "normal", {MG: "cry"}),
    L(MG, "네, 알겠습니다. 도윤 씨한테도, 정말 미안해요.", "cry", {DY: "happy"}),
    L(DY, "점장님, 괜찮아요. 저도 말씀 못 드린 게 있었으니까요.", "happy"),
    L(MR, "도윤아, 그 우유 말이야. 내가 평생 받은 것 중에 제일 비싼 선물이었다.", "happy", {DY: "cry"}),
    L(N, "점장은 그날부터 가게 앞 수레 자리에 작은 의자를 하나 놓아 두었어요."),
])
s_fin = scene("여러분께", "park", [DY, MR], mood="warm", when="한 달 뒤", lines=[
    L(N, "한 달 뒤, 저는 정규직 면접에 합격했어요. 이력서에 쓴 마지막 한 줄은 편의점 야간 근무 석 달이었죠."),
    L(MR, "도윤아, 이거 먹어. 내가 오늘은 우유를 샀어. 따뜻하게 데웠다.", "happy", {DY: "happy"}),
    L(DY, "할머니, 오늘은 제가 살 차례인데요.", "happy"),
    L(MR, "이번엔 내가 살래. 20년 만에 처음으로 밥값 내는 거야.", "happy"),
    L(N, "저는 따뜻한 우유를 두 손으로 받았어요. 그날 우유는 평생 마신 것 중 제일 따뜻했어요."),
    L(N, "작은 친절이 20년 뒤 돌아오기도 한다는 걸, 저는 할머니께 배웠어요."),
    L(N, "여러분이라면 도윤이처럼 하실 수 있을까요? 댓글로 들려주세요."),
    L(N, "※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다."),
])

TITLE = "폐지 줍는 할머니에게 매일 우유를 건넨 편의점 알바생, 할머니가 남기고 간 봉투를 열고 주저앉았습니다"
TITLE = "폐지 줍는 할머니께 우유를 건넨 알바생, 할머니가 남긴 봉투를 열고 주저앉았습니다"
DESC_SHORT = "새벽마다 폐지 줍는 할머니께 몰래 우유를 건네던 편의점 알바생. 점장은 그를 도둑으로 몰았고, 사라진 할머니가 남긴 봉투에는 뜻밖의 서류가 있었습니다.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #감동사연 #사이다사연 #편의점 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "convenience-milk",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Orus",
    "cast": {
        DY: {"name": "도윤", "gvoice": "ko-KR-Chirp3-HD-Orus", "color": "#26a69a", "hair": "spiky", "hair_color": "#222222", "skin": "#fbdcc4"},
        MR: {"name": "막례 할머니", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#8d6e63", "hair": "bun", "hair_color": "#b7b2ad", "skin": "#e8b994"},
        MG: {"name": "점장", "gvoice": "ko-KR-Chirp3-HD-Fenrir", "color": "#c62828", "hair": "short", "hair_color": "#333333", "accessory": "glasses"},
        KD: {"name": "어린 도윤", "gvoice": "ko-KR-Chirp3-HD-Zephyr", "color": "#ffca28", "hair": "short", "hair_color": "#222222", "skin": "#ffe0c8", "scale": 0.6},
        TC: {"name": "선생님", "gvoice": "ko-KR-Chirp3-HD-Kore", "color": "#7e57c2", "hair": "long", "hair_color": "#3a2618"},
    },
    "scenes": S,
    "teaser": [[s_open, 1, 3], [s_env, 4, 6], [s_ledger, 5, 6]],
    "shorts_speed": 1.25,
    "shorts": [
        {"format": "full", "speed": 1.0,
         "clips": [[s_open, 1, 5], [s_first, 2, 7], [s_milk, 2, 8], [s_bully, 1, 8], [s_receipt, 1, 7], [s_hosp, 5, 8], [s_env, 3, 7]],
         "hook": "재고 빼돌려서\n거지한테 퍼 주냐",
         "hook_who": MG, "hook_emotion": "angry", "hook_tone": "red", "hook_prop": {"type": "envelope", "text": "할머니의 봉투"},
         "cta_line": "할머니가 남긴 봉투의 뒷이야기, 아래 본편에서 이어집니다.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"거지한테 퍼 주냐\" 점장이 알바생을 도둑으로 몰았다 #시니어사연 #사이다사연 #편의점",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_env, 4, 8], [s_ledger, 0, 3], [s_past, 0, 7], [s_ledger, 3, 9], [s_end, 1, 8]],
         "hook": "맨 앞 장 이름이\n도윤이",
         "hook_who": MR, "hook_emotion": "happy", "hook_tone": "gold", "hook_prop": {"type": "ledger", "text": "20년 치 급식비"},
         "cta_line": "20년 만에 돌아온 은혜, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"맨 앞 장 이름 좀 봐요. 도윤이\" 20년 전 급식비의 주인 #감동사연 #은혜갚기 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.0,
         "clips": [[s_bully, 5, 8], [s_receipt, 1, 7], [s_gone, 2, 6], [s_hosp, 1, 8], [s_env, 4, 8], [s_ledger, 5, 9], [s_fin, 1, 5]],
         "hook": "평생 받은 것 중\n제일 비싼 선물",
         "hook_who": MR, "hook_emotion": "happy", "hook_tone": "blue", "hook_prop": {"type": "envelope", "text": "할머니의 봉투"},
         "cta_line": "우유 한 잔의 진짜 사연, 본편에서 이어서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"그 우유가 평생 받은 것 중 제일 비싼 선물이었다\" #감동사연 #할머니 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"clips": [[s_bully, 1, 3], [s_env, 3, 5]], "hook": "폐지 할머니의\n봉투를 연 점장",
         "hook_who": MG, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "envelope", "text": "할머니의 봉투"},
         "end_text": "봉투 속 서류는 본편에서 ▶",
         "title": "\"이 건물 소유자가 김막례?\" #시니어사연 #사이다사연 #편의점"},
    ],
    "thumbnail": {
        "text": "할머니가 남긴\n봉투 한 장",
        "highlight": "봉투 한 장",
        "badge": "사이다+감동",
        "variants": [
            {"style": "story", "tone": "red", "face": [MG, "shock"], "prop": {"type": "envelope", "text": "할머니의 봉투"}},
            {"style": "story", "tone": "gold", "face": [DY, "cry"], "text": "맨 앞 장 이름은\n도윤이", "highlight": "도윤이",
             "badge": "눈물 주의", "prop": {"type": "ledger", "text": "20년 치 급식비"}},
            {"style": "story", "tone": "blue", "face": [MR, "cry"], "text": "제일 비싼\n선물", "highlight": "비싼 선물",
             "badge": "할머니의 20년", "prop": {"type": "envelope", "text": "건물 등기부"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“재고 빼돌려서 거지한테 퍼 주냐”… 알바생을 도둑으로 몬 점장이 봉투 속 서류를 보고 얼어붙었다",
                           "폐지 할머니께 몰래 우유를 건넨 편의점 알바생, 20년 전 급식비의 후원자를 알고 무너졌다"],
        "description": "“재고 빼돌려서 거지한테 퍼 주냐?” 새벽마다 폐지 줍는 할머니께 따뜻한 우유를 건네던 편의점 알바생을 점장이 도둑으로 몰았습니다. 그리고 할머니가 남긴 낡은 봉투 속에는 점장이 얼어붙을 서류가 들어 있었습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 도윤이처럼 하실 수 있을까요? 점장의 사과를 받아 주실 수 있을까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #감동사연",
        "tags": ["사연", "시니어사연", "사이다 사연", "감동 사연", "편의점", "폐지 할머니", "알바생", "은혜 갚기", "급식비", "인생이야기", "사연 만화", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-11-06T18:00:00+09:00",
        "pinned_comment": "여러분이라면 도윤이처럼 하실 수 있을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-11-06T18:10:00+09:00", "2026-11-07T12:00:00+09:00", "2026-11-08T12:00:00+09:00", "2026-11-08T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
