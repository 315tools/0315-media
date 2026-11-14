"""2026-11-14(토, 소형가전의 날) 게시물 6개 → docs/posts/2026-11-14/{A,B,C,A2,B2,C2}
점심: 토요일 전국 가을비 → 눅눅한 집 습기·신발·이불 / 퇴근길: 다음 주 수능일 6년 만의 영하권 → 미리 방한 가전
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-14"
DL = "2026.11.14 (토)"
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



DEH, SHOE, BED = "8291673143", "8037241711", "8533494484"
HAND, BLK, FAN = "9121607800", "9042228033", "7030236539"
N_DEH = "리치매직 제습기 1.6L"
N_SHOE = "퓨어코치 사방향 슈케어 신발 건조기 SD02F"
N_BED = "파나소닉 UV살균 침구 청소기 MC-DC10W"
N_HAND = "카프 충전식 양면 발열 손난로 보조배터리 10000mAh KF-HW1"
N_BLK = "한일메디컬 네모 USB 전기담요 (1인용 극세사)"
N_FAN = "카프 PTC 공기순환 미니 온풍기 KF-FH01"

# ═════════ A · 점심 12:00 — 토요일 전국 가을비 ═════════
SRC1 = "출처: 뉴스S·톱스타뉴스(11/13), 에너지경제(11/13), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 주말</div>
<h1>토요일 <span class="hl">전국 가을비</span><br>밤부터 그쳐요</h1>
<p class="lead">제주 최대 60mm, 남부 최대 40mm<br>일요일엔 평년보다 포근</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(14일) <span class="hl">예상 강수량</span></h2>
<div class="fig"><div><small>제주도</small><strong>10~60mm</strong></div><div><small>광주·전남·경남권</small><strong>10~40mm</strong></div></div>
<div class="fig"><div><small>충청·전북·경북권</small><strong>5~30mm</strong></div><div><small>서울·인천·경기남부</small><strong>5~10mm</strong></div></div>
<div class="box">오늘 기온 아침 6~14도, 낮 11~17도<br>중부는 <b class="hl">늦은 밤</b> 대부분 그쳐요</div>""", SRC1, DL),
    a_slide(3, n, """<h2>내일(15일)은 <span class="hl">포근</span></h2>
<div class="fig"><div><small>15일 아침</small><strong>6~13도</strong></div><div><small>15일 낮</small><strong>16~21도</strong></div></div>
<ul class="chk"><li>남부는 15일 새벽, 제주는 아침까지 비</li><li>평년(최저 0~9도·최고 11~17도)보다 높아요</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>비 오는 날 <span class="hl">집 관리</span></h2>
<ul class="chk"><li>젖은 신발은 바로 말리기</li><li>실내 빨래는 <span class="hl">제습</span>하면서</li><li>비 그친 일요일엔 환기</li><li>눅눅한 이불은 털고 말리기</li></ul>""", "", DL),
    a_slide(5, n, f"""<h2>비 오는 주말 <span class="hl">뽀송 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(DEH)}"><div>리치매직 제습기<span>1.6L · 원룸·방 한 칸용</span></div></li>
<li><b>2</b><img src="{img(SHOE)}"><div>퓨어코치 신발 건조기<span>사방향 슈케어 · SD02F</span></div></li>
<li><b>3</b><img src="{img(BED)}"><div>파나소닉 침구 청소기<span>UV살균 · MC-DC10W</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/14 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "토요일 전국 가을비",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 토요일(14일) 전국 가을비… 밤부터 그치고 일요일은 포근 🌧️

· 예상 강수량: 제주도 10~60mm, 광주·전남·부산·울산·경남 10~40mm, 충청권·전북·대구·경북 5~30mm, 서울·인천·경기남부·강원 5~10mm
· 오늘 아침 6~14도, 낮 11~17도
· 중부는 14일 늦은 밤 대부분 그치고, 남부는 15일 새벽, 제주는 15일 아침까지
· 15일(일) 아침 6~13도, 낮 16~21도 — 평년(최저 0~9도, 최고 11~17도)보다 높아요

✔ 젖은 신발 바로 말리고, 실내 빨래는 제습하면서, 비 그친 일요일엔 환기

🔗 비 오는 주말 뽀송 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 뉴스S·톱스타뉴스·에너지경제신문(11/13) — 기상청 예보

#광고 #생활뉴스 #날씨 #주말날씨 #가을비 #제습기 #신발건조기 #소형가전""",
    "products": [prod(1, DEH, N_DEH, "A"), prod(2, SHOE, N_SHOE, "A"), prod(3, BED, N_BED, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 수능일 6년 만의 영하권 ═════════
SRC2 = "출처: 한국일보·데일리안·YTN(11/12), 기상청 예보"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">날씨 · 다음 주</div>
<h1>6년 만에<br><span class="hl">수능 한파</span></h1>
<p class="lead">19일(목) 서울 아침 -1도<br>화·수 비 온 뒤 찬 바람</p>""", SRC2, DL),
    a_slide(2, n, """<h2>서울 <span class="hl">아침 기온</span></h2>
<div class="fig"><div><small>17일(화)</small><strong>8도</strong></div><div><small>18일(수)</small><strong>4도</strong></div></div>
<div class="fig"><div><small>19일(목) 수능일</small><strong>-1도</strong></div><div><small>19일 낮</small><strong>5도</strong></div></div>
<div class="box">전국 19일 아침 -3~6도, 낮 4~13도</div>""", SRC2, DL),
    a_slide(3, n, """<h2>왜 <span class="hl">6년 만</span>?</h2>
<ul class="chk"><li>17일 오후~18일 오전 전국에 비</li><li>그 뒤 차고 건조한 <span class="hl">북서풍</span></li><li>서울 수능일 아침 영하는 2020년 이후 처음</li><li>2020년(12월 3일) 서울 아침 -1.1도</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>미리 <span class="hl">추위 대비</span></h2>
<ul class="chk"><li>얇은 옷 <span class="hl">여러 겹</span> + 두꺼운 외투</li><li>핫팩 등 방한용품 챙기기</li><li>17일 기상청 최신 예보 확인</li><li>배로 이동하면 일정 미리 확인</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>찬 바람 대비 <span class="hl">방한 가전</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(HAND)}"><div>카프 충전식 손난로<span>양면 발열 · 보조배터리 겸용</span></div></li>
<li><b>2</b><img src="{img(BLK)}"><div>한일메디컬 USB 전기담요<span>1인용 극세사</span></div></li>
<li><b>3</b><img src="{img(FAN)}"><div>카프 PTC 미니 온풍기<span>KF-FH01 · 책상 옆에</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/14 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "6년 만의 수능 한파 예보",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 6년 만에 '수능 한파'… 19일(목) 서울 아침 -1도 예보 🥶

· 서울 아침 기온: 17일(화) 8도 → 18일(수) 4도 → 19일(목) -1도, 19일 낮 5도
· 전국 19일 아침 -3~6도, 낮 4~13도
· 17일 오후~18일 오전 전국에 비, 그 뒤 차고 건조한 북서풍
· 서울 수능일 아침 영하권은 시험이 12월 3일에 치러진 2020년(-1.1도) 이후 처음
· 17~18일 바다 물결이 높아 배로 이동하는 수험생은 일정 미리 확인

✔ 얇은 옷 여러 겹 + 두꺼운 외투, 핫팩 등 방한용품 챙기기
✔ 수능일 전후 날씨는 바뀔 수 있어요 — 17일 기상청 최신 예보 확인

🔗 찬 바람 대비 방한 가전 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 한국일보·데일리안·YTN(11/12) — 기상청 예보

#광고 #생활뉴스 #날씨 #수능한파 #수능 #손난로 #겨울가전 #소형가전""",
    "products": [prod(1, HAND, N_HAND, "A"), prod(2, BLK, N_BLK, "A"), prod(3, FAN, N_FAN, "A")],
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



write(DATE, "B", [poll("비 오는 주말,<br>실내 빨래 말리는 법은? 🌧️", "토요일 전국 비, 밤부터 그쳐요 (기상청 예보)",
                       [("보일러 살짝", "바닥 난방으로 말리기"), ("선풍기 바람", "계절 상관없이 출동"),
                        ("그냥 기다린다", "언젠간 마르겠지…"), ("제습기 켜기", "문 닫고 돌리면 뽀송")], DEH)], {
    "title": "실내 빨래 말리는 법 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 비 오는 주말, 실내 빨래 말리는 법은? 🌧️
댓글에 번호로 투표해주세요!

1️⃣ 보일러 살짝
2️⃣ 선풍기 바람
3️⃣ 그냥 기다린다
4️⃣ 제습기 켜기

※ 14일(토) 전국 비, 중부는 늦은 밤 대부분 그침 (기상청 예보, 뉴스S·톱스타뉴스 11/13)

🔗 4번 리치매직 제습기 링크는 프로필에
👥 빨래 냄새 때문에 고민인 친구 태그

#광고 #투표 #공감 #주말 #실내건조 #제습기""",
    "products": [prod(1, DEH, N_DEH, "B")],
})

write(DATE, "B2", [poll("영하로 떨어진 아침,<br>나의 손 시림 대처법은? 🧤", "다음 주 19일 서울 아침 -1도 예보 (기상청)",
                        [("주머니에 쏙", "손은 무조건 주머니"), ("장갑 필수", "외출 전 무조건 착용"),
                         ("뜨거운 음료", "컵으로 손 녹이기"), ("충전식 손난로", "충전해두고 계속 따끈")], HAND)], {
    "title": "손 시림 대처법 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 영하로 떨어진 아침, 나의 손 시림 대처법은? 🧤
댓글에 번호로 투표해주세요!

1️⃣ 주머니에 쏙
2️⃣ 장갑 필수
3️⃣ 뜨거운 음료
4️⃣ 충전식 손난로

※ 19일(목) 서울 아침 -1도, 6년 만의 수능 한파 예보 (기상청 예보, 한국일보·데일리안 11/12)

🔗 4번 카프 충전식 손난로 링크는 프로필에
👥 겨울만 되면 손이 얼음장인 친구 태그

#광고 #투표 #공감 #수능한파 #손난로 #겨울""",
    "products": [prod(1, HAND, N_HAND, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/14 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("토요일 전국 가을비", "비 오는 주말", "뽀송 가전", "BEST3", [DEH, SHOE, BED]),
    c_prod(1, "0136", DEH, "리치매직<br>제습기 1.6L", ["1.6L 물통 제습기", "원룸·방 한 칸에", "실내 빨래 말릴 때"],
           ["💰 9만원대", "🚀 로켓배송"]),
    c_prod(2, "0137", SHOE, "퓨어코치<br>신발 건조기", ["사방향 슈케어", "젖은 운동화 말리기", "SD02F"],
           ["💰 5만원대", "🚀 로켓배송"]),
    c_prod(3, "0138", BED, "파나소닉<br>UV 침구 청소기", ["UV살균 침구 청소기", "눅눅한 이불 관리", "MC-DC10W"],
           ["💰 12만원대", "🚀 로켓배송"]),
    c_howto("0136~0138"),
], {
    "title": "비 오는 주말 뽀송 가전 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

토요일 전국 가을비 🌧️ 비 오는 주말 뽀송 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 리치매직 제습기 1.6L 💛 품번 0136
원룸·방 한 칸에 두기 좋은 1.6L 물통 제습기.

2. 퓨어코치 사방향 슈케어 신발 건조기 SD02F 💛 품번 0137
비에 젖은 운동화를 말리는 신발 건조기.

3. 파나소닉 UV살균 침구 청소기 MC-DC10W 💛 품번 0138
UV살균 기능이 있는 침구 청소기.

※ 날씨: 기상청 예보(뉴스S·톱스타뉴스·에너지경제신문 11/13 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #제습기 #신발건조기 #침구청소기 #주말날씨""",
    "products": [prod(1, DEH, N_DEH, "C", "0136"), prod(2, SHOE, N_SHOE, "C", "0137"), prod(3, BED, N_BED, "C", "0138")],
})

write(DATE, "C2", [
    c_cover("6년 만의 수능 한파", "영하 아침", "방한 가전", "BEST3", [HAND, BLK, FAN]),
    c_prod(1, "0139", HAND, "카프<br>충전식 손난로", ["양면 발열 손난로", "10000mAh 보조배터리 겸용", "KF-HW1"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(2, "0140", BLK, "한일메디컬<br>USB 전기담요", ["USB 연결 전기담요", "1인용 극세사", "무릎·어깨에 덮기"],
           ["💰 2만원대", "🚚 무료배송"]),
    c_prod(3, "0141", FAN, "카프<br>PTC 미니 온풍기", ["PTC 미니 온풍기", "공기순환 난방", "KF-FH01"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_howto("0139~0141"),
], {
    "title": "영하 아침 방한 가전 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

6년 만의 수능 한파 예보 🥶 영하 아침 방한 가전 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 카프 충전식 양면 발열 손난로 보조배터리 10000mAh KF-HW1 💛 품번 0139
충전해서 쓰는 양면 발열 손난로, 보조배터리 겸용.

2. 한일메디컬 네모 USB 전기담요 (1인용 극세사) 💛 품번 0140
USB로 연결해 무릎·어깨에 덮는 극세사 전기담요.

3. 카프 PTC 공기순환 미니 온풍기 KF-FH01 💛 품번 0141
책상 옆에 두기 좋은 PTC 미니 온풍기.

✔ 난방기구는 주변 물건 치우고, 외출 땐 전원 끄기

※ 날씨: 19일(목) 서울 아침 -1도 예보 — 기상청(한국일보·데일리안·YTN 11/12 보도)
※ {NOTE}

#광고 #쿠팡추천템 #소형가전 #손난로 #전기담요 #미니온풍기 #수능한파""",
    "products": [prod(1, HAND, N_HAND, "C", "0139"), prod(2, BLK, N_BLK, "C", "0140"), prod(3, FAN, N_FAN, "C", "0141")],
})
print("ok")
