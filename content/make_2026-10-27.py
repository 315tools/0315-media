"""2026-10-27(화, 식품의 날) 게시물 6개 → docs/posts/2026-10-27/{A,B,C,A2,B2,C2}
점심: 김장 재료비 4.6%↓, 배추 12.5%↓·새우젓 37.9%↑ / 퇴근길: 올해 노지감귤 7.8%↑·당도↑, 내일 아침 서울 2도
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-10-27"
DL = "2026.10.27 (화)"
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


SHRIMP, CHILI, KIMCHI = "8416417558", "8072535485", "9432971346"
TANGE, JUICE, CHIP = "9225706227", "9780048111", "8735012408"
N_SHRIMP, N_CHILI, N_KIMCHI = "일월식품 강화도 참새우젓 추젓 2kg", "국산 청송 햇 고춧가루 1kg", "청원김치 포기김치 골드 5kg"
N_TANGE, N_JUICE, N_CHIP = "귤탐 당도선별 11Brix 감귤 2kg", "트레이더스 100% 착즙 제주감귤 주스 180ml×24", "미엘미 제주햇살품은 감귤칩"

# ═════════ A · 점심 12:00 — 김장 재료비 ═════════
SRC1 = "출처: 충청일보(10/26, aT 10/23 소매가 분석), 이투데이·연합뉴스(10/18)"
n = 6
a1 = [
    a_slide(1, n, """<div class="tag">물가 · 김장</div>
<h1>올해 김장 재료비<br><span class="hl">4.6% 내렸지만</span><br>새우젓은 껑충</h1>
<p class="lead">배추는 싸지고 젓갈은 비싸진<br>올해 김장 물가 정리</p>""", SRC1, DL),
    a_slide(2, n, """<h2>김장 재료비 (aT 소매가)</h2>
<div class="fig"><div><small>올해 (10/23)</small><strong>19.8만원</strong></div><div><small>지난해 같은 때</small><strong>20.8만원</strong></div></div>
<div class="box">배추 20포기·무 5개·고춧가루 2kg<br>깐마늘·새우젓·대파 기준 <b class="hl">9,548원↓</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>내린 것 · 오른 것</h2>
<div class="fig"><div><small>배추 1포기</small><strong>4,537원</strong></div><div><small>전년 대비</small><strong style="color:#1f6fd1">12.5%↓</strong></div></div>
<div class="fig"><div><small>새우젓 1kg</small><strong>20,863원</strong></div><div><small>전년 대비</small><strong style="color:#d7263d">37.9%↑</strong></div></div>
<p class="lead" style="font-size:32px">무 1.4%↓ · 깐마늘 3.5%↓ · 대파 13.8%↓ · 고춧가루 비슷</p>""", SRC1, DL),
    a_slide(4, n, """<h2>왜 이렇게 됐나</h2>
<ul class="chk"><li>가을배추 생산 122.2만t<br>전년보다 <span class="hl">19.3%</span> 많을 전망</li><li>새우젓 1~8월 생산<br>약 9,500t, <span class="hl">3.5%</span> 감소</li><li>배추값, 일주일 새 18.4% 하락<br>(10/16 → 10/23)</li></ul>""", SRC1, DL),
    a_slide(5, n, """<h2>김장 장보기 체크</h2>
<ul class="chk"><li>배추는 값 내려갈 때 미리 가격 비교</li><li>새우젓은 필요한 양만 계산</li><li>11/4~22 새우젓·액젓 할인 예정<br><span style="font-size:34px">(해수부, 대형마트·온라인 최대 50%)</span></li><li>11/9부터 김장 재료 할인 대책</li></ul>""", SRC1, DL),
    a_slide(6, n, f"""<h2>김장 <span class="hl">장바구니템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SHRIMP)}"><div>일월식품 강화도 추젓<span>참새우젓 2kg</span></div></li>
<li><b>2</b><img src="{img(CHILI)}"><div>국산 청송 햇 고춧가루<span>1kg · 김장용</span></div></li>
<li><b>3</b><img src="{img(KIMCHI)}"><div>청원김치 포기김치 골드<span>5kg · 김장 대신</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/27 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "김장 재료비 4.6%↓·새우젓 37.9%↑",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 올해 김장 재료비 4.6% 내렸지만, 새우젓은 껑충

· 10/23 aT 소매가 기준 김장 재료비 19만8,204원 (지난해 같은 때 20만7,752원)
· 배추 1포기 4,537원, 전년보다 12.5%↓ — 일주일 새 18.4% 하락
· 새우젓 1kg 2만863원, 전년보다 37.9%↑
· 무 1.4%↓, 깐마늘 3.5%↓, 대파 13.8%↓, 국산 고춧가루는 비슷
· 가을배추 생산 19.3% 증가 전망, 새우젓 1~8월 생산 3.5% 감소
· 11/4~22 대형마트·온라인 새우젓·멸치액젓 최대 50% 할인 예정(해수부)

