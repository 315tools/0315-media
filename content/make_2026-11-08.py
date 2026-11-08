"""2026-11-08(일, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-08/{A,B,C,A2,B2,C2}
점심: 아침 영하권·중부 비/눈·도로 살얼음 / 퇴근길: 월요일 출근길 살얼음·강풍·대기 건조 → 정전기
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-08"
DL = "2026.11.08 (일)"
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







ICE, FOG, SCR = "9288511975", "9616489040", "8189924302"
BAND, KEY, SPR = "9067034374", "9770783565", "9438134263"
N_ICE = "이지유 2세대 도시형 원터치 경량 아이젠 10핀 (파우치 포함)"
N_FOG = "오브린 극세사 대형 김서림방지 안경닦이 10p"
N_SCR = "윤이네 털 장갑형 성에제거기 스크래퍼"
N_BAND = "오늘의생활 밴드형 정전기방지팔찌 1+1"
N_KEY = "메탈 정전기 제거 키링 (LED 표시등)"
N_SPR = "하시 정전기 방지 스프레이"

# ═════════ A · 점심 12:00 — 아침 영하권 + 중부 비·눈 + 살얼음 ═════════
SRC1 = "출처: 톱스타뉴스(11/8)·아시아투데이·아시아경제(11/7), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 일요일</div>
<h1>아침 영하권,<br><span class="hl">오후엔 비·눈</span></h1>
<p class="lead">수도권·강원 비, 강원 산지 눈<br>밤사이 도로 살얼음 주의</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(8일) 기온</h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>-1~7도</strong></div><div><small>전국 낮 최고</small><strong>7~15도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>2도</strong></div><div><small>서울 낮</small><strong>7도</strong></div></div>
<div class="box">낮과 밤 기온차 <b class="hl">10~15도</b><br>두꺼운 겉옷 챙기세요</div>""", SRC1, DL),
    a_slide(3, n, """<h2>비·눈 <span class="hl">시간표</span></h2>
<ul class="chk"><li>낮 12~3시 경기북부·강원북부</li><li>오후 3~6시 수도권·강원 전역</li><li>저녁 6~9시 충청 북부·경북 북부</li><li>밤 9~12시 대부분 그쳐요</li></ul>
<div class="box">수도권 <b class="hl">5㎜ 안팎</b> · 강원 산지 눈 <b class="hl">1㎝ 안팎</b></div>""", SRC1, DL),
    a_slide(4, n, """<h2>살얼음 길 <span class="hl">체크리스트</span></h2>
<ul class="chk"><li>경기북동부·강원 내륙·산지 <span class="hl">살얼음</span></li><li>운전은 감속, 안전거리 넉넉히</li><li>그늘진 길·다리 위 조심</li><li>주머니에서 손 빼고 걷기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>얼음 아침 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(ICE)}"><div>이지유 도시형 원터치 아이젠<span>10핀 · 파우치 포함</span></div></li>
<li><b>2</b><img src="{img(FOG)}"><div>오브린 김서림방지 안경닦이<span>극세사 대형 · 10p</span></div></li>
<li><b>3</b><img src="{img(SCR)}"><div>윤이네 장갑형 성에제거기<span>털장갑에 스크래퍼 결합</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/8 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "일요일 아침 영하권·중부 비",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 일요일 아침 영하권… 오후엔 수도권·강원 비, 강원 산지 눈 🌨️

· 8일 아침 최저 -1~7도, 낮 최고 7~15도 — 낮과 밤 기온차 10~15도
· 서울 아침 2도, 낮 7도
· 낮 경기북부·강원북부부터 비 → 오후 수도권·강원 전역 → 저녁 충청 북부·경북 북부, 밤 9~12시 대부분 그침
· 예상 강수량 수도권 5㎜ 안팎, 강원 산지 눈 1㎝ 안팎
· 경기북동부·강원 내륙·산지는 비나 눈이 얼어 도로 살얼음 생길 수 있어요

✔ 운전은 감속·안전거리, 걸을 땐 그늘진 길·다리 위 조심

🔗 얼음 아침 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 톱스타뉴스(11/8)·아시아투데이·아시아경제(11/7) — 기상청 예보

#광고 #생활뉴스 #날씨 #살얼음 #빙판길 #아이젠 #겨울준비""",
    "products": [prod(1, ICE, N_ICE, "A"), prod(2, FOG, N_FOG, "A"), prod(3, SCR, N_SCR, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 월요일 출근길 + 대기 건조 → 정전기 ═════════
SRC2 = "출처: 헤럴드경제·한국사회복지저널(11/8)·남도일보(11/7), 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 내일</div>
<h1>찌릿찌릿<br><span class="hl">정전기 시즌</span></h1>
<p class="lead">강원영동·경북북부동해안 건조특보<br>수도권 등 동쪽도 건조해요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>내일(9일 월) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>2~12도</strong></div><div><small>전국 낮 최고</small><strong>10~15도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>4도</strong></div><div><small>서울 낮</small><strong>12도</strong></div></div>
<div class="box">경기북동부·강원 내륙·산지<br>출근길 <b class="hl">도로 살얼음</b> 주의</div>""", SRC2, DL),
    a_slide(3, n, """<h2>비·<span class="hl">바람</span> 소식</h2>
<ul class="chk"><li>남부·제주 비, 저녁에 대부분 그침</li><li>제주 5~30㎜ · 광주·전남·경남권 5~10㎜</li><li>서해안·제주 <span class="hl">순간풍속 55㎞/h</span> 안팎</li><li>10일(화) 아침 -1~10도, 낮 10~16도</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>건조한 날 <span class="hl">정전기 줄이기</span></h2>
<ul class="chk"><li>실내 <span class="hl">습도</span> 챙기기</li><li>손·몸에 보습제 바르기</li><li>문고리 잡기 전 벽 먼저 짚기</li><li>산불·화재 예방에도 주의</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>찌릿 방지 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BAND)}"><div>오늘의생활 정전기방지팔찌<span>밴드형 · 1+1</span></div></li>
<li><b>2</b><img src="{img(KEY)}"><div>메탈 정전기 제거 키링<span>LED 표시등</span></div></li>
<li><b>3</b><img src="{img(SPR)}"><div>하시 정전기 방지 스프레이<span>옷에 뿌리는 타입</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/8 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "대기 건조·정전기 시즌",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 강원영동·경북북부동해안 건조특보… 수도권 등 동쪽도 건조, 정전기 조심 ⚡

· 건조특보가 내려진 강원영동·경북북부동해안은 대기가 매우 건조, 수도권 등 동쪽 지역도 건조 (8일 비로 특보 일부 해제 가능성)
· 9일(월) 아침 최저 2~12도, 낮 최고 10~15도 / 서울 아침 4도, 낮 12도
· 경기북동부·강원 내륙·산지는 출근길 도로 살얼음 주의
· 9일 남부·제주 비 — 제주 5~30㎜, 광주·전남·부산·울산·경남 5~10㎜, 저녁에 대부분 그침
· 9일 서해안·제주 순간풍속 55㎞/h 안팎 강풍
· 10일(화) 아침 -1~10도, 낮 10~16도

✔ 실내 습도·보습 챙기고, 산불·화재 예방에도 주의

🔗 찌릿 방지 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 헤럴드경제·한국사회복지저널(11/8)·남도일보(11/7) — 기상청 예보

#광고 #생활뉴스 #날씨 #건조 #정전기 #정전기방지 #겨울준비""",
    "products": [prod(1, BAND, N_BAND, "A"), prod(2, KEY, N_KEY, "A"), prod(3, SPR, N_SPR, "A")],
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






write(DATE, "B", [poll("영하권 아침,<br>빙판길 나의 걸음은? 🧊", "8일 아침 -1~7도, 강원 내륙 살얼음 (기상청 예보)",
                       [("펭귄 걸음", "종종종 보폭 줄이기"), ("손 빼고 걷기", "주머니 손은 위험해"),
                        ("집에 있기", "오늘은 안 나가요"), ("아이젠 장착", "운동화에 착 끼우기")], ICE)], {
    "title": "빙판길 걸음 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 영하권 아침, 빙판길 나의 걸음은? 🧊
댓글에 번호로 투표해주세요!

1️⃣ 펭귄 걸음
2️⃣ 손 빼고 걷기
3️⃣ 집에 있기
4️⃣ 아이젠 장착

※ 8일 아침 최저 -1~7도, 경기북동부·강원 내륙·산지 도로 살얼음 주의 (기상청 예보, 톱스타뉴스 11/8·아시아경제 11/7)

🔗 4번 이지유 도시형 원터치 아이젠 링크는 프로필에
👥 빙판길에서 꼭 한 번 미끄러지는 친구 태그

#광고 #투표 #공감 #빙판길 #살얼음 #아이젠""",
    "products": [prod(1, ICE, N_ICE, "B")],
})

write(DATE, "B2", [poll("문고리 잡기 무서운 계절…<br>정전기 대처법은? ⚡", "강원영동 건조특보, 수도권도 건조 (기상청 예보)",
                        [("소매로 잡기", "옷으로 감싸서 쓱"), ("벽 먼저 터치", "찌릿 미리 빼기"),
                         ("그냥 맞기", "따끔… 이번에도 졌다"), ("정전기 팔찌", "손목에 차고 다니기")], BAND)], {
    "title": "정전기 대처법 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 문고리 잡기 무서운 계절… 정전기 대처법은? ⚡
댓글에 번호로 투표해주세요!

1️⃣ 소매로 잡기
2️⃣ 벽 먼저 터치
3️⃣ 그냥 맞기
4️⃣ 정전기 팔찌

※ 강원영동·경북북부동해안 건조특보, 수도권 등 동쪽 지역도 건조 (기상청 예보, 한국사회복지저널 11/8·남도일보 11/7)

🔗 4번 오늘의생활 정전기방지팔찌 링크는 프로필에
👥 차 문 열 때마다 비명 지르는 친구 태그

#광고 #투표 #공감 #정전기 #건조 #겨울""",
    "products": [prod(1, BAND, N_BAND, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/8 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("아침 영하권 · 도로 살얼음", "얼음 아침", "특이템", "BEST3", [ICE, FOG, SCR]),
    c_prod(1, "0100", ICE, "이지유<br>도시형 원터치 아이젠", ["운동화에 끼우는 10핀", "원터치 착용", "파우치에 넣어 휴대"],
           ["💰 8천원대", "🚀 로켓배송"]),
    c_prod(2, "0101", FOG, "오브린<br>김서림방지 안경닦이", ["김서림 방지 극세사 천", "대형 사이즈", "10장 구성"],
           ["💰 4천원대", "🚀 로켓배송"]),
    c_prod(3, "0102", SCR, "윤이네<br>장갑형 성에제거기", ["털장갑 + 스크래퍼", "손 시리지 않게", "차 유리 성에 긁기"],
           ["💰 5천원대", "🚚 무료배송"]),
    c_howto("0100~0102"),
], {
    "title": "얼음 아침 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

아침 영하권에 도로 살얼음 🧊 얼음 아침 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 이지유 2세대 도시형 원터치 경량 아이젠 10핀 💛 품번 0100
운동화에 끼워 쓰는 도시형 아이젠, 파우치 포함.

2. 오브린 극세사 대형 김서림방지 안경닦이 10p 💛 품번 0101
추운 밖에서 실내로 들어올 때 안경 김서림 대비.

3. 윤이네 털 장갑형 성에제거기 스크래퍼 💛 품번 0102
털장갑에 스크래퍼가 붙어 있어 손 시리지 않게 성에 제거.

※ 날씨: 기상청 예보(톱스타뉴스 11/8, 아시아경제 11/7 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #아이젠 #김서림방지 #성에제거기 #겨울준비""",
    "products": [prod(1, ICE, N_ICE, "C", "0100"), prod(2, FOG, N_FOG, "C", "0101"), prod(3, SCR, N_SCR, "C", "0102")],
})

write(DATE, "C2", [
    c_cover("건조특보 · 대기 건조", "찌릿 방지", "특이템", "BEST3", [BAND, KEY, SPR]),
    c_prod(1, "0103", BAND, "오늘의생활<br>정전기방지팔찌", ["손목에 차는 밴드형", "1+1 구성", "정전기 계절 대비"],
           ["💰 6천원대", "🚀 로켓배송"]),
    c_prod(2, "0104", KEY, "메탈<br>정전기 제거 키링", ["열쇠고리형", "LED 표시등", "차 문·현관문 전에"],
           ["💰 8천원대", "🚀 로켓배송"]),
    c_prod(3, "0105", SPR, "하시<br>정전기 방지 스프레이", ["옷에 뿌리는 타입", "니트·코트 정전기 대비", "외출 전 칙칙"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_howto("0103~0105"),
], {
    "title": "찌릿 방지 특이템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

건조특보에 정전기 계절 ⚡ 찌릿 방지 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 오늘의생활 밴드형 정전기방지팔찌 1+1 💛 품번 0103
손목에 차고 다니는 밴드형 정전기 방지 팔찌.

2. 메탈 정전기 제거 키링 (LED 표시등) 💛 품번 0104
열쇠고리에 달아 두는 정전기 제거 키링.

3. 하시 정전기 방지 스프레이 💛 품번 0105
니트·코트 등 옷에 뿌리는 정전기 방지 스프레이.

✔ 실내 습도·보습도 함께 챙기기

※ 날씨: 기상청 예보(한국사회복지저널 11/8, 남도일보 11/7 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #정전기 #정전기방지 #건조 #겨울준비""",
    "products": [prod(1, BAND, N_BAND, "C", "0103"), prod(2, KEY, N_KEY, "C", "0104"), prod(3, SPR, N_SPR, "C", "0105")],
})
print("ok")
