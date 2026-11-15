"""2026-11-15(일, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-14/{A,B,C,A2,B2,C2}
점심: 비 그친 포근한 일요일(낮 최고 21도) → 가벼운 나들이 특이템 / 퇴근길: 올해 김장비용 9% 하락 → 김장 특이템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-15"
DL = "2026.11.15 (일)"
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

NOTE = "11/15 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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






MAT, CUP, SEAT = "9216944059", "7288013604", "7330431138"
KMAT, GAR, GLV = "8429418365", "8512946878", "8326356395"
N_MAT = "브리즈문 포켓 방수 피크닉 돗자리"
N_CUP = "실리만 국내생산 하모니 접이식 휴대컵"
N_SEAT = "다인네 접이식 휴대용 4단 방석 2p + 파우치 2p 세트"
N_KMAT = "헬로앤코 무봉제 다용도 김장매트"
N_GAR = "쿠팸-M2 무선 전동 마늘 다지기 350ml"
N_GLV = "살리미템 김장용 긴 위생장갑 60cm"

# ═════════ A · 점심 12:00 — 비 그친 포근한 일요일 ═════════
SRC1 = "출처: 머니투데이(11/15), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 오늘</div>
<h1>비 그친 일요일<br><span class="hl">낮 최고 21도</span></h1>
<p class="lead">오전부터 차차 맑아져요<br>미세먼지도 '좋음~보통'</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(15일) <span class="hl">전국 기온</span></h2>
<div class="fig"><div><small>아침 최저</small><strong>6~13도</strong></div><div><small>낮 최고</small><strong>16~21도</strong></div></div>
<div class="fig"><div><small>서울</small><strong>9 → 18도</strong></div><div><small>부산</small><strong>13 → 21도</strong></div></div>
<div class="box">대전·대구·광주·전주 낮 <b class="hl">19도</b><br>당분간 평년보다 높은 기온</div>""", SRC1, DL),
    a_slide(3, n, """<h2>나들이 전 <span class="hl">체크</span></h2>
<ul class="chk"><li>강원 동해안·산지는 흐리고<br>저녁 6시 이후 곳에 따라 약한 빗방울</li><li>밤부터 동해안 <span class="hl">너울성 파도</span> 주의</li><li>아침·저녁은 쌀쌀 — 겉옷 챙기기</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>가볍게 <span class="hl">공원 나들이</span></h2>
<ul class="chk"><li>비 온 뒤 잔디는 축축 — <span class="hl">방수 매트</span></li><li>앉을 곳 없으면 접이식 방석</li><li>따뜻한 음료는 접이식 컵에</li><li>쓰레기는 되가져오기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>주머니 쏙 <span class="hl">나들이 특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(MAT)}"><div>브리즈문 포켓 돗자리<span>방수 · 접으면 주머니 크기</span></div></li>
<li><b>2</b><img src="{img(CUP)}"><div>실리만 접이식 휴대컵<span>국내생산 · 납작하게 접혀요</span></div></li>
<li><b>3</b><img src="{img(SEAT)}"><div>다인네 접이식 4단 방석<span>2p + 파우치 세트</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/15 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "비 그친 포근한 일요일",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 비 그친 일요일(15일), 낮 최고 21도 포근 ☀️

· 전국 흐리다가 오전부터 차차 맑아짐
· 아침 최저 6~13도, 낮 최고 16~21도 — 당분간 평년보다 높아요
· 서울 9→18도, 대전 11→19도, 대구 11→19도, 광주 12→19도, 부산 13→21도
· 미세먼지 전 권역 '좋음~보통'
· 강원 동해안·산지는 흐리고 오후 6시 이후 곳에 따라 약한 빗방울, 밤부터 동해안 너울성 파도 주의

✔ 비 온 뒤 잔디는 축축 — 방수 매트, 아침·저녁 쌀쌀하니 겉옷 챙기기

🔗 주머니 쏙 나들이 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 머니투데이(11/15) — 기상청 예보

#광고 #생활뉴스 #날씨 #일요일날씨 #나들이 #피크닉 #돗자리 #특이한상품""",
    "products": [prod(1, MAT, N_MAT, "A"), prod(2, CUP, N_CUP, "A"), prod(3, SEAT, N_SEAT, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 김장비용 9% 하락 ═════════
SRC2 = "출처: aT 조사(11/9 기준) — 미디어펜·한국영농신문(11/10·12), 아시아경제(11/15)"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">물가 · 김장철</div>
<h1>올해 김장비용<br><span class="hl">19만9456원</span></h1>
<p class="lead">4인 가족·배추 20포기 기준<br>작년보다 9.0% 낮아요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>배추값이 <span class="hl">크게 내렸어요</span></h2>
<div class="fig"><div><small>배추 20포기</small><strong>54,980원</strong></div><div><small>작년 대비</small><strong>-26.5%</strong></div></div>
<div class="fig"><div><small>쪽파</small><strong>-48.9%</strong></div><div><small>갓</small><strong>-20.5%</strong></div></div>
<div class="box">무 -5.6% · 대파 -10.3% · 고춧가루 -1.8%</div>""", SRC2, DL),
    a_slide(3, n, """<h2>오른 것도 <span class="hl">있어요</span></h2>
<div class="fig"><div><small>새우젓</small><strong>+40.2%</strong></div><div><small>깐마늘</small><strong>+21.6%</strong></div></div>
<ul class="chk"><li>생강 +3.8% · 천일염 +3.0%</li><li>평년보다는 <span class="hl">13.4%</span> 낮은 수준</li><li>전국 53곳(시장·대형유통) 조사</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>김장재료 <span class="hl">할인 기간</span></h2>
<ul class="chk"><li>배추·무·고춧가루·마늘 등<br>최대 <span class="hl">40%</span> 할인 — 12월 2일까지</li><li>새우젓·액젓·천일염·굴 등<br>최대 <span class="hl">50%</span> 할인 — 11월 29일까지</li><li>할인율·구매 한도는 매장마다 달라요</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>김장 날 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(KMAT)}"><div>헬로앤코 김장매트<span>무봉제 · 다용도</span></div></li>
<li><b>2</b><img src="{img(GAR)}"><div>쿠팸 무선 전동 마늘 다지기<span>350ml · 강화유리</span></div></li>
<li><b>3</b><img src="{img(GLV)}"><div>살리미템 김장용 긴 장갑<span>60cm 팔토시형</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/15 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "올해 김장비용 9% 하락",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 올해 김장비용 19만9456원… 작년보다 9.0% 낮아요 🥬

· 4인 가족·배추 20포기 기준 199,456원 (aT, 11월 9일 기준)
· 작년 11월 상순(219,071원)보다 9.0%, 평년보다 13.4% 낮음
· 배추 20포기 54,980원(-26.5%), 쪽파 -48.9%, 갓 -20.5%, 대파 -10.3%, 무 -5.6%, 고춧가루 -1.8%
· 오른 품목: 새우젓 +40.2%, 깐마늘 +21.6%, 생강 +3.8%, 천일염 +3.0%
· 정부 지원 김장재료 할인: 농산물 최대 40%(12월 2일까지), 수산물 최대 50%(11월 29일까지) — 할인율·한도는 매장마다 달라요

🔗 김장 날 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 한국농수산식품유통공사(aT) 조사 — 미디어펜(11/10)·한국영농신문(11/12)·아시아경제(11/15)

#광고 #생활뉴스 #물가 #김장 #김장비용 #김장매트 #특이한상품""",
    "products": [prod(1, KMAT, N_KMAT, "A"), prod(2, GAR, N_GAR, "A"), prod(3, GLV, N_GLV, "A")],
})

