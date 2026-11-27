"""2026-11-27(금, 식품의 날) 게시물 6개 → docs/posts/2026-11-27/{A,B,C,A2,B2,C2}
점심: 오늘 서울 낮 16도·약한 비 → 주말 서울 낮 8도·일요일 아침 영하 2도 → 주말 뜨끈한 국물 집밥 / 퇴근길: 딸기 도매가 작년보다 18.6%↓ → 딸기·연유·그릭요거트
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-27"
DL = "2026.11.27 (금)"
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


GOM, BUDAE, UDON = "7675260700", "296139681", "8341377794"
BERRY, MILK, YOG = "7707393706", "8312789832", "7216495213"
N_GOM = "양반 진국 사골곰탕 500g x 14개"
N_BUDAE = "곰곰 더 오리지널 부대찌개 (냉동)"
N_UDON = "면사랑 사누끼 우동면 5개입 (냉동)"
N_BERRY = "하동품애 GAP 한단 설향 딸기 대과"
N_MILK = "서울우유 연유 200g 튜브형"
N_YOG = "매일바이오 그릭요거트 무가당 플레인"

# ═════════ A · 점심 12:00 — 주말 기온 뚝 ═════════
SRC1 = "출처: SBS(11/27)·이투데이·파이낸셜뉴스(11/26) — 기상청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 날씨</div>
<h1>오늘 16도<br><span class="hl">주말엔 뚝</span></h1>
<p class="lead">일요일 서울 아침<br>영하 2도</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(27일) <span class="hl">포근해요</span></h2>
<div class="fig"><div><small>서울 낮</small><strong>16도</strong></div><div><small>대구·광주 낮</small><strong>20도</strong></div></div>
<div class="box">중부·호남 <b class="hl">1mm 안팎</b> 약한 비<br>중부는 바람 강하게 불어요</div>""", SRC1, DL),
    a_slide(3, n, """<h2>주말 <span class="hl">서울 기온</span></h2>
<div class="fig"><div><small>토 낮 최고</small><strong>8도</strong></div><div><small>일 아침</small><strong>-2도</strong></div></div>
<div class="box">하루 만에 낮 기온 <b class="hl">8도</b>↓<br>내륙 체감온도 <b class="hl">영하 5도</b> 안팎</div>""", SRC1, DL),
    a_slide(4, n, """<h2>주말 <span class="hl">이것 조심</span></h2>
<ul class="chk"><li>토요일 충청·전라 <span class="hl">비 또는 눈</span></li><li>일요일 새벽 젖은 길 <span class="hl">살얼음</span></li><li>다리 위·고갯길·터널 입구 <span class="hl">특히</span></li><li>월요일 서울 낮 <span class="hl">15도</span>로 다시 올라요</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>주말엔 <span class="hl">뜨끈한 국물</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(GOM)}"><div>사골곰탕 500g x 14개<span>양반 진국 · 데우기만</span></div></li>
<li><b>2</b><img src="{img(BUDAE)}"><div>더 오리지널 부대찌개<span>곰곰 · 냉동</span></div></li>
<li><b>3</b><img src="{img(UDON)}"><div>사누끼 우동면 5개입<span>면사랑 · 국물에 사리로</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/27 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "오늘 16도, 주말엔 서울 낮 8도로 뚝",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘은 포근, 주말엔 기온 뚝 🥶 일요일 서울 아침 영하 2도

· 27일(금) 서울 낮 16도, 대구·광주 20도까지 — 평년보다 높아요
· 중부·호남에 1mm 안팎 약한 비, 중부는 바람 강해요
· 28일(토) 서울 낮 최고 8도로 크게 떨어지고, 충청·전라엔 비 또는 눈
· 29일(일) 서울 아침 영하 2도·낮 8도, 내륙 체감온도 영하 5도 안팎
· 28일 밤~29일 새벽 젖은 노면이 얼 수 있어 다리 위·고갯길·터널 입구 조심
· 30일(월) 서울 낮 15도로 다시 오를 전망

✔ 주말 외출은 따뜻하게
✔ 일요일 아침 운전·보행은 살얼음 조심

🔗 주말 뜨끈한 국물 ①~③은 프로필 링크에 있어요
🛒 더 많은 집밥템은 @0315_pick

출처: SBS(2026.11.27)·이투데이(2026.11.26)·파이낸셜뉴스(2026.11.26) — 기상청 예보

#광고 #생활뉴스 #날씨 #주말날씨 #기온뚝 #국물요리 #사골곰탕""",
    "products": [prod(1, GOM, N_GOM, "A"), prod(2, BUDAE, N_BUDAE, "A"), prod(3, UDON, N_UDON, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 딸기값 뚝 ═════════
SRC2 = "출처: 한국경제·서울경제(11/25) — aT·농촌경제연구원"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 물가</div>
<h1>딸기값<br><span class="hl">작년보다 ↓</span></h1>
<p class="lead">올겨울 딸기<br>작황이 좋아요</p>""", SRC2, DL),
    a_slide(2, n, """<h2>가락시장 <span class="hl">도매가</span></h2>
<div class="fig"><div><small>딸기 2kg (24일)</small><strong>4.4만원</strong></div><div><small>작년 11월 평균</small><strong>5.4만원</strong></div></div>
<div class="box">작년 11월보다 <b class="hl">18.6%</b>↓<br>재작년 11월보다 <b class="hl">37.3%</b>↓</div>""", SRC2, DL),
    a_slide(3, n, """<h2>소매가도 <span class="hl">내려요</span></h2>
<div class="fig"><div><small>1kg 전국 평균</small><strong>3.3만원</strong></div><div><small>일주일 전</small><strong>4.1만원</strong></div></div>
<div class="box">일주일 새 약 <b class="hl">19%</b>↓<br>aT 가격정보 기준</div>""", SRC2, DL),
    a_slide(4, n, """<h2>왜 <span class="hl">내렸을까</span></h2>
<ul class="chk"><li>심은 뒤 선선해 <span class="hl">고온 피해 적어</span></li><li>병해충 피해도 <span class="hl">줄었어요</span></li><li>11월 출하량 <span class="hl">4.0%</span>↑ 전망</li><li><span class="hl">12월 중순</span>까지 내림세 전망</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>딸기 <span class="hl">실컷 먹기</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BERRY)}"><div>설향 딸기 대과<span>하동품애 · GAP 인증</span></div></li>
<li><b>2</b><img src="{img(MILK)}"><div>연유 200g 튜브형<span>서울우유 · 찍어 먹기</span></div></li>
<li><b>3</b><img src="{img(YOG)}"><div>그릭요거트 플레인<span>매일바이오 · 무가당</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/27 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "딸기 도매가 작년보다 18.6% 내려",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 올겨울 딸기값, 작년보다 내렸어요 🍓

· 서울 가락시장 딸기 2kg 평균 경락가 4만4267원(24일 거래)
· 작년 11월 평균(5만4354원)보다 18.6%, 재작년 11월(7만632원)보다 37.3% 낮아요
· 전국 평균 소매가 1kg 3만2873원 — 일주일 전(4만803원)보다 약 19% 하락

왜 내렸을까
· 모종 심은 뒤 날씨가 선선해 고온 피해가 적고 병해충도 줄었어요
· 농촌경제연구원: 이달 출하량 작년보다 4.0% 증가 전망 (면적 2.9%↓, 단위 면적당 생산량 7.1%↑)
· 출하 농가가 늘어 12월 중순까지 내림세가 이어질 전망
· 크리스마스 수요·한파는 변수

🔗 딸기 실컷 먹기 ①~③은 프로필 링크에 있어요
🛒 더 많은 장보기템은 @0315_pick

출처: 한국경제(2026.11.25)·서울경제(2026.11.25) — aT 농산물 가격정보·한국농촌경제연구원

#광고 #생활뉴스 #물가 #딸기 #딸기값 #겨울과일 #장보기""",
    "products": [prod(1, BERRY, N_BERRY, "A"), prod(2, MILK, N_MILK, "A"), prod(3, YOG, N_YOG, "A")],
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


write(DATE, "B", [poll("주말 기온 뚝,<br>집에서 끓일 국물은? 🍲", "일요일 서울 아침 영하 2도 · 기상청",
                       [("김치찌개", "밥 두 공기 각"), ("라면", "제일 빠름"),
                        ("어묵탕", "꼬치 꽂아서"), ("사골곰탕", "파 송송 데우기만")], GOM)], {
    "title": "주말 국물 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 주말 기온 뚝, 집에서 끓일 국물은? 🍲
댓글에 번호로 투표해주세요!

1️⃣ 김치찌개
2️⃣ 라면
3️⃣ 어묵탕
4️⃣ 사골곰탕

※ 27일 서울 낮 16도였다가 28일 낮 8도, 29일 아침 영하 2도로 뚝 (기상청 예보, 이투데이 11/26·SBS 11/27)

🔗 4번 양반 진국 사골곰탕 링크는 프로필에
👥 주말 집콕 메뉴 같이 정할 사람 태그

#광고 #투표 #공감 #주말날씨 #국물요리 #사골곰탕""",
    "products": [prod(1, GOM, N_GOM, "B")],
})

write(DATE, "B2", [poll("딸기값 내렸대요,<br>나는 이렇게 먹는다 🍓", "가락시장 딸기 작년 11월보다 18.6%↓",
                        [("그냥 씻어서", "원조가 최고"), ("딸기우유", "갈아서 한 잔"),
                         ("생크림 케이크", "연말엔 필수"), ("연유 듬뿍", "찍먹이 진리")], MILK)], {
    "title": "딸기 먹는 법 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 딸기값 내렸대요, 나는 이렇게 먹는다 🍓
댓글에 번호로 투표해주세요!

1️⃣ 그냥 씻어서
2️⃣ 딸기우유
3️⃣ 생크림 케이크
4️⃣ 연유 듬뿍

※ 서울 가락시장 딸기 2kg 평균 경락가 4만4267원, 작년 11월 평균보다 18.6% 낮아요 (한국경제·서울경제 11/25)

🔗 4번 서울우유 연유 튜브형 링크는 프로필에
👥 딸기 같이 먹을 사람 태그

#광고 #투표 #공감 #딸기 #연유 #겨울과일""",
    "products": [prod(1, MILK, N_MILK, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/27 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("주말엔 기온 뚝 🥶", "뜨끈하게", "주말 국물", "BEST3", [GOM, BUDAE, UDON]),
    c_prod(1, "0214", GOM, "사골곰탕<br>14개", ["양반 진국 사골곰탕", "500g 파우치 14개", "데우기만 하면 끝"],
           ["💰 1만원대", "📦 500g x 14"]),
    c_prod(2, "0215", BUDAE, "오리지널<br>부대찌개", ["곰곰 더 오리지널", "냉동 보관", "냄비에 끓이기만"],
           ["💰 1만원대", "📦 냉동"]),
    c_prod(3, "0216", UDON, "사누끼<br>우동면 5개", ["면사랑 사누끼 우동면", "1인분씩 5개입", "국물 사리로 딱"],
           ["💰 4천원대", "📦 5개입"]),
    c_howto("0214~0216"),
], {
    "title": "주말 국물 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

주말엔 기온 뚝 🥶 뜨끈하게 주말 국물 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 양반 진국 사골곰탕 500g x 14개 💛 품번 0214
파우치째 데우기만 하면 되는 사골 국물.

2. 곰곰 더 오리지널 부대찌개 (냉동) 💛 품번 0215
냄비에 붓고 끓이면 주말 저녁 한 냄비.

3. 면사랑 사누끼 우동면 5개입 (냉동) 💛 품번 0216
곰탕·부대찌개에 사리로 넣기 좋아요.

✔ 29일(일) 서울 아침 영하 2도, 낮 8도로 주말 기온 뚝

※ 날씨: 기상청 예보(이투데이·파이낸셜뉴스 11/26, SBS 11/27)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #국물요리 #사골곰탕 #부대찌개 #우동""",
    "products": [prod(1, GOM, N_GOM, "C", "0214"), prod(2, BUDAE, N_BUDAE, "C", "0215"), prod(3, UDON, N_UDON, "C", "0216")],
})

write(DATE, "C2", [
    c_cover("딸기값 작년보다 ↓ 🍓", "실컷 먹자", "딸기 세트", "BEST3", [BERRY, MILK, YOG]),
    c_prod(1, "0217", BERRY, "설향 딸기<br>대과", ["하동품애 한단 설향", "GAP 인증", "큼직한 대과"],
           ["💰 1만원대", "📦 대과"]),
    c_prod(2, "0218", MILK, "연유<br>튜브형", ["서울우유 연유", "200g 튜브형", "딸기 찍어 먹기"],
           ["💰 3천원대", "📦 200g"]),
    c_prod(3, "0219", YOG, "그릭요거트<br>플레인", ["매일바이오", "무가당 플레인", "딸기 올려 한 그릇"],
           ["💰 3천원대", "📦 무가당"]),
    c_howto("0217~0219"),
], {
    "title": "딸기 실컷 먹기 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

딸기값 작년보다 내렸어요 🍓 실컷 먹자 딸기 세트 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 하동품애 GAP 한단 설향 딸기 대과 💛 품번 0217
큼직한 설향 대과, 씻어서 바로.

2. 서울우유 연유 200g 튜브형 💛 품번 0218
튜브형이라 딸기에 쭉 짜서 찍먹.

3. 매일바이오 그릭요거트 무가당 플레인 💛 품번 0219
딸기 썰어 올리면 간단한 디저트.

✔ 가락시장 딸기 2kg 평균 경락가 4만4267원, 작년 11월보다 18.6% 낮아요

※ 물가: aT·한국농촌경제연구원(한국경제·서울경제 11/25)
※ {NOTE}

#광고 #쿠팡추천템 #식품 #딸기 #연유 #그릭요거트 #겨울과일""",
    "products": [prod(1, BERRY, N_BERRY, "C", "0217"), prod(2, MILK, N_MILK, "C", "0218"), prod(3, YOG, N_YOG, "C", "0219")],
})
print("ok")
