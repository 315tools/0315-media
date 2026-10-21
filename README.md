# 0315 미디어 자동 발행

인스타 채널 3개(@0315news · @0315_zzal · @0315_pick)에 쿠팡 파트너스 게시물을 자동으로 올리는 저장소.

## 하루 흐름

1. **매일 아침, Claude 예약 작업**이 채널별 게시물을 만든다.
   - `docs/posts/<날짜>/<A|B|C>/` 에 이미지(01.jpg…)와 `post.json`(캡션, 상품 목록)
   - `links/<날짜>.md` 에 그날 넣을 상품 목록
2. **링크 넣기 (쿠팡 최종 승인 전까지만)**
   - GitHub에서 `links/<날짜>.md` 를 열고 연필(편집) → 각 상품의 `파트너스:` 뒤에 파트너스 링크 붙여넣기 → Commit
3. **GitHub Actions**(30분마다)가 발행 시간이 지났고 링크가 다 채워진 게시물을 인스타에 올리고, 프로필 링크 페이지를 갱신한다.

| 채널 | 기본 발행 시간 | 프로필 링크에 넣을 주소 |
| --- | --- | --- |
| A @0315news | 20:00 | `https://<아이디>.github.io/0315-media/news/` |
| B @0315_zzal | 21:00 | `https://<아이디>.github.io/0315-media/zzal/` |
| C @0315_pick | 21:30 | `https://<아이디>.github.io/0315-media/pick/` |

## 게시물 하나 멈추기 / 다시 올리기

`post.json` 의 `"status"` 를
- `"hold"` → 발행 안 함
- 지우거나 `"ready"` → 발행 대상
- 3번 실패하면 자동으로 멈춘다. `result.error` 확인 후 `"attempts"` 를 지우면 다시 시도.

## 처음 한 번 설정

1. **Settings → Pages**: Source `Deploy from a branch`, Branch `main` / 폴더 `/docs`
2. **Settings → Secrets and variables → Actions → New repository secret** (값은 채팅에 붙여넣지 말 것)

| 이름 | 내용 |
| --- | --- |
| `IG_TOKEN_NEWS` / `IG_USER_ID_NEWS` | @0315news 장기 토큰 / 인스타 사용자 ID |
| `IG_TOKEN_ZZAL` / `IG_USER_ID_ZZAL` | @0315_zzal |
| `IG_TOKEN_PICK` / `IG_USER_ID_PICK` | @0315_pick |
| `GH_PAT` | 토큰 자동 갱신용 (이 저장소 Secrets 쓰기 권한만 준 fine-grained 토큰) |
| `COUPANG_ACCESS_KEY` / `COUPANG_SECRET_KEY` | 쿠팡 최종 승인 후 |

3. 인스타 프로필 링크에 위 표의 주소를 넣는다.

## 파일

| 경로 | 역할 |
| --- | --- |
| `config/channels.json` | 채널 아이디, 발행 시간, subId, 대가성 문구 |
| `scripts/render.py` | `slides/*.html` → 1080×1350 JPEG |
| `scripts/links.py` | 링크 입력 파일 만들기(`make`) / post.json에 반영(`sync`) |
| `scripts/publish.py` | 인스타 발행 (`--dry-run` 으로 미리보기) |
| `scripts/linkpage.py` | 채널별 프로필 링크 페이지 |
| `scripts/refresh_tokens.py` | 인스타 토큰 매달 갱신 |
| `scripts/coupang.py` | 쿠팡 파트너스 API (승인 후) |

## 규칙

- 상품 게시물은 캡션 첫 줄, 이미지 위쪽 띠, 첫 해시태그 `#광고` 세 곳에 광고 표시.
- 짤은 직접 만든 것만. 커뮤니티 이미지·캡처 금지.
- 쿠팡 상품 사진은 약관 확인 전까지 쓰지 않음.
- 승인 전에 파트너스 사이트를 브라우저 자동화로 조작하지 않음.
- `docs/posts/2026-10-26/` 는 샘플(status: hold). 실제 운영 전에 지워도 됨.
