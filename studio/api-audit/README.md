# YouTube API 심사 준비 가이드

목표: 우리 Google Cloud 프로젝트가 API로 올린 영상이 **비공개로 잠기지 않도록** YouTube API 심사(Audit)를 통과하는 것.
심사 전에도 아래 1~3단계를 하면 자동 업로드를 **테스트**할 수 있습니다. 테스트 영상은 비공개로 잠깁니다.

---

## 1. OAuth 동의 화면 만들기 (Google Cloud 콘솔, 약 5분)
1. console.cloud.google.com → 기존 프로젝트 선택
2. **API 및 서비스 → OAuth 동의 화면** (또는 "Google 인증 플랫폼 → 브랜딩")
   - 사용자 유형: **외부**
   - 앱 이름: `Gyeoltaro Studio`
   - 사용자 지원 이메일 / 개발자 연락처: 본인 이메일
   - 앱 홈페이지: `https://gyeoltaro.github.io/studio/`
   - 개인정보처리방침: `https://gyeoltaro.github.io/studio/legal/privacy.html`
   - 서비스 약관: `https://gyeoltaro.github.io/studio/legal/terms.html`
3. **데이터 액세스(범위)**: `.../auth/youtube.upload`, `.../auth/youtube` 추가
4. **대상(테스트 사용자)**: YouTube 채널에 쓰는 구글 계정을 추가
   - 게시 상태가 "테스트"면 로그인 연결이 **7일마다 만료**됩니다. 그때마다 `upload.py auth`를 다시 실행하세요.

## 2. OAuth 클라이언트 ID 만들기
**API 및 서비스 → 사용자 인증 정보 → + 사용자 인증 정보 만들기 → OAuth 클라이언트 ID**
- 애플리케이션 유형: **TV 및 입력 제한 기기** (휴대폰에서 코드만 입력하면 연결됩니다)
  - 이 유형에서 YouTube 권한이 거부되면 **데스크톱 앱**으로 하나 더 만들고 `auth --manual`을 씁니다.
- 생성된 **클라이언트 ID**와 **클라이언트 보안 비밀번호**를 클라우드 환경 설정의 환경 변수에 추가합니다.
  ```
  YT_CLIENT_ID=....apps.googleusercontent.com
  YT_CLIENT_SECRET=....
  ```

## 3. 채널 연결 (Claude가 실행)
새 세션에서 Claude에게 "유튜브 계정 연결해줘"라고 말하면 `python3 studio/tools/upload.py auth`를 실행합니다.
화면에 나온 코드를 휴대폰의 google.com/device 에 입력하고 허용하세요.
발급된 `YT_REFRESH_TOKEN=...`을 환경 변수에 추가하면 연결이 끝납니다.

## 4. 심사 신청
- 신청서: **YouTube API Services – Audit and Quota Extension Form** (https://support.google.com/youtube/contact/yt_api_form)
  - 주소가 바뀌었으면 위 이름으로 검색하세요.
- 준비물
  - [x] 개인정보처리방침·약관 페이지 연락처: kkjlg@naver.com
  - [ ] 데모 영상 (아래 5번 대본, 화면 녹화 2~3분, YouTube에 "일부 공개"로 올려 링크 첨부)
  - [ ] 아래 6번 영문 답변을 신청서 항목에 붙여넣기
- 결과는 이메일로 옵니다. 추가 질문이 오면 그 메일을 Claude에게 보여 주세요. 답장 초안을 써 드립니다.
- 통과하면 환경 변수에 `YT_AUDITED=1`을 추가합니다. 그 뒤로는 경고 없이 바로 예약 공개 업로드가 됩니다.

## 5. 데모 영상 대본 (화면 녹화)
1. 대시보드 `https://gyeoltaro.github.io/studio/` → 작업실에 원문 붙여넣기 → 프롬프트 생성 (10초)
2. 렌더링 결과 `output/` 폴더: 롱폼, 숏폼, 썸네일 (10초)
3. `upload.py upload ... --dry-run` 출력: 제목, 설명, 예약 시간, `containsSyntheticMedia: true`, `selfDeclaredMadeForKids: false` 표시 (20초)
4. `upload.py auth` → google.com/device 에서 본인 계정으로 허용하는 동의 화면 (30초)
5. 실제 업로드 → YouTube 스튜디오에서 예약 상태, 썸네일, 재생목록 확인 (30초)
6. Google 계정 → 서드 파티 액세스에서 권한 철회가 가능함을 보여 주기 (10초)

## 6. 신청서 영문 답변 초안
> 신청서의 실제 항목명과 다를 수 있으니, 비슷한 항목에 맞춰 붙여넣으세요.

**App / project name**
Gyeoltaro Studio

**Describe your use of the YouTube API Services**
Gyeoltaro Studio is a private, single-user production tool that I (the channel owner) use to publish my own original cartoon videos to my own YouTube channel. It renders videos from scripts I write, then uses `videos.insert` to upload them as scheduled (`publishAt`) videos, `thumbnails.set` to set my custom thumbnail, and `playlists`/`playlistItems` to add them to my own playlists. Every upload sets `containsSyntheticMedia: true` (the videos use synthetic voices) and `selfDeclaredMadeForKids: false`. Separately, it uses an API key with `search.list`, `videos.list`, `channels.list` and `commentThreads.list` to read public data and write internal research reports about which topics and title styles perform well. Those reports are seen only by me.

**Which API clients / users will access the API?**
One user: the owner of the channel. There is no public sign-up, and no other accounts are authorized.

**OAuth scopes requested and why**
- `https://www.googleapis.com/auth/youtube.upload`: upload my own rendered videos.
- `https://www.googleapis.com/auth/youtube`: set thumbnails and manage my own playlists.

**How is API data stored?**
The OAuth refresh token is stored only as an encrypted environment secret in my private build environment. It is never committed to the source repository or written to logs. Public API data used for research is kept locally for at most 30 days and then deleted automatically (`research.py` prunes files older than 30 days on every run). Raw API data is excluded from the public repository through `.gitignore`. No API data is shared, sold, or used for advertising.

**Expected usage / quota**
About 1 long-form video and 3–4 Shorts per day, plus a few read-only research queries per day. This fits within the default quota of 10,000 units per day. I am not requesting a quota increase.

**Links**
- Homepage: https://gyeoltaro.github.io/studio/
- Privacy policy: https://gyeoltaro.github.io/studio/legal/privacy.html
- Terms of service: https://gyeoltaro.github.io/studio/legal/terms.html
- Source code: https://github.com/gyeoltaro/gyeoltaro.github.io/tree/main/studio
- Demo video: (데모 영상 링크)

## 7. 규정 준수 체크리스트 (심사에서 자주 보는 것)
- [x] 업로드 시 합성 콘텐츠 공개(`containsSyntheticMedia`)와 아동용 아님 설정
- [x] 본인 채널 외 다른 채널에 쓰기 작업(댓글, 좋아요, 구독) 없음
- [x] API 원자료 30일 초과 보관 안 함, 저장소에 원자료 없음
- [x] 개인정보처리방침에 YouTube 서비스 약관, Google 개인정보처리방침 링크, 권한 철회 방법 명시
- [x] 연락처 이메일 기입 (kkjlg@naver.com)
- [ ] 데모 영상 링크
