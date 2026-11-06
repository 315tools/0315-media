"""2026-11-06(금, 식품의 날) 게시물 6개 → docs/posts/2026-11-06/{A,B,C,A2,B2,C2}
점심: 입동 서울 첫 영하·따끈한 아침 간편식 / 퇴근길: 일요일 중부 비·눈·집콕 국물 밀키트
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-06"
DL = "2026.11.06 (금)"
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





SOUP, NRG, JUK = "8169306605", "8989662831", "8616947721"
BDJ, KAL, SHA = "7387532866", "1546636258", "8308733382"
N_SOUP = "폰타나 컵수프 머쉬룸·콘·브로콜리·어니언 각 2p"
N_NRG = "오뚜기 옛날 구수한 누룽지 컵형"
N_JUK = "동원 양반죽 간편식 파우치 6종"
N_BDJ = "MYCHEF 놀부 부대찌개 밀키트 2인분"
N_KAL = "프레시지 장칼국수 밀키트 2인분"
N_SHA = "채선당 모둠 샤브 전골"

# ═════════ A · 점심 12:00 — 입동 서울 첫 영하 ═════════
SRC1 = "출처: 한국경제(11/6)·경향신문·디지털타임스(11/5), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 입동</div>
<h1>내일 서울<br><span class="hl">첫 영하</span> 전망</h1>
<p class="lead">7일(토, 입동) 서울 아침 -1도<br>체감온도는 -5도 안팎</p>""", SRC1, DL),
    a_slide(2, n, """<h2>이틀 기온 한눈에</h2>
<div class="fig"><div><small>6일(금) 아침</small><strong>1~11도</strong></div><div><small>6일 낮</small><strong>8~16도</strong></div></div>
<div class="fig"><div><small>7일(토) 아침</small><strong>-4~5도</strong></div><div><small>7일 낮</small><strong>8~14도</strong></div></div>
<div class="box">경기 연천·강원 대관령<br>7일 아침 <b class="hl">-5도</b> 예보</div>""", SRC1, DL),
    a_slide(3, n, """<h2>바람이 <span class="hl">체감 추위</span>를 키워요</h2>
<div class="fig"><div><small>순간풍속(7일 오전까지)</small><strong>초속 15m</strong></div><div><small>해상 물결</small><strong>1.5~4m</strong></div></div>
<div class="box">내륙 중심으로 <b class="hl">서리</b>가 내리고<br>얼음이 어는 곳도 있겠어요</div>""", SRC1, DL),
    a_slide(4, n, """<h2>첫 영하 아침 <span class="hl">준비</span></h2>
<ul class="chk"><li>두꺼운 외투·목도리 꺼내 두기</li><li>빈속 대신 <span class="hl">따끈한 한 끼</span></li><li>사무실 서랍에 컵수프·누룽지</li><li>바람 센 날 야외 활동 짧게</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>추운 아침 <span class="hl">든든템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SOUP)}"><div>폰타나 컵수프 4종<span>머쉬룸·콘·브로콜리·어니언 각 2p</span></div></li>
<li><b>2</b><img src="{img(NRG)}"><div>오뚜기 옛날 누룽지 컵<span>컵형 · 구수한 누룽지</span></div></li>
<li><b>3</b><img src="{img(JUK)}"><div>동원 양반죽 파우치 6종<span>전복·쇠고기·참치 등 6가지</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/6 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "입동 서울 첫 영하 -1도",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 입동(7일) 서울 아침 -1도, 올가을 첫 영하 전망 🥶

· 6일(금) 아침 1~11도, 낮 8~16도 — 수도권 아침은 전날보다 5~8도가량 낮아요
· 7일(토, 입동) 아침 -4~5도, 낮 8~14도 — 서울 -1도, 체감 -5도 안팎
· 경기 연천·강원 대관령은 7일 아침 -5도 예보
· 7일 오전까지 순간풍속 초속 15m 안팎 강한 바람, 내륙엔 서리·얼음 어는 곳도

✔ 두꺼운 외투·목도리 챙기고, 빈속 출근은 피하기

🔗 추운 아침 든든템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 한국경제(11/6)·경향신문(11/5)·디지털타임스(11/5) — 기상청 예보

#광고 #생활뉴스 #날씨 #입동 #첫영하 #컵수프 #누룽지 #양반죽""",
    "products": [prod(1, SOUP, N_SOUP, "A"), prod(2, NRG, N_NRG, "A"), prod(3, JUK, N_JUK, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 일요일 중부 비·눈 ═════════
SRC2 = "출처: 경향신문(11/5)·한국경제(11/6), 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 주말</div>
<h1>일요일 중부<br><span class="hl">비 소식</span></h1>
<p class="lead">강원 산지엔 눈<br>다음 주 초까지 쌀쌀</p>""", SRC2, DL),
    a_slide(2, n, """<h2>8일(일) 비는 <span class="hl">이렇게</span></h2>
<ul class="chk"><li>오전 <span class="hl">북쪽 지역</span>부터 시작</li><li>오후 수도권·강원·충북 북부로</li><li>강원 내륙은 비·눈 섞일 수도</li><li>강원 산지는 <span class="hl">눈</span></li></ul>""", SRC2, DL),
    a_slide(3, n, """<h2>다음 주 초까지 <span class="hl">쌀쌀</span></h2>
<div class="fig"><div><small>8일(일) 아침</small><strong>-2~6도</strong></div><div><small>8일 낮</small><strong>7~15도</strong></div></div>
<div class="fig"><div><small>9일(월) 아침</small><strong>0~9도</strong></div><div><small>9일 낮</small><strong>10~15도</strong></div></div>
<div class="box">평년보다 낮은 기온<br>내륙은 <b class="hl">일교차 10도 이상</b></div>""", SRC2, DL),
    a_slide(4, n, """<h2>비 오는 주말 <span class="hl">준비</span></h2>
<ul class="chk"><li>일요일 외출엔 우산</li><li>장보기는 토요일에 미리</li><li>저녁은 집에서 <span class="hl">뜨끈한 전골</span></li><li>월요일 출근길 외투 챙기기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>집콕 주말 <span class="hl">국물템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BDJ)}"><div>놀부 부대찌개 밀키트<span>MYCHEF · 2인분</span></div></li>
<li><b>2</b><img src="{img(KAL)}"><div>프레시지 장칼국수<span>밀키트 · 2인분</span></div></li>
<li><b>3</b><img src="{img(SHA)}"><div>채선당 모둠 샤브 전골<span>집에서 샤브샤브 한 냄비</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/6 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "일요일 중부 비·강원 산지 눈",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 일요일(8일) 중부 비, 강원 산지엔 눈 🌧️

· 8일 오전 북쪽 지역부터 비 → 오후 수도권·강원·충북 북부로 확대
· 강원 내륙은 비·눈이 섞이고, 산지는 눈 소식
· 8일 아침 -2~6도, 낮 7~15도 / 9일(월) 아침 0~9도, 낮 10~15도
· 다음 주 초반까지 평년보다 낮은 기온, 내륙은 일교차 10도 이상

✔ 일요일 외출엔 우산, 장보기는 토요일에 미리

🔗 집콕 주말 국물템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 경향신문(11/5)·한국경제(11/6) — 기상청 예보

#광고 #생활뉴스 #날씨 #주말날씨 #집콕 #밀키트 #부대찌개 #샤브샤브""",
    "products": [prod(1, BDJ, N_BDJ, "A"), prod(2, KAL, N_KAL, "A"), prod(3, SHA, N_SHA, "A")],
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


write(DATE, "B", [poll("추운 아침,<br>나의 아침밥은? 🥶", "7일(입동) 서울 아침 -1도 (기상청 예보)",
                       [("굶고 출근", "5분 더 자는 게 이득"), ("편의점 삼각김밥", "가는 길에 해결"),
                        ("커피 한 잔", "카페인이 곧 아침"), ("따끈한 컵수프", "물만 부으면 몸이 사르르")], SOUP)], {
    "title": "추운 아침 아침밥 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 추운 아침, 나의 아침밥은? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 굶고 출근
2️⃣ 편의점 삼각김밥
3️⃣ 커피 한 잔
4️⃣ 따끈한 컵수프

※ 7일(입동) 서울 아침 -1도, 체감 -5도 안팎 (기상청 예보, 한국경제 11/6)

🔗 4번 폰타나 컵수프 링크는 프로필에
👥 아침마다 커피로 버티는 친구 태그

#광고 #투표 #공감 #입동 #아침밥 #컵수프""",
    "products": [prod(1, SOUP, N_SOUP, "B")],
})

write(DATE, "B2", [poll("비 오는 일요일 저녁,<br>메뉴는? 🍲", "8일(일) 중부 비, 강원 산지 눈 (기상청 예보)",
                        [("배달 앱 켜기", "고민은 배송만 늦출 뿐"), ("라면 하나", "국물엔 역시 라면"),
                         ("냉장고 털기", "있는 걸로 버틴다"), ("부대찌개 보글보글", "햄 듬뿍 냄비째")], BDJ)], {
    "title": "비 오는 일요일 저녁 메뉴 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 비 오는 일요일 저녁, 메뉴는? 🍲
댓글에 번호로 투표해주세요!

1️⃣ 배달 앱 켜기
2️⃣ 라면 하나
3️⃣ 냉장고 털기
4️⃣ 부대찌개 보글보글

※ 8일(일) 오전 북쪽부터 비, 오후 수도권·강원·충북 북부로 확대 (기상청 예보, 경향신문 11/5)

🔗 4번 놀부 부대찌개 밀키트 링크는 프로필에
👥 주말마다 메뉴 못 고르는 친구 태그

#광고 #투표 #공감 #주말 #집콕 #부대찌개""",
    "products": [prod(1, BDJ, N_BDJ, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/6 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("입동 서울 첫 영하", "추운 아침", "든든템", "BEST3", [SOUP, NRG, JUK]),
    c_prod(1, "0088", SOUP, "폰타나<br>컵수프 4종", ["머쉬룸·콘·브로콜리·어니언", "맛별 2p씩 8개", "사무실 서랍 상비용"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0089", NRG, "오뚜기<br>옛날 누룽지 컵", ["컵형 누룽지", "구수한 한 그릇", "아침 대용·야식용"],
           ["💰 1만원 이하", "🚀 로켓배송"]),
    c_prod(3, "0090", JUK, "동원<br>양반죽 파우치 6종", ["전복·쇠고기·참치 등", "죽 6종 구성", "파우치형 간편식"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_howto("0088~0090"),
], {
    "title": "추운 아침 든든템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

입동 서울 첫 영하 🥶 추운 아침 든든템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 폰타나 컵수프 머쉬룸·콘·브로콜리·어니언 각 2p 💛 품번 0088
네 가지 맛 컵수프, 사무실 서랍에 두고 아침 대용으로.

2. 오뚜기 옛날 구수한 누룽지 컵형 💛 품번 0089
컵형 누룽지, 구수한 한 그릇.

3. 동원 양반죽 파우치 6종 💛 품번 0090
전복·쇠고기·참치죽 등 6종이 든 파우치 죽 세트.

※ 날씨: 기상청 예보(한국경제 11/6·경향신문 11/5 보도)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #간편식 #컵수프 #누룽지 #양반죽 #입동""",
    "products": [prod(1, SOUP, N_SOUP, "C", "0088"), prod(2, NRG, N_NRG, "C", "0089"), prod(3, JUK, N_JUK, "C", "0090")],
})

write(DATE, "C2", [
    c_cover("일요일 중부 비", "집콕 저녁", "국물템", "BEST3", [BDJ, KAL, SHA]),
    c_prod(1, "0091", BDJ, "놀부<br>부대찌개 밀키트", ["MYCHEF 밀키트", "2인분", "냄비에 끓이기만"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0092", KAL, "프레시지<br>장칼국수 밀키트", ["장칼국수 밀키트", "2인분", "비 오는 날 한 그릇"],
           ["💰 1만원 이하", "🚀 로켓배송"]),
    c_prod(3, "0093", SHA, "채선당<br>모둠 샤브 전골", ["집에서 샤브 전골", "주말 저녁 한 냄비", "로켓프레시 상품"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0091~0093"),
], {
    "title": "집콕 저녁 국물템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

일요일 중부 비 🌧️ 집콕 저녁 국물템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. MYCHEF 놀부 부대찌개 밀키트 2인분 💛 품번 0091
냄비에 넣고 끓이면 되는 부대찌개 밀키트.

2. 프레시지 장칼국수 밀키트 2인분 💛 품번 0092
비 오는 날 끓여 먹는 장칼국수 2인분.

3. 채선당 모둠 샤브 전골 💛 품번 0093
주말 저녁 집에서 샤브 전골 한 냄비.

※ 날씨: 기상청 예보(경향신문 11/5·한국경제 11/6 보도)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #밀키트 #부대찌개 #칼국수 #샤브샤브 #집콕""",
    "products": [prod(1, BDJ, N_BDJ, "C", "0091"), prod(2, KAL, N_KAL, "C", "0092"), prod(3, SHA, N_SHA, "C", "0093")],
})
print("ok")
