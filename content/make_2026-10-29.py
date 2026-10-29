"""2026-10-29(목, 생활용품의 날) 게시물 6개 → docs/posts/2026-10-29/{A,B,C,A2,B2,C2}
점심: 아침 최저 0도·오후부터 비(수도권 최대 20mm) / 퇴근길: 주말 날씨·다음 주 초 또 기온 뚝 → 겨울옷 꺼내기
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-10-29"
DL = "2026.10.29 (목)"
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


UMB, DRY, STAND = "9474468616", "9626026172", "216551398"
LINT, HANG, WASH = "4947594003", "6643638905", "2322706995"
N_UMB, N_DRY, N_STAND = "솔리앤 초경량 UV차단 3단 자동우산", "서프라이즈 신발용 진짜 좋은 제습제 8p", "리템 자석형 우산꽂이"
N_LINT, N_HANG, N_WASH = "필립스 보풀제거기", "코멧 홈 어깨 뿔 방지 논슬립 옷걸이", "쉬슬러 구스다운워시 전용 액상세제 650ml"

# ═════════ A · 점심 12:00 — 오후부터 비 ═════════
SRC1 = "출처: 세계일보·뉴스1(10/29, 기상청 예보)"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 퇴근길 비</div>
<h1>아침 최저 0도,<br><span class="hl">오후부터 비</span><br>우산 챙기세요</h1>
<p class="lead">수도권 북부·강원 영서부터 시작<br>밤엔 충청·전북 서부까지 확대</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘 아침 · 낮 기온</h2>
<div class="fig"><div><small>서울</small><strong>5 / 13도</strong></div><div><small>춘천</small><strong>1 / 13도</strong></div></div>
<div class="fig"><div><small>대전</small><strong>1 / 15도</strong></div><div><small>부산</small><strong>8 / 18도</strong></div></div>
<div class="box">내륙 일교차 <b class="hl">10~15도</b><br>강원·충북·경북 내륙 아침 영하권</div>""", SRC1, DL),
    a_slide(3, n, """<h2>예상 강수량 (29~30일)</h2>
<div class="fig"><div><small>인천·경기 북부</small><strong>5~20mm</strong></div><div><small>서울·경기 남부</small><strong>5~10mm</strong></div></div>
<div class="box">중부는 30일 <b class="hl">새벽</b>,<br>남부·제주는 30일 <b class="hl">오전</b> 대부분 그쳐요</div>""", SRC1, DL),
    a_slide(4, n, """<h2>퇴근길 비 체크</h2>
<ul class="chk"><li>출근 땐 맑아도 우산 챙기기</li><li>중부 서해안 <span class="hl">돌풍·천둥·번개</span></li><li>젖은 신발은 그날 바로 말리기</li><li>빗길 가시거리↓ · 미끄럼 주의</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>퇴근길 비 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(UMB)}"><div>솔리앤 3단 자동우산<span>초경량 · UV차단</span></div></li>
<li><b>2</b><img src="{img(DRY)}"><div>서프라이즈 신발 제습제<span>8p · 신발 속에 쏙</span></div></li>
<li><b>3</b><img src="{img(STAND)}"><div>리템 자석형 우산꽂이<span>현관문에 착 붙이는 거치대</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/29 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "아침 0도·오후부터 비",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 아침 최저 0도, 오후부터 비 — 퇴근길 우산 챙기세요 ☔

· 아침 0~9도, 낮 13~19도 (서울 5/13, 춘천 1/13, 대전 1/15, 부산 8/18)
· 강원 내륙·산지, 충북, 경북 내륙 아침 영하권 · 내륙 일교차 10~15도
· 오후 수도권 북부·강원 영서 중북부부터 비 → 밤엔 수도권·충청·전북 서부 등으로 확대
· 예상 강수량: 인천·경기 북부 5~20mm, 서울·경기 남부 5~10mm
· 중부 30일 새벽, 남부·제주 30일 오전 대부분 그쳐요
· 중부 서해안 돌풍·천둥·번개 가능, 빗길 미끄럼 주의

✔ 출근 땐 맑아도 우산 챙기기, 젖은 신발은 그날 바로 말리기

🔗 퇴근길 비 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 세계일보(10/29), 뉴스1(10/29) — 기상청 예보

#광고 #생활뉴스 #날씨 #가을비 #퇴근길 #우산 #일교차 #생활템""",
    "products": [prod(1, UMB, N_UMB, "A"), prod(2, DRY, N_DRY, "A"), prod(3, STAND, N_STAND, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 다음 주 초 또 기온 뚝 → 겨울옷 꺼내기 ═════════
SRC2 = "출처: 뉴스1(10/28, 기상청 예보)"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 주말</div>
<h1>다음 주 초<br><span class="hl">또 기온 뚝</span><br>겨울옷 꺼낼 때</h1>
<p class="lead">금요일 추위 누그러지고<br>토요일은 맑을 전망</p>""", SRC2, DL),
    a_slide(2, n, """<h2>주말 날씨 흐름</h2>
<div class="fig"><div><small>금 (30일)</small><strong>누그러짐</strong></div><div><small>토 (31일)</small><strong>맑음</strong></div></div>
<div class="fig"><div><small>일 (1일)</small><strong>오후 비</strong></div><div><small>다음 주 초</small><strong>또 뚝</strong></div></div>
<div class="box">맑은 <b class="hl">토요일</b>이<br>겨울옷 꺼내 정리하기 좋아요</div>""", SRC2, DL),
    a_slide(3, n, """<h2>겨울옷 꺼낼 때 체크</h2>
<ul class="chk"><li>니트 보풀부터 정리</li><li>니트는 어깨 늘어나지 않게 걸기</li><li>패딩은 세탁 라벨 먼저 확인</li><li>맑은 날 바람 통하게 널어 두기</li></ul>""", "", DL),
    a_slide(4, n, f"""<h2>겨울옷 정리 <span class="hl">생활템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(LINT)}"><div>필립스 보풀제거기<span>니트·코트 보풀 정리</span></div></li>
<li><b>2</b><img src="{img(HANG)}"><div>코멧 홈 논슬립 옷걸이<span>어깨 뿔 방지 형태</span></div></li>
<li><b>3</b><img src="{img(WASH)}"><div>쉬슬러 구스다운워시<span>패딩 전용 액상세제 650ml</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/29 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "다음 주 초 또 기온 뚝",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 다음 주 초 또 기온 뚝 — 맑은 토요일, 겨울옷 꺼내 두세요 🧥

· 오늘 아침 영하권 추위, 금요일(30일)엔 추위 누그러져요
· 토요일(31일) 맑음, 일요일(1일) 오후 전국 비
· 다음 주 초 다시 기온이 크게 떨어질 전망

✔ 겨울옷 꺼낼 때: 니트 보풀 정리, 어깨 늘어나지 않게 걸기, 패딩은 세탁 라벨 먼저 확인, 맑은 날 바람 통하게 널기

🔗 겨울옷 정리 생활템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 뉴스1(10/28) — 기상청 예보

#광고 #생활뉴스 #주말날씨 #겨울옷 #옷정리 #보풀제거 #패딩세탁 #생활템""",
    "products": [prod(1, LINT, N_LINT, "A"), prod(2, HANG, N_HANG, "A"), prod(3, WASH, N_WASH, "A")],
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


write(DATE, "B", [poll("퇴근길에 비 오면<br>나는 어떻게 함? ☔", "오늘 오후부터 비 · 서울 5~10mm (기상청 예보)",
                       [("편의점 우산 또 구매", "집에 우산만 n개"), ("그냥 맞고 뛴다", "이 정도는 괜찮아"),
                        ("그칠 때까지 버틴다", "회사 로비 대기"), ("가방 속 3단 우산", "늘 들고 다니는 편")], UMB)], {
    "title": "퇴근길 비 우산 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 퇴근길에 비 오면 나는 어떻게 함? ☔
댓글에 번호로 투표해주세요!

1️⃣ 편의점 우산 또 구매
2️⃣ 그냥 맞고 뛴다
3️⃣ 그칠 때까지 버틴다
4️⃣ 가방 속 3단 우산

🔗 4번 3단 자동우산 링크는 프로필에
👥 집에 우산 제일 많은 친구 태그

#광고 #투표 #공감 #가을비 #퇴근길 #우산 #직장인""",
    "products": [prod(1, UMB, N_UMB, "B")],
})

write(DATE, "B2", [poll("겨울옷 꺼냈을 때<br>제일 먼저 보이는 건? 🧥", "다음 주 초 또 기온 뚝 (기상청 예보)",
                        [("작년에 못 지운 얼룩", "세탁소 갈 걸…"), ("어깨 뿔난 니트", "옷걸이 자국 그대로"),
                         ("납작해진 패딩", "숨 죽은 볼륨"), ("보풀 가득한 니트", "한 시즌 만에 이렇게?")], LINT)], {
    "title": "겨울옷 꺼내기 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 겨울옷 꺼냈을 때 제일 먼저 보이는 건? 🧥
댓글에 번호로 투표해주세요!

1️⃣ 작년에 못 지운 얼룩
2️⃣ 어깨 뿔난 니트
3️⃣ 납작해진 패딩
4️⃣ 보풀 가득한 니트

🔗 4번 보풀제거기 링크는 프로필에
👥 옷장 정리 미뤄둔 친구 태그

#광고 #투표 #공감 #겨울옷 #옷장정리 #보풀 #니트""",
    "products": [prod(1, LINT, N_LINT, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/29 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("오늘 오후부터 비", "퇴근길 비 올 때", "생활템", "BEST3", [UMB, DRY, STAND]),
    c_prod(1, "0040", UMB, "솔리앤<br>초경량 3단 자동우산", ["자동으로 펴지는 3단 우산", "초경량 접이식", "UV차단 · 가방 속 상비용"],
           ["💰 6천원대", "🚚 무료배송"]),
    c_prod(2, "0041", DRY, "서프라이즈<br>신발용 제습제 8p", ["젖은 신발 속에 넣어 두기", "8개입 · 총 640g", "신발장 습기 관리"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0042", STAND, "리템<br>자석형 우산꽂이", ["현관문에 자석으로 부착", "바닥 공간 차지 없이", "젖은 우산 바로 걸기"],
           ["💰 5천원대", "🚀 로켓배송"]),
    c_howto("0040~0042"),
], {
    "title": "퇴근길 비 생활템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

오늘 오후부터 비 ☔ 퇴근길 비 올 때 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 솔리앤 초경량 UV차단 3단 자동우산 💛 품번 0040
가방 속에 넣어 두는 가벼운 3단 자동우산.

2. 서프라이즈 신발용 제습제 8p 💛 품번 0041
젖은 신발 속에 넣어 두는 제습제.

3. 리템 자석형 우산꽂이 💛 품번 0042
현관문에 자석으로 붙이는 우산 거치대.

※ {NOTE}

#광고 #쿠팡추천템 #생활템 #가을비 #자동우산 #신발제습제 #우산꽂이 #퇴근길""",
    "products": [prod(1, UMB, N_UMB, "C", "0040"), prod(2, DRY, N_DRY, "C", "0041"), prod(3, STAND, N_STAND, "C", "0042")],
})

write(DATE, "C2", [
    c_cover("다음 주 초 또 기온 뚝", "겨울옷 꺼낼 때", "정리 생활템", "BEST3", [LINT, HANG, WASH]),
    c_prod(1, "0043", LINT, "필립스<br>보풀제거기", ["니트·코트 보풀 정리", "손에 쥐는 소형", "꺼낸 겨울옷 첫 손질"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(2, "0044", HANG, "코멧 홈<br>어깨 뿔 방지 논슬립 옷걸이", ["어깨 뿔 방지 형태", "논슬립 · 옷 흘러내림 방지", "니트·셔츠 걸어두기"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0045", WASH, "쉬슬러<br>구스다운워시 650ml", ["구스다운 전용 액상세제", "650ml 본품", "집에서 패딩 세탁할 때"],
           ["💰 1만원대", "🚚 무료배송"]),
    c_howto("0043~0045"),
], {
    "title": "겨울옷 정리 생활템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

다음 주 초 또 기온 뚝 🧥 겨울옷 꺼낼 때 정리 생활템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 필립스 보풀제거기 💛 품번 0043
꺼낸 니트·코트 보풀 정리용.

2. 코멧 홈 어깨 뿔 방지 논슬립 옷걸이 💛 품번 0044
어깨 뿔 방지 형태, 옷이 흘러내리지 않는 논슬립.

3. 쉬슬러 구스다운워시 전용 액상세제 650ml 💛 품번 0045
집에서 패딩 세탁할 때 쓰는 구스다운 전용 세제.

※ {NOTE}

#광고 #쿠팡추천템 #생활템 #겨울옷 #보풀제거기 #논슬립옷걸이 #패딩세탁 #옷장정리""",
    "products": [prod(1, LINT, N_LINT, "C", "0043"), prod(2, HANG, N_HANG, "C", "0044"), prod(3, WASH, N_WASH, "C", "0045")],
})
print("ok")
