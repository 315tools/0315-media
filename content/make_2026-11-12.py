"""2026-11-12(목, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-12/{A,B,C,A2,B2,C2}
점심: 수도권 미세먼지 나쁨·일교차 15도 → 먼지 잡는 생활템 / 퇴근길: 주말 전국 비 → 습한 주말 욕실·창틀 청소템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-12"
DL = "2026.11.12 (목)"
cat = json.loads((ROOT / "catalog" / f"{DATE}.json").read_text(encoding="utf-8"))


def link(pid, key):
    """catalog 에서 채널(key)용 파트너스 링크 찾기"""
    url = f"https://www.coupang.com/vp/products/{pid}"
    for u in cat.get("urls", []):
        if u["url"] == url and u["key"] == key and u["affiliate_url"]:
            return u["affiliate_url"]
    for s in cat["searches"].values():
        if s["key"] != key:
            continue
        for it in s["items"]:
            if str(it["productId"]) == str(pid) and it["affiliate_url"]:
                return it["affiliate_url"]
    raise SystemExit(f"링크 없음: {pid} {key}")


def prod(no, pid, name, key, code=None):
    d = {"no": no, "name": name, "coupang_url": f"https://www.coupang.com/vp/products/{pid}", "affiliate_url": link(pid, key)}
    if code:
        d["code"] = code
    return d



MASK, WIPE, DUSTER = "9138672512", "6943521716", "8039804672"
MOLD, BRUSH, DRAIN = "7506301128", "8151323896", "7196702728"
N_MASK = "닥터피앤비 국산 KF94 대형 보건용 마스크 100매"
N_WIPE = "크린액티브 대용량 정전기 청소포 대형 310매"
N_DUSTER = "크린메이트 극세사 먼지떨이"
N_MOLD = "홈스타 바르는 곰팡이 싹 세정제"
N_BRUSH = "테일스타 창문 틈새·창틀 청소 브러시 2세트"
N_DRAIN = "펑크린 울트라겔 배수관 세정제"

# ═════════ A · 점심 12:00 — 수도권 미세먼지 나쁨·일교차 15도 ═════════
SRC1 = "출처: 데일리한국·머니투데이(11/12) — 기상청·환경부 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활용품 · 오늘</div>
<h1>오늘 수도권<br>미세먼지 <span class="hl">'나쁨'</span></h1>
<p class="lead">낮밤 기온 차 15도 안팎<br>외출·청소 체크</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(12일) <span class="hl">미세먼지</span></h2>
<div class="box"><b class="hl">'나쁨'</b><br>서울·경기 남부 등</div>
<div class="box"><b class="hl">새벽~아침 한때 '나쁨'</b><br>인천·대전·충남 등</div>
<div class="box">그 밖의 지역 '좋음'~'보통'</div>""", SRC1, DL),
    a_slide(3, n, """<h2>오늘 <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>-2~8도</strong></div><div><small>전국 낮 최고</small><strong>14~21도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>5도</strong></div><div><small>서울 낮</small><strong>15도</strong></div></div>
<div class="box">낮밤 기온 차 <b class="hl">15도 안팎</b><br>오전 내륙 곳곳 짙은 안개</div>""", SRC1, DL),
    a_slide(4, n, """<h2>먼지 많은 날 <span class="hl">생활 수칙</span></h2>
<ul class="chk"><li>외출할 땐 <span class="hl">보건용 마스크</span></li><li>집에 오면 손·얼굴 씻기</li><li>바닥 먼지는 <span class="hl">마른 청소포</span>로 먼저</li><li>겉옷은 현관에서 <span class="hl">털고</span> 들어오기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>먼지 잡는 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(MASK)}"><div>국산 KF94 대형 마스크<span>100매 · 10매씩 포장</span></div></li>
<li><b>2</b><img src="{img(WIPE)}"><div>정전기 청소포 대형<span>310매 대용량</span></div></li>
<li><b>3</b><img src="{img(DUSTER)}"><div>극세사 먼지떨이<span>선반·가구 위 먼지</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/12 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "수도권 미세먼지 나쁨·일교차 15도",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘 서울·경기 남부 등 미세먼지 '나쁨' 😷 낮밤 기온 차 15도 안팎

· 12일(목) 미세먼지: 서울·경기 남부 등 '나쁨', 인천·대전·충남은 새벽~아침 한때 '나쁨'
· 그 밖의 지역 '좋음'~'보통'
· 전국 아침 최저 -2~8도, 낮 최고 14~21도
· 서울 아침 5도, 낮 15도 — 일교차 15도 안팎
· 오전 내륙 곳곳 짙은 안개, 오후부터 서쪽 지역 차차 흐려짐

✔ 외출할 땐 보건용 마스크
✔ 집에 오면 손·얼굴 씻기, 겉옷은 현관에서 털기
✔ 바닥 먼지는 마른 청소포로 먼저

🔗 먼지 잡는 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 데일리한국·머니투데이(2026.11.12) — 기상청·환경부 예보

#광고 #생활뉴스 #미세먼지 #날씨 #일교차 #KF94 #청소""",
    "products": [prod(1, MASK, N_MASK, "A"), prod(2, WIPE, N_WIPE, "A"), prod(3, DUSTER, N_DUSTER, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 주말 전국 비 ═════════
SRC2 = "출처: 공감신문·이코노미톡뉴스(11/12) — 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활용품 · 주말</div>
<h1>이번 주말<br><span class="hl">전국에 비</span></h1>
<p class="lead">내일(13일) 오후 남부부터<br>토요일 오전 전국 대부분</p>""", SRC2, DL),
    a_slide(2, n, """<h2>비 <span class="hl">언제부터?</span></h2>
<ul class="chk"><li>13일(금) 늦은 오후 <span class="hl">전남 해안·제주</span></li><li>13일 밤 충청·전라·경상 서부</li><li>14일(토) 새벽 <span class="hl">수도권</span>·강원 남부</li><li>14일 오전 <span class="hl">전국 대부분</span></li></ul>""", SRC2, DL),
    a_slide(3, n, """<h2>예상 <span class="hl">강수량</span> (13~14일)</h2>
<div class="fig"><div><small>서울·인천·경기</small><strong>5~20mm</strong></div><div><small>충청·전북·대구경북</small><strong>5~30mm</strong></div></div>
<div class="fig"><div><small>광주전남·부울경</small><strong>10~40mm</strong></div><div><small>제주도</small><strong>10~60mm</strong></div></div>
<div class="box">중부는 14일 밤 대부분 그쳐요</div>""", SRC2, DL),
    a_slide(4, n, """<h2>비 온 뒤 <span class="hl">다음 주</span></h2>
<div class="box"><b class="hl">18~19일</b><br>찬 공기 내려와 기온 큰 폭 하락</div>
<ul class="chk"><li>습한 주말, 욕실 <span class="hl">환기</span> 자주</li><li>창틀 고인 빗물·먼지 <span class="hl">닦기</span></li><li>추워지기 전 <span class="hl">물때·곰팡이</span> 정리</li></ul>""", "출처: 이코노미톡뉴스(11/12) — 기상청 중기예보", DL),
    a_slide(5, n, f"""<h2>비 오는 주말 <span class="hl">청소템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(MOLD)}"><div>바르는 곰팡이 세정제<span>실리콘·타일 줄눈용</span></div></li>
<li><b>2</b><img src="{img(BRUSH)}"><div>창틀 틈새 청소 브러시<span>2세트 구성</span></div></li>
<li><b>3</b><img src="{img(DRAIN)}"><div>울트라겔 배수관 세정제<span>젤 타입 · 냄새·막힘</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/12 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "주말 전국 비·다음 주 기온 뚝",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 이번 주말 전국에 비 ☔ 비 그친 뒤 다음 주엔 기온 뚝

· 13일(금) 늦은 오후 전남 해안·제주부터 비 → 밤 충청·전라·경상 서부
· 14일(토) 새벽 수도권·강원 남부, 오전엔 전국 대부분
· 중부지방은 14일 밤 대부분 그침
· 예상 강수량(13~14일): 서울·인천·경기 5~20mm, 충청·전북·대구경북 5~30mm, 광주전남·부산울산경남 10~40mm, 제주도 10~60mm
· 14일 아침 6~14도, 낮 12~18도
· 18~19일 찬 공기 내려와 기온 큰 폭 하락 예상

✔ 습한 주말엔 욕실 환기 자주
✔ 창틀에 고인 빗물·먼지 닦기
✔ 추워지기 전 물때·곰팡이 정리

🔗 비 오는 주말 청소템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 공감신문·이코노미톡뉴스(2026.11.12) — 기상청 예보

#광고 #생활뉴스 #주말날씨 #비소식 #대청소 #곰팡이제거 #생활용품""",
    "products": [prod(1, MOLD, N_MOLD, "A"), prod(2, BRUSH, N_BRUSH, "A"), prod(3, DRAIN, N_DRAIN, "A")],
})

