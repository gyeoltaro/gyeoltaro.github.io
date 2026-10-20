"""대본 원본: 이 파일을 실행하면 project.json 이 만들어집니다 (창작 사연)
구성: 장인(화자) 시점. 선 자리를 박차고 나간 사위(앞당김) → 딸과 사위의 결혼·병상·장례 → 12년의 처가살이
→ 마을의 수군거림과 재혼 권유 → 몰래 만든 선 자리 → 사위 수첩 첫 장에 적힌 딸의 부탁 → 마주 앉은 밤
쇼츠: 완결형 2개(쇼츠 전용 압축 장면, 1분 30초~2분) + 예고형 2개(25초 안팎)"""
import json
F, S_, M, MK, N_, E, N = "father", "jeonghun", "miyeon", "miyeon_kid", "neighbor", "eunhee", "narrator"


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


s_open = scene("선 자리", "cafe", [F, S_, E], mood="tense", when="현재", lines=[
    L(N, "일흔넷 된 이 늙은이가, 사위 몰래 선 자리를 만들었습니다."),
    dict(L(S_, "아버님, 이게 뭐예요? 저 선 같은 거 안 봐요.", "shock", {F: "surprised", E: "surprised"}), sfx="thud"),
    L(F, "앉아 봐라. 은희 씨 좋은 사람이다. 너도 이제 네 인생 살아야지.", "sad"),
    L(S_, "죄송합니다, 은희 씨. 아버님, 저 먼저 들어가 볼게요.", "angry", {E: "sad"}),
    L(N, "십이 년 동안 한 번도 언성을 높인 적 없던 사위였어요."),
    L(N, "그날 밤, 저는 사위가 두고 간 낡은 수첩을 열었습니다. 그리고 첫 장에서 손이 멈췄어요."),
    L(N, "제 사위 정훈이 이야기를, 처음부터 해 볼까 합니다."),
])
scene("딸의 약속", "room", [F, MK], mood="warm", when="35년 전", flashback=True, lines=[
    L(N, "미연이 엄마는 미연이가 일곱 살 때 세상을 떠났어요. 그 뒤로는 저랑 딸, 둘뿐이었죠."),
    L(MK, "아빠, 또 라면이야? 아빠는 맨날 밥을 안 먹어.", "angry", {F: "sad"}),
    L(F, "아빠는 배가 안 고파서 그래. 미연이나 많이 먹어.", "sad"),
    L(MK, "거짓말. 아빠 외로우면 밥 안 먹는 거 다 알아.", "sad", {F: "surprised"}),
    L(MK, "내가 커서 아빠 밥 맨날 해 줄게. 약속!", "happy", {F: "cry"}),
    L(N, "그 꼬마가 자라서, 서른 살에 남자 하나를 데려왔습니다."),
])
scene("상견례", "living", [F, S_, M], mood="warm", when="16년 전", flashback=True, lines=[
    L(N, "외동딸 미연이가 처음 데려온 남자가 정훈이었어요. 저는 영 마음에 들지 않았죠."),
    L(F, "자네, 월급은 얼마나 받나? 우리 미연이 고생시킬 거면 지금 일어나게.", "angry", {S_: "surprised"}),
    L(M, "아빠! 왜 그래, 진짜.", "angry", {F: "think"}),
    L(S_, "아버님, 돈은 많이 못 드려도 따님 평생 웃게 해 드리겠습니다.", "happy", {F: "think"}),
    L(F, "말은 누가 못 하나. 두고 보겠네.", "think"),
    L(M, "아빠, 정훈 씨가 아빠 혼자 사는 거 걱정돼서 결혼하면 자주 오재.", "happy", {F: "surprised"}),
    L(N, "그 '두고 보겠네'가, 이렇게 긴 세월이 될 줄은 몰랐습니다."),
])
s_ward = scene("병실", "hospital", [M, S_], mood="sad", when="12년 전", flashback=True, lying=[M], lines=[
    L(N, "결혼 사 년 만에, 미연이가 아팠어요. 손쓸 수 없는 병이라고 했습니다."),
    L(M, "정훈 씨, 아빠는 지금 복도에 있지? 잠깐 둘이서만 얘기해.", "sad", {S_: "cry"}),
    L(S_, "응, 아버님 커피 사러 가셨어. 무슨 얘긴데.", "cry"),
    L(M, "부탁이 하나 있어. 꼭 들어줘야 해.", "sad"),
    L(S_, "무슨 부탁이든 다 들어줄게. 그러니까 그런 말 하지 마.", "cry", {M: "sad"}),
    L(N, "그날 병실 문 너머로 둘이 나눈 이야기를, 저는 십이 년 동안 몰랐습니다."),
])
scene("장례식 다음 날", "memorial", [F, S_], mood="sad", when="12년 전", lines=[
    L(N, "미연이를 보내고 난 다음 날, 저는 사위를 불러 앉혔어요."),
    L(F, "정훈아, 이제 우리 집에 올 필요 없다. 자네는 아직 젊어.", "sad", {S_: "sad"}),
    L(F, "장인 노릇 그만하겠네. 자네 인생 살게.", "sad"),
    L(S_, "아버님, 이번 주 토요일에 올게요. 보일러 고치기로 했잖아요.", "happy", {F: "surprised"}),
    L(F, "내 말 못 들었나? 오지 말라니까.", "angry"),
    L(S_, "미연이가 그랬어요. 아버님 보일러는 겨울 오기 전에 꼭 봐 드리라고요.", "sad", {F: "sad"}),
    L(N, "그런데 그 토요일, 사위는 공구함을 들고 대문을 두드렸습니다."),
])
s_yard = scene("주말마다 오는 사위", "yard", [F, S_], mood="warm", when="10년 전", lines=[
    L(N, "그렇게 이 년 동안, 사위는 주말마다 세 시간을 운전해 시골집에 왔어요."),
    L(S_, "아버님, 오늘 김장은 제가 할게요. 앉아 계세요.", "happy", {F: "think"}),
    L(F, "됐다. 매주 이게 무슨 고생이냐.", "angry"),
    L(S_, "그래서 말인데요, 저 회사를 읍내 지점으로 옮겼어요. 여기서 같이 살게요.", "happy", {F: "shock"}),
    dict(L(F, "뭐? 이 사람이 정신이 있나! 서울 집은?", "shock", {S_: "happy"}), sfx="ding"),
    L(S_, "팔았어요. 아버님 혼자 밥 거르시는 거, 이제 못 보겠어요.", "sad"),
    L(F, "자네가 왜 그렇게까지 하나. 자네는 남이야, 이제.", "angry", {S_: "sad"}),
    L(S_, "남 아니에요. 아버님은 제 아버지예요.", "sad", {F: "cry"}),
    L(N, "저는 그날 처음으로, 사위 앞에서 고개를 돌리고 울었습니다."),
])
scene("마을의 수군거림", "street", [F, N_], mood="tense", when="5년 전", lines=[
    L(N, "사위와 산 지 칠 년쯤 됐을 때였어요. 동네에 말이 돌기 시작했습니다."),
    L(N_, "효자 사위 났다고들 하지. 근데 오 영감, 그거 젊은 사람 발목 잡는 거 아녀?", "think", {F: "sad"}),
    L(F, "내가 잡은 게 아니라, 저 녀석이 안 간다는 거요.", "angry"),
    L(N_, "그러니까 더 놓아줘야지. 영감 가고 나면 그 사람은 혼자여.", "sad", {F: "think"}),
    L(N_, "읍내 사람들은 영감이 사위 붙잡고 산다고 수군거려. 듣기 좋은 소리는 아니지.", "think", {F: "angry"}),
    L(N, "그 말이, 가시처럼 가슴에 박혔어요."),
])
scene("재혼 권유", "kitchen", [F, S_], mood="calm", when="5년 전", lines=[
    L(F, "정훈아, 너 이제 마흔이다. 좋은 사람 만나서 다시 시작해라.", "sad", {S_: "happy"}),
    L(S_, "아버님 김치찌개보다 맛있게 끓이는 사람 있으면 생각해 볼게요.", "happy"),
    L(F, "농담하지 말고. 내가 미연이 볼 낯이 없어.", "angry", {S_: "sad"}),
    L(S_, "미연이는… 아버님 웃으시면 좋아할 거예요. 그거면 돼요.", "sad"),
    L(F, "넌 왜 미연이 얘기만 나오면 말을 돌리냐.", "think", {S_: "sad"}),
    L(S_, "찌개 식어요, 아버님. 얼른 드세요.", "happy"),
    L(N, "사위는 늘 그렇게 웃으며 넘겼어요. 저는 그게 더 미안했습니다."),
])
scene("업고 뛴 밤", "night", [F, S_], mood="tense", when="1년 전", weather="rain", lines=[
    L(N, "작년 겨울, 저는 새벽에 화장실에 가다 쓰러졌어요."),
    dict(L(S_, "아버님! 아버님, 정신 차리세요!", "shock", {F: "sad"}), sfx="thud"),
    L(N, "구급차가 오려면 사십 분이라고 했어요. 사위는 저를 업고 빗길을 뛰었습니다."),
    L(F, "정훈아… 내려놔라. 너 무릎 다 나간다.", "cry", {S_: "cry"}),
    L(S_, "안 돼요. 아버님까지 보내면, 저 진짜 혼자예요.", "cry"),
    L(N, "응급실 의사가 그러더군요. 조금만 늦었어도 큰일 날 뻔했다고."),
    L(N, "그 말을 듣고, 저는 결심했어요. 이 아이를 이제는 놓아줘야겠다고."),
])
scene("늙은이의 결심", "park", [F, N_], mood="calm", when="한 달 전", lines=[
    L(F, "순자 씨, 지난번에 말한 은희 씨 말이오. 한번 자리 좀 만들어 주시오.", "think", {N_: "surprised"}),
    L(N_, "정훈이가 알아요? 그 사람 성격에 싫다 할 텐데.", "think"),
    L(F, "모르게 해야지. 그냥 차 한잔하자고 불러낼 거요.", "sad"),
    L(F, "내가 먼저 가면, 그 아이 옆에 누가 있겠소.", "cry", {N_: "sad"}),
    L(N_, "그 마음은 알겠소. 근데 영감, 그 사람이 왜 안 떠나는지는 물어봤소?", "think", {F: "think"}),
    L(F, "물어봐도 웃기만 하오. 그러니 내가 나서야지.", "sad"),
    L(N_, "알았소. 은희 씨한테는 내가 잘 말해 두리다. 착한 사람이오.", "happy", {F: "sad"}),
    L(N, "그렇게 저는 평생 처음으로, 사위를 속였습니다."),
])
scene("박차고 나간 사위", "cafe", [F, S_, E], mood="tense", lines=[
    L(N, "그리고 그날, 찻집에서 사위는 처음으로 저에게 화를 냈어요."),
    L(E, "괜찮아요, 정훈 씨. 저도 사실 억지로 나온 거예요.", "happy", {S_: "sad"}),
    L(S_, "은희 씨 탓이 아니에요. 아버님, 저 약속한 게 있어요.", "sad", {F: "surprised"}),
    L(F, "약속? 무슨 약속을 누구랑 했단 말이냐.", "surprised"),
    L(S_, "…먼저 들어가 볼게요. 죄송합니다.", "sad", {F: "think"}),
    L(N, "사위가 앉았던 의자 위에는, 늘 품에 넣고 다니던 낡은 수첩이 떨어져 있었어요."),
])
s_note = scene("수첩 첫 장", "room_night", [F], mood="sad", when="그날 밤", lines=[
    L(N, "남의 수첩을 보는 건 도리가 아닌 줄 알면서도, 저는 그날 밤 수첩을 열었습니다."),
    L(S_, "아버님 혈압약 바뀜. 아침 한 알, 저녁 반 알. 짜게 드시면 안 됨.", "normal"),
    L(S_, "미연이 기일. 아버님이 오늘 처음으로 웃으셨다. 미연아, 봤지?", "happy"),
    dict(L(F, "이건… 미연이 글씨 아니냐.", "shock"), sfx="ding"),
    L(M, "정훈 씨, 우리 아빠 혼자 두지 마. 아빠는 외로우면 밥을 안 먹어.", "sad"),
    L(F, "미연아… 네가 이걸 부탁했구나. 이 바보 같은 녀석은 그걸 십이 년을 지켰고.", "cry"),
])
s_promise = scene("그날의 약속", "hospital", [M, S_], mood="sad", when="12년 전 · 병실", flashback=True, lying=[M], lines=[
    L(M, "아빠를 부탁해. 당신밖에 없어.", "cry", {S_: "cry"}),
    L(S_, "걱정 마. 아버님은 내가 지킬게. 약속해.", "cry"),
    L(M, "그리고 하나 더. 당신도 꼭 행복해야 해. 좋은 사람 생기면 꼭 만나.", "sad", {S_: "cry"}),
    L(S_, "그건… 아버님이 웃으실 때까지는 못 해.", "cry"),
    L(M, "바보. 그럼 우리 아빠 빨리 웃게 해 줘.", "happy", {S_: "cry"}),
])
s_talk = scene("마주 앉은 밤", "kitchen", [F, S_], mood="hope", when="그날 새벽", lines=[
    L(N, "새벽녘에 들어온 사위 앞에, 저는 수첩을 내밀었어요."),
    L(S_, "아버님… 읽으셨어요?", "surprised", {F: "cry"}),
    L(F, "이 바보야. 미연이가 너 행복하라는 말도 했다며. 그건 왜 안 지키냐.", "cry", {S_: "cry"}),
    L(S_, "아버님이랑 사는 게, 지금 제 행복이에요. 진짜예요.", "cry"),
    L(F, "그럼 나도 약속 하나 하자. 내가 밥 잘 먹고 오래 살 테니, 너는 네 인생도 살아라.", "sad", {S_: "cry"}),
    dict(L(S_, "…네, 아버님. 대신 김치찌개는 계속 끓여 주셔야 해요.", "happy", {F: "happy"}), sfx="ding"),
    L(F, "그래, 이 녀석아. 짜게는 안 끓이마.", "happy", {S_: "happy"}),
    L(N, "그날 새벽, 저희 둘은 식은 찌개를 데워 마주 앉아 먹었어요. 미연이가 바라던 대로요."),
])
scene("감 따는 날", "yard", [F, S_, E], mood="warm", when="1년 뒤", lines=[
    L(N, "일 년이 지났어요. 사위는 여전히 저랑 이 시골집에 삽니다."),
    L(S_, "아버님, 올해 감은 은희 씨가 따 준대요.", "happy", {F: "happy", E: "happy"}),
    L(E, "아버님, 곶감 만드는 법은 제가 배워 갈게요.", "happy"),
    L(F, "그래, 천천히들 해라. 나는 하나도 안 급하다.", "happy"),
    L(S_, "아버님, 은희 씨 오면 김치찌개 끓여 주신다고 하셨잖아요. 싱겁게요.", "happy", {F: "happy"}),
    L(F, "이 녀석, 그 소리는 은희 씨 앞에서 하지 마라.", "happy", {E: "happy"}),
    L(N, "요즘 사위 수첩 맨 뒷장에는 새 글이 적혀 있어요. 미연아, 아버님이 요즘 자주 웃으셔."),
])
scene("여러분께", "living", [F, S_], mood="warm", lines=[
    L(N, "자식도 아닌 사위가, 딸과의 약속 하나로 십이 년을 지켜 줬습니다."),
    L(N, "여러분이라면 정훈이처럼 할 수 있었을까요? 장인이었다면 사위를 놓아주셨을까요?"),
    L(F, "여러분 곁의 고마운 사람에게, 오늘 밥 한 끼 먹었냐고 물어봐 주세요.", "happy", {S_: "happy"}),
    L(S_, "아버님, 오늘 저녁은 제가 끓일게요. 싱겁게요.", "happy", {F: "happy"}),
    L(N, "여러분의 생각을 댓글로 들려주세요. 이 이야기는 실제 사연을 바탕으로 한 것이 아닌, 창작 사연입니다."),
    L(N, "구독과 좋아요는 다음 이야기에 큰 힘이 됩니다."),
])

