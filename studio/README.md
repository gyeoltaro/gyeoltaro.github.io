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
- 말하는 캐릭터는 입이 움직이고 눈을 깜빡이며, 대사는 하단 자막+이름표로 표시됩니다.
- `lines` 없이 `narration` 만 있는 장면은 기존 슬라이드 형식으로 렌더링됩니다.
