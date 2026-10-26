"""2026-10-26(월, 생활용품의 날) 게시물 6개 → docs/posts/2026-10-26/{A,B,C,A2,B2,C2}
점심: 보일러 켜기 전 점검·실내 18~20℃ / 퇴근길: 28일 아침 -2~7℃, 5~10도 뚝 → 겨울 잠자리 준비
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-10-26"
DL = "2026.10.26 (월)"
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


THERMO, CURT, SOCK = "9642046260", "6711426204", "9081602559"
QUILT, PACK, BLANK = "6718528503", "8451050587", "4368997131"
N_THERMO, N_CURT, N_SOCK = "아이리버 디지털 미니 온습도계 ITH-100", "코멧 홈 단열 아일렛 암막 커튼 2개입", "이지하임 무압박 수면양말 4켤레"
N_QUILT, N_PACK, N_BLANK = "코멧 홈 양면 극세사 차렵이불", "조은리빙 이불 압축팩", "라이프란스 포근양 극세사 담요"

# ═════════ A · 점심 12:00 — 보일러 켜기 전 점검 ═════════
SRC1 = "출처: 서울시 환경 누리집(10/23), 비건뉴스(10/24)"
n = 6
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 난방</div>
<h1>보일러 켜기 전<br><span class="hl">이것부터</span><br>확인하세요</h1>
<p class="lead">서울시가 알려 준<br>난방 시작 전 점검 순서</p>""", SRC1, DL),
    a_slide(2, n, """<h2>보일러 가동 전 점검</h2>
<ul class="chk"><li>전원·작동 상태·오류 표시</li><li>배관·연결부 누수·부식</li><li>배기통 이탈·찌그러짐·막힘</li><li>시험 가동해 따뜻해지는지</li></ul>
<div class="box">가스 냄새·배기통 이상이 있으면<br><b class="hl">사용 중단 → 전문업체 점검</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>서울시 권장 실내 환경</h2>
<div class="fig"><div><small>실내 온도</small><strong>18~20℃</strong></div><div><small>실내 습도</small><strong>40~60%</strong></div></div>
<p class="lead" style="font-size:34px">온도는 개인 건강 상태에 따라 조절<br>난방 중에도 짧게 환기하기</p>""", SRC1, DL),
    a_slide(4, n, """<h2>보일러 주변도 정리</h2>
<ul class="chk"><li>보일러 주변 쌓인 물건 치우기</li><li>스프레이·비닐 등 불붙기 쉬운 물건 X</li><li>바닥 상자 옮겨 물기·얼룩 확인</li><li>결로 줄이려면 <span class="hl">5~10분</span> 환기</li></ul>
<p class="lead" style="font-size:32px">한국에너지공단 난방설비 매뉴얼 안내 (비건뉴스 인용)</p>""", SRC1, DL),
    a_slide(5, n, """<h2>난방비 아끼는 습관</h2>
<ul class="chk"><li>밤에는 커튼 닫아 열 손실 줄이기</li><li>문틈·창틈은 문풍지로</li><li>내복·양말·겉옷 활용</li><li>외출 땐 외출 모드</li></ul>""", "출처: 서울시 환경 누리집(10/23)", DL),
    a_slide(6, n, f"""<h2>난방 시작 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(THERMO)}"><div>아이리버 미니 온습도계<span>18~20℃·40~60% 확인용</span></div></li>
<li><b>2</b><img src="{img(CURT)}"><div>코멧 홈 단열 암막 커튼<span>아일렛형 2장 세트</span></div></li>
<li><b>3</b><img src="{img(SOCK)}"><div>이지하임 무압박 수면양말<span>4켤레 세트</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/26 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "보일러 켜기 전 점검",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 보일러 켜기 전 이것부터 확인하세요

· 전원·오류 표시, 배관 누수·부식, 배기통 이탈·막힘 확인 후 시험 가동
· 가스 냄새나 배기통 이상이 있으면 사용 중단 → 전문업체 점검
· 서울시 권장 실내 온도 18~20℃, 습도 40~60%
· 보일러 주변 물건·불붙기 쉬운 물건 치우기, 결로 줄이려면 5~10분 환기
· 밤엔 커튼 닫고, 문틈은 문풍지로, 내복·양말 활용

🔗 난방 시작 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 서울시 환경 누리집(10/23), 비건뉴스(10/24)

#광고 #생활뉴스 #보일러 #난방 #난방비절약 #겨울준비 #온습도계 #생활꿀팁""",
    "products": [prod(1, THERMO, N_THERMO, "A"), prod(2, CURT, N_CURT, "A"), prod(3, SOCK, N_SOCK, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 28일 아침 -2~7℃ ═════════
SRC2 = "출처: 기상청 예보 인용 보도 — 이투데이·톱스타뉴스(10/26)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 생활</div>
<h1>오늘 서울 낮 20도,<br>수요일 아침은<br><span class="hl">5~10도 뚝</span></h1>
<p class="lead">내일 오후부터 찬 공기가 내려와<br>이번 주 중반 쌀쌀해집니다.</p>""", SRC2, DL),
    a_slide(2, n, """<h2>전국 아침 최저기온</h2>
<div class="fig"><div><small>27일(화)</small><strong>6~15℃</strong></div><div><small>28일(수)</small><strong>-2~7℃</strong></div></div>
<div class="box">28일 아침, 전날보다<br><b class="hl">5~10도가량 낮아질 전망</b></div>""", SRC2, DL),
    a_slide(3, n, """<h2>28일 영하권 예상 지역</h2>
<ul class="chk"><li>경기 북동부</li><li>강원 내륙·산지</li><li>충북·일부 남부 내륙</li></ul>
<p class="lead" style="font-size:36px">내륙 곳곳 서리·얼음 가능<br>강한 바람에 체감온도는 더 낮아요.</p>""", SRC2, DL),
    a_slide(4, n, """<h2>오늘 밤 잠자리 준비</h2>
<ul class="chk"><li>겨울 이불 꺼내 먼지 털기</li><li>여름 이불은 말린 뒤 보관</li><li>소파·책상엔 무릎담요 하나</li><li>창문 닫고 자기 전 짧게 환기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>이불 바꾸는 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(QUILT)}"><div>코멧 홈 극세사 차렵이불<span>양면 극세사</span></div></li>
<li><b>2</b><img src="{img(PACK)}"><div>조은리빙 이불 압축팩<span>여름 이불 부피 줄이기</span></div></li>
<li><b>3</b><img src="{img(BLANK)}"><div>라이프란스 극세사 담요<span>소파·사무실 무릎담요</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/26 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "수요일 아침 5~10도 뚝",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 오늘 서울 낮 20도, 수요일 아침은 5~10도 뚝

· 26일 서울 아침 15도 / 낮 20도
· 27일 오후부터 찬 공기 남하, 강한 바람에 체감온도 더 낮아
· 28일(수) 전국 아침 최저 -2~7℃, 전날보다 5~10도가량 낮아질 전망
· 경기 북동부·강원 내륙·충북·일부 남부 내륙은 영하, 서리·얼음 가능

🔗 겨울 이불로 바꾸는 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 기상청 예보 인용 보도(이투데이·톱스타뉴스 10/26)

#광고 #생활뉴스 #날씨 #첫추위 #겨울이불 #이불정리 #극세사이불 #겨울준비""",
    "products": [prod(1, QUILT, N_QUILT, "A"), prod(2, PACK, N_PACK, "A"), prod(3, BLANK, N_BLANK, "A")],
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


write(DATE, "B", [poll("보일러 처음 켜는<br>나만의 기준은? 🔥", "서울시 권장 실내 18~20℃ · 습도 40~60%",
                       [("10월 되면 켠다", "달력이 기준"), ("손 시려야 켠다", "버틸 때까지 버팀"),
                        ("가족이 먼저 켠다", "나는 모르는 일"), ("온습도계 보고 켠다", "18도 밑이면 출동")], THERMO)], {
    "title": "보일러 켜는 기준 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 보일러 처음 켜는 나만의 기준은? 🔥
댓글에 번호로 투표해주세요!

1️⃣ 10월 되면 켠다
2️⃣ 손 시려야 켠다
3️⃣ 가족이 먼저 켠다
4️⃣ 온습도계 보고 켠다

🔗 4번 미니 온습도계 링크는 프로필에
👥 끝까지 보일러 안 켜는 친구 태그

#광고 #투표 #공감 #보일러 #난방 #겨울준비 #자취생""",
    "products": [prod(1, THERMO, N_THERMO, "B")],
})

write(DATE, "B2", [poll("수요일 아침 기온 뚝,<br>이불 언제 바꿈? 🛏️", "28일 아침 전국 -2~7℃ 예상",
                        [("아직 여름 이불", "덮고 웅크리면 됨"), ("이불 두 개 겹친다", "꺼내기 귀찮아서"),
                         ("전기장판부터 깐다", "바닥이 따뜻해야"), ("극세사 이불 꺼낸다", "오늘 밤 바로 교체")], QUILT)], {
    "title": "겨울 이불 교체 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 수요일 아침 기온 뚝, 이불 언제 바꿈? 🛏️
댓글에 번호로 투표해주세요!

1️⃣ 아직 여름 이불
2️⃣ 이불 두 개 겹친다
3️⃣ 전기장판부터 깐다
4️⃣ 극세사 이불 꺼낸다

🔗 4번 극세사 차렵이불 링크는 프로필에
👥 아직도 여름 이불 덮는 친구 태그

#광고 #투표 #공감 #첫추위 #겨울이불 #극세사이불 #자취생""",
    "products": [prod(1, QUILT, N_QUILT, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/26 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("보일러 켜기 전 체크", "난방 시작 전에", "생활템", "BEST3", [THERMO, CURT, SOCK]),
    c_prod(1, "0022", THERMO, "아이리버<br>디지털 미니 온습도계", ["온도·습도·시계를 한 화면에", "실내 18~20℃·40~60% 맞추기", "책상·거실 어디든 두기"],
           ["💰 1만원 미만", "🚀 로켓배송"]),
    c_prod(2, "0023", CURT, "코멧 홈<br>단열 암막 커튼", ["빛을 막는 단열 암막 커튼", "아일렛형 2장 세트", "밤엔 닫아서 열 손실 줄이기"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0024", SOCK, "이지하임<br>무압박 수면양말", ["발목 조이지 않는 수면양말", "남녀공용 4켤레 세트", "보일러 켜기 전 발부터"],
           ["💰 1만원 미만", "🚀 로켓배송"]),
    c_howto("0022~0024"),
], {
    "title": "난방 시작 생활템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

보일러 켜기 전 체크 🔥 난방 시작 전에! 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 아이리버 디지털 미니 온습도계 💛 품번 0022
온도·습도·시계를 한 화면에. 실내 18~20℃·습도 40~60% 맞추기.

2. 코멧 홈 단열 암막 커튼 💛 품번 0023
아일렛형 2장 세트. 밤엔 닫아서 열 손실 줄이기.

3. 이지하임 무압박 수면양말 💛 품번 0024
발목 안 조이는 수면양말, 남녀공용 4켤레.

※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #겨울준비 #온습도계 #암막커튼 #수면양말 #자취템""",
    "products": [prod(1, THERMO, N_THERMO, "C", "0022"), prod(2, CURT, N_CURT, "C", "0023"), prod(3, SOCK, N_SOCK, "C", "0024")],
})

write(DATE, "C2", [
    c_cover("수요일 아침 5~10도 뚝", "오늘 밤 바꾸는", "겨울 이불템", "BEST3", [QUILT, PACK, BLANK]),
    c_prod(1, "0025", QUILT, "코멧 홈<br>극세사 차렵이불", ["앞뒤 모두 극세사인 양면 이불", "솔리드 단색이라 무난", "겨울 이불 교체용"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0026", PACK, "조은리빙<br>이불 압축팩", ["밸브형 진공 압축팩", "여름 이불 부피 줄여 보관", "옷장·침대 밑 정리에"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0027", BLANK, "라이프란스<br>포근양 극세사 담요", ["포근한 극세사 담요", "소파·사무실 무릎담요로", "출퇴근 차 안에도"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0025~0027"),
], {
    "title": "겨울 이불템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

수요일 아침 5~10도 뚝 🥶 오늘 밤 바꾸는 겨울 이불템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 코멧 홈 극세사 차렵이불 💛 품번 0025
앞뒤 모두 극세사인 양면 이불. 겨울 이불 교체용.

2. 조은리빙 이불 압축팩 💛 품번 0026
밸브형 진공 압축팩. 여름 이불 부피 줄여 보관.

3. 라이프란스 포근양 극세사 담요 💛 품번 0027
소파·사무실 무릎담요로 쓰기 좋은 극세사 담요.

※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #첫추위 #겨울이불 #이불압축팩 #극세사담요 #자취템""",
    "products": [prod(1, QUILT, N_QUILT, "C", "0025"), prod(2, PACK, N_PACK, "C", "0026"), prod(3, BLANK, N_BLANK, "C", "0027")],
})
print("ok")
