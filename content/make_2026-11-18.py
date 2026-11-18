"""2026-11-18(수, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-18/{A,B,C,A2,B2,C2}
점심: 6년 만의 수능 한파(19일 아침 서울 영하 1도) → 방한 특이템 / 퇴근길: 독감 3주 연속 증가(질병청) → 손 씻기·실내 특이템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-18"
DL = "2026.11.18 (수)"
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


EAR, NECK, GLOVE = "8409328867", "8354669597", "9739268745"
SOAP, MIST, TREE = "8837251876", "7821938293", "245831112"
N_EAR = "지빈 남녀공용 방한 끈없는 귀덮개"
N_NECK = "몬타라 두꺼운 기모 넥워머"
N_GLOVE = "윈터블락 기모 스마트폰 터치 방한 장갑"
N_SOAP = "미홀 타입C 충전식 자동 거품 손세정기 600ml"
N_MIST = "신지모루 테이블 미스트 USB 무드등 미니 가습기 600ml"
N_TREE = "나눔 프로젝트 하트 트리 종이 가습기 (자연기화식)"

# ═════════ A · 점심 12:00 — 6년 만의 수능 한파 ═════════
SRC1 = "출처: 경향신문·이투데이(11/17) — 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">생활 · 내일 날씨</div>
<h1>6년 만의<br><span class="hl">수능 한파</span></h1>
<p class="lead">19일(목) 아침<br>서울 영하 1도</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(18일) <span class="hl">비·눈</span></h2>
<ul class="chk"><li>낮부터 전국 곳곳 <span class="hl">비 또는 눈</span></li><li>강원 내륙·충북·경북 일부 <span class="hl">눈</span>으로</li><li>강원 일부 적설 <span class="hl">1cm 내외</span></li><li>비 그친 뒤 찬 바람, 기온 급락</li></ul>""", SRC1, DL),
    a_slide(3, n, """<h2>수능날 <span class="hl">아침 기온</span></h2>
<div class="fig"><div><small>19일 아침 최저</small><strong>-4~6도</strong></div><div><small>낮 최고</small><strong>3~10도</strong></div></div>
<div class="box">서울 <b class="hl">-1도</b> · 춘천 -2도 · 대전 0도</div>
<div class="box">전날보다 최대 <b class="hl">10도가량</b> 낮아요</div>""", SRC1, DL),
    a_slide(4, n, """<h2>체감은 <span class="hl">더 추워요</span></h2>
<div class="box">체감온도는 기온보다 <b class="hl">3도가량</b> 낮고<br>중부는 <b class="hl">영하 5도 안팎</b></div>
<ul class="chk"><li>목도리·장갑, <span class="hl">얇은 옷 여러 겹</span></li><li>살얼음 대비 <span class="hl">일찍 출발</span></li><li>시험 끝난 저녁엔 더 추워요</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>수능날 챙길 <span class="hl">방한 특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(EAR)}"><div>끈없는 귀덮개<span>머리띠 없이 귀에 쏙</span></div></li>
<li><b>2</b><img src="{img(NECK)}"><div>두꺼운 기모 넥워머<span>목도리 대신 쏙</span></div></li>
<li><b>3</b><img src="{img(GLOVE)}"><div>스마트폰 터치 장갑<span>기모 · 낀 채로 터치</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/18 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "6년 만의 수능 한파",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 6년 만의 '수능 한파' 🥶 19일(목) 아침 서울 영하 1도

· 18일(수) 낮부터 전국 곳곳 비 또는 눈, 강원 내륙·충북·경북 일부는 눈(강원 일부 1cm 내외)
· 비 그친 뒤 북서쪽 찬 바람, 기온 큰 폭으로 하락
· 19일(목) 아침 최저 영하 4도~영상 6도, 낮 최고 3~10도 — 전날보다 최대 10도가량 낮아요
· 서울 영하 1도, 춘천 영하 2도, 대전·청주 0도, 부산 3도, 광주 4도
· 체감온도는 기온보다 3도가량 낮고 중부는 영하 5도 안팎
· 서울 수능일 아침 영하는 2020년 이후 처음

✔ 목도리·장갑 챙기고 얇은 옷 여러 겹
✔ 도로 살얼음 대비 평소보다 일찍 출발
✔ 시험 끝난 저녁엔 기온이 더 떨어져요

수험생 여러분 모두 응원합니다 💪

🔗 수능날 방한 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 경향신문(2026.11.17)·이투데이(2026.11.17) — 기상청 예보

#광고 #생활뉴스 #날씨 #수능한파 #수능 #방한템 #넥워머""",
    "products": [prod(1, EAR, N_EAR, "A"), prod(2, NECK, N_NECK, "A"), prod(3, GLOVE, N_GLOVE, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 독감 3주 연속 증가 ═════════
SRC2 = "출처: 국제뉴스(11/16)·FAM타임스(11/17) — 질병관리청"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 건강</div>
<h1>독감 환자<br><span class="hl">3주 연속 증가</span></h1>
<p class="lead">외래 1000명당<br>28.9명</p>""", SRC2, DL),
    a_slide(2, n, """<h2>독감 <span class="hl">의사환자</span> 분율</h2>
<div class="fig"><div><small>11월 1~7일</small><strong>28.9명</strong></div><div><small>한 주 전</small><strong>22.8명</strong></div></div>
<div class="box">올 절기 유행기준 <b class="hl">12.9명</b>의<br>약 2.2배 수준</div>""", SRC2, DL),
    a_slide(3, n, """<h2><span class="hl">학생</span> 중심 확산</h2>
<div class="fig"><div><small>7~12세</small><strong>73.5명</strong></div><div><small>13~18세</small><strong>52.2명</strong></div></div>
<div class="box">13~18세는 한 주 새 <b class="hl">39.6%</b> 늘어<br>전 연령 중 증가율 최대</div>""", SRC2, DL),
    a_slide(4, n, """<h2>질병청 <span class="hl">예방 수칙</span></h2>
<ul class="chk"><li>자주 <span class="hl">손 씻기</span></li><li><span class="hl">기침 예절</span> 지키기</li><li>주기적으로 <span class="hl">실내 환기</span></li><li>증상 있으면 마스크 쓰고 진료</li><li>어르신·어린이는 예방접종</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>집에서 쓰는 <span class="hl">겨울 특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SOAP)}"><div>자동 거품 손세정기<span>손 대면 거품이 쏙</span></div></li>
<li><b>2</b><img src="{img(MIST)}"><div>무드등 미니 가습기<span>USB · 600ml</span></div></li>
<li><b>3</b><img src="{img(TREE)}"><div>트리 종이 가습기<span>전기 없이 자연기화</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/18 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "독감 환자 3주 연속 증가",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 독감 환자 3주 연속 증가 🤧 외래 1000명당 28.9명

· 11월 1~7일 인플루엔자 의사환자 분율 28.9명(외래 1000명당) — 한 주 전 22.8명
· 올 절기 유행기준(12.9명)의 약 2.2배
· 7~12세 73.5명, 13~18세 52.2명 — 13~18세는 한 주 새 39.6% 늘어 증가율 최대

질병관리청 예방 수칙
✔ 자주 손 씻기, 기침 예절 지키기
✔ 주기적으로 실내 환기
✔ 발열·기침이 있으면 마스크 쓰고 의료기관 진료
✔ 어르신·어린이·임신부는 예방접종

🔗 집에서 쓰는 겨울 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 특이템은 @0315_pick

출처: 국제뉴스(2026.11.16)·FAM타임스(2026.11.17) — 질병관리청 감시 자료

#광고 #생활뉴스 #독감 #인플루엔자 #손씻기 #손세정기 #가습기""",
    "products": [prod(1, SOAP, N_SOAP, "A"), prod(2, MIST, N_MIST, "A"), prod(3, TREE, N_TREE, "A")],
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


write(DATE, "B", [poll("수능 한파 아침,<br>제일 먼저 챙길 건? 🥶", "19일 아침 서울 영하 1도 · 6년 만의 수능 한파",
                       [("롱패딩 하나면 끝", "무릎까지 덮어야 안심"), ("핫팩 양손에 하나씩", "주머니 속 난로"),
                        ("목도리 칭칭", "목만 따뜻해도 다름"), ("귀덮개", "귀가 제일 먼저 얼어요")], EAR)], {
    "title": "수능 한파 방한템 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 수능 한파 아침, 제일 먼저 챙길 건? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 롱패딩 하나면 끝
2️⃣ 핫팩 양손에 하나씩
3️⃣ 목도리 칭칭
4️⃣ 귀덮개

※ 19일(목) 아침 서울 영하 1도, 서울 수능일 아침 영하는 2020년 이후 처음 (기상청 예보, 경향신문 11/17)

🔗 4번 끈없는 귀덮개 링크는 프로필에
👥 내일 수능 보는 친구 태그하고 응원 한마디 💪

#광고 #투표 #공감 #수능 #수능한파 #방한템""",
    "products": [prod(1, EAR, N_EAR, "B")],
})

write(DATE, "B2", [poll("밖에서 들어오면<br>손 씻기, 솔직히? 🧼", "독감 3주 연속 증가 · 질병청 \"자주 손 씻기\"",
                        [("현관 들어서자마자", "신발 벗고 바로 직행"), ("밥 먹기 전에만", "그때는 꼭 씻어요"),
                         ("생각날 때", "물만 묻히는 날도"), ("자동 거품기 생기면", "손 대면 거품 쏙")], SOAP)], {
    "title": "손 씻기 습관 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 밖에서 들어오면 손 씻기, 솔직히? 🧼
댓글에 번호로 투표해주세요!

1️⃣ 현관 들어서자마자
2️⃣ 밥 먹기 전에만
3️⃣ 생각날 때
4️⃣ 자동 거품기 생기면

※ 인플루엔자 의사환자 3주 연속 증가, 11월 1~7일 외래 1000명당 28.9명 (질병관리청, 국제뉴스 11/16)

🔗 4번 자동 거품 손세정기 링크는 프로필에
👥 손 안 씻는 친구 태그

#광고 #투표 #공감 #손씻기 #독감 #손세정기""",
    "products": [prod(1, SOAP, N_SOAP, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/18 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("6년 만의 수능 한파 🥶", "칼바람 막는", "방한 특이템", "BEST3", [EAR, NECK, GLOVE]),
    c_prod(1, "0160", EAR, "끈없는<br>귀덮개", ["머리띠 없는 귀덮개", "귀에 끼우기만", "모자·후드와 함께 OK"],
           ["💰 1만원대", "📦 남녀공용"]),
    c_prod(2, "0161", NECK, "두꺼운<br>기모 넥워머", ["두꺼운 기모 안감", "목에 쏙 끼우는 타입", "목도리보다 간편"],
           ["💰 8천원대", "📦 남녀공용"]),
    c_prod(3, "0162", GLOVE, "스마트폰<br>터치 장갑", ["기모 방한 장갑", "낀 채로 화면 터치", "남녀공용"],
           ["💰 2만원대", "📦 남녀공용"]),
    c_howto("0160~0162"),
], {
    "title": "방한 특이템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

6년 만의 수능 한파 🥶 칼바람 막는 방한 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 지빈 남녀공용 방한 끈없는 귀덮개 💛 품번 0160
머리띠 없이 귀에 끼우는 귀덮개, 모자·후드와 함께 쓰기 좋아요.

2. 몬타라 두꺼운 기모 넥워머 💛 품번 0161
두꺼운 기모 안감 넥워머, 목도리보다 간편하게.

3. 윈터블락 기모 스마트폰 터치 방한 장갑 💛 품번 0162
장갑 낀 채로 스마트폰 터치 가능한 기모 장갑.

✔ 19일(목) 아침 서울 영하 1도, 체감은 기온보다 3도가량 낮아요

※ 날씨: 기상청 예보(경향신문·이투데이 11/17)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #방한템 #귀덮개 #넥워머 #터치장갑""",
    "products": [prod(1, EAR, N_EAR, "C", "0160"), prod(2, NECK, N_NECK, "C", "0161"), prod(3, GLOVE, N_GLOVE, "C", "0162")],
})

write(DATE, "C2", [
    c_cover("독감 3주 연속 증가 🤧", "집에서 쓰는", "겨울 특이템", "BEST3", [SOAP, MIST, TREE]),
    c_prod(1, "0163", SOAP, "자동 거품<br>손세정기", ["손 대면 거품이 쏙", "타입C 충전식", "600ml 대용량"],
           ["💰 1만5천원대", "📦 충전식"]),
    c_prod(2, "0164", MIST, "무드등<br>미니 가습기", ["신지모루 테이블 미스트", "USB 연결 · 무드등 겸용", "600ml 물통"],
           ["💰 1만1천원대", "📦 USB"]),
    c_prod(3, "0165", TREE, "트리<br>종이 가습기", ["전기 없는 자연기화식", "트리 모양 인테리어", "책상 위에 두기 좋아요"],
           ["💰 2만4천원대", "📦 무전원"]),
    c_howto("0163~0165"),
], {
    "title": "겨울 실내 특이템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

독감 3주 연속 증가 🤧 집에서 쓰는 겨울 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 미홀 타입C 충전식 자동 거품 손세정기 600ml 💛 품번 0163
손을 대면 거품이 나오는 충전식 손세정기.

2. 신지모루 테이블 미스트 USB 무드등 미니 가습기 600ml 💛 품번 0164
무드등 겸용 USB 미니 가습기.

3. 나눔 프로젝트 하트 트리 종이 가습기 💛 품번 0165
전기 없이 쓰는 트리 모양 자연기화식 종이 가습기.

✔ 질병청 예방 수칙: 자주 손 씻기, 기침 예절, 주기적 환기

※ 독감 통계: 질병관리청(국제뉴스 11/16·FAM타임스 11/17)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #손세정기 #미니가습기 #종이가습기 #겨울필수템""",
    "products": [prod(1, SOAP, N_SOAP, "C", "0163"), prod(2, MIST, N_MIST, "C", "0164"), prod(3, TREE, N_TREE, "C", "0165")],
})
print("ok")
