"""2026-11-24(화, 식품의 날) 게시물 6개 → docs/posts/2026-11-24/{A,B,C,A2,B2,C2}
점심: 10월 생산자물가(한국은행) 사과 29.2%·돼지고기 12.8%↓ → 돼지고기·사과즙 / 퇴근길: 영하권 추위+강풍, 25일까지 → 겨울 간식(고구마·유자차·호떡)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-24"
DL = "2026.11.24 (화)"
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


NECK, LEG, AJUICE = "188172346", "7313224375", "9766077327"
SWEET, YUJA, HOTTEOK = "7525821319", "345075023", "9169972940"
N_NECK = "도드람한돈 1등급 목심 구이용 (냉장)"
N_LEG = "선진포크 한돈 미박 앞다리 수육용 1kg + 분말스프 2p (냉장)"
N_AJUICE = "영주 햇살듬뿍 사과즙"
N_SWEET = "파머스넷 세척 무농약 꿀고구마"
N_YUJA = "고흥식품 통 유자차"
N_HOTTEOK = "백설 찹쌀 호떡믹스 400g + 호떡누르개 세트"

# ═════════ A · 점심 12:00 — 10월 생산자물가 ═════════
SRC1 = "출처: 노컷뉴스·아시아경제(11/20) — 한국은행"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 물가</div>
<h1>사과·돼지고기<br><span class="hl">출하값 ↓</span></h1>
<p class="lead">10월 생산자물가<br>석 달 만에 하락</p>""", SRC1, DL),
    a_slide(2, n, """<h2>먹거리 <span class="hl">크게 내렸어요</span></h2>
<div class="fig"><div><small>사과</small><strong>-29.2%</strong></div><div><small>돼지고기</small><strong>-12.8%</strong></div></div>
<div class="box">9월보다 내린 폭<br>농림수산품 전체 <b class="hl">-8.3%</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>품목별 <span class="hl">흐름</span></h2>
<ul class="chk"><li>농산물 <span class="hl">-11.8%</span></li><li>축산물 <span class="hl">-7.3%</span></li><li>생산자물가 전체 <span class="hl">-0.1%</span></li><li>음식점·숙박은 <span class="hl">+0.7%</span></li></ul>
<p class="lead" style="font-size:30px">모두 9월 대비 · 잠정치</p>""", SRC1, DL),
    a_slide(4, n, """<h2>생산자물가란?</h2>
<div class="box">농장·공장에서 <b class="hl">출하할 때</b> 가격<br>마트 가격엔 <b class="hl">시차를 두고</b> 반영돼요</div>
<ul class="chk"><li>한은 "일시적 영향일 <span class="hl">가능성</span>"</li><li>장 볼 땐 <span class="hl">할인·제철</span> 체크</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>값 내린 품목 <span class="hl">장보기</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(NECK)}"><div>한돈 1등급 목심<span>도드람 · 구이용 냉장</span></div></li>
<li><b>2</b><img src="{img(LEG)}"><div>앞다리 수육용 1kg<span>선진포크 · 분말스프 2p</span></div></li>
<li><b>3</b><img src="{img(AJUICE)}"><div>영주 사과즙<span>햇살듬뿍 · 파우치형</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/24 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "사과·돼지고기 출하값 하락",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 10월 생산자물가, 사과·돼지고기가 크게 내렸어요 🍎🐷

한국은행 '2026년 10월 생산자물가지수(잠정)' (11월 20일 발표, 9월 대비)
· 생산자물가 전체 0.1% 하락 — 석 달 만에 하락 전환
· 농림수산품 8.3% 하락 (농산물 -11.8%, 축산물 -7.3%)
· 사과 29.2%, 돼지고기 12.8% 하락
· 반면 음식점·숙박 서비스는 0.7% 상승

✔ 생산자물가는 농장·공장 출하 단계 가격이라, 마트 가격에는 시차를 두고 반영돼요
✔ 한은은 농산물 하락이 일시적 영향일 가능성이 크다고 봤어요

🔗 값 내린 품목 장보기 ①~③은 프로필 링크에 있어요
🛒 더 많은 장바구니템은 @0315_pick

출처: 노컷뉴스(2026.11.20)·아시아경제(2026.11.20) — 한국은행 발표

#광고 #생활뉴스 #물가 #생산자물가 #돼지고기 #사과 #장보기""",
    "products": [prod(1, NECK, N_NECK, "A"), prod(2, LEG, N_LEG, "A"), prod(3, AJUICE, N_AJUICE, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 영하권 추위 + 강풍 ═════════
SRC2 = "출처: 세계일보(11/23) — 기상청"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>영하권 추위에<br><span class="hl">강풍까지</span></h1>
<p class="lead">추위는 수요일(25일)까지<br>이어질 전망</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘(24일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>-6~+7도</strong></div><div><small>낮 최고</small><strong>2~10도</strong></div></div>
<div class="box">서울 <b class="hl">-2도 → 3도</b><br>대전 0도 → 4도 · 부산 5도 → 9도</div>""", SRC2, DL),
    a_slide(3, n, """<h2>바람이 <span class="hl">매서워요</span></h2>
<ul class="chk"><li>대부분 순간풍속 <span class="hl">시속 55km 안팎</span></li><li>해안·제주 등 <span class="hl">시속 70km 이상</span></li><li>체감온도는 기온보다 <span class="hl">더 낮아요</span></li><li>간판·화분 등 <span class="hl">날림 주의</span></li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>눈·비 & <span class="hl">빙판길</span></h2>
<ul class="chk"><li>충남 서부·세종 등 <span class="hl">1cm 안팎 눈</span></li><li>제주 산지 25일 새벽까지 <span class="hl">1~5cm</span></li><li>그늘진 길 <span class="hl">살얼음</span> 조심</li><li>미세먼지는 대체로 <span class="hl">좋음</span></li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>칼바람 저녁 <span class="hl">겨울 간식</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SWEET)}"><div>세척 꿀고구마<span>파머스넷 · 무농약</span></div></li>
<li><b>2</b><img src="{img(YUJA)}"><div>통 유자차<span>고흥식품 · 따뜻한 한 잔</span></div></li>
<li><b>3</b><img src="{img(HOTTEOK)}"><div>찹쌀 호떡믹스<span>백설 · 호떡누르개 포함</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/24 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "영하권 추위에 강풍, 25일까지 이어져",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 영하권 추위에 강풍까지 🌬 추위는 25일(수)까지 이어져요

· 24일(화) 아침 최저 영하 6도~영상 7도, 낮 최고 2~10도
· 서울 영하 2도→3도, 대전 0도→4도, 부산 5도→9도
· 대부분 지역 순간풍속 시속 55km 안팎, 해안·제주 등은 70km 이상
· 찬 공기가 들어오며 체감온도는 기온보다 더 낮아요
· 충남 서부·세종 등 1cm 안팎 눈, 제주 산지는 25일 새벽까지 1~5cm
· 미세먼지는 대체로 '좋음'

✔ 퇴근길 그늘진 길·다리 위 살얼음 조심
✔ 바람에 날릴 수 있는 물건은 미리 정리

🔗 칼바람 저녁 겨울 간식 ①~③은 프로필 링크에 있어요
🛒 더 많은 겨울 간식은 @0315_pick

출처: 세계일보(2026.11.23) — 기상청 예보

#광고 #생활뉴스 #날씨 #강풍 #영하권 #겨울간식 #고구마""",
    "products": [prod(1, SWEET, N_SWEET, "A"), prod(2, YUJA, N_YUJA, "A"), prod(3, HOTTEOK, N_HOTTEOK, "A")],
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


write(DATE, "B", [poll("돼지고기 출하값 ↓<br>오늘 저녁 메뉴는? 🐷", "10월 생산자물가 돼지고기 -12.8% · 한국은행",
                       [("삼겹살", "국룰은 국룰"), ("제육볶음", "밥 두 공기 각"),
                        ("김치찌개", "추운 날엔 국물"), ("목살 구이", "두툼하게 구워 먹기")], NECK)], {
    "title": "돼지고기 저녁 메뉴 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 돼지고기 출하값 내렸대요, 오늘 저녁 메뉴는? 🐷
댓글에 번호로 투표해주세요!

1️⃣ 삼겹살
2️⃣ 제육볶음
3️⃣ 김치찌개
4️⃣ 목살 구이

※ 10월 생산자물가에서 돼지고기 12.8%, 사과 29.2% 하락(9월 대비) — 출하 단계 가격이라 소비자 가격엔 시차가 있어요 (한국은행, 노컷뉴스 11/20)

🔗 4번 한돈 1등급 목심 링크는 프로필에
👥 고기 같이 구워 먹을 사람 태그

#광고 #투표 #공감 #저녁메뉴 #돼지고기 #목살""",
    "products": [prod(1, NECK, N_NECK, "B")],
})

write(DATE, "B2", [poll("칼바람 부는 날,<br>고구마는 어떻게? 🍠", "영하권 추위·강풍 25일까지 · 기상청",
                        [("군고구마", "길거리 냄새 못 참음"), ("찐고구마", "김치랑 같이"),
                         ("고구마 맛탕", "달달함 끝판왕"), ("에어프라이어", "집에서 군고구마")], SWEET)], {
    "title": "고구마 먹는 법 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 칼바람 부는 날, 고구마는 어떻게 먹어요? 🍠
댓글에 번호로 투표해주세요!

1️⃣ 군고구마
2️⃣ 찐고구마
3️⃣ 고구마 맛탕
4️⃣ 에어프라이어 군고구마

※ 24일 아침 최저 영하 6도~영상 7도, 순간풍속 시속 55km 안팎 강풍 — 추위는 25일까지 이어질 전망 (기상청 예보, 세계일보 11/23)

🔗 4번 세척 꿀고구마 링크는 프로필에
👥 고구마 같이 먹을 사람 태그

#광고 #투표 #공감 #고구마 #겨울간식 #에어프라이어""",
    "products": [prod(1, SWEET, N_SWEET, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/24 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("사과·돼지고기 출하값 ↓ 🛒", "값 내린", "장바구니", "BEST3", [NECK, LEG, AJUICE]),
    c_prod(1, "0196", NECK, "한돈 1등급<br>목심 구이용", ["도드람한돈", "1등급 국내산", "냉장 구이용"],
           ["💰 1만원대", "📦 목심"]),
    c_prod(2, "0197", LEG, "앞다리<br>수육용 1kg", ["선진포크 한돈", "미박 앞다리 1kg", "분말스프 2p 포함"],
           ["💰 1만원대", "📦 1kg+스프"]),
    c_prod(3, "0198", AJUICE, "영주<br>사과즙", ["햇살듬뿍 사과즙", "개별 파우치형", "간편하게 한 포"],
           ["💰 1만원대", "📦 파우치"]),
    c_howto("0196~0198"),
], {
    "title": "값 내린 장바구니 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

사과·돼지고기 출하값 내렸어요 🛒 값 내린 장바구니 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 도드람한돈 1등급 목심 구이용 (냉장) 💛 품번 0196
두툼하게 구워 먹는 국내산 1등급 목심.

2. 선진포크 한돈 미박 앞다리 수육용 1kg + 분말스프 2p 💛 품번 0197
스프까지 들어 있어 수육 한 냄비 간편하게.

3. 영주 햇살듬뿍 사과즙 💛 품번 0198
파우치형이라 아침에 한 포씩.

✔ 10월 생산자물가(9월 대비) 사과 29.2%·돼지고기 12.8% 하락 — 출하 단계 가격이라 소비자 가격엔 시차가 있어요

※ 물가: 한국은행(노컷뉴스·아시아경제 11/20)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #장보기 #한돈 #수육 #사과즙""",
    "products": [prod(1, NECK, N_NECK, "C", "0196"), prod(2, LEG, N_LEG, "C", "0197"), prod(3, AJUICE, N_AJUICE, "C", "0198")],
})

write(DATE, "C2", [
    c_cover("영하권 추위에 강풍 🌬", "칼바람 저녁", "겨울 간식", "BEST3", [SWEET, YUJA, HOTTEOK]),
    c_prod(1, "0199", SWEET, "세척<br>꿀고구마", ["파머스넷", "무농약 인증", "세척 고구마"],
           ["💰 1만원대", "📦 박스"]),
    c_prod(2, "0200", YUJA, "고흥식품<br>통 유자차", ["통 유자차", "병에 담긴 유자청", "뜨거운 물에 한 스푼"],
           ["💰 9천원대", "📦 병"]),
    c_prod(3, "0201", HOTTEOK, "찹쌀<br>호떡믹스", ["백설 찹쌀 호떡믹스", "400g 구성", "호떡누르개 포함"],
           ["💰 9천원대", "📦 믹스+누르개"]),
    c_howto("0199~0201"),
], {
    "title": "칼바람 저녁 겨울 간식 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

영하권 추위에 강풍까지 🌬 칼바람 저녁 겨울 간식 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 파머스넷 세척 무농약 꿀고구마 💛 품번 0199
씻어 나와서 바로 굽거나 찌기 좋아요.

2. 고흥식품 통 유자차 💛 품번 0200
뜨거운 물에 한 스푼, 따뜻한 차 한 잔.

3. 백설 찹쌀 호떡믹스 400g + 호떡누르개 세트 💛 품번 0201
누르개까지 들어 있어 집에서 호떡 굽기.

✔ 24일 아침 최저 영하 6도~영상 7도, 강한 바람에 체감온도 더 낮아 — 추위는 25일까지

※ 날씨: 기상청 예보(세계일보 11/23)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #겨울간식 #고구마 #유자차 #호떡""",
    "products": [prod(1, SWEET, N_SWEET, "C", "0199"), prod(2, YUJA, N_YUJA, "C", "0200"), prod(3, HOTTEOK, N_HOTTEOK, "C", "0201")],
})
print("ok")
