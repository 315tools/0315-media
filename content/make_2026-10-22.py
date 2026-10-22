"""2026-10-22(목, 생활용품의 날) 게시물 3개 생성 → docs/posts/2026-10-22/{A,B,C}"""
import json
from pathlib import Path

ROOT = Path("/home/claude/0315-media")
DATE = "2026-10-22"
AD = "광고 · 쿠팡 파트너스 활동으로 수수료를 제공받습니다"
DISC = "[광고] 이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다."
FONT = "'Noto Sans CJK KR','Noto Color Emoji',sans-serif"
BASE = f"""*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:{FONT};position:relative;-webkit-font-smoothing:antialiased}}
.ad{{position:absolute;left:0;right:0;top:0;height:64px;display:flex;align-items:center;padding:0 56px;font-size:27px;font-weight:700;z-index:5}}"""


def page(css, body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{css}</style></head><body>{body}</body></html>'


def write(ch, slides, post):
    d = ROOT / "docs" / "posts" / DATE / ch
    (d / "slides").mkdir(parents=True, exist_ok=True)
    for old in (d / "slides").glob("*.html"):
        old.unlink()
    for i, html in enumerate(slides, 1):
        (d / "slides" / f"{i:02d}.html").write_text(html, encoding="utf-8")
    post.update({"channel": ch, "date": DATE, "slides": [], "result": {}})
    (d / "post.json").write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ───────────── A · 기사형 생활뉴스 ─────────────
NAVY, RED, INK, MUTE, BG = "#0f2a4a", "#d7263d", "#14181f", "#5b6573", "#ffffff"
SRC = "출처: 기상청 발표 인용 보도 — 머니투데이·데일리안(10/21), 재경일보(10/22)"
A_CSS = f"""body{{background:{BG};color:{INK}}}.ad{{background:{INK};color:#fff}}
.mast{{position:absolute;left:72px;right:72px;top:104px;display:flex;justify-content:space-between;align-items:center;border-bottom:4px solid {NAVY};padding-bottom:18px}}
.brand{{font-size:36px;font-weight:900;color:{NAVY};letter-spacing:-1px}}.brand b{{color:{RED}}}
.date{{font-size:28px;font-weight:700;color:{MUTE}}}
.body{{position:absolute;left:72px;right:72px;top:210px;bottom:170px;display:flex;flex-direction:column;justify-content:center;gap:34px}}
.tag{{align-self:flex-start;background:{RED};color:#fff;font-size:30px;font-weight:800;padding:8px 18px;border-radius:6px}}
h1{{font-size:96px;line-height:1.16;font-weight:900;letter-spacing:-3px;color:{INK}}}
h2{{font-size:78px;line-height:1.2;font-weight:900;letter-spacing:-2px}}
.lead{{font-size:44px;line-height:1.5;font-weight:500;color:#2a3140}}
.hl{{color:{RED}}}
.fig{{display:flex;gap:24px}}.fig div{{flex:1;background:#f2f5f9;border-radius:16px;padding:28px 26px}}
.fig small{{display:block;font-size:30px;color:{MUTE};font-weight:700;margin-bottom:8px}}.fig strong{{font-size:72px;font-weight:900;color:{NAVY};letter-spacing:-2px}}
.box{{background:#f2f5f9;border-left:10px solid {NAVY};border-radius:8px;padding:34px 36px;font-size:42px;line-height:1.55;font-weight:600}}
ul.chk{{list-style:none;display:flex;flex-direction:column;gap:22px}}ul.chk li{{font-size:46px;font-weight:700;line-height:1.35;padding-left:64px;position:relative}}
ul.chk li:before{{content:'✓';position:absolute;left:0;top:0;width:46px;height:46px;border-radius:8px;background:{NAVY};color:#fff;font-size:32px;display:grid;place-items:center}}
ol.prod{{list-style:none;display:flex;flex-direction:column;gap:20px}}ol.prod li{{display:flex;gap:24px;align-items:center;font-size:44px;font-weight:700;background:#f2f5f9;border-radius:14px;padding:22px 26px}}
ol.prod b{{flex:none;width:64px;height:64px;border-radius:12px;background:{RED};color:#fff;display:grid;place-items:center;font-size:36px}}ol.prod span{{font-size:30px;color:{MUTE};font-weight:600;display:block;margin-top:4px}}
.src{{position:absolute;left:72px;right:72px;bottom:96px;font-size:24px;color:{MUTE};border-top:2px solid #e3e8ef;padding-top:16px}}
.foot{{position:absolute;left:72px;right:72px;bottom:40px;display:flex;justify-content:space-between;font-size:28px;font-weight:700;color:{MUTE}}}"""


def a_slide(i, n, inner, src=True):
    return page(A_CSS, f"""<div class="ad">{AD}</div>
<div class="mast"><div class="brand">0315 <b>생활뉴스</b></div><div class="date">2026.10.22 (목) · {i}/{n}</div></div>
<div class="body">{inner}</div>{f'<div class="src">{SRC}</div>' if src else ''}
<div class="foot"><span>@0315news</span><span>{'옆으로 →' if i < n else ''}</span></div>""")


n = 7
a_slides = [
    a_slide(1, n, """<div class="tag">날씨 · 생활</div>
<h1>올가을 첫 <span class="hl">한파주의보</span>…<br>하루 새 아침기온<br>10도 '뚝'</h1>
<p class="lead">21일 밤 9시 경기·강원·충청 등 내륙 곳곳 발효.<br>오늘 아침이 올가을 들어 가장 추웠습니다.</p>"""),
    a_slide(2, n, """<h2>오늘 아침, 얼마나 추웠나</h2>
<div class="fig"><div><small>서울 아침</small><strong>4.4℃</strong></div><div><small>체감온도</small><strong>1℃</strong></div></div>
<div class="fig"><div><small>대관령</small><strong>-3℃</strong></div><div><small>파주·철원</small><strong>0℃</strong></div></div>
<p class="lead">전날보다 <b class="hl">5~10도</b> 낮았고, 경기·강원 일부는 영하권 문턱까지 내려갔습니다.</p>"""),
    a_slide(3, n, """<h2>'한파주의보'는<br>언제 내려질까</h2>
<div class="box">① 아침 최저기온이 전날보다 <b class="hl">10도 이상</b> 떨어지고<br>② <b class="hl">3도 이하</b>이면서<br>③ 평년보다 <b class="hl">3도 이상</b> 낮을 때</div>
<p class="lead">세 조건이 겹칠 것으로 예상될 때 기상청이 발표합니다.</p>"""),
    a_slide(4, n, """<h2>낮엔 14~22도,<br>일교차 <span class="hl">15도</span></h2>
<p class="lead">기상청은 일교차가 15도 안팎으로 벌어질 수 있다며 <b>건강 관리</b>에 유의하라고 당부했습니다.</p>
<div class="box">공기가 건조해 호흡기가 마르기 쉬워요.<br>실내 습도는 <b class="hl">50% 안팎</b>이 권장됩니다.</div>"""),
    a_slide(5, n, """<h2>추위는 짧게,<br>23일 낮부터 회복</h2>
<p class="lead">기온은 23일 낮부터 평년 수준을 되찾을 전망입니다. 다만 첫 한파특보는 <b>겨울 채비를 시작할 때</b>라는 신호이기도 합니다.</p>
<div class="box">내일(23일) 서울 낮 최고 <b class="hl">19℃</b> 안팎 예상</div>"""),
    a_slide(6, n, """<h2>지금 해두면 좋은 것</h2>
<ul class="chk"><li>창문·현관 틈 외풍 막기</li><li>실내 습도 50% 맞추기</li><li>잠자리 보온부터 챙기기</li><li>두꺼운 외투 대신 얇게 겹쳐 입기</li></ul>""", src=False),
    a_slide(7, n, """<h2>오늘 정리한 <span class="hl">겨울 채비템</span></h2>
<ol class="prod"><li><b>1</b><div>3중 단열 뽁뽁이<span>창문 외풍·결로 막기</span></div></li>
<li><b>2</b><div>국내생산 우레탄 문풍지<span>문틈 바람 차단</span></div></li>
<li><b>3</b><div>초음파 가습기 4L<span>건조한 실내 습도 관리</span></div></li>
<li><b>4</b><div>탄소열선 전기요<span>보일러 켜기 전 잠자리 보온</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/22 ①~④</p>""", src=False),
]
a_caption = f"""{DISC}

[생활뉴스] 올가을 첫 한파주의보…하루 새 아침기온 10도 '뚝'

· 21일 밤 9시 경기·강원·충청 등 내륙 곳곳 한파주의보
· 오늘 서울 아침 4.4℃(체감 1℃), 대관령 -3℃
· 일교차 15도 안팎 → 건강관리·실내 습도 50% 유지
· 23일 낮부터 기온 평년 회복

🔗 겨울 채비템 ①~④는 프로필 링크에 있어요
🛒 외풍차단템 자세한 비교는 @0315_pick

출처: 기상청 발표 인용 보도(머니투데이·데일리안 10/21, 재경일보 10/22)

#광고 #한파주의보 #생활뉴스 #오늘날씨 #일교차 #겨울준비 #외풍차단"""
write("A", a_slides, {
    "title": "올가을 첫 한파주의보",
    "caption": a_caption,
    "products": [
        {"no": 1, "name": "탐사 국내생산 3중 단열뽁뽁이 에어캡", "coupang_url": "https://www.coupang.com/vp/products/320451654", "affiliate_url": ""},
        {"no": 2, "name": "코멧 국내생산 사계절 우레탄 문풍지 3m 5개", "coupang_url": "https://www.coupang.com/vp/products/8301704105", "affiliate_url": ""},
        {"no": 3, "name": "홈플래닛 초음파 가습기 4L", "coupang_url": "https://www.coupang.com/vp/products/324788226", "affiliate_url": ""},
        {"no": 4, "name": "한일 탄소열선 전기요 (싱글)", "coupang_url": "https://www.coupang.com/vp/products/9150828084", "affiliate_url": ""},
    ],
})

# ───────────── B · 투표형 공감짤 ─────────────
B_CSS = """body{background:#ffe14d;color:#16181c}.ad{background:#16181c;color:#fff}
.q{position:absolute;left:64px;right:64px;top:120px}
.q small{display:inline-block;background:#16181c;color:#ffe14d;font-size:32px;font-weight:900;padding:8px 20px;border-radius:8px;margin-bottom:22px}
.q h1{font-size:86px;font-weight:900;letter-spacing:-3px;line-height:1.15}
.q p{font-size:36px;font-weight:700;margin-top:16px;color:#3a3a2a}
.opts{position:absolute;left:64px;right:64px;top:520px;display:flex;flex-direction:column;gap:22px}
.o{background:#fff;border:5px solid #16181c;border-radius:22px;padding:26px 30px;display:flex;align-items:center;gap:26px;box-shadow:0 8px 0 #16181c}
.o b{flex:none;width:78px;height:78px;border-radius:50%;background:#16181c;color:#ffe14d;font-size:44px;display:grid;place-items:center}
.o span{font-size:46px;font-weight:900;letter-spacing:-1px;line-height:1.25}.o em{display:block;font-style:normal;font-size:30px;font-weight:700;color:#6b6b5a}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;align-items:center;font-size:34px;font-weight:900}
.foot span:last-child{font-size:30px;color:#3a3a2a}"""
b_slide = page(B_CSS, f"""<div class="ad">{AD}</div>
<div class="q"><small>📊 오늘의 투표</small><h1>첫 한파주의보 뜬 날,<br>보일러 언제 켬? 🥶</h1><p>오늘 아침 서울 체감 1℃</p></div>
<div class="opts">
 <div class="o"><b>1</b><span>오늘 바로 켰다<em>추운데 참는 게 더 손해</em></span></div>
 <div class="o"><b>2</b><span>11월까지 버틴다<em>10월에 켜면 지는 거</em></span></div>
 <div class="o"><b>3</b><span>엄마가 켜줄 때까지<em>우리 집 보일러 결정권자 따로 있음</em></span></div>
 <div class="o"><b>4</b><span>전기요 + 뽁뽁이로 버틴다<em>가스비 방어 끝판왕</em></span></div>
</div>
<div class="foot"><span>👇 댓글에 번호로 투표</span><span>@0315_zzal</span></div>""")
b_caption = f"""{DISC}

📊 첫 한파주의보 뜬 날, 보일러 언제 켬? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 오늘 바로 켰다
2️⃣ 11월까지 버틴다
3️⃣ 엄마가 켜줄 때까지
4️⃣ 전기요 + 뽁뽁이로 버틴다

🔗 4번 전기요·뽁뽁이 링크는 프로필에
👥 우리 집 보일러 결정권자 태그

#광고 #투표 #공감 #보일러 #한파주의보 #가스비 #자취"""
write("B", [b_slide], {
    "title": "보일러 언제 켬? 투표",
    "caption": b_caption,
    "products": [
        {"no": 1, "name": "한일 탄소열선 전기요 (싱글)", "coupang_url": "https://www.coupang.com/vp/products/9150828084", "affiliate_url": ""},
        {"no": 2, "name": "탐사 국내생산 3중 단열뽁뽁이 에어캡", "coupang_url": "https://www.coupang.com/vp/products/320451654", "affiliate_url": ""},
    ],
})

# ───────────── C · 상품소개 (상위 계정 스타일) ─────────────
C_CSS = """body{background:#1b1d22;color:#fff}.ad{background:#fff;color:#111}
.hook{position:absolute;left:0;right:0;top:250px;text-align:center}.hook span{background:#000;color:#fff;font-size:44px;font-weight:800;padding:10px 26px;border-radius:6px}
.big{position:absolute;left:40px;right:40px;top:360px;text-align:center;font-weight:900;letter-spacing:-4px;line-height:1.12;text-shadow:0 6px 0 rgba(0,0,0,.35)}
.big .y{color:#ffe14d}.emo{position:absolute;left:0;right:0;bottom:250px;text-align:center;font-size:150px;letter-spacing:20px}
.num{position:absolute;left:64px;top:110px;font-size:120px;font-weight:900;color:#ffe14d;letter-spacing:-4px}
.code{position:absolute;right:64px;top:140px;background:#ffe14d;color:#111;font-size:36px;font-weight:900;padding:10px 22px;border-radius:10px}
.pemo{position:absolute;left:0;right:0;top:250px;text-align:center;font-size:190px;line-height:1}
.pname{position:absolute;left:64px;right:64px;top:500px;font-size:72px;font-weight:900;letter-spacing:-2px;line-height:1.2}
.pts{position:absolute;left:64px;right:64px;top:770px;display:flex;flex-direction:column;gap:20px}
.pts div{font-size:44px;font-weight:700;line-height:1.35;padding-left:56px;position:relative}.pts div:before{content:'✔';position:absolute;left:0;color:#ffe14d}
.meta{position:absolute;left:64px;right:64px;bottom:150px;display:flex;gap:16px;flex-wrap:wrap}
.meta span{background:#2c3038;border-radius:999px;padding:12px 24px;font-size:32px;font-weight:700}
.foot{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-size:30px;font-weight:700;color:#b9bec8}
.howto{position:absolute;left:64px;right:64px;top:260px;display:flex;flex-direction:column;gap:30px}
.howto h2{font-size:84px;font-weight:900;letter-spacing:-2px}.howto h2 .y{color:#ffe14d}
.step{display:flex;gap:26px;align-items:center;background:#2c3038;border-radius:18px;padding:30px}
.step b{flex:none;width:76px;height:76px;border-radius:50%;background:#ffe14d;color:#111;font-size:44px;display:grid;place-items:center}
.step p{font-size:44px;font-weight:700;line-height:1.35}.step small{display:block;font-size:30px;color:#b9bec8;font-weight:600}"""
C_NOTE = "10/22 쿠팡 판매량순 기준 · 가격은 바뀔 수 있어요"


def c_foot(right="옆으로 →"):
    return f'<div class="foot"><span>@0315_pick</span><span>{right}</span></div>'


c_cover = page(C_CSS, f"""<div class="ad">{AD}</div>
<div class="hook"><span>첫 한파주의보 떴다면</span></div>
<div class="big"><div style="font-size:150px">만원 이하</div><div class="y" style="font-size:170px">외풍차단템</div><div style="font-size:190px">BEST3</div></div>
<div class="emo">🪟🚪🧊</div>{c_foot()}""")


def c_prod(no, code, emo, name, pts, meta):
    return page(C_CSS, f"""<div class="ad">{AD}</div>
<div class="num">{no:02d}</div><div class="code">품번 {code}</div>
<div class="pemo">{emo}</div><div class="pname">{name}</div>
<div class="pts">{''.join(f'<div>{p}</div>' for p in pts)}</div>
<div class="meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>{c_foot()}""")


c_slides = [
    c_cover,
    c_prod(1, "0001", "🪟", "3중 단열 뽁뽁이<br>(국내생산)", ["창문에 붙이기만 하면 끝", "공기층 3겹으로 외풍·결로 차단", "민무늬라 어느 창에 붙여도 무난"],
           ["⭐ 리뷰 2.4만+", "💰 9천원 안팎", "🚀 내일 도착"]),
    c_prod(2, "0002", "🚪", "국내생산 우레탄 문풍지<br>(3m × 5개입)", ["문틈에 붙여 들어오는 바람 차단", "5개입이라 방문·창문 여러 곳에", "사계절 쓰는 우레탄 소재"],
           ["⭐ 리뷰 1,800+", "💰 6천원대", "🚀 내일 도착"]),
    c_prod(3, "0003", "🧊", "실리콘 틈새막이 테이프<br>(45mm × 5m)", ["반투명이라 창틀에 티 안 남", "길게 잘라 쓰는 테이프형", "3천원대로 가장 부담 없음"],
           ["⭐ 리뷰 1,300+", "💰 3천원대", "🚀 내일 도착"]),
    page(C_CSS, f"""<div class="ad">{AD}</div>
<div class="howto"><h2>구매 방법 <span class="y">2가지</span></h2>
<div class="step"><b>1</b><p>프로필 링크 클릭<small>품번 0001~0003 바로 찾기</small></p></div>
<div class="step"><b>2</b><p>댓글에 "링크" 남기기<small>DM으로 보내드려요</small></p></div>
<div class="step"><b>✓</b><p>저장해두고 살 때 꺼내보기<small>{C_NOTE}</small></p></div></div>{c_foot("")}"""),
]
c_caption = f"""{DISC}

첫 한파주의보 떴다면 🥶 만원 이하 외풍차단템 BEST3

❤️구매 방법❤️
1. 프로필 링크 클릭 → 품번 검색
2. 댓글에 "링크" 남기면 DM 드려요

1. 3중 단열 뽁뽁이 💛 품번 0001
창문에 붙이기만 하면 끝. 공기층 3겹이라 외풍·결로를 같이 막아줘요.

2. 국내생산 우레탄 문풍지 💛 품번 0002
5개입이라 방문·창문 여러 곳을 한 번에. 문틈으로 들어오는 바람을 막아줘요.

3. 실리콘 틈새막이 테이프 💛 품번 0003
반투명이라 창틀에 티가 안 나요. 3천원대로 제일 부담 없는 선택.

※ {C_NOTE}

#광고 #쿠팡추천템 #외풍차단 #뽁뽁이 #문풍지 #겨울준비 #자취템 #살림템"""
write("C", c_slides, {
    "title": "만원 이하 외풍차단템 BEST3",
    "caption": c_caption,
    "products": [
        {"no": 1, "code": "0001", "name": "탐사 국내생산 3중 단열뽁뽁이 에어캡", "coupang_url": "https://www.coupang.com/vp/products/320451654", "affiliate_url": ""},
        {"no": 2, "code": "0002", "name": "코멧 국내생산 사계절 우레탄 문풍지 3m 5개", "coupang_url": "https://www.coupang.com/vp/products/8301704105", "affiliate_url": ""},
        {"no": 3, "code": "0003", "name": "아텍스 실리콘 틈새차단 문풍지 테이프 45mm×5m", "coupang_url": "https://www.coupang.com/vp/products/9287063502", "affiliate_url": ""},
    ],
})
print("ok")
