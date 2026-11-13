"""2026-11-13(금, 식품의 날) 게시물 6개 → docs/posts/2026-11-13/{A,B,C,A2,B2,C2}
점심: 수능 D-6 컨디션은 수면·식사 → 가벼운 아침·간식 / 퇴근길: 오늘 밤~토요일 전국 비 → 비 오는 주말 부침개
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-13"
DL = "2026.11.13 (금)"
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





NUT, PUMP, BARLEY = "9366950331", "8013400397", "6138531422"
FLOUR, PAJEON, NOKDU = "1510131644", "8626762125", "8969593560"
N_NUT = "투데이넛 너트한줌 클래식 30p"
N_PUMP = "죽이야기 짜먹는 단호박죽 7p"
N_BARLEY = "동서 한잔용 보리차"
N_FLOUR = "CJ 백설 부침가루 1kg + 튀김가루 1kg"
N_PAJEON = "사옹원 프리미엄 해물파전 (냉동)"
N_NOKDU = "풀무원 철판 도톰 녹두전 (냉동)"

# ═════════ A · 점심 12:00 — 수능 D-6 컨디션 관리 ═════════
SRC1 = "출처: 의약일보(11/12) — 박효진 한림대강남성심병원 교수"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">식품 · 수능 D-6</div>
<h1>수능 일주일 앞<br>컨디션은 <span class="hl">수면·식사</span></h1>
<p class="lead">19일(목) 수능<br>남은 기간 생활 리듬 체크</p>""", SRC1, DL),
    a_slide(2, n, """<h2><span class="hl">수면</span>은 이렇게</h2>
<div class="box">시험 당일 <b class="hl">기상 시간</b>에 맞춰<br>일정한 시간에 자고 일어나기</div>
<div class="box">시험 직전 갑자기 수면 시간 바꾸기·<br>밤늦게까지 공부는 <b class="hl">피하기</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2><span class="hl">식사</span>는 이렇게</h2>
<ul class="chk"><li>기름진 음식보다 <span class="hl">소화 잘되는 음식</span></li><li>규칙적으로, <span class="hl">적당량</span></li><li>아침 안 먹었다면 <span class="hl">조금씩 적응</span></li><li>안 먹던 보양식·영양제는 새로 시작 X</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>긴장될 땐 <span class="hl">가볍게</span></h2>
<ul class="chk"><li>가벼운 <span class="hl">산책·스트레칭</span></li><li><span class="hl">심호흡</span>으로 긴장 풀기</li><li>시험 직전 운동량 급증은 피하기</li><li>수면제·안정제 <span class="hl">임의 복용 X</span></li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>가벼운 <span class="hl">아침·간식</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(NUT)}"><div>하루 견과 한 줌<span>30봉 · 한 봉씩 소포장</span></div></li>
<li><b>2</b><img src="{img(PUMP)}"><div>짜먹는 단호박죽<span>7개입 · 파우치형</span></div></li>
<li><b>3</b><img src="{img(BARLEY)}"><div>한잔용 보리차<span>티백 · 따뜻하게</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/13 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "수능 D-6 컨디션은 수면·식사",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 수능 일주일 앞 📚 컨디션 관리는 수면과 식사가 중요

· 19일(목) 2027학년도 수능
· 수면: 시험 당일 기상 시간에 맞춰 일정한 시간에 자고 일어나기
· 시험 직전 갑자기 수면 시간을 바꾸거나 밤늦게까지 공부하는 건 피하기
· 식사: 기름진 음식보다 소화가 잘되는 음식을 규칙적으로 적당량
· 아침을 안 먹던 수험생은 당일 갑자기 많이 먹지 말고 남은 기간 조금씩 적응
· 평소 먹지 않던 보양식·영양제·건강기능식품을 새로 시작하기보다 익숙한 식사 유지
· 긴장될 땐 가벼운 산책·스트레칭·심호흡, 수면제·안정제 임의 복용은 삼가기

✔ 새 음식보다 평소 먹던 것으로
✔ 당일 기상 시간에 맞춰 생활 리듬 맞추기

🔗 가벼운 아침·간식 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 의약일보(2026.11.12) — 박효진 한림대강남성심병원 가정의학과 교수

#광고 #생활뉴스 #수능 #수험생 #수능D6 #수험생간식 #하루견과""",
    "products": [prod(1, NUT, N_NUT, "A"), prod(2, PUMP, N_PUMP, "A"), prod(3, BARLEY, N_BARLEY, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 오늘 밤~토요일 전국 비 ═════════
SRC2 = "출처: 매일일보(11/12)·월요신문(11/13) — 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">식품 · 주말</div>
<h1>오늘 남부부터<br><span class="hl">토요일 전국 비</span></h1>
<p class="lead">낮엔 최고 20도 포근<br>비 오는 주말 대비</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘(13일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>2~10도</strong></div><div><small>전국 낮 최고</small><strong>15~20도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>8도</strong></div><div><small>서울 낮</small><strong>17도</strong></div></div>
<div class="box">평년과 비슷하거나 <b class="hl">조금 높아요</b></div>""", SRC2, DL),
    a_slide(3, n, """<h2>비 <span class="hl">언제부터?</span></h2>
<ul class="chk"><li>13일 늦은 오후 <span class="hl">전남 해안·제주</span></li><li>13일 밤 호남·충청·경상 서부</li><li>14일 새벽 <span class="hl">인천·경기 남부</span>·강원 남부</li><li>14일 오전 <span class="hl">나머지 중부</span></li></ul>
<div class="box">중부·전북은 <b class="hl">14일 밤</b> 그쳐요</div>""", SRC2, DL),
    a_slide(4, n, """<h2>예상 <span class="hl">강수량</span> (13~14일)</h2>
<div class="fig"><div><small>제주</small><strong>10~60mm</strong></div><div><small>광주전남·부울경</small><strong>10~40mm</strong></div></div>
<div class="fig"><div><small>충청·전북·대구경북</small><strong>5~30mm</strong></div><div><small>경기 남부·강원</small><strong>5~10mm</strong></div></div>
<div class="box">서울·인천·경기 북부 <b class="hl">5mm 안팎</b></div>""", "출처: 매일일보(11/12) — 기상청 예보", DL),
    a_slide(5, n, f"""<h2>비 오는 주말 <span class="hl">부침개</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FLOUR)}"><div>부침가루 + 튀김가루<span>각 1kg 세트</span></div></li>
<li><b>2</b><img src="{img(PAJEON)}"><div>냉동 해물파전<span>데우기만 · 로켓프레시</span></div></li>
<li><b>3</b><img src="{img(NOKDU)}"><div>철판 도톰 녹두전<span>냉동 · 로켓프레시</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/13 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "오늘 남부부터 토요일 전국 비",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 오늘 낮 최고 20도 포근 ☁️ 늦은 오후 남부부터 비, 토요일 전국으로 ☔

· 13일(금) 아침 2~10도, 낮 15~20도 (서울 8도·17도)
· 13일 늦은 오후 전남 해안·제주부터 비 → 밤 호남·충청·경상 서부
· 14일(토) 새벽 인천·경기 남부·강원 남부, 오전 나머지 중부
· 그치는 때: 중부·전북 14일 밤, 전남 동부·영남 15일 새벽, 제주 15일 아침
· 예상 강수량(13~14일): 제주 10~60mm, 광주·전남·부산·울산·경남 10~40mm, 충청·전북·대구·경북 5~30mm, 경기 남부·강원 5~10mm, 서울·인천·경기 북부 5mm 안팎

✔ 토요일 외출엔 우산 챙기기
✔ 비 오는 주말 장보기는 미리

🔗 비 오는 주말 부침개 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 매일일보(2026.11.12)·월요신문(2026.11.13) — 기상청 예보

#광고 #생활뉴스 #주말날씨 #비소식 #부침개 #해물파전 #녹두전""",
    "products": [prod(1, FLOUR, N_FLOUR, "A"), prod(2, PAJEON, N_PAJEON, "A"), prod(3, NOKDU, N_NOKDU, "A")],
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





write(DATE, "B", [poll("수능 D-6,<br>수험생 간식은? 📚", "19일(목) 수능 · 평소 먹던 걸로 가볍게",
                       [("초콜릿 몇 조각", "당 충전은 이걸로"), ("찹쌀떡", "붙어라 붙어라"),
                        ("따뜻한 차 한 잔", "속 편한 게 최고"), ("견과 한 줌", "한 봉씩 톡 뜯어서")], NUT)], {
    "title": "수험생 간식 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 수능 D-6, 수험생 간식은? 📚
댓글에 번호로 투표해주세요!

1️⃣ 초콜릿 몇 조각
2️⃣ 찹쌀떡
3️⃣ 따뜻한 차 한 잔
4️⃣ 견과 한 줌

※ 19일(목) 수능. 시험 앞두고는 평소 먹지 않던 음식보다 소화 잘되는 익숙한 음식이 좋아요 (의약일보 11/12)

🔗 4번 투데이넛 너트한줌 클래식 링크는 프로필에
👥 수능 보는 동생·친구 태그하고 응원 한마디

#광고 #투표 #공감 #수능 #수험생 #수험생간식""",
    "products": [prod(1, NUT, N_NUT, "B")],
})

write(DATE, "B2", [poll("비 오는 주말,<br>부침개는 뭐로? ☔", "13일 밤~14일(토) 전국 비 (기상청 예보)",
                        [("김치전", "바삭한 끝부분이 국룰"), ("감자전", "쫀득함이 최고"),
                         ("녹두전", "고소함은 이길 수 없지"), ("해물파전", "오징어·새우 듬뿍")], PAJEON)], {
    "title": "비 오는 주말 부침개 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 비 오는 주말, 부침개는 뭐로? ☔
댓글에 번호로 투표해주세요!

1️⃣ 김치전
2️⃣ 감자전
3️⃣ 녹두전
4️⃣ 해물파전

※ 13일(금) 늦은 오후 남부부터 비, 14일(토) 전국으로 확대 (기상청 예보, 매일일보 11/12·월요신문 11/13)

🔗 4번 사옹원 프리미엄 해물파전 링크는 프로필에
👥 주말에 같이 부침개 부쳐 먹을 사람 태그

#광고 #투표 #공감 #비오는날 #부침개 #주말""",
    "products": [prod(1, PAJEON, N_PAJEON, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/13 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("수능 D-6, 컨디션 관리", "수험생", "아침·간식", "BEST3", [NUT, PUMP, BARLEY]),
    c_prod(1, "0130", NUT, "너트한줌<br>하루 견과", ["한 봉씩 소포장", "30봉 구성", "가방에 쏙"],
           ["💰 1만6천원대", "🚀 로켓배송"]),
    c_prod(2, "0131", PUMP, "짜먹는<br>단호박죽", ["파우치형 단호박죽", "7개입", "아침 가볍게"],
           ["💰 1만3천원대", "🚀 로켓배송"]),
    c_prod(3, "0132", BARLEY, "한잔용<br>보리차", ["한 잔씩 티백", "따뜻하게 우려서", "구수한 보리차"],
           ["💰 5천원대", "🚀 로켓배송"]),
    c_howto("0130~0132"),
], {
    "title": "수험생 아침·간식 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

수능 D-6 📚 수험생 아침·간식 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 투데이넛 너트한줌 클래식 30p 💛 품번 0130
한 봉씩 소포장된 하루 견과, 30봉 구성.

2. 죽이야기 짜먹는 단호박죽 7p 💛 품번 0131
파우치에서 바로 짜먹는 단호박죽, 7개입.

3. 동서 한잔용 보리차 💛 품번 0132
한 잔씩 우려 마시는 티백 보리차.

✔ 시험 앞두곤 새 음식보다 평소 먹던 걸로, 소화 잘되게

※ 수험생 컨디션: 의약일보(11/12)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #수능 #수험생간식 #하루견과 #단호박죽""",
    "products": [prod(1, NUT, N_NUT, "C", "0130"), prod(2, PUMP, N_PUMP, "C", "0131"), prod(3, BARLEY, N_BARLEY, "C", "0132")],
})

write(DATE, "C2", [
    c_cover("토요일 전국 비 ☔", "비 오는 주말", "부침개", "BEST3", [FLOUR, PAJEON, NOKDU]),
    c_prod(1, "0133", FLOUR, "부침가루<br>+ 튀김가루", ["부침가루 1kg", "튀김가루 1kg", "집에서 직접 부치기"],
           ["💰 8천원대", "🚚 무료배송"]),
    c_prod(2, "0134", PAJEON, "프리미엄<br>해물파전", ["냉동 해물파전", "팬에 데우기만", "로켓프레시"],
           ["💰 8천원대", "🚀 로켓배송"]),
    c_prod(3, "0135", NOKDU, "철판 도톰<br>녹두전", ["냉동 녹두전", "도톰한 두께", "로켓프레시"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0133~0135"),
], {
    "title": "비 오는 주말 부침개 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

토요일 전국 비 ☔ 비 오는 주말 부침개 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. CJ 백설 부침가루 1kg + 튀김가루 1kg 💛 품번 0133
부침가루·튀김가루 각 1kg 세트, 집에서 직접 부칠 때.

2. 사옹원 프리미엄 해물파전 (냉동) 💛 품번 0134
팬에 데워 먹는 냉동 해물파전.

3. 풀무원 철판 도톰 녹두전 (냉동) 💛 품번 0135
도톰하게 부친 냉동 녹두전.

✔ 냉동전은 제품 조리법대로 데워 드세요

※ 날씨: 기상청 예보(매일일보 11/12·월요신문 11/13)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #비오는날 #부침개 #해물파전 #녹두전""",
    "products": [prod(1, FLOUR, N_FLOUR, "C", "0133"), prod(2, PAJEON, N_PAJEON, "C", "0134"), prod(3, NOKDU, N_NOKDU, "C", "0135")],
})
print("ok")
