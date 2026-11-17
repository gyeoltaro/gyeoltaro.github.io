# 하늘 발차기 (국가대표태권도용)

움직이는 송판을 밟고 하늘 끝까지 뛰어오르는 2D 태권도 점프 아케이드 게임입니다.

- 주소: https://gyeoltaro.github.io/nationaltkd/skykick/
- `skykick/` 게임을 복사한 별도 버전입니다. 도장 현판 글씨는 "국가대표 태권도"이고, 최고 기록과 랭킹은 다른 도장 버전이나 무한의 격파와 섞이지 않습니다.
  - 이 기기의 최고 기록과 설정은 `skykick_nationaltkd.*` 이름으로 저장됩니다.
  - 랭킹은 같은 Firebase 프로젝트(`infinite-gyeokpa`)의 `skykick_nationaltkd_ranking` 컬렉션에 따로 저장됩니다.
- 게임 방법, 발판 종류, 띠 승급 기준은 [`skykick/README.md`](../../skykick/README.md)와 같습니다.

## 파일

| 파일 | 내용 |
|---|---|
| `index.html` | 게임 전체. 스크립트 맨 위 `DOJANG` 설정만 원본과 다릅니다 |
| `firebase-config.js` | Firebase 웹 설정값 (무한의 격파와 같은 프로젝트) |
| `firestore.rules` | 모든 도장, 모든 게임의 랭킹 규칙을 담은 공용 규칙 |

## 랭킹전 켜기 (한 번만)

1. https://console.firebase.google.com/project/infinite-gyeokpa/firestore 를 열고 위쪽 **규칙** 탭을 누릅니다.
2. 기존 내용을 모두 지우고 `firestore.rules` 내용을 그대로 붙여 넣은 뒤 **게시**합니다.
   - 기존 무한의 격파 5개 도장과 어울림 태권도 하늘 발차기 규칙이 그대로 들어 있어서, 통째로 바꿔도 기존 랭킹은 그대로 동작합니다.

규칙을 올리기 전에는 랭킹 화면에 "랭킹전은 준비 중이에요"가 표시되고, 게임은 그대로 할 수 있습니다.
