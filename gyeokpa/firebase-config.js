// 무한의 격파 랭킹전 Firebase 설정
//
// Firebase 콘솔 > 프로젝트 설정 > 일반 > 내 앱(웹)에 나오는 firebaseConfig 값을
// 아래 null 자리에 넣으면 랭킹전이 켜집니다. 그 전까지는 랭킹 화면에 "준비 중"이 표시됩니다.
// 이 값들은 브라우저에 공개되는 웹 설정이라 저장소에 올려도 괜찮습니다.
// 실제 보호는 firestore.rules(보안 규칙)가 맡습니다.
//
// 예시:
// window.GYEOKPA_FIREBASE = {
//   apiKey: "AIza...",
//   authDomain: "프로젝트ID.firebaseapp.com",
//   projectId: "프로젝트ID",
//   storageBucket: "프로젝트ID.appspot.com",
//   messagingSenderId: "1234567890",
//   appId: "1:1234567890:web:abcdef"
// };
window.GYEOKPA_FIREBASE = null;
