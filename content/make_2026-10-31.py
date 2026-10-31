"""2026-10-31(토, 소형가전의 날) 게시물 6개 → docs/posts/2026-10-31/{A,B,C,A2,B2,C2}
점심: 주말 비 그치면 다시 쌀쌀·출근 준비 가전 / 퇴근길: 내일(일) 전국 비·집콕 간식 가전
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-10-31"
DL = "2026.10.31 (토)"
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



POT, IRON, MAT = "9697944572", "6528214120", "6746447827"
FRY, WAF, HOT = "7405872679", "7615116735", "305643272"
N_POT, N_IRON, N_MAT = "키친아트 내열강화유리 무선 전기포트 1.8L", "필립스 핸디형 스팀다리미 1000 시리즈", "일월 숲속애 온수매트"
N_FRY, N_WAF, N_HOT = "홈플래닛 에어프라이어 2L", "대우어플라이언스 3in1 와플메이커 DEW-D220", "보아르 혼요 멀티 전골 전기냄비 VO-KI006"

# ═════════ A · 점심 12:00 — 비 그치면 다시 쌀쌀, 출근길 준비 ═════════
SRC1 = "출처: 아주경제(10/31)·뉴스1·허프포스트코리아(10/30), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 다음 주</div>
<h1>주말 비 그치면<br><span class="hl">다시 쌀쌀</span><br>출근길 준비</h1>
<p class="lead">서울 첫 서리 관측<br>2일(월) 아침 최저 1~10도</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(31일) 아침 · 낮 기온</h2>
<div class="fig"><div><small>서울</small><strong>9 / 14도</strong></div><div><small>대전</small><strong>9 / 17도</strong></div></div>
<div class="fig"><div><small>대구</small><strong>8 / 19도</strong></div><div><small>부산</small><strong>12 / 21도</strong></div></div>
<div class="box">전국 아침 3~12도, 낮 14~21도<br>경상권 일교차 <b class="hl">10도 안팎</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>일요일 비 → 월요일</h2>
<div class="fig"><div><small>1일(일) 수도권·강원</small><strong>5mm 미만</strong></div></div>
<div class="fig"><div><small>1일(일) 광주·전남·제주</small><strong>5~30mm</strong></div></div>
<div class="box">비 그친 2일(월)<br>아침 <b class="hl">1~10도</b> · 낮 11~18도</div>""", SRC1, DL),
    a_slide(4, n, """<h2>출근길 체크</h2>
<ul class="chk"><li>월요일 아침 <span class="hl">외투</span> 챙기기</li><li>다음 주 기온 평년과 비슷하거나 낮음</li><li>일요일 밤 외투 구김 미리 펴기</li><li>아침엔 따뜻한 물 한 잔</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>쌀쌀한 아침 <span class="hl">출근 준비 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(POT)}"><div>키친아트 무선 전기포트<span>1.8L · 내열강화유리</span></div></li>
<li><b>2</b><img src="{img(IRON)}"><div>필립스 핸디형 스팀다리미<span>1000 시리즈 · 외투 구김 펴기</span></div></li>
<li><b>3</b><img src="{img(MAT)}"><div>일월 숲속애 온수매트<span>쌀쌀한 밤 침대·바닥용</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/31 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "비 그치면 다시 쌀쌀·출근길 준비",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 주말 비 그치면 다시 쌀쌀 — 월요일 출근길 외투 챙기세요 🧥

· 오늘(31일) 전국 아침 3~12도, 낮 14~21도 (서울 9/14, 대전 9/17, 대구 8/19, 부산 12/21)
· 경상권은 일교차 10도 안팎
· 서울에서 첫 서리 관측
· 내일(11/1) 충청·전북부터 비, 밤에는 전국으로 — 예상 강수량 수도권·강원 5mm 미만, 충청·전북·영남 5~10mm, 광주·전남·제주 5~30mm
· 비 그친 2일(월) 아침 1~10도, 낮 11~18도 — 다음 주 기온 평년과 비슷하거나 다소 낮음

✔ 월요일 아침 외투 챙기기, 외투 구김은 일요일 밤에 미리, 아침엔 따뜻한 물 한 잔

🔗 출근 준비 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활가전은 @0315_pick

출처: 아주경제(10/31), 뉴스1(10/30), 허프포스트코리아(10/30) — 기상청 예보

#광고 #생활뉴스 #주말날씨 #출근길 #첫서리 #전기포트 #스팀다리미 #온수매트""",
    "products": [prod(1, POT, N_POT, "A"), prod(2, IRON, N_IRON, "A"), prod(3, MAT, N_MAT, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 일요일 전국 비, 집콕 간식 ═════════
SRC2 = "출처: SBS·뉴스1·허프포스트코리아(10/30), 기상청 예보"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 일요일</div>
<h1>내일 전국 비<br><span class="hl">집콕 간식</span><br>만들어 볼까</h1>
<p class="lead">일요일 오후~월요일 오전 비<br>주말 서울 낮 13~14도</p>""", SRC2, DL),
    a_slide(2, n, """<h2>1일(일) 예상 강수량</h2>
<div class="fig"><div><small>수도권·강원</small><strong>5mm 미만</strong></div><div><small>충청·전북</small><strong>5~10mm</strong></div></div>
<div class="fig"><div><small>부산·대구·경상</small><strong>5~10mm</strong></div><div><small>광주·전남·제주</small><strong>5~30mm</strong></div></div>
<div class="box">충청·전북부터 시작해<br>밤에는 <b class="hl">전국으로 확대</b></div>""", SRC2, DL),
    a_slide(3, n, """<h2>일요일 체크</h2>
<ul class="chk"><li>나들이·빨래는 <span class="hl">토요일</span>에</li><li>비는 월요일 오전까지</li><li>비 그친 뒤 아침 기온 다시 뚝</li><li>집에서 따뜻한 간식 타임</li></ul>""", SRC2, DL),
    a_slide(4, n, f"""<h2>비 오는 일요일 <span class="hl">집콕 간식 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FRY)}"><div>홈플래닛 에어프라이어 2L<span>1~2인용 · 냉동 간식 데우기</span></div></li>
<li><b>2</b><img src="{img(WAF)}"><div>대우 3in1 와플메이커<span>와플·샌드위치·붕어빵틀</span></div></li>
<li><b>3</b><img src="{img(HOT)}"><div>보아르 혼요 멀티 전골냄비<span>테이블에서 전골·라면</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/31 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "내일 전국 비·집콕 간식",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 내일(일) 전국 비 — 집에서 따뜻한 간식 만들어 볼까요 🧇

· 1일(일) 충청·전북부터 비 시작, 밤에는 전국으로 확대
· 일요일 오후~월요일 오전 전국에 비
· 예상 강수량: 수도권·강원 5mm 미만, 충청·전북 5~10mm, 부산·대구·경상 5~10mm, 광주·전남·제주 5~30mm
· 주말 서울 낮 기온 13~14도
· 비 그친 뒤 다음 주 아침 기온 다시 낮아짐

✔ 나들이·빨래는 오늘(토) 끝내기, 월요일 오전까지 우산 챙기기

🔗 집콕 간식 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활가전은 @0315_pick

출처: SBS(10/30), 뉴스1(10/30), 허프포스트코리아(10/30) — 기상청 예보

#광고 #생활뉴스 #일요일날씨 #집콕 #집콕간식 #에어프라이어 #와플메이커 #전기냄비""",
    "products": [prod(1, FRY, N_FRY, "A"), prod(2, WAF, N_WAF, "A"), prod(3, HOT, N_HOT, "A")],
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




write(DATE, "B", [poll("아침 3도 주말,<br>눈 뜨면 제일 먼저? ☕", "31일 아침 최저 3~12도 (기상청 예보)",
                       [("이불 속 5분 더", "알람 끄고 다시 눕기"), ("휴대폰부터 확인", "누워서 스크롤"),
                        ("보일러 버튼", "일단 따뜻하게"), ("따뜻한 물 한 잔", "전기포트 딸깍")], POT)], {
    "title": "주말 아침 첫 행동 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 아침 3도 주말, 눈 뜨면 제일 먼저 하는 건? ☕
댓글에 번호로 투표해주세요!

1️⃣ 이불 속 5분 더
2️⃣ 휴대폰부터 확인
3️⃣ 보일러 버튼
4️⃣ 따뜻한 물 한 잔

🔗 4번 무선 전기포트 링크는 프로필에
👥 주말 아침 이불 밖 못 나오는 친구 태그

#광고 #투표 #공감 #주말아침 #전기포트 #쌀쌀한날씨 #주말""",
    "products": [prod(1, POT, N_POT, "B")],
})

write(DATE, "B2", [poll("비 오는 일요일,<br>집콕 간식은? 🧇", "일요일 오후~월요일 오전 전국 비 (SBS 10/30)",
                        [("배달 앱 켠다", "고민은 배송만 늦출 뿐"), ("라면 끓인다", "비 오면 국룰"),
                         ("부침개 부친다", "빗소리 = 전 부치는 소리"), ("와플 직접 굽기", "와플메이커 출동")], WAF)], {
    "title": "비 오는 일요일 집콕 간식 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 비 오는 일요일, 집콕 간식은? 🧇
댓글에 번호로 투표해주세요!

1️⃣ 배달 앱 켠다
2️⃣ 라면 끓인다
3️⃣ 부침개 부친다
4️⃣ 와플 직접 굽기

🔗 4번 와플메이커 링크는 프로필에
👥 비 오면 전 부치자는 친구 태그

#광고 #투표 #공감 #집콕 #비오는날 #와플 #일요일""",
    "products": [prod(1, WAF, N_WAF, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/31 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("주말 비 그치면 다시 쌀쌀", "쌀쌀한 아침", "출근 준비 가전", "BEST3", [POT, IRON, MAT]),
    c_prod(1, "0052", POT, "키친아트<br>무선 전기포트 1.8L", ["내열강화유리 무선 전기포트", "1.8L 대용량", "아침 따뜻한 물 한 잔"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0053", IRON, "필립스<br>핸디형 스팀다리미", ["1000 시리즈 핸디형", "걸어둔 채 스팀으로", "외투·셔츠 구김 펴기"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0054", MAT, "일월<br>숲속애 온수매트", ["온수 순환식 매트", "침대·바닥에 깔기", "쌀쌀한 밤 이불 속"],
           ["💰 10만원대", "🚀 로켓배송"]),
    c_howto("0052~0054"),
], {
    "title": "출근 준비 가전 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

주말 비 그치면 다시 쌀쌀 🧥 쌀쌀한 아침 출근 준비 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 키친아트 내열강화유리 무선 전기포트 1.8L 💛 품번 0052
아침 따뜻한 물 한 잔, 1.8L 무선 전기포트.

2. 필립스 핸디형 스팀다리미 1000 시리즈 💛 품번 0053
걸어둔 외투·셔츠 구김을 스팀으로.

3. 일월 숲속애 온수매트 💛 품번 0054
쌀쌀한 밤 침대·바닥에 까는 온수매트.

※ 날씨: 기상청 예보(아주경제 10/31·뉴스1 10/30 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #전기포트 #스팀다리미 #온수매트 #출근준비 #겨울준비""",
    "products": [prod(1, POT, N_POT, "C", "0052"), prod(2, IRON, N_IRON, "C", "0053"), prod(3, MAT, N_MAT, "C", "0054")],
})

write(DATE, "C2", [
    c_cover("내일 전국 비 소식", "비 오는 일요일", "집콕 간식 가전", "BEST3", [FRY, WAF, HOT]),
    c_prod(1, "0055", FRY, "홈플래닛<br>에어프라이어 2L", ["1~2인용 2L 용량", "냉동 간식 데우기", "자리 덜 차지하는 크기"],
           ["💰 3만원대", "🚀 로켓배송"]),
    c_prod(2, "0056", WAF, "대우어플라이언스<br>3in1 와플메이커", ["와플·샌드위치·붕어빵틀", "플레이트 분리형", "집에서 굽는 간식"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0057", HOT, "보아르 혼요<br>멀티 전골 전기냄비", ["테이블에 두는 전기냄비", "전골·라면·찌개", "비 오는 날 국물 요리"],
           ["💰 4만원대", "🚀 로켓배송"]),
    c_howto("0055~0057"),
], {
    "title": "집콕 간식 가전 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

내일 전국 비 소식 ☔ 비 오는 일요일 집콕 간식 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 홈플래닛 에어프라이어 2L 💛 품번 0055
1~2인용, 냉동 간식 데우기 좋은 크기.

2. 대우어플라이언스 3in1 와플메이커 DEW-D220 💛 품번 0056
와플·샌드위치·붕어빵틀 분리형 플레이트.

3. 보아르 혼요 멀티 전골 전기냄비 VO-KI006 💛 품번 0057
테이블에 두고 끓이는 전골·라면용 전기냄비.

※ 날씨: 기상청 예보(SBS·뉴스1 10/30 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #집콕 #에어프라이어 #와플메이커 #전기냄비 #비오는날""",
    "products": [prod(1, FRY, N_FRY, "C", "0055"), prod(2, WAF, N_WAF, "C", "0056"), prod(3, HOT, N_HOT, "C", "0057")],
})
print("ok")
