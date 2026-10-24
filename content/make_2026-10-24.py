"""2026-10-24(토, 소형가전의 날) 게시물 6개 → docs/posts/2026-10-24/{A,B,C,A2,B2,C2}
점심: 다음 주 수요일 첫 추위(아침 5~10도 뚝) / 퇴근길: 주말 남부 비·빨래 실내건조
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402

DATE = "2026-10-24"
DL = "2026.10.24 (토)"
cat = json.loads((ROOT / "catalog" / f"{DATE}.json").read_text(encoding="utf-8"))


def link(pid, key):
    """catalog 에서 채널(key)용 파트너스 링크 찾기"""
    url = f"https://www.coupang.com/vp/products/{pid}"
    for u in cat["urls"]:
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


HEATER, CUSHION, FOOT = "8366829430", "7485208545", "8974619660"
CIRC, DEHUM, RACK = "5346040112", "8709628803", "9310480468"

# ═════════ A · 점심 12:00 — 다음 주 첫 추위 ═════════
SRC1 = "출처: 기상청 중기예보(10/24 06시 발표), 위키트리(10/23) 기상청 전망 인용"
n = 6
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 생활</div>
<h1>다음 주 수요일<br>아침 기온<br><span class="hl">5~10도 '뚝'</span></h1>
<p class="lead">북서쪽 찬 공기가 내려옵니다.<br>서울 아침 2도, 일부 내륙은 영하권.</p>""", SRC1, DL),
    a_slide(2, n, """<h2>서울 다음 주 기온</h2>
<div class="fig"><div><small>10/28(수) 아침</small><strong>2℃</strong></div><div><small>10/28(수) 낮</small><strong>13℃</strong></div></div>
<div class="fig"><div><small>11/2(월) 아침</small><strong>1℃</strong></div><div><small>11/2(월) 낮</small><strong>11℃</strong></div></div>
<p class="lead" style="font-size:36px">대전·대구도 28일 아침 1℃ 예상입니다.</p>""", SRC1, DL),
    a_slide(3, n, """<h2>평년보다 <span class="hl">쌀쌀</span></h2>
<div class="box">28일, 31일~11월 3일 전국<br>아침 <b class="hl">-1~10℃</b> · 낮 <b class="hl">11~17℃</b><br><small style="font-size:34px;color:#5b6577">평년: 아침 3~12℃ · 낮 15~20℃</small></div>
<p class="lead">29~30일은 평년과 비슷하다가 다시 내려갑니다. 내륙은 일교차 10도 이상.</p>""", SRC1, DL),
    a_slide(4, n, """<h2>첫 추위 전 체크</h2>
<ul class="chk"><li>두꺼운 겉옷·이불 미리 꺼내기</li><li>난방기구 먼지 털고 작동 확인</li><li>전열기는 멀티탭 말고 벽 콘센트에</li><li>외출 땐 난방기구 전원 끄기</li></ul>""", "", DL),
    a_slide(5, n, """<h2>보일러 켜기 전엔</h2>
<p class="lead">아직 집 전체 난방은 이르다면, 앉아 있는 자리만 데우는 <b class="hl">1인 난방가전</b>이 방법입니다.</p>
<div class="box">책상 밑 · 소파 · 사무실 의자<br>필요한 곳만, 쓸 때만 켜기</div>""", "", DL),
    a_slide(6, n, f"""<h2>첫 추위 대비 <span class="hl">1인 난방템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(HEATER)}"><div>한일 PTC 미니 온풍기<span>책상 위·발밑 온풍</span></div></li>
<li><b>2</b><img src="{img(CUSHION)}"><div>브루노 극세사 온열방석<span>의자·소파에 깔기</span></div></li>
<li><b>3</b><img src="{img(FOOT)}"><div>러비쉬 전기 풋워머<span>발 시린 날 쏙</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/24 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "다음 주 첫 추위",
    "caption": f"""{DISC}

[생활뉴스] 다음 주 수요일 아침 기온 5~10도 '뚝'

· 28일(수) 찬 공기 남하, 아침 기온 전날보다 5~10도 낮아져
· 서울 28일 아침 2℃ / 낮 13℃, 11월 2일 아침 1℃
· 28일·31일~11/3 전국 아침 -1~10℃, 평년(3~12℃)보다 낮아
· 내륙은 일교차 10도 이상

🔗 1인 난방템 ①~③은 프로필 링크에 있어요
🛒 더 많은 난방템 비교는 @0315_pick

출처: 기상청 중기예보(10/24 06시 발표), 위키트리 10/23 보도

#광고 #생활뉴스 #날씨 #첫추위 #기온뚝 #난방템 #미니온풍기""",
    "products": [prod(1, HEATER, "한일전기 PTC 미니 온풍기", "A"), prod(2, CUSHION, "BRUNO 극세사 온열방석 BHP-2213", "A"),
                 prod(3, FOOT, "러비쉬 BOOTS 온열 전기 풋워머", "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 주말 남부 비 ═════════
SRC2 = "출처: 기상청 예보 인용 보도 — 데일리안(10/23), 세계일보(10/23)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 생활</div>
<h1>주말 남부·제주<br><span class="hl">비 소식</span>…<br>중부는 구름</h1>
<p class="lead">비는 일요일까지 이어집니다.<br>미세먼지는 전국 '좋음~보통'.</p>""", SRC2, DL),
    a_slide(2, n, """<h2>토요일 기온</h2>
<div class="fig"><div><small>서울 아침</small><strong>13℃</strong></div><div><small>서울 낮</small><strong>21℃</strong></div></div>
<div class="fig"><div><small>춘천 아침</small><strong>10℃</strong></div><div><small>부산 낮</small><strong>19℃</strong></div></div>
<p class="lead">전국 낮 기온은 16~21도 안팎입니다.</p>""", SRC2, DL),
    a_slide(3, n, """<h2>어디에 비가 오나</h2>
<div class="box">25일까지 예상 강수량<br>부산·울산·경남 <b class="hl">30~80mm</b><br>광주·전남, 대구·경북 남부 <b class="hl">20~60mm</b><br>충청권 <b class="hl">5mm 안팎</b></div>
<p class="lead" style="font-size:38px">남해안은 바람도 강하니 외출 전 예보를 확인하세요.</p>""", SRC2, DL),
    a_slide(4, n, """<h2>비 오는 주말 빨래</h2>
<ul class="chk"><li>탈수 한 번 더 돌리기</li><li>옷 사이 주먹 하나 간격 두고 널기</li><li>바람 순환시켜 빨리 말리기</li><li>습도 높으면 제습기 함께 켜기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>빨래 <span class="hl">실내건조템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(CIRC)}"><div>듀플렉스 서큘레이터<span>빨래 쪽으로 바람 순환</span></div></li>
<li><b>2</b><img src="{img(DEHUM)}"><div>펠티어 미니 제습기<span>1.8L 물통</span></div></li>
<li><b>3</b><img src="{img(RACK)}"><div>리프룸 온열 빨래건조대<span>열선으로 데워 말리기</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/24 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "주말 남부 비·실내 빨래",
    "caption": f"""{DISC}

[생활뉴스] 주말 남부·제주 비 소식…중부는 구름

· 서울 아침 13℃ → 낮 21℃, 전국 낮 16~21도 안팎
· 25일까지 부산·울산·경남 30~80mm, 광주·전남 20~60mm
· 미세먼지 전국 '좋음~보통'

🔗 빨래 실내건조템 ①~③은 프로필 링크에 있어요

출처: 기상청 예보 인용 보도(데일리안 10/23, 세계일보 10/23)

#광고 #생활뉴스 #주말날씨 #실내건조 #빨래 #서큘레이터 #제습기""",
    "products": [prod(1, CIRC, "듀플렉스 에어 서큘레이터 DP-24BF", "A"), prod(2, DEHUM, "펠티어방식 1.8L 미니 제습기 DB-DH7", "A"),
                 prod(3, RACK, "리프룸 온열 빨래건조대 스텐", "A")],
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


write(DATE, "B", [poll("다음 주 아침 2도,<br>난방 언제 켬? 🥶", "서울 10/28(수) 아침 2℃ 예보",
                       [("바로 보일러 켠다", "추위는 못 참지"), ("11월까진 버틴다", "가스비 아껴야 해"),
                        ("이불 한 겹 더 덮는다", "전기장판보다 이불파"), ("온열방석 하나로 버틴다", "앉은 자리만 따뜻하게")], CUSHION)], {
    "title": "난방 언제 켬? 투표",
    "caption": f"""{DISC}

📊 다음 주 아침 2도, 난방 언제 켬? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 바로 보일러 켠다
2️⃣ 11월까진 버틴다
3️⃣ 이불 한 겹 더 덮는다
4️⃣ 온열방석 하나로 버틴다

🔗 4번 온열방석 링크는 프로필에
👥 맨날 춥다는 친구 태그

#광고 #투표 #공감 #첫추위 #난방 #보일러 #자취생""",
    "products": [prod(1, CUSHION, "BRUNO 극세사 온열방석 BHP-2213", "B")],
})

write(DATE, "B2", [poll("주말에 비 오면<br>빨래 어떻게 함? 🧺", "남부·제주 일요일까지 비 소식",
                        [("건조기 돌린다", "건조기는 사랑입니다"), ("맑은 날로 미룬다", "빨래통은 이미 한계"),
                         ("빨래방 간다", "한 번에 끝내기"), ("서큘레이터 틀고 실내건조", "바람이 답이다")], CIRC)], {
    "title": "주말 빨래 투표",
    "caption": f"""{DISC}

📊 주말에 비 오면 빨래 어떻게 함? 🧺
댓글에 번호로 투표해주세요!

1️⃣ 건조기 돌린다
2️⃣ 맑은 날로 미룬다
3️⃣ 빨래방 간다
4️⃣ 서큘레이터 틀고 실내건조

🔗 4번 서큘레이터 링크는 프로필에
👥 빨래 쌓아두는 친구 태그

#광고 #투표 #공감 #주말 #빨래 #실내건조 #자취생""",
    "products": [prod(1, CIRC, "듀플렉스 에어 서큘레이터 DP-24BF", "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/24 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("다음 주 아침 2도", "보일러 켜기 전", "1인 난방가전", "BEST3", [HEATER, CUSHION, FOOT]),
    c_prod(1, "0010", HEATER, "한일 PTC<br>미니 온풍기", ["책상 위·발밑에 두는 작은 온풍기", "PTC 히터 방식", "필요한 자리만 데우기"],
           ["💰 5만원대", "🚀 로켓배송"]),
    c_prod(2, "0011", CUSHION, "브루노<br>극세사 온열방석", ["의자·소파에 까는 온열방석", "부드러운 극세사 커버", "45×45cm"],
           ["💰 2만원대", "📐 45×45cm", "🚀 로켓배송"]),
    c_prod(3, "0012", FOOT, "러비쉬<br>전기 풋워머", ["부츠처럼 발을 쏙 넣는 발 온열기", "사무실 책상 밑에 두기 좋음", "발 시린 사람 추천"],
           ["💰 4만원대", "🚀 로켓배송"]),
    c_howto("0010~0012"),
], {
    "title": "1인 난방가전 BEST3",
    "caption": f"""{DISC}

다음 주 아침 2도 🥶 보일러 켜기 전 1인 난방가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 한일 PTC 미니 온풍기 💛 품번 0010
책상 위·발밑에 두고 필요한 자리만 따뜻하게.

2. 브루노 극세사 온열방석 💛 품번 0011
의자·소파에 깔기 좋은 45×45cm 온열방석.

3. 러비쉬 전기 풋워머 💛 품번 0012
부츠처럼 발을 쏙. 사무실 책상 밑에 두기 좋아요.

※ {NOTE}
※ 전열기는 멀티탭 말고 벽 콘센트에, 외출 땐 전원 끄기

#광고 #쿠팡추천템 #난방템 #미니온풍기 #온열방석 #발난로 #자취템 #사무실템""",
    "products": [prod(1, HEATER, "한일전기 PTC 미니 온풍기", "C", "0010"), prod(2, CUSHION, "BRUNO 극세사 온열방석 BHP-2213", "C", "0011"),
                 prod(3, FOOT, "러비쉬 BOOTS 온열 전기 풋워머", "C", "0012")],
})

write(DATE, "C2", [
    c_cover("비 오는 주말엔", "빨래 빨리 말리는", "실내건조템", "BEST3", [CIRC, DEHUM, RACK]),
    c_prod(1, "0013", CIRC, "듀플렉스<br>에어 서큘레이터", ["빨래 쪽으로 바람을 보내 순환", "각도 조절되는 탁상형", "평소엔 공기 순환용"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0014", DEHUM, "펠티어 방식<br>미니 제습기", ["1.8L 물통의 소형 제습기", "원룸·드레스룸·욕실용", "빨래 널린 방 습기 잡기"],
           ["💰 4만원대", "💧 1.8L", "🚀 로켓배송"]),
    c_prod(3, "0015", RACK, "리프룸<br>온열 빨래건조대", ["전기 열선으로 데워 말리는 건조대", "스텐 소재", "수건·양말 빨리 말리기"],
           ["💰 8만원대", "🔌 전기 열선"]),
    c_howto("0013~0015"),
], {
    "title": "실내건조템 BEST3",
    "caption": f"""{DISC}

비 오는 주말 🧺 빨래 빨리 말리는 실내건조템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 듀플렉스 에어 서큘레이터 💛 품번 0013
빨래 쪽으로 바람을 보내 순환. 평소엔 공기 순환용.

2. 펠티어 방식 미니 제습기 1.8L 💛 품번 0014
원룸·드레스룸에서 빨래 습기 잡기.

3. 리프룸 온열 빨래건조대 💛 품번 0015
전기 열선으로 데워 수건·양말을 빨리 말려요.

※ {NOTE}

#광고 #쿠팡추천템 #실내건조 #빨래 #서큘레이터 #제습기 #빨래건조대 #자취템""",
    "products": [prod(1, CIRC, "듀플렉스 에어 서큘레이터 DP-24BF", "C", "0013"), prod(2, DEHUM, "펠티어방식 1.8L 미니 제습기 DB-DH7", "C", "0014"),
                 prod(3, RACK, "리프룸 온열 빨래건조대 스텐", "C", "0015")],
})
print("ok")
