"""2026-11-21(토, 소형가전의 날) 게시물 6개 → docs/posts/2026-11-21/{A,B,C,A2,B2,C2}
점심: 토요일 아침 영하 8도 강추위·강풍 → 몸 녹이는 방한 가전 / 퇴근길: 난방온도 1도 낮추면 에너지 7% 절약 → 보조 난방·습도 가전
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-21"
DL = "2026.11.21 (토)"
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


FOOT, CUSH, HEAT = "9178700071", "7658093689", "7648527343"
MAT, CIRC, HUM = "9801959597", "8551060597", "8974720992"
N_FOOT = "이놀 3단 전기 발난로 풋워머 100W (양모 극세사)"
N_CUSH = "디누스 탄소 1인용 전기방석 HE-HP01 (44x44cm)"
N_HEAT = "쿠쿠 카본 히터"
N_MAT = "한일의료기 오브휴 이중열선 탄소 전기요 HL-S210 (100x180cm)"
N_CIRC = "아이리스 저소음 컴팩트 에어 써큘레이터"
N_HUM = "NINESPEED 12L 대용량 초음파 가습기 (자동습도조절·UV살균)"

# ═════════ A · 점심 12:00 — 토요일 아침 영하 강추위 ═════════
SRC1 = "출처: 경향신문(11/21), 아시아경제·이투데이(11/20), 기상청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 주말</div>
<h1>토요일 아침<br><span class="hl">영하 8도</span> 강추위</h1>
<p class="lead">강한 바람에 체감온도 더 낮아요<br>일요일 낮부터 차차 풀려요</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(21일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침</small><strong>-8~3도</strong></div><div><small>전국 낮</small><strong>1~11도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>-5도</strong></div><div><small>서울 낮</small><strong>2도</strong></div></div>
<div class="box">평년(아침 -3~6도, 낮 8~15도)보다 낮아요<br>오전 8시 파주 <b class="hl">-8.9도</b> 관측</div>""", SRC1, DL),
    a_slide(3, n, """<h2>눈·비와 <span class="hl">바람</span></h2>
<ul class="chk"><li>충남·전라·제주 중심 비 또는 눈</li><li>제주 산지 대설주의보, 2~7cm 적설</li><li>전국 대부분 시속 55km 이상 <span class="hl">강한 바람</span></li><li>강원영동·경북북동부 건조특보</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>주말 <span class="hl">추위 대비</span></h2>
<ul class="chk"><li>눈·비 온 곳은 <span class="hl">빙판길</span> 조심</li><li>외출은 겹쳐 입고 목·손 감싸기</li><li>건조한 지역은 불조심</li><li>22일(일) 아침 -9~0도, 낮 4~10도</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>언 몸 녹이는 <span class="hl">방한 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FOOT)}"><div>이놀 전기 발난로<span>3단 · 양모 극세사 풋워머</span></div></li>
<li><b>2</b><img src="{img(CUSH)}"><div>디누스 탄소 전기방석<span>1인용 · 44x44cm</span></div></li>
<li><b>3</b><img src="{img(HEAT)}"><div>쿠쿠 카본 히터<span>거실·방 보조 난방</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/21 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "토요일 아침 영하 8도 강추위",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 토요일 아침 영하 8도 강추위 🥶 일요일 낮부터 차차 풀려요

· 21일(토) 전국 아침 -8~3도, 낮 1~11도 — 평년(아침 -3~6도, 낮 8~15도)보다 낮아요
· 서울 아침 -5도·낮 2도 예보, 오전 8시 서울 -4.7도·파주 -8.9도 관측
· 전국 대부분 시속 55km 이상 강한 바람 → 체감온도는 더 낮아요
· 충남·전라·제주 중심 비 또는 눈, 제주 산지(대설주의보) 2~7cm 적설
· 강원영동·경북북동부 건조특보, 서울·경기북동부·강원영서도 건조
· 22일(일) 아침 -9~0도, 낮 4~10도 — 낮부터 점차 풀리고 다음 주엔 평년 기온

✔ 눈·비 온 곳은 빙판길·도로 살얼음 조심
✔ 건조한 지역은 산불 등 화재 예방

🔗 언 몸 녹이는 방한 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 경향신문(11/21), 아시아경제·이투데이(11/20) — 기상청 예보

#광고 #생활뉴스 #날씨 #강추위 #주말날씨 #발난로 #전기방석 #소형가전""",
    "products": [prod(1, FOOT, N_FOOT, "A"), prod(2, CUSH, N_CUSH, "A"), prod(3, HEAT, N_HEAT, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 난방온도 1도 낮추면 7% 절약 ═════════
SRC2 = "출처: 전기신문(11/17), 헤럴드경제(11/19), 한국에너지공단"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 난방비</div>
<h1>난방온도 <span class="hl">1도</span>만<br>낮춰도 7% 절약</h1>
<p class="lead">겨울철 적정 실내온도는 20도<br>보일러 회사가 알려준 습관</p>""", SRC2, DL),
    a_slide(2, n, """<h2>1도의 <span class="hl">차이</span></h2>
<div class="fig"><div><small>적정 실내온도</small><strong>20도</strong></div><div><small>1도 낮추면</small><strong>약 7%↓</strong></div></div>
<div class="box">정부 안내: 난방온도 1도 낮추면<br>월 <b class="hl">5,203원</b> 에너지 비용 절약<br><small>단열·난방 방식에 따라 달라요</small></div>""", SRC2, DL),
    a_slide(3, n, """<h2>외출할 땐 <span class="hl">끄지 말고</span></h2>
<ul class="chk"><li>설정온도만 낮추기 (1~3도)</li><li>다시 데우는 데 에너지가 더 들어요</li><li>외출모드는 오래 비울 때</li><li>외풍 심한 집은 '온돌' 모드</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>집에서 <span class="hl">따뜻하게</span></h2>
<ul class="chk"><li>내복·수면양말·카디건</li><li>바닥엔 러그·카펫</li><li>창문엔 에어캡·문풍지</li><li>환기 뒤 <span class="hl">실내 습도</span> 살피기</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>보일러 옆 <span class="hl">겨울 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(MAT)}"><div>한일 오브휴 전기요<span>이중열선 탄소 · 100x180cm</span></div></li>
<li><b>2</b><img src="{img(CIRC)}"><div>아이리스 써큘레이터<span>저소음 · 컴팩트</span></div></li>
<li><b>3</b><img src="{img(HUM)}"><div>NINESPEED 가습기<span>12L 대용량 · 자동습도조절</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/21 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "난방온도 1도 낮추면 7% 절약",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 난방온도 1도만 낮춰도 에너지 약 7% 절약 🔥 보일러 회사가 알려준 습관

· 한국에너지공단 권장 겨울철 적정 실내 난방온도 20도
· 난방온도 1도 낮추면 에너지 소비량 약 7% 절감 (한국에너지공단)
· 정부 '2026년 겨울철 에너지절약 실천요령': 1도 낮추면 월 5,203원 절약 — 단열·난방 방식에 따라 달라요
· 외출할 땐 보일러를 끄기보다 설정온도만 낮추기 (경동나비엔 1~2도, 귀뚜라미 2~3도 권장)
· 외출모드는 오래 집을 비울 때 (경동나비엔 일주일 이상, 귀뚜라미 하루 이상)
· 단열 좋은 집은 '실내온도' 모드, 외풍 심한 집은 '온돌' 모드

✔ 내복·수면양말·카디건, 바닥엔 러그
✔ 창문엔 에어캡·문풍지, 환기 뒤엔 실내 습도도 살피기

🔗 보일러 옆 겨울 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 전기신문(11/17)·헤럴드경제(11/19) — 한국에너지공단·경동나비엔·귀뚜라미

#광고 #생활뉴스 #난방비 #난방비절약 #겨울 #전기요 #가습기 #소형가전""",
    "products": [prod(1, MAT, N_MAT, "A"), prod(2, CIRC, N_CIRC, "A"), prod(3, HUM, N_HUM, "A")],
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


write(DATE, "B", [poll("영하 8도 토요일,<br>제일 먼저 시린 곳은? 🥶", "토요일 아침 -8~3도, 강한 바람 (기상청 예보)",
                       [("손", "주머니에서 안 나와"), ("귀·코", "빨개지는 건 순식간"),
                        ("목", "목도리 없인 못 나가"), ("발끝", "발난로에 쏙 넣고 싶다")], FOOT)], {
    "title": "제일 먼저 시린 곳 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 영하 8도 토요일, 제일 먼저 시린 곳은? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 손
2️⃣ 귀·코
3️⃣ 목
4️⃣ 발끝

※ 21일(토) 전국 아침 -8~3도, 서울 -5도 예보 + 시속 55km 이상 강한 바람 (기상청 예보, 아시아경제·이투데이 11/20)

🔗 4번 이놀 전기 발난로 링크는 프로필에
👥 겨울만 되면 발이 얼음장인 친구 태그

#광고 #투표 #공감 #강추위 #발난로 #겨울""",
    "products": [prod(1, FOOT, N_FOOT, "B")],
})

write(DATE, "B2", [poll("겨울밤 우리 집<br>보일러 온도는? 🔥", "적정 실내온도 20도, 1도 낮추면 약 7% 절약 (한국에너지공단)",
                        [("20도 이하", "내복으로 버틴다"), ("21~23도", "적당히 따뜻하게"),
                         ("24도 이상", "겨울엔 반팔이지"), ("낮추고 전기요", "등만 따뜻하면 OK")], MAT)], {
    "title": "우리 집 보일러 온도 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 겨울밤 우리 집 보일러 온도는? 🔥
댓글에 번호로 투표해주세요!

1️⃣ 20도 이하
2️⃣ 21~23도
3️⃣ 24도 이상
4️⃣ 낮추고 전기요

※ 겨울철 적정 실내온도 20도, 난방온도 1도 낮추면 에너지 약 7% 절감 (한국에너지공단, 전기신문 11/17)

🔗 4번 한일의료기 오브휴 전기요 링크는 프로필에
👥 보일러 온도로 매일 다투는 사람 태그

#광고 #투표 #공감 #난방비 #보일러 #전기요""",
    "products": [prod(1, MAT, N_MAT, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/21 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("토요일 아침 영하 8도", "언 몸 녹이는", "방한 가전", "BEST3", [FOOT, CUSH, HEAT]),
    c_prod(1, "0178", FOOT, "이놀<br>전기 발난로", ["3단 온도 조절 풋워머", "양모 극세사 안감", "100W"],
           ["💰 3만원대", "🚀 로켓배송"]),
    c_prod(2, "0179", CUSH, "디누스<br>탄소 전기방석", ["1인용 탄소 전기방석", "의자·바닥에 깔기", "HE-HP01 · 44x44cm"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0180", HEAT, "쿠쿠<br>카본 히터", ["카본 전기 히터", "거실·방 보조 난방", "쿠쿠 브랜드"],
           ["💰 6만원대", "🚀 로켓배송"]),
    c_howto("0178~0180"),
], {
    "title": "언 몸 녹이는 방한 가전 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

토요일 아침 영하 8도 🥶 언 몸 녹이는 방한 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 이놀 3단 전기 발난로 풋워머 100W (양모 극세사) 💛 품번 0178
발을 쏙 넣는 3단 조절 전기 발난로.

2. 디누스 탄소 1인용 전기방석 HE-HP01 (44x44cm) 💛 품번 0179
의자나 바닥에 까는 1인용 탄소 전기방석.

3. 쿠쿠 카본 히터 💛 품번 0180
거실·방 보조 난방용 카본 히터.

✔ 난방기구는 주변 물건 치우고, 외출·취침 땐 전원 끄기

※ 날씨: 21일(토) 전국 아침 -8~3도 — 기상청(경향신문 11/21·아시아경제·이투데이 11/20 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #발난로 #전기방석 #카본히터 #강추위""",
    "products": [prod(1, FOOT, N_FOOT, "C", "0178"), prod(2, CUSH, N_CUSH, "C", "0179"), prod(3, HEAT, N_HEAT, "C", "0180")],
})

write(DATE, "C2", [
    c_cover("난방온도 1도 낮추면 7% 절약", "보일러 옆", "겨울 가전", "BEST3", [MAT, CIRC, HUM]),
    c_prod(1, "0181", MAT, "한일의료기<br>오브휴 전기요", ["이중열선 탄소 전기요", "100x180cm", "HL-S210"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(2, "0182", CIRC, "아이리스<br>써큘레이터", ["저소음 컴팩트 써큘레이터", "실내 공기 순환", "작은 크기"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0183", HUM, "NINESPEED<br>12L 가습기", ["12L 대용량 초음파", "자동 습도 조절", "UV살균"],
           ["💰 7만원대", "🚀 로켓배송"]),
    c_howto("0181~0183"),
], {
    "title": "보일러 옆 겨울 가전 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

난방온도 1도 낮추면 에너지 약 7% 절약 🔥 보일러 옆 겨울 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 한일의료기 오브휴 이중열선 탄소 전기요 HL-S210 (100x180cm) 💛 품번 0181
이중열선 탄소 전기요.

2. 아이리스 저소음 컴팩트 에어 써큘레이터 💛 품번 0182
실내 공기를 돌려주는 컴팩트 써큘레이터.

3. NINESPEED 12L 대용량 초음파 가습기 (자동습도조절·UV살균) 💛 품번 0183
자동 습도 조절이 되는 12L 초음파 가습기.

✔ 가습기 물통은 자주 비우고 씻어서 쓰기

※ 적정 실내온도 20도·1도 낮추면 약 7% 절감 — 한국에너지공단(전기신문 11/17·헤럴드경제 11/19 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #전기요 #써큘레이터 #가습기 #난방비""",
    "products": [prod(1, MAT, N_MAT, "C", "0181"), prod(2, CIRC, N_CIRC, "C", "0182"), prod(3, HUM, N_HUM, "C", "0183")],
})
print("ok")
