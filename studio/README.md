# 유튜브 자동화 스튜디오

`studio/index.html` (GitHub Pages: `/studio/`) 에서 부서별 프롬프트를 복사해 Claude Code 에 붙여넣으면
Claude 가 `project.json` 작성 → 롱폼/숏폼/썸네일 렌더링까지 수행합니다.

## 준비
    pip install pillow edge-tts
    sudo apt install ffmpeg fonts-nanum      # 한글 폰트(없으면 --font 로 지정)
    python3 studio/tools/studio.py check

## 사용
1. 대시보드 → 작업실에 원문 붙여넣기 → "총괄 PD" 프롬프트 복사 → Claude 에 붙여넣기
2. 결과: `studio/projects/<slug>/output/` 의 longform.mp4, short_XX.mp4, thumbnail.png
3. 업로드(수동) 후 대시보드의 로드맵/수익 트래커 갱신

`projects/example/` 에 샘플 project.json 이 있습니다.
