#!/bin/bash
# 클라우드 세션 시작 시 유튜브 스튜디오(studio/) 렌더링에 필요한 패키지 설치
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# 파이썬 패키지 (Pillow: 그림, edge-tts: 음성)
python3 -c "import PIL, edge_tts" 2>/dev/null || pip install -q pillow edge-tts

# apt 패키지: 썸네일용 굵은 한글 폰트(Noto Sans CJK Black), 오프라인 대체 음성(espeak-ng)
need=()
[ -f /usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc ] || need+=(fonts-noto-cjk-extra)
command -v espeak-ng >/dev/null 2>&1 || need+=(espeak-ng)
command -v ffmpeg >/dev/null 2>&1 || need+=(ffmpeg)
if [ ${#need[@]} -gt 0 ]; then
  export DEBIAN_FRONTEND=noninteractive
  apt-get install -y -q "${need[@]}" >/dev/null 2>&1 || {
    apt-get update -q >/dev/null 2>&1
    apt-get install -y -q "${need[@]}" >/dev/null 2>&1
  }
fi

echo "studio 준비 완료: $(python3 "$CLAUDE_PROJECT_DIR/studio/tools/studio.py" check 2>&1 | tr '\n' ' ')"
