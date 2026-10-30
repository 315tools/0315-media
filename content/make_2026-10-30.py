"""2026-10-30(금, 식품의 날) 게시물 6개 → docs/posts/2026-10-30/{A,B,C,A2,B2,C2}
점심: 오늘 낮 21도 포근 → 주말 다시 뚝·겨울 간식 / 퇴근길: 매일유업 11월부터 9개 품목 최대 8% 인상(매일우유·드링크 요거트 동결)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-10-30"
DL = "2026.10.30 (금)"
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


BUN, POTA, FISH = "7165408021", "7308154285", "7324843040"
MILK, YOG, GRAN = "9736556263", "7183750807", "257055522"
N_BUN, N_POTA, N_FISH = "삼립 단팥호빵 10봉", "가든클래식스 고구마공장 아이스 군고구마 1kg (냉동)", "삼진어묵 오동통 모듬어묵 + 스프"
N_MILK, N_YOG, N_GRAN = "매일우유 멸균 오리지널", "매일바이오 드링킹 플레인", "포스트 크랜베리 아몬드 그래놀라"

# ═════════ A · 점심 12:00 — 오늘 포근, 주말 다시 뚝 ═════════
SRC1 = "출처: 이투데이(10/30)·아주경제·한국일보(10/29), 기상청 예보"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 주말</div>
<h1>오늘은 포근,<br><span class="hl">주말 다시 뚝</span><br>겨울 간식 타이밍</h1>
<p class="lead">일요일 아침 최저 1~10도<br>다음 주 초 평년보다 추워요</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(30일) 아침 · 낮 기온</h2>
<div class="fig"><div><small>서울</small><strong>9 / 18도</strong></div><div><small>대전</small><strong>9 / 19도</strong></div></div>
<div class="fig"><div><small>대구</small><strong>9 / 20도</strong></div><div><small>부산</small><strong>13 / 21도</strong></div></div>
<div class="box">전국 아침 4~13도, 낮 17~21도<br>평년과 <b class="hl">비슷하거나 조금 높아요</b></div>""", SRC1, DL),
    a_slide(3, n, """<h2>주말 기온 흐름</h2>
<div class="fig"><div><small>토 (31일) 맑음</small><strong>2~12 / 13~21도</strong></div></div>
<div class="fig"><div><small>일 (11/1) 오후 비</small><strong>1~10 / 11~17도</strong></div></div>
<div class="box">다음 주 초 서울<br>3일 아침 <b class="hl">3도</b> · 낮 13도</div>""", SRC1, DL),
    a_slide(4, n, """<h2>주말 체크</h2>
<ul class="chk"><li>일교차 <span class="hl">10~15도</span> · 겉옷 챙기기</li><li>일요일 오후 중부 서해안·전라권 비</li><li>다음 주 초 평년보다 낮은 기온</li><li>따뜻한 간식은 냉동실에 미리</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>쌀쌀한 주말 <span class="hl">겨울 간식</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(BUN)}"><div>삼립 단팥호빵<span>10봉 · 겨울 대표 간식</span></div></li>
<li><b>2</b><img src="{img(POTA)}"><div>아이스 군고구마 1kg<span>냉동 · 고구마공장</span></div></li>
<li><b>3</b><img src="{img(FISH)}"><div>삼진어묵 오동통 모듬어묵<span>스프 포함 · 어묵탕용</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/30 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "오늘 포근·주말 다시 뚝",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 오늘은 포근, 주말엔 다시 기온 뚝 — 겨울 간식 미리 챙기세요 🍠

· 오늘(30일) 아침 4~13도, 낮 17~21도 — 평년과 비슷하거나 조금 높아요 (서울 9/18, 대전 9/19, 대구 9/20, 부산 13/21)
· 토요일(31일) 맑음, 아침 2~12도·낮 13~21도
· 일요일(11/1) 오후부터 중부 서해안·전라권 비, 아침 1~10도·낮 11~17도
· 다음 주 초 평년보다 낮은 기온 (서울 3일 아침 3도·낮 13도)
· 당분간 일교차 10~15도 안팎

✔ 겉옷 챙기기, 일요일 오후 비 소식 확인, 따뜻한 간식은 냉동실에 미리

🔗 겨울 간식 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 이투데이(10/30), 아주경제(10/29), 한국일보(10/29), 서울신문(10/29) — 기상청 예보

#광고 #생활뉴스 #주말날씨 #일교차 #겨울간식 #호빵 #군고구마 #어묵탕""",
    "products": [prod(1, BUN, N_BUN, "A"), prod(2, POTA, N_POTA, "A"), prod(3, FISH, N_FISH, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 매일유업 11월 가격 인상 ═════════
SRC2 = "출처: 뉴스핌·천지일보(10/27)"
n = 4
a2 = [
    a_slide(1, n, """<div class="tag">물가 · 장바구니</div>
<h1>11월부터<br>요거트·우유<br><span class="hl">최대 8% 인상</span></h1>
<p class="lead">매일유업 4개 브랜드 9개 품목<br>흰 우유 '매일우유'는 동결</p>""", SRC2, DL),
    a_slide(2, n, """<h2>브랜드별 인상률</h2>
<div class="fig"><div><small>매일바이오 떠먹는·그릭</small><strong>3~8%</strong></div><div><small>상하목장 유기농 등</small><strong>6~8%</strong></div></div>
<div class="fig"><div><small>소화가 잘되는 우유</small><strong>4~7%</strong></div><div><small>아몬드브리즈</small><strong>6~7.6%</strong></div></div>
<div class="box">11월 1일부터<br>유통채널별 <b class="hl">순차 적용</b></div>""", SRC2, DL),
    a_slide(3, n, """<h2>장보기 체크</h2>
<ul class="chk"><li><span class="hl">매일우유·드링크 요거트</span>는 가격 유지</li><li>자주 사는 제품 인상 여부 확인</li><li>유통기한 보고 먹을 만큼만</li><li>회사 측 이유: 지속적인 원가 상승</li></ul>""", SRC2, DL),
    a_slide(4, n, f"""<h2>가격 유지 품목 <span class="hl">아침템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(MILK)}"><div>매일우유 멸균 오리지널<span>200ml 팩 · 가격 동결 품목</span></div></li>
<li><b>2</b><img src="{img(YOG)}"><div>매일바이오 드링킹 플레인<span>드링크 요거트 · 동결 품목</span></div></li>
<li><b>3</b><img src="{img(GRAN)}"><div>포스트 크랜베리 아몬드 그래놀라<span>우유·요거트에 곁들이기</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 10/30 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "매일유업 11월부터 최대 8% 인상",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 11월부터 요거트·우유 일부 최대 8% 인상 — 흰 우유 '매일우유'는 동결 🥛

· 매일유업, 11월 1일부터 4개 브랜드 9개 품목 가격 3~8% 인상 (유통채널별 순차 적용)
· 매일바이오 떠먹는 요거트·그릭요거트 3~8%
· 상하목장 유기농 요거트·유기농 우유·무항생제 우유 6~8%
· 소화가 잘되는 우유 4~7%, 아몬드브리즈 6~7.6%
· 매일우유와 드링크 요거트는 가격 유지
· 회사 측: "지속적인 원가 상승으로 불가피하게 일부 제품 가격 조정"

✔ 자주 사는 제품 인상 여부 확인, 유통기한 보고 먹을 만큼만

🔗 가격 유지 품목 아침템 ①~③은 프로필 링크에 있어요
🛒 더 많은 먹거리는 @0315_pick

출처: 뉴스핌(10/27), 천지일보(10/27)

#광고 #생활뉴스 #물가 #장바구니 #우유 #요거트 #아침식사 #그래놀라""",
    "products": [prod(1, MILK, N_MILK, "A"), prod(2, YOG, N_YOG, "A"), prod(3, GRAN, N_GRAN, "A")],
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


write(DATE, "B", [poll("쌀쌀해지면 제일<br>땡기는 겨울 간식은? 🍠", "일요일 아침 최저 1~10도 (기상청 예보)",
                       [("붕어빵", "팥 vs 슈크림 논쟁"), ("군고구마", "호호 불어 먹기"),
                        ("어묵 국물", "종이컵 한 잔"), ("김 모락 호빵", "냉동실 상비템")], BUN)], {
    "title": "겨울 간식 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 쌀쌀해지면 제일 땡기는 겨울 간식은? 🍠
댓글에 번호로 투표해주세요!

1️⃣ 붕어빵
2️⃣ 군고구마
3️⃣ 어묵 국물
4️⃣ 김 모락 호빵

🔗 4번 단팥호빵 링크는 프로필에
👥 붕어빵 팥파 vs 슈크림파 친구 태그

#광고 #투표 #공감 #겨울간식 #호빵 #붕어빵 #주말""",
    "products": [prod(1, BUN, N_BUN, "B")],
})

write(DATE, "B2", [poll("출근 전 아침,<br>나는 뭐 먹음? 🥣", "11월부터 요거트 일부 최대 8%↑ (10/27 보도)",
                        [("안 먹는다", "커피로 버팀"), ("편의점 삼각김밥", "출근길 픽업"),
                         ("우유에 시리얼", "3분 컷"), ("드링킹 요거트 한 병", "들고 나가면 끝")], YOG)], {
    "title": "출근 전 아침 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 출근 전 아침, 나는 뭐 먹음? 🥣
댓글에 번호로 투표해주세요!

1️⃣ 안 먹는다
2️⃣ 편의점 삼각김밥
3️⃣ 우유에 시리얼
4️⃣ 드링킹 요거트 한 병

🔗 4번 드링킹 요거트 링크는 프로필에
👥 아침 꼭 챙겨 먹는 친구 태그

#광고 #투표 #공감 #아침식사 #출근 #요거트 #직장인""",
    "products": [prod(1, YOG, N_YOG, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "10/30 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("주말 다시 기온 뚝", "냉동실에 쟁이는", "겨울 간식", "BEST3", [BUN, POTA, FISH]),
    c_prod(1, "0046", BUN, "삼립<br>단팥호빵 10봉", ["겨울 대표 간식 단팥호빵", "10봉 구성", "냉동실 상비 간식"],
           ["💰 1만원대", "🚚 무료배송"]),
    c_prod(2, "0047", POTA, "고구마공장<br>아이스 군고구마 1kg", ["냉동 아이스 군고구마", "1kg 대용량", "출출할 때 꺼내 먹기"],
           ["💰 1만원대", "🚀 로켓프레시"]),
    c_prod(3, "0048", FISH, "삼진어묵<br>오동통 모듬어묵", ["모듬어묵 + 스프 구성", "어묵탕 끓이기 간편", "쌀쌀한 저녁 국물 메뉴"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_howto("0046~0048"),
], {
    "title": "겨울 간식 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

주말 다시 기온 뚝 🍠 냉동실에 쟁이는 겨울 간식 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 삼립 단팥호빵 10봉 💛 품번 0046
겨울 대표 간식, 냉동실 상비용.

2. 가든클래식스 고구마공장 아이스 군고구마 1kg 💛 품번 0047
냉동 아이스 군고구마 1kg.

3. 삼진어묵 오동통 모듬어묵 + 스프 💛 품번 0048
스프가 함께 들어 있는 어묵탕용 모듬어묵.

※ {NOTE}

#광고 #쿠팡추천템 #겨울간식 #호빵 #군고구마 #어묵탕 #간식추천 #주말""",
    "products": [prod(1, BUN, N_BUN, "C", "0046"), prod(2, POTA, N_POTA, "C", "0047"), prod(3, FISH, N_FISH, "C", "0048")],
})

write(DATE, "C2", [
    c_cover("11월 우유·요거트 일부 인상", "가격 유지템", "아침 한 끼", "BEST3", [MILK, YOG, GRAN]),
    c_prod(1, "0049", MILK, "매일우유<br>멸균 오리지널", ["흰 우유 가격 동결 품목", "200ml 멸균팩", "시리얼·그래놀라와 함께"],
           ["💰 3만원대", "🚚 무료배송"]),
    c_prod(2, "0050", YOG, "매일바이오<br>드링킹 플레인", ["드링크 요거트 가격 유지 품목", "들고 마시는 플레인 요거트", "바쁜 출근길 한 병"],
           ["💰 5천원대", "🚀 로켓프레시"]),
    c_prod(3, "0051", GRAN, "포스트<br>크랜베리 아몬드 그래놀라", ["크랜베리·아몬드 그래놀라", "우유·요거트에 곁들이기", "3분 아침 한 그릇"],
           ["💰 9천원대", "🚀 로켓배송"]),
    c_howto("0049~0051"),
], {
    "title": "아침 한 끼 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

11월부터 우유·요거트 일부 인상 🥛 가격 유지 품목으로 아침 한 끼 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 매일우유 멸균 오리지널 💛 품번 0049
가격 동결된 흰 우유, 200ml 멸균팩.

2. 매일바이오 드링킹 플레인 💛 품번 0050
가격 유지되는 드링크 요거트.

3. 포스트 크랜베리 아몬드 그래놀라 💛 품번 0051
우유·요거트에 곁들이는 그래놀라.

※ 가격 인상·동결: 매일유업 발표(뉴스핌·천지일보 10/27 보도)
※ {NOTE}

#광고 #쿠팡추천템 #아침식사 #우유 #요거트 #그래놀라 #장보기 #물가""",
    "products": [prod(1, MILK, N_MILK, "C", "0049"), prod(2, YOG, N_YOG, "C", "0050"), prod(3, GRAN, N_GRAN, "C", "0051")],
})
print("ok")
