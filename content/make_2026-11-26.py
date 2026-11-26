"""2026-11-26(목, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-26/{A,B,C,A2,B2,C2}
점심: 낮 최고 18도 포근·미세먼지 좋음 → 포근한 날 대청소템 / 퇴근길: 금 21도 → 토 낮 7~13도 다시 쌀쌀 → 샤워 후 보송 따뜻템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-26"
DL = "2026.11.26 (목)"
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

WIN, DUST, MAGIC = "7660460402", "8023977745", "7790158804"
CAP, GOWN, MAT = "8925430404", "9761240494", "9012669893"
N_WIN = "코아 강도조절 자석 유리창 유리닦이 5-25mm"
N_DUST = "지니홀딩스 길이 연장 극세사 먼지털이개"
N_MAGIC = "코멧 매직블럭 중형 100개 + 집게핀"
N_CAP = "솔버 빨리 마르는 헤어캡 2개"
N_GOWN = "좋은 하루 극세사 샤워가운 남녀공용"
N_MAT = "디아르 프리미엄 극세사 미끄럼방지 발매트"

# ═════════ A · 점심 12:00 — 낮 18도 포근 ═════════
SRC1 = "출처: 게임톡(11/26)·M이코노미뉴스(11/25) — 기상청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>오늘 낮<br><span class="hl">최고 18도</span><br>포근한 목요일</h1>
<p class="lead">미세먼지도 대부분 '좋음'<br>내일은 21도까지</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(26일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>-3~9도</strong></div><div><small>낮 최고</small><strong>13~18도</strong></div></div>
<div class="box">서울 <b class="hl">5도 → 16도</b><br>대구 0도 → 16도 · 제주 8도 → 20도</div>""", SRC1, DL),
    a_slide(3, n, """<h2>아침 안개 · <span class="hl">건조 주의</span></h2>
<ul class="chk"><li>전북·경북 내륙 <span class="hl">짙은 안개</span></li><li>가시거리 <span class="hl">1km 미만</span>인 곳도</li><li>강원 영동·경북 북부 동해안 <span class="hl">매우 건조</span></li><li>산불·불씨 <span class="hl">조심</span></li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>포근한 날 <span class="hl">해두면 좋은 것</span></h2>
<ul class="chk"><li>창문 열고 <span class="hl">환기</span>하기</li><li>겨울 전 <span class="hl">유리창 닦기</span></li><li>높은 곳 <span class="hl">먼지 털기</span></li><li>내일(27일) 수도권 <span class="hl">오전~낮 비</span></li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>포근한 날 <span class="hl">대청소템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(WIN)}"><div>자석 유리창닦이<span>코아 · 강도 조절</span></div></li>
<li><b>2</b><img src="{img(DUST)}"><div>연장 극세사 먼지털이<span>지니홀딩스 · 길이 연장</span></div></li>
<li><b>3</b><img src="{img(MAGIC)}"><div>매직블럭 중형 100개<span>코멧 · 집게핀 포함</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/26 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "오늘 낮 최고 18도 포근, 미세먼지 좋음",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘 낮 최고 18도 ☀️ 포근한 목요일

· 26일(목) 아침 최저 영하 3도~영상 9도, 낮 최고 13~18도
· 서울 5도→16도, 대전 4도→16도, 대구 0도→16도, 부산 6도→17도, 제주 8도→20도
· 미세먼지 대부분 지역 '좋음'
· 새벽~아침 전북 내륙·경북 중북부 내륙 가시거리 1km 미만 안개
· 강원 영동·경북 북부 동해안 대기 매우 건조 — 산불 주의
· 27일(금) 낮 최고 15~21도, 수도권은 오전~낮 비

✔ 포근할 때 창문 열고 환기
✔ 겨울 전에 유리창·높은 곳 먼지 정리

🔗 포근한 날 대청소템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 게임톡(2026.11.26)·M이코노미뉴스(2026.11.25) — 기상청 예보

#광고 #생활뉴스 #날씨 #포근 #대청소 #유리창청소 #생활용품""",
    "products": [prod(1, WIN, N_WIN, "A"), prod(2, DUST, N_DUST, "A"), prod(3, MAGIC, N_MAGIC, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 토요일 다시 쌀쌀 ═════════
SRC2 = "출처: 게임톡(11/26)·국제뉴스(11/25) — 기상청"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>금요일 21도<br>토요일 <span class="hl">다시 쌀쌀</span></h1>
<p class="lead">토요일 낮 최고 7~13도<br>하루 만에 뚝</p>""", SRC2, DL),
    a_slide(2, n, """<h2>금(27일) → 토(28일) <span class="hl">낮 기온</span></h2>
<div class="fig"><div><small>27일 낮 최고</small><strong>15~21도</strong></div><div><small>28일 낮 최고</small><strong>7~13도</strong></div></div>
<div class="box">27일 아침 최저 <b class="hl">1~11도</b><br>평년보다 높다가 토요일 <b class="hl">쌀쌀</b></div>""", SRC2, DL),
    a_slide(3, n, """<h2>금요일 <span class="hl">비 소식</span></h2>
<ul class="chk"><li>수도권 <span class="hl">오전~낮</span> · 5mm 미만</li><li>강원 내륙·산지 <span class="hl">5mm 미만</span></li><li>충청권·전북 <span class="hl">1mm 안팎</span></li><li>출근길 <span class="hl">우산</span> 챙기기</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>토요일엔 <span class="hl">비 또는 눈</span></h2>
<ul class="chk"><li>새벽 <span class="hl">전라권</span></li><li>오전 경기 남부 서해안·충청권</li><li>경상 서부 내륙·제주 <span class="hl">비 또는 눈</span></li><li>쌀쌀한 주말 <span class="hl">샤워 후 보온</span></li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>샤워 후 <span class="hl">보송 따뜻템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(GOWN)}"><div>극세사 샤워가운<span>좋은 하루 · 남녀공용</span></div></li>
<li><b>2</b><img src="{img(CAP)}"><div>빨리 마르는 헤어캡<span>솔버 · 2개</span></div></li>
<li><b>3</b><img src="{img(MAT)}"><div>극세사 발매트<span>디아르 · 미끄럼방지</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/26 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "금요일 21도, 토요일 다시 쌀쌀",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 금요일 21도 → 토요일 다시 쌀쌀 🥶

· 27일(금) 아침 최저 1~11도, 낮 최고 15~21도 — 평년보다 높아요
· 27일 비: 수도권(오전~낮)·강원 내륙·산지 5mm 미만, 충청권·전북 1mm 안팎
· 28일(토) 낮 최고 7~13도로 내려가요
· 28일 새벽 전라권, 오전 경기 남부 서해안·충청권·경상 서부 내륙·제주 비 또는 눈

✔ 금요일 수도권 출근길 우산 챙기기
✔ 쌀쌀한 주말, 샤워 후 체온 지키기

🔗 샤워 후 보송 따뜻템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 게임톡(2026.11.26)·국제뉴스(2026.11.25) — 기상청 예보

#광고 #생활뉴스 #날씨 #주말날씨 #샤워가운 #헤어캡 #생활용품""",
    "products": [prod(1, GOWN, N_GOWN, "A"), prod(2, CAP, N_CAP, "A"), prod(3, MAT, N_MAT, "A")],
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


write(DATE, "B", [poll("낮 18도 포근한 날,<br>집에서 제일 먼저? ☀️", "26일 낮 최고 13~18도 · 기상청",
                       [("창문 활짝 환기", "공기부터 바꾸자"), ("밀린 빨래 돌리기", "이때다 싶음"),
                        ("그냥 누워 있기", "포근하면 더 졸림"), ("유리창 닦기", "자석 창문닦이로 안팎 한 번에")], WIN)], {
    "title": "포근한 날 집에서 할 일 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 낮 18도 포근한 날, 집에서 제일 먼저 할 일은? ☀️
댓글에 번호로 투표해주세요!

1️⃣ 창문 활짝 환기
2️⃣ 밀린 빨래 돌리기
3️⃣ 그냥 누워 있기
4️⃣ 자석 창문닦이로 유리창 닦기

※ 26일 아침 최저 영하 3도~영상 9도, 낮 최고 13~18도, 미세먼지 대부분 '좋음' (기상청 예보, 게임톡 11/26)

🔗 4번 자석 유리창닦이 링크는 프로필에
👥 대청소 미루는 친구 태그

#광고 #투표 #공감 #대청소 #환기 #생활용품""",
    "products": [prod(1, WIN, N_WIN, "B")],
})

write(DATE, "B2", [poll("주말 다시 쌀쌀,<br>샤워 후 나는? 🚿", "28일 낮 최고 7~13도 · 기상청",
                        [("수건 두르고 전력질주", "방까지 3초"), ("욕실에서 옷 다 입기", "김 서린 채로"),
                         ("난방 미리 올려두기", "준비성 만렙"), ("극세사 샤워가운", "걸치면 끝")], GOWN)], {
    "title": "샤워 후 추위 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 주말 다시 쌀쌀… 샤워하고 나올 때 나는? 🚿
댓글에 번호로 투표해주세요!

1️⃣ 수건 두르고 방까지 전력질주
2️⃣ 욕실에서 옷 다 입고 나오기
3️⃣ 난방 미리 올려두기
4️⃣ 극세사 샤워가운 걸치기

※ 27일(금) 낮 최고 15~21도 → 28일(토) 7~13도 (기상청 예보, 게임톡 11/26)

🔗 4번 극세사 샤워가운 링크는 프로필에
👥 샤워 후 추위 타는 친구 태그

#광고 #투표 #공감 #샤워 #주말날씨 #샤워가운""",
    "products": [prod(1, GOWN, N_GOWN, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/26 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("오늘 낮 최고 18도 ☀️", "포근한 날", "대청소템", "BEST3", [WIN, DUST, MAGIC]),
    c_prod(1, "0208", WIN, "자석<br>유리창닦이", ["코아 강도조절", "안팎 동시에 닦기", "유리 두께 5~25mm"],
           ["💰 3만원대", "📦 1개"]),
    c_prod(2, "0209", DUST, "연장 극세사<br>먼지털이", ["지니홀딩스", "길이 연장", "천장·높은 곳 먼지"],
           ["💰 1만원 미만", "📦 1개"]),
    c_prod(3, "0210", MAGIC, "매직블럭<br>중형 100개", ["코멧", "물만 묻혀 문지르기", "집게핀 1개 포함"],
           ["💰 1만원 미만", "📦 100개"]),
    c_howto("0208~0210"),
], {
    "title": "포근한 날 대청소템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

오늘 낮 최고 18도 ☀️ 포근한 날 대청소템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 코아 강도조절 자석 유리창 유리닦이 💛 품번 0208
자석으로 유리창 안팎을 한 번에. 유리 두께 5~25mm용.

2. 지니홀딩스 길이 연장 극세사 먼지털이개 💛 품번 0209
손 안 닿는 천장·높은 곳 먼지까지.

3. 코멧 매직블럭 중형 100개 + 집게핀 💛 품번 0210
물만 묻혀 문지르는 청소 스펀지 대용량.

✔ 26일 낮 최고 13~18도, 미세먼지 대부분 '좋음' — 환기·대청소하기 좋은 날

※ 날씨: 기상청 예보(게임톡 11/26·M이코노미뉴스 11/25)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #자석창문닦이 #먼지털이 #매직블럭 #대청소""",
    "products": [prod(1, WIN, N_WIN, "C", "0208"), prod(2, DUST, N_DUST, "C", "0209"), prod(3, MAGIC, N_MAGIC, "C", "0210")],
})

write(DATE, "C2", [
    c_cover("금 21도 → 토 낮 7~13도 🥶", "샤워 후", "보송 따뜻템", "BEST3", [GOWN, CAP, MAT]),
    c_prod(1, "0211", GOWN, "극세사<br>샤워가운", ["좋은 하루", "남녀공용", "샤워 후 바로 걸치기"],
           ["💰 1만원대", "📦 1벌"]),
    c_prod(2, "0212", CAP, "빨리 마르는<br>헤어캡", ["솔버", "젖은 머리 감싸기", "2개 구성"],
           ["💰 1만원 미만", "📦 2개"]),
    c_prod(3, "0213", MAT, "극세사<br>발매트", ["디아르 프리미엄", "미끄럼방지", "욕실 앞 보송하게"],
           ["💰 1만원대", "📦 1개"]),
    c_howto("0211~0213"),
], {
    "title": "샤워 후 보송 따뜻템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

금요일 낮 21도 → 토요일 낮 7~13도 🥶 샤워 후 보송 따뜻템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 좋은 하루 극세사 샤워가운 남녀공용 💛 품번 0211
샤워하고 나오자마자 걸치는 극세사 가운.

2. 솔버 빨리 마르는 헤어캡 2개 💛 품번 0212
젖은 머리를 감싸 두는 헤어캡.

3. 디아르 프리미엄 극세사 미끄럼방지 발매트 💛 품번 0213
욕실 앞 맨발을 보송하게.

✔ 27일(금) 낮 최고 15~21도 → 28일(토) 7~13도, 주말 다시 쌀쌀

※ 날씨: 기상청 예보(게임톡 11/26·국제뉴스 11/25)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #샤워가운 #헤어캡 #발매트 #주말날씨""",
    "products": [prod(1, GOWN, N_GOWN, "C", "0211"), prod(2, CAP, N_CAP, "C", "0212"), prod(3, MAT, N_MAT, "C", "0213")],
})
print("ok")
