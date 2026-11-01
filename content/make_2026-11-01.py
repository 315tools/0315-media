"""2026-11-01(일, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-01/{A,B,C,A2,B2,C2}
점심: 11월 첫날 전국 비·낮 10~18도 / 퇴근길: 비 그친 뒤 3일 서울 아침 3도, 사무실 보온템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-01"
DL = "2026.11.01 (일)"
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




SHOE, TAPE, UMB = "9452930886", "7707999407", "9558071037"
CUP, PAD, CAPE = "9786132902", "9221650737", "9209366324"
N_SHOE, N_TAPE, N_UMB = "슈렌다 미끄럼방지 실리콘 신발방수커버", "스코라 물흡수 테이프 10cm x 5m", "HANNAL 접이식 미니 우산 물기흡수 파우치"
N_CUP, N_PAD, N_CAPE = "로이젠 휴대용 USB 컵워머 (55도 유지)", "아이리버 그래핀 온열 마우스패드 IMP-260U", "르세라 똑딱이 망토 극세사 입는 담요"

# ═════════ A · 점심 12:00 — 11월 첫날 전국 비 ═════════
SRC1 = "출처: 천지일보·뉴스1(10/31), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 오늘</div>
<h1>11월 첫날<br><span class="hl">전국 곳곳 비</span><br>낮에도 쌀쌀</h1>
<p class="lead">아침 3~10도 · 낮 10~18도<br>제주 최대 60mm</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(1일) 아침 · 낮 기온</h2>
<div class="fig"><div><small>서울</small><strong>5 / 13도</strong></div><div><small>춘천</small><strong>3 / 11도</strong></div></div>
<div class="fig"><div><small>대전</small><strong>6 / 12도</strong></div><div><small>부산</small><strong>9 / 18도</strong></div></div>
<div class="box">낮 기온 <b class="hl">평년보다 조금 낮음</b><br>아침은 평년과 비슷</div>""", SRC1, DL),
    a_slide(3, n, """<h2>1~2일 예상 강수량</h2>
<div class="fig"><div><small>서울·인천·경기북부</small><strong>1mm 안팎</strong></div><div><small>충청</small><strong>5~10mm</strong></div></div>
<div class="fig"><div><small>광주·전남·경남</small><strong>5~40mm</strong></div><div><small>제주</small><strong>10~60mm</strong></div></div>
<div class="box">오전 경기 남서부·충청부터<br>밤에는 <b class="hl">전국 대부분</b>으로</div>""", SRC1, DL),
    a_slide(4, n, """<h2>비 오는 일요일 체크</h2>
<ul class="chk"><li>제주 밤 <span class="hl">시간당 20mm</span> 강한 비</li><li>신발 젖지 않게 대비</li><li>창가 결로·물기 닦아두기</li><li>젖은 우산은 파우치에</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>비 오는 날 <span class="hl">특이한 생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SHOE)}"><div>슈렌다 실리콘 신발방수커버<span>신발 위에 신는 미끄럼방지 덧신</span></div></li>
<li><b>2</b><img src="{img(TAPE)}"><div>스코라 물흡수 테이프<span>10cm x 5m · 창틀 물기 흡수</span></div></li>
<li><b>3</b><img src="{img(UMB)}"><div>HANNAL 우산 물기흡수 파우치<span>접이식 미니 우산 수납</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/1 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "11월 첫날 전국 비",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 11월 첫날 전국 곳곳 비 — 낮에도 쌀쌀해요 ☔

· 오늘(1일) 전국 아침 3~10도, 낮 10~18도 (서울 5/13, 춘천 3/11, 대전 6/12, 부산 9/18, 제주 14/22)
· 낮 기온은 평년보다 조금 낮음
· 오전 경기 남서부·충청부터 비, 밤에는 전국 대부분으로 확대
· 1~2일 예상 강수량: 서울·인천·경기북부 1mm 안팎, 경기남부·강원 5mm 안팎, 충청 5~10mm, 전북·대구·경북 5~20mm, 광주·전남·부산·울산·경남 5~40mm, 제주 10~60mm
· 제주는 밤늦게 시간당 20mm 안팎 강한 비 가능

✔ 신발 젖지 않게, 창가 물기 닦아두기, 젖은 우산은 파우치에

🔗 비 오는 날 특이한 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 천지일보(10/31), 뉴스1(10/31) — 기상청 예보

#광고 #생활뉴스 #일요일날씨 #11월날씨 #비오는날 #신발방수커버 #결로테이프 #우산파우치""",
    "products": [prod(1, SHOE, N_SHOE, "A"), prod(2, TAPE, N_TAPE, "A"), prod(3, UMB, N_UMB, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 비 그친 뒤 기온 뚝 ═════════
SRC2 = "출처: 데일리안(10/31)·YTN(10/28), 기상청 예보"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 이번 주</div>
<h1>비 그치면<br><span class="hl">기온 뚝</span><br>3일 서울 3도</h1>
<p class="lead">찬 공기 남하<br>평년(아침 6도)보다 낮아요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>비 그치는 시간 · 기온</h2>
<div class="fig"><div><small>2일(월) 새벽</small><strong>중부·전라 그침</strong></div></div>
<div class="fig"><div><small>3일(화) 서울 아침</small><strong>3도</strong></div><div><small>서울 평년 아침</small><strong>6도</strong></div></div>
<div class="box">경상권·제주는<br>2일 <b class="hl">아침</b>에 비 그침</div>""", SRC2, DL),
    a_slide(3, n, """<h2>출근길 · 사무실 체크</h2>
<ul class="chk"><li>바람 불면 <span class="hl">체감온도</span>는 더 낮게</li><li>화요일 아침 외투 한 겹 더</li><li>사무실 손·어깨 보온</li><li>따뜻한 음료 식지 않게</li></ul>""", SRC2, DL),
    a_slide(4, n, f"""<h2>추운 사무실 <span class="hl">특이한 보온템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(CUP)}"><div>로이젠 USB 컵워머<span>머그 올려두면 55도 유지</span></div></li>
<li><b>2</b><img src="{img(PAD)}"><div>아이리버 온열 마우스패드<span>그래핀 히팅 · 4단 온열조절</span></div></li>
<li><b>3</b><img src="{img(CAPE)}"><div>르세라 똑딱이 망토 담요<span>어깨에 입는 극세사 담요</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/1 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "비 그친 뒤 3일 서울 아침 3도",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 비 그치면 기온 뚝 — 3일(화) 서울 아침 3도 🧣

· 2일(월) 중부·전라권은 새벽, 경상권·제주는 아침에 비 그침
· 찬 공기가 내려오면서 3일(화) 서울 아침 기온 3도까지 떨어질 전망
· 이 시기 서울 평년 기온은 아침 6도, 낮 16도 안팎
· 바람이 불면 체감온도는 더 낮아짐 (영하권에선 풍속 초속 1m마다 약 1도씩)

✔ 화요일 아침 외투 한 겹 더, 사무실에선 손·어깨 보온, 따뜻한 음료 식지 않게

🔗 추운 사무실 특이한 보온템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 데일리안(10/31), YTN(10/28) — 기상청 예보

#광고 #생활뉴스 #이번주날씨 #기온뚝 #출근길 #컵워머 #온열마우스패드 #망토담요""",
    "products": [prod(1, CUP, N_CUP, "A"), prod(2, PAD, N_PAD, "A"), prod(3, CAPE, N_CAPE, "A")],
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





write(DATE, "B", [poll("비 오는 날<br>새 운동화 신었다면? 👟", "11월 첫날 전국 곳곳 비 (기상청 예보)",
                       [("그냥 젖는다", "운동화는 빨면 된다"), ("물웅덩이 점프", "징검다리 모드"),
                        ("비닐봉지 덧신기", "패션은 포기"), ("실리콘 방수 덧신", "신발 위에 쓱")], SHOE)], {
    "title": "비 오는 날 새 운동화 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 비 오는 날 새 운동화 신고 나왔다면? 👟
댓글에 번호로 투표해주세요!

1️⃣ 그냥 젖는다
2️⃣ 물웅덩이 점프
3️⃣ 비닐봉지 덧신기
4️⃣ 실리콘 방수 덧신

🔗 4번 신발방수커버 링크는 프로필에
👥 비 오는 날 꼭 흰 운동화 신는 친구 태그

#광고 #투표 #공감 #비오는날 #운동화 #신발방수커버 #일요일""",
    "products": [prod(1, SHOE, N_SHOE, "B")],
})

write(DATE, "B2", [poll("화요일 아침 3도,<br>사무실 추울 때 나는? 🥶", "3일 서울 아침 3도 전망 (데일리안 10/31)",
                        [("히터 앞자리 사수", "자리 바꿔달라 조르기"), ("카디건 상주", "의자에 항상 걸려 있음"),
                         ("핫팩 양손", "주머니 속 난로"), ("망토 담요 입기", "똑딱이 채우고 업무")], CAPE)], {
    "title": "추운 사무실 대처 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 화요일 아침 3도, 사무실 추울 때 나는? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 히터 앞자리 사수
2️⃣ 카디건 상주
3️⃣ 핫팩 양손
4️⃣ 망토 담요 입기

🔗 4번 똑딱이 망토 담요 링크는 프로필에
👥 사무실에서 제일 추위 타는 동료 태그

#광고 #투표 #공감 #사무실 #직장인 #망토담요 #추위""",
    "products": [prod(1, CAPE, N_CAPE, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/1 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("11월 첫날 전국 비", "비 오는 날", "특이한 생활템", "BEST3", [SHOE, TAPE, UMB]),
    c_prod(1, "0058", SHOE, "슈렌다<br>실리콘 신발방수커버", ["신발 위에 신는 실리콘 덧신", "미끄럼방지 바닥", "210~290 사이즈"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0059", TAPE, "스코라<br>물흡수 테이프", ["창틀에 붙이는 물흡수 테이프", "10cm x 5m", "결로 물기 흡수"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0060", UMB, "HANNAL<br>우산 물기흡수 파우치", ["접이식 미니 우산 수납", "물기 흡수 파우치", "가방에 넣기 전 쏙"],
           ["💰 1만원 미만", "🚀 로켓배송"]),
    c_howto("0058~0060"),
], {
    "title": "비 오는 날 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

11월 첫날 전국 비 ☔ 비 오는 날 특이한 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 슈렌다 미끄럼방지 실리콘 신발방수커버 💛 품번 0058
신발 위에 신는 실리콘 덧신, 210~290 사이즈.

2. 스코라 물흡수 테이프 10cm x 5m 💛 품번 0059
창틀에 붙여 결로 물기를 흡수하는 테이프.

3. HANNAL 접이식 미니 우산 물기흡수 파우치 💛 품번 0060
젖은 접이식 우산을 가방에 넣기 전에 쏙.

※ 날씨: 기상청 예보(천지일보·뉴스1 10/31 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #비오는날 #신발방수커버 #결로테이프 #우산파우치 #생활꿀템""",
    "products": [prod(1, SHOE, N_SHOE, "C", "0058"), prod(2, TAPE, N_TAPE, "C", "0059"), prod(3, UMB, N_UMB, "C", "0060")],
})

write(DATE, "C2", [
    c_cover("비 그치면 기온 뚝", "추운 사무실", "특이한 보온템", "BEST3", [CUP, PAD, CAPE]),
    c_prod(1, "0061", CUP, "로이젠<br>USB 컵워머", ["머그 올려두면 55도 유지", "올리면 켜지는 자동 전원", "KC인증"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(2, "0062", PAD, "아이리버<br>온열 마우스패드", ["그래핀 히팅 온열 패드", "4단 온열조절", "IMP-260U"],
           ["💰 3만원대", "🚀 로켓배송"]),
    c_prod(3, "0063", CAPE, "르세라<br>똑딱이 망토 담요", ["어깨에 입는 극세사 담요", "똑딱이 버튼 고정", "무릎담요 겸용 대형"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0061~0063"),
], {
    "title": "사무실 보온 특이템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

비 그치면 기온 뚝 🧣 추운 사무실 특이한 보온템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 로이젠 휴대용 USB 컵워머 💛 품번 0061
머그를 올려두면 55도로 유지, KC인증.

2. 아이리버 그래핀 온열 마우스패드 IMP-260U 💛 품번 0062
책상 위 손 시릴 때, 4단 온열조절 마우스패드.

3. 르세라 똑딱이 망토 극세사 입는 담요 💛 품번 0063
어깨에 두르고 똑딱이로 고정하는 대형 담요.

※ 날씨: 기상청 예보(데일리안 10/31 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #사무실템 #컵워머 #온열마우스패드 #망토담요 #직장인템""",
    "products": [prod(1, CUP, N_CUP, "C", "0061"), prod(2, PAD, N_PAD, "C", "0062"), prod(3, CAPE, N_CAPE, "C", "0063")],
})
print("ok")
