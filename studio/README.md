# 유튜브 자동화 스튜디오

`studio/index.html` (GitHub Pages: `/studio/`) 에서 부서별 프롬프트를 복사해 Claude Code 에 붙여넣으면
Claude 가 만화 콘티 `project.json`(cast·bg·lines) 작성 → 롱폼/숏폼/썸네일 렌더링까지 수행합니다.

## 준비
    pip install pillow edge-tts
    sudo apt install ffmpeg fonts-nanum      # 한글 폰트(없으면 --font 로 지정)
    python3 studio/tools/studio.py check

## 사용
1. 대시보드 → 작업실에 원문 붙여넣기 → "총괄 PD" 프롬프트 복사 → Claude 에 붙여넣기
2. 결과: `studio/projects/<slug>/output/` 의 longform.mp4, short_XX.mp4, thumbnail.png
3. 업로드(수동) 후 대시보드의 로드맵/수익 트래커 갱신

`projects/example/` 에 샘플 project.json 이 있습니다.

## 만화 형식
캐릭터와 배경은 코드로 직접 그립니다(`tools/cartoon.py`) — 외부 이미지 불필요.
- `cast`: 캐릭터별 이름·셔츠색·머리·안경/리본·목소리(edge-tts)·피치
- 장면 `bg`: room / street / office / cafe / park / night / plain
- 대사 `emotion`: normal / happy / sad / angry / surprised / think (표정·팔·이펙트 변화), `react` 로 듣는 쪽 반응
- 음성: Google Cloud TTS(환경변수 GOOGLE_TTS_API_KEY, 캐릭터별 `gvoice` 로 음성 지정 가능) → edge-tts → 구글 번역 음성(남성 캐릭터는 음높이 변환) → espeak-ng → 무음 순으로 자동 대체
- 말하는 캐릭터는 입이 움직이고 눈을 깜빡이며, 대사는 하단 자막+이름표로 표시됩니다.
- `lines` 없이 `narration` 만 있는 장면은 기존 슬라이드 형식으로 렌더링됩니다.

## 속도
- 대사 음성은 8개씩 동시에, 만화 프레임은 CPU 코어 수만큼 병렬로 만듭니다 (약 6분 영상 + 숏폼 3개 ≈ 2분, 4코어 기준).
- 분량 기준: 분당 약 400자(Google 음성 실측). 8분(미드롤 광고 기준)이면 대사 약 3,200자 이상 — 렌더링 후 부족하면 추가할 글자 수를 알려 줍니다.
- `--fast`: 미리보기용 빠른 인코딩(가변 프레임레이트). 업로드용은 옵션 없이 렌더링하세요.

## 시뮬레이션 예시
`projects/sim-habit/` — 퍼온 글(source.txt)부터 부서별 산출물(01 소재선별, 02 재각본, project.json, 10 숏폼 업로드, 11 SEO, 13 검수)까지 실제 파이프라인 결과 예시.

## 숏폼 (3초 후크 + 배속)
- 첫 장면에 **후크 카드**가 자동으로 붙습니다: 큰 글씨 + 폭발 배경 + 캐릭터가 `hook_line` 을 외침 (약 1~2초) → 바로 본론
- 기본 **1.25배속** (`shorts_speed`, 숏폼별 `speed` 로 변경). 음높이는 유지됩니다.
- `shorts[]`: `scenes`, `hook`(상단 고정 문구), `hook_line`(후크 대사, 없으면 hook 사용), `hook_who`, `hook_emotion`, `speed`

## 썸네일 (A/B/C 3종)
`thumb` 명령이 `thumbnail.png`(A), `thumbnail_b.png`, `thumbnail_c.png` 를 만듭니다 — 유튜브 **테스트 및 비교**(썸네일 3개 A/B 테스트)용.
- 구성: 집중선 배경 + 확대한 캐릭터(흰 스티커 테두리) + 초대형 굵은 글씨 + 강조 박스 + 배지
- `thumbnail`: `text`(2줄은 `\n`), `highlight`(강조 단어), `badge`(좌상단 문구), `variants`(최대 3개: `palette` yellow/blue/red/green/purple, `chars` [[캐릭터, 표정], …])
- 굵은 폰트: Noto Sans CJK KR Black. 클라우드 세션에서는 `.claude/hooks/session-start.sh` 가 자동 설치 (로컬은 `sudo apt install fonts-noto-cjk-extra`)

