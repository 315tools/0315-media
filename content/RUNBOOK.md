# 매일 콘텐츠 제작 순서 (예약 작업용)

0315 미디어 3채널(@0315news · @0315_zzal · @0315_pick)의 **오늘자** 게시물을 만든다.
발행은 GitHub Actions(publish.yml, 30분마다)가 한다: 시간이 됐고 링크가 다 채워진 게시물만 올라간다.
**채널마다 하루 2개(총 6개)**. 발행 시각(KST, config/channels.json 의 times):
| 채널 | 1회차(slot 1, 폴더 A·B·C) | 2회차(slot 2, 폴더 A2·B2·C2) |
| A 뉴스 | 08:00 | 20:00 |
| B 짤 | 12:30 | 21:00 |
| C 픽 | 12:00 | 21:30 |
post.json 에 "slot": 1 또는 2 를 넣는다. 1회차와 2회차는 주제·상품을 다르게(같은 날 분야는 같아도 됨).
1회차 시각이 이미 지난 뒤에 만들면 그 게시물은 만들자마자 올라가므로, 아침 9시 전에 끝내는 것이 좋다.

## 1. 오늘 분야 정하기
config/channels.json 의 weekly_plan 에서 오늘 요일 분야(생활용품/식품/소형가전/특이한 상품)를 고른다.
지난 게시물(docs/posts/*/*/post.json)과 상품이 겹치지 않게 한다.

## 2. 소재 찾기
- A(뉴스): 오늘·어제 실제 뉴스 중 오늘 분야 상품과 자연스럽게 이어지는 생활 정보 기사. WebSearch 로 2곳 이상 확인,
  모든 수치에 출처(언론사·날짜) 표기. 지어낸 수치 금지.
- B(짤): 같은 주제로 공감 투표 1장(질문 + 보기 3~4개, 마지막 보기에 상품 연결). 결과 수치 지어내지 않음.
  커뮤니티 글은 소재 참고만, 캡처 금지.
- C(픽): 같은 주제 상품 BEST3, 상품마다 1장 + 표지 + 구매방법 장. 품번은 지난 번호에 이어서 4자리.

## 3. 상품 고르기 + 파트너스 링크 (사용자 크롬, Claude in Chrome)
- 쿠팡 파트너스 상품 검색: https://partners.coupang.com/#affiliate/ws/link/0/<검색어>
  판매량 많은 것 중 가격·후기 무난한 것. 상품 위에 마우스 → '링크 생성' → 단축 URL(link.coupang.com/a/...) 복사.
- **링크 생성이 막힌 상품(판매자 제한)은 바로 다른 상품으로 교체.**
- 상품 번호(coupang.com/vp/products/<번호>) 페이지의 og:image 주소를 config/product_images.json 에 추가
  → push 하면 images.yml 이 assets/products/<번호>.jpg 로 받아 커밋 → git pull.
- 크롬을 쓸 수 없으면: 상품 후보만 정하고 링크 칸을 비워 둔 채 진행, 마지막에 사용자에게 링크 입력 요청.

## 4. 만들기
- content/make_2026-10-22.py 를 복사해 content/make_<날짜>.py 로 만들고(write() 의 폴더 이름을 A·A2 처럼, post 에 "slot" 추가) 내용·상품·사진(img(상품번호))만 바꾼다.
  디자인(CSS)·광고 표시(맨 위 광고 띠, 캡션 첫 줄 [광고] 문구, 첫 해시태그 #광고)는 그대로 유지.
- 실행: python3 content/make_<날짜>.py
- 렌더: python3 scripts/render.py docs/posts/<날짜>/{A,B,C,A2,B2,C2}  (make 후 반드시 여섯 개 모두)
- 링크 파일: python3 scripts/links.py make <날짜> → links/<날짜>.md 의 '파트너스:' 칸 채우기 (항목 이름은 A-1, A2-1 형식) → python3 scripts/links.py sync
- 렌더된 jpg 몇 장을 직접 열어 겹침·잘림·오탈자 확인.

## 5. 올리기
git add -A; git commit; git pull --rebase; git push. (커밋 메시지 끝 Co-Authored-By 줄 유지)
미리보기: python3 scripts/preview.py <날짜> <출력.html> → Artifact 로 게시해 사용자에게 보여 준다.

## 6. 보고 (한국어 존댓말, 짧게)
오늘 주제, 채널별 상품, 발행 시각, 링크 비어 있는 상품(있으면 사용자가 채울 곳: links/<날짜>.md).
