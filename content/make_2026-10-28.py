"""2026-10-28(수, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-10-28/{A,B,C,A2,B2,C2}
점심: 오늘 아침 최저 -2도, 5~10도 뚝·내륙 서리·얼음 / 퇴근길: 이번 주말 단풍 절정(단풍나무·참나무 10/31)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-10-28"
DL = "2026.10.28 (수)"
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


FROST, GLOVE, EAR = "8304588513", "8502669620", "9784342440"
STICK, CUP, SEAT = "8915242678", "7601277829", "7330431138"
N_FROST, N_GLOVE, N_EAR = "탐사 차량용 성에방지 커버 (블랙박스 녹화 가능)", "꿈보 초전도 스마트 터치 장갑 1+1", "로이엔 접이식 퍼 귀마개 귀도리"
N_STICK, N_CUP, N_SEAT = "셀루미 메가 스틱 올인원 셀카봉 삼각대 171.7cm", "접이식 실리콘 텀블러 자바라컵 1+1", "다인네 접이식 휴대용 4단 방석 2p + 파우치"

# ═════════ A · 점심 12:00 — 첫 영하권 아침 ═════════
SRC1 = "출처: 월요신문·뉴스1(10/28, 기상청 예보)"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 첫 추위</div>
<h1>오늘 아침<br><span class="hl">최저 -2도</span><br>하루 새 5~10도 뚝</h1>
<p class="lead">경기 북동부·강원 내륙 영하권<br>내륙 곳곳 서리·얼음</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘 아침 · 낮 기온</h2>
<div class="fig"><div><small>춘천</small><strong>-2 / 13도</strong></div><div><small>서울</small><strong>2 / 13도</strong></div></div>
<div class="fig"><div><small>대전</small><strong>1 / 13도</strong></div><div><small>대구</small><strong>1 / 14도</strong></div></div>
<div class="box">전국 아침 <b class="hl">-2~7도</b> · 낮 <b class="hl">11~17도</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>바람에 체감은 더 춥게</h2>
<ul class="chk"><li>전남 해안·제주 오전까지<br>순간풍속 <span class="hl">시속 70km</span> 이상</li><li>남부지방 아침까지<br>순간풍속 시속 55km 이상</li><li>미세먼지는 전 권역 <span class="hl">좋음</span></li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>첫 영하권 체크</h2>
<ul class="chk"><li>아침 차 앞유리 서리·얼음 확인</li><li>손·귀부터 시려요, 장갑·귀마개</li><li>낮엔 13도 안팎, 얇게 겹쳐 입기</li><li>서리 내린 길·계단 미끄럼 조심</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>첫 추위 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FROST)}"><div>탐사 성에방지 커버<span>블랙박스 녹화 가능</span></div></li>
<li><b>2</b><img src="{img(GLOVE)}"><div>꿈보 스마트 터치 장갑<span>1+1 · 장갑 낀 채 폰</span></div></li>
<li><b>3</b><img src="{img(EAR)}"><div>로이엔 접이식 귀마개<span>퍼 귀도리 · 접어서 휴대</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/28 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "오늘 아침 -2도·5~10도 뚝",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘 아침 최저 -2도, 하루 새 5~10도 뚝

· 북서쪽 찬 공기로 아침 기온 전날보다 5~10도 떨어져
· 아침 -2~7도, 낮 11~17도 (춘천 -2/13, 서울 2/13, 대전 1/13, 대구 1/14, 부산 7/17)
· 경기 북동부·강원 내륙 영하권, 내륙 곳곳 서리·얼음
· 전남 해안·제주 오전까지 순간풍속 시속 70km 이상 — 체감온도 더 낮아요
· 미세먼지는 전 권역 '좋음'

✔ 아침 차 앞유리 서리 확인, 장갑·귀마개 챙기기, 낮엔 얇게 겹쳐 입기

🔗 첫 추위 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 월요신문(10/28), 뉴스1(10/28) — 기상청 예보

#광고 #생활뉴스 #날씨 #첫추위 #영하권 #출근길 #서리 #방한템""",
    "products": [prod(1, FROST, N_FROST, "A"), prod(2, GLOVE, N_GLOVE, "A"), prod(3, EAR, N_EAR, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 단풍 절정 ═════════
SRC2 = "출처: 산림청 '2026 단풍절정 예측지도' 인용 한국영농신문(9/23)·국제뉴스(10/10)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">나들이 · 단풍</div>
<h1>이번 주말,<br><span class="hl">단풍 절정</span><br>예상됩니다</h1>
<p class="lead">단풍나무·참나무 10월 31일<br>은행나무 10월 30일 절정 예측</p>""", SRC2, DL),
    a_slide(2, n, """<h2>산별 절정 예상일</h2>
<div class="fig"><div><small>설악산</small><strong>10/20</strong></div><div><small>속리산</small><strong>10/28</strong></div></div>
<div class="fig"><div><small>내장산</small><strong>11/4</strong></div><div><small>한라산</small><strong>11/6</strong></div></div>""", SRC2, DL),
    a_slide(3, n, """<h2>'절정'이란?</h2>
<div class="box">산 전체의 약 <b class="hl">50%</b>가<br>물든 때를 말해요</div>
<p class="lead" style="font-size:36px">올해는 최근 5년 평균보다<br>약 0.8일 늦을 것으로 분석</p>""", SRC2, DL),
    a_slide(4, n, """<h2>단풍 나들이 체크</h2>
<ul class="chk"><li>기온·비·바람 따라 며칠씩 달라져요</li><li>비가 많이 오면 절정 전에 낙엽</li><li>출발 전 현지 상황 다시 확인</li><li>오늘 아침 춘천 <span class="hl">-2도</span>, 겉옷 챙기기</li></ul>""",
            "출처: 국제뉴스(10/10, 산림청 예측), 월요신문(10/28, 기상청 예보)", DL),
    a_slide(5, n, f"""<h2>단풍 나들이 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(STICK)}"><div>셀루미 메가 스틱<span>셀카봉 겸 삼각대 171.7cm</span></div></li>
<li><b>2</b><img src="{img(CUP)}"><div>접이식 실리콘 텀블러<span>1+1 · 접으면 납작</span></div></li>
<li><b>3</b><img src="{img(SEAT)}"><div>다인네 접이식 4단 방석<span>2p + 파우치</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/28 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "이번 주말 단풍 절정",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 이번 주말, 단풍 절정 예상됩니다 🍁

· 산림청 '2026 한반도 단풍절정 예측지도' — 단풍나무·참나무류 10월 31일, 은행나무 10월 30일
· 산별 절정 예상: 설악산 10/20, 속리산 10/28, 내장산 11/4, 한라산 11/6
· 절정 = 산 전체의 약 50%가 물든 때, 올해는 최근 5년 평균보다 약 0.8일 늦어
· 기온·비·바람에 따라 며칠씩 달라질 수 있어 출발 전 현지 확인 필요
· 오늘 아침 춘천 -2도·서울 2도 — 아침 나들이엔 겉옷 챙기기

🔗 단풍 나들이 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 한국영농신문(9/23)·국제뉴스(10/10) — 산림청 예측, 월요신문(10/28) — 기상청 예보

#광고 #생활뉴스 #단풍 #단풍절정 #가을나들이 #주말나들이 #등산 #은행나무""",
    "products": [prod(1, STICK, N_STICK, "A"), prod(2, CUP, N_CUP, "A"), prod(3, SEAT, N_SEAT, "A")],
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


write(DATE, "B", [poll("첫 영하권 출근길,<br>나의 방한 1순위는? 🥶", "오늘 아침 춘천 -2도 · 서울 2도 (기상청 예보)",
                       [("패딩 조기 개시", "아직 10월이지만"), ("핫팩 주머니에", "손만 따뜻하면 돼"),
                        ("목도리 칭칭", "목이 따뜻해야 살아"), ("귀도리 장착", "귀가 제일 시려")], EAR)], {
    "title": "첫 영하권 방한 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 첫 영하권 출근길, 나의 방한 1순위는? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 패딩 조기 개시
2️⃣ 핫팩 주머니에
3️⃣ 목도리 칭칭
4️⃣ 귀도리 장착

🔗 4번 접이식 귀도리 링크는 프로필에
👥 벌써 패딩 꺼낸 친구 태그

#광고 #투표 #공감 #첫추위 #출근길 #귀도리 #직장인""",
    "products": [prod(1, EAR, N_EAR, "B")],
})

write(DATE, "B2", [poll("단풍 구경 가면<br>나는 어떤 타입? 🍁", "이번 주말 단풍나무 절정 예측 10/31 (산림청)",
                        [("정상까지 등산파", "땀 흘려야 제맛"), ("드라이브파", "창밖으로 감상"),
                         ("카페 창가파", "커피 한 잔에 단풍 한 장"), ("인생샷 남기기파", "삼각대 들고 출동")], STICK)], {
    "title": "단풍 구경 타입 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 단풍 구경 가면 나는 어떤 타입? 🍁
댓글에 번호로 투표해주세요!

1️⃣ 정상까지 등산파
2️⃣ 드라이브파
3️⃣ 카페 창가파
4️⃣ 인생샷 남기기파

🔗 4번 셀카봉 삼각대 링크는 프로필에
👥 단풍 보러 같이 갈 친구 태그

#광고 #투표 #공감 #단풍 #가을나들이 #인생샷 #셀카봉""",
    "products": [prod(1, STICK, N_STICK, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/28 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("오늘 아침 -2도", "첫 영하 출근길", "방한 특이템", "BEST3", [FROST, GLOVE, EAR]),
    c_prod(1, "0034", FROST, "탐사<br>차량용 성에방지 커버", ["앞유리 서리·눈 덮개", "블랙박스 녹화 가능 창", "보관용 가방 포함"],
           ["💰 7천원대", "🚀 로켓배송"]),
    c_prod(2, "0035", GLOVE, "꿈보<br>초전도 스마트 터치 장갑", ["장갑 낀 채 스마트폰 터치", "1+1 구성", "출근길 손 시림 대비"],
           ["💰 8천원대", "🚀 로켓배송"]),
    c_prod(3, "0036", EAR, "로이엔<br>접이식 퍼 귀마개", ["접어서 가방에 쏙", "퍼 귀도리", "남녀공용"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0034~0036"),
], {
    "title": "첫 영하 방한 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

오늘 아침 -2도 🥶 첫 영하 출근길 방한 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 탐사 차량용 성에방지 커버 💛 품번 0034
앞유리 서리·눈 덮개, 블랙박스 녹화 가능 창 + 보관 가방.

2. 꿈보 초전도 스마트 터치 장갑 1+1 💛 품번 0035
장갑 낀 채로 스마트폰 터치.

3. 로이엔 접이식 퍼 귀마개 💛 품번 0036
접어서 가방에 넣고 다니는 귀도리.

※ {NOTE}

#광고 #쿠팡추천템 #특이템 #첫추위 #성에방지커버 #터치장갑 #귀도리 #출근길""",
    "products": [prod(1, FROST, N_FROST, "C", "0034"), prod(2, GLOVE, N_GLOVE, "C", "0035"), prod(3, EAR, N_EAR, "C", "0036")],
})

write(DATE, "C2", [
    c_cover("이번 주말 단풍 절정", "단풍 보러 갈 때", "나들이 특이템", "BEST3", [STICK, CUP, SEAT]),
    c_prod(1, "0037", STICK, "셀루미<br>메가 스틱 셀카봉 삼각대", ["셀카봉 겸 삼각대", "최대 171.7cm", "단풍 배경 단체 사진"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0038", CUP, "접이식<br>실리콘 텀블러 자바라컵", ["접으면 납작해지는 컵", "1+1 구성", "가방 속 공간 절약"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0039", SEAT, "다인네<br>접이식 휴대용 4단 방석", ["4단으로 접는 방석", "2p + 파우치 2p", "벤치·바위 위에 깔기"],
           ["💰 4천원대", "🚀 로켓배송"]),
    c_howto("0037~0039"),
], {
    "title": "단풍 나들이 특이템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

이번 주말 단풍 절정 🍁 단풍 보러 갈 때 나들이 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 셀루미 메가 스틱 셀카봉 삼각대 171.7cm 💛 품번 0037
셀카봉 겸 삼각대, 단풍 배경 단체 사진용.

2. 접이식 실리콘 텀블러 자바라컵 1+1 💛 품번 0038
접으면 납작해져서 가방 속 공간 절약.

3. 다인네 접이식 휴대용 4단 방석 2p 💛 품번 0039
벤치·바위 위에 깔고 앉기, 파우치 포함.

※ {NOTE}

#광고 #쿠팡추천템 #특이템 #단풍 #가을나들이 #셀카봉 #접이식컵 #휴대용방석""",
    "products": [prod(1, STICK, N_STICK, "C", "0037"), prod(2, CUP, N_CUP, "C", "0038"), prod(3, SEAT, N_SEAT, "C", "0039")],
})
print("ok")