# ═════════ B · 투표 ═════════
write(DATE, "B", [poll("포근한 일요일 나들이,<br>공원에서 앉는 법은? 🌳", "오늘 낮 최고 21도, 오전부터 맑아져요 (기상청 예보)",
                       [("벤치 사수", "빈자리 날 때까지 대기"), ("그냥 서 있기", "걷기만 하다 온다"),
                        ("신문지 깔기", "있는 걸로 대충"), ("포켓 돗자리", "주머니에서 꺼내 촥")], MAT)], {
    "title": "공원 나들이 앉는 법 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 포근한 일요일 나들이, 공원에서 앉는 법은? 🌳
댓글에 번호로 투표해주세요!

1️⃣ 벤치 사수
2️⃣ 그냥 서 있기
3️⃣ 신문지 깔기
4️⃣ 포켓 돗자리

※ 15일(일) 오전부터 차차 맑아져 낮 최고 16~21도 (기상청 예보, 머니투데이 11/15)

🔗 4번 브리즈문 포켓 방수 돗자리 링크는 프로필에
👥 오늘 같이 산책 갈 친구 태그

#광고 #투표 #공감 #일요일 #나들이 #돗자리""",
    "products": [prod(1, MAT, N_MAT, "B")],
})

write(DATE, "B2", [poll("김장하는 날,<br>나의 포지션은? 🥬", "올해 김장비용 작년보다 9% 낮아요 (aT 조사)",
                        [("배추 절이기 담당", "소금 뿌리는 손이 바쁨"), ("수육 담당", "김장의 진짜 목적"),
                         ("사진만 찍기", "가족 단톡방 업로드"), ("버무리기 담당", "김장매트 깔고 시작")], KMAT)], {
    "title": "김장 포지션 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 김장하는 날, 나의 포지션은? 🥬
댓글에 번호로 투표해주세요!

1️⃣ 배추 절이기 담당
2️⃣ 수육 담당
3️⃣ 사진만 찍기
4️⃣ 버무리기 담당

※ 4인 가족 김장비용 19만9456원, 작년보다 9.0% 낮음 (aT 11월 9일 기준, 미디어펜 11/10)

🔗 4번 헬로앤코 김장매트 링크는 프로필에
👥 김장 날 같이 버무릴 가족 태그

#광고 #투표 #공감 #김장 #김장매트 #김장철""",
    "products": [prod(1, KMAT, N_KMAT, "B")],
})

