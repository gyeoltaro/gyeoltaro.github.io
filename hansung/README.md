# 무한의 격파 (한성태권도용)

좌우 버튼으로 송판, 겹송판, 기와를 끝없이 격파하는 2D 태권도 아케이드 게임입니다.

- 주소: https://gyeoltaro.github.io/hansung/
- `gyeokpa/` 게임을 복사한 별도 버전입니다. 족자 글씨는 "한성 태권도"이고, 최고 기록과 랭킹은 `gyeokpa/`와 섞이지 않습니다.
  - 랭킹은 같은 Firebase 프로젝트(`infinite-gyeokpa`)의 `hansung_ranking` 컬렉션에 따로 저장됩니다.
  - 이 폴더의 `firestore.rules`에는 모든 도장(gyeokpa, worldtkd, hansung)의 규칙이 함께 들어 있습니다. 콘솔에 규칙을 붙여 넣을 때는 이 파일을 쓰세요.
- 파일 하나(`index.html`)로 동작하고, 그래픽과 효과음, 배경음악을 모두 브라우저에서 직접 그리고 연주합니다.
- 랭킹전은 Firebase(Firestore)에 저장됩니다. 설정 전에는 랭킹 화면에 "준비 중"이 표시되고, 나머지 게임은 그대로 동작합니다.

## 파일

| 파일 | 내용 |
|---|---|
| `index.html` | 게임 전체 |
| `firebase-config.js` | Firebase 웹 설정값. 여기에 값을 넣으면 랭킹전이 켜집니다 |
| `firestore.rules` | 랭킹 보안 규칙. Firebase 콘솔에 붙여 넣습니다 |

## 랭킹전 켜기 (Firebase 설정)

1. https://console.firebase.google.com 에서 **프로젝트 추가**를 누릅니다. 이름은 예를 들어 `infinite-gyeokpa`로 하고, Google 애널리틱스는 꺼도 됩니다.
2. 왼쪽 메뉴 **빌드 > Authentication > 시작하기 > 로그인 방법**에서 **익명**을 켭니다.
   - 플레이어마다 로그인 없이 기기별 아이디가 생기고, 자기 기록만 고칠 수 있게 하는 데 씁니다.
3. 같은 Authentication의 **설정 > 승인된 도메인**에 `gyeoltaro.github.io`를 추가합니다.
4. **빌드 > Firestore Database > 데이터베이스 만들기**를 누릅니다. 위치는 `asia-northeast3 (서울)`, 모드는 **프로덕션 모드**로 고릅니다.
5. Firestore의 **규칙** 탭에 `firestore.rules` 내용을 그대로 붙여 넣고 **게시**합니다.
   - 같은 Firebase 프로젝트를 다른 앱과 같이 쓰고 있다면, 기존 규칙을 지우지 말고 `match /ranking/{uid} { ... }`와 `match /hansung_ranking/{uid} { ... }` 부분만 합쳐 넣으세요.
6. 톱니바퀴 **프로젝트 설정 > 일반 > 내 앱**에서 웹(`</>`) 앱을 추가합니다. 호스팅 설정은 체크하지 않아도 됩니다.
7. 화면에 나오는 `firebaseConfig` 값을 `firebase-config.js`의 `null` 자리에 넣습니다.

## 운영 메모

- **무료 사용량:** Firestore 무료 한도는 하루 읽기 5만 건입니다. 게임을 한 번 열 때 랭킹 상위 100개를 읽으므로, 하루 수백 번 열리는 정도까지는 무료로 충분합니다.
- **기록 삭제:** 부적절한 닉네임은 Firebase 콘솔 **Firestore Database > 데이터 > hansung_ranking**에서 해당 문서를 지우면 됩니다.
- **점수 조작 방어:** 로그인 없는 게임이라 점수 조작을 완전히 막을 수는 없습니다. 보안 규칙은 형식, 범위(10만 장 이하), 자기 기록만 갱신하는 조건을 검사합니다.
