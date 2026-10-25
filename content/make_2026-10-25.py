"""2026-10-25(일, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-10-25/{A,B,C,A2,B2,C2}
점심: 독감 의심환자 작년 2배·개인위생 / 퇴근길: 일교차 15도→수요일 아침 서울 2도
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402

DATE = "2026-10-25"
DL = "2026.10.25 (일)"
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




SOAP, HUMI, BRUSH = "6673786978", "8399098479", "9724692652"
HAND, VEST, NECK = "9189208667", "6362095588", "8485153887"

# ═════════ A · 점심 12:00 — 독감 의심환자 작년 2배 ═════════
SRC1 = "출처: 질병관리청 발표(10/24) 인용 — 싱글리스트·글로벌경제신문(10/24)"
n = 6
a1 = [
    a_slide(1, n, """<div class="tag">건강 · 생활</div>
<h1>독감 의심환자<br>작년의<br><span class="hl">2배 넘어</span></h1>
<p class="lead">질병관리청 "더 추워지기 전에<br>독감 백신 맞으세요"</p>""", SRC1, DL),
    a_slide(2, n, """<h2>외래 1천 명당 독감 의심환자</h2>
<div class="fig"><div><small>올해 42주차</small><strong>17.7명</strong></div><div><small>작년 같은 주</small><strong>7.9명</strong></div></div>
<div class="box">직전 주 21.6명보다는 줄었지만<br>작년과 비교하면 <b class="hl">여전히 높은 수준</b></div>
<p class="lead" style="font-size:34px">42주차 = 10월 11~17일, 의원급 외래 기준</p>""", SRC1, DL),
    a_slide(3, n, """<h2>독감 백신 접종률</h2>
<div class="fig"><div><small>65세 이상</small><strong>58.7%</strong></div><div><small>작년 같은 기간</small><strong>60.8%</strong></div></div>
<div class="fig"><div><small>6개월~14세</small><strong>48.6%</strong></div><div><small>작년 같은 기간</small><strong>36.0%</strong></div></div>
<p class="lead" style="font-size:34px">10월 22일 18시 기준</p>""", SRC1, DL),
    a_slide(4, n, """<h2>접종 전 알아둘 것</h2>
<ul class="chk"><li>항체가 생기기까지 <span class="hl">약 2주</span></li><li>작년에 맞았어도 올해 새로 접종</li><li>무료 대상: 65세 이상·임신부·<br>생후 6개월~14세</li><li>주소지 상관없이 위탁 의료기관·보건소</li></ul>""", SRC1, DL),
    a_slide(5, n, """<h2>생활 속 개인위생</h2>
<ul class="chk"><li>밖에서 돌아오면 비누로 손 씻기</li><li>기침은 옷소매로 가리기</li><li>하루 몇 번 창문 열고 환기</li><li>열·기침 심하면 병원 진료</li></ul>
<p class="lead" style="font-size:34px">질병관리청은 접종과 함께 개인위생 수칙을 당부했습니다.</p>""", "", DL),
    a_slide(6, n, f"""<h2>손 씻기 돕는 <span class="hl">위생 특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SOAP)}"><div>르메이어 자동 거품 디스펜서<span>손 대면 거품이 나와요</span></div></li>
