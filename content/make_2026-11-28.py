"""2026-11-28(토, 소형가전의 날) 게시물 6개 → docs/posts/2026-11-27/{A,B,C,A2,B2,C2}
점심: 오늘 낮 기온 5~10도 뚝·칼바람·남부 비/눈 → 몸 녹이는 찜질·족욕 가전 / 퇴근길: 블랙프라이데이 주말, 최종 결제액 비교 → 작은 주방·청소 가전
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-28"
DL = "2026.11.28 (토)"
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


FOOT, SHO, KNEE = "7345491394", "7435285276", "8337624056"
OVEN, VAC, MW = "24205802", "1279673092", "6784715012"
N_FOOT = "비타그램 접이식 족욕기 VG-FB1000"
N_SHO = "테슬테즐 전기 온열 어깨 찜질기 PS-A1"
N_KNEE = "한일의료기 원적외선 전기온열 무릎 찜질기"
N_OVEN = "제니퍼룸 미니 오븐 토스터 JR-OT12OM"
N_VAC = "홈마블 무선 핸디형 청소기 H80"
N_MW = "쿠쿠 전자레인지 다이얼식 20L"

# ═════════ A · 점심 12:00 — 낮 기온 뚝·칼바람 ═════════
SRC1 = "출처: 이투데이·한국경제(11/28)·아시아경제(11/27) — 기상청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>낮 기온<br><span class="hl">5~10도 뚝</span></h1>
<p class="lead">오늘(28일) 칼바람에<br>남부엔 비·눈</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘 <span class="hl">서울 기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>4도</strong></div><div><small>낮 최고</small><strong>8도</strong></div></div>
<div class="box">수도권 아침 전날보다 <b class="hl">5~8도</b>↓<br>전국 낮 기온 <b class="hl">5~10도</b>↓</div>""", SRC1, DL),
    a_slide(3, n, """<h2>남부 <span class="hl">비 · 눈</span></h2>
<div class="fig"><div><small>전북·전남·제주 비</small><strong>5mm</strong></div><div><small>제주 산지 눈</small><strong>1~5cm</strong></div></div>
<div class="box">전북 동부·광주전남 북동부<br>눈 <b class="hl">1~3cm</b> 예상</div>""", SRC1, DL),
    a_slide(4, n, """<h2>오늘 <span class="hl">이것 조심</span></h2>
<ul class="chk"><li>순간풍속 <span class="hl">55km/h</span> 안팎 강풍</li><li>해안·제주 <span class="hl">강풍특보</span> 가능</li><li>강원 영동 등 <span class="hl">매우 건조</span></li><li>내일 아침 대부분 <span class="hl">영하권</span></li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>집에서 <span class="hl">몸 녹이기</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FOOT)}"><div>접이식 족욕기<span>비타그램 · VG-FB1000</span></div></li>
<li><b>2</b><img src="{img(SHO)}"><div>온열 어깨 찜질기<span>테슬테즐 · PS-A1</span></div></li>
<li><b>3</b><img src="{img(KNEE)}"><div>전기온열 무릎 찜질기<span>한일의료기 · 원적외선</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/28 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "오늘 낮 기온 5~10도 뚝, 칼바람에 남부 비·눈",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 다시 추워졌어요 🥶 낮 기온 5~10도 뚝, 칼바람까지

· 28일(토) 아침 최저 0~9도, 낮 최고 7~13도 — 서울은 4~8도
· 수도권 아침 기온 전날보다 5~8도, 전국 낮 기온 5~10도 낮아요
· 비: 전북·전남광주·제주 5mm 안팎, 대전·세종·충남·충북·경남 서부 내륙 5mm 미만
· 눈: 제주 산지 1~5cm, 전북 동부·전남광주 북동부 1~3cm
· 바람: 전국 대부분 순간풍속 55km/h(15m/s) 안팎, 해안·제주엔 강풍특보 가능
· 강원 영동 등 건조특보 지역은 매우 건조 — 불씨 조심
· 내일(29일) 아침은 전국 대부분 영하권

✔ 외출할 땐 목·손 따뜻하게
✔ 집에 오면 몸부터 녹이기

🔗 집에서 몸 녹이는 ①~③은 프로필 링크에 있어요
🛒 더 많은 겨울 가전은 @0315_pick

출처: 이투데이(2026.11.28)·한국경제(2026.11.28)·아시아경제(2026.11.27) — 기상청 예보

#광고 #생활뉴스 #날씨 #기온뚝 #칼바람 #족욕기 #찜질기""",
    "products": [prod(1, FOOT, N_FOOT, "A"), prod(2, SHO, N_SHO, "A"), prod(3, KNEE, N_KNEE, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 블프 주말 ═════════
SRC2 = "출처: 세계일보(11/28)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 소비</div>
<h1>블프 주말<br><span class="hl">가전도 할인</span></h1>
<p class="lead">'최대 할인율'만 보고<br>사면 아쉬워요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>가전 <span class="hl">기획전</span></h2>
<div class="fig"><div><small>쿠팡 가전·디지털</small><strong>29일까지</strong></div><div><small>G마켓 최대</small><strong>78%</strong></div></div>
<div class="box">전자레인지·미니오븐·청소기<br><b class="hl">난방·건강 가전</b>도 할인 대상</div>""", SRC2, DL),
    a_slide(3, n, """<h2>끝나는 날 <span class="hl">제각각</span></h2>
<ul class="chk"><li>11번가 블랙 패션 위크 <span class="hl">29일</span>까지</li><li>G마켓·롯데온 <span class="hl">30일</span>까지</li><li>무신사 겨울 블프 <span class="hl">12월 2일</span>까지</li><li>유니클로 겨울 감사제 <span class="hl">12월 10일</span>까지</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>사기 전에 <span class="hl">비교</span></h2>
<ul class="chk"><li>할인율은 <span class="hl">회원 등급·결제 수단</span>에 따라 달라요</li><li>평소 판매가와 <span class="hl">최종 결제액</span> 비교</li><li>쿠폰 적용 <span class="hl">조건</span> 확인</li><li>업체별 <span class="hl">종료일</span> 확인</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>작은 집 <span class="hl">기본 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(OVEN)}"><div>미니 오븐 토스터<span>제니퍼룸 · JR-OT12OM</span></div></li>
<li><b>2</b><img src="{img(VAC)}"><div>무선 핸디형 청소기<span>홈마블 · H80</span></div></li>
<li><b>3</b><img src="{img(MW)}"><div>전자레인지 20L<span>쿠쿠 · 다이얼식</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/28 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "블랙프라이데이 주말, 가전도 할인…최종 결제액 비교",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 블랙프라이데이 주말 🛍️ 가전도 할인, 사기 전에 이것만 확인

· 쿠팡 가전·디지털 블랙프라이데이 기획전 29일까지 — 전자레인지·미니오븐·청소기, 난방·건강 가전도 할인 대상
· G마켓 30일까지 최대 78% 할인
· 롯데온 30일까지 '11월 라스트찬스'
· 11번가 '블랙 패션 위크' 29일까지(행사 상품 최대 30%)
· 무신사 12월 2일까지, 유니클로 겨울 감사제 12월 10일까지

사기 전에
· 할인율은 상품·회원 등급·결제 수단에 따라 달라요
· '최대 할인율'보다 평소 판매가와 쿠폰 적용 후 최종 결제액을 비교
· 업체마다 종료일·할인 조건이 달라요

🔗 작은 집 기본 가전 ①~③은 프로필 링크에 있어요 (할인 여부·가격은 링크에서 확인)
🛒 더 많은 가전은 @0315_pick

출처: 세계일보(2026.11.28)

#광고 #생활뉴스 #소비 #블랙프라이데이 #블프 #소형가전 #자취템""",
    "products": [prod(1, OVEN, N_OVEN, "A"), prod(2, VAC, N_VAC, "A"), prod(3, MW, N_MW, "A")],
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


write(DATE, "B", [poll("칼바람 뚫고 집 도착,<br>몸 녹이는 방법은? 🥶", "오늘 낮 기온 5~10도 뚝 · 기상청",
                       [("뜨거운 샤워", "일단 물부터"), ("전기장판 속으로", "그대로 기절"),
                        ("따뜻한 차 한 잔", "손부터 녹이기"), ("족욕", "발이 따뜻해야")], FOOT)], {
    "title": "몸 녹이는 방법 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 칼바람 뚫고 집 도착, 몸 녹이는 방법은? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 뜨거운 샤워
2️⃣ 전기장판 속으로
3️⃣ 따뜻한 차 한 잔
4️⃣ 족욕

※ 28일 전국 낮 기온 전날보다 5~10도 낮고, 순간풍속 55km/h 안팎 강한 바람 (기상청 예보, 이투데이 11/28)

🔗 4번 비타그램 접이식 족욕기 링크는 프로필에
👥 추위 많이 타는 친구 태그

#광고 #투표 #공감 #칼바람 #기온뚝 #족욕기""",
    "products": [prod(1, FOOT, N_FOOT, "B")],
})

write(DATE, "B2", [poll("블프 주말,<br>나는 이런 타입 🛍️", "쿠팡 가전·디지털 기획전 29일까지 · 세계일보",
                        [("장바구니만 채움", "결제는 다음에"), ("최저가 끝까지 비교", "탭 20개 열기"),
                         ("필요한 것만 딱", "계획 소비러"), ("미니오븐 하나 들이기", "토스트·군고구마")], OVEN)], {
    "title": "블프 쇼핑 타입 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 블프 주말, 나는 이런 타입 🛍️
댓글에 번호로 투표해주세요!

1️⃣ 장바구니만 채움
2️⃣ 최저가 끝까지 비교
3️⃣ 필요한 것만 딱
4️⃣ 미니오븐 하나 들이기

※ 쿠팡 가전·디지털 블랙프라이데이 기획전 29일까지, 할인율은 회원 등급·결제 수단에 따라 달라요 (세계일보 11/28)

🔗 4번 제니퍼룸 미니 오븐 토스터 링크는 프로필에 (가격은 링크에서 확인)
👥 같이 장바구니 털 친구 태그

#광고 #투표 #공감 #블랙프라이데이 #미니오븐 #자취템""",
    "products": [prod(1, OVEN, N_OVEN, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/28 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("칼바람에 기온 뚝 🥶", "집에서", "몸 녹이는", "BEST3", [FOOT, SHO, KNEE]),
    c_prod(1, "0220", FOOT, "접이식<br>족욕기", ["비타그램 VG-FB1000", "접어서 보관", "발부터 따뜻하게"],
           ["💰 3만원대", "📦 접이식"]),
    c_prod(2, "0221", SHO, "온열 어깨<br>찜질기", ["테슬테즐 PS-A1", "어깨에 걸치는 형태", "전기 온열 방식"],
           ["💰 4만원대", "📦 어깨용"]),
    c_prod(3, "0222", KNEE, "온열 무릎<br>찜질기", ["한일의료기", "원적외선 전기온열", "무릎에 감싸는 형태"],
           ["💰 4만원대", "📦 무릎용"]),
    c_howto("0220~0222"),
], {
    "title": "집에서 몸 녹이는 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

칼바람에 기온 뚝 🥶 집에서 몸 녹이는 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 비타그램 접이식 족욕기 VG-FB1000 💛 품번 0220
쓰고 나면 접어서 보관하는 족욕기.

2. 테슬테즐 전기 온열 어깨 찜질기 PS-A1 💛 품번 0221
어깨에 걸치고 TV 보면서.

3. 한일의료기 원적외선 전기온열 무릎 찜질기 💛 품번 0222
무릎에 감싸 두는 전기 온열 찜질기.

✔ 28일 전국 낮 기온 전날보다 5~10도 낮아요, 29일 아침 대부분 영하권

※ 날씨: 기상청 예보(이투데이·한국경제 11/28, 아시아경제 11/27)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #족욕기 #찜질기 #겨울가전 #집콕""",
    "products": [prod(1, FOOT, N_FOOT, "C", "0220"), prod(2, SHO, N_SHO, "C", "0221"), prod(3, KNEE, N_KNEE, "C", "0222")],
})

write(DATE, "C2", [
    c_cover("블프 주말 🛍️", "작은 집", "기본 가전", "BEST3", [OVEN, VAC, MW]),
    c_prod(1, "0223", OVEN, "미니 오븐<br>토스터", ["제니퍼룸 JR-OT12OM", "오트밀 색상", "토스트·데우기"],
           ["💰 4만원대", "📦 미니"]),
    c_prod(2, "0224", VAC, "무선 핸디<br>청소기", ["홈마블 H80", "무선 핸디형", "책상·소파 틈새"],
           ["💰 4만원대", "📦 핸디형"]),
    c_prod(3, "0225", MW, "전자레인지<br>20L", ["쿠쿠", "다이얼식 20L", "돌리기만 하면 끝"],
           ["💰 5만원대", "📦 20L"]),
    c_howto("0223~0225"),
], {
    "title": "작은 집 기본 가전 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

블프 주말 🛍️ 작은 집 기본 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 제니퍼룸 미니 오븐 토스터 JR-OT12OM 💛 품번 0223
토스트 굽고 식은 음식 데우기.

2. 홈마블 무선 핸디형 청소기 H80 💛 품번 0224
선 없이 책상·소파 틈새 청소.

3. 쿠쿠 전자레인지 다이얼식 20L 💛 품번 0225
다이얼 돌리면 끝나는 기본 전자레인지.

✔ 블프 할인율은 회원 등급·결제 수단마다 달라요 — 최종 결제액 비교하기

※ 블프 정보: 세계일보(11/28)
※ {NOTE} · 할인 여부는 링크에서 확인

#광고 #쿠팡추천템 #소형가전 #블랙프라이데이 #미니오븐 #핸디청소기 #전자레인지""",
    "products": [prod(1, OVEN, N_OVEN, "C", "0223"), prod(2, VAC, N_VAC, "C", "0224"), prod(3, MW, N_MW, "C", "0225")],
})
print("ok")
