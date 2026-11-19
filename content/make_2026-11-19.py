"""2026-11-19(목, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-19/{A,B,C,A2,B2,C2}
점심: 올해 김장비용 2020년대 최저(한국물가정보) → 김장 생활용품 / 퇴근길: 수능일 영하권·살얼음, 주말 추위 절정 → 빙판길·눈길 생활용품
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-19"
DL = "2026.11.19 (목)"
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


BOWL, SLICER, BAG = "9337195897", "9489736746", "9334827505"
CLEAT, COVER, SHOVEL = "9145443723", "9016200408", "9576518715"
N_BOWL = "에버튼하우스 스텐 대야 + 채반 세트 53cm"
N_SLICER = "대한명도 4세대 3단 두께조절 채칼 슬라이서"
N_BAG = "두껍고 질긴 김장봉투 소·중·대"
N_CLEAT = "에버리즈 미끄럼방지 도시형 아이젠 2+2"
N_COVER = "고릴라몰 미끄럼방지 신발 방수 커버"
N_SHOVEL = "접이식 경량 눈삽 제설도구"

# ═════════ A · 점심 12:00 — 김장비용 2020년대 최저 ═════════
SRC1 = "출처: 세계일보·연합뉴스(11/16) — 한국물가정보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 물가</div>
<h1>올해 김장비용<br><span class="hl">2020년대 최저</span></h1>
<p class="lead">4인 가족 전통시장<br>28만8500원</p>""", SRC1, DL),
    a_slide(2, n, """<h2>4인 가족 <span class="hl">김장비용</span></h2>
<div class="fig"><div><small>전통시장</small><strong>28.85만</strong></div><div><small>대형마트</small><strong>36.03만</strong></div></div>
<div class="box">작년보다 전통시장 <b class="hl">14.8%</b>↓<br>대형마트 <b class="hl">10.9%</b>↓</div>""", SRC1, DL),
    a_slide(3, n, """<h2>배추값 <span class="hl">뚝</span>, 젓갈은 ↑</h2>
<ul class="chk"><li>배추 20포기 <span class="hl">8만원</span> (33.3%↓)</li><li>쪽파 <span class="hl">50%</span>↓ · 총각무·대파 20%↓</li><li>천일염 <span class="hl">16.7%</span>↑</li><li>새우젓 <span class="hl">33.3%</span>↑</li></ul>
<p class="lead" style="font-size:30px">전통시장 기준</p>""", SRC1, DL),
    a_slide(4, n, """<h2>올해 <span class="hl">김장 적기</span></h2>
<div class="box">중부 <b class="hl">11월 하순~12월 초</b><br>남부 <b class="hl">12월 초~중순</b></div>
<ul class="chk"><li>일평균 기온 <span class="hl">4도 이하</span></li><li>최저기온 <span class="hl">0도 이하</span>가 이어질 때</li><li>날짜 정하고 도구부터 챙기기</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>김장 전 챙길 <span class="hl">생활용품</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BOWL)}"><div>스텐 대야+채반 세트<span>53cm · 절임·버무리기</span></div></li>
<li><b>2</b><img src="{img(SLICER)}"><div>3단 두께조절 채칼<span>무채 썰기 한 번에</span></div></li>
<li><b>3</b><img src="{img(BAG)}"><div>두꺼운 김장봉투<span>소·중·대 · 보관·나눔용</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/19 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "올해 김장비용 2020년대 최저",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 올해 김장비용 2020년대 들어 최저 🥬 4인 가족 전통시장 28만8500원

· 한국물가정보 조사(김장재료 11개 품목, 4인 가족 기준)
· 전통시장 28만8500원 — 지난해보다 14.8% 감소
· 대형마트 36만340원 — 지난해보다 10.9% 감소
· 배추(20포기) 8만원으로 33.3% 하락, 쪽파 50%·총각무·대파 각 20% 하락
· 반면 천일염 16.7%, 새우젓 33.3% 상승 (전통시장 기준)

올해 김장 적기
✔ 중부(서울·경기·충청) 11월 하순~12월 초
✔ 남부(전라·경상) 12월 초~중순
✔ 일평균 기온 4도 이하, 최저기온 0도 이하가 이어질 때가 적기

🔗 김장 전 챙길 생활용품 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 세계일보(2026.11.16)·연합뉴스(2026.11.16) — 한국물가정보 조사

#광고 #생활뉴스 #김장 #김장비용 #배추값 #김장준비 #채칼""",
    "products": [prod(1, BOWL, N_BOWL, "A"), prod(2, SLICER, N_SLICER, "A"), prod(3, BAG, N_BAG, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 수능일 영하권·살얼음 ═════════
SRC2 = "출처: SBS·월요신문·이코노믹리뷰(11/19) — 기상청"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>수능일 <span class="hl">영하권</span><br>주말 추위 절정</h1>
<p class="lead">퇴근길·주말<br>살얼음 조심</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘(19일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>-4~7도</strong></div><div><small>낮 최고</small><strong>3~10도</strong></div></div>
<div class="box">서울 아침 <b class="hl">-1도</b> · 낮 <b class="hl">4도</b><br>태백 -7도 · 춘천 -3도</div>""", SRC2, DL),
    a_slide(3, n, """<h2>눈·비 뒤 <span class="hl">살얼음</span></h2>
<ul class="chk"><li>밤사이 내린 눈·비가 <span class="hl">얼어붙어</span></li><li>도로 위 <span class="hl">살얼음</span> 주의</li><li>전북 남부 내륙 <span class="hl">최고 8cm</span> 눈</li><li>강원 산지 등 <span class="hl">한파주의보</span></li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>주말엔 <span class="hl">더 추워요</span></h2>
<div class="box">이번 주말 <b class="hl">추위 절정</b><br>찬 바람에 체감은 더 낮아요</div>
<ul class="chk"><li>그늘진 길·횡단보도 <span class="hl">천천히</span></li><li>주머니에서 <span class="hl">손 빼고</span> 걷기</li><li>밑창 미끄러운 신발 피하기</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>빙판길 대비 <span class="hl">생활용품</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(CLEAT)}"><div>도시형 아이젠<span>신발에 끼우는 2+2</span></div></li>
<li><b>2</b><img src="{img(COVER)}"><div>미끄럼방지 신발 커버<span>눈·비 오는 날 덧신</span></div></li>
<li><b>3</b><img src="{img(SHOVEL)}"><div>접이식 눈삽<span>현관·차 앞 눈 치우기</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/19 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "수능일 영하권, 주말 추위 절정",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 수능일 전국 영하권 🥶 주말엔 추위 절정, 살얼음 조심

· 19일(목) 아침 최저 영하 4도~영상 7도, 낮 최고 3~10도
· 서울 아침 영하 1도·낮 4도, 태백 영하 7도, 춘천 영하 3도
· 서울 수능일 아침 영하권은 2020년 이후 6년 만
· 밤사이 내린 눈·비가 얼어 도로 살얼음 주의, 전북 남부 내륙 최고 8cm 눈
· 강원 산지 등 일부 동쪽 지역 한파주의보
· 이번 주말 추위가 절정에 달할 전망

✔ 그늘진 길·횡단보도는 천천히
✔ 주머니에서 손 빼고 걷기
✔ 밑창 미끄러운 신발은 피하기

수험생 여러분, 오늘 정말 고생 많으셨어요 👏

🔗 빙판길 대비 생활용품 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: SBS(2026.11.19)·월요신문(2026.11.19)·이코노믹리뷰(2026.11.19) — 기상청 예보

#광고 #생활뉴스 #날씨 #수능 #한파 #빙판길 #아이젠""",
    "products": [prod(1, CLEAT, N_CLEAT, "A"), prod(2, COVER, N_COVER, "A"), prod(3, SHOVEL, N_SHOVEL, "A")],
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


write(DATE, "B", [poll("김장할 때<br>제일 힘든 일은? 🥬", "올해 김장비용 2020년대 최저 · 한국물가정보",
                       [("배추 절이기", "밤새 뒤집기 담당"), ("양념 버무리기", "허리가 안 펴져요"),
                        ("뒷정리·설거지", "끝나도 끝난 게 아님"), ("무채 썰기", "채칼 있으면 금방")], SLICER)], {
    "title": "김장 제일 힘든 일 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 김장할 때 제일 힘든 일은? 🥬
댓글에 번호로 투표해주세요!

1️⃣ 배추 절이기
2️⃣ 양념 버무리기
3️⃣ 뒷정리·설거지
4️⃣ 무채 썰기

※ 올해 4인 가족 김장비용 전통시장 28만8500원, 2020년대 들어 최저 (한국물가정보, 세계일보 11/16)

🔗 4번 3단 두께조절 채칼 링크는 프로필에
👥 김장 같이 할 가족 태그

#광고 #투표 #공감 #김장 #김장준비 #채칼""",
    "products": [prod(1, SLICER, N_SLICER, "B")],
})

write(DATE, "B2", [poll("빙판길 출근,<br>내 걸음은? 🐧", "수능일 영하권 · 주말 추위 절정 예보",
                        [("펭귄 걸음", "종종종 조심조심"), ("평소처럼 성큼", "그러다 미끄덩"),
                         ("아예 안 나감", "주말은 이불 속"), ("아이젠 장착", "빙판도 성큼성큼")], CLEAT)], {
    "title": "빙판길 걸음 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 빙판길 출근, 내 걸음은? 🐧
댓글에 번호로 투표해주세요!

1️⃣ 펭귄 걸음
2️⃣ 평소처럼 성큼
3️⃣ 아예 안 나감
4️⃣ 아이젠 장착

※ 19일 밤사이 내린 눈·비가 얼어 도로 살얼음 주의, 이번 주말 추위 절정 (기상청 예보, SBS 11/19)

🔗 4번 도시형 아이젠 링크는 프로필에
👥 빙판길에서 꼭 넘어지는 친구 태그

#광고 #투표 #공감 #빙판길 #한파 #아이젠""",
    "products": [prod(1, CLEAT, N_CLEAT, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/19 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("김장비용 2020년대 최저 🥬", "김장 전에", "챙길 생활템", "BEST3", [BOWL, SLICER, BAG]),
    c_prod(1, "0166", BOWL, "스텐 대야<br>+ 채반 세트", ["53cm 스텐 대야", "채반 함께 구성", "절이기·버무리기·물빼기"],
           ["💰 2만원대", "📦 세트"]),
    c_prod(2, "0167", SLICER, "3단 두께조절<br>채칼", ["두께 3단 조절", "무채·당근채 한 번에", "국내산 · SUS304 칼날"],
           ["💰 1만원대", "📦 슬라이서"]),
    c_prod(3, "0168", BAG, "두꺼운<br>김장봉투", ["일반 비닐보다 두껍게", "소·중·대 크기", "김치 보관·나눔용"],
           ["💰 6천원대", "📦 소·중·대"]),
    c_howto("0166~0168"),
], {
    "title": "김장 생활템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

김장비용 2020년대 최저 🥬 김장 전에 챙길 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 에버튼하우스 스텐 대야 + 채반 세트 53cm 💛 품번 0166
절이기·버무리기·물빼기까지 한 세트로.

2. 대한명도 4세대 3단 두께조절 채칼 💛 품번 0167
두께 3단 조절, 무채 썰기가 한결 편해요.

3. 두껍고 질긴 김장봉투 소·중·대 💛 품번 0168
일반 비닐보다 두꺼운 김장봉투, 보관·나눔용으로.

✔ 올해 김장 적기: 중부 11월 하순~12월 초, 남부 12월 초~중순

※ 김장비용: 한국물가정보(세계일보·연합뉴스 11/16)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #김장 #김장준비 #채칼 #김장봉투""",
    "products": [prod(1, BOWL, N_BOWL, "C", "0166"), prod(2, SLICER, N_SLICER, "C", "0167"), prod(3, BAG, N_BAG, "C", "0168")],
})

write(DATE, "C2", [
    c_cover("주말 추위 절정 🥶", "빙판길·눈길", "대비 생활템", "BEST3", [CLEAT, COVER, SHOVEL]),
    c_prod(1, "0169", CLEAT, "도시형<br>아이젠", ["신발에 끼우는 미끄럼방지", "출퇴근·등하교용", "2+2 구성"],
           ["💰 4천원대", "📦 2+2"]),
    c_prod(2, "0170", COVER, "미끄럼방지<br>신발 커버", ["신발 위에 씌우는 덧신", "눈·비 오는 날 방수", "미끄럼방지 타입"],
           ["💰 5천원대", "📦 덧신"]),
    c_prod(3, "0171", SHOVEL, "접이식<br>눈삽", ["접어서 보관", "가벼운 제설도구", "현관·차 앞 눈 치우기"],
           ["💰 1만원대", "📦 접이식"]),
    c_howto("0169~0171"),
], {
    "title": "빙판길 대비 생활템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

주말 추위 절정 🥶 빙판길·눈길 대비 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 에버리즈 미끄럼방지 도시형 아이젠 2+2 💛 품번 0169
신발에 끼워 쓰는 출퇴근용 미끄럼방지 아이젠.

2. 고릴라몰 미끄럼방지 신발 방수 커버 💛 품번 0170
눈·비 오는 날 신발 위에 씌우는 덧신.

3. 접이식 경량 눈삽 제설도구 💛 품번 0171
접어서 보관하는 가벼운 눈삽.

✔ 19일 밤사이 눈·비가 얼어 도로 살얼음 주의, 이번 주말 추위 절정

※ 날씨: 기상청 예보(SBS·월요신문 11/19)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #빙판길 #아이젠 #눈삽 #겨울필수템""",
    "products": [prod(1, CLEAT, N_CLEAT, "C", "0169"), prod(2, COVER, N_COVER, "C", "0170"), prod(3, SHOVEL, N_SHOVEL, "C", "0171")],
})
print("ok")
