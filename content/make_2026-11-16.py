"""2026-11-16(월, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-16/{A,B,C,A2,B2,C2}
점심: 월요일 아침 기온 뚝(일부 남부 내륙 5~10도↓) → 포근한 잠자리템 / 퇴근길: 17~18일 전국 비 → 수능일 6년 만의 서울 영하 → 비 오는 날 현관·옷장템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-16"
DL = "2026.11.16 (월)"
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


SOCKS, BLANKET, PAD = "9775833107", "6718528503", "126289261"
UMB, MAT, DEHUM = "7355599561", "7505237596", "1744895218"
N_SOCKS = "극세사 털 수면양말 남여공용 4켤레 세트"
N_BLANKET = "코멧 홈 양면 극세사 솔리드 차렵이불"
N_PAD = "보몽드 극세사 누빔패드"
N_UMB = "코멧 베이직 자동 장우산 2p"
N_MAT = "맑은 코일 현관매트 100x135cm 두께 20mm"
N_DEHUM = "홈플래닛 대용량 옷걸이형 제습제"

# ═════════ A · 점심 12:00 — 월요일 아침 기온 뚝 ═════════
SRC1 = "출처: 아시아경제·서울경제(11/16) — 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활용품 · 오늘</div>
<h1>월요일 아침<br>기온 <span class="hl">'뚝'</span></h1>
<p class="lead">북쪽 찬 공기 내려와<br>출근길 쌀쌀</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(16일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>3~11도</strong></div><div><small>전국 낮 최고</small><strong>12~19도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>8도</strong></div><div><small>서울 낮</small><strong>17도</strong></div></div>
<div class="box">일부 남부 내륙은 아침 기온이<br>전날보다 <b class="hl">5~10도</b> 떨어져요</div>""", SRC1, DL),
    a_slide(3, n, """<h2>비·눈·<span class="hl">안개</span></h2>
<div class="box"><b class="hl">5~30mm</b><br>강원 동해안·산지, 경북 북부 동해안</div>
<div class="box">강원 높은 산지 <b class="hl">눈 1~5cm</b><br>살얼음 주의</div>
<div class="box">충청·남부 내륙 새벽~오전<br>짙은 안개 · 서리</div>""", SRC1, DL),
    a_slide(4, n, """<h2>쌀쌀한 밤 <span class="hl">잠자리 체크</span></h2>
<ul class="chk"><li>얇은 이불은 <span class="hl">겨울 이불</span>로 교체</li><li>발이 차면 <span class="hl">수면양말</span></li><li>매트리스 위에 <span class="hl">도톰한 패드</span></li><li>자기 전 실내 너무 덥지 않게</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>포근한 <span class="hl">잠자리템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SOCKS)}"><div>극세사 털 수면양말<span>남여공용 4켤레</span></div></li>
<li><b>2</b><img src="{img(BLANKET)}"><div>양면 극세사 차렵이불<span>앞뒤 모두 극세사</span></div></li>
<li><b>3</b><img src="{img(PAD)}"><div>극세사 누빔패드<span>매트리스 위에 깔기</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/16 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "월요일 아침 기온 뚝",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 월요일 아침 기온 '뚝' 🥶 북쪽 찬 공기에 출근길 쌀쌀

· 16일(월) 아침 최저 3~11도, 낮 최고 12~19도
· 서울 아침 8도, 낮 17도
· 일부 남부 내륙은 아침 기온이 전날보다 5~10도 하락
· 강원 동해안·산지, 경북 북부 동해안 5~30mm 비 / 강원 높은 산지 눈 1~5cm
· 충청·남부 내륙 새벽~오전 짙은 안개, 일부 서리

✔ 얇은 이불은 겨울 이불로 교체
✔ 발이 차면 수면양말
✔ 매트리스 위에 도톰한 패드

🔗 포근한 잠자리템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 아시아경제·서울경제(2026.11.16) — 기상청 예보

#광고 #생활뉴스 #날씨 #출근길 #겨울이불 #수면양말 #생활용품""",
    "products": [prod(1, SOCKS, N_SOCKS, "A"), prod(2, BLANKET, N_BLANKET, "A"), prod(3, PAD, N_PAD, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 17~18일 전국 비 → 수능일 영하 ═════════
SRC2 = "출처: 남도일보(11/16)·경향신문(11/15) — 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활용품 · 이번 주</div>
<h1>화·수 <span class="hl">전국 비</span><br>수능일엔 영하</h1>
<p class="lead">비 그친 뒤 기온 큰 폭 하락<br>서울 아침 6년 만의 영하권</p>""", SRC2, DL),
    a_slide(2, n, """<h2>비 <span class="hl">언제?</span></h2>
<ul class="chk"><li>17일(화) 오후 <span class="hl">수도권·강원·충청·전라·제주</span></li><li>저녁엔 경상권까지</li><li>18일(수) 오후~밤 <span class="hl">전국 대부분</span> 또 비</li><li>일부 강원·충북·경북 북부 비 또는 눈</li></ul>""", SRC2, DL),
    a_slide(3, n, """<h2>17일 <span class="hl">예상 강수량</span></h2>
<div class="fig"><div><small>수도권·강원·충청</small><strong>5~10mm</strong></div><div><small>제주</small><strong>5~10mm</strong></div></div>
<div class="box">전라권·경상권 <b class="hl">5mm 안팎</b></div>
<div class="box">18일부터 전국 대부분 <b class="hl">강한 바람</b></div>""", SRC2, DL),
    a_slide(4, n, """<h2>19일(목) <span class="hl">수능일</span></h2>
<div class="fig"><div><small>서울 아침</small><strong>-1도</strong></div><div><small>춘천 아침</small><strong>-3도</strong></div></div>
<div class="box">전국 아침 <b class="hl">-4~6도</b>, 낮 <b class="hl">3~10도</b></div>
<div class="box">서울 아침 영하 수능은<br><b class="hl">2020년 이후 6년 만</b></div>""", "출처: 남도일보(11/16) — 기상청 예보", DL),
    a_slide(5, n, f"""<h2>비 오는 이틀 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(UMB)}"><div>자동 장우산 2p<span>버튼 하나로 펼치기</span></div></li>
<li><b>2</b><img src="{img(MAT)}"><div>코일 현관매트<span>100x135cm · 20mm</span></div></li>
<li><b>3</b><img src="{img(DEHUM)}"><div>옷걸이형 제습제<span>옷장에 걸어두기</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/16 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "화·수 전국 비·수능일 영하",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 화·수 전국 비 ☔ 그친 뒤 수능일(19일) 서울 아침 영하 1도

· 17일(화) 오후 수도권·강원·충청·전라·제주에 비 → 저녁 경상권까지
· 17일 예상 강수량: 수도권·강원·충청 5~10mm, 제주 5~10mm, 전라·경상 5mm 안팎
· 18일(수) 오후~밤 전국 대부분 다시 비, 일부 강원·충북·경북 북부는 비 또는 눈
· 18일부터 전국 대부분 강한 바람
· 19일(목) 아침 -4~6도, 낮 3~10도 / 서울 아침 -1도, 춘천 -3도
· 서울 아침 영하권 수능은 2020년 이후 6년 만

✔ 이틀 연속 비, 우산 챙기기
✔ 현관에 빗물·흙 털 매트
✔ 습한 날 옷장엔 제습제

🔗 비 오는 이틀 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 남도일보(2026.11.16)·경향신문(2026.11.15) — 기상청 예보

#광고 #생활뉴스 #날씨 #비소식 #수능한파 #장우산 #생활용품""",
    "products": [prod(1, UMB, N_UMB, "A"), prod(2, MAT, N_MAT, "A"), prod(3, DEHUM, N_DEHUM, "A")],
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


write(DATE, "B", [poll("쌀쌀한 월요일 아침,<br>이불 밖 탈출 방법은? 🛏️", "16일 아침 최저 3~11도 · 일부 남부 내륙 5~10도 하락 (기상청)",
                       [("알람 5번 미루기", "5분만… 5분만…"), ("이불 덮은 채 굴러 나오기", "애벌레 출근"),
                        ("난방 켜고 다시 눕기", "따뜻해지면 일어남"), ("수면양말 신고 버티기", "발만 따뜻하면 OK")], SOCKS)], {
    "title": "월요일 아침 이불 밖 탈출 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 쌀쌀한 월요일 아침, 이불 밖 탈출 방법은? 🛏️
댓글에 번호로 투표해주세요!

1️⃣ 알람 5번 미루기
2️⃣ 이불 덮은 채 굴러 나오기
3️⃣ 난방 켜고 다시 눕기
4️⃣ 수면양말 신고 버티기

※ 16일(월) 아침 최저 3~11도, 일부 남부 내륙은 전날보다 5~10도 하락 (기상청 예보, 아시아경제·서울경제 11/16)

🔗 4번 극세사 털 수면양말 링크는 프로필에
👥 월요일 아침마다 지각 위기인 친구 태그

#광고 #투표 #공감 #월요일 #출근길 #수면양말""",
    "products": [prod(1, SOCKS, N_SOCKS, "B")],
})

write(DATE, "B2", [poll("비 오는 날 출근길,<br>나는 어떤 타입? ☔", "17일 오후~18일 전국 비 · 수도권 5~10mm (기상청)",
                        [("비 맞고 그냥 뛰기", "젖으면 마르겠지"), ("편의점 우산 또 사기", "집에 우산 10개째"),
                         ("택시 타고 출근", "오늘만 플렉스"), ("튼튼한 장우산 챙기기", "바람 불어도 든든")], UMB)], {
    "title": "비 오는 날 출근길 타입 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 비 오는 날 출근길, 나는 어떤 타입? ☔
댓글에 번호로 투표해주세요!

1️⃣ 비 맞고 그냥 뛰기
2️⃣ 편의점 우산 또 사기
3️⃣ 택시 타고 출근
4️⃣ 튼튼한 장우산 챙기기

※ 17일(화) 오후~18일(수) 전국 비, 수도권·강원·충청 5~10mm (기상청 예보, 남도일보 11/16)

🔗 4번 코멧 자동 장우산 2p 링크는 프로필에
👥 우산 맨날 두고 오는 친구 태그

#광고 #투표 #공감 #비오는날 #출근길 #장우산""",
    "products": [prod(1, UMB, N_UMB, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/16 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("월요일 아침 기온 '뚝' 🥶", "포근한", "잠자리템", "BEST3", [SOCKS, BLANKET, PAD]),
    c_prod(1, "0148", SOCKS, "극세사 털<br>수면양말", ["도톰한 극세사 털양말", "남여공용", "4켤레 세트"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_prod(2, "0149", BLANKET, "양면 극세사<br>차렵이불", ["앞뒤 모두 극세사", "솔리드 단색", "겨울 이불 교체용"],
           ["💰 1만9천원대", "🚀 로켓배송"]),
    c_prod(3, "0150", PAD, "극세사<br>누빔패드", ["매트리스 위에 까는 패드", "극세사 누빔", "잠자리 포근하게"],
           ["💰 1만7천원대", "🚀 로켓배송"]),
    c_howto("0148~0150"),
], {
    "title": "포근한 잠자리템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

월요일 아침 기온 '뚝' 🥶 포근한 잠자리템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 극세사 털 수면양말 남여공용 4켤레 세트 💛 품번 0148
도톰한 극세사 털양말, 남여공용 4켤레 세트.

2. 코멧 홈 양면 극세사 솔리드 차렵이불 💛 품번 0149
앞뒤 모두 극세사인 단색 차렵이불, 겨울 이불 교체용.

3. 보몽드 극세사 누빔패드 💛 품번 0150
매트리스 위에 까는 극세사 누빔패드.

✔ 쌀쌀한 밤엔 이불·패드부터 겨울용으로

※ 날씨: 기상청 예보(아시아경제·서울경제 11/16)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #겨울이불 #차렵이불 #수면양말 #누빔패드""",
    "products": [prod(1, SOCKS, N_SOCKS, "C", "0148"), prod(2, BLANKET, N_BLANKET, "C", "0149"), prod(3, PAD, N_PAD, "C", "0150")],
})

write(DATE, "C2", [
    c_cover("화·수 전국 비 ☔", "비 오는 이틀", "생활템", "BEST3", [UMB, MAT, DEHUM]),
    c_prod(1, "0151", UMB, "자동<br>장우산 2p", ["버튼식 자동 장우산", "2개 구성", "가족과 나눠 쓰기"],
           ["💰 1만5천원대", "🚀 로켓배송"]),
    c_prod(2, "0152", MAT, "코일<br>현관매트", ["100x135cm 큰 사이즈", "두께 20mm 코일", "빗물·흙 털기"],
           ["💰 2만3천원대", "🚀 로켓배송"]),
    c_prod(3, "0153", DEHUM, "옷걸이형<br>제습제", ["옷장 봉에 거는 타입", "대용량", "습한 날 옷장 관리"],
           ["💰 1만1천원대", "🚀 로켓배송"]),
    c_howto("0151~0153"),
], {
    "title": "비 오는 이틀 생활템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

화·수 전국 비 ☔ 비 오는 이틀 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 코멧 베이직 자동 장우산 2p 💛 품번 0151
버튼으로 펼치는 자동 장우산 2개 구성.

2. 맑은 코일 현관매트 100x135cm 두께 20mm 💛 품번 0152
현관에서 빗물·흙을 털어주는 큰 사이즈 코일매트.

3. 홈플래닛 대용량 옷걸이형 제습제 💛 품번 0153
옷장 봉에 걸어 쓰는 대용량 제습제.

✔ 비 그친 뒤 19일(수능일)엔 서울 아침 영하 1도 — 따뜻하게 챙겨 입으세요

※ 날씨: 기상청 예보(남도일보 11/16·경향신문 11/15)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #비오는날 #장우산 #현관매트 #제습제""",
    "products": [prod(1, UMB, N_UMB, "C", "0151"), prod(2, MAT, N_MAT, "C", "0152"), prod(3, DEHUM, N_DEHUM, "C", "0153")],
})
print("ok")