# ── 쇼츠 전용 압축 장면 (완결형) ──
full1 = [
    scene("선 자리", "cafe", [F, S_], mood="tense", shorts_only=True, lines=[
        dict(L(S_, "아버님, 이게 뭐예요? 저 선 안 봐요!", "shock", {F: "surprised"}), sfx="thud"),
        L(N, "아내를 먼저 보낸 뒤 십이 년째 저를 모시는 사위. 제가 몰래 선 자리를 만들었습니다."),
        L(F, "너도 이제 네 인생 살아야지. 내가 먼저 가면 넌 혼자다.", "sad", {S_: "angry"}),
        L(N, "십이 년 동안 한 번도 언성을 높인 적 없던 아이가, 그날 처음 화를 냈어요."),
        L(S_, "저 약속한 게 있어요. 먼저 들어갈게요.", "angry", {F: "think"}),
    ]),
    scene("딸의 장례식 다음 날", "memorial", [F, S_], mood="sad", shorts_only=True, when="12년 전", lines=[
        L(N, "십이 년 전, 하나뿐인 딸을 먼저 보냈어요. 저는 사위에게 이제 오지 말라고 했습니다."),
        L(F, "자네는 아직 젊어. 장인 노릇 그만하겠네.", "sad", {S_: "sad"}),
        L(S_, "아버님, 이번 주 토요일에 올게요. 보일러 고치기로 했잖아요.", "happy", {F: "surprised"}),
    ]),
    scene("십이 년", "yard", [F, S_], mood="warm", shorts_only=True, when="12년 동안", lines=[
        L(N, "딸 장례식 다음 날, 이제 오지 말라고 했는데 사위는 토요일마다 공구함을 들고 왔어요."),
        L(S_, "저 회사 읍내로 옮겼어요. 아버님 혼자 밥 거르시는 거 못 보겠어요.", "happy", {F: "cry"}),
        L(F, "자네는 남이야, 이제. 왜 이렇게까지 하나.", "angry", {S_: "sad"}),
        L(S_, "남 아니에요. 아버님은 제 아버지예요.", "sad", {F: "cry"}),
        L(N, "그렇게 사위는 서울 집을 팔고, 이 시골집에 들어와 살았습니다."),
        L(N, "재혼하라고 할 때마다 사위는 웃기만 했어요. 저는 그게 늘 미안했습니다."),
    ]),
    scene("수첩 첫 장", "room_night", [F], mood="sad", shorts_only=True, when="그날 밤", lines=[
        L(N, "그날 밤, 사위가 떨어뜨린 낡은 수첩을 열었어요. 첫 장에 딸의 글씨가 있었습니다."),
        dict(L(M, "정훈 씨, 우리 아빠 혼자 두지 마. 아빠는 외로우면 밥을 안 먹어.", "sad"), sfx="ding"),
        L(S_, "미연이 기일. 아버님이 오늘 처음으로 웃으셨다. 미연아, 봤지?", "happy"),
        L(F, "미연아… 이 녀석이 그 부탁을 십이 년이나 지켰구나.", "cry"),
    ]),
    scene("마주 앉은 새벽", "kitchen", [F, S_], mood="hope", shorts_only=True, lines=[
        L(F, "미연이가 너 행복하라는 말도 했다며. 그건 왜 안 지키냐, 이 바보야.", "cry", {S_: "cry"}),
        L(S_, "아버님이랑 사는 게 지금 제 행복이에요.", "cry"),
        L(F, "그럼 나는 밥 잘 먹고 오래 살 테니, 너는 네 인생도 살아라.", "happy", {S_: "happy"}),
        L(S_, "네, 아버님. 대신 김치찌개는 계속 끓여 주셔야 해요.", "happy", {F: "happy"}),
        L(N, "아내의 부탁 하나로 십이 년을 지킨 사위. 여러분이라면 이 사위를 놓아주셨을까요?"),
    ]),
]
full2 = [
    scene("병실의 부탁", "hospital", [M, S_], mood="sad", shorts_only=True, when="12년 전", lying=[M], lines=[
        dict(L(M, "아빠를 부탁해. 당신밖에 없어.", "cry", {S_: "cry"}), sfx="ding"),
        L(S_, "걱정 마. 아버님은 내가 지킬게.", "cry"),
        L(M, "그리고 당신도 꼭 행복해야 해. 좋은 사람 생기면 꼭 만나.", "sad", {S_: "cry"}),
        L(N, "아내가 떠나고, 사위는 이 약속을 아무에게도 말하지 않았습니다."),
    ]),
    scene("처가살이", "yard", [F, S_], mood="warm", shorts_only=True, when="10년 전", lines=[
        L(N, "장인은 이제 오지 말라고 했지만, 사위는 주말마다 세 시간을 운전해 시골집에 왔어요."),
        L(S_, "아버님, 저 회사를 읍내로 옮겼어요. 여기서 같이 살게요.", "happy", {F: "shock"}),
        L(F, "이 사람이 정신이 있나! 자네는 남이야, 이제.", "angry", {S_: "sad"}),
        L(S_, "남 아니에요. 아버님 혼자 밥 거르시는 거, 이제 못 보겠어요.", "sad", {F: "cry"}),
    ]),
    scene("업고 뛴 밤", "night", [F, S_], mood="tense", shorts_only=True, when="12년 뒤", weather="rain", lines=[
        L(N, "십이 년 동안 장인 곁을 지킨 사위. 어느 겨울밤, 장인이 쓰러졌어요."),
        dict(L(S_, "아버님! 정신 차리세요!", "shock", {F: "sad"}), sfx="thud"),
        L(F, "정훈아, 내려놔라… 너 무릎 다 나간다.", "cry", {S_: "cry"}),
        L(S_, "안 돼요. 아버님까지 보내면 저 진짜 혼자예요.", "cry"),
        L(N, "구급차를 기다릴 수 없어서, 사위는 장인을 업고 빗길을 뛰었습니다."),
    ]),
    scene("몰래 만든 선 자리", "cafe", [F, S_], mood="tense", shorts_only=True, lines=[
        L(N, "그날 장인은 결심했어요. 이 아이를 이제는 놓아줘야겠다고. 그리고 몰래 선 자리를 만들었습니다."),
        L(S_, "아버님, 저 약속한 게 있어요. 죄송합니다.", "angry", {F: "surprised"}),
        L(F, "약속? 무슨 약속을 누구랑 했단 말이냐.", "surprised", {S_: "sad"}),
        L(N, "그날 밤 장인은 사위가 떨어뜨린 수첩 첫 장에서, 먼저 떠난 딸의 글씨를 발견했습니다."),
        dict(L(M, "정훈 씨, 우리 아빠 혼자 두지 마. 아빠는 외로우면 밥을 안 먹어.", "sad"), sfx="ding"),
    ]),
    scene("새벽의 약속", "kitchen", [F, S_], mood="hope", shorts_only=True, lines=[
        L(F, "이 바보야. 행복하라는 약속은 왜 안 지키냐.", "cry", {S_: "cry"}),
        L(S_, "아버님이 웃으시는 게 제 행복이에요. 미연이도 그걸 바랐을 거예요.", "cry", {F: "cry"}),
        L(F, "그럼 같이 지키자. 나는 오래 살고, 너는 네 인생도 살고.", "happy", {S_: "happy"}),
        L(N, "그날 새벽, 장인과 사위는 식은 찌개를 데워 마주 앉아 먹었습니다."),
        L(N, "아내의 부탁 하나로 십이 년을 지킨 사위. 여러분이 장인이었다면, 이 사위에게 뭐라고 하셨을까요?"),
    ]),
]

