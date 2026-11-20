"""2026-11-20(금, 식품의 날) 게시물 6개 → docs/posts/2026-11-20/{A,B,C,A2,B2,C2}
점심: 11월 장바구니 물가(한국물가정보) 배추·달걀↓ 대구·생태↑ → 장보기 식품 / 퇴근길: 주말까지 강추위, 일요일 오후부터 풀림 → 뜨끈한 겨울 간식
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-20"
DL = "2026.11.20 (금)"
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


RICE, EGG, CHICK = "166996432", "9594066206", "9752054562"
JJIN, ODENG, TEA = "5498846415", "7324843040", "7300051253"
N_RICE = "곰곰 2026년산 햅쌀 소중한 우리쌀 상등급"
N_EGG = "젊은 닭 유정란 특대란 30구 (무항생제·난각번호 2번)"
N_CHICK = "하림 친환경 프레쉬업 무항생제 닭볶음탕용 900g"
N_JJIN = "본가 안흥찐빵 500g x 2봉 (20입)"
N_ODENG = "삼진어묵 오동통 모듬어묵 + 스프"
N_TEA = "우리차 쌍화차 110T"

# ═════════ A · 점심 12:00 — 11월 장바구니 물가 ═════════
SRC1 = "출처: 직썰·문화투데이(11/19) — 한국물가정보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 물가</div>
<h1>배추·달걀은 ↓<br><span class="hl">대구는 ↑</span></h1>
<p class="lead">11월 셋째 주<br>전통시장 장바구니</p>""", SRC1, DL),
    a_slide(2, n, """<h2>김장 채소 <span class="hl">내렸어요</span></h2>
<div class="fig"><div><small>배추 1포기</small><strong>4천원</strong></div><div><small>무 1개</small><strong>2천원</strong></div></div>
<div class="box">한 달 전보다 배추 <b class="hl">3천원</b>↓ · 무 <b class="hl">1천원</b>↓<br>일반미 8kg <b class="hl">2만8천원</b> (1천원↓)</div>""", SRC1, DL),
    a_slide(3, n, """<h2>닭고기·달걀도 <span class="hl">↓</span></h2>
<ul class="chk"><li>닭고기 1kg <span class="hl">6천원</span> (500원↓)</li><li>달걀 1판 <span class="hl">9천원</span> (500원↓)</li><li>소·돼지고기는 <span class="hl">한 달 전과 같아요</span></li><li>감귤·단감도 출하 늘어 <span class="hl">하락</span></li></ul>
<p class="lead" style="font-size:30px">전통시장 기준</p>""", SRC1, DL),
    a_slide(4, n, """<h2>겨울 생선은 <span class="hl">올랐어요</span></h2>
<div class="fig"><div><small>대구 1마리</small><strong>3만원</strong></div><div><small>생태 1마리</small><strong>1.3만원</strong></div></div>
<div class="box">대구 <b class="hl">5천원</b>↑ · 생태 <b class="hl">3천원</b>↑<br>높은 해수온에 어획 여건 악화</div>""", SRC1, DL),
    a_slide(5, n, f"""<h2>값 내린 품목 <span class="hl">장보기</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(RICE)}"><div>2026년산 햅쌀<span>곰곰 소중한 우리쌀</span></div></li>
<li><b>2</b><img src="{img(EGG)}"><div>유정란 특대란 30구<span>무항생제 · 난각번호 2번</span></div></li>
<li><b>3</b><img src="{img(CHICK)}"><div>닭볶음탕용 닭 900g<span>하림 · 무항생제 냉장</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/20 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "배추·달걀 내리고 대구·생태 올라",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 11월 장바구니, 배추·달걀은 내리고 대구·생태는 올랐어요 🛒

한국물가정보 '11월 KPI 물가동향'(11월 셋째 주 전통시장 기준)
· 배추 1포기 4천원 — 한 달 전보다 3천원 하락
· 무 1개 2천원 — 1천원 하락
· 일반미 8kg 2만8천원 — 1천원 하락
· 닭고기 1kg 6천원, 달걀 1판 9천원 — 각 500원 하락
· 소고기·돼지고기는 한 달 전과 같은 가격
· 감귤·단감은 출하량이 늘어 하락

반면 겨울 생선은 올랐어요
· 대구 1마리 3만원 — 5천원 상승
· 생태 1마리 1만3천원 — 3천원 상승
· 높은 해수온으로 어획 여건이 나빠진 영향

🔗 값 내린 품목 장보기 ①~③은 프로필 링크에 있어요
🛒 더 많은 장바구니템은 @0315_pick

출처: 직썰(2026.11.19)·문화투데이(2026.11.19) — 한국물가정보 조사

#광고 #생활뉴스 #물가 #장바구니물가 #배추값 #달걀 #햅쌀""",
    "products": [prod(1, RICE, N_RICE, "A"), prod(2, EGG, N_EGG, "A"), prod(3, CHICK, N_CHICK, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 주말까지 강추위 ═════════
SRC2 = "출처: SBS(11/20)·충청일보(11/19) — 기상청"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>주말까지<br><span class="hl">강추위</span></h1>
<p class="lead">일요일 오후부터<br>서서히 풀려요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘(20일) <span class="hl">서울</span></h2>
<div class="fig"><div><small>아침</small><strong>-3도</strong></div><div><small>낮</small><strong>3도</strong></div></div>
<div class="box">춘천 아침 <b class="hl">-5도</b><br>어제보다 <b class="hl">2~4도</b>가량 ↓</div>""", SRC2, DL),
    a_slide(3, n, """<h2>찬 바람에 <span class="hl">체감 ↓</span></h2>
<ul class="chk"><li>중부 종일 체감온도 <span class="hl">영하권</span></li><li>충청·호남·제주 <span class="hl">내일까지 눈·비</span></li><li>충청권 예상 적설 <span class="hl">1~5cm</span></li><li>귀갓길 빙판·살얼음 <span class="hl">조심</span></li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>주말 <span class="hl">아침 기온</span></h2>
<div class="fig"><div><small>토요일</small><strong>-7~-3도</strong></div><div><small>일요일</small><strong>-9~-2도</strong></div></div>
<div class="box">충청권 기준<br>일요일 오후부터 추위 <b class="hl">물러나요</b></div>""", SRC2, DL),
    a_slide(5, n, f"""<h2>뜨끈한 <span class="hl">겨울 간식</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(JJIN)}"><div>안흥찐빵 20입<span>500g x 2봉 · 단팥</span></div></li>
<li><b>2</b><img src="{img(ODENG)}"><div>모듬어묵 + 스프<span>삼진어묵 · 어묵탕 한 냄비</span></div></li>
<li><b>3</b><img src="{img(TEA)}"><div>쌍화차 110T<span>스틱형 · 따뜻한 차 한 잔</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/20 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "주말까지 강추위, 일요일 오후부터 풀려",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 주말까지 강추위 🥶 일요일 오후부터 서서히 풀려요

· 20일(금) 서울 아침 영하 3도, 춘천 영하 5도 — 어제보다 2~4도가량 낮아
· 서울·춘천 낮 기온도 3도에 그쳐
· 찬 바람에 중부 지방은 종일 체감온도 영하권
· 충청·호남·제주 중심으로 내일까지 눈·비, 충청권 예상 적설 1~5cm
· 주말 아침 충청권 토요일 영하 7~영하 3도, 일요일 영하 9~영하 2도
· 일요일 오후부터 추위가 서서히 물러나고, 다음 주엔 평년 기온 회복

✔ 귀갓길 그늘진 길·살얼음 조심
✔ 주말 외출은 따뜻하게 겹쳐 입기

🔗 뜨끈한 겨울 간식 ①~③은 프로필 링크에 있어요
🛒 더 많은 겨울 간식은 @0315_pick

출처: SBS(2026.11.20)·충청일보(2026.11.19) — 기상청 예보

#광고 #생활뉴스 #날씨 #강추위 #주말날씨 #겨울간식 #찐빵""",
    "products": [prod(1, JJIN, N_JJIN, "A"), prod(2, ODENG, N_ODENG, "A"), prod(3, TEA, N_TEA, "A")],
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


write(DATE, "B", [poll("요즘 장 볼 때<br>제일 먼저 담는 건? 🛒", "배추·달걀 ↓ 대구·생태 ↑ · 한국물가정보",
                       [("배추·무", "김장철엔 무조건"), ("고기", "메인은 있어야죠"),
                        ("감귤", "한 박스는 기본"), ("달걀 한 판", "냉장고 필수템")], EGG)], {
    "title": "장바구니 1순위 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 요즘 장 볼 때 제일 먼저 담는 건? 🛒
댓글에 번호로 투표해주세요!

1️⃣ 배추·무
2️⃣ 고기
3️⃣ 감귤
4️⃣ 달걀 한 판

※ 11월 셋째 주 전통시장 기준 배추 1포기 4천원·달걀 1판 9천원으로 한 달 전보다 하락, 대구·생태는 상승 (한국물가정보, 직썰 11/19)

🔗 4번 유정란 특대란 30구 링크는 프로필에
👥 장보기 같이 가는 사람 태그

#광고 #투표 #공감 #장보기 #장바구니물가 #달걀""",
    "products": [prod(1, EGG, N_EGG, "B")],
})

write(DATE, "B2", [poll("강추위 퇴근길,<br>제일 당기는 건? 🥶", "주말까지 강추위 · 일요일 오후부터 풀림",
                        [("붕어빵", "현금 챙겨야 함"), ("군고구마", "냄새 못 참음"),
                         ("어묵 국물", "한 컵만 더요"), ("뜨끈한 찐빵", "집에서 쪄 먹기")], JJIN)], {
    "title": "강추위 퇴근길 간식 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 강추위 퇴근길, 제일 당기는 건? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 붕어빵
2️⃣ 군고구마
3️⃣ 어묵 국물
4️⃣ 뜨끈한 찐빵

※ 20일 서울 아침 영하 3도·낮 3도, 주말까지 강추위 이어지다 일요일 오후부터 풀릴 전망 (기상청 예보, SBS 11/20)

🔗 4번 안흥찐빵 링크는 프로필에
👥 퇴근길 간식 같이 사 먹는 사람 태그

#광고 #투표 #공감 #강추위 #겨울간식 #찐빵""",
    "products": [prod(1, JJIN, N_JJIN, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/20 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("배추·달걀값 내렸어요 🛒", "이번 주", "장바구니", "BEST3", [RICE, EGG, CHICK]),
    c_prod(1, "0172", RICE, "2026년산<br>햅쌀", ["곰곰 소중한 우리쌀", "2026년산 햅쌀", "상등급 백미"],
           ["💰 3만원대", "📦 백미"]),
    c_prod(2, "0173", EGG, "유정란<br>특대란 30구", ["무항생제 유정란", "난각번호 2번", "특대란 30구"],
           ["💰 1만원대", "📦 30구"]),
    c_prod(3, "0174", CHICK, "닭볶음탕용<br>닭 900g", ["하림 프레쉬업", "친환경 무항생제", "냉장 절단육"],
           ["💰 9천원대", "📦 900g"]),
    c_howto("0172~0174"),
], {
    "title": "이번 주 장바구니 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

배추·달걀값 내렸어요 🛒 이번 주 장바구니 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 곰곰 2026년산 햅쌀 소중한 우리쌀 상등급 💛 품번 0172
올해 나온 햅쌀로 밥맛 챙기기.

2. 젊은 닭 유정란 특대란 30구 💛 품번 0173
무항생제·난각번호 2번 유정란 한 판.

3. 하림 친환경 프레쉬업 무항생제 닭볶음탕용 900g 💛 품번 0174
냉장 절단육, 주말 닭볶음탕 한 냄비.

✔ 11월 셋째 주 전통시장 기준 닭고기 1kg 6천원·달걀 1판 9천원, 한 달 전보다 각 500원 하락

※ 물가: 한국물가정보(직썰·문화투데이 11/19)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #장보기 #햅쌀 #유정란 #닭볶음탕""",
    "products": [prod(1, RICE, N_RICE, "C", "0172"), prod(2, EGG, N_EGG, "C", "0173"), prod(3, CHICK, N_CHICK, "C", "0174")],
})

write(DATE, "C2", [
    c_cover("주말까지 강추위 🥶", "뜨끈하게", "겨울 간식", "BEST3", [JJIN, ODENG, TEA]),
    c_prod(1, "0175", JJIN, "안흥찐빵<br>20입", ["500g x 2봉 구성", "모두 20개입", "단팥 찐빵"],
           ["💰 1만원대", "📦 20입"]),
    c_prod(2, "0176", ODENG, "모듬어묵<br>+ 스프", ["삼진어묵 오동통", "스프 함께 구성", "어묵탕 한 냄비"],
           ["💰 8천원대", "📦 어묵+스프"]),
    c_prod(3, "0177", TEA, "쌍화차<br>110T", ["스틱형 포장", "뜨거운 물에 타기만", "110개입 대용량"],
           ["💰 1만원대", "📦 110T"]),
    c_howto("0175~0177"),
], {
    "title": "강추위 겨울 간식 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

주말까지 강추위 🥶 뜨끈하게 겨울 간식 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 본가 안흥찐빵 500g x 2봉 (20입) 💛 품번 0175
단팥 찐빵 20개, 넉넉하게 쟁여두기.

2. 삼진어묵 오동통 모듬어묵 + 스프 💛 품번 0176
스프까지 들어 있어 어묵탕 한 냄비 뚝딱.

3. 우리차 쌍화차 110T 💛 품번 0177
스틱형이라 뜨거운 물에 타기만 하면 끝.

✔ 20일 서울 아침 영하 3도, 주말까지 추위 이어지다 일요일 오후부터 풀릴 전망

※ 날씨: 기상청 예보(SBS 11/20·충청일보 11/19)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #겨울간식 #찐빵 #어묵탕 #쌍화차""",
    "products": [prod(1, JJIN, N_JJIN, "C", "0175"), prod(2, ODENG, N_ODENG, "C", "0176"), prod(3, TEA, N_TEA, "C", "0177")],
})
print("ok")