# ═════════ C · 상품소개 ═════════
write(DATE, "C", [
    c_cover("낮 최고 21도 포근한 일요일", "주머니 쏙", "나들이 특이템", "BEST3", [MAT, CUP, SEAT]),
    c_prod(1, "0142", MAT, "브리즈문<br>포켓 돗자리", ["방수 피크닉 돗자리", "접으면 주머니 크기", "비 온 뒤 잔디에도"],
           ["💰 8천원대", "🚀 로켓배송"]),
    c_prod(2, "0143", CUP, "실리만<br>접이식 휴대컵", ["국내생산 실리콘 컵", "납작하게 접어서 휴대", "따뜻한 음료 담기"],
           ["💰 9천원대", "📦 일반배송"]),
    c_prod(3, "0144", SEAT, "다인네<br>접이식 4단 방석", ["휴대용 4단 접이식 방석", "2p + 파우치 2p", "벤치·잔디 어디든"],
           ["💰 4천원대", "🚀 로켓배송"]),
    c_howto("0142~0144"),
], {
    "title": "주머니 쏙 나들이 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

낮 최고 21도 포근한 일요일 ☀️ 주머니 쏙 나들이 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 브리즈문 포켓 방수 피크닉 돗자리 💛 품번 0142
접으면 주머니에 들어가는 방수 돗자리.

2. 실리만 국내생산 하모니 접이식 휴대컵 💛 품번 0143
납작하게 접어 들고 다니는 실리콘 컵.

3. 다인네 접이식 휴대용 4단 방석 2p + 파우치 2p 세트 💛 품번 0144
4단으로 접히는 휴대용 방석, 파우치 포함 2개 세트.

※ 날씨: 15일 아침 6~13도, 낮 16~21도 — 기상청 예보(머니투데이 11/15 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #나들이 #돗자리 #접이식컵 #등산방석""",
    "products": [prod(1, MAT, N_MAT, "C", "0142"), prod(2, CUP, N_CUP, "C", "0143"), prod(3, SEAT, N_SEAT, "C", "0144")],
})

write(DATE, "C2", [
    c_cover("올해 김장비용 9% 하락", "김장하는 날", "손 편한 특이템", "BEST3", [KMAT, GAR, GLV]),
    c_prod(1, "0145", KMAT, "헬로앤코<br>김장매트", ["무봉제 다용도 매트", "배추 버무리기·절이기", "분갈이에도"],
           ["💰 1만5천원대", "🚀 로켓배송"]),
    c_prod(2, "0146", GAR, "쿠팸 무선<br>전동 마늘 다지기", ["무선 전동 다지기 350ml", "강화유리 용기 · 6중날", "마늘·야채 다지기"],
           ["💰 1만4천원대", "🚚 무료배송"]),
    c_prod(3, "0147", GLV, "살리미템<br>김장용 긴 장갑", ["60cm 팔토시형 위생장갑", "도톰한 밴드형", "양념 묻을 걱정 덜기"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_howto("0145~0147"),
], {
    "title": "김장하는 날 특이템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

올해 김장비용 9% 하락 🥬 김장하는 날 손 편한 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 헬로앤코 무봉제 다용도 김장매트 💛 품번 0145
배추 절이고 버무릴 때 까는 무봉제 매트.

2. 쿠팸-M2 무선 전동 마늘 다지기 350ml 💛 품번 0146
강화유리 용기에 6중날, 무선 전동 다지기.

3. 살리미템 김장용 긴 위생장갑 60cm 💛 품번 0147
팔까지 덮는 60cm 팔토시형 비닐장갑.

※ 김장비용: 4인 가족 199,456원, 작년보다 9.0% 낮음 — aT 조사(미디어펜 11/10 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #김장 #김장매트 #마늘다지기 #김장장갑""",
    "products": [prod(1, KMAT, N_KMAT, "C", "0145"), prod(2, GAR, N_GAR, "C", "0146"), prod(3, GLV, N_GLV, "C", "0147")],
})
print("ok")
