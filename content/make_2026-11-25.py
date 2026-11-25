"""2026-11-25(수, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-25/{A,B,C,A2,B2,C2}
점심: 아침 영하 8도·밤부터 중부 강풍 → 따뜻한 점심 특이템 / 퇴근길: 26일 서울 15도·27일 20도 기온 롤러코스터 → 겹쳐입기템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-25"
DL = "2026.11.25 (수)"
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



BOX, JUK, CUSH = "9785769611", "9702275066", "9750788589"
VEST, MUF, DUCK = "2303809571", "7650971425", "7945325075"
N_BOX = "직장인 휴대용 전기 도시락 스팀 가열 2단 (스테인리스 용기 4개)"
N_JUK = "트윙고 라스텐 보온죽통 TWL-FJ400TG 400ml"
N_CUSH = "WHH 사계절 쿠션담요 2in1 접이식 낮잠이불"
N_VEST = "TOPBOY 남녀공용 라운드넥 지퍼 경량 패딩조끼"
N_MUF = "아웃도어프로덕츠 방한 패딩 머플러"
N_DUCK = "루시아이 오리 웜핸드 쿠션 담요"

# ═════════ A · 점심 12:00 — 파주·포천 영하 8도 아침 ═════════
SRC1 = "출처: 스페셜타임스·코리안투데이(11/25) — 기상청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>오늘 아침<br><span class="hl">영하 8도</span></h1>
<p class="lead">파주·포천 꽁꽁<br>밤부터 중부 강풍</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(25일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>-8~3도</strong></div><div><small>낮 최고</small><strong>4~12도</strong></div></div>
<div class="box">서울 <b class="hl">-4도 → 7도</b><br>일교차 <b class="hl">11도</b> · 춘천 -8도 → 5도</div>""", SRC1, DL),
    a_slide(3, n, """<h2>밤부터 <span class="hl">바람 주의</span></h2>
<ul class="chk"><li>중부·경북 동해안 <span class="hl">강풍 가능</span></li><li>현수막·나뭇가지 <span class="hl">낙하물 조심</span></li><li>체감온도 <span class="hl">크게 내려가요</span></li><li>미세먼지 대체로 <span class="hl">좋음~보통</span></li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>눈·비 & <span class="hl">살얼음</span></h2>
<ul class="chk"><li>인천·경기·충남 서해안 <span class="hl">비 또는 눈</span></li><li>강수량 <span class="hl">1mm 미만</span> · 적설 1cm 미만</li><li>눈·비 내린 곳 <span class="hl">도로 살얼음</span></li><li>점심은 <span class="hl">따뜻하게</span> 챙기기</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>추운 날 <span class="hl">따뜻한 점심템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BOX)}"><div>스팀 가열 전기 도시락<span>2단 · 스텐 용기 4개</span></div></li>
<li><b>2</b><img src="{img(JUK)}"><div>미니 보온죽통 400ml<span>트윙고 라스텐</span></div></li>
<li><b>3</b><img src="{img(CUSH)}"><div>2in1 쿠션담요<span>WHH · 접으면 쿠션</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/25 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "오늘 아침 영하 8도, 밤부터 중부 강풍",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘 아침 파주·포천 영하 8도 🥶 밤부터는 중부 강풍

· 25일(수) 아침 최저 영하 8도~영상 3도, 낮 최고 4~12도
· 서울 영하 4도→7도(일교차 11도), 춘천 영하 8도→5도, 대전 영하 3도→9도, 부산 영하 1도→10도
· 인천·경기 서해안, 충남 북부 서해안 비 또는 눈(1mm 미만, 적설 1cm 미만)
· 밤부터 중부지방·경북 동해안 중심 강풍 — 현수막·나뭇가지 낙하물 주의
· 미세먼지 서울·인천 '보통', 그 밖 '좋음'

✔ 눈·비 내린 곳은 도로 살얼음 조심
✔ 일교차 커서 겉옷은 한 겹 더

🔗 추운 날 따뜻한 점심템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 스페셜타임스(2026.11.25)·코리안투데이(2026.11.25) — 기상청 예보

#광고 #생활뉴스 #날씨 #영하권 #강풍 #도시락 #점심""",
    "products": [prod(1, BOX, N_BOX, "A"), prod(2, JUK, N_JUK, "A"), prod(3, CUSH, N_CUSH, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 기온 롤러코스터 ═════════
SRC2 = "출처: 위키트리·톱스타뉴스(11/24) — 기상청"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>내일은 <span class="hl">15도</span><br>기온 롤러코스터</h1>
<p class="lead">금요일엔 낮 최고 20도<br>반짝 포근</p>""", SRC2, DL),
    a_slide(2, n, """<h2>내일(26일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>-2~8도</strong></div><div><small>낮 최고</small><strong>12~18도</strong></div></div>
<div class="box">서울 <b class="hl">4도 → 15도</b><br>오늘보다 아침·낮 모두 <b class="hl">8도↑</b></div>""", SRC2, DL),
    a_slide(3, n, """<h2>금요일(27일) <span class="hl">반짝 포근</span></h2>
<ul class="chk"><li>낮 최고 <span class="hl">20도</span>까지</li><li>수도권·강원 내륙·충청 북부 <span class="hl">비</span></li><li>비는 <span class="hl">오전~낮</span> 사이</li><li>남부·제주는 대체로 <span class="hl">맑음</span></li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>이럴 땐 <span class="hl">이렇게</span></h2>
<ul class="chk"><li>아침·낮 <span class="hl">일교차 11도 안팎</span></li><li>겉옷은 <span class="hl">벗고 입기 쉽게</span></li><li>동해안 <span class="hl">건조특보</span> · 불씨 조심</li><li>급한 기온 변화에 <span class="hl">건강 관리</span></li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>롤러코스터 날씨 <span class="hl">겹쳐입기템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(VEST)}"><div>경량 패딩조끼<span>TOPBOY · 남녀공용</span></div></li>
<li><b>2</b><img src="{img(MUF)}"><div>방한 패딩 머플러<span>아웃도어프로덕츠</span></div></li>
<li><b>3</b><img src="{img(DUCK)}"><div>오리 웜핸드 쿠션<span>루시아이 · 담요 겸용</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/25 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "내일 서울 낮 15도, 금요일 20도 반짝 포근",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 오늘 영하 → 내일 15도 🎢 기온 롤러코스터

· 26일(목) 아침 최저 영하 2도~영상 8도, 낮 최고 12~18도
· 서울 아침 4도·낮 15도 — 25일보다 아침·낮 모두 8도가량 올라요
· 27일(금) 낮 최고 20도까지 '반짝 포근', 수도권·강원 내륙·충청 북부는 오전~낮 비
· 강원 영동·경북 북부 동해안 건조특보 — 산불·화재 주의

✔ 일교차 크니 벗고 입기 쉬운 겹쳐 입기
✔ 금요일 수도권 출근길 우산 챙기기

🔗 롤러코스터 날씨 겹쳐입기템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 위키트리(2026.11.24)·톱스타뉴스(2026.11.24) — 기상청 예보

#광고 #생활뉴스 #날씨 #일교차 #경량패딩 #머플러 #겹쳐입기""",
    "products": [prod(1, VEST, N_VEST, "A"), prod(2, MUF, N_MUF, "A"), prod(3, DUCK, N_DUCK, "A")],
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


write(DATE, "B", [poll("영하 8도 아침,<br>점심 도시락은? 🍱", "25일 아침 최저 -8~3도 · 기상청",
                       [("회사 전자레인지", "줄 서는 건 기본"), ("보온 도시락", "아침에 싸면 끝"),
                        ("그냥 사 먹기", "추워도 나간다"), ("전기 도시락", "책상에서 데우기")], BOX)], {
    "title": "추운 날 점심 도시락 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 영하 8도 아침, 오늘 점심 도시락은 어떻게? 🍱
댓글에 번호로 투표해주세요!

1️⃣ 회사 전자레인지 줄 서기
2️⃣ 보온 도시락
3️⃣ 그냥 사 먹기
4️⃣ 책상에서 데우는 전기 도시락

※ 25일 아침 최저 영하 8도~영상 3도, 서울 영하 4도→7도 — 밤부터 중부 강풍 (기상청 예보, 스페셜타임스 11/25)

🔗 4번 스팀 가열 전기 도시락 링크는 프로필에
👥 점심 같이 먹는 사람 태그

#광고 #투표 #공감 #점심 #도시락 #직장인""",
    "products": [prod(1, BOX, N_BOX, "B")],
})

write(DATE, "B2", [poll("오늘 영하, 내일 15도<br>내 옷차림은? 🎢", "26일 서울 4도→15도 · 기상청",
                        [("롱패딩 고수", "춥다 했다가 덥다 함"), ("코트 하나로", "멋이 우선"),
                         ("후드티 + 맨투맨", "버틸 수 있다"), ("경량 패딩조끼", "벗었다 입었다")], VEST)], {
    "title": "기온 롤러코스터 옷차림 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 오늘 영하, 내일 15도… 내 옷차림은? 🎢
댓글에 번호로 투표해주세요!

1️⃣ 롱패딩 고수
2️⃣ 코트 하나로
3️⃣ 후드티 + 맨투맨
4️⃣ 경량 패딩조끼로 겹쳐 입기

※ 26일 서울 아침 4도·낮 15도, 27일(금) 낮 최고 20도까지 오를 전망 (기상청 예보, 위키트리 11/24)

🔗 4번 경량 패딩조끼 링크는 프로필에
👥 옷 고민하는 친구 태그

#광고 #투표 #공감 #옷차림 #일교차 #경량패딩""",
    "products": [prod(1, VEST, N_VEST, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/25 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("오늘 아침 영하 8도 🥶", "추운 날", "따뜻한 점심", "BEST3", [BOX, JUK, CUSH]),
    c_prod(1, "0202", BOX, "스팀 가열<br>전기 도시락", ["플러그 꽂아 스팀 가열", "2단 구성", "스테인리스 용기 4개"],
           ["💰 2만원대", "📦 2단"]),
    c_prod(2, "0203", JUK, "미니<br>보온죽통", ["트윙고 라스텐", "400ml 1인용", "스텐 보온 도시락"],
           ["💰 1만원대", "📦 400ml"]),
    c_prod(3, "0204", CUSH, "2in1<br>쿠션담요", ["WHH 사계절 쿠션담요", "펼치면 낮잠이불", "사무실·차량용"],
           ["💰 1만원대", "📦 쿠션+담요"]),
    c_howto("0202~0204"),
], {
    "title": "추운 날 따뜻한 점심 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

오늘 아침 영하 8도 🥶 추운 날 따뜻한 점심 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 직장인 휴대용 전기 도시락 스팀 가열 2단 💛 품번 0202
책상에서 플러그 꽂고 스팀으로 데우는 도시락.

2. 트윙고 라스텐 보온죽통 400ml 💛 품번 0203
아침에 담은 국·죽을 따뜻하게.

3. WHH 사계절 쿠션담요 2in1 💛 품번 0204
평소엔 쿠션, 펼치면 점심 낮잠 담요.

✔ 25일 아침 최저 영하 8도~영상 3도, 서울 일교차 11도 — 밤부터 중부 강풍

※ 날씨: 기상청 예보(스페셜타임스·코리안투데이 11/25)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #전기도시락 #보온죽통 #쿠션담요 #직장인점심""",
    "products": [prod(1, BOX, N_BOX, "C", "0202"), prod(2, JUK, N_JUK, "C", "0203"), prod(3, CUSH, N_CUSH, "C", "0204")],
})

write(DATE, "C2", [
    c_cover("내일 15도, 금요일 20도 🎢", "롤러코스터 날씨", "겹쳐입기템", "BEST3", [VEST, MUF, DUCK]),
    c_prod(1, "0205", VEST, "경량<br>패딩조끼", ["TOPBOY 남녀공용", "라운드넥 지퍼", "코트 안에 겹쳐 입기"],
           ["💰 1만원대", "📦 조끼"]),
    c_prod(2, "0206", MUF, "방한<br>패딩 머플러", ["아웃도어프로덕츠", "패딩 소재 목도리", "더우면 풀어서 가방에"],
           ["💰 2만원대", "📦 머플러"]),
    c_prod(3, "0207", DUCK, "오리<br>웜핸드 쿠션", ["루시아이", "손 넣는 오리 쿠션", "담요 겸용"],
           ["💰 1만원대", "📦 쿠션+담요"]),
    c_howto("0205~0207"),
], {
    "title": "롤러코스터 날씨 겹쳐입기템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

오늘 영하 → 내일 15도 🎢 롤러코스터 날씨 겹쳐입기템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. TOPBOY 남녀공용 라운드넥 지퍼 경량 패딩조끼 💛 품번 0205
코트·재킷 안에 겹쳐 입고, 더우면 벗기.

2. 아웃도어프로덕츠 방한 패딩 머플러 💛 품번 0206
아침엔 두르고 낮엔 풀어서 가방에.

3. 루시아이 오리 웜핸드 쿠션 담요 💛 품번 0207
손 넣는 오리 쿠션, 담요까지 들어 있어요.

✔ 26일 서울 아침 4도·낮 15도, 27일(금) 낮 최고 20도 반짝 포근

※ 날씨: 기상청 예보(위키트리·톱스타뉴스 11/24)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #경량패딩조끼 #패딩머플러 #쿠션담요 #일교차""",
    "products": [prod(1, VEST, N_VEST, "C", "0205"), prod(2, MUF, N_MUF, "C", "0206"), prod(3, DUCK, N_DUCK, "C", "0207")],
})
print("ok")
