"""2026-11-03(화, 식품의 날) 게시물 6개 → docs/posts/2026-11-02/{A,B,C,A2,B2,C2}
점심: 10월 소비자물가(채소 11.2%↓·외식 2.9%↑)·제철 채소 / 퇴근길: 일교차 15도·5일 비·따뜻한 차
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-03"
DL = "2026.11.03 (화)"
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





CAR, CAB, RAD = "9683692850", "9429896552", "9786650353"
YUJA, GING, JUJU = "2528304", "9392103490", "5191057386"
N_CAR, N_CAB, N_RAD = "사계농산 국내산 흙당근 상 5kg", "국내산 아삭한 양배추 특품 2kg 3개", "국내산 햇 다발무 가을무 5kg 내외(무청 포함)"
N_YUJA, N_GING, N_JUJU = "꽃샘 꿀유자차 S", "선비비책 100% 국산 진짜 생강청", "청년농원 대추차 삼각티백 50개입"

# ═════════ A · 점심 12:00 — 10월 소비자물가 ═════════
SRC1 = "출처: 세계일보·서울신문(11/3), 국가데이터처 10월 소비자물가동향"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">물가 · 오늘 발표</div>
<h1>10월 물가 2.8%↑<br><span class="hl">채소는 11.2%↓</span><br>외식은 2.9%↑</h1>
<p class="lead">가공식품 상승률<br>11개월 만에 최대</p>""", SRC1, DL),
    a_slide(2, n, """<h2>숫자로 보는 10월 장바구니</h2>
<div class="fig"><div><small>채소류</small><strong>11.2%↓</strong></div><div><small>농산물 전체</small><strong>7.5%↓</strong></div></div>
<div class="fig"><div><small>가공식품</small><strong>2.9%↑</strong></div><div><small>외식</small><strong>2.9%↑</strong></div></div>
<div class="box">작년 같은 달 대비 · <b class="hl">신선채소 11.3%↓</b><br>신선과실 8.6%↓</div>""", SRC1, DL),
    a_slide(3, n, """<h2>오른 것 · 내린 것</h2>
<ul class="chk"><li>채소는 생육 좋아 <span class="hl">가격 하락</span></li><li>가공식품 2.9%↑ (9월 2.1%)</li><li>외식 2.9%↑ — 2월 이후 최고</li><li>축산물 4.8%↑ · 수산물 5.4%↑</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>이번 주 <span class="hl">장보기</span> 팁</h2>
<ul class="chk"><li>값 내린 <span class="hl">제철 채소</span> 위주로</li><li>당근·양배추·무로 반찬 돌려 막기</li><li>가공식품은 단가 비교 후 담기</li><li>외식 대신 도시락 한 번</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>값 내린 <span class="hl">제철 채소</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(CAR)}"><div>사계농산 국내산 흙당근<span>상품 · 5kg</span></div></li>
<li><b>2</b><img src="{img(CAB)}"><div>국내산 양배추 특품<span>2kg · 3개</span></div></li>
<li><b>3</b><img src="{img(RAD)}"><div>국내산 햇 다발무<span>가을무 · 5kg 내외 · 무청 포함</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/3 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "10월 물가 2.8%↑·채소 11.2%↓",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 10월 소비자물가 2.8%↑ — 채소는 11.2% 내리고, 외식은 2.9% 올라 🥕

· 10월 소비자물가 작년 같은 달보다 2.8% 상승 (국가데이터처, 11/3 발표)
· 농산물 7.5%↓, 채소류 11.2%↓ — 생육 여건이 좋아 가격 하락
· 가공식품 2.9%↑ — 지난해 11월 이후 11개월 만에 가장 큰 상승
· 외식 2.9%↑ — 올해 2월 이후 최고
· 축산물 4.8%↑, 수산물 5.4%↑

✔ 이번 주 장보기는 값 내린 제철 채소 위주로, 가공식품은 단가 비교 후 담기

🔗 값 내린 제철 채소 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 세계일보·서울신문(11/3) — 국가데이터처 2026년 10월 소비자물가동향

#광고 #생활뉴스 #소비자물가 #장보기 #제철채소 #당근 #양배추 #가을무""",
    "products": [prod(1, CAR, N_CAR, "A"), prod(2, CAB, N_CAB, "A"), prod(3, RAD, N_RAD, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 일교차·비 소식 ═════════
SRC2 = "출처: 세계일보·톱스타뉴스(11/3), 기상청 예보"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 이번 주</div>
<h1>일교차 <span class="hl">15도</span><br>목요일엔<br>전국 비</h1>
<p class="lead">오늘 아침 0~9도 · 낮 15~19도<br>5일 비 · 6일 낮 9~17도</p>""", SRC2, DL),
    a_slide(2, n, """<h2>이번 주 기온</h2>
<div class="fig"><div><small>내일(4일) 아침</small><strong>2~11도</strong></div><div><small>내일 낮</small><strong>15~19도</strong></div></div>
<div class="fig"><div><small>5일(목)</small><strong>전국 비</strong></div><div><small>6일(금) 낮</small><strong>9~17도</strong></div></div>
<div class="box">5일 광주·전남 <b class="hl">10~40mm</b><br>서울·인천·경기 5mm 안팎</div>""", SRC2, DL),
    a_slide(3, n, """<h2>일교차 큰 날 체크</h2>
<ul class="chk"><li>아침·저녁엔 <span class="hl">겉옷 한 겹</span> 더</li><li>목요일 우산 챙기기</li><li>비 그친 금요일 낮 기온 뚝</li><li>퇴근 후엔 <span class="hl">따뜻한 차</span> 한 잔</li></ul>""", SRC2, DL),
    a_slide(4, n, f"""<h2>퇴근 후 한 잔 <span class="hl">따뜻한 차</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(YUJA)}"><div>꽃샘 꿀유자차 S<span>꿀 넣은 유자차 · 로켓배송</span></div></li>
<li><b>2</b><img src="{img(GING)}"><div>선비비책 진짜 생강청<span>100% 국산 생강</span></div></li>
<li><b>3</b><img src="{img(JUJU)}"><div>청년농원 대추차 티백<span>삼각티백 50개입</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/3 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "일교차 15도·목요일 전국 비",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 일교차 15도 안팎, 목요일(5일)엔 전국 비 ☔

· 오늘(3일) 아침 0~9도, 낮 15~19도 — 아침 기온이 전날보다 5~8도 낮아 일교차 15도 안팎
· 내일(4일) 아침 2~11도, 낮 15~19도 (서울 아침 8도·낮 18도)
· 5일(목) 비가 남부와 중부로 확대 — 광주·전남 10~40mm, 서울·인천·경기 5mm 안팎
· 6일(금) 아침 2~12도, 낮 9~17도로 낮 기온 뚝

✔ 아침·저녁엔 겉옷 한 겹 더, 목요일엔 우산 챙기기

🔗 퇴근 후 따뜻한 차 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 세계일보·톱스타뉴스(11/3) — 기상청 예보

#광고 #생활뉴스 #날씨 #일교차 #비소식 #유자차 #생강청 #대추차""",
    "products": [prod(1, YUJA, N_YUJA, "A"), prod(2, GING, N_GING, "A"), prod(3, JUJU, N_JUJU, "A")],
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


write(DATE, "B", [poll("외식비 또 올랐다,<br>오늘 점심은? 🍱", "10월 외식 물가 2.9%↑ (국가데이터처)",
                       [("그래도 맛집", "점심은 포기 못 해"), ("편의점 도시락", "가성비 최고"),
                        ("굶고 저녁에 몰아먹기", "다이어트라 치자"), ("양배추 도시락", "채소는 11.2%↓")], CAB)], {
    "title": "외식비 오른 날 점심 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 외식비 또 올랐다, 오늘 점심은? 🍱
댓글에 번호로 투표해주세요!

1️⃣ 그래도 맛집
2️⃣ 편의점 도시락
3️⃣ 굶고 저녁에 몰아먹기
4️⃣ 양배추 도시락

※ 10월 외식 2.9%↑, 채소류 11.2%↓ (국가데이터처, 11/3 발표)

🔗 4번 국내산 양배추 링크는 프로필에
👥 점심 메뉴 매일 고민하는 직장 동료 태그

#광고 #투표 #공감 #점심메뉴 #외식물가 #도시락 #양배추""",
    "products": [prod(1, CAB, N_CAB, "B")],
})

write(DATE, "B2", [poll("일교차 15도,<br>퇴근하고 한 잔은? ☕", "아침 0~9도 · 낮 15~19도 (기상청 예보)",
                        [("아이스 아메리카노", "얼죽아는 계절 안 탐"), ("따뜻한 라떼", "부드럽게 마무리"),
                         ("컵라면 국물", "이게 진짜 한 잔"), ("꿀유자차", "목이 칼칼할 땐")], YUJA)], {
    "title": "퇴근 후 한 잔 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 일교차 15도, 퇴근하고 마시는 한 잔은? ☕
댓글에 번호로 투표해주세요!

1️⃣ 아이스 아메리카노
2️⃣ 따뜻한 라떼
3️⃣ 컵라면 국물
4️⃣ 꿀유자차

🔗 4번 꽃샘 꿀유자차 링크는 프로필에
👥 한겨울에도 얼죽아인 친구 태그

#광고 #투표 #공감 #일교차 #퇴근길 #유자차 #얼죽아""",
    "products": [prod(1, YUJA, N_YUJA, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/3 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("10월 채소값 11.2%↓", "값 내린", "제철 채소", "BEST3", [CAR, CAB, RAD]),
    c_prod(1, "0070", CAR, "사계농산<br>국내산 흙당근", ["국내산 흙당근 상품", "5kg 1박스", "볶음·카레·주스까지"],
           ["💰 1만원대", "📦 무료배송"]),
    c_prod(2, "0071", CAB, "국내산<br>양배추 특품", ["아삭한 국내산 양배추", "2kg 3개", "쌈·샐러드·볶음용"],
           ["💰 1만원대", "📦 무료배송"]),
    c_prod(3, "0072", RAD, "국내산<br>햇 다발무", ["가을 햇무 · 무청 포함", "5kg 내외 1박스", "뭇국·깍두기·동치미용"],
           ["💰 1만원대", "📦 무료배송"]),
    c_howto("0070~0072"),
], {
    "title": "제철 채소 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

10월 채소값 11.2%↓ 🥕 값 내린 제철 채소 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 사계농산 국내산 흙당근 상 5kg 💛 품번 0070
볶음·카레·주스까지 넉넉한 5kg 1박스.

2. 국내산 아삭한 양배추 특품 2kg 3개 💛 품번 0071
쌈·샐러드·볶음에 두루 쓰는 양배추.

3. 국내산 햇 다발무 가을무 5kg 내외 💛 품번 0072
무청까지 들어 있는 가을 햇무, 뭇국·깍두기용.

※ 물가: 국가데이터처 10월 소비자물가동향(세계일보·서울신문 11/3 보도)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #제철채소 #당근 #양배추 #가을무 #장보기""",
    "products": [prod(1, CAR, N_CAR, "C", "0070"), prod(2, CAB, N_CAB, "C", "0071"), prod(3, RAD, N_RAD, "C", "0072")],
})

write(DATE, "C2", [
    c_cover("일교차 15도", "퇴근 후 한 잔", "따뜻한 차", "BEST3", [YUJA, GING, JUJU]),
    c_prod(1, "0073", YUJA, "꽃샘<br>꿀유자차 S", ["꿀 넣은 유자차", "뜨거운 물에 타서 한 잔", "새콤달콤 겨울 단골"],
           ["💰 1만원 미만", "🚀 로켓배송"]),
    c_prod(2, "0074", GING, "선비비책<br>진짜 생강청", ["100% 국산 생강청", "물에 타 생강차로", "알싸하고 진한 맛"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0075", JUJU, "청년농원<br>대추차 티백", ["대추차 삼각티백", "50개입", "티백이라 사무실에서도"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0073~0075"),
], {
    "title": "따뜻한 차 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

일교차 15도 ☕ 퇴근 후 한 잔, 따뜻한 차 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 꽃샘 꿀유자차 S 💛 품번 0073
뜨거운 물에 타 마시는 꿀유자차.

2. 선비비책 100% 국산 진짜 생강청 💛 품번 0074
국산 생강으로 만든 생강청, 물에 타면 생강차.

3. 청년농원 대추차 삼각티백 50개입 💛 품번 0075
티백이라 회사에서도 간편하게.

※ 날씨: 기상청 예보(세계일보·톱스타뉴스 11/3 보도)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #유자차 #생강청 #대추차 #일교차 #겨울차""",
    "products": [prod(1, YUJA, N_YUJA, "C", "0073"), prod(2, GING, N_GING, "C", "0074"), prod(3, JUJU, N_JUJU, "C", "0075")],
})
print("ok")
