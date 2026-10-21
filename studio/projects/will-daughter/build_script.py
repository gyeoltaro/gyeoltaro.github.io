"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 며느리(화자) 시점. 유언장 낭독에서 도둑으로 몰리는 장면(앞당김) → 남편 장례식 → 치매 진단 → 혼자 지낸 명절
→ '우리 딸'이라 부르던 밤 → 인감 찾으러 온 시누이들 → 마지막 맑은 밤 → 장례식 → 낭독(8년 전 날짜) → 영상 편지 → 막내의 사과
쇼츠: 완결형 2개(쇼츠 전용 압축 장면, 1분 30초~2분) + 예고형 2개(25초 안팎)"""
import json
H, FA, S1, S2, S3, LW, HU, DR, N = "hyesuk", "father", "mikyung", "misun", "mijin", "lawyer", "dongsu", "doctor", "narrator"


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


s_open = scene("유언장 낭독", "study", [H, S1, LW], mood="tense", when="현재", lines=[
    L(N, "시아버지 장례를 치르고 일주일 뒤, 변호사님이 유언장을 읽었습니다."),
    L(LW, "고 김만복 님의 유언입니다. 살던 집은 며느리 강혜숙에게 남긴다.", "normal", {S1: "shock", H: "surprised"}),
    dict(L(S1, "뭐라고요? 치매 노인 속여서 쓴 거지! 올케, 이게 무슨 짓이야!", "angry", {H: "shock"}), sfx="thud"),
    L(N, "십 년 동안 아버님 기저귀를 갈았던 저는, 그날 도둑이 됐어요."),
    L(N, "그런데 그 유언장에는, 아무도 몰랐던 날짜가 하나 적혀 있었습니다."),
    L(N, "이 이야기를 하려면, 남편을 보내던 날로 돌아가야 해요."),
])
scene("남편의 장례식", "memorial", [H, FA, S1], mood="sad", when="11년 전", flashback=True, lines=[
    L(N, "결혼 십오 년째 되던 해, 남편이 교통사고로 갑자기 떠났어요. 아이도 없이 저 혼자 남았죠."),
    L(S1, "올케, 이제 친정 가도 돼. 아버지는 우리 세 자매가 알아서 할게.", "normal", {H: "sad"}),
    L(H, "네, 형님. 그래도 아버님 혼자 계시면 식사는…", "sad"),
    L(S1, "그건 우리 집안 일이야. 올케는 이제 남이잖아.", "angry", {FA: "sad"}),
    L(FA, "혜숙아… 갈 데 없으면, 여기 있어라. 아니, 내가 부탁하마. 있어 다오.", "cry", {H: "cry"}),
    L(N, "그날 아버님 손이 너무 차가워서, 저는 그 손을 놓을 수가 없었어요."),
])
scene("둘만의 밥상", "room", [H, FA], mood="warm", when="10년 전", flashback=True, lines=[
    L(N, "남편 없는 시댁에서의 첫 겨울. 아버님과 둘이 마주 앉은 밥상은 늘 조용했어요."),
    L(FA, "혜숙아, 된장국 좀 먹어 봐라. 내가 끓였다. 동수 놈이 좋아하던 거다.", "sad", {H: "sad"}),
    L(H, "아버님… 짜요. 그래도 맛있어요.", "cry", {FA: "happy"}),
    L(FA, "짜냐? 하하, 동수도 맨날 짜다고 했지. 그래도 다 먹었어.", "happy", {H: "happy"}),
    L(H, "아버님, 내일부터는 제가 끓일게요. 대신 맛은 봐 주세요.", "happy"),
    L(N, "그날 이후로, 아버님은 매일 저녁 국 맛을 봐 주셨어요. 늘 '짜다'고 하시면서요."),
])
scene("치매 진단", "hospital", [H, FA, DR], mood="tense", when="7년 전", flashback=True, lines=[
    L(N, "그렇게 함께 산 지 사 년째, 아버님이 길을 잃기 시작하셨어요."),
    L(DR, "알츠하이머 초기입니다. 점점 가족도 못 알아보실 수 있어요.", "normal", {H: "sad", FA: "think"}),
    L(FA, "괜찮다, 혜숙아. 나는 네 얼굴은 안 잊을 거다.", "happy", {H: "cry"}),
    L(N, "시누이들에게 전화했어요. 돌아온 대답은 짧았습니다."),
    dict(L(S1, "요양원 보내. 올케가 왜 그렇게까지 해? 우린 바빠.", "angry"), sfx="ding"),
    L(H, "형님, 아버님은 집에 계시고 싶어 하세요.", "sad"),
    L(FA, "혜숙아, 나 때문에 네 인생 다 가겠다. 미안하다.", "sad", {H: "cry"}),
    L(H, "아버님, 저 여기 있고 싶어서 있는 거예요. 걱정 마세요.", "happy"),
])
scene("요양원 서류", "cafe", [H, S1], mood="tense", when="6년 전", lines=[
    L(N, "진단 일 년 뒤, 큰형님이 저를 찻집으로 불러냈어요."),
    L(S1, "올케, 여기 요양원 입소 서류야. 사인만 해. 비용은 아버지 통장에서 내면 돼.", "think", {H: "surprised"}),
    L(H, "형님, 아버님은 집에서 지내고 싶다고 하셨어요. 아직 저를 알아보세요.", "sad"),
    L(S1, "올케가 무슨 자격으로 그런 말을 해? 아버지 재산은 우리 거야.", "angry", {H: "shock"}),
    L(H, "재산 얘기가 아니에요. 아버님이 원하시는 걸 말씀드리는 거예요.", "sad", {S1: "angry"}),
    dict(L(S1, "좋아. 그럼 올케가 끝까지 해 봐. 우리한테 손 벌리지 말고.", "angry"), sfx="thud"),
    L(N, "그날 이후로 시누이들의 전화는 더 뜸해졌어요."),
])
scene("혼자 지낸 명절", "kitchen", [H], mood="calm", when="5년 전 · 추석", lines=[
    L(N, "명절이면 저는 전을 부치고 송편을 빚었어요. 아무도 오지 않을 걸 알면서도요."),
    L(H, "아버님, 올해는 형님들 오실지도 몰라요. 동그랑땡 많이 부쳐 놨어요.", "happy"),
    L(S2, "올케, 나 미선이. 이번 추석엔 못 가. 근데 아버지 통장은 누가 갖고 있어?", "think", {H: "sad"}),
    L(H, "형님… 아버님 안부부터 물어보시면 안 될까요?", "sad"),
    L(S2, "안부야 올케가 잘 알 테니까. 통장이나 잘 챙겨 둬.", "angry"),
    L(FA, "혜숙아, 오늘 손님 오냐? 전을 왜 이렇게 많이 부쳤어.", "think", {H: "sad"}),
    L(H, "아니요, 아버님. 우리 둘이 실컷 먹으려고요.", "happy", {FA: "happy"}),
    L(N, "그날 밤, 식은 동그랑땡을 아버님과 둘이서 먹었어요."),
])
s_night = scene("우리 딸", "room_night", [H, FA], mood="sad", when="3년 전", lines=[
    L(N, "병이 깊어지면서, 아버님은 밤마다 저를 찾으셨어요."),
    L(FA, "우리 딸… 우리 딸 어디 갔냐.", "sad", {H: "surprised"}),
    L(H, "아버님, 저 혜숙이에요. 며느리요.", "sad"),
    L(FA, "아니다. 너는 우리 딸이다. 내 손 잡아 다오.", "happy", {H: "cry"}),
    L(N, "딸들 이름은 다 잊으셨는데, 이상하게 저는 '우리 딸'이라고 부르셨어요."),
    L(N, "그 말 한마디에, 기저귀를 가는 밤도 하나도 힘들지 않았습니다."),
])
scene("인감 찾는 시누이들", "living", [H, S1, S2, FA], mood="tense", when="2년 전", lines=[
    L(N, "몇 년 만에 시누이들이 찾아왔어요. 아버님 생신도 아닌 날이었죠."),
    L(S1, "올케, 아버지 인감도장 어디 있어? 서류 좀 정리해야 해서.", "think", {H: "surprised"}),
    L(FA, "누구요? 아주머니들은 누군데 남의 집에 왔소?", "think", {S1: "shock", S2: "surprised"}),
    L(S2, "아빠, 나야, 미선이! 딸도 못 알아봐?", "angry", {FA: "think"}),
    L(FA, "혜숙아, 이 사람들 무서워. 내 옆에 있어라.", "sad", {H: "sad"}),
    dict(L(S1, "올케가 아버지 세뇌시켰지? 우리 얼굴도 못 알아보게!", "angry", {H: "shock"}), sfx="thud"),
    L(H, "형님, 아버님은 형님들 사진을 매일 머리맡에 두세요. 제가 닦아 드려요.", "sad", {S1: "angry"}),
    L(N, "시누이들은 그날 인감도장을 찾지 못하고 돌아갔어요."),
])
scene("마지막 맑은 밤", "room", [H, FA], mood="calm", when="한 달 전", lines=[
    L(N, "돌아가시기 사흘 전, 아버님이 아주 잠깐 정신이 맑아지셨어요."),
    L(FA, "혜숙아… 고생 많았다. 내가 다 알고 있었다.", "sad", {H: "surprised"}),
    L(H, "아버님, 저 알아보시겠어요? 저 혜숙이요.", "cry"),
    L(FA, "딸들한테는… 내가 미안하다고 전해라. 나도 좋은 아비는 아니었다.", "sad", {H: "cry"}),
    L(FA, "알지. 내 딸 혜숙이. 서랍 맨 밑에 변호사 명함 있다. 그거면 된다.", "happy", {H: "cry"}),
    L(N, "그 말을 마지막으로, 아버님은 다시 저를 '우리 딸'이라고만 부르셨어요."),
])
scene("장례식", "memorial", [H, S1, S2, S3], mood="tense", when="일주일 전", lines=[
    L(N, "장례식 날, 시누이 셋이 뒤늦게 도착했어요."),
    L(S2, "언니, 집은 팔아서 셋이 나누면 되지? 요즘 시세 꽤 나가.", "think", {S1: "think", H: "sad"}),
    L(S1, "올케는 그동안 여기서 공짜로 살았으니 할 말 없을 거고.", "angry", {H: "sad"}),
    L(S3, "언니들, 아빠 영정 앞에서 그런 얘기 좀 하지 마.", "sad", {S1: "angry"}),
    L(H, "형님들, 아버님 마지막 가시는 길이에요. 오늘만큼은 아버님 얘기만 해요.", "sad", {S2: "angry"}),
    L(S2, "올케가 뭔데 우리 집 일에 끼어들어? 남이잖아.", "angry", {H: "sad"}),
    L(N, "막내 미진 아가씨만, 영정 앞에서 한참을 울었어요."),
])
s_date = scene("8년 전의 날짜", "office", [S1, LW, H], mood="tense", lines=[
    L(N, "다시 그날, 변호사님 사무실입니다. 큰형님은 이미 다른 변호사 명함까지 들고 와 있었어요."),
    L(S1, "치매 노인이 쓴 유언장이 효력이 있어요? 소송할 거예요!", "angry", {LW: "normal"}),
    L(LW, "날짜를 보시죠. 이 유언장은 8년 전, 치매 진단을 받기 일 년 전에 쓰신 겁니다.", "normal", {S1: "shock"}),
    dict(L(LW, "정신이 온전하다는 의사 소견서도 함께 첨부돼 있습니다.", "normal", {S1: "shock", H: "surprised"}), sfx="ding"),
    L(S1, "8년 전이요? 그때 아버지는 멀쩡하셨는데…", "shock"),
    L(LW, "그리고 영상 편지가 하나 있습니다. 가족이 다 모이면 틀어 달라고 하셨어요.", "normal", {H: "cry"}),
])
s_video = scene("영상 편지", "living", [FA, S1, H], mood="sad", when="8년 전 녹화", flashback=True, lines=[
    L(FA, "얘들아, 이 영상을 볼 때쯤 나는 아마 너희를 못 알아보고 떠났을 거다.", "sad", {S1: "shock"}),
    L(FA, "내가 정신을 잃으면, 너희는 안 올 거다. 그리고 혜숙이는 남을 거다. 나는 안다.", "sad", {H: "cry"}),
    L(FA, "너희 엄마가 아플 때도 그랬다. 병원에 있던 건 혜숙이 하나였다.", "angry", {S1: "cry"}),
    L(FA, "그래서 집은 혜숙이에게 준다. 원망하지 마라. 이건 내가 맑을 때 정한 거다.", "normal"),
    dict(L(FA, "혜숙아, 너는 내 며느리가 아니다. 내 딸이다. 고맙다, 우리 딸.", "cry", {H: "cry"}), sfx="ding"),
    L(N, "영상이 끝나고, 사무실에는 한참 동안 아무 소리도 없었어요."),
    L(S1, "…아버지가 우리를 이렇게까지 알고 계셨네.", "cry", {H: "sad"}),
    L(N, "큰형님은 그 말만 남기고, 아무 말 없이 사무실을 나갔습니다."),
])
s_sorry = scene("막내의 사과", "street", [H, S3], mood="hope", lines=[
    L(N, "언니들이 먼저 나가고, 막내 미진 아가씨만 남았어요."),
    L(S3, "언니, 미안해요. 무서워서 못 왔어요. 아빠가 나를 못 알아볼까 봐.", "cry", {H: "sad"}),
    L(H, "아가씨, 아버님은 잊으신 게 아니에요. 딸들 사진은 끝까지 머리맡에 두셨어요.", "sad", {S3: "cry"}),
    L(S3, "언니가 그 사진 매일 닦아 줬던 거죠? 이제 알겠어요.", "cry"),
    L(S3, "언니, 집 받는 거 미안해하지 마요. 언니가 아빠 딸이었어요.", "sad", {H: "cry"}),
    L(H, "다음 기일엔 같이 가요. 아버님 좋아하시던 동그랑땡 부쳐서요.", "happy", {S3: "happy"}),
    L(S3, "네, 언니. 이번엔 제가 부칠게요. 짜게요.", "happy", {H: "happy"}),
])
scene("아버님 이름으로", "park", [H, S3], mood="warm", when="6개월 뒤", lines=[
    L(N, "저는 집을 판 돈의 절반을, 아버님이 다니시던 요양 센터에 기부했어요."),
    L(S3, "언니, 현판 봤어요? '김만복 할아버지 쉼터'래요.", "happy", {H: "happy"}),
    L(H, "아버님이 보시면 쑥스러워하시겠다. 그래도 좋아하실 거예요.", "happy"),
    L(S3, "언니, 남은 돈으로는 뭐 할 거예요? 언니도 이제 언니 인생 살아요.", "think", {H: "happy"}),
    L(H, "아버님 된장국 맛 내는 국밥집 하나 할까 봐요. 짜지 않게요.", "happy", {S3: "happy"}),
    L(N, "큰형님은 아직 연락이 없어요. 그래도 언젠가 이 쉼터에 한번 오시면 좋겠습니다."),
    L(N, "아버님도 분명 그걸 바라실 테니까요."),
])
scene("여러분께", "room", [H], mood="warm", lines=[
    L(N, "피는 한 방울도 안 섞였지만, 저는 십 년 동안 그분의 딸이었어요."),
    L(N, "여러분이라면 시누이들을 용서하실 수 있을까요? 혜숙이라면 집을 받으셨을까요?"),
    L(H, "여러분 곁의 어르신께, 오늘 손 한번 잡아 드리세요. 생각보다 많이 기다리세요.", "happy"),
    L(N, "여러분의 생각을 댓글로 들려주세요. 이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

# ── 쇼츠 전용 압축 장면 (완결형) ──
full1 = [
    scene("유언장 낭독", "study", [H, S1, LW], mood="tense", shorts_only=True, lines=[
        dict(L(S1, "치매 노인 속여서 쓴 유언장이지? 올케, 이게 무슨 짓이야!", "angry", {H: "shock"}), sfx="thud"),
        L(N, "시아버지 유언장에는 '집은 며느리 강혜숙에게'라고 적혀 있었어요."),
        L(N, "남편을 일찍 보내고도 시댁에 남아, 치매 시아버지를 십 년 동안 혼자 모신 며느리였습니다."),
        L(H, "형님, 저는 아버님이 원하셔서 곁에 있었던 거예요.", "sad", {S1: "angry"}),
        L(S1, "말은 잘하네. 그 집이 탐나서 버틴 거잖아!", "angry"),
        L(N, "저는 아무 말도 못 했어요. 십 년이 한순간에 도둑질이 돼 버렸으니까요."),
    ]),
    scene("십 년", "room_night", [H, FA], mood="sad", shorts_only=True, when="10년 동안", lines=[
        L(N, "시누이 셋은 명절에도 오지 않았어요. 전화는 늘 통장 얘기뿐이었죠."),
        L(S1, "요양원 보내. 올케가 왜 그렇게까지 해? 우린 바빠.", "angry", {H: "sad"}),
        L(FA, "우리 딸… 내 손 잡아 다오.", "sad", {H: "cry"}),
        L(N, "딸들 이름은 다 잊은 아버님이, 밤마다 며느리를 '우리 딸'이라 불렀습니다."),
        L(N, "그리고 장례 일주일 뒤, 유언장을 읽는 날이 왔어요."),
    ]),
    scene("8년 전의 날짜", "office", [S1, LW, H], mood="tense", shorts_only=True, lines=[
        L(S1, "소송할 거예요! 치매 노인이 쓴 게 무슨 효력이 있어요!", "angry", {LW: "normal"}),
        dict(L(LW, "이 유언장은 8년 전, 치매 진단 일 년 전에 쓰신 겁니다. 의사 소견서도 있어요.", "normal", {S1: "shock"}), sfx="ding"),
        L(S1, "8년 전이요…?", "shock", {H: "surprised"}),
        L(LW, "가족이 다 모이면 틀어 달라고 하신 영상 편지도 있습니다.", "normal", {H: "cry"}),
    ]),
    scene("영상 편지", "living", [FA, S1, H, S3], mood="sad", shorts_only=True, when="8년 전 녹화", lines=[
        L(FA, "내가 정신을 잃으면 너희는 안 올 거다. 그리고 혜숙이는 남을 거다. 나는 안다.", "sad", {S1: "cry"}),
        L(FA, "너희 엄마가 아플 때도 병원에 있던 건 혜숙이 하나였다.", "angry", {S1: "cry"}),
        L(FA, "그래서 집은 혜숙이에게 준다. 이건 내가 맑을 때 정한 거다.", "normal"),
        dict(L(FA, "혜숙아, 너는 내 며느리가 아니다. 내 딸이다.", "cry", {H: "cry"}), sfx="ding"),
        L(N, "큰형님은 아무 말 없이 사무실을 나갔고, 막내만 남아 며느리 손을 잡았어요."),
        L(S3, "언니, 미안해요. 언니가 아빠 딸이었어요.", "cry", {H: "cry"}),
        L(H, "아가씨, 다음 기일엔 같이 가요. 아버님 좋아하시던 동그랑땡 부쳐서요.", "happy", {S3: "cry"}),
        L(N, "피 한 방울 안 섞인 며느리를 끝까지 딸로 기억한 시아버지. 여러분이라면 이 시누이들을 용서하실 수 있을까요?"),
    ]),
]
full2 = [
    scene("우리 딸", "room_night", [H, FA], mood="sad", shorts_only=True, when="3년 전", lines=[
        dict(L(FA, "우리 딸… 우리 딸 어디 갔냐.", "sad", {H: "surprised"}), sfx="ding"),
        L(H, "아버님, 저 혜숙이에요. 며느리요.", "sad"),
        L(FA, "아니다. 너는 우리 딸이다. 내 손 잡아 다오.", "happy", {H: "cry"}),
        L(N, "치매 시아버지를 십 년째 혼자 모신 며느리. 아버님은 친딸들 얼굴은 잊고, 며느리만 '우리 딸'이라 부르셨어요."),
        L(N, "시누이 셋은 명절에도 오지 않았어요. 전화는 늘 통장 얘기뿐이었죠."),
    ]),
    scene("인감 찾는 시누이들", "living", [H, S1, FA], mood="tense", shorts_only=True, when="2년 전", lines=[
        L(S1, "올케, 아버지 인감도장 어디 있어?", "think", {H: "surprised"}),
        L(FA, "아주머니는 누군데 남의 집에 왔소? 혜숙아, 무섭다.", "sad", {S1: "shock"}),
        dict(L(S1, "올케가 아버지 세뇌시켰지? 우리 얼굴도 못 알아보게!", "angry", {H: "shock"}), sfx="thud"),
        L(H, "형님, 아버님은 형님들 사진을 매일 머리맡에 두세요.", "sad", {S1: "angry"}),
        L(N, "그리고 이 년 뒤, 아버님이 세상을 떠나셨어요."),
    ]),
    scene("유언장", "study", [H, S1, LW], mood="tense", shorts_only=True, when="장례 일주일 뒤", lines=[
        L(N, "아버님이 떠나시고 일주일 뒤, 변호사님이 유언장을 읽었어요."),
        L(LW, "살던 집은 며느리 강혜숙에게 남긴다.", "normal", {S1: "shock", H: "surprised"}),
        dict(L(S1, "치매 노인 속여서 쓴 거지! 올케, 이게 무슨 짓이야!", "angry", {H: "shock"}), sfx="thud"),
        L(LW, "이 유언장은 8년 전, 치매 진단 전에 쓰신 겁니다. 영상 편지도 남기셨어요.", "normal", {S1: "shock"}),
        L(S1, "치매 노인 속여서 쓴 거지! 소송할 거야!", "angry", {H: "shock"}),
        dict(L(LW, "정신이 온전하다는 의사 소견서도 있습니다. 그리고 영상 편지를 남기셨어요.", "normal", {S1: "shock"}), sfx="ding"),
        L(S1, "8년 전…? 그때 아버지는 멀쩡하셨는데.", "shock", {H: "cry"}),
    ]),
    scene("영상 편지", "living", [FA, H, S3], mood="sad", shorts_only=True, when="8년 전 녹화", lines=[
        L(FA, "내가 정신을 잃으면 너희는 안 올 거다. 그리고 혜숙이는 남을 거다. 나는 안다.", "sad", {H: "cry"}),
        L(FA, "너희 엄마가 아플 때도 병원에 있던 건 혜숙이 하나였다.", "sad", {H: "cry"}),
        L(FA, "혜숙아, 너는 내 며느리가 아니다. 내 딸이다. 고맙다, 우리 딸.", "cry", {H: "cry"}),
        L(S3, "언니… 아빠가 언니를 딸이라고 부른 거, 이제야 알겠어요. 미안해요.", "cry", {H: "cry"}),
        L(N, "피 한 방울 안 섞인 며느리를, 아버님은 끝까지 딸로 기억하셨습니다. 여러분은 이 며느리에게 뭐라고 해 주고 싶으세요?"),
    ]),
]

TITLE = "치매 시아버지 10년 모신 며느리, 유언장 날 도둑으로 몰렸다가 시누이들이 얼어붙었다"
DESC_SHORT = "남편을 먼저 보내고도 치매 시아버지를 10년 동안 혼자 모신 며느리. 유언장을 읽는 날 시누이들은 며느리를 도둑으로 몰았지만, 유언장에 적힌 날짜와 영상 편지가 모든 걸 바꿨습니다.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #사이다사연 #감동사연 #며느리 #시아버지 #유언장 #인생이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "will-daughter",
    "voice": "ko-KR-SunHiNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Autonoe",
    "cast": {
        H: {"name": "며느리 혜숙", "gvoice": "ko-KR-Chirp3-HD-Autonoe", "color": "#8e5aa8", "hair": "bun", "hair_color": "#3b2a20", "skin": "#f6d2b2"},
        FA: {"name": "시아버지", "gvoice": "ko-KR-Chirp3-HD-Iapetus", "color": "#7b6b5d", "hair": "short", "hair_color": "#e0dbd5", "skin": "#eec29e"},
        S1: {"name": "큰시누 미경", "gvoice": "ko-KR-Chirp3-HD-Achernar", "color": "#c62828", "hair": "short", "hair_color": "#2b1d18", "accessory": "glasses"},
        S2: {"name": "둘째 시누 미선", "gvoice": "ko-KR-Chirp3-HD-Zephyr", "color": "#ef6c00", "hair": "long", "hair_color": "#5a3a24"},
        S3: {"name": "막내 시누 미진", "gvoice": "ko-KR-Chirp3-HD-Kore", "color": "#4db6ac", "hair": "long", "hair_color": "#2e2420", "accessory": "bow"},
        LW: {"name": "변호사", "gvoice": "ko-KR-Chirp3-HD-Schedar", "color": "#455a64", "hair": "short", "hair_color": "#222222", "accessory": "glasses"},
        HU: {"name": "남편 동수", "gvoice": "ko-KR-Chirp3-HD-Orus", "color": "#5c6bc0", "hair": "short", "hair_color": "#222222"},
        DR: {"name": "의사", "gvoice": "ko-KR-Chirp3-HD-Sadaltager", "color": "#eceff1", "hair": "short", "hair_color": "#333333", "accessory": "glasses"},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 (영상 편지 내용은 숨김)
    "teaser": [[s_open, 2, 3], [s_date, 2, 4], [s_night, 3, 4]],
    "shorts_speed": 1.25,
    "shorts": [
        {"format": "full", "speed": 1.1, "clips": [[i] for i in full1], "hook": "유언장 낭독 날\n도둑 된 며느리",
         "hook_who": H, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "will", "text": "8년 전"},
         "cta_line": "며느리의 십 년, 더 긴 이야기는 아래 본편에서 들려 드릴게요.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "치매 시아버지 10년 모신 며느리, 유언장 낭독 날 시누이들이 얼어붙었다 #시니어사연 #사이다사연 #감동사연 #며느리 #유언장 #인생이야기",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.1, "clips": [[i] for i in full2], "hook": "친딸은 잊고\n며느리만 기억한 아버지",
         "hook_who": FA, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "will", "text": "우리 딸"},
         "cta_line": "시아버지와 며느리의 이야기 전체는 아래 본편에서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "친딸은 잊고 며느리만 '우리 딸'이라 부른 치매 시아버지 #시니어사연 #감동사연 #며느리 #시아버지 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"clips": [[s_open, 2, 4], [s_date, 1, 4]], "hook": "유언장 읽는 날\n도둑 된 며느리",
         "hook_who": H, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "will", "text": "8년 전"},
         "end_text": "날짜의 비밀은 본편에서 ▶",
         "title": "유언장 읽는 날 도둑 된 며느리 #시니어사연 #사이다사연 #며느리"},
        {"clips": [[s_date, 4, 6], [s_video, 0, 3]], "hook": "시아버지가 남긴\n영상 편지",
         "hook_who": FA, "hook_emotion": "sad", "hook_tone": "gold", "hook_prop": {"type": "will", "text": "8년 전"},
         "end_text": "편지의 마지막 말은 본편에서 ▶",
         "title": "시아버지가 남긴 영상 편지 #시니어사연 #감동사연 #며느리"},
    ],
    "thumbnail": {
        "text": "유언장 날\n도둑 된 며느리",
        "highlight": "도둑 된 며느리",
        "badge": "10년 간병",
        "variants": [
            {"style": "story", "tone": "red", "face": [S1, "angry"], "prop": {"type": "will", "text": "8년 전"}},
            {"style": "story", "tone": "blue", "face": [FA, "cry"], "text": "친딸은 잊고\n며느리만 기억", "highlight": "며느리만 기억",
             "badge": "눈물 주의", "prop": {"type": "will", "text": "우리 딸"}},
            {"style": "story", "tone": "gold", "face": [H, "cry"], "text": "유언장 날짜의\n반전", "highlight": "반전",
             "badge": "끝까지 보세요", "prop": {"type": "will", "text": "8년 전"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“치매 노인 속여서 쓴 거지!”… 10년 간병한 며느리를 도둑으로 몬 시누이들, 유언장 날짜를 보고 얼어붙었다",
                           "친딸은 잊고 며느리만 '우리 딸'이라 부른 치매 시아버지, 8년 전 남긴 영상 편지"],
        "description": "“치매 노인 속여서 쓴 거지!” 남편을 먼저 보내고도 시댁에 남아 치매 시아버지를 10년 동안 혼자 모신 며느리 혜숙. 장례 일주일 뒤 유언장에 '집은 며느리에게'라고 적혀 있자 시누이들은 며느리를 도둑으로 몰아세웁니다. 그런데 유언장에는 아무도 몰랐던 날짜가 적혀 있었습니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 시누이들을 용서하실 수 있을까요? 혜숙이라면 집을 받으셨을까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #사이다사연",
        "tags": ["사연", "시니어사연", "사이다 사연", "감동 사연", "며느리", "시아버지", "시누이", "유언장", "치매", "간병", "인생이야기", "사연 만화", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-22T18:00:00+09:00",
        "pinned_comment": "여러분이라면 시누이들을 용서하실 수 있을까요? 혜숙이라면 집을 받으셨을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-22T18:10:00+09:00", "2026-10-23T12:00:00+09:00", "2026-10-23T19:00:00+09:00", "2026-10-24T12:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
for k, f in (("full1", full1), ("full2", full2)):
    print(k, sum(len(l["text"]) for i in f for l in S[i]["lines"]), "chars")
