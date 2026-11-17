"""2026-11-17(화, 식품의 날) 게시물 6개 → docs/posts/2026-11-17/{A,B,C,A2,B2,C2}
점심: 제철 과일값 하락(사과 -30.68%, KAMIS 11/13) → 제철 과일 / 퇴근길: 오늘 전국 비 뒤 기온 급락, 19일 아침 영하 4도 → 뜨끈한 저녁 국물
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-17"
DL = "2026.11.17 (화)"
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


APPLE, MANDARIN, PERSIMMON = "9795359305", "9750353182", "9805900315"
GOMTANG, MANDU, UDON = "7527803282", "2341738091", "116679285"
N_APPLE = "산지직송 고당도 가정용 부사 사과 5kg"
N_MANDARIN = "고당도 선별 제주 노지 감귤 5kg"
N_PERSIMMON = "꼼꼼선별 국산 진영 단감 중대과 5kg"
N_GOMTANG = "비비고 사골곰탕"
N_MANDU = "한만두 푸짐한 왕만두 1.4kg (냉동)"
N_UDON = "오뚜기 가쓰오 사누끼 우동 4인"

# ═════════ A · 점심 12:00 — 제철 과일값 하락 ═════════
SRC1 = "출처: 파이낸셜뉴스(11/15) — KAMIS 11/13 소매가"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">식품 · 장바구니</div>
<h1>제철 과일값<br><span class="hl">줄줄이 하락</span></h1>
<p class="lead">사과는 1년 전보다<br>30% 넘게 내렸어요</p>""", SRC1, DL),
    a_slide(2, n, """<h2>사과 <span class="hl">10개</span> 소매가</h2>
<div class="fig"><div><small>11월 13일 기준</small><strong>1만8281원</strong></div><div><small>1년 전보다</small><strong>-30.68%</strong></div></div>
<div class="box">평년과 비교해도 <b class="hl">28.46%</b> 저렴</div>
<div class="box">올해 생산량 <b class="hl">49만6000t</b><br>작년보다 10.8% 늘 전망</div>""", SRC1, DL),
    a_slide(3, n, """<h2>다른 <span class="hl">제철 과일</span>은?</h2>
<div class="fig"><div><small>감귤(노지) 10개</small><strong>3852원</strong></div><div><small>1년 전보다</small><strong>-1.86%</strong></div></div>
<div class="fig"><div><small>단감 5개</small><strong>5857원</strong></div><div><small>1년 전보다</small><strong>-0.34%</strong></div></div>
<div class="box">감귤 생산량 <b class="hl">5.6%↑</b> 전망<br>이달 출하량도 8.1% 늘 듯</div>""", SRC1 + " · 농업관측센터", DL),
    a_slide(4, n, """<h2>왜 <span class="hl">내렸나?</span></h2>
<ul class="chk"><li>올해 <span class="hl">날씨가 좋아</span> 사과가 잘 자람</li><li>사과 재배면적도 <span class="hl">5.1%</span> 넓어짐</li><li>이달 사과 출하량 <span class="hl">13.8%</span> 증가 예상</li><li>작년엔 작황 부진으로 비쌌어요</li></ul>""", SRC1 + " · 농업관측센터", DL),
    a_slide(5, n, f"""<h2>지금 담기 좋은 <span class="hl">제철 과일</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(APPLE)}"><div>가정용 부사 사과<span>5kg · 산지직송</span></div></li>
<li><b>2</b><img src="{img(MANDARIN)}"><div>제주 노지 감귤<span>5kg · 당도 선별</span></div></li>
<li><b>3</b><img src="{img(PERSIMMON)}"><div>국산 진영 단감<span>중대과 5kg</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/17 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "제철 과일값 줄줄이 하락",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 제철 과일값 줄줄이 하락 🍎 사과 10개 1만8281원, 1년 전보다 30.68%↓

· 사과(10개) 1만8281원 — 전년 대비 -30.68%, 평년 대비 -28.46%
· 감귤(노지, 10개) 3852원 — 전년 대비 -1.86%
· 단감(5개) 5857원 — 전년 대비 -0.34%
· (11월 13일 소매가, 농산물유통정보 KAMIS)

왜 내렸을까?
· 올해 기상 여건이 좋아 사과 생육이 개선, 재배면적도 5.1% 증가
· 사과 생산량 49만6000t(전년 대비 +10.8%), 이달 출하량 +13.8% 전망
· 감귤 생산량 43만3000t(+5.6%), 이달 출하량 +8.1% 전망

🔗 지금 담기 좋은 제철 과일 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 파이낸셜뉴스(2026.11.15) — KAMIS 11/13 소매가격, 한국농촌경제연구원 농업관측센터

#광고 #생활뉴스 #장바구니물가 #제철과일 #사과 #감귤 #단감""",
    "products": [prod(1, APPLE, N_APPLE, "A"), prod(2, MANDARIN, N_MANDARIN, "A"), prod(3, PERSIMMON, N_PERSIMMON, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 비 그친 뒤 기온 급락 ═════════
SRC2 = "출처: 톱스타뉴스·서울신문(11/17) — 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">식품 · 오늘 밤</div>
<h1>비 그치면<br>기온 <span class="hl">'뚝'</span></h1>
<p class="lead">목요일 아침<br>최저 영하 4도</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘(17일) <span class="hl">비</span></h2>
<ul class="chk"><li>중부·전라 <span class="hl">낮 12~18시</span>부터</li><li>경상권 <span class="hl">저녁 18~21시</span>부터</li><li>대부분 늦은 밤 그침</li><li>경기동부·강원·충북 등 일부 18일 새벽까지</li></ul>""", SRC2, DL),
    a_slide(3, n, """<h2>예상 <span class="hl">강수량</span></h2>
<div class="fig"><div><small>서울·인천·경기</small><strong>5~10mm</strong></div><div><small>제주</small><strong>5~20mm</strong></div></div>
<div class="box">강원·충청 <b class="hl">5~10mm</b></div>
<div class="box">전라·경상 <b class="hl">5mm 안팎</b></div>""", SRC2, DL),
    a_slide(4, n, """<h2>내일부터 <span class="hl">추워요</span></h2>
<div class="fig"><div><small>18일(수) 낮</small><strong>8~15도</strong></div><div><small>19일(목) 아침</small><strong>-4~6도</strong></div></div>
<div class="box">18일 낮은 오늘보다 <b class="hl">3~6도</b> 낮고</div>
<div class="box">19일 아침은 18일보다 <b class="hl">5~10도</b> 더 낮아요</div>""", SRC2, DL),
    a_slide(5, n, f"""<h2>뜨끈한 <span class="hl">저녁 국물</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(GOMTANG)}"><div>비비고 사골곰탕<span>데우기만 하면 완성</span></div></li>
<li><b>2</b><img src="{img(MANDU)}"><div>한만두 왕만두<span>1.4kg · 만둣국 OK</span></div></li>
<li><b>3</b><img src="{img(UDON)}"><div>가쓰오 사누끼 우동<span>오뚜기 · 4인</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/17 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "비 그친 뒤 기온 급락",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 오늘 전국 비 ☔ 그치면 기온 '뚝' — 19일(목) 아침 최저 영하 4도

· 17일(화) 중부·전라권 낮 12~18시, 경상권 저녁 18~21시부터 비
· 대부분 늦은 밤 그치고, 경기동부·강원·충북·경상권 일부는 18일 새벽까지
· 예상 강수량: 서울·인천·경기·강원·충청 5~10mm, 제주 5~20mm, 전라·경상 5mm 안팎
· 18일(수) 아침 2~11도, 낮 8~15도 — 오늘보다 3~6도 낮아요
· 19일(목) 아침 영하 4도~영상 6도, 낮 3~10도 — 18일 아침보다 5~10도 더 낮아요

✔ 퇴근길 우산 챙기기
✔ 추운 밤엔 뜨끈한 국물 한 그릇

🔗 뜨끈한 저녁 국물 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 톱스타뉴스(2026.11.17)·서울신문(2026.11.17) — 기상청 예보

#광고 #생활뉴스 #날씨 #비소식 #기온급락 #사골곰탕 #저녁메뉴""",
    "products": [prod(1, GOMTANG, N_GOMTANG, "A"), prod(2, MANDU, N_MANDU, "A"), prod(3, UDON, N_UDON, "A")],
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


write(DATE, "B", [poll("겨울 귤,<br>앉은 자리에서 몇 개? 🍊", "감귤(노지) 10개 3852원 · 생산량 5.6%↑ 전망",
                       [("1~2개면 충분", "적당히가 최고"), ("5개는 기본", "손 노래질 때까지"),
                        ("셀 수 없음", "껍질 산이 증거"), ("귤은 박스로 사는 것", "5kg 쟁여두기")], MANDARIN)], {
    "title": "겨울 귤 몇 개 먹나 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 겨울 귤, 앉은 자리에서 몇 개? 🍊
댓글에 번호로 투표해주세요!

1️⃣ 1~2개면 충분
2️⃣ 5개는 기본
3️⃣ 셀 수 없음
4️⃣ 귤은 박스로 사는 것

※ 감귤(노지) 10개 소매가 3852원(11/13, KAMIS), 올해 감귤 생산량 전년 대비 5.6% 증가 전망 (파이낸셜뉴스 11/15)

🔗 4번 제주 노지 감귤 5kg 링크는 프로필에
👥 귤 먹다 손 노래진 친구 태그

#광고 #투표 #공감 #귤 #감귤 #겨울간식""",
    "products": [prod(1, MANDARIN, N_MANDARIN, "B")],
})

write(DATE, "B2", [poll("비 오고 추운 저녁,<br>당기는 메뉴는? 🍲", "오늘 전국 비 · 19일 아침 최저 영하 4도 (기상청)",
                        [("라면 하나 끓이기", "국룰 중의 국룰"), ("배달 짬뽕", "얼큰한 게 최고"),
                         ("편의점 어묵", "퇴근길 한 컵"), ("집에서 만둣국", "왕만두 퐁당")], MANDU)], {
    "title": "비 오고 추운 저녁 메뉴 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 비 오고 추운 저녁, 당기는 메뉴는? 🍲
댓글에 번호로 투표해주세요!

1️⃣ 라면 하나 끓이기
2️⃣ 배달 짬뽕
3️⃣ 편의점 어묵
4️⃣ 집에서 만둣국

※ 17일(화) 전국 비, 19일(목) 아침 최저 영하 4도~영상 6도 (기상청 예보, 톱스타뉴스 11/17)

🔗 4번 한만두 푸짐한 왕만두 링크는 프로필에
👥 오늘 저녁 메뉴 같이 정할 친구 태그

#광고 #투표 #공감 #저녁메뉴 #비오는날 #만둣국""",
    "products": [prod(1, MANDU, N_MANDU, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/17 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("사과값 1년 새 30%↓ 🍎", "지금 담기 좋은", "제철 과일", "BEST3", [APPLE, MANDARIN, PERSIMMON]),
    c_prod(1, "0154", APPLE, "가정용<br>부사 사과", ["산지직송 고당도 부사", "가정용 5kg", "집에서 넉넉하게"],
           ["💰 2만2천원대", "📦 산지직송"]),
    c_prod(2, "0155", MANDARIN, "제주 노지<br>감귤 5kg", ["당도 선별 노지 감귤", "새콤달콤 제주산", "5kg 넉넉하게"],
           ["💰 1만9천원대", "📦 5kg 박스"]),
    c_prod(3, "0156", PERSIMMON, "국산<br>진영 단감", ["진영 단감 중대과", "꼼꼼 선별", "5kg 박스"],
           ["💰 2만5천원대", "📦 5kg 박스"]),
    c_howto("0154~0156"),
], {
    "title": "제철 과일 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

사과값 1년 새 30%↓ 🍎 지금 담기 좋은 제철 과일 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 산지직송 고당도 가정용 부사 사과 5kg 💛 품번 0154
가정용 부사 사과 5kg, 산지직송.

2. 고당도 선별 제주 노지 감귤 5kg 💛 품번 0155
당도 선별한 제주 노지 감귤 5kg 박스.

3. 꼼꼼선별 국산 진영 단감 중대과 5kg 💛 품번 0156
진영 단감 중대과 5kg 박스.

✔ 사과(10개) 소매가 1만8281원, 1년 전보다 30.68% 하락

※ 과일값: KAMIS 11/13 소매가(파이낸셜뉴스 11/15)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #제철과일 #사과 #감귤 #단감""",
    "products": [prod(1, APPLE, N_APPLE, "C", "0154"), prod(2, MANDARIN, N_MANDARIN, "C", "0155"), prod(3, PERSIMMON, N_PERSIMMON, "C", "0156")],
})

write(DATE, "C2", [
    c_cover("비 그치면 기온 '뚝' 🥶", "뜨끈한", "저녁 국물", "BEST3", [GOMTANG, MANDU, UDON]),
    c_prod(1, "0157", GOMTANG, "비비고<br>사골곰탕", ["데우기만 하면 완성", "떡국·만둣국 육수로도", "500g 파우치"],
           ["💰 2만1천원대", "🚀 로켓배송"]),
    c_prod(2, "0158", MANDU, "한만두<br>푸짐한 왕만두", ["냉동 왕만두 1.4kg", "찜·만둣국 모두 OK", "넉넉한 대용량"],
           ["💰 1만2천원대", "🚀 로켓배송"]),
    c_prod(3, "0159", UDON, "가쓰오<br>사누끼 우동", ["오뚜기 4인분", "가쓰오 국물", "끓이기만 하면 끝"],
           ["💰 7천원대", "🚀 로켓배송"]),
    c_howto("0157~0159"),
], {
    "title": "뜨끈한 저녁 국물 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

비 그치면 기온 '뚝' 🥶 뜨끈한 저녁 국물 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 비비고 사골곰탕 💛 품번 0157
데우기만 하면 되는 사골곰탕, 떡국·만둣국 육수로도.

2. 한만두 푸짐한 왕만두 1.4kg (냉동) 💛 품번 0158
찜으로도 만둣국으로도 좋은 냉동 왕만두.

3. 오뚜기 가쓰오 사누끼 우동 4인 💛 품번 0159
가쓰오 국물 우동 4인분.

✔ 19일(목) 아침 최저 영하 4도 — 따뜻하게 챙겨 입으세요

※ 날씨: 기상청 예보(톱스타뉴스·서울신문 11/17)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #저녁메뉴 #사골곰탕 #왕만두 #우동""",
    "products": [prod(1, GOMTANG, N_GOMTANG, "C", "0157"), prod(2, MANDU, N_MANDU, "C", "0158"), prod(3, UDON, N_UDON, "C", "0159")],
})
print("ok")