## 리서치·분석 (YouTube Data API v3)
공개 데이터로 주제 수요, 떡상 공식, SEO 를 분석합니다. 결과는 `studio/research/<이름>/report.md`(+`data.json`), 끝에 Claude 가 답할 분석 질문이 붙습니다. 원자료는 YouTube API 개발자 정책에 따라 git 에 올리지 않고 30일 뒤 자동 삭제합니다.
```
python3 studio/tools/research.py topic "습관 만들기" --days 90 [--long|--shorts]   # 주제 리서치 (검색 1회=할당량 100)
python3 studio/tools/research.py video https://youtu.be/VIDEO_ID                  # 왜 잘 됐나 (비교군 대비)
python3 studio/tools/research.py channel @내채널                                   # 채널 회고
python3 studio/tools/research.py trend --days 180                                 # 한국 인기 영상 종합 + 장르 10개 비교 (할당량 약 1,600)
```
- 지표: 하루 조회수, **구독자 대비 조회수 배수**(떡상 지표), 참여율, 제목 패턴(길이·숫자·질문형·괄호), 영상 길이, 업로드 요일·시간, 자주 쓰인 단어·태그, 인기 댓글
- 준비: Google Cloud 콘솔에서 **YouTube Data API v3 사용 설정** + API 키 제한사항에 추가 (키는 `GOOGLE_TTS_API_KEY` 재사용, 또는 `YOUTUBE_API_KEY`)
- 시청 지속률·CTR·유입 경로 같은 비공개 통계는 YouTube Analytics API(OAuth) 가 필요 — 현재는 YouTube 스튜디오 수치를 붙여넣어 분석

## 업로드
**지금 (심사 전): 업로드 키트**
`python3 studio/tools/studio.py kit studio/projects/<slug>/project.json` → `output/upload.html`
- 휴대폰에서 열어 제목, 설명(챕터 자동 계산), 태그, 고정 댓글을 **복사 버튼**으로 붙여넣고 YouTube 앱으로 올립니다. 영상 1편에 1~2분.
- 업로드 정보는 `project.json` 의 `publish`(롱폼)와 `shorts[]`의 `title`, `publish_at`.

**심사 통과 후: 자동 업로드** (`studio/tools/upload.py`)
```
python3 studio/tools/upload.py auth                       # 최초 1회 계정 연결 (google.com/device 에 코드 입력)
python3 studio/tools/upload.py upload <project.json> --dry-run
python3 studio/tools/upload.py upload <project.json>      # 예약 업로드 + 썸네일 + 재생목록, 중복 업로드 방지
```
- 2020년 7월 28일 이후 만든 프로젝트는 **YouTube API 심사 전에는 업로드 영상이 비공개로 잠깁니다.** 심사 준비는 `studio/api-audit/README.md`.
- 개인정보처리방침과 약관 페이지: `studio/legal/privacy.html`, `studio/legal/terms.html`

## 사연 만화 기능
- 음성: 캐릭터별 `gvoice` 에 Google **Chirp3-HD** 음성(예: `ko-KR-Chirp3-HD-Aoede`, `-Charon`, `-Puck`, `-Gacrux`, `-Kore`)을 지정하면 가장 자연스럽습니다. 해설 목소리는 `narrator_gvoice`.
- 배경: `hospital`(병실), `memorial`(추모·장례식장) 추가. 별칭 `funeral`, `bank`(=office), `hoesik`(회식 고깃집: 메뉴패·홍등·불판, 별칭 `restaurant`·`bar`·`bbq`), `warehouse`(새벽 물류센터), `bakery`(빵집), `hallway`(아파트 복도), `wedding`(결혼식장)
- 장면 `lying: ["dad"]`: hospital 배경의 침대에 누운 모습으로 그림
- 장면 `shorts_only: true`: 롱폼·챕터에서는 빠지고 숏폼에만 쓰는 장면 (예: "결말은 본편에서")
- 예시: `projects/dad-bankbook/` (창작 사연, `build_script.py` 가 대본 원본) · `projects/mil-sidedish/` · `projects/newbie-ceo/` · `projects/divorce-eve/` · `projects/upstairs-grandma/`(시점 전환)

