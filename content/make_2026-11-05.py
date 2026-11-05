"""2026-11-05(목, 생활용품의 날) 게시물 6개 → docs/posts/2026-11-05/{A,B,C,A2,B2,C2}
점심: 비 그친 뒤 기온 뚝·입동 아침 -4도·보온템 / 퇴근길: 배추·무 풍년 김장·김장 도구
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-05"
DL = "2026.11.05 (목)"
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





HOT, BAG, TUM = "9389565227", "9682116990", "9131039021"
MAT, GLV, BOX = "9779540438", "6199242647", "7115546499"
N_HOT = "쏘핫 장시간 프리미엄 붙이는 핫팩"
N_BAG = "ZOZI 손넣는 퍼커버 2L 온수찜질팩 물주머니"
N_TUM = "DS 액정 온도 표시 원터치 진공 스테인리스 텀블러"
N_MAT = "키친9단 국산 무봉제 원형 접이식 김장매트"
N_GLV = "모스트픽 기모안감 목 긴 고무장갑 3개 세트"
N_BOX = "까사베니 연마제 없는 스테인레스 김치통"

# ═════════ A · 점심 12:00 — 비 그친 뒤 기온 뚝·입동 영하 ═════════
SRC1 = "출처: 재경일보(11/5)·뉴스1(11/4), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 오늘~주말</div>
<h1>비 그치면<br>기온 <span class="hl">5~8도 뚝</span></h1>
<p class="lead">입동(7일) 아침 최저 -4도<br>찬 바람까지 강하게</p>""", SRC1, DL),
    a_slide(2, n, """<h2>사흘 기온 한눈에</h2>
<div class="fig"><div><small>5일(목) 낮</small><strong>12~20도</strong></div><div><small>6일(금) 아침</small><strong>1~11도</strong></div></div>
<div class="fig"><div><small>7일(토) 아침</small><strong>-4~5도</strong></div><div><small>7일 낮</small><strong>8~14도</strong></div></div>
<div class="box">수도권 6일 아침은 오늘보다<br><b class="hl">5~8도 낮아질 전망</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>바람이 <span class="hl">체감 추위</span>를 키워요</h2>
<div class="fig"><div><small>순간풍속(6~7일 오전)</small><strong>55km/h</strong></div><div><small>산지</small><strong>70km/h</strong></div></div>
<div class="box">중부·전북 동부·경상 내륙<br>7일 아침 <b class="hl">영하권</b><br>낮밤 기온 차도 크게 벌어져요</div>""", SRC1, DL),
    a_slide(4, n, """<h2>입동 추위 <span class="hl">미리 준비</span></h2>
<ul class="chk"><li>오늘은 오후까지 <span class="hl">우산</span></li><li>내일부터 두꺼운 외투·목도리</li><li>출근길엔 <span class="hl">붙이는 핫팩</span></li><li>따뜻한 물은 텀블러에 담아 가기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>입동 추위 <span class="hl">보온템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(HOT)}"><div>쏘핫 붙이는 핫팩<span>장시간 · 옷 안쪽에 붙이는 타입</span></div></li>
<li><b>2</b><img src="{img(BAG)}"><div>ZOZI 보온 물주머니 2L<span>손 넣는 퍼커버 · 찜질 겸용</span></div></li>
<li><b>3</b><img src="{img(TUM)}"><div>DS 온도표시 진공 텀블러<span>뚜껑에 온도 표시 · 원터치</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/5 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "비 그친 뒤 기온 뚝·입동 -4도",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 비 그치면 기온 5~8도 뚝, 입동(7일) 아침엔 -4도 🥶

· 5일(목) 전국 비, 오후에 대부분 그칠 전망 — 낮 12~20도
· 6일(금) 아침 1~11도, 낮 8~16도 — 수도권 아침은 5일보다 5~8도 낮아질 전망
· 7일(토, 입동) 아침 -4~5도, 낮 8~14도 — 중부·전북 동부·경상 내륙 중심 영하권
· 6일~7일 오전 순간풍속 시속 55km 안팎(산지 70km 안팎) — 체감 추위는 더 클 수 있어요

✔ 오늘은 우산, 내일부터는 두꺼운 외투·목도리 챙기기

🔗 입동 추위 보온템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 재경일보(11/5)·뉴스1(11/4) — 기상청 예보

#광고 #생활뉴스 #날씨 #입동 #기온뚝 #핫팩 #물주머니 #보온텀블러""",
    "products": [prod(1, HOT, N_HOT, "A"), prod(2, BAG, N_BAG, "A"), prod(3, TUM, N_TUM, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 배추·무 풍년, 김장 ═════════
SRC2 = "출처: 아주경제·파이낸셜뉴스(11/3), 농식품부·한국농촌경제연구원"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 김장철</div>
<h1>올해 배추·무<br><span class="hl">풍년</span><br>김장 부담 ↓</h1>
<p class="lead">배추·무 도매가격<br>평년보다 37%·32% 낮아</p>""", SRC2, DL),
    a_slide(2, n, """<h2>숫자로 보는 김장철</h2>
<div class="fig"><div><small>가을배추 생산</small><strong>18.5%↑</strong></div><div><small>가을무 생산</small><strong>11.1%↑</strong></div></div>
<div class="fig"><div><small>배추 도매가(평년比)</small><strong>37%↓</strong></div><div><small>무 도매가(평년比)</small><strong>32%↓</strong></div></div>
<div class="box">가을배추 <b class="hl">121만4천t</b> 전망<br>양호한 날씨로 작황 개선</div>""", SRC2, DL),
    a_slide(3, n, """<h2>김장 재료 <span class="hl">할인</span>도</h2>
<div class="fig"><div><small>농산물 할인</small><strong>최대 40%</strong></div><div><small>천일염·새우젓 등</small><strong>최대 50%</strong></div></div>
<div class="box">역대 최대 <b class="hl">640억 원</b> 할인 지원<br>할인 매장·1인 한도는 매장마다 달라요</div>""", SRC2, DL),
    a_slide(4, n, """<h2>직접 담그는 집 <span class="hl">58.6%</span></h2>
<div class="box">작년 64.2%보다 5.6%p 줄었지만<br>4인 가구 김장 규모는<br><b class="hl">23.4포기</b>로 작년과 비슷</div>
<ul class="chk"><li>매트·장갑·김치통 미리 꺼내 보기</li><li>할인 기간 확인하고 장보기</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>김장날 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(MAT)}"><div>키친9단 원형 김장매트<span>국산 · 무봉제 · 접이식</span></div></li>
<li><b>2</b><img src="{img(GLV)}"><div>모스트픽 기모 고무장갑<span>목 긴 밴드형 · 3개 세트</span></div></li>
<li><b>3</b><img src="{img(BOX)}"><div>까사베니 스텐 김치통<span>연마제 없는 스테인리스</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/5 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "배추·무 풍년·김장 부담↓",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 올해 배추·무 풍년, 김장 부담 덜어요 🥬

· 가을배추 생산 121만4천t 전망 — 작년보다 18.5%↑, 가을무 37만2천t으로 11.1%↑
· 배추·무 도매가격은 평년보다 각각 37%, 32% 낮은 수준
· 김장 재료 할인에 역대 최대 640억 원 — 농산물 최대 40%, 천일염·새우젓 등 수산물 최대 50%
· 직접 담그겠다는 가구 58.6%(작년 64.2%), 4인 가구 김장 규모는 23.4포기로 작년과 비슷

✔ 할인 매장·기간·1인 한도는 매장마다 다르니 확인하고 장보기

🔗 김장날 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 아주경제·파이낸셜뉴스(11/3) — 농림축산식품부·해양수산부·한국농촌경제연구원

#광고 #생활뉴스 #김장 #김장철 #배추 #김장매트 #고무장갑 #김치통""",
    "products": [prod(1, MAT, N_MAT, "A"), prod(2, GLV, N_GLV, "A"), prod(3, BOX, N_BOX, "A")],
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


write(DATE, "B", [poll("기온 뚝 떨어진 밤,<br>나의 보온법은? 🛌", "7일(입동) 아침 -4~5도 (기상청 예보)",
                       [("보일러 풀가동", "가스비는 내일의 나에게"), ("양말 신고 잠", "발만 따뜻하면 돼"),
                        ("이불 두 겹", "무거워도 포근하게"), ("뜨끈한 물주머니", "품에 안고 바로 꿀잠")], BAG)], {
    "title": "추운 밤 보온법 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 기온 뚝 떨어진 밤, 나의 보온법은? 🛌
댓글에 번호로 투표해주세요!

1️⃣ 보일러 풀가동
2️⃣ 양말 신고 잠
3️⃣ 이불 두 겹
4️⃣ 뜨끈한 물주머니

※ 6일 수도권 아침 5일보다 5~8도↓, 7일(입동) 아침 -4~5도 (기상청 예보)

🔗 4번 ZOZI 보온 물주머니 링크는 프로필에
👥 겨울만 되면 발 시린 친구 태그

#광고 #투표 #공감 #입동 #추위 #물주머니""",
    "products": [prod(1, BAG, N_BAG, "B")],
})

write(DATE, "B2", [poll("김장하는 날,<br>나의 포지션은? 🥬", "배추·무 도매가 평년보다 37%·32%↓",
                        [("배추 절이기", "새벽부터 소금 담당"), ("속 버무리기", "손맛은 내가 책임"),
                         ("수육 담당", "김장은 핑계, 수육이 본업"), ("매트 깔고 총지휘", "판은 내가 깐다")], MAT)], {
    "title": "김장 포지션 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 김장하는 날, 나의 포지션은? 🥬
댓글에 번호로 투표해주세요!

1️⃣ 배추 절이기
2️⃣ 속 버무리기
3️⃣ 수육 담당
4️⃣ 매트 깔고 총지휘

※ 올해 배추·무 도매가격 평년보다 각각 37%·32% 낮은 수준 (아주경제 11/3, 농식품부)

🔗 4번 키친9단 원형 김장매트 링크는 프로필에
👥 김장날 수육만 먹고 가는 친구 태그

#광고 #투표 #공감 #김장 #김장철 #김장매트""",
    "products": [prod(1, MAT, N_MAT, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/5 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("입동 아침 -4도", "출근길 추위", "보온템", "BEST3", [HOT, BAG, TUM]),
    c_prod(1, "0082", HOT, "쏘핫<br>붙이는 핫팩", ["옷 안쪽에 붙이는 타입", "장시간 발열", "출근길·야외 대기용"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0083", BAG, "ZOZI<br>보온 물주머니 2L", ["손 넣는 퍼커버", "온수 찜질팩 겸용", "잘 때 품에 쏙"],
           ["💰 1만원 이하", "🚀 로켓배송"]),
    c_prod(3, "0084", TUM, "DS 온도표시<br>진공 텀블러", ["뚜껑에 온도 액정 표시", "원터치 진공 스테인리스", "따뜻한 물 들고 출근"],
           ["💰 1만원 이하", "📦 무료배송"]),
    c_howto("0082~0084"),
], {
    "title": "입동 보온템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

입동 아침 -4도 🥶 출근길 추위 보온템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 쏘핫 장시간 프리미엄 붙이는 핫팩 💛 품번 0082
옷 안쪽에 붙여 쓰는 핫팩, 출근길·야외 대기용.

2. ZOZI 손넣는 퍼커버 2L 물주머니 💛 품번 0083
따뜻한 물 담아 손 넣고, 잘 때는 품에.

3. DS 액정 온도 표시 진공 텀블러 💛 품번 0084
뚜껑에 온도가 보이는 원터치 텀블러.

※ 날씨: 기상청 예보(재경일보 11/5·뉴스1 11/4 보도)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #생활템 #핫팩 #물주머니 #보온텀블러 #입동""",
    "products": [prod(1, HOT, N_HOT, "C", "0082"), prod(2, BAG, N_BAG, "C", "0083"), prod(3, TUM, N_TUM, "C", "0084")],
})

write(DATE, "C2", [
    c_cover("배추·무 풍년", "김장날", "생활템", "BEST3", [MAT, GLV, BOX]),
    c_prod(1, "0085", MAT, "키친9단<br>원형 김장매트", ["국산 무봉제", "접이식 원형", "배추 절임·버무리기"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0086", GLV, "모스트픽<br>기모 고무장갑", ["기모 안감", "목 긴 밴드형", "3개 세트"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0087", BOX, "까사베니<br>스텐 김치통", ["연마제 없는 스테인리스", "김장 후 소분 보관", "김치·반찬 보관"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_howto("0085~0087"),
], {
    "title": "김장날 생활템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

배추·무 풍년 🥬 김장날 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 키친9단 국산 무봉제 원형 접이식 김장매트 💛 품번 0085
배추 절이고 속 버무릴 때 펼치는 원형 매트.

2. 모스트픽 기모안감 목 긴 고무장갑 3개 💛 품번 0086
기모 안감에 목이 긴 밴드형 고무장갑 3개 세트.

3. 까사베니 연마제 없는 스테인레스 김치통 💛 품번 0087
김장 끝나고 소분해 두는 스텐 김치통.

※ 김장철: 배추·무 도매가 평년보다 37%·32%↓(아주경제 11/3, 농식품부)
※ {NOTE}

#광고 #쿠팡추천템 #생활용품 #생활템 #김장 #김장매트 #고무장갑 #김치통""",
    "products": [prod(1, MAT, N_MAT, "C", "0085"), prod(2, GLV, N_GLV, "C", "0086"), prod(3, BOX, N_BOX, "C", "0087")],
})
print("ok")
