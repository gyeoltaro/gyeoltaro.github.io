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
공개 데이터로 주제 수요, 떡상 공식, SEO 를 분석합니다. 결과는 `studio/research/<이름>/report.md`(+`data.json`), 끝에 Claude 가 답할 분석 질문이 붙습니다.
```
python3 studio/tools/research.py topic "습관 만들기" --days 90 [--long|--shorts]   # 주제 리서치 (검색 1회=할당량 100)
python3 studio/tools/research.py video https://youtu.be/VIDEO_ID                  # 왜 잘 됐나 (비교군 대비)
python3 studio/tools/research.py channel @내채널                                   # 채널 회고
python3 studio/tools/research.py trend --days 180                                 # 한국 인기 영상 종합 + 장르 10개 비교 (할당량 약 1,600)
```
- 지표: 하루 조회수, **구독자 대비 조회수 배수**(떡상 지표), 참여율, 제목 패턴(길이·숫자·질문형·괄호), 영상 길이, 업로드 요일·시간, 자주 쓰인 단어·태그, 인기 댓글
- 준비: Google Cloud 콘솔에서 **YouTube Data API v3 사용 설정** + API 키 제한사항에 추가 (키는 `GOOGLE_TTS_API_KEY` 재사용, 또는 `YOUTUBE_API_KEY`)
- 시청 지속률·CTR·유입 경로 같은 비공개 통계는 YouTube Analytics API(OAuth) 가 필요 — 현재는 YouTube 스튜디오 수치를 붙여넣어 분석
