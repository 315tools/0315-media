"""2026-11-02(월, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-02/{A,B,C,A2,B2,C2}
점심: 화요일 아침 기온 5~10도 뚝·외풍 차단템 / 퇴근길: 난방비 절약법·실내 보온템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-02"
DL = "2026.11.02 (월)"
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





SEAL, POP, PACK = "9287063502", "34357682", "9243340974"
TENT, SLIP, HUMI = "2229091647", "9775575350", "198159585"
N_SEAL, N_POP, N_PACK = "아텍스 실리콘 문풍지 테이프 45mm x 5m", "뽁순이 3중 뽁뽁이 단열에어캡", "마지온 틈새차단 현관문 창문 고무 패킹 6M"
N_TENT, N_SLIP, N_HUMI = "코멧 원터치 난방텐트 + 보관가방", "리빙도감 남녀공용 방한 겨울 털 슬리퍼", "대중산업 방방가습기 600 자연증발식 무전원 4세트"

# ═════════ A · 점심 12:00 — 내일 아침 기온 뚝 ═════════
SRC1 = "출처: 경향신문(11/1)·톱스타뉴스(11/2), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 내일</div>
<h1>내일(3일) 아침<br><span class="hl">기온 5~10도 뚝</span><br>서리·얼음</h1>
<p class="lead">아침 0~9도 · 낮 15~19도<br>일교차 15도 안팎</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘 vs 내일 기온</h2>
<div class="fig"><div><small>오늘(2일) 아침</small><strong>6~13도</strong></div><div><small>오늘 낮</small><strong>14~20도</strong></div></div>
<div class="fig"><div><small>내일(3일) 아침</small><strong>0~9도</strong></div><div><small>내일 낮</small><strong>15~19도</strong></div></div>
<div class="box">북서쪽 <b class="hl">찬 공기</b> 남하<br>낮과 밤 기온 차 15도 안팎</div>""", SRC1, DL),
    a_slide(3, n, """<h2>내일 아침 서리·얼음</h2>
<ul class="chk"><li>전국 내륙 곳곳 <span class="hl">서리</span></li><li>경기 북동부·강원 내륙·산지 얼음</li><li>충청 내륙·전북 북동부 얼음</li><li>경북 북동 산지 얼음</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>창문·문틈 <span class="hl">외풍</span> 체크</h2>
<ul class="chk"><li>창틀·현관문 틈 바람 확인</li><li>뽁뽁이·문풍지로 틈새 막기</li><li>틈새 열 손실 줄이면 <span class="hl">실내 2~3도↑</span></li><li>커튼·러그도 보온에 도움</li></ul>""", "출처: 세계일보(2025.12.1)", DL),
    a_slide(5, n, f"""<h2>찬바람 막는 <span class="hl">외풍 차단템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SEAL)}"><div>아텍스 실리콘 문풍지<span>반투명 테이프 · 45mm x 5m</span></div></li>
<li><b>2</b><img src="{img(POP)}"><div>뽁순이 3중 뽁뽁이<span>창문에 붙이는 단열 에어캡</span></div></li>
<li><b>3</b><img src="{img(PACK)}"><div>마지온 틈새차단 고무 패킹<span>현관문·창문용 · 6M</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/2 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "내일 아침 기온 5~10도 뚝",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 내일(3일) 아침 기온 5~10도 뚝 — 서리·얼음 주의 🌬️

· 오늘(2일) 아침 6~13도, 낮 14~20도 → 내일(3일) 아침 0~9도, 낮 15~19도
· 북서쪽 찬 공기가 내려오면서 아침 기온이 하루 새 5~10도 떨어질 전망
· 낮과 밤의 기온 차 15도 안팎
· 전국 내륙 곳곳 서리, 경기 북동부·강원 내륙·산지·충청 내륙·전북 북동부·경북 북동 산지엔 얼음

✔ 창틀·현관문 틈 바람 확인 — 뽁뽁이·문풍지 등으로 틈새 열 손실을 줄이면 실내 온도가 2~3도 오르는 효과가 있다고 해요

🔗 찬바람 막는 외풍 차단템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 경향신문(11/1), 톱스타뉴스(11/2) — 기상청 예보 / 세계일보(2025.12.1)

#광고 #생활뉴스 #내일날씨 #기온뚝 #일교차 #문풍지 #뽁뽁이 #외풍차단""",
    "products": [prod(1, SEAL, N_SEAL, "A"), prod(2, POP, N_POP, "A"), prod(3, PACK, N_PACK, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 난방비 절약법 ═════════
SRC2 = "출처: 국제뉴스(11/1)·세계일보(2025.12.1), 한국에너지공단"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 난방비</div>
<h1>보일러 켜기 전<br><span class="hl">난방비</span><br>아끼는 법</h1>
<p class="lead">난방 온도 1도 낮추면<br>에너지 소비 약 7%↓</p>""", SRC2, DL),
    a_slide(2, n, """<h2>숫자로 보는 난방 절약</h2>
<div class="fig"><div><small>겨울 권장 실내온도</small><strong>20도</strong></div><div><small>난방 1도 낮추면</small><strong>약 7%↓</strong></div></div>
<div class="fig"><div><small>창문·문 틈새 차단</small><strong>약 5.5%↓</strong></div><div><small>안 쓰는 방 밸브 잠금</small><strong>약 4.4%↓</strong></div></div>
<div class="box">절감률은 <b class="hl">한국에너지공단</b> 기준<br>(국제뉴스 11/1 보도)</div>""", SRC2, DL),
    a_slide(3, n, """<h2>오늘 밤부터 해볼 것</h2>
<ul class="chk"><li>내복·실내복 입으면 20도도 <span class="hl">23~24도</span>처럼</li><li>보일러 켤 땐 가습기 함께</li><li>바닥 냉기는 실내화로</li><li>에너지바우처 신청 <span class="hl">12/31까지</span></li></ul>""", SRC2, DL),
    a_slide(4, n, f"""<h2>난방비 아끼는 <span class="hl">보온 생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(TENT)}"><div>코멧 원터치 난방텐트<span>보관가방 포함</span></div></li>
<li><b>2</b><img src="{img(SLIP)}"><div>리빙도감 겨울 털 슬리퍼<span>남녀공용 방한 실내화</span></div></li>
<li><b>3</b><img src="{img(HUMI)}"><div>대중산업 방방가습기 600<span>전기 없는 자연증발식 · 4세트</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/2 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "난방비 아끼는 법",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 보일러 켜기 전, 난방비 아끼는 법 🔥

· 겨울철 권장 실내온도는 20도
· 난방 온도를 1도 낮추면 에너지 소비 약 7% 감소 (한국에너지공단)
· 창문·문 틈새 차단 약 5.5%, 안 쓰는 방 밸브 잠그기 약 4.4% 절감 (한국에너지공단 기준)
· 내복·실내복을 입으면 20도에서도 23~24도를 유지하는 효과
· 에너지공단은 보일러를 켤 때 가습기를 함께 쓰라고 추천 — 습도가 높으면 열을 오래 간직
· 2026년도 에너지바우처 신청은 12월 31일까지 (문의 1600-3190)

✔ 오늘 밤부터 실내온도 20도, 바닥 냉기는 실내화로

🔗 난방비 아끼는 보온 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 국제뉴스(11/1), 세계일보(2025.12.1) — 한국에너지공단 자료

#광고 #생활뉴스 #난방비 #난방비절약 #에너지바우처 #난방텐트 #털슬리퍼 #자연가습기""",
    "products": [prod(1, TENT, N_TENT, "A"), prod(2, SLIP, N_SLIP, "A"), prod(3, HUMI, N_HUMI, "A")],
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






write(DATE, "B", [poll("내일 아침 0도대,<br>창문 바람 숭숭? 🌬️", "3일 아침 기온 5~10도 뚝 (기상청 예보)",
                       [("이불 속으로 피신", "창문은 못 본 척"), ("커튼 꽁꽁 치기", "일단 가리고 본다"),
                        ("보일러 온도 올리기", "고지서는 나중에"), ("뽁뽁이 붙이기", "창문에 붙여 단열")], POP)], {
    "title": "창문 외풍 대처 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 내일 아침 0도대, 창문 바람 숭숭 들어오면? 🌬️
댓글에 번호로 투표해주세요!

1️⃣ 이불 속으로 피신
2️⃣ 커튼 꽁꽁 치기
3️⃣ 보일러 온도 올리기
4️⃣ 뽁뽁이 붙이기

🔗 4번 단열 뽁뽁이 링크는 프로필에
👥 겨울마다 창문 바람 때문에 고생하는 친구 태그

#광고 #투표 #공감 #기온뚝 #외풍 #뽁뽁이 #월요일""",
    "products": [prod(1, POP, N_POP, "B")],
})

write(DATE, "B2", [poll("보일러 온도 올리기 전<br>나의 첫 행동은? 🔥", "난방 1도 낮추면 에너지 약 7%↓ (한국에너지공단)",
                        [("바로 보일러 ON", "참지 않는다"), ("수면양말 신기", "발부터 따뜻하게"),
                         ("이불 두 겹", "무게로 버틴다"), ("난방텐트 치기", "침대 위 작은 집")], TENT)], {
    "title": "보일러 켜기 전 첫 행동 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 보일러 온도 올리기 전, 나의 첫 행동은? 🔥
댓글에 번호로 투표해주세요!

1️⃣ 바로 보일러 ON
2️⃣ 수면양말 신기
3️⃣ 이불 두 겹
4️⃣ 난방텐트 치기

🔗 4번 원터치 난방텐트 링크는 프로필에
👥 집에서 제일 추위 타는 가족 태그

#광고 #투표 #공감 #난방비 #보일러 #난방텐트 #겨울준비""",
    "products": [prod(1, TENT, N_TENT, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/2 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("내일 아침 기온 뚝", "찬바람 막는", "외풍 차단템", "BEST3", [SEAL, POP, PACK]),
    c_prod(1, "0064", SEAL, "아텍스<br>실리콘 문풍지", ["반투명 실리콘 문풍지 테이프", "45mm x 5m", "창문·문틈 틈새 외풍 차단"],
           ["💰 1만원 미만", "🚀 로켓배송"]),
    c_prod(2, "0065", POP, "뽁순이<br>3중 뽁뽁이", ["창문에 붙이는 단열 에어캡", "3중 구조 뽁뽁이", "유리창 외풍·냉기 차단"],
           ["💰 1만원 미만", "🚀 로켓배송"]),
    c_prod(3, "0066", PACK, "마지온<br>틈새차단 고무 패킹", ["현관문·창문 틈새 고무 패킹", "블랙 · 6M", "문 틈으로 드는 바람 차단"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0064~0066"),
], {
    "title": "외풍 차단 생활템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

내일 아침 기온 5~10도 뚝 🌬️ 찬바람 막는 외풍 차단템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 아텍스 틈새 외풍차단 실리콘 문풍지 테이프 💛 품번 0064
반투명 실리콘 테이프, 45mm x 5m.

2. 뽁순이 3중 뽁뽁이 단열에어캡 💛 품번 0065
창문에 붙여 냉기를 막는 3중 에어캡.

3. 마지온 틈새차단 현관문 창문 고무 패킹 💛 품번 0066
현관문·창문 틈에 붙이는 고무 패킹, 블랙 6M.

※ 날씨: 기상청 예보(경향신문 11/1·톱스타뉴스 11/2 보도)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #외풍차단 #문풍지 #뽁뽁이 #틈새막이 #겨울준비""",
    "products": [prod(1, SEAL, N_SEAL, "C", "0064"), prod(2, POP, N_POP, "C", "0065"), prod(3, PACK, N_PACK, "C", "0066")],
})

write(DATE, "C2", [
    c_cover("난방비 아끼는 법", "보일러 덜 켜는", "보온 생활템", "BEST3", [TENT, SLIP, HUMI]),
    c_prod(1, "0067", TENT, "코멧<br>원터치 난방텐트", ["원터치로 펴는 난방텐트", "보관가방 포함", "침대 위 외풍 막기"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(2, "0068", SLIP, "리빙도감<br>겨울 털 슬리퍼", ["남녀공용 방한 털 슬리퍼", "겨울 실내화", "바닥 냉기 막기"],
           ["💰 1만원 미만", "📦 무료배송"]),
    c_prod(3, "0069", HUMI, "대중산업<br>방방가습기 600", ["전기 없는 자연증발식 가습기", "국내생산", "4세트 구성"],
           ["💰 3만원대", "📦 무료배송"]),
    c_howto("0067~0069"),
], {
    "title": "난방비 절약 보온템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

난방 1도 낮추면 에너지 약 7%↓ 🔥 보일러 덜 켜는 보온 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 코멧 원터치 난방텐트 + 보관가방 💛 품번 0067
침대 위에 원터치로 펴는 난방텐트.

2. 리빙도감 남녀공용 방한 겨울 털 슬리퍼 💛 품번 0068
바닥 냉기 막아주는 털 실내화.

3. 대중산업 방방가습기 600 (4세트) 💛 품번 0069
전기 없이 쓰는 국내생산 자연증발식 가습기.

※ 절감률: 한국에너지공단 기준(국제뉴스 11/1 보도)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #난방비절약 #난방텐트 #털슬리퍼 #자연가습기 #겨울준비""",
    "products": [prod(1, TENT, N_TENT, "C", "0067"), prod(2, SLIP, N_SLIP, "C", "0068"), prod(3, HUMI, N_HUMI, "C", "0069")],
})
print("ok")

