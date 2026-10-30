"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 며느리(화자) 시점. 결혼식 혼주 인사에서 시어머니가 친정을 깎아내리는 순간(앞당김) → 과수원집 딸 → 민수와의 만남
→ 상견례의 사과 상자 → 예단 목록 → 아빠의 굽은 등 → 시아버지의 수상한 전화 → 혼주 인사 → 30년 전 쌀 스무 포대
→ 큰절 → 시어머니의 사과 → 과수원의 첫 명절
쇼츠: 완결형 3개(롱폼 장면을 이어 붙인 2분 20초~2분 40초, 가장 센 대사로 시작) + 예고형 1개"""
import json
JH, JK, MS, MIL, FIL, DAD, MOM, N = "jihye", "jihye_kid", "minsu", "mother", "father", "dad", "mom", "narrator"


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


s_open = scene("혼주 인사", "wedding", [MIL, DAD, FIL], mood="tense", when="결혼식 날", lines=[
    L(N, "결혼식 날, 혼주 인사를 하던 시어머니가 마이크를 잡고 하객들을 둘러봤어요."),
    dict(L(MIL, "없는 집 딸 데려왔지만, 저희가 잘 가르쳐서 살게 하겠습니다.", "happy", {DAD: "sad", FIL: "angry"}), sfx="thud"),
    L(N, "하객석 맨 앞줄에서, 평생 사과 농사만 지은 우리 아빠가 고개를 숙였어요."),
    L(N, "저는 신부 입장을 기다리며, 그 모습을 문틈으로 보고 있었어요. 숨이 멎는 것 같았죠."),
    L(N, "그때, 옆에 앉아 있던 시아버지가 천천히 일어나 마이크를 받아 들었습니다."),
    L(N, "이 이야기를 하려면, 제가 자란 사과 과수원부터 말씀드려야 해요."),
])
scene("과수원집 딸", "orchard", [JK, DAD], mood="warm", when="25년 전", flashback=True, lines=[
    L(N, "저는 경북 산골 사과 과수원집 외동딸이에요."),
    L(JK, "아빠, 이 사과는 상처 났어. 못 팔겠다.", "sad", {DAD: "happy"}),
    L(DAD, "지혜야, 사과는 상처 난 게 더 달다. 비바람을 견뎌서 그래.", "happy"),
    L(JK, "그럼 아빠도 달아? 아빠 손에 상처 많잖아.", "happy", {DAD: "happy"}),
    L(DAD, "하하, 그럼. 아빠가 제일 달지.", "happy"),
    L(N, "아빠는 평생 남한테 받은 것보다 준 게 많은 사람이었어요. 그때는 그걸 몰랐죠."),
])
scene("민수를 만난 날", "cafe", [JH, MS], mood="warm", when="3년 전", lines=[
    L(N, "서울에서 직장을 다니다, 민수 씨를 만났어요."),
    L(MS, "지혜 씨네 사과, 진짜 맛있었어요. 아버님이 보내 주신 거라면서요.", "happy", {JH: "happy"}),
    L(JH, "아빠가 상처 난 것만 골라서 보냈을 거예요. 그게 더 달다고.", "happy"),
    L(MS, "저도 꼭 뵙고 싶어요. 우리 아버지도 사과 엄청 좋아하시거든요.", "happy"),
    L(MS, "아버지가 그러셨어요. 세상에서 제일 맛있는 사과는 경북 산골 사과라고.", "think", {JH: "surprised"}),
    L(JH, "경북 산골이요? 저희 집이 거기예요! 신기하다.", "surprised", {MS: "happy"}),
    L(N, "그때 민수 씨네가 강남에서 꽤 큰 회사를 한다는 건, 한참 뒤에야 알았어요."),
])
s_sang = scene("상견례", "hoesik", [MIL, DAD, MOM, FIL], mood="tense", when="결혼 석 달 전", lines=[
    L(N, "상견례 날, 아빠와 엄마는 새벽에 딴 사과를 한 상자 들고 올라왔어요."),
    L(DAD, "변변찮지만 저희 과수원에서 딴 겁니다. 드셔 보시라고요.", "happy", {MIL: "think"}),
    dict(L(MIL, "어머, 사과요? 시골에서 뭘 해 오시겠어요. 예단은 기대도 안 해요.", "happy", {DAD: "sad", MOM: "sad"}), sfx="thud"),
    L(MIL, "이건 가져가세요. 저희는 과일 잘 안 먹어서요.", "normal", {FIL: "angry"}),
    L(MOM, "사돈, 그래도 한번 드셔 보세요. 올해 사과가 유난히 달아요.", "sad", {MIL: "think"}),
    L(N, "시어머니가 사과 상자를 테이블 끝으로 밀었어요. 아빠는 웃으며 고개만 끄덕였죠."),
    L(N, "그런데 그날 시아버지는 식사 내내 말없이, 우리 아빠 얼굴만 한참 바라보고 있었어요."),
])
scene("예단 목록", "living", [JH, MIL], mood="tense", when="결혼 두 달 전", lines=[
    L(MIL, "지혜야, 예단 목록 보냈다. 다른 집들은 이 정도는 다 해.", "normal", {JH: "sad"}),
    L(JH, "어머님, 저희 집 형편에는 조금 어려울 것 같아요.", "sad"),
    L(MIL, "그러니까 처음부터 수준을 맞췄어야지. 우리 민수가 아깝다는 소리 들으면 어떡하니.", "angry", {JH: "cry"}),
    L(JH, "…네, 어머님. 최대한 해 볼게요.", "sad"),
    L(N, "저는 그 목록을 아빠한테 보여 주지 못했어요. 아빠가 또 웃으며 괜찮다고 할 게 뻔해서요."),
])
scene("민수의 다짐", "street", [JH, MS], mood="hope", when="결혼 한 달 반 전", lines=[
    L(N, "예단 목록을 받은 날, 민수 씨가 퇴근길에 저를 찾아왔어요."),
    L(MS, "지혜야, 엄마가 예단 목록 보냈다며. 미안해. 그거 신경 쓰지 마.", "sad", {JH: "sad"}),
    L(JH, "어머님 마음도 이해해. 아들 하나 키워서 장가보내는 건데.", "sad"),
    L(MS, "이해하지 마. 엄마가 틀린 거야. 내가 엄마한테 다시 말할게.", "angry", {JH: "surprised"}),
    L(MS, "그리고 아버님 사과, 우리 아버지가 몰래 다 가져가셨어. 한 알도 안 버리셨대.", "think", {JH: "surprised"}),
    L(JH, "아버님이? 상견례 날 한마디도 안 하셨잖아.", "surprised", {MS: "think"}),
    L(N, "그 말이 이상하게 오래 마음에 남았어요. 시아버지는 왜 그 사과를 몰래 챙기셨을까요."),
])
s_back = scene("아빠의 굽은 등", "orchard", [JH, DAD], mood="sad", when="결혼 한 달 전", lines=[
    L(N, "결혼 한 달 전, 집에 내려갔더니 아빠가 과수원에서 상자를 싸고 있었어요."),
    L(DAD, "지혜야, 사돈댁에 보낼 사과다. 이번엔 제일 좋은 것만 골랐다.", "happy", {JH: "sad"}),
    L(JH, "아빠, 그 집 사과 안 먹는대. 보내지 마.", "cry", {DAD: "sad"}),
    L(DAD, "괜찮다. 우리 딸 시집가는 집인데, 아빠가 할 수 있는 게 이거밖에 없다.", "happy"),
    L(N, "상자를 싸는 아빠 등이 그날따라 유난히 굽어 보였어요."),
    L(JH, "아빠, 나 결혼 그만할까. 아빠 무시당하는 거 싫어.", "cry", {DAD: "surprised"}),
    L(DAD, "무슨 소리. 민수 그 녀석 눈빛 보니까 괜찮은 놈이더라. 아빠는 하나도 안 서운하다.", "happy"),
])
s_call = scene("수상한 전화", "study", [JH, FIL], mood="calm", when="결혼식 일주일 전", lines=[
    L(N, "결혼식 일주일 전, 시댁에 들렀다가 서재 앞에서 걸음을 멈췄어요."),
    L(FIL, "형님, 이번엔 제가 갚을 차례입니다. 결혼식 날, 제가 다 말씀드리겠습니다.", "sad"),
    L(JH, "형님…? 아버님이 누구한테 형님이라고 하시는 거지?", "think"),
    L(FIL, "아니요, 이번엔 말리지 마세요. 삼십 년을 참았습니다.", "cry"),
    L(N, "전화를 끊은 시아버지는 오래된 사진 한 장을 한참 들여다보고 계셨어요."),
    L(N, "사진 속에는 낡은 트럭 앞에서 웃고 있는 젊은 남자 둘이 있었어요."),
    L(N, "그중 한 사람은, 어딘가 우리 아빠를 닮아 있었죠."),
])
s_mic = scene("혼주 인사", "wedding", [MIL, DAD, FIL, JH], mood="tense", when="결혼식 날", lines=[
    L(N, "그리고 결혼식 날, 혼주 인사 시간이 왔어요."),
    L(MIL, "오늘 와 주신 하객 여러분, 정말 감사합니다.", "happy", {DAD: "happy"}),
    dict(L(MIL, "없는 집 딸 데려왔지만, 저희가 잘 가르쳐서 살게 하겠습니다.", "happy", {DAD: "sad", JH: "shock"}), sfx="thud"),
    L(N, "하객석이 술렁였어요. 아빠는 웃으려다가, 결국 고개를 숙였어요."),
    L(JH, "아빠… 미안해. 나 때문에.", "cry", {DAD: "sad"}),
    dict(L(FIL, "잠깐만. 그 마이크, 나 좀 줘요.", "angry", {MIL: "surprised"}), sfx="ding"),
])
s_past = scene("쌀 스무 포대", "warehouse", [FIL, DAD], mood="sad", when="30년 전", flashback=True, lines=[
    L(FIL, "삼십 년 전, 저는 작은 공장을 하다가 다 망했습니다. 빚쟁이가 매일 찾아왔지요.", "sad"),
    L(FIL, "친척도 친구도 전화를 안 받았습니다. 아이들 분유 살 돈도 없었어요.", "cry", {DAD: "sad"}),
    L(DAD, "이 사장, 트럭에 쌀 스무 포대 실어 왔네. 애들 밥은 굶기지 말게.", "happy", {FIL: "cry"}),
    L(DAD, "그리고 이건 사과 판 돈이야. 공장 다시 일으키는 데 보태게.", "happy"),
    L(FIL, "형님, 이걸 어떻게 갚습니까. 저는 지금 아무것도 없습니다.", "cry"),
    L(DAD, "갚긴 뭘 갚아. 나중에 잘되면 누구 하나 밥 굶지 않게 해 주면 돼.", "happy", {FIL: "cry"}),
    L(DAD, "그리고 이 일은 아무한테도 말하지 마. 자네 집사람한테도.", "normal"),
])
s_bow = scene("큰절", "wedding", [FIL, DAD, MIL, JH], mood="hope", lines=[
    L(FIL, "그때 쌀 스무 포대를 싣고 산골에서 다섯 시간을 달려온 분이, 바로 오늘 신부 아버님입니다.", "cry", {MIL: "shock"}),
    L(FIL, "저희 회사는 그 돈으로 다시 일어났습니다. 이 결혼은 제가 먼저 부탁드린 겁니다.", "sad", {DAD: "surprised"}),
    dict(L(MIL, "여보… 그게 무슨 소리예요? 왜 나한테는 한 번도…", "shock", {FIL: "sad"}), sfx="thud"),
    L(FIL, "형님이 아무한테도 말하지 말라고 하셨어. 받은 사람이 떠벌리면 준 사람이 부끄러워진다고.", "sad"),
    L(N, "시아버지는 하객 수백 명 앞에서, 우리 아빠에게 큰절을 올렸어요."),
    L(FIL, "형님, 삼십 년 만에 인사드립니다. 그때 정말 고마웠습니다.", "cry", {DAD: "cry"}),
    L(DAD, "이 사장, 일어나게. 사람들 다 보는데 왜 이래.", "surprised", {FIL: "cry"}),
    L(DAD, "그때 일은 다 잊었습니다. 우리 딸만… 잘 부탁합니다.", "cry", {JH: "cry", MIL: "cry"}),
    L(N, "식장에 박수가 터졌어요. 시어머니는 마이크를 쥔 채, 한참 동안 아무 말도 하지 못했어요."),
])
scene("삼십 년 전 시어머니", "kitchen", [MIL], mood="sad", when="30년 전 · 시어머니의 기억", flashback=True, lines=[
    L(N, "그날 밤 시어머니가 들려준 이야기는 이랬어요."),
    L(MIL, "애가 배고프다고 우는데, 분유 통이 비었어. 쌀독도 바닥이고.", "cry"),
    L(MIL, "그날 아침, 대문 앞에 쌀 포대가 산처럼 쌓여 있었어. 나는 친정에서 보낸 줄만 알았지.", "surprised"),
    L(MIL, "남편은 아무 말도 안 했어. 누가 보냈는지 끝까지 안 알려 줬어.", "think"),
    L(MIL, "그 쌀로 우리 애들이 겨울을 났어. 민수도 그 쌀밥 먹고 컸고.", "cry"),
])
s_sorry = scene("그날 밤", "room_night", [JH, MIL], mood="sad", when="그날 밤", lines=[
    L(N, "피로연이 끝난 밤, 시어머니가 저를 따로 불렀어요."),
    L(MIL, "지혜야… 내가 오늘 무슨 짓을 한 건지 모르겠다.", "cry", {JH: "surprised"}),
    L(MIL, "그때 우리 애들 분유 값이 없어서 내가 울던 거, 기억나. 그 쌀이 어디서 왔는지 몰랐어.", "cry"),
    L(JH, "어머님, 아빠는 그런 거 정말 다 잊고 사세요.", "sad", {MIL: "cry"}),
    L(MIL, "그래서 더 부끄럽다. 상견례 날 그 사과 상자, 내가 밀어냈잖니.", "cry"),
    L(MIL, "미안하다. 사돈어른한테도, 너한테도. 정말 미안하다.", "cry", {JH: "cry"}),
    L(JH, "어머님, 다음 주에 같이 과수원 가요. 아빠가 제일 단 사과 따 놓으신대요.", "happy", {MIL: "cry"}),
    L(MIL, "그래. 이번엔 내가 상자째 다 들고 올게.", "happy"),
])
scene("과수원의 첫 명절", "orchard", [MIL, MOM, FIL, DAD], mood="warm", when="그해 추석", lines=[
    L(N, "그해 추석, 시댁 식구들이 모두 우리 과수원에 내려왔어요."),
    L(MIL, "사돈, 이 사과는 상처가 났네요. 이건 어떻게 해요?", "think", {MOM: "happy"}),
    L(MOM, "그게 제일 달아요. 하나 드셔 보세요.", "happy", {MIL: "surprised"}),
    L(MIL, "어머, 정말 다네요. 우리 집에 열 상자만 보내 주세요. 제값 다 드릴게요.", "happy", {MOM: "happy"}),
    L(FIL, "형님, 오늘은 제가 한잔 따르겠습니다.", "happy", {DAD: "happy"}),
    L(DAD, "그래, 이 사장. 아니, 이제 사돈이지.", "happy"),
    L(N, "그날 밤, 두 아버지는 삼십 년 전 그 트럭 이야기를 하며 새벽까지 술잔을 기울였어요."),
])
scene("여러분께", "park", [JH], mood="warm", lines=[
    L(N, "아빠는 지금도 그날 얘기만 나오면 손사래를 쳐요. 다 지난 일이라고요."),
    L(N, "여러분이라면 이 시어머니를 용서하실 수 있을까요? 시아버지가 마이크를 잡은 건 잘한 일일까요?"),
    L(JH, "누군가 조용히 베푼 은혜가, 언젠가 꼭 돌아온다고 믿어요.", "happy"),
    L(N, "여러분의 생각을 댓글로 들려주세요. 이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

TITLE = "상견례에서 친정을 무시한 시어머니, 결혼식 날 시아버지가 마이크를 잡고 큰절을 했다"
DESC_SHORT = "상견례에서 시골 과수원집 친정을 무시하고, 결혼식 혼주 인사에서도 '없는 집 딸'이라 말한 시어머니. 그때 시아버지가 마이크를 잡았습니다. 30년 전 쌀 스무 포대를 싣고 온 사람이 누구였는지.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #사이다사연 #감동사연 #결혼식 #시어머니 #은혜갚기 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "wedding-mic",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Erinome",
    "cast": {
        JH: {"name": "지혜", "gvoice": "ko-KR-Chirp3-HD-Erinome", "color": "#ff8a65", "hair": "long", "hair_color": "#3a2618", "skin": "#fbdcc4"},
        JK: {"name": "어린 지혜", "gvoice": "ko-KR-Chirp3-HD-Leda", "color": "#ffb74d", "hair": "long", "hair_color": "#3a2618", "skin": "#ffe0c8", "accessory": "bow", "scale": 0.7},
        MS: {"name": "민수", "gvoice": "ko-KR-Chirp3-HD-Puck", "color": "#42a5f5", "hair": "short", "hair_color": "#222222"},
        MIL: {"name": "시어머니", "gvoice": "ko-KR-Chirp3-HD-Achernar", "color": "#ad1457", "hair": "bun", "hair_color": "#3b2a20", "accessory": "glasses"},
        FIL: {"name": "시아버지", "gvoice": "ko-KR-Chirp3-HD-Iapetus", "color": "#37474f", "hair": "short", "hair_color": "#bdb7b0"},
        DAD: {"name": "친정아버지", "gvoice": "ko-KR-Chirp3-HD-Algenib", "color": "#6d8b3a", "hair": "short", "hair_color": "#9e9a96", "skin": "#e8b994"},
        MOM: {"name": "친정엄마", "gvoice": "ko-KR-Chirp3-HD-Gacrux", "color": "#a1887f", "hair": "bun", "hair_color": "#6d625a", "skin": "#eec4a2"},
    },
    "scenes": S,
    # 0:00 하이라이트: 혼주 인사와 마이크 (30년 전 사연과 큰절은 숨김)
    "teaser": [[s_sang, 2, 3], [s_mic, 2, 3], [s_mic, 5, 6]],
    "shorts_speed": 1.25,
    "shorts": [
        # 완결형 1: 혼주 인사로 시작 → 상견례 → 아빠의 등 → 마이크 → 30년 전 → 큰절
        {"format": "full", "speed": 1.0,
         "clips": [[s_mic, 2, 3], [s_sang, 1, 5], [s_back, 1, 7], [s_mic, 3, 6], [s_past, 0, 6], [s_bow, 0, 9]],
         "hook": "없는 집 딸\n데려왔지만",
         "hook_who": MIL, "hook_emotion": "happy", "hook_tone": "red", "hook_prop": {"type": "ricebag", "text": "30년 전 쌀 스무 포대"},
         "cta_line": "두 아버지의 삼십 년, 더 긴 이야기는 아래 본편에서 들려 드릴게요.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "\"없는 집 딸 데려왔지만\" 혼주 인사 중 시아버지가 마이크를 뺏었다 #시니어사연 #사이다사연 #결혼식 #시어머니",
         "description": DESC_SHORT},
        # 완결형 2: 사과 상자로 시작 → 예단 → 수상한 전화 → 마이크 → 큰절 → 사과
        {"format": "full", "speed": 1.0,
         "clips": [[s_sang, 2, 6], [4, 0, 5], [s_call, 1, 5], [s_mic, 2, 6], [s_bow, 0, 4], [s_bow, 4, 9], [s_sorry, 1, 8]],
         "hook": "시골에서 뭘\n해 오시겠어요",
         "hook_who": MIL, "hook_emotion": "happy", "hook_tone": "gold", "hook_prop": {"type": "ricebag", "text": "쌀 스무 포대"},
         "cta_line": "이 가족의 이야기 전체는 아래 본편에서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"시골에서 뭘 해 오시겠어요\" 사과 상자를 밀어낸 시어머니의 최후 #시니어사연 #사이다사연 #상견례 #며느리",
         "description": DESC_SHORT},
        # 완결형 3: 감동형 — 30년 전 쌀 트럭으로 시작 → 과수원 → 아빠의 등 → 큰절 → 과수원 명절
        {"format": "full", "speed": 1.0,
         "clips": [[s_past, 1, 3], [1, 1, 6], [s_back, 1, 7], [s_past, 0, 6], [s_bow, 0, 2], [s_bow, 4, 9], [len(S) - 2, 1, 6]],
         "hook": "쌀 스무 포대를\n싣고 온 사람",
         "hook_who": DAD, "hook_emotion": "happy", "hook_tone": "blue", "hook_prop": {"type": "ricebag", "text": "쌀 스무 포대"},
         "cta_line": "삼십 년 만에 돌아온 은혜, 처음부터 본편에서 보실 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "\"애들 밥은 굶기지 말게\" 30년 전 쌀 스무 포대의 주인 #감동사연 #은혜갚기 #결혼식 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        # 예고형: 마이크를 잡는 순간까지
        {"clips": [[s_sang, 2, 4], [s_mic, 2, 6]], "hook": "혼주 인사 중\n마이크를 뺏은 시아버지",
         "hook_who": FIL, "hook_emotion": "angry", "hook_tone": "red", "hook_prop": {"type": "ricebag", "text": "30년 전"},
         "end_text": "시아버지가 한 말은 본편에서 ▶",
         "title": "\"그 마이크, 나 좀 줘요\" #시니어사연 #사이다사연 #결혼식"},
    ],
    "thumbnail": {
        "text": "결혼식 날\n시아버지의 큰절",
        "highlight": "시아버지의 큰절",
        "badge": "사이다+감동",
        "variants": [
            {"style": "story", "tone": "red", "face": [MIL, "shock"], "prop": {"type": "ricebag", "text": "30년 전 쌀 스무 포대"}},
            {"style": "story", "tone": "gold", "face": [FIL, "cry"], "text": "마이크를 잡은\n시아버지", "highlight": "시아버지",
             "badge": "혼주 인사", "prop": {"type": "ricebag", "text": "쌀 스무 포대"}},
            {"style": "story", "tone": "blue", "face": [DAD, "cry"], "text": "30년 전\n쌀 스무 포대", "highlight": "쌀 스무 포대",
             "badge": "눈물 주의", "prop": {"type": "ricebag", "text": "30년 전"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“없는 집 딸 데려왔지만”… 혼주 인사 중 마이크를 뺏은 시아버지가 하객 앞에서 한 말",
                           "상견례에서 사과 상자를 밀어낸 시어머니, 30년 전 쌀 스무 포대의 주인을 알고 무너졌다"],
        "description": "“없는 집 딸 데려왔지만, 저희가 잘 가르쳐서 살게 하겠습니다.” 상견례에서 시골 과수원집 친정을 무시하던 시어머니가 결혼식 혼주 인사에서까지 친정아버지를 깎아내린 날. 그때 시아버지가 일어나 마이크를 받아 들었습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 이 시어머니를 용서하실 수 있을까요? 시아버지가 마이크를 잡은 건 잘한 일일까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #사이다사연",
        "tags": ["사연", "시니어사연", "사이다 사연", "감동 사연", "결혼식", "상견례", "시어머니", "시아버지", "친정아버지", "은혜 갚기", "인생이야기", "사연 만화", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-11-02T18:00:00+09:00",
        "pinned_comment": "여러분이라면 이 시어머니를 용서하실 수 있을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-11-02T18:10:00+09:00", "2026-11-03T12:00:00+09:00", "2026-11-04T12:00:00+09:00", "2026-11-04T19:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