TITLE = "12년째 장인을 모시는 사위, 선 자리를 박차고 나간 날 수첩 첫 장을 보고 울었습니다"
DESC_SHORT = "아내를 먼저 보낸 뒤 12년째 장인을 모시는 사위. 몰래 만든 선 자리를 박차고 나간 날, 장인은 사위의 수첩 첫 장에서 딸의 부탁을 읽게 됩니다.\n※ AI 음성과 직접 그린 만화로 제작한 창작 사연입니다.\n#시니어사연 #감동사연 #사위 #장인 #인생이야기 #가족이야기 #Shorts"
proj = {
    "title": TITLE,
    "slug": "son-in-law-promise",
    "voice": "ko-KR-InJoonNeural",
    "narrator_gvoice": "ko-KR-Chirp3-HD-Charon",
    "cast": {
        F: {"name": "장인 오덕수", "gvoice": "ko-KR-Chirp3-HD-Charon", "color": "#6d6a75", "hair": "short", "hair_color": "#c9c3bc", "skin": "#efc6a2", "accessory": "glasses"},
        S_: {"name": "사위 정훈", "gvoice": "ko-KR-Chirp3-HD-Fenrir", "color": "#3f8f6b", "hair": "short", "hair_color": "#222222", "skin": "#f6d2b2"},
        M: {"name": "미연", "gvoice": "ko-KR-Chirp3-HD-Aoede", "color": "#f48fb1", "hair": "long", "hair_color": "#3a2618", "skin": "#fbdcc4"},
        N_: {"name": "순자 할머니", "gvoice": "ko-KR-Chirp3-HD-Vindemiatrix", "color": "#9575cd", "hair": "bun", "hair_color": "#d6d0ca", "skin": "#edc4a0"},
        E: {"name": "은희", "gvoice": "ko-KR-Chirp3-HD-Erinome", "color": "#4fc3f7", "hair": "bun", "hair_color": "#4a3020"},
    },
    "scenes": S,
    # 0:00 하이라이트: 절정 대사를 먼저 (수첩·새벽 대화 결말은 숨김)
    "teaser": [[s_yard, 3, 5], [s_open, 1, 2], [s_note, 3, 5]],
    "shorts_speed": 1.25,
    "shorts": [
        {"format": "full", "speed": 1.1, "clips": [[i] for i in full1], "hook": "12년째 장인 모신\n사위의 비밀",
         "hook_who": S_, "hook_emotion": "shock", "hook_tone": "red", "hook_prop": {"type": "notebook", "text": "아빠를 부탁해"},
         "cta_line": "두 사람의 십이 년, 더 긴 이야기는 아래 본편에서 들려 드릴게요.", "end_text": "더 긴 이야기는 본편에서 ▶",
         "title": "선 자리를 박차고 나간 사위, 수첩 첫 장에 적힌 아내의 부탁 #시니어사연 #감동사연 #사위 #장인 #인생이야기 #가족이야기",
         "description": DESC_SHORT},
        {"format": "full", "speed": 1.1, "clips": [[i] for i in full2], "hook": "아내가 남긴\n마지막 부탁",
         "hook_who": M, "hook_emotion": "cry", "hook_tone": "blue", "hook_prop": {"type": "notebook", "text": "아빠를 부탁해"},
         "cta_line": "장인과 사위의 이야기 전체는 아래 본편에서 볼 수 있어요.", "end_text": "전체 이야기는 본편에서 ▶",
         "title": "아내가 남긴 마지막 부탁, 사위는 12년을 지켰습니다 #시니어사연 #감동사연 #사위 #장인 #인생이야기 #눈물주의",
         "description": DESC_SHORT},
        {"clips": [[s_open, 1, 4], [s_yard, 3, 6]], "hook": "선 자리 박차고\n나간 사위",
         "hook_who": S_, "hook_emotion": "angry", "hook_tone": "red", "hook_prop": {"type": "notebook", "text": "약속"},
         "end_text": "사위가 지킨 약속은 본편에서 ▶",
         "title": "선 자리 박차고 나간 사위 #시니어사연 #감동사연 #사위"},
        {"clips": [[s_note, 3, 6], [s_promise, 0, 3]], "hook": "사위 수첩\n첫 장의 글씨",
         "hook_who": F, "hook_emotion": "cry", "hook_tone": "gold", "hook_prop": {"type": "notebook", "text": "아빠를 부탁해"},
         "end_text": "두 사람의 결말은 본편에서 ▶",
         "title": "사위 수첩 첫 장의 글씨 #시니어사연 #감동사연 #사위"},
    ],
    "thumbnail": {
        "text": "12년째 처가살이\n사위의 약속",
        "highlight": "사위의 약속",
        "badge": "눈물 주의",
        "variants": [
            {"style": "story", "tone": "red", "face": [F, "cry"], "prop": {"type": "notebook", "text": "아빠를 부탁해"}},
            {"style": "story", "tone": "blue", "face": [S_, "shock"], "text": "선 자리 박차고\n나간 사위", "highlight": "나간 사위",
             "badge": "12년의 비밀", "prop": {"type": "notebook", "text": "약속"}},
            {"style": "story", "tone": "gold", "face": [S_, "cry"], "text": "아내의\n마지막 부탁", "highlight": "마지막 부탁",
             "badge": "끝까지 보세요", "prop": {"type": "notebook", "text": "아빠를 부탁해"}},
        ],
    },
    "publish": {
        "title": TITLE,
        "title_variants": ["“아버님, 저 약속한 게 있어요”… 12년째 장인과 사는 사위가 끝내 숨긴 아내의 부탁",
                           "아내를 먼저 보내고 12년째 처가살이하는 사위, 장인이 몰래 만든 선 자리에서 일어난 일"],
        "description": "“아버님, 이게 뭐예요? 저 선 같은 거 안 봐요.” 아내를 먼저 보낸 뒤 12년째 시골에서 장인을 모시는 사위 정훈. 사위의 앞날이 걱정된 장인이 몰래 선 자리를 만들던 날, 사위는 처음으로 화를 내고 자리를 뜹니다. 그날 밤 장인은 사위의 낡은 수첩 첫 장에서 먼저 떠난 딸의 글씨를 발견합니다.\n\n⏱ 챕터\n{chapters}\n\n여러분이라면 정훈이처럼 할 수 있었을까요? 장인이었다면 사위를 놓아주셨을까요? 댓글로 들려주세요.\n\n※ 이 이야기는 창작 사연이며, 등장인물과 사건은 실제와 관련이 없습니다.\n※ AI 음성과 직접 그린 만화로 제작되었습니다.\n#사연 #시니어사연 #감동사연",
        "tags": ["사연", "시니어사연", "감동 사연", "사위", "장인", "처가살이", "가족 사연", "인생이야기", "사연 만화", "사연 애니메이션", "눈물 사연", "효도", "창작 사연"],
        "category": 1,
        "playlist": "감동 가족 사연",
        "publish_at": "2026-10-21T18:00:00+09:00",
        "pinned_comment": "여러분이라면 정훈이처럼 할 수 있었을까요? 장인이었다면 사위를 놓아주셨을까요? 🙏",
        "made_for_kids": False,
        "synthetic_media": True,
    },
}
times = ["2026-10-21T18:10:00+09:00", "2026-10-22T12:00:00+09:00", "2026-10-22T19:00:00+09:00", "2026-10-23T12:00:00+09:00"]
for s, t in zip(proj["shorts"], times):
    s["publish_at"] = t
json.dump(proj, open("project.json", "w"), ensure_ascii=False, indent=1)
lines = [l for s in S if not s.get("shorts_only") for l in s["lines"]]
print("scenes", len(S), "lines", len(lines), "chars", sum(len(l["text"]) for l in lines), "title", len(TITLE))
for k, f in (("full1", full1), ("full2", full2)):
    print(k, sum(len(l["text"]) for i in f for l in S[i]["lines"]), "chars")