※ 배추 20포기·무 5개·고춧가루 2kg·깐마늘 1.3kg·새우젓 800g·대파 1kg 기준, 액젓·생강·쪽파·소금 제외

🔗 김장 장바구니템 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리템은 @0315_pick

출처: 충청일보(10/26, aT KAMIS 10/23 소매가 분석), 이투데이·연합뉴스(10/18)

#광고 #생활뉴스 #김장 #김장물가 #새우젓 #배추값 #장보기 #물가""",
    "products": [prod(1, SHRIMP, N_SHRIMP, "A"), prod(2, CHILI, N_CHILI, "A"), prod(3, KIMCHI, N_KIMCHI, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 노지감귤 ═════════
SRC2 = "출처: 쿡앤셰프·뉴스1(10/23), 기상청 예보 인용 톱스타뉴스(10/26)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">먹거리 · 제철</div>
<h1>올해 귤,<br><span class="hl">더 많이·더 달게</span><br>나옵니다</h1>
<p class="lead">제주 노지감귤 생산 7.8% 증가 전망<br>당도도 지난해보다 높아요.</p>""", SRC2, DL),
    a_slide(2, n, """<h2>올해 노지감귤 전망</h2>
<div class="fig"><div><small>예상 생산량</small><strong>44.3만t</strong></div><div><small>지난해 대비</small><strong>7.8%↑</strong></div></div>
<div class="box">평균 당도 <b class="hl">8.5브릭스</b><br>지난해보다 1.1, 5년 평균보다 1.4 높음</div>""", "출처: 쿡앤셰프(10/23, 제주농산물수급관리센터)", DL),
    a_slide(3, n, """<h2>초반 시세는?</h2>
<div class="fig"><div><small>평균 도매가 5kg</small><strong>9,733원</strong></div><div><small>지난해 대비</small><strong>7%↓</strong></div></div>
<p class="lead" style="font-size:36px">출하 물량이 지난해의 두 배 이상<br>출하 초기부터 값이 내려갔어요.</p>""", "출처: 뉴스1(10/23)", DL),
    a_slide(4, n, """<h2>귤 맛있게 두는 법</h2>
<ul class="chk"><li>상자째 두지 말고 한 번 펼쳐 확인</li><li>무른 귤은 바로 골라내기</li><li>서로 눌리지 않게 넓게 두기</li><li>내일 아침 서울 <span class="hl">2도</span>, 베란다는 얼지 않게</li></ul>""", "출처: 기상청 예보 인용 톱스타뉴스(10/26)", DL),
    a_slide(5, n, f"""<h2>귤 철 <span class="hl">먹거리템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(TANGE)}"><div>귤탐 당도선별 감귤<span>11Brix 선별 · 2kg</span></div></li>
<li><b>2</b><img src="{img(JUICE)}"><div>100% 착즙 제주감귤 주스<span>180ml × 24개</span></div></li>
<li><b>3</b><img src="{img(CHIP)}"><div>미엘미 제주 감귤칩<span>말린 감귤 간식</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/27 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "올해 노지감귤 7.8%↑·당도↑",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 올해 귤, 더 많이·더 달게 나옵니다

· 올해 제주 노지감귤 예상 생산 44만3,300t, 지난해보다 7.8%↑ (제주농산물수급관리센터)
· 평균 당도 8.5브릭스 — 지난해보다 1.1, 5년 평균보다 1.4 높아
· 출하 초기 평균 도매가 5kg 9,733원, 지난해보다 7%↓ (출하량 두 배 이상)
· 내일(28일) 아침 서울 2도, 전국 -2~7℃ 예보 — 베란다 보관은 얼지 않게

🔗 귤 철 먹거리템 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리템은 @0315_pick

출처: 쿡앤셰프(10/23), 뉴스1(10/23), 기상청 예보 인용 톱스타뉴스(10/26)

#광고 #생활뉴스 #감귤 #제주감귤 #노지감귤 #제철과일 #귤 #겨울간식""",
    "products": [prod(1, TANGE, N_TANGE, "A"), prod(2, JUICE, N_JUICE, "A"), prod(3, CHIP, N_CHIP, "A")],
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


write(DATE, "B", [poll("올해 김장,<br>우리 집은 어떻게? 🥬", "배추값 12.5%↓ · 새우젓 37.9%↑ (aT 10/23)",
                       [("온 가족 출동", "주말 하루 통째로"), ("엄마 김치 얻어먹기", "통 들고 대기"),
                        ("절임배추로 반만", "속만 내가 버무림"), ("포기김치 사 먹기", "5kg 한 박스면 끝")], KIMCHI)], {
    "title": "올해 김장 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 올해 김장, 우리 집은 어떻게? 🥬
댓글에 번호로 투표해주세요!

1️⃣ 온 가족 출동
2️⃣ 엄마 김치 얻어먹기
3️⃣ 절임배추로 반만
4️⃣ 포기김치 사 먹기

🔗 4번 포기김치 5kg 링크는 프로필에
👥 김장날만 되면 사라지는 친구 태그

#광고 #투표 #공감 #김장 #김치 #포기김치 #자취생""",
    "products": [prod(1, KIMCHI, N_KIMCHI, "B")],
})

write(DATE, "B2", [poll("귤 한 상자 오면<br>나는 어떤 타입? 🍊", "올해 노지감귤 당도 8.5브릭스, 지난해보다 ↑",
                        [("앉은자리 10개", "손끝 노래질 때까지"), ("하루 2개 아껴 먹기", "상자 끝까지 계획적"),
                         ("껍질 까서 나눠주기", "가족 담당 귤 까기"), ("당도선별 귤만 산다", "신 귤은 못 참아")], TANGE)], {
    "title": "귤 먹는 타입 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 귤 한 상자 오면 나는 어떤 타입? 🍊
댓글에 번호로 투표해주세요!

1️⃣ 앉은자리 10개
2️⃣ 하루 2개 아껴 먹기
3️⃣ 껍질 까서 나눠주기
4️⃣ 당도선별 귤만 산다

🔗 4번 당도선별 감귤 링크는 프로필에
👥 귤 앉은자리에서 다 먹는 친구 태그

#광고 #투표 #공감 #귤 #감귤 #제철과일 #겨울간식""",
    "products": [prod(1, TANGE, N_TANGE, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/27 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("배추 12.5%↓ 새우젓 37.9%↑", "올해 김장", "장바구니템", "BEST3", [SHRIMP, CHILI, KIMCHI]),
    c_prod(1, "0028", SHRIMP, "일월식품<br>강화도 참새우젓 추젓", ["김장용 추젓 2kg", "강화도 참새우젓", "필요한 양 계산해서 준비"],
           ["💰 2만원대"]),
    c_prod(2, "0029", CHILI, "국산 청송<br>햇 고춧가루", ["2026년 햇 고춧가루", "김장용 1kg", "국산 청송 고추"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0030", KIMCHI, "청원김치<br>포기김치 골드", ["김장 대신 포기김치 5kg", "로켓프레시 신선 배송", "한 박스로 겨울 준비"],
           ["💰 2만원대", "🚀 로켓프레시"]),
    c_howto("0028~0030"),
], {
    "title": "김장 장바구니템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

배추 12.5%↓ 새우젓 37.9%↑ 🥬 올해 김장 장바구니템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 일월식품 강화도 참새우젓 추젓 2kg 💛 품번 0028
김장용 추젓. 새우젓은 필요한 양만 계산해서 준비하기.

2. 국산 청송 햇 고춧가루 1kg 💛 품번 0029
2026년 햇 고춧가루, 김장용.

3. 청원김치 포기김치 골드 5kg 💛 품번 0030
직접 담그기 어렵다면 포기김치 한 박스로.

※ {NOTE}

#광고 #쿠팡추천템 #식품 #김장 #새우젓 #고춧가루 #포기김치 #자취템""",
    "products": [prod(1, SHRIMP, N_SHRIMP, "C", "0028"), prod(2, CHILI, N_CHILI, "C", "0029"), prod(3, KIMCHI, N_KIMCHI, "C", "0030")],
})

write(DATE, "C2", [
    c_cover("올해 귤 당도 8.5브릭스", "귤 철 왔다", "감귤템", "BEST3", [TANGE, JUICE, CHIP]),
    c_prod(1, "0031", TANGE, "귤탐<br>당도선별 감귤", ["11Brix 당도선별 감귤", "로열과 2kg", "로켓프레시 신선 배송"],
           ["💰 2만원대", "🚀 로켓프레시"]),
    c_prod(2, "0032", JUICE, "트레이더스<br>100% 착즙 제주감귤 주스", ["100% 착즙 제주감귤 주스", "180ml × 24개 (4.32L)", "한 병씩 들고 다니기"],
           ["💰 2만원대"]),
    c_prod(3, "0033", CHIP, "미엘미<br>제주햇살품은 감귤칩", ["말린 제주 감귤칩", "사무실·출퇴근 간식", "귤 껍질 안 까도 되는 귤맛"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0031~0033"),
], {
    "title": "감귤템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

올해 귤 당도 8.5브릭스 🍊 귤 철 왔다! 감귤템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 귤탐 당도선별 11Brix 감귤 2kg 💛 품번 0031
당도선별 로열과, 로켓프레시 배송.

2. 트레이더스 100% 착즙 제주감귤 주스 💛 품번 0032
180ml 24개, 한 병씩 들고 다니기 좋아요.

3. 미엘미 제주햇살품은 감귤칩 💛 품번 0033
껍질 안 까도 되는 말린 감귤 간식.

※ {NOTE}

#광고 #쿠팡추천템 #식품 #감귤 #제주감귤 #착즙주스 #감귤칩 #겨울간식""",
    "products": [prod(1, TANGE, N_TANGE, "C", "0031"), prod(2, JUICE, N_JUICE, "C", "0032"), prod(3, CHIP, N_CHIP, "C", "0033")],
})
print("ok")
