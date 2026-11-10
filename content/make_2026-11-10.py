"""2026-11-10(화, 식품의 날) 게시물 6개 → docs/posts/2026-11-10/{A,B,C,A2,B2,C2}
점심: 아침 영하권·일교차 15도 → 따뜻한 간식 / 퇴근길: 내일 11월 11일 가래떡데이(농업인의 날)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-10"
DL = "2026.11.10 (화)"
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


YUJA, BAM, GOGU = "8610547094", "6855917521", "9801632833"
TTEOK, JOCHEONG, TBK = "8771531346", "8202492933", "9580732566"
N_YUJA = "마이데이즈 고흥 꿀 유자차 스틱 (휴대용)"
N_BAM = "CJ 맛밤"
N_GOGU = "국내산 꿀고구마 베니하루카 (26년 햇고구마)"
N_TTEOK = "농협식품 통가래떡"
N_JOCHEONG = "청정원 조청쌀엿"
N_TBK = "미정당 가래떡 쌀떡볶이 (냉동)"

# ═════════ A · 점심 12:00 — 아침 영하권·일교차 15도 → 따뜻한 간식 ═════════
SRC1 = "출처: 신아일보·월요신문·아시아경제(11/10), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">식품 · 오늘</div>
<h1>아침 영하권,<br><span class="hl">따뜻한 간식</span> 타임</h1>
<p class="lead">내륙 아침 영하로 뚝<br>낮밤 기온 차 15도 이상</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(10일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>-3~9도</strong></div><div><small>전국 낮 최고</small><strong>12~18도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>0~1도</strong></div><div><small>서울 낮</small><strong>12도</strong></div></div>
<div class="box">수도권·충남·전라 아침 <b class="hl">전날보다 3~8도↓</b><br>중부 내륙·경상 내륙 얼음 어는 곳</div>""", SRC1, DL),
    a_slide(3, n, """<h2>일교차 큰 날 <span class="hl">이렇게</span></h2>
<ul class="chk"><li>아침엔 얇은 옷 <span class="hl">겹쳐 입기</span></li><li>낮엔 한 겹 벗어 체온 조절</li><li>따뜻한 물·차 자주 마시기</li><li>그늘진 길·다리 위 <span class="hl">얼음</span> 조심</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>오후 출출할 땐 <span class="hl">겨울 간식</span></h2>
<ul class="chk"><li>텀블러에 <span class="hl">유자차</span> 한 잔</li><li>까서 바로 먹는 <span class="hl">군밤</span></li><li>에어프라이어·오븐 <span class="hl">군고구마</span></li><li>고구마는 냉장고 대신 서늘한 곳에</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>따뜻한 <span class="hl">겨울 간식</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(YUJA)}"><div>고흥 꿀 유자차 스틱<span>휴대용 · 텀블러에 쏙</span></div></li>
<li><b>2</b><img src="{img(BAM)}"><div>CJ 맛밤<span>까서 바로 먹는 밤</span></div></li>
<li><b>3</b><img src="{img(GOGU)}"><div>국내산 꿀고구마<span>베니하루카 · 26년 햇고구마</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/10 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "아침 영하권·따뜻한 겨울 간식",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘 아침 내륙 영하권, 낮밤 기온 차 15도 이상… 따뜻한 간식 챙길 때 🍠

· 10일(화) 전국 아침 최저 -3~9도, 낮 최고 12~18도 — 대체로 맑음
· 서울 아침 0~1도, 낮 12도
· 수도권·충남권·전라권 아침 기온 전날보다 3~8도가량 낮아져
· 중부 내륙·전북 동부·경상권 내륙은 얼음 어는 곳, 부산·울산·경북 동해안은 새벽까지 비

✔ 아침엔 얇은 옷 겹쳐 입고, 낮엔 한 겹 벗어 체온 조절
✔ 따뜻한 물·차 자주 마시기
✔ 그늘진 길·다리 위 얼음 조심
✔ 오후 출출할 땐 유자차 한 잔, 군밤, 군고구마
✔ 고구마는 냉장고 대신 서늘한 곳에 보관

🔗 겨울 간식 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 신아일보·월요신문·아시아경제(11/10) — 기상청 예보

#광고 #생활뉴스 #날씨 #일교차 #겨울간식 #군고구마 #유자차""",
    "products": [prod(1, YUJA, N_YUJA, "A"), prod(2, BAM, N_BAM, "A"), prod(3, GOGU, N_GOGU, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 내일 11월 11일 가래떡데이 ═════════
SRC2 = "출처: 농축유통신문(2025.11.10), 한국금융경제신문, 농민신문(11/9)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">식품 · 내일</div>
<h1>내일 11월 11일은<br><span class="hl">가래떡데이</span></h1>
<p class="lead">막대 과자 말고<br>우리 쌀 가래떡 한 줄 어때요?</p>""", SRC2, DL),
    a_slide(2, n, """<h2>왜 <span class="hl">11월 11일?</span></h2>
<div class="fig"><div><small>농업인의 날 제정</small><strong>1996년</strong></div><div><small>가래떡데이 지정</small><strong>2006년</strong></div></div>
<div class="box">十一(11)을 합치면 <b class="hl">흙 토(土)</b><br>쌀 소비를 늘리려고 가래떡데이로</div>""", SRC2, DL),
    a_slide(3, n, """<h2>가래떡 <span class="hl">맛있게 먹기</span></h2>
<ul class="chk"><li>프라이팬에 살짝 <span class="hl">구워서</span></li><li>꿀·<span class="hl">조청</span>에 콕 찍어 간식으로</li><li>얇게 썰면 떡국</li><li>길게 자르면 떡볶이</li></ul>""", "출처: 한국금융경제신문", DL),
    a_slide(4, n, """<h2>곳곳 <span class="hl">가래떡 행사</span></h2>
<ul class="chk"><li>농협 증평군지부, 가래떡데이 맞아<br>쌀 소비 촉진 행사 (농민신문 11/9)</li><li>지난해엔 국립식량과학원이<br>귀리·자색고구마 섞은 <span class="hl">곡물 가래떡</span> 나눔</li></ul>""", "출처: 농민신문(11/9), 농축유통신문(2025.11.10)", DL),
    a_slide(5, n, f"""<h2>가래떡데이 <span class="hl">장바구니</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(TTEOK)}"><div>농협식품 통가래떡<span>구워 먹기 좋은 통가래떡</span></div></li>
<li><b>2</b><img src="{img(JOCHEONG)}"><div>청정원 조청쌀엿<span>구운 가래떡 콕</span></div></li>
<li><b>3</b><img src="{img(TBK)}"><div>미정당 가래떡 쌀떡볶이<span>냉동 · 간편 조리</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/10 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "내일은 가래떡데이",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 내일 11월 11일은 농업인의 날이자 '가래떡데이' 🍡

· 정부는 1996년 11월 11일을 '농업인의 날'로 제정 — 十一(11)을 합치면 흙 토(土)
· 2006년부터 쌀 소비를 늘리려고 이날을 '가래떡데이'로 지정
· 올해도 농협 증평군지부 등 곳곳에서 가래떡데이 쌀 소비 촉진 행사
· 지난해엔 국립식량과학원이 우리 쌀에 귀리·자색고구마를 섞은 '곡물 가래떡' 나눔 행사

✔ 프라이팬에 살짝 구워 꿀·조청에 찍어 간식으로
✔ 얇게 썰면 떡국, 길게 자르면 떡볶이

🔗 가래떡데이 장바구니 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 농축유통신문(2025.11.10), 한국금융경제신문, 농민신문(2026.11.9)

#광고 #생활뉴스 #가래떡데이 #농업인의날 #가래떡 #11월11일 #우리쌀""",
    "products": [prod(1, TTEOK, N_TTEOK, "A"), prod(2, JOCHEONG, N_JOCHEONG, "A"), prod(3, TBK, N_TBK, "A")],
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


write(DATE, "B", [poll("아침 영하권 출근길,<br>손 녹일 간식은? 🍠", "10일 내륙 아침 영하권, 일교차 15도 이상 (기상청 예보)",
                       [("편의점 호빵", "호호 불어 한 입"), ("붕어빵", "팥 vs 슈크림"),
                        ("군고구마", "겨울엔 역시"), ("유자차 한 잔", "텀블러에 스틱 쏙")], YUJA)], {
    "title": "출근길 겨울 간식 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 아침 영하권 출근길, 손 녹일 간식은? 🍠
댓글에 번호로 투표해주세요!

1️⃣ 편의점 호빵
2️⃣ 붕어빵
3️⃣ 군고구마
4️⃣ 유자차 한 잔

※ 10일(화) 전국 아침 -3~9도, 낮 12~18도 — 낮밤 기온 차 15도 이상 (기상청 예보, 신아일보·월요신문 11/10)

🔗 4번 고흥 꿀 유자차 스틱 링크는 프로필에
👥 붕어빵 머리부터 먹는 친구 태그

#광고 #투표 #공감 #겨울간식 #출근길 #유자차""",
    "products": [prod(1, YUJA, N_YUJA, "B")],
})

write(DATE, "B2", [poll("내일 11월 11일,<br>나는 무슨 파? 🍡", "11월 11일 = 농업인의 날 · 가래떡데이 (2006년 지정)",
                        [("빼빼로 파", "초코 과자 주고받기"), ("둘 다 파", "과자도 떡도 좋아"),
                         ("평일 파", "그냥 수요일"), ("가래떡 파", "구워서 조청 콕")], TTEOK)], {
    "title": "빼빼로 vs 가래떡 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 내일 11월 11일, 나는 무슨 파? 🍡
댓글에 번호로 투표해주세요!

1️⃣ 빼빼로 파
2️⃣ 둘 다 파
3️⃣ 평일 파
4️⃣ 가래떡 파

※ 11월 11일은 농업인의 날(1996년 제정), 2006년부터 쌀 소비를 늘리려고 '가래떡데이'로 (농축유통신문 2025.11.10)
※ 가래떡은 프라이팬에 살짝 구워 꿀·조청에 찍어 먹기 (한국금융경제신문)

🔗 4번 농협식품 통가래떡 링크는 프로필에
👥 내일 가래떡 사 줄 친구 태그

#광고 #투표 #공감 #가래떡데이 #빼빼로데이 #11월11일""",
    "products": [prod(1, TTEOK, N_TTEOK, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/10 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("아침 영하권 · 일교차 15도", "겨울", "간식템", "BEST3", [YUJA, BAM, GOGU]),
    c_prod(1, "0112", YUJA, "고흥 꿀<br>유자차 스틱", ["고흥 유자 + 꿀", "스푼 모양 스틱", "텀블러에 하나 쏙"],
           ["💰 5천원대", "🚚 일반배송"]),
    c_prod(2, "0113", BAM, "CJ<br>맛밤", ["까서 바로 먹는 밤", "사무실 서랍 간식", "여러 봉 묶음"],
           ["💰 2만4천원대", "🚀 로켓배송"]),
    c_prod(3, "0114", GOGU, "국내산<br>꿀고구마", ["베니하루카 품종", "26년 햇고구마", "에어프라이어 군고구마"],
           ["💰 8천원대", "🚚 무료배송"]),
    c_howto("0112~0114"),
], {
    "title": "겨울 간식템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

아침 영하권, 일교차 15도 🍠 따뜻한 겨울 간식템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 마이데이즈 고흥 꿀 유자차 스틱 (휴대용) 💛 품번 0112
스푼 모양 스틱이라 텀블러에 하나씩 타 먹기 좋아요.

2. CJ 맛밤 💛 품번 0113
까서 바로 먹는 밤. 사무실 서랍 간식으로.

3. 국내산 꿀고구마 베니하루카 (26년 햇고구마) 💛 품번 0114
에어프라이어·오븐에 구워 군고구마로.

✔ 고구마는 냉장고 대신 서늘한 곳에 보관

※ 날씨: 기상청 예보(신아일보·월요신문 11/10)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #겨울간식 #군고구마 #맛밤 #유자차""",
    "products": [prod(1, YUJA, N_YUJA, "C", "0112"), prod(2, BAM, N_BAM, "C", "0113"), prod(3, GOGU, N_GOGU, "C", "0114")],
})

write(DATE, "C2", [
    c_cover("내일 11월 11일 · 가래떡데이", "가래떡데이", "장바구니", "BEST3", [TTEOK, JOCHEONG, TBK]),
    c_prod(1, "0115", TTEOK, "농협식품<br>통가래떡", ["구워 먹기 좋은", "통가래떡", "떡국·떡볶이로도"],
           ["💰 3천원대", "🚀 로켓프레시"]),
    c_prod(2, "0116", JOCHEONG, "청정원<br>조청쌀엿", ["구운 가래떡에 콕", "요리 단맛 낼 때도", "병 타입"],
           ["💰 3천원대", "🚀 로켓배송"]),
    c_prod(3, "0117", TBK, "미정당<br>가래떡 쌀떡볶이", ["가래떡 쌀떡볶이", "냉동 간편 조리", "퇴근길 저녁으로"],
           ["💰 6천원대", "🚀 로켓프레시"]),
    c_howto("0115~0117"),
], {
    "title": "가래떡데이 장바구니 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

내일 11월 11일은 가래떡데이 🍡 가래떡데이 장바구니 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 농협식품 통가래떡 💛 품번 0115
프라이팬에 살짝 구워 간식으로, 썰어서 떡국·떡볶이로.

2. 청정원 조청쌀엿 💛 품번 0116
구운 가래떡 찍어 먹는 조청.

3. 미정당 가래떡 쌀떡볶이 (냉동) 💛 품번 0117
가래떡 쌀떡볶이 간편 조리 제품.

✔ 11월 11일은 농업인의 날(1996년 제정), 2006년부터 가래떡데이

※ 농축유통신문(2025.11.10), 한국금융경제신문
※ {NOTE}

#광고 #쿠팡추천템 #식품 #가래떡데이 #가래떡 #조청 #떡볶이""",
    "products": [prod(1, TTEOK, N_TTEOK, "C", "0115"), prod(2, JOCHEONG, N_JOCHEONG, "C", "0116"), prod(3, TBK, N_TBK, "C", "0117")],
})
print("ok")
