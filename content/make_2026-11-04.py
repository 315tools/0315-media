"""2026-11-04(수, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-04/{A,B,C,A2,B2,C2}
점심: 독감 한 달 일찍·손 씻기 / 퇴근길: 5일 전국 비 뒤 7일 영하권·충전식 방한템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-04"
DL = "2026.11.04 (수)"
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





DISP, TBR, KEY = "9640305791", "9668475716", "9640148209"
HAND, FOOT, NECK = "9207288847", "9063031376", "9306852022"
N_DISP = "LOMESO 자동 디스펜서 젤/거품 420ml 충전식"
N_TBR = "투비뉴 휴대용 UVC LED 무선 칫솔살균기 TO-TB25"
N_KEY = "플르부아 그린 플로럴 하트 키링 새니타이저"
N_HAND = "모란카노 마그네틱 듀얼 손난로 6000mAh"
N_FOOT = "스토렐라 곰발바닥 USB 발열쿠션 발난로"
N_NECK = "USB 발열목도리 충전식 온열 넥워머"

# ═════════ A · 점심 12:00 — 독감 한 달 일찍 ═════════
SRC1 = "출처: 파이낸셜뉴스(11/3)·세계일보(9/11), 질병관리청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">건강 · 생활정보</div>
<h1>올해 독감<br><span class="hl">한 달 일찍</span><br>찾아왔다</h1>
<p class="lead">유행주의보 9월 11일 발령<br>작년(10월 17일)보다 약 한 달 빨라</p>""", SRC1, DL),
    a_slide(2, n, """<h2>숫자로 보는 올해 독감</h2>
<div class="fig"><div><small>유행주의보</small><strong>9/11</strong></div><div><small>작년 발령</small><strong>10/17</strong></div></div>
<div class="fig"><div><small>9월 초 의심환자</small><strong>25.3명</strong></div><div><small>작년 같은 주</small><strong>6.6명</strong></div></div>
<div class="box">외래 1천 명당 · 36주차 기준<br><b class="hl">약 3.8배</b> (유행 기준 12.9명)</div>""", SRC1, DL),
    a_slide(3, n, """<h2>질병청이 권하는 수칙</h2>
<ul class="chk"><li><span class="hl">손 자주 씻기</span></li><li>기침은 휴지·옷소매로 가리기</li><li>실내는 자주 환기</li><li>의심되면 진료 받기</li></ul>
<div class="box">백신은 면역 생기기까지 <b class="hl">약 2주</b><br>작년에 맞았어도 올해 다시</div>""", SRC1, DL),
    a_slide(4, n, """<h2>손 씻기 <span class="hl">귀찮지 않게</span></h2>
<ul class="chk"><li>펌프 누를 필요 없는 <span class="hl">자동 디스펜서</span></li><li>칫솔은 말려서 보관</li><li>밖에선 가방에 <span class="hl">휴대용 새니타이저</span></li><li>사무실 창문 한 번씩 열기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>손 씻기 돕는 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(DISP)}"><div>LOMESO 자동 디스펜서<span>젤/거품 겸용 · 420ml · 충전식</span></div></li>
<li><b>2</b><img src="{img(TBR)}"><div>투비뉴 휴대용 칫솔살균기<span>UVC LED · 무선 · 벽걸이</span></div></li>
<li><b>3</b><img src="{img(KEY)}"><div>플르부아 하트 키링<span>가방에 거는 새니타이저</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/4 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "올해 독감 한 달 일찍",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 올해 독감, 작년보다 한 달 일찍 찾아왔어요 🤧

· 질병관리청 인플루엔자 유행주의보 9월 11일 발령 — 작년(10월 17일)보다 약 한 달 빨라
· 9월 초(36주차) 외래 1천 명당 의심환자 25.3명 — 작년 같은 주 6.6명의 약 3.8배 (유행 기준 12.9명)
· 백신은 면역이 생기기까지 약 2주 — 작년에 맞았어도 올해 다시 접종
· 손 자주 씻기, 기침은 휴지·옷소매로, 실내 자주 환기

✔ 독감이 의심되면 참지 말고 진료 받기

🔗 손 씻기 돕는 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 파이낸셜뉴스(11/3)·세계일보(9/11) — 질병관리청

#광고 #생활뉴스 #독감 #인플루엔자 #손씻기 #자동디스펜서 #칫솔살균기 #특이템""",
    "products": [prod(1, DISP, N_DISP, "A"), prod(2, TBR, N_TBR, "A"), prod(3, KEY, N_KEY, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 비 뒤 주말 영하권 ═════════
SRC2 = "출처: 업코리아(11/4)·경향신문(11/3), 기상청 예보"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 이번 주</div>
<h1>내일 전국 비<br>토요일엔<br><span class="hl">영하권</span></h1>
<p class="lead">7일(토) 아침 -4~5도<br>낮 7~14도</p>""", SRC2, DL),
    a_slide(2, n, """<h2>이번 주 날씨</h2>
<div class="fig"><div><small>오늘(4일) 낮</small><strong>15~19도</strong></div><div><small>5일(목)</small><strong>전국 비</strong></div></div>
<div class="fig"><div><small>7일(토) 아침</small><strong>-4~5도</strong></div><div><small>7일 낮</small><strong>7~14도</strong></div></div>
<div class="box">5일 광주·전남·부산·경남 <b class="hl">10~40mm</b><br>수도권 5mm 안팎</div>""", SRC2, DL),
    a_slide(3, n, """<h2>영하권 오기 전 체크</h2>
<ul class="chk"><li>목요일엔 우산 챙기기</li><li>주말 아침엔 <span class="hl">두꺼운 외투</span></li><li>손·발·목 <span class="hl">세 곳</span>을 따뜻하게</li><li>충전식 방한템은 미리 충전</li></ul>""", SRC2, DL),
    a_slide(4, n, f"""<h2>충전해 쓰는 <span class="hl">방한 특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(HAND)}"><div>모란카노 듀얼 손난로<span>자석으로 붙는 2개 · 6000mAh</span></div></li>
<li><b>2</b><img src="{img(FOOT)}"><div>스토렐라 곰발바닥 발난로<span>USB 발열쿠션</span></div></li>
<li><b>3</b><img src="{img(NECK)}"><div>USB 발열목도리<span>충전식 온열 넥워머</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/4 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "내일 전국 비·토요일 영하권",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 내일(5일) 전국 비, 토요일(7일) 아침엔 영하권 🥶

· 오늘(4일) 아침 3~11도, 낮 15~19도 (서울 8도→18도)
· 5일 제주 10~40mm(산지 20~60mm), 광주·전남·부산·울산·경남 10~40mm, 수도권 5mm 안팎
· 7일(토) 아침 -4~5도, 낮 7~14도 — 영하권 추위가 나타나는 곳 있어
· 이번 주말 서울 등 중부지방 대부분 영하권 추위 예보

✔ 목요일엔 우산, 주말 아침엔 두꺼운 외투 챙기기

🔗 충전해 쓰는 방한 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 업코리아(11/4)·경향신문(11/3) — 기상청 예보

#광고 #생활뉴스 #날씨 #영하권 #비소식 #손난로 #발난로 #넥워머""",
    "products": [prod(1, HAND, N_HAND, "A"), prod(2, FOOT, N_FOOT, "A"), prod(3, NECK, N_NECK, "A")],
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


write(DATE, "B", [poll("독감 벌써 유행,<br>나의 손 씻기는? 🧼", "유행주의보 작년보다 한 달 일찍 (질병관리청)",
                       [("물만 휙", "3초면 충분하지"), ("비누로 30초", "나는 모범 시민"),
                        ("밥 먹기 전에만", "그게 어디야"), ("자동 디스펜서", "손만 대면 거품이 쓱")], DISP)], {
    "title": "손 씻기 스타일 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 독감 벌써 유행, 나의 손 씻기 스타일은? 🧼
댓글에 번호로 투표해주세요!

1️⃣ 물만 휙
2️⃣ 비누로 30초
3️⃣ 밥 먹기 전에만
4️⃣ 자동 디스펜서

※ 인플루엔자 유행주의보 9/11 발령, 작년(10/17)보다 약 한 달 일찍 (질병관리청)

🔗 4번 LOMESO 자동 디스펜서 링크는 프로필에
👥 화장실 다녀와서 물만 묻히는 친구 태그

#광고 #투표 #공감 #독감 #손씻기 #자동디스펜서""",
    "products": [prod(1, DISP, N_DISP, "B")],
})

write(DATE, "B2", [poll("토요일 영하권,<br>제일 먼저 시린 곳은? 🥶", "7일 아침 -4~5도 (기상청 예보)",
                        [("손끝", "폰 만지다 얼어버림"), ("발끝", "양말 두 겹도 소용없음"),
                         ("목덜미", "바람이 슝"), ("주머니 속 손난로", "이거 하나면 해결")], HAND)], {
    "title": "제일 먼저 시린 곳 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 토요일 영하권, 제일 먼저 시린 곳은? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 손끝
2️⃣ 발끝
3️⃣ 목덜미
4️⃣ 주머니 속 손난로 (이미 해결)

※ 7일(토) 아침 -4~5도, 낮 7~14도 (기상청 예보)

🔗 4번 모란카노 듀얼 손난로 링크는 프로필에
👥 손 차가운 친구 태그

#광고 #투표 #공감 #영하권 #추위 #손난로""",
    "products": [prod(1, HAND, N_HAND, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/4 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("독감 한 달 일찍", "손 씻기 돕는", "특이템", "BEST3", [DISP, TBR, KEY]),
    c_prod(1, "0076", DISP, "LOMESO<br>자동 디스펜서", ["손 대면 젤·거품이 쓱", "420ml 대용량", "C타입 충전식"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0077", TBR, "투비뉴<br>휴대용 칫솔살균기", ["UVC LED 무선", "벽걸이·휴대 겸용", "C타입 충전"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0078", KEY, "플르부아<br>하트 키링", ["가방에 거는 새니타이저", "하트 모양 키링", "그린 플로럴 향"],
           ["💰 1만원대", "📦 무료배송"]),
    c_howto("0076~0078"),
], {
    "title": "손 씻기 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

독감 한 달 일찍 🧼 손 씻기 돕는 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. LOMESO 자동 디스펜서 젤/거품 420ml 💛 품번 0076
손만 대면 나오는 충전식 디스펜서, 젤·거품 겸용.

2. 투비뉴 휴대용 UVC LED 칫솔살균기 💛 품번 0077
무선이라 벽에 붙이거나 들고 다니기.

3. 플르부아 하트 키링 새니타이저 💛 품번 0078
가방에 걸어 두는 하트 모양 새니타이저.

※ 독감: 질병관리청 유행주의보 9/11 발령(파이낸셜뉴스 11/3 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #특이템 #자동디스펜서 #칫솔살균기 #손씻기 #독감""",
    "products": [prod(1, DISP, N_DISP, "C", "0076"), prod(2, TBR, N_TBR, "C", "0077"), prod(3, KEY, N_KEY, "C", "0078")],
})

write(DATE, "C2", [
    c_cover("토요일 영하권", "충전해 쓰는", "방한템", "BEST3", [HAND, FOOT, NECK]),
    c_prod(1, "0079", HAND, "모란카노<br>듀얼 손난로", ["자석으로 붙는 2개", "6000mAh 충전식", "둘이 나눠 쓰기"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0080", FOOT, "스토렐라<br>곰발바닥 발난로", ["곰발바닥 모양 발열쿠션", "USB 전원", "책상 밑 발 시릴 때"],
           ["💰 1만원대", "📦 무료배송"]),
    c_prod(3, "0081", NECK, "USB<br>발열목도리", ["충전식 온열 넥워머", "패딩 머플러형", "목덜미 바람 차단"],
           ["💰 1만원대", "📦 무료배송"]),
    c_howto("0079~0081"),
], {
    "title": "충전식 방한템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

토요일 영하권 🥶 충전해 쓰는 방한 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 모란카노 마그네틱 듀얼 손난로 6000mAh 💛 품번 0079
자석으로 붙었다 떨어지는 손난로 2개.

2. 스토렐라 곰발바닥 USB 발열쿠션 발난로 💛 품번 0080
책상 밑 시린 발을 곰발바닥으로.

3. USB 발열목도리 충전식 온열 넥워머 💛 품번 0081
목덜미 바람 막는 충전식 머플러.

※ 날씨: 기상청 예보(업코리아 11/4·경향신문 11/3 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #특이템 #손난로 #발난로 #넥워머 #영하권""",
    "products": [prod(1, HAND, N_HAND, "C", "0079"), prod(2, FOOT, N_FOOT, "C", "0080"), prod(3, NECK, N_NECK, "C", "0081")],
})
print("ok")
