# 매일 콘텐츠 제작 순서 (예약 작업용)

0315 미디어 3채널(@0315news · @0315_zzal · @0315_pick)의 **오늘자** 게시물을 만든다.
발행은 GitHub Actions(publish.yml, 30분마다)가 한다: 시간이 됐고 링크가 다 채워진 게시물만 올라간다.
**채널마다 하루 2개(총 6개)**. 발행 시각(KST, config/channels.json 의 times):
| 채널 | 1회차(slot 1, 폴더 A·B·C) | 2회차(slot 2, 폴더 A2·B2·C2) |
| A 뉴스 | 12:00 | 18:00 |
| B 짤 | 12:20 | 18:30 |
| C 픽 | 12:40 | 19:00 |
post.json 에 "slot": 1 또는 2 를 넣는다. 1회차와 2회차는 주제·상품을 다르게(같은 날 분야는 같아도 됨).
매일 오전 9시 예약 작업이 혼자 만든다(파트너스 API 사용, 사용자 컴퓨터 불필요). 점심 게시물(12:00) 전에 6개 모두 push 를 끝낸다.

## 1. 오늘 분야 정하기
config/channels.json 의 weekly_plan 에서 오늘 요일 분야(생활용품/식품/소형가전/특이한 상품)를 고른다.
지난 게시물(docs/posts/*/*/post.json)과 상품이 겹치지 않게 한다.

## 2. 소재 찾기
- **금지 주제: 정치(선거·정당·정치인·정책 논쟁), 전쟁·무력 충돌·테러·군사.** 사건사고·재난 피해를 상품 판매로 잇지 않는다. (config/channels.json banned_topics)
- A(뉴스): 오늘·어제 실제 뉴스 중 오늘 분야 상품과 자연스럽게 이어지는 생활 정보 기사. WebSearch 로 2곳 이상 확인,
  모든 수치에 출처(언론사·날짜) 표기. 지어낸 수치 금지.
- B(짤): 같은 주제로 공감 투표 1장(질문 + 보기 3~4개, 마지막 보기에 상품 연결). 결과 수치 지어내지 않음.
  커뮤니티 글은 소재 참고만, 캡처 금지.
- C(픽): 같은 주제 상품 BEST3, 상품마다 1장 + 표지 + 구매방법 장. 품번은 지난 번호에 이어서 4자리.

## 3. 상품 고르기 + 파트너스 링크 (쿠팡 파트너스 API, 컴퓨터 필요 없음)
- requests/<날짜>.json 에 검색어를 적어 push → products.yml(GitHub Actions)이 API로 검색·대표사진 저장·채널별 링크 생성
  → catalog/<날짜>.json 커밋. 끝날 때까지 기다렸다가 git pull.
  형식: {"searches":[{"key":"A","keyword":"가습기","limit":8}, ...]}  (key = 그 상품을 쓸 채널, 링크 subId 가 채널별로 붙음)
  끝났는지 확인: gh api "repos/315tools/0315-media/actions/workflows/products.yml/runs?per_page=1" 의 status/conclusion.
- **검색 API 는 시간당 약 10회 제한** → 하루 검색어 8개 이하. 같은 상품을 여러 채널에 쓰면 채널마다 key 를 달리해 따로 검색하지 말고,
  필요하면 "urls":[{"key":"B","url":"https://www.coupang.com/vp/products/<번호>"}] 로 그 채널 링크만 추가 생성.
- catalog 의 affiliate_url 이 null 인 상품 = 판매자 제한(링크 불가) → 쓰지 않는다.
- 사진은 catalog 의 image(assets/products/<번호>.jpg, 쿠팡이 파트너스용으로 주는 대표 이미지)만 쓴다.
- 후보 중 가격·로켓배송·상품명(과장 없는 것)을 보고 고른다. 상품명은 짧게 다듬되 사실과 다르게 바꾸지 않는다.
- post.json 의 products[].affiliate_url 에 catalog 링크를 바로 넣는다(links/<날짜>.md 는 기록용으로 links.py make 후 그대로 커밋).

## 4. 만들기
- content/make_2026-10-22.py 를 복사해 content/make_<날짜>.py 로 만들고(write() 의 폴더 이름을 A·A2 처럼, post 에 "slot" 추가) 내용·상품·사진(img(상품번호))만 바꾼다. img() 는 assets/products/<번호>.jpg 를 읽음.
  디자인(CSS)·광고 표시(맨 위 광고 띠, 캡션 첫 줄 [광고] 문구, 첫 해시태그 #광고)는 그대로 유지.
- 실행: python3 content/make_<날짜>.py
- 렌더: python3 scripts/render.py docs/posts/<날짜>/{A,B,C,A2,B2,C2}  (make 후 반드시 여섯 개 모두)
- 링크 기록: python3 scripts/links.py make <날짜> (post.json 에 이미 들어간 링크가 그대로 적힘). 비어 있는 칸이 없어야 발행된다.
- 렌더된 jpg 몇 장을 직접 열어 겹침·잘림·오탈자 확인.

## 구매 안내 문구 (현재 방식)
- **프로필 링크만 안내한다.** "댓글에 '링크' 남기면 DM" 문구는 쓰지 않는다(자동 DM 아직 없음). C 의 구매방법 장도 "프로필 링크 → 품번 검색" 1가지로.
- 자동 DM 이 연결되면 이 항목을 바꾼다.
- **쿠팡 인플루언서 자동 DM 재신청 알림:** 10/22 신청 시 "참여 기준 미충족"으로 거절됨(팔로워 부족 추정). 사용자 결정: 팔로워가 쌓이면 다시 신청.
  reports/accounts.json(매주 월요일 check.yml 이 갱신)에서 어느 계정이든 팔로워 1,000 이상이면 보고 끝에
  "@계정 팔로워 N명 — 쿠팡 인플루언서 자동 DM 재신청해 볼까요?" 한 줄을 붙인다.

## 5. 올리기
git add -A; git commit; git pull --rebase; git push. (커밋 메시지 끝 Co-Authored-By 줄 유지)
미리보기: python3 scripts/preview.py <날짜> <출력.html> → Artifact 로 게시해 사용자에게 보여 준다.

## 6. 보고 (한국어 존댓말, 짧게)
오늘 주제, 채널별 상품, 발행 시각, 링크 비어 있는 상품(있으면 사용자가 채울 곳: links/<날짜>.md).
