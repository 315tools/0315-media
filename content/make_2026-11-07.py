"""2026-11-07(토, 소형가전의 날) 게시물 6개 → docs/posts/2026-11-06/{A,B,C,A2,B2,C2}
점심: 입동 한파·대기 건조·가습기 / 퇴근길: 낮밤 기온차 10~15도·밤 난방 가전
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-07"
DL = "2026.11.07 (토)"
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






HEA, BND, ARB = "9136176625", "8457552215", "8389642536"
YO, CAR, RAD = "9150828084", "335473675", "1195421"
N_HEA = "신일 가열식 가습기"
N_BND = "블랙앤데커 무드등 대용량 듀얼 초음파 가습기 5L"
N_ARB = "에어보나 자동습도조절 복합식 가습기 5L"
N_YO = "한일의료기 탄소열선 고급 전기요 HL-D205"
N_CAR = "신일 원적외선 카본히터 4단 SEH-PC260PW"
N_RAD = "니코 미니 오일 라디에이터 WH-M07"

# ═════════ A · 점심 12:00 — 입동 한파 + 대기 건조 ═════════
SRC1 = "출처: 뉴스1·파이낸셜뉴스·게임톡(11/7), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 입동</div>
<h1>입동 한파에<br><span class="hl">공기도 바싹</span></h1>
<p class="lead">서울 아침 -1도, 올가을 첫 영하권<br>강원 동해안엔 건조특보</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(7일) 기온</h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>-6~5도</strong></div><div><small>전국 낮 최고</small><strong>8~14도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>-1도</strong></div><div><small>서울 낮</small><strong>9도</strong></div></div>
<div class="box">평년(최저 2~11도·최고 15~20도)보다<br><b class="hl">낮은 기온</b>이에요</div>""", SRC1, DL),
    a_slide(3, n, """<h2>대기는 <span class="hl">건조</span>해요</h2>
<ul class="chk"><li>강원 북부 동해안 <span class="hl">건조특보</span></li><li>그 지역 중심으로 매우 건조</li><li>수도권·강원 영동도 건조</li><li>미세먼지는 전국 <span class="hl">'좋음'</span></li></ul>
<div class="box">강원·경북 동쪽, 전남 곳곳<br><b class="hl">한파주의보</b>(6일 밤 9시 발효)</div>""", SRC1, DL),
    a_slide(4, n, """<h2>건조한 날 <span class="hl">체크리스트</span></h2>
<ul class="chk"><li>물 자주 마시기</li><li>실내 <span class="hl">습도</span> 챙기기</li><li>환기는 짧고 자주</li><li>불씨·난방기구 주변 정리</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>건조한 겨울 <span class="hl">가습기</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(HEA)}"><div>신일 가열식 가습기<span>물을 끓여 내보내는 가열식</span></div></li>
<li><b>2</b><img src="{img(BND)}"><div>블랙앤데커 초음파 가습기<span>5L 대용량 · 무드등</span></div></li>
<li><b>3</b><img src="{img(ARB)}"><div>에어보나 복합식 가습기<span>5L · 자동 습도조절</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/7 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "입동 한파·대기 건조",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 입동(7일) 서울 아침 -1도, 올가을 첫 영하권… 공기도 건조 🥶

· 오늘 아침 최저 -6~5도, 낮 최고 8~14도 — 평년(최저 2~11도, 최고 15~20도)보다 낮아요
· 서울 아침 -1도, 낮 9도
· 강원·경북 동쪽과 전남 곳곳 한파주의보 (6일 밤 9시 발효)
· 건조특보가 내려진 강원 북부 동해안 중심으로 매우 건조, 수도권·강원 영동도 건조
· 미세먼지는 전국 '좋음'

✔ 물 자주 마시고, 실내 습도 챙기고, 난방기구 주변 정리하기

🔗 건조한 겨울 가습기 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 뉴스1·파이낸셜뉴스·게임톡(11/7) — 기상청 예보

#광고 #생활뉴스 #날씨 #입동 #건조특보 #가습기 #겨울가전""",
    "products": [prod(1, HEA, N_HEA, "A"), prod(2, BND, N_BND, "A"), prod(3, ARB, N_ARB, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 낮밤 기온차 10~15도 ═════════
SRC2 = "출처: 파이낸셜뉴스(뉴스1)·게임톡(11/7), 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 주말</div>
<h1>낮밤 기온차<br><span class="hl">10~15도</span></h1>
<p class="lead">아침 기온 하루 새 5~10도 뚝<br>밤 난방 미리 챙기세요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>주말·월요일 <span class="hl">기온</span></h2>
<div class="fig"><div><small>8일(일) 아침</small><strong>-1~6도</strong></div><div><small>8일 낮</small><strong>8~16도</strong></div></div>
<div class="fig"><div><small>9일(월) 아침</small><strong>-1~11도</strong></div><div><small>9일 낮</small><strong>9~16도</strong></div></div>
<div class="box">아침은 영하권, 낮은 10도 안팎<br><b class="hl">겉옷 조절</b>이 필요해요</div>""", SRC2, DL),
    a_slide(3, n, """<h2>일요일엔 <span class="hl">비 소식</span></h2>
<ul class="chk"><li>오전 경기 북부·강원 중북부부터</li><li>늦은 오후 수도권·강원 전역</li><li>저녁엔 충청권 북부까지</li><li>강원 내륙·산지는 <span class="hl">비 또는 눈</span></li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>추운 밤 <span class="hl">난방 안전</span></h2>
<ul class="chk"><li>잠들기 전 <span class="hl">타이머</span> 맞추기</li><li>히터 주변 옷·이불 치우기</li><li>외출할 땐 전원 끄고 플러그 뽑기</li><li>한 콘센트에 여러 대 꽂지 않기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>추운 밤 <span class="hl">난방 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(YO)}"><div>한일의료기 탄소열선 전기요<span>HL-D205 · 잠자리 난방</span></div></li>
<li><b>2</b><img src="{img(CAR)}"><div>신일 원적외선 카본히터<span>4단 · SEH-PC260PW</span></div></li>
<li><b>3</b><img src="{img(RAD)}"><div>니코 미니 오일 라디에이터<span>WH-M07 · 미니 사이즈</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/7 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "낮밤 기온차 10~15도",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 낮밤 기온차 10~15도… 아침은 하루 새 5~10도 뚝 🌡️

· 7일 아침 기온은 전날보다 5~10도 낮아졌고, 낮과 밤 기온차는 10~15도
· 8일(일) 아침 -1~6도, 낮 8~16도 / 9일(월) 아침 -1~11도, 낮 9~16도
· 8일 오전 경기 북부·강원 중북부부터 비 → 늦은 오후 수도권·강원, 저녁 충청권 북부로
· 강원 내륙·산지는 비 또는 눈

✔ 난방기구는 타이머 맞추고, 주변 물건 치우고, 외출 땐 플러그 뽑기

🔗 추운 밤 난방 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 파이낸셜뉴스(뉴스1 제공)·게임톡(11/7) — 기상청 예보

#광고 #생활뉴스 #날씨 #일교차 #난방 #전기요 #히터 #겨울가전""",
    "products": [prod(1, YO, N_YO, "A"), prod(2, CAR, N_CAR, "A"), prod(3, RAD, N_RAD, "A")],
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



write(DATE, "B", [poll("공기 바싹 마른 날,<br>나의 대처법은? 🏜️", "강원 동해안 건조특보, 수도권도 건조 (기상청 예보)",
                       [("물 벌컥벌컥", "속부터 촉촉하게"), ("젖은 수건 널기", "자취생 국룰 가습기"),
                        ("립밤·핸드크림", "바르고 또 바르기"), ("가습기 틀기", "무드등까지 켜면 완벽")], BND)], {
    "title": "건조한 날 대처법 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 공기 바싹 마른 날, 나의 대처법은? 🏜️
댓글에 번호로 투표해주세요!

1️⃣ 물 벌컥벌컥
2️⃣ 젖은 수건 널기
3️⃣ 립밤·핸드크림
4️⃣ 가습기 틀기

※ 7일 강원 북부 동해안 건조특보, 수도권·강원 영동도 건조 (기상청 예보, 게임톡·파이낸셜뉴스 11/7)

🔗 4번 블랙앤데커 초음파 가습기 링크는 프로필에
👥 젖은 수건으로 버티는 친구 태그

#광고 #투표 #공감 #건조 #입동 #가습기""",
    "products": [prod(1, BND, N_BND, "B")],
})

write(DATE, "B2", [poll("이불 밖은 위험해…<br>나의 잠자리 난방은? 🛏️", "낮밤 기온차 10~15도 (기상청 예보)",
                        [("이불 두 겹", "무거워야 잠이 와"), ("수면양말 필수", "발만 따뜻하면 OK"),
                         ("보일러 빵빵", "관리비는 내일의 나에게"), ("전기요 켜기", "등부터 따끈하게")], YO)], {
    "title": "잠자리 난방 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 이불 밖은 위험해… 나의 잠자리 난방은? 🛏️
댓글에 번호로 투표해주세요!

1️⃣ 이불 두 겹
2️⃣ 수면양말 필수
3️⃣ 보일러 빵빵
4️⃣ 전기요 켜기

※ 7일 낮과 밤 기온차 10~15도, 8일(일) 아침 -1~6도 (기상청 예보, 파이낸셜뉴스·게임톡 11/7)

🔗 4번 한일의료기 탄소열선 전기요 링크는 프로필에
👥 겨울만 되면 이불 밖으로 안 나오는 친구 태그

#광고 #투표 #공감 #겨울밤 #전기요 #난방""",
    "products": [prod(1, YO, N_YO, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/7 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("입동 한파 · 건조특보", "건조한 겨울", "가습기", "BEST3", [HEA, BND, ARB]),
    c_prod(1, "0094", HEA, "신일<br>가열식 가습기", ["물을 끓여 내보내는", "가열식 가습기", "건조한 방 습도 챙기기"],
           ["💰 7만원대", "🚀 로켓배송"]),
    c_prod(2, "0095", BND, "블랙앤데커<br>초음파 가습기 5L", ["듀얼 초음파 분무", "5L 대용량 물통", "무드등 기능"],
           ["💰 3만원대", "🚀 로켓배송"]),
    c_prod(3, "0096", ARB, "에어보나<br>복합식 가습기 5L", ["가열+초음파 복합식", "자동 습도조절", "5L 물통"],
           ["💰 5만원대", "🚀 로켓배송"]),
    c_howto("0094~0096"),
], {
    "title": "건조한 겨울 가습기 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

입동 한파에 건조특보 🏜️ 건조한 겨울 가습기 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 신일 가열식 가습기 💛 품번 0094
물을 끓여 수증기로 내보내는 가열식 가습기.

2. 블랙앤데커 무드등 대용량 듀얼 초음파 가습기 5L 💛 품번 0095
5L 물통에 무드등까지 있는 초음파 가습기.

3. 에어보나 자동습도조절 복합식 가습기 5L 💛 품번 0096
가열식과 초음파식을 합친 복합식, 습도 자동 조절.

※ 날씨: 기상청 예보(뉴스1·파이낸셜뉴스·게임톡 11/7 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #가습기 #가열식가습기 #겨울가전 #입동""",
    "products": [prod(1, HEA, N_HEA, "C", "0094"), prod(2, BND, N_BND, "C", "0095"), prod(3, ARB, N_ARB, "C", "0096")],
})

write(DATE, "C2", [
    c_cover("낮밤 기온차 10~15도", "추운 밤", "난방템", "BEST3", [YO, CAR, RAD]),
    c_prod(1, "0097", YO, "한일의료기<br>탄소열선 전기요", ["탄소열선 전기요", "HL-D205", "잠자리 등 따끈하게"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(2, "0098", CAR, "신일<br>원적외선 카본히터", ["원적외선 카본히터", "4단 조절", "SEH-PC260PW"],
           ["💰 14만원대", "🚀 로켓배송"]),
    c_prod(3, "0099", RAD, "니코<br>미니 오일 라디에이터", ["미니 오일 라디에이터", "미니 사이즈", "WH-M07"],
           ["💰 3만원대", "🚀 로켓배송"]),
    c_howto("0097~0099"),
], {
    "title": "추운 밤 난방템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

낮밤 기온차 10~15도 🌡️ 추운 밤 난방템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 한일의료기 탄소열선 고급 전기요 HL-D205 💛 품번 0097
잠자리를 등부터 따뜻하게 데우는 탄소열선 전기요.

2. 신일 원적외선 카본히터 4단 SEH-PC260PW 💛 품번 0098
4단으로 세기를 고르는 원적외선 카본히터.

3. 니코 미니 오일 라디에이터 WH-M07 💛 품번 0099
미니 사이즈 오일 라디에이터.

✔ 난방기구는 주변 물건 치우고, 외출 땐 전원 끄기

※ 날씨: 기상청 예보(파이낸셜뉴스·게임톡 11/7 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #전기요 #카본히터 #라디에이터 #겨울가전""",
    "products": [prod(1, YO, N_YO, "C", "0097"), prod(2, CAR, N_CAR, "C", "0098"), prod(3, RAD, N_RAD, "C", "0099")],
})
print("ok")
