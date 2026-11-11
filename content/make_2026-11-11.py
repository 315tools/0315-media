"""2026-11-11(수, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-11/{A,B,C,A2,B2,C2}
점심: 아침 짙은 안개·일교차 15도 → 흐린 유리 특이템 / 퇴근길: 수능 D-8 → 수험생 응원템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-11"
DL = "2026.11.11 (수)"
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



FOG, MIRROR, DRY = "6976280145", "9062665363", "9811887422"
WATCH, YEOT, BLANKET = "8366678245", "7623011291", "9798276856"
N_FOG = "더클래스 안티포그 김서림 방지제 120ml 2개"
N_MIRROR = "누띤 김서림 방지 사이드미러·창문 방수필름 세트"
N_DRY = "변색 확인 차량용 고흡습 제습백 (재사용)"
N_WATCH = "슈페르바 저소음 큰숫자 아날로그 수능시계"
N_YEOT = "옛다합격 행운합격엿 + 페레로로쉐 세트"
N_BLANKET = "양털 안감 체크 망토 담요 (무릎담요 겸용)"

# ═════════ A · 점심 12:00 — 짙은 안개·일교차 15도 → 운전 시야 특이템 ═════════
SRC1 = "출처: 데일리한국·게임톡(11/11), 톱스타뉴스(11/10) — 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">특이한 상품 · 오늘</div>
<h1>짙은 안개 출근길,<br><span class="hl">시야 확보</span> 먼저</h1>
<p class="lead">내륙 아침 영하권<br>낮밤 기온 차 15도 안팎</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(11일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>-2~6도</strong></div><div><small>전국 낮 최고</small><strong>14~19도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>5도</strong></div><div><small>서울 낮</small><strong>16도</strong></div></div>
<div class="box">낮밤 기온 차 <b class="hl">15도 안팎</b><br>내륙 중심 얼음 어는 곳·서리</div>""", SRC1, DL),
    a_slide(3, n, """<h2>오전 10시까지 <span class="hl">짙은 안개</span></h2>
<div class="box"><b class="hl">가시거리 200m 미만</b><br>경기 동부·강원 내륙·충북·경상 내륙</div>
<div class="box"><b class="hl">가시거리 1km 미만</b><br>인천·경기 서부·강원 산지·충남·전라</div>""", SRC1, DL),
    a_slide(4, n, """<h2>안개 낀 날 <span class="hl">운전</span></h2>
<ul class="chk"><li>전조등·안개등 <span class="hl">켜기</span></li><li>차간 거리 평소보다 넉넉히</li><li>다리 위·강·호수 근처 <span class="hl">더 짙어요</span></li><li>일부 도로 <span class="hl">살얼음</span> 조심</li></ul>""", "출처: 톱스타뉴스(11/10) — 기상청 예보", DL),
    a_slide(5, n, f"""<h2>흐린 유리 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FOG)}"><div>안티포그 김서림 방지제<span>뿌리고 닦는 스프레이</span></div></li>
<li><b>2</b><img src="{img(MIRROR)}"><div>사이드미러 방수필름<span>미러·창문 세트 · 헤라 포함</span></div></li>
<li><b>3</b><img src="{img(DRY)}"><div>차량용 고흡습 제습백<span>색 바뀌면 말려서 다시</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/11 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "짙은 안개·일교차 15도 운전 시야",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘 아침 곳곳 짙은 안개, 낮밤 기온 차 15도 안팎… 출근길 시야 확보 먼저 🌫️

· 11일(수) 전국 아침 최저 -2~6도, 낮 최고 14~19도 — 대체로 맑음
· 서울 아침 5도, 낮 16도
· 오전 10시까지 경기 동부·강원 내륙·충북·경상 내륙 가시거리 200m 미만 짙은 안개
· 인천·경기 서부·강원 산지·충남·전라도 가시거리 1km 미만
· 내륙 중심 얼음 어는 곳·서리, 일부 도로 살얼음

✔ 전조등·안개등 켜고 차간 거리 넉넉히
✔ 다리 위·강·호수 근처는 안개가 더 짙어요
✔ 그늘진 길·다리 위 살얼음 조심

🔗 흐린 유리 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 데일리한국·게임톡(11/11), 톱스타뉴스(11/10) — 기상청 예보

#광고 #생활뉴스 #날씨 #안개 #일교차 #출근길 #김서림방지""",
    "products": [prod(1, FOG, N_FOG, "A"), prod(2, MIRROR, N_MIRROR, "A"), prod(3, DRY, N_DRY, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 수능 D-8 ═════════
SRC2 = "출처: 머니투데이(9/8), 뉴시스(3/31), KB Think(10/14)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">특이한 상품 · 수능</div>
<h1>수능까지<br><span class="hl">D-8</span></h1>
<p class="lead">11월 19일(목) 시행<br>지금 챙길 준비물 체크</p>""", SRC2, DL),
    a_slide(2, n, """<h2>2027 수능 <span class="hl">일정</span></h2>
<div class="fig"><div><small>시험일</small><strong>11/19(목)</strong></div><div><small>지원자</small><strong>55만1864명</strong></div></div>
<div class="fig"><div><small>예비소집</small><strong>11/18(수)</strong></div><div><small>성적 통지</small><strong>12/11(금)</strong></div></div>
<div class="box">시험 당일 <b class="hl">오전 8시 10분</b>까지 입실</div>""", SRC2, DL),
    a_slide(3, n, """<h2>꼭 챙길 <span class="hl">준비물</span></h2>
<ul class="chk"><li><span class="hl">수험표</span> + 신분증</li><li>모바일 신분증은 <span class="hl">안 돼요</span></li><li>시계는 전자 기능 없는 <span class="hl">아날로그</span>만</li><li>컴퓨터용 사인펜은 시험장에서 줘요</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>가져가면 안 되는 <span class="hl">것</span></h2>
<ul class="chk"><li>휴대전화·스마트워치·이어폰</li><li>전자식 화면 있는 시계</li><li>보조배터리 등 <span class="hl">충전식 물품</span></li><li>실수로 가져왔다면<br>1교시 전 <span class="hl">감독관에게</span> 제출</li></ul>""", "출처: KB Think(10/14) · 최종 기준은 시험장 공지 확인", DL),
    a_slide(5, n, f"""<h2>수험생 응원 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(WATCH)}"><div>저소음 아날로그 수능시계<span>큰 숫자 · 손목시계</span></div></li>
<li><b>2</b><img src="{img(YEOT)}"><div>행운합격엿 + 페레로로쉐<span>딱 붙으라는 응원 세트</span></div></li>
<li><b>3</b><img src="{img(BLANKET)}"><div>양털 안감 망토 담요<span>공부할 때 어깨까지 폭</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/11 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "수능 D-8 준비물 체크",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 2027학년도 수능 D-8 ✏️ 11월 19일(목), 지금 챙길 준비물 체크

· 시험일 11월 19일(목), 성적 통지 12월 11일(금)
· 지원자 55만1864명 (한국교육과정평가원 집계)
· 예비소집 11월 18일(수), 당일 오전 8시 10분까지 입실
· 준비물: 수험표 + 신분증 (모바일 신분증 불가)
· 시계는 전자 기능·화면 없는 아날로그만
· 휴대전화·스마트워치·이어폰·보조배터리 등은 반입 금지 — 실수로 가져오면 1교시 전 감독관에게 제출
· 컴퓨터용 사인펜은 시험장에서 제공

✔ 최종 기준은 수험표·시험장 공지로 꼭 확인하세요
✔ 수험생 응원 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 머니투데이(2026.9.8), 뉴시스(2026.3.31), KB Think(2026.10.14)

#광고 #생활뉴스 #수능 #수능D8 #수험생 #수능준비물 #수능시계""",
    "products": [prod(1, WATCH, N_WATCH, "A"), prod(2, YEOT, N_YEOT, "A"), prod(3, BLANKET, N_BLANKET, "A")],
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




write(DATE, "B", [poll("짙은 안개 출근길,<br>제일 아찔한 순간은? 🌫️", "11일 오전 내륙 곳곳 가시거리 200m 미만 (기상청 예보)",
                       [("앞차가 안 보일 때", "브레이크등만 빨갛게"), ("다리 위 살얼음", "괜히 핸들 꽉"),
                        ("깜빡이 없이 끼어들기", "안개 속 기습"), ("앞유리 김서림", "닦아도 또 뿌옇게")], FOG)], {
    "title": "안개 출근길 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 짙은 안개 출근길, 제일 아찔한 순간은? 🌫️
댓글에 번호로 투표해주세요!

1️⃣ 앞차가 안 보일 때
2️⃣ 다리 위 살얼음
3️⃣ 깜빡이 없이 끼어들기
4️⃣ 앞유리 김서림

※ 11일(수) 오전 10시까지 경기 동부·강원 내륙·충북·경상 내륙 가시거리 200m 미만, 낮밤 기온 차 15도 안팎 (기상청 예보, 데일리한국·게임톡 11/11)

🔗 4번 더클래스 안티포그 김서림 방지제 링크는 프로필에
👥 오늘 아침 운전한 친구 태그

#광고 #투표 #공감 #안개 #출근길 #김서림""",
    "products": [prod(1, FOG, N_FOG, "B")],
})

write(DATE, "B2", [poll("수능 D-8,<br>수험생 선물 딱 하나만? 🎁", "2027 수능 11월 19일(목) · 지원자 55만1864명",
                        [("찹쌀떡·엿", "딱 붙어라"), ("두루마리 휴지", "술술 잘 풀어라"),
                         ("포크", "잘 찍어라"), ("아날로그 수능시계", "실용성 최고")], WATCH)], {
    "title": "수험생 선물 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 수능 D-8, 수험생 선물 딱 하나만? 🎁
댓글에 번호로 투표해주세요!

1️⃣ 찹쌀떡·엿
2️⃣ 두루마리 휴지
3️⃣ 포크
4️⃣ 아날로그 수능시계

※ 2027학년도 수능 11월 19일(목), 지원자 55만1864명 (머니투데이 9/8, 평가원 집계)
※ 시험장엔 전자 기능 없는 아날로그 시계만 (KB Think 10/14, 최종 기준은 시험장 공지)

🔗 4번 슈페르바 저소음 수능시계 링크는 프로필에
👥 수능 보는 친구·동생 태그하고 응원 한마디

#광고 #투표 #공감 #수능 #수험생선물 #수능응원""",
    "products": [prod(1, WATCH, N_WATCH, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/11 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("오늘 아침 짙은 안개 · 일교차 15도", "흐린 유리", "특이템", "BEST3", [FOG, MIRROR, DRY]),
    c_prod(1, "0118", FOG, "더클래스<br>안티포그", ["뿌리고 닦는 스프레이", "김서림 방지 + 유리 세정", "120ml 2개"],
           ["💰 1만6천원대", "🚀 로켓배송"]),
    c_prod(2, "0119", MIRROR, "사이드미러<br>방수필름", ["사이드미러 + 창문 필름", "빗물·김서림 방지", "붙이는 헤라 포함"],
           ["💰 7천원대", "🚀 로켓배송"]),
    c_prod(3, "0120", DRY, "차량용<br>고흡습 제습백", ["차 안 습기 잡는 200g", "파랑→분홍 변색", "말려서 다시 쓰기"],
           ["💰 1만9천원대", "🚚 무료배송"]),
    c_howto("0118~0120"),
], {
    "title": "흐린 유리 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

오늘 아침 짙은 안개, 일교차 15도 🌫️ 흐린 유리 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 더클래스 안티포그 김서림 방지제 120ml 2개 💛 품번 0118
뿌리고 닦는 스프레이 타입. 김서림 방지와 유리 세정을 한 번에.

2. 누띤 김서림 방지 사이드미러·창문 방수필름 세트 💛 품번 0119
사이드미러·창문에 붙이는 필름, 붙일 때 쓰는 헤라 포함.

3. 변색 확인 차량용 고흡습 제습백 💛 품번 0120
차 안에 두는 200g 제습백. 파랑에서 분홍으로 바뀌면 말려서 다시 써요.

✔ 안개 낀 날은 전조등·안개등 켜고 차간 거리 넉넉히

※ 날씨: 기상청 예보(데일리한국·게임톡 11/11)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #김서림방지 #사이드미러 #차량용품 #안개""",
    "products": [prod(1, FOG, N_FOG, "C", "0118"), prod(2, MIRROR, N_MIRROR, "C", "0119"), prod(3, DRY, N_DRY, "C", "0120")],
})

write(DATE, "C2", [
    c_cover("수능 D-8 · 11월 19일(목)", "수험생", "응원템", "BEST3", [WATCH, YEOT, BLANKET]),
    c_prod(1, "0121", WATCH, "저소음<br>아날로그 수능시계", ["째깍 소리 적은 저소음", "한눈에 큰 숫자", "전자 화면 없는 아날로그"],
           ["💰 6천원대", "🚀 로켓배송"]),
    c_prod(2, "0122", YEOT, "행운합격엿<br>+ 페레로로쉐", ["엿 10입 + 페레로 12입", "딱 붙으라는 응원", "선물 상자 포장"],
           ["💰 2만5천원대", "🚀 로켓배송"]),
    c_prod(3, "0123", BLANKET, "양털 안감<br>망토 담요", ["어깨까지 덮는 망토형", "양털 안감 체크 담요", "무릎담요로도"],
           ["💰 1만3천원대", "🚚 무료배송"]),
    c_howto("0121~0123"),
], {
    "title": "수험생 응원템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

수능 D-8 ✏️ 수험생 응원템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 슈페르바 저소음 큰숫자 아날로그 수능시계 💛 품번 0121
째깍 소리 적은 저소음, 큰 숫자 아날로그 손목시계.

2. 옛다합격 행운합격엿 + 페레로로쉐 세트 💛 품번 0122
엿 10입 + 페레로로쉐 12입 응원 선물 세트.

3. 양털 안감 체크 망토 담요 💛 품번 0123
어깨까지 덮는 망토형, 공부할 때 무릎담요로도.

✔ 수능 시험장엔 전자 기능·화면 없는 아날로그 시계만 가능 — 최종 기준은 시험장 공지 확인

※ 수능 11월 19일(목) (뉴시스 3/31), 시계 규정 KB Think(10/14)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #수능 #수험생선물 #수능시계 #합격엿""",
    "products": [prod(1, WATCH, N_WATCH, "C", "0121"), prod(2, YEOT, N_YEOT, "C", "0122"), prod(3, BLANKET, N_BLANKET, "C", "0123")],
})
print("ok")