<li><b>2</b><img src="{img(HUMI)}"><div>오아 듀얼미스트 무선 가습기<span>책상 위 미니 가습기</span></div></li>
<li><b>3</b><img src="{img(BRUSH)}"><div>미가 벽걸이 칫솔 살균기<span>1인용 · 무타공 부착</span></div></li></ol>
<p class="lead" style="font-size:34px">🔗 프로필 링크 → 10/25 점심 ①~③<br>※ 생활용품이에요. 예방은 백신 접종이 먼저!</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "독감 의심환자 작년 2배",
    "caption": f"""{DISC}

[생활뉴스] 독감 의심환자 작년의 2배 넘어…"추워지기 전 백신 맞으세요"

· 42주차(10/11~17) 외래 1천 명당 독감 의심환자 17.7명, 작년 같은 주 7.9명
· 직전 주(21.6명)보다는 줄었지만 여전히 높은 수준
· 65세 이상 접종률 58.7%(작년 60.8%), 6개월~14세 48.6%(작년 36.0%)
· 항체 형성까지 약 2주, 작년에 맞았어도 올해 새로 접종

🔗 손 씻기 돕는 위생템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 질병관리청 발표(10/24) 인용 보도 — 싱글리스트, 글로벌경제신문

#광고 #생활뉴스 #독감 #독감예방접종 #환절기 #손씻기 #개인위생""",
    "products": [prod(1, SOAP, "르메이어 비접촉 자동 센서 거품 디스펜서", "A"), prod(2, HUMI, "오아 듀얼미스트 미니 무선 가습기", "A"),
                 prod(3, BRUSH, "MIGA 1인용 무선 UV-C LED 칫솔 살균기", "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 일교차 15도 → 수요일 아침 2도 ═════════
SRC2 = "출처: 기상청 예보 인용 보도 — 더페어(10/25), 더리포트(10/24)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 생활</div>
<h1>오늘은 낮 24도,<br>수요일 아침은<br><span class="hl">서울 2도</span></h1>
<p class="lead">일교차 큰 주말 뒤<br>이번 주 출근길엔 첫 추위가 옵니다.</p>""", SRC2, DL),
    a_slide(2, n, """<h2>오늘(25일) 수도권</h2>
<div class="fig"><div><small>서울 아침</small><strong>12℃</strong></div><div><small>서울 낮</small><strong>24℃</strong></div></div>
<div class="box">낮과 밤 기온 차 <b class="hl">15도 안팎</b><br>경기 북부 일부는 아침 10도 아래</div>""", SRC2, DL),
    a_slide(3, n, """<h2>28일(수) 예상 기온</h2>
<div class="fig"><div><small>서울</small><strong>2~13℃</strong></div><div><small>대전</small><strong>1~13℃</strong></div></div>
<div class="fig"><div><small>대구</small><strong>1~14℃</strong></div><div><small>춘천</small><strong>-1~14℃</strong></div></div>
<p class="lead" style="font-size:38px">평년보다 3도가량 낮을 전망입니다.</p>""", SRC2, DL),
    a_slide(4, n, """<h2>첫 추위 출근길 체크</h2>
<ul class="chk"><li>얇은 옷 여러 겹 + 겉옷 하나</li><li>목·손부터 따뜻하게</li><li>충전식 방한템은 전날 밤 충전</li><li>발열 제품은 맨살에 오래 대지 않기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>출근길 <span class="hl">충전식 방한템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(HAND)}"><div>알로코리아 펭귄 손난로<span>보조배터리 겸용 5000mAh</span></div></li>
<li><b>2</b><img src="{img(VEST)}"><div>에쉬울프 USB 발열조끼<span>겉옷 안에 입는 조끼</span></div></li>
<li><b>3</b><img src="{img(NECK)}"><div>투데이리빙 USB 발열 목도리<span>3단 온도 조절</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/25 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "일교차 15도→수요일 2도",
    "caption": f"""{DISC}

[생활뉴스] 오늘은 낮 24도, 수요일 아침은 서울 2도

· 25일 서울 아침 12℃ / 낮 24℃, 수도권 일교차 15도 안팎
· 28일(수) 서울 2~13℃, 대전 1~13℃, 대구 1~14℃, 춘천 -1~14℃
· 평년보다 3도가량 낮을 전망

🔗 출근길 충전식 방한템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 기상청 예보 인용 보도(더페어 10/25, 더리포트 10/24)

#광고 #생활뉴스 #날씨 #일교차 #첫추위 #출근길 #손난로 #발열조끼""",
    "products": [prod(1, HAND, "알로코리아 펭귄 충전식 손난로 보조배터리 5000mAh", "A"), prod(2, VEST, "에쉬울프 USB 발열조끼 DR013", "A"),
                 prod(3, NECK, "투데이리빙 USB 발열 패딩 목도리", "A")],
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


write(DATE, "B", [poll("환절기 목 칼칼할 때<br>나는 어떻게 함? 😷", "독감 의심환자 작년의 2배 넘어 (질병청)",
                       [("바로 병원 간다", "참으면 더 길어져"), ("따뜻한 차 마신다", "생강차·유자차 파"),
                        ("일단 일찍 잔다", "잠이 보약"), ("가습기 틀고 잔다", "건조한 방이 문제")], HUMI)], {
    "title": "목 칼칼할 때 투표",
    "caption": f"""{DISC}

📊 환절기 목 칼칼할 때 나는 어떻게 함? 😷
댓글에 번호로 투표해주세요!

1️⃣ 바로 병원 간다
2️⃣ 따뜻한 차 마신다
3️⃣ 일단 일찍 잔다
4️⃣ 가습기 틀고 잔다

🔗 4번 미니 가습기 링크는 프로필에
👥 맨날 감기 달고 사는 친구 태그

#광고 #투표 #공감 #환절기 #감기 #가습기 #자취생""",
    "products": [prod(1, HUMI, "오아 듀얼미스트 미니 무선 가습기", "B")],
})

write(DATE, "B2", [poll("수요일 아침 2도,<br>출근룩 뭐 입음? 🥶", "서울 10/28(수) 아침 2℃ 예상",
                        [("아직 트렌치코트", "멋은 포기 못 해"), ("롱패딩 꺼낸다", "이미 겨울 모드"),
                         ("내복부터 챙긴다", "안에서 버틴다"), ("발열조끼 입는다", "충전해서 입는 조끼")], VEST)], {
    "title": "출근룩 투표",
    "caption": f"""{DISC}

📊 수요일 아침 2도, 출근룩 뭐 입음? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 아직 트렌치코트
2️⃣ 롱패딩 꺼낸다
3️⃣ 내복부터 챙긴다
4️⃣ 발열조끼 입는다

🔗 4번 발열조끼 링크는 프로필에
👥 추위 많이 타는 친구 태그

#광고 #투표 #공감 #첫추위 #출근룩 #발열조끼 #직장인""",
    "products": [prod(1, VEST, "에쉬울프 USB 발열조끼 DR013", "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/25 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("독감 의심환자 작년 2배", "환절기엔 손부터", "위생 특이템", "BEST3", [SOAP, HUMI, BRUSH]),
    c_prod(1, "0016", SOAP, "르메이어 비접촉<br>자동 거품 디스펜서", ["손을 대면 센서로 거품이 나와요", "펌프를 누르지 않아도 됨", "욕실·주방 세면대에"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(2, "0017", HUMI, "오아 듀얼미스트<br>미니 무선 가습기", ["분사구 2개의 탁상용 초음파 가습기", "무선이라 책상·침대 옆 어디든", "건조한 사무실·원룸에"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0018", BRUSH, "미가 1인용<br>벽걸이 칫솔 살균기", ["UV-C LED 칫솔 살균기", "구멍 안 뚫는 무타공 부착", "무선 충전식이라 깔끔"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0016~0018"),
], {
    "title": "환절기 위생 특이템 BEST3",
    "caption": f"""{DISC}

독감 의심환자 작년 2배 😷 환절기 손 씻기부터! 위생 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 르메이어 비접촉 자동 거품 디스펜서 💛 품번 0016
손을 대면 센서로 거품이 나와요. 욕실·주방 세면대에.

2. 오아 듀얼미스트 미니 무선 가습기 💛 품번 0017
분사구 2개 탁상용 가습기. 건조한 사무실·원룸에.

3. 미가 1인용 벽걸이 칫솔 살균기 💛 품번 0018
UV-C LED 칫솔 살균기. 구멍 안 뚫고 붙이는 무타공.

※ {NOTE}
※ 생활용품이에요. 독감 예방은 백신 접종이 먼저!

#광고 #쿠팡추천템 #특이템 #환절기 #자동디스펜서 #미니가습기 #칫솔살균기 #자취템""",
    "products": [prod(1, SOAP, "르메이어 비접촉 자동 센서 거품 디스펜서", "C", "0016"), prod(2, HUMI, "오아 듀얼미스트 미니 무선 가습기", "C", "0017"),
                 prod(3, BRUSH, "MIGA 1인용 무선 UV-C LED 칫솔 살균기", "C", "0018")],
})

write(DATE, "C2", [
    c_cover("수요일 아침 2도", "출근길 덜 춥게", "충전식 방한템", "BEST3", [HAND, VEST, NECK]),
    c_prod(1, "0019", HAND, "알로코리아<br>펭귄 손난로", ["펭귄 모양 충전식 손난로", "보조배터리 겸용 5000mAh", "주머니 속 핫팩 대신"],
           ["💰 2만원대", "🔋 5000mAh", "🚀 로켓배송"]),
    c_prod(2, "0020", VEST, "에쉬울프<br>USB 발열조끼", ["USB로 데우는 온열 조끼", "겉옷 안에 입기", "출근길·야외 활동에"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0021", NECK, "투데이리빙<br>USB 발열 목도리", ["열선이 들어간 패딩 목도리", "3단 온도 조절 버튼", "목부터 따뜻하게"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0019~0021"),
], {
    "title": "충전식 방한템 BEST3",
    "caption": f"""{DISC}

수요일 아침 2도 🥶 출근길 덜 춥게! 충전식 방한템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 알로코리아 펭귄 손난로 💛 품번 0019
펭귄 모양 충전식 손난로, 보조배터리 겸용 5000mAh.

2. 에쉬울프 USB 발열조끼 💛 품번 0020
USB로 데우는 온열 조끼. 겉옷 안에 입기 좋아요.

3. 투데이리빙 USB 발열 목도리 💛 품번 0021
열선 패딩 목도리, 3단 온도 조절.

※ {NOTE}
※ 발열 제품은 맨살에 오래 대지 마세요(저온화상 주의)

#광고 #쿠팡추천템 #특이템 #첫추위 #손난로 #발열조끼 #발열목도리 #출근길""",
    "products": [prod(1, HAND, "알로코리아 펭귄 충전식 손난로 보조배터리 5000mAh", "C", "0019"), prod(2, VEST, "에쉬울프 USB 발열조끼 DR013", "C", "0020"),
                 prod(3, NECK, "투데이리빙 USB 발열 패딩 목도리", "C", "0021")],
})
print("ok")
