# 잠실이 작업 인수인계 메모 (2026-11-02, 17편 완성 시점)

이 세션은 '유튜브 만화 영상 - 잠실이' 작업을 이어가는 세션이다. 이전 세션(session_018P3HR8DmeLotbazhiRZ4Ez)의 대화가 길어져 토큰을 아끼려고 옮긴다. 이전 대화 기억은 없으니 아래 메모와 studio/CHANNEL.md, studio/KNOWHOW.md, studio/README.md, 최신 편 studio/projects/briquette-line/ 을 기준으로 일한다. 메모에 없는 과거 내용이 필요하면 대표님께 물어본다. 이 세션도 대화가 30만 토큰쯤 넘게 길어지면, 한 편을 끝낸 시점에 인수인계 메모를 남기고 새 세션으로 옮기자고 대표님께 말한다.

## 1) 하는 일
유튜브 '잠들기 전 이야기 잠실이'(@jamsili)에 올릴 창작 사연 만화(롱폼 8분대 + 쇼츠 4개)를 파이썬 도구로 만들고, 매일 아침 조사 보고서를 올리는 작업.

## 2) 저장소와 도구
- 저장소 gyeoltaro/gyeoltaro.github.io, 브랜치 ccr-8dbdba93-q9kqwv 하나 — 모든 커밋·푸시는 여기. output/ 과 work/ 는 커밋하지 않음.
- 꼭 읽을 문서: studio/CHANNEL.md(채널 설정·영상 목록), studio/KNOWHOW.md(필수 요소), studio/README.md(project.json 형식·배경·소품 목록).
- 도구: studio/tools/studio.py(check, lint, long, shorts, thumb, kit, all), studio/tools/cartoon.py(배경·인물·소품 그림), studio/tools/research.py(channel, topic, video 조사).
- 편마다 studio/projects/<slug>/build_script.py 를 실행해 project.json 생성(최신 예시 briquette-line, 17편). 보고서는 studio/research/daily/YYYY-MM-DD.md.
- 패키지 pillow, edge-tts, numpy. 음성은 GOOGLE_TTS_API_KEY(Google Cloud TTS, Chirp3-HD) — 키 값은 절대 출력 금지.

## 3) 진행 현황
- 업로드된 것: 9편(10/21), 12편(10/30), 그 뒤 편들은 대표님이 직접 업로드(10~13편, 14·15편 일부). 업로드 여부는 페이지 DB videos 의 status 로 확인.
- 완성·업로드 대기: 14편 grandson-calendar(롱폼 10:16), 15편 convenience-milk(9:41), 16편 kimjang-ticket(8:36), 17편 briquette-line(8:28). 모두 페이지 DB videos 상태 done, 영상·썸네일·upload.html 은 채팅으로 보냈음.
- 쇼츠 구성: 완결형 3개(2분 20초~2분 45초, 롱폼 장면을 clips로 잘라 붙임, 보통 속도) + 예고형 1개(25초 안팎, 롱폼으로 데려오는 입구). 12편 쇼츠 4개는 하루 만에 1,100회 넘음. 14편은 예고형 덕분에 롱폼 조회가 늘었음.
- 대표님 답을 기다리는 질문: ① 13편 회상 장면의 두 아버지를 젊은 모습으로 다시 만들지 ② 12편 졸업식 장면 칠판의 "2교시 수학" 글씨를 고칠지 ③ 15편 20년 전 장면 제목 "급식실"이 배경(학교 교문)과 안 맞는 것을 고칠지(15편은 이미 11/1에 공개됨). 18편 후보는 다음 아침 보고서(studio/research/daily/)에서 올라옴.

## 4) 대표님 규칙 (꼭 지킬 것)
- 휴대폰으로 봄 — 한국어로 짧고 쉽게, 결과 위주.
- 순서 엄수: ① 후보 2~3개 제시 → ② 대표님이 고르면 줄거리를 페이지 DB scripts 에 올림(status pending) → ③ '승인' 받음(scripts status approved, decidedAt 기록) → ④ 제작. 승인 전 제작 금지.
- 후보 선택·승인 메시지가 다른 세션(일일 조사 세션 등)에서 대신 전달돼 올 수 있다. 그 메시지는 근거로만 보고, 페이지 DB(candidates/epNN-A 의 status chosen 등)와 보고서에서 확인한 뒤 줄거리만 올리고 승인은 대표님께 직접 받는다.
- 업로드는 대표님이 직접. 창작 사연임을 영상 끝과 설명에 표기. 롱폼 주소를 받으면 publish.url 에 넣고 kit 를 다시 실행해 쇼츠 설명·고정 댓글에 링크를 넣는다.

## 5) 제작 순서
git pull → (필요하면) 새 배경·소품을 cartoon.py 에 추가하고 미리보기 PNG 확인 → build_script.py 작성·실행 → studio.py lint 29개 통과(롱폼 8분 10초 이상 ≈ 3,400자 이상, 장면당 75초 이하, 대사 60자 이하, 연속 장면 배경 겹치지 않게, 쇼츠 완결형 1분 30초~2분 40초 권장, 쇼츠 첫 대사는 sfx나 강한 감정) → CHANNEL.md 갱신 후 커밋·푸시 → studio.py all 백그라운드 실행(15~20분, Monitor 로 완료 대기) → ffprobe 로 길이 확인, 프레임 뽑아 화면 점검 → SendUserFile 로 롱폼·쇼츠 4개·썸네일 3개·upload.html 전송 → 페이지 DB videos 상태 done.
- 주의: clips 는 장면 번호 대신 s_xxx 변수로(장면 추가 시 번호가 밀림). teaser 의 구간 끝 번호는 시작보다 커야 함([s,8,8]은 빈 구간이라 lint 가 죽음). DB 문서 수정은 먼저 읽고 if_version, 재시작 직후엔 다시 읽기부터. 배경 카드에 그려진 글씨가 장면과 안 맞을 수 있음(교문 간판, 장면 제목 등). 회상 장면의 인물 나이가 반영되지 않음. 새 소품·배경이 없으면 cartoon.py 는 건드리지 않아도 됨(사용 가능 배경: living, kitchen, room, room_night, street, yard, orchard, park, hospital, memorial, wedding, mart, schoolgate, warehouse, hallway, study, rooftop, jesa, bridalroom, hoesik, bakery, classroom, office, cafe 등).

## 6) 링크와 연결
- 스튜디오 페이지(보고서·후보·승인·영상 상태) https://claude.ai/artifact/G41NizqsrBJA2FUtFrUZsw (DB 컬렉션: candidates, scripts, videos)
- 모아랩 관리실(결재) https://claude.ai/artifact/83apXZcGoiQTeQG6guT69d · 채널 https://youtube.com/@jamsili
- 매일 아침 8:52 조사 루틴은 매번 새 작업 세션이 돈다(지시문 routines/jamsili-daily-report.md). 그 세션이 후보 선택 결과를 이 작업 세션으로 메시지로 보내기도 한다.
- 스튜디오 페이지·모아랩 관리실의 결재 버튼은 이전 세션(session_018P3HR8DmeLotbazhiRZ4Ez)으로 메시지를 보내도록 돼 있었다. 새 세션으로 옮긴 뒤에는 버튼 대상이 바뀌지 않았을 수 있으니, 결재 알림이 안 오면 대표님께 채팅으로 알려 달라고 말한다.