# ═════════ B · 투표 ═════════
def poll(q, sub, opts, last_photo):
    rows = ""
    for i, (t, e) in enumerate(opts, 1):
        ph = f'<div class="ph"><img src="{img(last_photo)}"></div>' if i == len(opts) else ""
        rows += f'<div class="o"><b>{i}</b><span>{t}<em>{e}</em></span>{ph}</div>\n'
    return page(B_CSS, f"""<div class="ad">{AD}</div>
<div class="q"><small>📊 오늘의 투표</small><h1>{q}</h1><p>{sub}</p></div>
<div class="opts">
{rows}</div>
<div class="foot"><span>👇 댓글에 번호로 투표</span><span>@0315_zzal</span></div>""")





write(DATE, "B", [poll("미세먼지 '나쁨'인 날,<br>나는 어떤 타입? 😷", "12일 서울·경기 남부 등 미세먼지 '나쁨' (기상청·환경부 예보)",
                       [("신경 안 쓰고 그냥 외출", "눈 침침해도 모름"), ("창문 꽁꽁 닫고 집콕", "환기는 내일의 나에게"),
                        ("집에 오자마자 샤워", "먼지 털고 씻기부터"), ("KF94 마스크 필수", "가방에 늘 여분")], MASK)], {
    "title": "미세먼지 나쁨 타입 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 미세먼지 '나쁨'인 날, 나는 어떤 타입? 😷
댓글에 번호로 투표해주세요!

1️⃣ 신경 안 쓰고 그냥 외출
2️⃣ 창문 꽁꽁 닫고 집콕
3️⃣ 집에 오자마자 샤워
4️⃣ KF94 마스크 필수

※ 12일(목) 서울·경기 남부 등 미세먼지 '나쁨', 낮밤 기온 차 15도 안팎 (기상청·환경부 예보, 데일리한국·머니투데이 11/12)

🔗 4번 닥터피앤비 KF94 대형 마스크 링크는 프로필에
👥 마스크 맨날 까먹는 친구 태그

#광고 #투표 #공감 #미세먼지 #KF94 #마스크""",
    "products": [prod(1, MASK, N_MASK, "B")],
})

