"""2026-10-23(금, 식품의 날) 게시물 6개 → docs/posts/2026-10-23/{A,B,C,A2,B2,C2}
점심: 쌀값·밥상 물가 / 퇴근길: 일교차 15도·쌀쌀한 저녁
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402

DATE = "2026-10-23"
DL = "2026.10.23 (금)"
cat = json.loads((ROOT / "catalog" / f"{DATE}.json").read_text(encoding="utf-8"))


def link(pid, key):
    """catalog 에서 채널(key)용 파트너스 링크 찾기"""
    url = f"https://www.coupang.com/vp/products/{pid}"
    for u in cat["urls"]:
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


RICE, BAP, NURUNG, GRAIN = "166996432", "9052582961", "8574402406", "1848953441"
YUJA, GINGER, HOTTEOK, RAMEN = "96760", "9392103490", "1369157", "7216841891"

# ═════════ A · 점심 12:00 — 쌀값·밥상 물가 ═════════
SRC1 = "출처: 파이낸셜뉴스(10/21·10/22) — aT 소매가격·닐슨·농촌경제연구원 자료 인용"
n = 6
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 물가</div>
<h1>쌀 20kg <span class="hl">6만2천원</span>…<br>밥상 물가<br>'들썩'</h1>
<p class="lead">쌀 소매가가 평년보다 11.3% 높습니다.<br>서울 비빔밥 한 그릇은 1만2천원 턱밑까지.</p>""", SRC1, DL),
    a_slide(2, n, """<h2>숫자로 보는 밥상 물가</h2>
<div class="fig"><div><small>쌀 20kg 소매가</small><strong>62,903원</strong></div><div><small>평년 대비</small><strong>+11.3%</strong></div></div>
<div class="fig"><div><small>서울 비빔밥</small><strong>11,923원</strong></div><div><small>서울 김밥 1줄</small><strong>3,923원</strong></div></div>
<p class="lead" style="font-size:34px">쌀값은 10월 20일 aT 기준, 외식 가격은 8월 서울 평균입니다.</p>""", SRC1, DL),
    a_slide(3, n, """<h2>즉석밥도 올랐다</h2>
<div class="fig"><div><small>작년 10월</small><strong>1,590원</strong></div><div><small>올해 9월</small><strong>1,642원</strong></div></div>
<p class="lead">즉석밥 평균 판매가가 <b class="hl">3.3%</b> 올랐습니다.</p>
<div class="box">130g 이하 <b>소용량 즉석밥</b> 비중<br>4%(2022 상반기) → <b class="hl">16%</b>(2026 상반기)</div>""", SRC1, DL),
    a_slide(4, n, """<h2>쌀은 덜 먹는다</h2>
<div class="fig"><div><small>1~8월 쌀 소매 판매량</small><strong>24.7만t</strong></div><div><small>작년 대비</small><strong>-7.1%</strong></div></div>
<p class="lead">1인 가구가 늘고 식습관이 바뀐 영향이라는 분석입니다. 업체들은 작은 용량 제품을 늘리고 있습니다.</p>""", SRC1, DL),
    a_slide(5, n, """<h2>밥값 아끼는 생활 팁</h2>
<ul class="chk"><li>밥은 한 번에 지어 1공기씩 냉동</li><li>잡곡 섞어 밥 짓기</li><li>바쁜 날 대비 즉석밥 몇 개 쟁여두기</li><li>누룽지로 간단한 아침</li></ul>""", "", DL),
    a_slide(6, n, f"""<h2>오늘 정리한 <span class="hl">밥상 아이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(RICE)}"><div>2026년산 햅쌀<span>곰곰 상등급 백미</span></div></li>
<li><b>2</b><img src="{img(BAP)}"><div>즉석밥 흰밥<span>바쁜 날 한 끼</span></div></li>
<li><b>3</b><img src="{img(NURUNG)}"><div>국산 가마솥 누룽지<span>2.5kg 대용량</span></div></li>
<li><b>4</b><img src="{img(GRAIN)}"><div>국산 혼합 17곡<span>쌀에 섞어 밥 짓기</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/23 점심 ①~④</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "쌀값·밥상 물가",
    "caption": f"""{DISC}

[생활뉴스] 쌀 20kg 6만2천원…밥상 물가 '들썩'

· 쌀 20kg 소매가 62,903원, 평년보다 11.3%↑ (10/20 aT)
· 서울 비빔밥 11,923원, 김밥 3,923원 (8월)
· 즉석밥 평균 1,590원 → 1,642원 (+3.3%)
· 1~8월 쌀 소매 판매량 24.7만t, 작년보다 7.1%↓

🔗 밥상 아이템 ①~④는 프로필 링크에 있어요
🛒 가성비 집밥템 비교는 @0315_pick

출처: 파이낸셜뉴스 10/21·10/22 보도(aT·닐슨·농촌경제연구원 자료 인용)

#광고 #생활뉴스 #쌀값 #밥상물가 #장바구니물가 #즉석밥 #집밥""",
    "products": [prod(1, RICE, "곰곰 2026년산 햅쌀 소중한 우리쌀 상등급", "A"), prod(2, BAP, "오뚜기 흰밥", "A"),
                 prod(3, NURUNG, "배대감 국산 100% 가마솥 누룽지 2.5kg", "A"), prod(4, GRAIN, "대구농산 국산 혼합 17곡 4kg", "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 일교차 15도 ═════════
SRC2 = "출처: 기상청 예보 인용 보도 — 머니투데이(10/23), 미디어파인(10/22)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 생활</div>
<h1>아침 7도, 낮 21도…<br><span class="hl">일교차 15도</span><br>금요일</h1>
<p class="lead">내륙 곳곳에 서리가 내렸습니다.<br>남부지방과 제주는 오후부터 비 소식.</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘 기온</h2>
<div class="fig"><div><small>서울 아침</small><strong>7℃</strong></div><div><small>서울 낮</small><strong>21℃</strong></div></div>
<div class="fig"><div><small>춘천 아침</small><strong>4℃</strong></div><div><small>제주 아침</small><strong>18℃</strong></div></div>
<p class="lead">아침은 평년보다 낮고, 낮 기온은 평년과 비슷하거나 조금 높았습니다.</p>""", SRC2, DL),
    a_slide(3, n, """<h2>남부·제주 비 소식</h2>
<div class="box">제주(북부·서부 제외) <b class="hl">30~80mm</b><br>광주·전남, 부산·울산·경남 <b class="hl">5~30mm</b></div>
<p class="lead">제주 남쪽 해상을 지나는 기압골 영향입니다. 제주에는 강풍특보가 나올 가능성도 있습니다.</p>""", SRC2, DL),
    a_slide(4, n, """<h2>일교차 큰 날 챙길 것</h2>
<ul class="chk"><li>얇은 겉옷 하나 더 챙기기</li><li>따뜻한 차로 수분 보충</li><li>남부지방은 우산 챙기기</li><li>저녁엔 따뜻한 집밥·간식</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>쌀쌀한 저녁 <span class="hl">따뜻템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(YUJA)}"><div>꿀유자차<span>뜨거운 물에 타기만</span></div></li>
<li><b>2</b><img src="{img(GINGER)}"><div>국산 생강청<span>따뜻한 물에 한 스푼</span></div></li>
<li><b>3</b><img src="{img(HOTTEOK)}"><div>찹쌀 호떡믹스<span>집에서 굽는 간식</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/23 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "일교차 15도 금요일",
    "caption": f"""{DISC}

[생활뉴스] 아침 7도, 낮 21도…일교차 15도 금요일

· 서울 아침 7℃ → 낮 21℃, 춘천 아침 4℃
· 내륙 곳곳 서리, 일부 강원 내륙·산지는 얼음
· 남부·제주 오후부터 비 (제주 30~80mm)

🔗 쌀쌀한 저녁 따뜻템 ①~③은 프로필 링크에 있어요

출처: 기상청 예보 인용 보도(머니투데이 10/23, 미디어파인 10/22)

#광고 #생활뉴스 #오늘날씨 #일교차 #가을날씨 #유자차 #집콕""",
    "products": [prod(1, YUJA, "담터 꿀유자차", "A"), prod(2, GINGER, "선비비책 100% 국산 생강청", "A"),
                 prod(3, HOTTEOK, "백설 찹쌀 호떡믹스", "A")],
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


write(DATE, "B", [poll("비빔밥 1만2천원 시대,<br>점심 어떻게 함? 🍚", "서울 비빔밥 평균 11,923원 (8월)",
                       [("그냥 사 먹는다", "점심은 나를 위한 투자"), ("편의점 김밥 한 줄", "김밥도 3,923원이지만…"),
                        ("구내식당이 최고", "가성비 원탑"), ("즉석밥 도시락 싸 간다", "반찬만 챙기면 끝")], BAP)], {
    "title": "점심 어떻게 함? 투표",
    "caption": f"""{DISC}

📊 비빔밥 1만2천원 시대, 점심 어떻게 함? 🍚
댓글에 번호로 투표해주세요!

1️⃣ 그냥 사 먹는다
2️⃣ 편의점 김밥 한 줄
3️⃣ 구내식당이 최고
4️⃣ 즉석밥 도시락 싸 간다

🔗 4번 즉석밥 링크는 프로필에
👥 점심 메뉴 맨날 고민하는 친구 태그

#광고 #투표 #공감 #점심메뉴 #직장인점심 #도시락 #밥값""",
    "products": [prod(1, BAP, "오뚜기 흰밥", "B")],
})

write(DATE, "B2", [poll("금요일 퇴근길,<br>오늘 저녁은? 🌙", "일교차 15도, 저녁엔 쌀쌀해요",
                        [("치킨 시킨다", "불금엔 역시"), ("고기 구우러 간다", "한 주 고생했으니까"),
                         ("일단 눕고 생각", "배고프면 그때…"), ("라면 끓인다", "쌀쌀할 땐 국물이 최고")], RAMEN)], {
    "title": "금요일 저녁 메뉴 투표",
    "caption": f"""{DISC}

📊 금요일 퇴근길, 오늘 저녁은? 🌙
댓글에 번호로 투표해주세요!

1️⃣ 치킨 시킨다
2️⃣ 고기 구우러 간다
3️⃣ 일단 눕고 생각
4️⃣ 라면 끓인다

🔗 4번 라면 링크는 프로필에
👥 오늘 저녁 같이 먹을 사람 태그

#광고 #투표 #공감 #불금 #저녁메뉴 #퇴근길 #라면""",
    "products": [prod(1, RAMEN, "오뚜기 진라면 매운맛 멀티팩", "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/23 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("쌀값 오를 때", "밥값 아끼는", "가성비 집밥템", "BEST3", [BAP, NURUNG, GRAIN]),
    c_prod(1, "0004", BAP, "오뚜기 흰밥<br>(즉석밥)", ["전자레인지에 데우면 바로 한 끼", "바쁜 아침·야식용으로 쟁여두기", "밥 짓기 귀찮은 날 든든"],
           ["💰 1만원 안팎", "🚀 로켓배송"]),
    c_prod(2, "0005", NURUNG, "국산 가마솥 누룽지<br>(2.5kg)", ["국산 쌀 100% 누룽지", "물 붓고 끓이면 구수한 아침", "2.5kg 대용량이라 오래 먹음"],
           ["💰 1만원 안팎", "📦 2.5kg", "🚀 로켓배송"]),
    c_prod(3, "0006", GRAIN, "국산 혼합 17곡<br>(4kg)", ["17가지 곡물이 한 봉지에", "쌀에 섞어 밥 짓기만 하면 끝", "4kg 대용량"],
           ["💰 1만원대", "📦 4kg", "🚀 로켓배송"]),
    c_howto("0004~0006"),
], {
    "title": "가성비 집밥템 BEST3",
    "caption": f"""{DISC}

쌀값 오를 때 🍚 밥값 아끼는 가성비 집밥템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 오뚜기 흰밥(즉석밥) 💛 품번 0004
데우면 바로 한 끼. 바쁜 아침·야식용으로 쟁여두기 좋아요.

2. 국산 가마솥 누룽지 2.5kg 💛 품번 0005
국산 쌀 100%. 물 붓고 끓이면 구수한 아침 완성.

3. 국산 혼합 17곡 4kg 💛 품번 0006
쌀에 섞어 밥 짓기만 하면 돼요.

※ {NOTE}

#광고 #쿠팡추천템 #집밥 #즉석밥 #누룽지 #잡곡밥 #자취템 #살림템""",
    "products": [prod(1, BAP, "오뚜기 흰밥", "C", "0004"), prod(2, NURUNG, "배대감 국산 100% 가마솥 누룽지 2.5kg", "C", "0005"),
                 prod(3, GRAIN, "대구농산 국산 혼합 17곡 4kg", "C", "0006")],
})

write(DATE, "C2", [
    c_cover("일교차 15도, 저녁엔", "쌀쌀한 저녁", "집콕 따뜻템", "BEST3", [YUJA, GINGER, HOTTEOK]),
    c_prod(1, "0007", YUJA, "담터 꿀유자차", ["뜨거운 물에 타기만 하면 끝", "새콤달콤한 유자 향", "만원 이하로 부담 없음"],
           ["💰 6천원대", "🚀 로켓배송"]),
    c_prod(2, "0008", GINGER, "국산 생강청", ["국산 생강으로 만든 생강청", "따뜻한 물에 한 스푼", "우유·홍차에 넣어도 OK"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0009", HOTTEOK, "백설 찹쌀 호떡믹스", ["집에서 굽는 찹쌀호떡", "프라이팬 하나면 충분", "쌀쌀한 저녁 간식으로"],
           ["💰 5천원대", "🚀 로켓배송"]),
    c_howto("0007~0009"),
], {
    "title": "집콕 따뜻템 BEST3",
    "caption": f"""{DISC}

일교차 15도 🌙 쌀쌀한 저녁 집콕 따뜻템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 담터 꿀유자차 💛 품번 0007
뜨거운 물에 타기만 하면 끝. 새콤달콤 유자 향.

2. 국산 생강청 💛 품번 0008
따뜻한 물에 한 스푼. 우유·홍차에 넣어도 좋아요.

3. 백설 찹쌀 호떡믹스 💛 품번 0009
프라이팬 하나로 집에서 굽는 찹쌀호떡.

※ {NOTE}

#광고 #쿠팡추천템 #유자차 #생강차 #호떡 #집콕 #겨울간식 #자취템""",
    "products": [prod(1, YUJA, "담터 꿀유자차", "C", "0007"), prod(2, GINGER, "선비비책 100% 국산 생강청", "C", "0008"),
                 prod(3, HOTTEOK, "백설 찹쌀 호떡믹스", "C", "0009")],
})
print("ok")