## 연출 (자동 작곡·효과음·카메라)
- **배경음악**: 장면 `mood`(warm/sad/tense/calm/hope)에 맞춰 `tools/sound.py` 가 코드로 작곡 — 저작권 없음. 대사가 나오면 자동으로 작아짐(사이드체인). `music: false` 로 끄기, `music_volume` 로 크기 조절. mood 가 없으면 대사 감정으로 추정
- **효과음**: 장면 전환 시 whoosh 자동, 대사에 `"sfx": "ding"|"thud"|"whoosh"`
- **카메라**: 장면 첫 대사·해설은 전체 샷, 감정 대사(sad/surprised/angry)는 말하는 사람 클로즈업, 나머지는 번갈아. 대사별 `"shot": "close"|"wide"`, 장면 `"shots": "wide"` 로 고정
- **캐릭터 크기**: `"scale": 0.72` (회상 속 어린 시절)
- **배경 추가**: `living`(거실), `kitchen`(부엌), `room_night`(밤 방)
- **음량**: 최종 단계에서 loudnorm 으로 약 -14~-16 LUFS 표준화

## 후킹 (썸네일 · 숏폼 첫 화면)
- **감정 표정 추가**: `cry`(ㅠㅠ 눈물 줄기·우는 입), `shock`(큰 흰 눈·이마 그늘선·느낌표)
- **소품**: `bankbook`(통장+금액), `letter`(편지), `money`(돈다발), `phone`(휴대폰), `photo`, `sidedish`(반찬통+쪽지), `key`(열쇠+이름표), `calendar`(달력+큰 글씨) — 빨간 원과 화살표로 시선을 끔
- **사연형 썸네일**: `thumbnail.variants[]` 에 `"style": "story"`, `tone`(red/blue/gold), `face`([캐릭터, 감정]), `prop`
- **숏폼 첫 화면(후크 카드)**: `shorts[]` 에 `hook`(2줄 큰 문구), `hook_emotion`, `hook_tone`, `hook_prop`. 첫 프레임은 온전한 표지, 0.1초 뒤 펀치 줌, 충격음

## 쇼츠 구성 (데이터·자료 조사 반영, 2026-10)
- 근거: 사연·감동 사연 쇼츠 조회수 상위 25%의 길이 중앙값 28~50초(나머지 74~82초), 제목 33~35자·해시태그 약 2개. 이탈의 50~60%가 첫 3초에 발생
- **표지 0.35초** → 곧바로 이야기 시작 (정지 화면 없음). 첫 대사 위에 큰 후크 문구
- `clips: [[장면, 시작줄, 끝줄], …]` 로 결정적인 대사부터 잘라 붙임 (느린 해설 생략)
- **구절 자막**: 크고 굵은 글씨가 말에 맞춰 짧은 구절 단위로 바뀜, 숫자는 노랑
- **떠다니는 카메라**: 기본 꺼짐 (사용자 피드백). 필요하면 `"drift": true`
- 쇼츠는 클로즈업 위주, 대사 사이 여백 0.06초
- 끝은 별도 장면 대신 `end_text` 안내 문구를 마지막 대사 위에 겹쳐 표시 (3초 절약)
- 슬픈 장면(mood: sad)에서는 듣는 인물의 기본 표정도 슬픔

## 필수 요소 점검 (KNOWHOW.md, 2026-10-06 조사)
- `python3 studio/tools/studio.py lint <project.json>` — 렌더링 전에 대본을 29개 항목으로 점검합니다(`all` 실행 시 맨 먼저 실행)
  - 항목: 길이 8분 이상, 0:00 하이라이트, 첫 20초 충격, 감정 비트 간격 90초 이하, 장면 75초 이하, 배경 연속 금지, 해설 비중 45% 이하, 시점 표시, 맺음 질문, 창작 표시, 최종 화면 20초, 제목 길이·A/B, 설명 질문·챕터, 쇼츠 길이·후크·첫 대사
- **0:00 하이라이트**: `"teaser": [[장면, 시작줄, 끝줄], …]` → 롱폼 맨 앞에 절정 대사 + 빨간 "▶ 하이라이트" 표시, 챕터 `0:00 하이라이트`
- **회상**: 장면에 `"flashback": true`(세피아 톤), `"when": "20년 전"`(오른쪽 위 배지)
- **쇼츠 반복 재생**: 끝에 표지를 0.45초 다시 붙여 첫 프레임과 이어짐 (`"shorts_loop": false` 로 끔)
- **제목 A/B/C**: `publish.title_variants` → 업로드 키트에 복사 칸. 키트에는 중간광고 추천 위치와 최종 화면 안내도 표시
- **장면별 해설 목소리**: 대사에 `"voice": "<인물 id>"` 를 넣으면 해설(narrator) 줄을 그 인물 목소리로 읽음 — 시점 전환 구성(예: 2부는 위층 할머니가 해설)
