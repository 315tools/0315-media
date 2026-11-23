"""2026-11-23(월, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-23/{A,B,C,A2,B2,C2}
점심: 월요일 아침 영하 4도·오후 전국 비·눈 → 비·눈 출근길 생활템 / 퇴근길: 난방비 줄이는 집 세팅(20도·습도 40~60%) → 온습도계·보온매트·문틈막이
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-23"
DL = "2026.11.23 (월)"
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


SPRAY, SILICA, TUMB = "7434490441", "8314586681", "9520614727"
THERMO, MAT, SEAL = "9642046260", "9806143283", "9749507906"
N_SPRAY = "콜로닐 워터스탑 신발 방수 스프레이"
N_SILICA = "크로반 실리카겔 제습제 (신발·의류·서랍장용)"
N_TUMB = "하토르 듀얼리드 스테인리스 진공 보온보냉 텀블러 500ml"
N_THERMO = "아이리버 디지털 미니 온습도계 ITH-100"
N_MAT = "두께 10mm 바닥 단열 PE 보온매트"
N_SEAL = "오렌 D형 문틈 틈새막이 (그레이)"

# ═════════ A · 점심 12:00 — 월요일 영하 4도, 오후 전국 비·눈 ═════════
SRC1 = "출처: 스페셜타임스(11/22) — 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 출근길</div>
<h1>월요일 아침 <span class="hl">영하 4도</span><br>오후엔 전국 비·눈</h1>
<p class="lead">강원 산지엔 눈, 바람도 강해요<br>퇴근길 우산 꼭 챙기세요</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(23일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침</small><strong>-4~4도</strong></div><div><small>전국 낮</small><strong>7~15도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>1도</strong></div><div><small>서울 낮</small><strong>9도</strong></div></div>
<div class="box">남부지방은 일교차 <b class="hl">15도 안팎</b><br>당분간 아침 영하권 이어져요</div>""", SRC1, DL),
    a_slide(3, n, """<h2>비·눈 <span class="hl">언제·얼마나</span></h2>
<ul class="chk"><li>오전 수도권·강원부터 → <span class="hl">오후 전국</span></li><li>수도권·강원내륙·제주 5~20mm</li><li>강원북부내륙·산지 눈 1~5cm</li><li>중부는 늦은 밤 대부분 그쳐요</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>바람도 <span class="hl">강해요</span></h2>
<div class="fig"><div><small>전국 순간풍속</small><strong>55km/h</strong></div><div><small>산지·충남서해안</small><strong>70km/h</strong></div></div>
<div class="box">충남서해안 <b class="hl">강풍특보</b> 가능성<br>미세먼지는 '좋음'~'보통'</div>""", SRC1, DL),
    a_slide(5, n, f"""<h2>비·눈 출근길 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SPRAY)}"><div>콜로닐 워터스탑<span>신발 방수 스프레이</span></div></li>
<li><b>2</b><img src="{img(SILICA)}"><div>크로반 실리카겔 제습제<span>신발·의류·서랍장용</span></div></li>
<li><b>3</b><img src="{img(TUMB)}"><div>하토르 보온 텀블러<span>진공 보온보냉 · 500ml</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/23 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "월요일 영하 4도, 오후 전국 비·눈",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 월요일 아침 영하 4도 🥶 오후엔 전국에 비·눈, 바람도 강해요

· 23일(월) 전국 아침 -4~4도, 낮 7~15도 — 서울 아침 1도·낮 9도, 춘천 -1도, 대전 0도, 대구 -1도, 부산 3도
· 남부지방은 낮과 밤 기온 차가 15도 안팎
· 비는 오전 수도권·강원내륙·산지·충남북서부에서 시작해 오후 전국으로, 경기북부·강원내륙·산지는 눈 오는 곳도
· 예상 강수량: 수도권·강원내륙·산지·제주 5~20mm, 충청·전라·대구·경북 5~10mm
· 강원북부내륙·산지 눈 1~5cm
· 순간풍속 시속 55km 안팎, 산지 70km 안팎 — 충남서해안은 강풍특보 가능성
· 미세먼지는 전 권역 '좋음'~'보통'
· 중부는 늦은 밤 대부분 그치고, 남부는 24일 이른 새벽, 제주는 24일 오전까지

✔ 퇴근길 우산 챙기기, 젖은 길·다리 위 미끄럼 조심
✔ 젖은 신발은 바로 말려두기

🔗 비·눈 출근길 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 스페셜타임스(11/22) — 기상청 예보

#광고 #생활뉴스 #날씨 #출근길 #비소식 #첫눈 #방수스프레이 #생활용품""",
    "products": [prod(1, SPRAY, N_SPRAY, "A"), prod(2, SILICA, N_SILICA, "A"), prod(3, TUMB, N_TUMB, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 난방비 줄이는 집 세팅 ═════════
SRC2 = "출처: 국제뉴스(11/1)·위키트리(11/20) — 한국에너지공단"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 난방비</div>
<h1>보일러 <span class="hl">20도</span><br>습도 <span class="hl">40~60%</span></h1>
<p class="lead">난방비 줄이는<br>겨울 집 세팅</p>""", SRC2, DL),
    a_slide(2, n, """<h2>실내 <span class="hl">온도</span></h2>
<div class="fig"><div><small>겨울 권장 실내온도</small><strong>20도</strong></div><div><small>1도 낮추면</small><strong>약 7%↓</strong></div></div>
<div class="box">20도를 넘기면 에너지<br><b class="hl">최대 20%</b>까지 더 써요<br><small>한국에너지공단 자료</small></div>""", SRC2, DL),
    a_slide(3, n, """<h2>보일러 <span class="hl">체크</span></h2>
<ul class="chk"><li>외출 땐 끄지 말고 <span class="hl">외출모드</span>·1~2도 낮게</li><li>안 쓰는 방은 분배기 밸브 잠그기</li><li>수도 레버는 <span class="hl">냉수 쪽</span>으로</li><li>보일러 안전점검 연 1회 이상</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>외풍·바닥 <span class="hl">막기</span></h2>
<ul class="chk"><li>습도 40~60%면 <span class="hl">덜 춥게</span> 느껴요</li><li>문풍지·에어캡으로 틈새 차단</li><li>두꺼운 커튼·러그 깔기</li><li>내복·덧신으로 체감온도 올리기</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>난방비 줄이는 <span class="hl">집 세팅템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(THERMO)}"><div>아이리버 미니 온습도계<span>온도·습도 한눈에</span></div></li>
<li><b>2</b><img src="{img(MAT)}"><div>바닥 단열 보온매트<span>두께 10mm · 냉기 차단</span></div></li>
<li><b>3</b><img src="{img(SEAL)}"><div>오렌 D형 문틈막이<span>틈새 외풍 차단</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/23 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "난방비 줄이는 겨울 집 세팅",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 보일러 20도, 습도 40~60% 🏠 난방비 줄이는 겨울 집 세팅

· 한국에너지공단 기준 겨울철 권장 실내온도 20도, 1도 낮추면 에너지 소비 약 7% 감소 (국제뉴스 11/1)
· 난방 온도가 20도를 넘으면 그렇지 않을 때보다 에너지를 최대 20%까지 더 씀 — 한국에너지공단 자료 (위키트리 11/20)
· 실내 습도 40~60%를 유지하면 덜 춥게 느껴져요
· 외출할 땐 보일러를 끄기보다 외출모드나 1~2도 낮게
· 안 쓰는 방은 분배기 밸브 잠그기 (에너지공단 기준 약 4.4% 절감)
· 수도 레버는 쓰고 나서 냉수 쪽으로 — 온수 쪽에 두면 보일러가 돌 수 있어요
· 문풍지·에어캡으로 틈새 막고, 커튼·러그·내복·덧신으로 체감온도 올리기
· 보일러는 연 1회 이상 안전점검 (가스안전공사)

🔗 난방비 줄이는 집 세팅템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 국제뉴스(11/1)·위키트리(11/20) — 한국에너지공단·가스안전공사 자료 인용

#광고 #생활뉴스 #난방비 #난방비절약 #겨울준비 #온습도계 #문풍지 #생활용품""",
    "products": [prod(1, THERMO, N_THERMO, "A"), prod(2, MAT, N_MAT, "A"), prod(3, SEAL, N_SEAL, "A")],
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


write(DATE, "B", [poll("비·눈 오는 월요일,<br>오늘 신발은? ☔", "23일 오후 전국 비, 강원 산지는 눈 (기상청 예보)",
                       [("그냥 운동화", "젖으면 젖는 대로"), ("장화 출격", "오늘을 위해 샀다"),
                        ("마음은 이미 재택", "출근 자체가 고민"), ("방수 스프레이", "칙칙 뿌리고 출발")], SPRAY)], {
    "title": "비·눈 오는 월요일 신발 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 비·눈 오는 월요일, 오늘 신발은? ☔
댓글에 번호로 투표해주세요!

1️⃣ 그냥 운동화
2️⃣ 장화 출격
3️⃣ 마음은 이미 재택
4️⃣ 방수 스프레이

※ 23일(월) 오전 수도권·강원부터 비, 오후 전국으로 — 강원북부내륙·산지 눈 1~5cm (기상청 예보, 스페셜타임스 11/22)

🔗 4번 콜로닐 워터스탑 방수 스프레이 링크는 프로필에
👥 비 오는 날 꼭 흰 운동화 신는 친구 태그

#광고 #투표 #공감 #월요일 #비소식 #방수스프레이""",
    "products": [prod(1, SPRAY, N_SPRAY, "B")],
})

write(DATE, "B2", [poll("우리 집 겨울<br>실내온도는? 🌡️", "겨울 권장 실내온도 20도 (한국에너지공단)",
                        [("18도 이하", "내복은 필수"), ("딱 20도", "모범 가정"),
                         ("24도 이상", "집에선 반팔"), ("몇 도인지 모름", "온습도계부터")], THERMO)], {
    "title": "우리 집 겨울 실내온도 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 우리 집 겨울 실내온도는? 🌡️
댓글에 번호로 투표해주세요!

1️⃣ 18도 이하
2️⃣ 딱 20도
3️⃣ 24도 이상
4️⃣ 몇 도인지 모름

※ 한국에너지공단 기준 겨울 권장 실내온도 20도, 1도 낮추면 에너지 소비 약 7% 감소 (국제뉴스 11/1)

🔗 4번 아이리버 미니 온습도계 링크는 프로필에
👥 보일러 온도로 매일 싸우는 가족 태그

#광고 #투표 #공감 #난방비 #실내온도 #온습도계""",
    "products": [prod(1, THERMO, N_THERMO, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/23 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("월요일 오후 전국 비·눈", "비·눈 오는 날", "출근길 생활템", "BEST3", [SPRAY, SILICA, TUMB]),
    c_prod(1, "0190", SPRAY, "콜로닐<br>워터스탑", ["신발에 뿌리는 방수 스프레이", "외출 전 미리 뿌려두기", "쓸 수 있는 소재는 상품 페이지 확인"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_prod(2, "0191", SILICA, "크로반<br>실리카겔 제습제", ["실리카겔 습기제거제", "신발·의류·서랍장용", "젖은 신발장 습기 관리"],
           ["💰 8천원대", "🚀 로켓배송"]),
    c_prod(3, "0192", TUMB, "하토르<br>보온 텀블러", ["스테인리스 진공 보온보냉", "뚜껑 2종 듀얼리드", "500ml · 웜 그레이"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_howto("0190~0192"),
], {
    "title": "비·눈 출근길 생활템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

월요일 아침 영하 4도, 오후엔 전국 비·눈 ☔ 비·눈 출근길 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 콜로닐 워터스탑 신발 방수 스프레이 💛 품번 0190
외출 전 신발에 뿌려두는 방수 스프레이. 쓸 수 있는 소재는 상품 페이지에서 확인하세요.

2. 크로반 실리카겔 제습제 💛 품번 0191
신발·의류·서랍장에 넣어 쓰는 실리카겔 습기제거제.

3. 하토르 듀얼리드 보온보냉 텀블러 500ml 💛 품번 0192
뚜껑 2종이 들어 있는 스테인리스 진공 텀블러.

✔ 방수 스프레이는 환기되는 곳에서 뿌리고 충분히 말린 뒤 신기

※ 날씨: 23일(월) 전국 아침 -4~4도, 오후 전국 비 — 기상청(스페셜타임스 11/22 보도)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #방수스프레이 #신발제습제 #보온텀블러 #비소식""",
    "products": [prod(1, SPRAY, N_SPRAY, "C", "0190"), prod(2, SILICA, N_SILICA, "C", "0191"), prod(3, TUMB, N_TUMB, "C", "0192")],
})

write(DATE, "C2", [
    c_cover("보일러 20도·습도 40~60%", "난방비 줄이는", "집 세팅템", "BEST3", [THERMO, MAT, SEAL]),
    c_prod(1, "0193", THERMO, "아이리버<br>미니 온습도계", ["실내 온도·습도 한눈에", "20도·40~60% 확인용", "ITH-100 · 화이트"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_prod(2, "0194", MAT, "바닥 단열<br>보온매트", ["두께 10mm PE 매트", "바닥 냉기 차단용", "거실·방"],
           ["💰 2만원대", "🚚 무료배송"]),
    c_prod(3, "0195", SEAL, "오렌<br>D형 문틈막이", ["문틈 틈새막이", "외풍·소음 차단용", "그레이"],
           ["💰 3천원대", "🚀 로켓배송"]),
    c_howto("0193~0195"),
], {
    "title": "난방비 줄이는 집 세팅템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

보일러 20도, 습도 40~60% 🏠 난방비 줄이는 집 세팅템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 아이리버 디지털 미니 온습도계 ITH-100 💛 품번 0193
실내 온도와 습도를 한눈에 보는 미니 온습도계.

2. 두께 10mm 바닥 단열 PE 보온매트 💛 품번 0194
거실·방 바닥 냉기를 막는 10mm 보온매트. 사이즈는 상품 페이지에서 확인하세요.

3. 오렌 D형 문틈 틈새막이 💛 품번 0195
문틈에 붙여 외풍을 막는 D형 틈새막이.

✔ 붙이기 전 문틀 먼지·물기 닦아내기

※ 겨울 권장 실내온도 20도, 1도 낮추면 에너지 소비 약 7% 감소 — 한국에너지공단(국제뉴스 11/1 보도)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #난방비절약 #온습도계 #보온매트 #문풍지""",
    "products": [prod(1, THERMO, N_THERMO, "C", "0193"), prod(2, MAT, N_MAT, "C", "0194"), prod(3, SEAL, N_SEAL, "C", "0195")],
})
print("ok")
