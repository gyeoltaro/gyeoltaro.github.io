// 무한의 격파 랭킹전 Firebase 설정 (프로젝트: infinite-gyeokpa)
//
// Firebase 콘솔 > 프로젝트 설정 > 일반 > 내 앱(웹)에 나오는 firebaseConfig 값입니다.
// null로 바꾸면 랭킹전이 꺼지고 랭킹 화면에 "준비 중"이 표시됩니다.
// 이 값들은 브라우저에 공개되는 웹 설정이라 저장소에 올려도 괜찮습니다.
// 실제 보호는 firestore.rules(보안 규칙)가 맡습니다.
window.GYEOKPA_FIREBASE = {
  apiKey: "AIzaSyCQw_URVDOTHrrsjMcM7d2pdJDClSU8oo0",
  authDomain: "infinite-gyeokpa.firebaseapp.com",
  projectId: "infinite-gyeokpa",
  storageBucket: "infinite-gyeokpa.firebasestorage.app",
  messagingSenderId: "431964854317",
  appId: "1:431964854317:web:7ee0f5856e3149f218c0a4"
};
