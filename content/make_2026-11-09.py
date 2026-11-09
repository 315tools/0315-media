"""2026-11-09(월, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-09/{A,B,C,A2,B2,C2}
점심: 쌀쌀한 월요일 + 겨울옷 꺼내기(패딩 볼륨·보풀) / 퇴근길: 내일 아침 영하권·일교차 → 난방 시작, 결로·곰팡이
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-09"
DL = "2026.11.09 (월)"
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




BALL, LINT, DOWN = "7871746353", "4947594003", "2322706995"
FILM, SQZ, MOLD = "9785790149", "4323766671", "4590711585"
N_BALL = "코멧 홈 건조기 양모 울드라이어볼 6p (파우치 포함)"
N_LINT = "필립스 보풀제거기"
N_DOWN = "쉬슬러 구스다운워시 전용 액상세제 650ml"
N_FILM = "아이푸룸 국내생산 창문 단열필름 (결로방지)"
N_SQZ = "욕실 거울·유리창 물기제거 청소 스퀴지"
N_MOLD = "청정세상 붓으로 바르는 곰팡이 제거제 (붓 포함)"

# ═════════ A · 점심 12:00 — 쌀쌀한 월요일 + 겨울옷 꺼내기 ═════════
SRC1 = "출처: 아시아경제·위키트리·이투데이(11/9), 위키트리(11/5), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 월요일</div>
<h1>겨울옷 꺼내는 날,<br><span class="hl">패딩 살리기</span></h1>
<p class="lead">쌀쌀한 월요일, 강원 내륙 영하권<br>납작해진 패딩 되살리는 법</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(9일) 기온</h2>
<div class="fig"><div><small>서울 아침 최저</small><strong>4도</strong></div><div><small>서울 낮 최고</small><strong>12도</strong></div></div>
<div class="fig"><div><small>춘천 아침</small><strong>3~4도</strong></div><div><small>전국 낮 최고</small><strong>10~14도</strong></div></div>
<div class="box">강원 산지(1000m 이상) 눈 <b class="hl">1~3㎝</b><br>남부·제주 곳곳 비</div>""", SRC1, DL),
    a_slide(3, n, """<h2>꺼낸 패딩 <span class="hl">볼륨 살리기</span></h2>
<ul class="chk"><li>그늘에 걸어 반나절~하루 환기</li><li>거꾸로 들고 위아래로 세게 털기</li><li>손바닥·옷솔로 전체 두드리기</li><li>삐져나온 털은 <span class="hl">안쪽으로</span> 당겨 넣기</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>집에서 <span class="hl">패딩 세탁</span>할 땐</h2>
<ul class="chk"><li>케어 라벨 먼저 확인</li><li>세탁망 + <span class="hl">30도 정도</span> 미온수</li><li>중성세제 조금, 섬유유연제 X</li><li>그늘 건조 → 건조기는 저온 + 건조기 볼</li><li>니트 보풀은 뜯지 말고 제거기로</li></ul>""", "출처: 위키트리(11/5)", DL),
    a_slide(5, n, f"""<h2>겨울옷 <span class="hl">관리템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BALL)}"><div>코멧 건조기 양모볼<span>6p · 파우치 포함</span></div></li>
<li><b>2</b><img src="{img(LINT)}"><div>필립스 보풀제거기<span>니트·코트 보풀 정리</span></div></li>
<li><b>3</b><img src="{img(DOWN)}"><div>쉬슬러 구스다운워시<span>다운 전용 액상세제 650ml</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/9 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "쌀쌀한 월요일·겨울옷 관리",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 쌀쌀한 월요일, 강원 내륙 영하권… 겨울옷 꺼냈다면 패딩부터 살려요 🧥

· 9일 서울 아침 4도, 낮 12도 / 전국 낮 최고 10~14도
· 강원 내륙·산지 아침 영하권, 해발 1000m 이상 강원 산지 눈 1~3㎝
· 남부·제주 곳곳 비(제주 5~30㎜), 미세먼지는 전국 '좋음'~'보통'

✔ 꺼낸 패딩은 그늘에 반나절~하루 걸어 환기
✔ 거꾸로 들고 세게 털고, 손바닥·옷솔로 두드려 볼륨 살리기
✔ 집 세탁은 케어 라벨 확인 → 세탁망, 30도 정도 미온수, 중성세제 조금, 섬유유연제는 빼기
✔ 그늘에서 눕혀 말리고, 건조기는 저온 + 건조기 볼
✔ 니트 보풀은 손으로 뜯지 말고 보풀 제거기로

🔗 겨울옷 관리템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 아시아경제·위키트리·이투데이(11/9) — 기상청 예보 / 위키트리(11/5) 패딩 관리법

#광고 #생활뉴스 #날씨 #겨울옷 #패딩세탁 #보풀제거 #생활꿀팁""",
    "products": [prod(1, BALL, N_BALL, "A"), prod(2, LINT, N_LINT, "A"), prod(3, DOWN, N_DOWN, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 내일 아침 영하권·큰 일교차 → 결로·곰팡이 ═════════
SRC2 = "출처: 위키트리·이투데이(11/9), 레이디경향(11/1), 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 내일</div>
<h1>창틀이 새까매진다면<br><span class="hl">결로 시즌</span></h1>
<p class="lead">내일 아침 중부 내륙 영하권<br>아침·낮 기온차 10~15도</p>""", SRC2, DL),
    a_slide(2, n, """<h2>내일(10일 화) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침 최저</small><strong>-3~10도</strong></div><div><small>전국 낮 최고</small><strong>12~18도</strong></div></div>
<div class="fig"><div><small>11일(수) 아침</small><strong>-2~7도</strong></div><div><small>11일(수) 낮</small><strong>14~19도</strong></div></div>
<div class="box">중부 내륙·전북 동부 <b class="hl">아침 영하권</b><br>대체로 맑음</div>""", SRC2, DL),
    a_slide(3, n, """<h2>결로는 <span class="hl">왜 생길까?</span></h2>
<ul class="chk"><li>따뜻하고 습한 실내 공기가</li><li>차가운 창문에 닿으면 물방울로</li><li>실내외 <span class="hl">온도 차</span> 큰 겨울에 심해져요</li><li>그대로 두면 창틀·실리콘 곰팡이</li></ul>""", "출처: 레이디경향(11/1)", DL),
    a_slide(4, n, """<h2>결로·곰팡이 <span class="hl">줄이기</span></h2>
<ul class="chk"><li>겨울에도 틈틈이 <span class="hl">환기</span></li><li>실내 빨래 건조·가습기 과다 점검</li><li>아침마다 창 물기 닦고 창틀까지 말리기</li><li>단열 필름·커튼, 가끔은 열어 두기</li><li>곰팡이는 창틀·실리콘용 제품으로</li></ul>""", "출처: 레이디경향(11/1)", DL),
    a_slide(5, n, f"""<h2>결로 대비 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(FILM)}"><div>아이푸룸 창문 단열필름<span>국내생산 · 결로방지</span></div></li>
<li><b>2</b><img src="{img(SQZ)}"><div>유리창 물기제거 스퀴지<span>아침 창 물기 쓱</span></div></li>
<li><b>3</b><img src="{img(MOLD)}"><div>청정세상 바르는 곰팡이 제거제<span>붓 포함</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/9 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "내일 아침 영하권·결로 시즌",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 내일 아침 중부 내륙 영하권, 아침·낮 기온차 10~15도… 창문 결로 시즌 💧

· 10일(화) 아침 최저 -3~10도, 낮 최고 12~18도 — 중부 내륙·전북 동부 아침 영하권
· 아침과 낮 기온차 10~15도 안팎
· 11일(수) 아침 -2~7도, 낮 14~19도

결로는 따뜻하고 습한 실내 공기가 차가운 창문에 닿아 생겨요. 실내외 온도 차가 큰 겨울에 심해져요.
✔ 겨울에도 틈틈이 환기, 실내 빨래 건조·가습기 과다 사용 점검
✔ 아침마다 창 물기를 닦고 창틀 아래 고인 물까지 말리기
✔ 단열 필름·두꺼운 커튼은 쓰되 가끔 열어 공기 순환
✔ 곰팡이는 창틀·실리콘에 쓸 수 있는 제품으로, 표시된 사용법대로 (염소계 표백제를 다른 세제와 섞지 않기)

🔗 결로 대비 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 위키트리·이투데이(11/9) — 기상청 예보 / 레이디경향(11/1) 결로·곰팡이 관리

#광고 #생활뉴스 #날씨 #결로 #곰팡이 #창문단열 #겨울준비""",
    "products": [prod(1, FILM, N_FILM, "A"), prod(2, SQZ, N_SQZ, "A"), prod(3, MOLD, N_MOLD, "A")],
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


write(DATE, "B", [poll("꺼낸 패딩이 납작할 때<br>나의 선택은? 🧥", "9일 강원 내륙 아침 영하권, 겨울옷 꺼낼 때 (기상청 예보)",
                       [("마구 털기", "거꾸로 들고 탕탕"), ("그냥 입기", "납작해도 따뜻해"),
                        ("세탁소 맡기기", "전문가에게 부탁"), ("건조기 볼과 함께", "저온으로 한 번 더")], BALL)], {
    "title": "납작 패딩 대처 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 꺼낸 패딩이 납작할 때 나의 선택은? 🧥
댓글에 번호로 투표해주세요!

1️⃣ 마구 털기
2️⃣ 그냥 입기
3️⃣ 세탁소 맡기기
4️⃣ 건조기 볼과 함께

※ 9일 강원 내륙·산지 아침 영하권 (기상청 예보, 아시아경제·위키트리 11/9)
※ 패딩은 그늘 건조 후 건조기를 쓴다면 저온 + 건조기 볼 (위키트리 11/5)

🔗 4번 코멧 건조기 양모볼 링크는 프로필에
👥 옷장에서 패딩 꺼내자마자 입고 나가는 친구 태그

#광고 #투표 #공감 #패딩 #겨울옷 #건조기볼""",
    "products": [prod(1, BALL, N_BALL, "B")],
})

write(DATE, "B2", [poll("아침마다 창문에<br>물방울 맺히면? 💧", "10일 아침 중부 내륙 영하권, 기온차 10~15도 (기상청 예보)",
                        [("손가락 낙서", "일단 그림부터"), ("휴지로 쓱", "휴지 한 통 순삭"),
                         ("못 본 척", "곰팡이야 미안"), ("스퀴지로 쓱", "물기 한 번에 싹")], SQZ)], {
    "title": "창문 결로 대처 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 아침마다 창문에 물방울 맺히면? 💧
댓글에 번호로 투표해주세요!

1️⃣ 손가락 낙서
2️⃣ 휴지로 쓱
3️⃣ 못 본 척
4️⃣ 스퀴지로 쓱

※ 10일(화) 아침 -3~10도, 중부 내륙 영하권, 아침·낮 기온차 10~15도 (기상청 예보, 위키트리 11/9)
※ 결로는 아침마다 닦고 창틀 아래 물기까지 말리기 (레이디경향 11/1)

🔗 4번 유리창 물기제거 스퀴지 링크는 프로필에
👥 창문에 하트 그리는 친구 태그

#광고 #투표 #공감 #결로 #창문 #겨울""",
    "products": [prod(1, SQZ, N_SQZ, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/9 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("쌀쌀한 월요일 · 겨울옷 꺼내는 날", "겨울옷", "관리템", "BEST3", [BALL, LINT, DOWN]),
    c_prod(1, "0106", BALL, "코멧<br>건조기 양모볼", ["울 드라이어볼 6개", "파우치 포함", "패딩 건조 때 함께"],
           ["💰 6천원대", "🚀 로켓배송"]),
    c_prod(2, "0107", LINT, "필립스<br>보풀제거기", ["니트·코트 보풀 정리", "손으로 뜯지 말고", "옷 오래 입기"],
           ["💰 1만2천원대", "🚀 로켓배송"]),
    c_prod(3, "0108", DOWN, "쉬슬러<br>구스다운워시", ["다운 전용 액상세제", "650ml", "집에서 패딩 세탁"],
           ["💰 7천원대", "🚀 로켓배송"]),
    c_howto("0106~0108"),
], {
    "title": "겨울옷 관리템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

쌀쌀한 월요일, 겨울옷 꺼내는 날 🧥 겨울옷 관리템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 코멧 홈 건조기 양모 울드라이어볼 6p (파우치 포함) 💛 품번 0106
패딩을 건조기로 말릴 때 함께 넣는 양모볼.

2. 필립스 보풀제거기 💛 품번 0107
니트·코트 보풀은 손으로 뜯지 말고 보풀 제거기로.

3. 쉬슬러 구스다운워시 전용 액상세제 650ml 💛 품번 0108
집에서 패딩 빨 때 쓰는 다운 전용 세제.

✔ 세탁 전 케어 라벨 확인, 섬유유연제는 빼기

※ 패딩 관리법: 위키트리(11/5) / 날씨: 기상청 예보(아시아경제 11/9)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #패딩세탁 #보풀제거기 #건조기볼 #겨울옷""",
    "products": [prod(1, BALL, N_BALL, "C", "0106"), prod(2, LINT, N_LINT, "C", "0107"), prod(3, DOWN, N_DOWN, "C", "0108")],
})

write(DATE, "C2", [
    c_cover("내일 아침 영하권 · 기온차 10~15도", "결로 대비", "생활템", "BEST3", [FILM, SQZ, MOLD]),
    c_prod(1, "0109", FILM, "아이푸룸<br>창문 단열필름", ["국내생산", "창문에 붙이는 단열필름", "결로·외풍 대비"],
           ["💰 4만5천원대", "🚀 로켓배송"]),
    c_prod(2, "0110", SQZ, "유리창<br>물기제거 스퀴지", ["거울·유리창 물기 제거", "아침 창 결로 쓱", "욕실에도"],
           ["💰 7천원대", "🚚 무료배송"]),
    c_prod(3, "0111", MOLD, "청정세상<br>바르는 곰팡이 제거제", ["붓 포함", "창틀·실리콘 틈새에", "사용법 지켜 쓰기"],
           ["💰 1만4천원대", "🚀 로켓배송"]),
    c_howto("0109~0111"),
], {
    "title": "결로 대비 생활템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

내일 아침 영하권, 창문 결로 시즌 💧 결로 대비 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 아이푸룸 국내생산 창문 단열필름 (결로방지) 💛 품번 0109
창문에 붙여 쓰는 단열필름.

2. 욕실 거울·유리창 물기제거 청소 스퀴지 💛 품번 0110
아침마다 창에 맺힌 물기를 닦아 내는 스퀴지.

3. 청정세상 붓으로 바르는 곰팡이 제거제 (붓 포함) 💛 품번 0111
창틀·실리콘 틈새 곰팡이에 바르는 타입. 표시된 사용법대로 쓰고 다른 세제와 섞지 않기.

✔ 겨울에도 틈틈이 환기, 창틀 아래 고인 물까지 말리기

※ 결로 관리: 레이디경향(11/1) / 날씨: 기상청 예보(위키트리 11/9)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #결로 #곰팡이제거 #창문단열 #겨울준비""",
    "products": [prod(1, FILM, N_FILM, "C", "0109"), prod(2, SQZ, N_SQZ, "C", "0110"), prod(3, MOLD, N_MOLD, "C", "0111")],
})
print("ok")