write(DATE, "B2", [poll("비 오는 주말,<br>집에서 뭐 할 거예요? ☔", "13일 밤~14일 전국 비 · 서울·경기 5~20mm",
                        [("이불 밖은 위험해", "하루 종일 누워 있기"), ("배달 + 정주행", "주말은 원래 이거지"),
                         ("밀린 잠 몰아 자기", "알람 끄고 푹"), ("욕실·창틀 대청소", "곰팡이 싹 정리")], MOLD)], {
    "title": "비 오는 주말 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 비 오는 주말, 집에서 뭐 할 거예요? ☔
댓글에 번호로 투표해주세요!

1️⃣ 이불 밖은 위험해
2️⃣ 배달 + 정주행
3️⃣ 밀린 잠 몰아 자기
4️⃣ 욕실·창틀 대청소

※ 13일(금) 밤~14일(토) 전국 비, 서울·인천·경기 예상 강수량 5~20mm (기상청 예보, 공감신문·이코노미톡뉴스 11/12)

🔗 4번 홈스타 바르는 곰팡이 세정제 링크는 프로필에
👥 주말에 같이 대청소할 사람 태그

#광고 #투표 #공감 #주말 #비오는날 #대청소""",
    "products": [prod(1, MOLD, N_MOLD, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/12 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


def c_cover(hook, l1, l2, l3, pids):
    return page(C_CSS, f"""<div class="ad">{AD}</div>
<div class="hook"><span>{hook}</span></div>
<div class="big"><div style="font-size:140px">{l1}</div><div class="y" style="font-size:160px">{l2}</div><div style="font-size:190px">{l3}</div></div>
<div class="trio">{''.join(f'<img src="{img(p)}">' for p in pids)}</div>{c_foot()}""")


def c_howto(codes):
    return page(C_CSS, f"""<div class="ad">{AD}</div>
<div class="howto"><h2>구매 <span class="y">방법</span></h2>
<div class="step"><b>1</b><p>프로필 링크 클릭<small>@0315_pick 프로필 맨 위 링크</small></p></div>
<div class="step"><b>2</b><p>품번 찾기<small>품번 {codes} 바로 찾기</small></p></div>
<div class="step"><b>✓</b><p>저장해두고 살 때 꺼내보기<small>{NOTE}</small></p></div></div>{c_foot("")}""")





write(DATE, "C", [
    c_cover("오늘 수도권 미세먼지 '나쁨'", "먼지 잡는", "생활템", "BEST3", [MASK, WIPE, DUSTER]),
    c_prod(1, "0124", MASK, "국산 KF94<br>대형 마스크", ["보건용 KF94 대형", "100매 · 10매씩 포장", "국산"],
           ["💰 1만4천원대", "🚚 무료배송"]),
    c_prod(2, "0125", WIPE, "정전기 청소포<br>대형 310매", ["마른 바닥 먼지·머리카락", "대형 사이즈", "310매 대용량"],
           ["💰 1만3천원대", "🚀 로켓배송"]),
    c_prod(3, "0126", DUSTER, "극세사<br>먼지떨이", ["극세사 소재", "선반·가구 위 먼지", "가볍게 쓱"],
           ["💰 1만원대", "🚚 무료배송"]),
    c_howto("0124~0126"),
], {
    "title": "먼지 잡는 생활템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

오늘 수도권 미세먼지 '나쁨' 😷 먼지 잡는 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 닥터피앤비 국산 KF94 대형 보건용 마스크 100매 💛 품번 0124
보건용 KF94 대형, 10매씩 나눠 포장된 100매.

2. 크린액티브 대용량 정전기 청소포 대형 310매 💛 품번 0125
마른 바닥 먼지·머리카락을 먼저 잡는 정전기 청소포, 대형 310매.

3. 크린메이트 극세사 먼지떨이 💛 품번 0126
선반·가구 위 먼지를 가볍게 터는 극세사 먼지떨이.

✔ 미세먼지 '나쁨'인 날은 외출할 때 보건용 마스크

※ 미세먼지: 기상청·환경부 예보(데일리한국·머니투데이 11/12)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #미세먼지 #KF94마스크 #청소포 #먼지떨이""",
    "products": [prod(1, MASK, N_MASK, "C", "0124"), prod(2, WIPE, N_WIPE, "C", "0125"), prod(3, DUSTER, N_DUSTER, "C", "0126")],
})

write(DATE, "C2", [
    c_cover("이번 주말 전국 비 ☔", "비 오는 주말", "청소템", "BEST3", [MOLD, BRUSH, DRAIN]),
    c_prod(1, "0127", MOLD, "바르는<br>곰팡이 세정제", ["짜서 바르는 튜브형", "실리콘·타일 줄눈", "욕실 곰팡이 청소"],
           ["💰 3천원대", "🚀 로켓배송"]),
    c_prod(2, "0128", BRUSH, "창틀 틈새<br>청소 브러시", ["창문 틈새·창틀 전용", "브러시 2세트", "고인 먼지 쓱"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_prod(3, "0129", DRAIN, "울트라겔<br>배수관 세정제", ["젤 타입 배수관 세정제", "막힘·냄새 관리", "세면대·싱크대"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_howto("0127~0129"),
], {
    "title": "비 오는 주말 청소템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

이번 주말 전국 비 ☔ 비 오는 주말 청소템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 홈스타 바르는 곰팡이 싹 세정제 💛 품번 0127
짜서 바르는 튜브형, 욕실 실리콘·타일 줄눈 곰팡이 청소용.

2. 테일스타 창문 틈새·창틀 청소 브러시 2세트 💛 품번 0128
창문 틈새·창틀에 고인 먼지를 긁어내는 브러시 2세트.

3. 펑크린 울트라겔 배수관 세정제 💛 품번 0129
젤 타입 배수관 세정제, 세면대·싱크대 막힘·냄새 관리.

✔ 세정제는 환기하면서, 제품 사용법대로 쓰세요

※ 날씨: 기상청 예보(공감신문·이코노미톡뉴스 11/12)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #대청소 #곰팡이제거 #창틀청소 #배수구청소""",
    "products": [prod(1, MOLD, N_MOLD, "C", "0127"), prod(2, BRUSH, N_BRUSH, "C", "0128"), prod(3, DRAIN, N_DRAIN, "C", "0129")],
})
print("ok")
