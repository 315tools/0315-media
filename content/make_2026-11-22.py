"""2026-11-22(일, 특이한 상품의 날) 게시물 6개 → docs/posts/2026-11-22/{A,B,C,A2,B2,C2}
점심: 절기 '소설' 아침 영하 9도 추위 → 발열 방한 특이템 / 퇴근길: 소설엔 겨울 이불 꺼내기(볕 말리기·54도 세탁) → 이불 관리 특이템
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from templates import (A_CSS, AD, B_CSS, C_CSS, DISC, ROOT, a_slide, c_foot, c_prod, img, page, write)  # noqa: E402,F401

DATE = "2026-11-22"
DL = "2026.11.22 (일)"
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


SOLE, BALA, GLOVE = "9287515322", "8445091675", "9774114207"
PIN, NET, DRY = "7589358430", "9749114640", "9496717549"
N_SOLE = "열선 발열깔창 (USB 전원 연결형)"
N_BALA = "우디우디 겨울 방한 기모 바라클라바"
N_GLOVE = "핫터치 스마트 발열장갑 (KC인증·배터리 포함·3단 온도조절)"
N_PIN = "디오셀 이불 밀림방지 고정핀 8p (2세트)"
N_NET = "케디브 고밀도 이불 세탁망 특대형 120x120cm (2개)"
N_DRY = "RichMagic 3in1 휴대용 미니 건조기 (의류·이불·신발)"

# ═════════ A · 점심 12:00 — 소설 아침 영하 9도 ═════════
SRC1 = "출처: 한국일보·서울경제(11/21), 위키트리(11/13), 기상청"
n = 5
a1 = [
    a_slide(1, n, """<div class="tag">날씨 · 절기</div>
<h1>첫눈 온다는 '소설'<br>아침 <span class="hl">영하 9도</span></h1>
<p class="lead">전국 대체로 맑고 건조해요<br>낮엔 4~10도로 조금 풀려요</p>""", SRC1, DL),
    a_slide(2, n, """<h2>오늘(22일) <span class="hl">기온</span></h2>
<div class="fig"><div><small>전국 아침</small><strong>-9~1도</strong></div><div><small>전국 낮</small><strong>4~10도</strong></div></div>
<div class="fig"><div><small>서울 아침</small><strong>-4도</strong></div><div><small>서울 낮</small><strong>5도</strong></div></div>
<div class="box">평년(아침 -3~6도, 낮 8~15도)보다 낮아요<br>춘천 아침 <b class="hl">-8도</b> 예보</div>""", SRC1, DL),
    a_slide(3, n, """<h2>추위와 <span class="hl">건조</span></h2>
<ul class="chk"><li>중부·경북 내륙 아침 영하 5도 안팎</li><li>서울·강원 등 <span class="hl">건조특보</span></li><li>바람도 불어 작은 불씨 조심</li><li>미세먼지는 오전 '좋음'</li></ul>""", SRC1, DL),
    a_slide(4, n, """<h2>절기 <span class="hl">소설</span>이란</h2>
<ul class="chk"><li>입동(11/7) 보름 뒤, 첫눈이 온다는 절기</li><li>올해는 22일 16시 23분 (한국천문연구원)</li><li>눈이 꼭 오는 날은 아니에요</li><li>실제 날씨는 <span class="hl">기상청 예보</span>로 확인</li></ul>""", SRC1, DL),
    a_slide(5, n, f"""<h2>찬 바람 막는 <span class="hl">발열 방한템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(SOLE)}"><div>열선 발열깔창<span>USB 전원 연결형</span></div></li>
<li><b>2</b><img src="{img(BALA)}"><div>우디우디 바라클라바<span>기모 · 머리·목 한 번에</span></div></li>
<li><b>3</b><img src="{img(GLOVE)}"><div>핫터치 발열장갑<span>KC인증 · 3단 온도조절</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/22 점심 ①~③</p>""", "", DL),
]
write(DATE, "A", a1, {
    "title": "소설 아침 영하 9도",
    "slot": 1,
    "caption": f"""{DISC}

[생활뉴스] 첫눈 온다는 절기 '소설', 아침 영하 9도 🥶 낮엔 조금 풀려요

· 22일(일) 전국 아침 -9~1도, 낮 4~10도 — 평년(아침 -3~6도, 낮 8~15도)보다 낮아요
· 서울 아침 -4도·낮 5도, 춘천 -8도, 청주·대전 -5도, 부산 -1도, 제주 6도 예보
· 중부 내륙과 경북 내륙은 아침 영하 5도 안팎
· 서울·경기 북동부 일부·강원·경북 동해안 등 건조특보, 바람도 불어 불씨 조심
· 미세먼지는 오전 전 권역 '좋음'
· 소설: 입동 보름 뒤 첫눈이 온다는 절기, 올해는 22일 16시 23분(한국천문연구원) — 눈이 꼭 오는 건 아니에요

✔ 얼음 얼고 서리 내리는 곳이 있어요, 아침 길 조심
✔ 건조한 날엔 화기 단속

🔗 찬 바람 막는 발열 방한템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 한국일보(11/21)·서울경제(11/21, 뉴시스) — 기상청 예보 / 위키트리(11/13)

#광고 #생활뉴스 #날씨 #소설 #절기 #강추위 #발열깔창 #특이한상품""",
    "products": [prod(1, SOLE, N_SOLE, "A"), prod(2, BALA, N_BALA, "A"), prod(3, GLOVE, N_GLOVE, "A")],
})

# ═════════ A2 · 퇴근길 18:00 — 소설엔 겨울 이불 ═════════
SRC2 = "출처: 위키트리(11/8·11/12·11/13), 미국폐협회·메이오클리닉"
n = 5
a2 = [
    a_slide(1, n, """<div class="tag">생활 · 침구</div>
<h1>소설엔 <span class="hl">겨울 이불</span><br>이렇게 꺼내요</h1>
<p class="lead">볕에 말리고, 뜨거운 물로 빨고<br>진드기 걱정 덜기</p>""", SRC2, DL),
    a_slide(2, n, """<h2>침구 세탁 <span class="hl">온도</span></h2>
<div class="fig"><div><small>미국폐협회</small><strong>49도↑</strong></div><div><small>메이오클리닉</small><strong>54도↑</strong></div></div>
<div class="box">두 곳 모두 <b class="hl">일주일에 한 번</b> 세탁 권고<br><small>미국 기준 · 빨기 전 케어라벨 먼저 확인</small></div>""", SRC2, DL),
    a_slide(3, n, """<h2>꺼낼 때 <span class="hl">체크</span></h2>
<ul class="chk"><li>바람 쐬고 <span class="hl">볕에 말리기</span></li><li>비·흐린 날은 피하기</li><li>말린 이불은 완전히 식힌 뒤 깔기</li><li>집 안 습도는 50% 아래로</li></ul>""", SRC2, DL),
    a_slide(4, n, """<h2>큰 이불 <span class="hl">빨래 팁</span></h2>
<ul class="chk"><li>문을 눌러야 닫히면 <span class="hl">빨래방</span>으로</li><li>커버 분리, 지퍼는 잠그기</li><li>저온 건조 + 건조볼</li><li>가운데·솔기까지 마른 뒤 접기</li></ul>""", SRC2, DL),
    a_slide(5, n, f"""<h2>이불 정리 <span class="hl">특이템</span></h2>
<ol class="prod"><li><b>1</b><img src="{img(PIN)}"><div>디오셀 이불 고정핀<span>밀림 방지 · 8p 2세트</span></div></li>
<li><b>2</b><img src="{img(NET)}"><div>케디브 이불 세탁망<span>특대형 120x120cm · 2개</span></div></li>
<li><b>3</b><img src="{img(DRY)}"><div>RichMagic 미니 건조기<span>의류·이불·신발 3in1</span></div></li></ol>
<p class="lead" style="font-size:36px">🔗 프로필 링크 → 11/22 저녁 ①~③</p>""", "", DL),
]
write(DATE, "A2", a2, {
    "title": "소설엔 겨울 이불 이렇게",
    "slot": 2,
    "caption": f"""{DISC}

[생활뉴스] 절기 '소설', 겨울 이불 꺼내는 날 🛏️ 볕에 말리고 뜨거운 물로 빨기

· 미국폐협회: 침구는 일주일에 한 번, 약 49도 이상 뜨거운 물로 세탁
· 메이오클리닉: 시트·베갯잇·담요는 일주일에 한 번 이상, 약 54도 이상 물로 세탁
· 미국폐협회: 천식 환자의 최대 85%가 집먼지진드기에 알레르기 반응
· 집 안 습도는 50% 아래로 — 두 기관 수치 모두 미국 기준이라 국내 권고와 다를 수 있어요, 케어라벨 먼저 확인
· 넣어 둔 이불은 바람 쐬고 볕에 말린 뒤, 완전히 식혀서 깔기 (비·흐린 날은 피하기)
· 세탁기 문을 눌러야 닫힐 만큼 크면 대형 빨래방, 커버는 분리하고 지퍼 잠그기
· 건조는 저온 + 건조볼, 가운데·솔기까지 다 마른 뒤 접기

🔗 이불 정리 특이템 ①~③은 프로필 링크에 있어요
🛒 더 많은 생활템은 @0315_pick

출처: 위키트리(11/8·11/12·11/13) — 미국폐협회·메이오클리닉 권고 인용

#광고 #생활뉴스 #소설 #겨울이불 #이불빨래 #침구관리 #세탁망 #특이한상품""",
    "products": [prod(1, PIN, N_PIN, "A"), prod(2, NET, N_NET, "A"), prod(3, DRY, N_DRY, "A")],
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


write(DATE, "B", [poll("영하 9도 소설 아침,<br>나의 방한 필살기는? 🥶", "22일 아침 -9~1도, 서울 -4도 (기상청 예보)",
                       [("내복", "안 보이는 곳의 진심"), ("핫팩", "주머니마다 하나씩"),
                        ("목도리 칭칭", "눈만 내놓고 다님"), ("발열깔창", "발바닥부터 따뜻하게")], SOLE)], {
    "title": "나의 방한 필살기 투표",
    "slot": 1,
    "caption": f"""{DISC}

📊 영하 9도 소설 아침, 나의 방한 필살기는? 🥶
댓글에 번호로 투표해주세요!

1️⃣ 내복
2️⃣ 핫팩
3️⃣ 목도리 칭칭
4️⃣ 발열깔창

※ 22일(일) 전국 아침 -9~1도, 서울 -4도 예보 (기상청 예보, 한국일보·서울경제 11/21)

🔗 4번 열선 발열깔창 링크는 프로필에
👥 겨울만 되면 발 시렵다는 친구 태그

#광고 #투표 #공감 #소설 #강추위 #발열깔창""",
    "products": [prod(1, SOLE, N_SOLE, "B")],
})

write(DATE, "B2", [poll("겨울 이불 빨래,<br>얼마나 자주 하세요? 🛏️", "침구는 주 1회 뜨거운 물로 (미국폐협회·메이오클리닉)",
                        [("매주", "부지런함 인증"), ("한 달에 한 번", "이 정도면 양호"),
                         ("계절 바뀔 때", "솔직히 이게 현실"), ("세탁망에 쏙", "큰 이불도 집에서")], NET)], {
    "title": "겨울 이불 빨래 주기 투표",
    "slot": 2,
    "caption": f"""{DISC}

📊 겨울 이불 빨래, 얼마나 자주 하세요? 🛏️
댓글에 번호로 투표해주세요!

1️⃣ 매주
2️⃣ 한 달에 한 번
3️⃣ 계절 바뀔 때
4️⃣ 세탁망에 쏙

※ 미국폐협회는 침구를 일주일에 한 번 약 49도 이상, 메이오클리닉은 약 54도 이상 물로 세탁 권고 (위키트리 11/12) — 케어라벨 먼저 확인

🔗 4번 케디브 이불 세탁망 링크는 프로필에
👥 이불 빨래 미루는 사람 태그

#광고 #투표 #공감 #소설 #이불빨래 #세탁망""",
    "products": [prod(1, NET, N_NET, "B")],
})

# ═════════ C · 상품소개 ═════════
NOTE = "11/22 쿠팡 검색 기준 · 가격은 바뀔 수 있어요"


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
    c_cover("소설 아침 영하 9도", "찬 바람 막는", "발열 방한템", "BEST3", [SOLE, BALA, GLOVE]),
    c_prod(1, "0184", SOLE, "열선<br>발열깔창", ["신발 속에 까는 열선 깔창", "USB 전원 연결형", "발바닥부터 따뜻하게"],
           ["💰 1만원대", "🚚 무료배송"]),
    c_prod(2, "0185", BALA, "우디우디<br>바라클라바", ["머리·목을 한 번에 덮는", "기모 방한 바라클라바", "블랙"],
           ["💰 2만원대", "🚀 로켓배송"]),
    c_prod(3, "0186", GLOVE, "핫터치<br>발열장갑", ["KC인증 충전식 발열장갑", "3단 온도 조절", "배터리·충전기 포함"],
           ["💰 6만원대", "🚀 로켓배송"]),
    c_howto("0184~0186"),
], {
    "title": "찬 바람 막는 발열 방한템 BEST3",
    "slot": 1,
    "caption": f"""{DISC}

첫눈 온다는 소설, 아침 영하 9도 🥶 찬 바람 막는 발열 방한템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 열선 발열깔창 (USB 전원 연결형) 💛 품번 0184
신발 속에 까는 열선 깔창. 전원 방식·사이즈는 상품 페이지에서 확인하세요.

2. 우디우디 겨울 방한 기모 바라클라바 💛 품번 0185
머리와 목을 한 번에 덮는 기모 바라클라바.

3. 핫터치 스마트 발열장갑 (KC인증) 💛 품번 0186
배터리·충전기가 들어 있는 3단 온도 조절 발열장갑.

✔ 발열 제품은 처음엔 낮은 단계로, 오래 쓸 땐 피부 상태 살피기

※ 날씨: 22일(일) 전국 아침 -9~1도 — 기상청(한국일보·서울경제 11/21 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #발열깔창 #바라클라바 #발열장갑 #소설""",
    "products": [prod(1, SOLE, N_SOLE, "C", "0184"), prod(2, BALA, N_BALA, "C", "0185"), prod(3, GLOVE, N_GLOVE, "C", "0186")],
})

write(DATE, "C2", [
    c_cover("소설, 겨울 이불 꺼내는 날", "겨울 이불", "정리 특이템", "BEST3", [PIN, NET, DRY]),
    c_prod(1, "0187", PIN, "디오셀<br>이불 고정핀", ["이불 속통 밀림 방지", "버섯 모양 고정핀", "8p × 2세트"],
           ["💰 5천원대", "🚀 로켓배송"]),
    c_prod(2, "0188", NET, "케디브<br>이불 세탁망", ["고밀도 특대형 세탁망", "120 x 120cm", "2개입"],
           ["💰 1만원대", "🚀 로켓배송"]),
    c_prod(3, "0189", DRY, "RichMagic<br>미니 건조기", ["휴대용 미니 건조기", "의류·이불·신발 3in1", "UV 살균 기능"],
           ["💰 5만원대", "🚀 로켓배송"]),
    c_howto("0187~0189"),
], {
    "title": "겨울 이불 정리 특이템 BEST3",
    "slot": 2,
    "caption": f"""{DISC}

절기 소설, 겨울 이불 꺼내는 날 🛏️ 이불 정리 특이템 BEST3

❤️구매 방법❤️
프로필 링크 클릭 → 품번 검색

1. 디오셀 이불 밀림방지 고정핀 8p (2세트) 💛 품번 0187
이불 속통이 커버 안에서 밀리지 않게 잡아주는 고정핀.

2. 케디브 고밀도 이불 세탁망 특대형 120x120cm (2개) 💛 품번 0188
큰 이불도 넣을 수 있는 특대형 세탁망.

3. RichMagic 3in1 휴대용 미니 건조기 💛 품번 0189
의류·이불·신발을 말리는 휴대용 미니 건조기.

✔ 빨기 전 이불 케어라벨 먼저 확인하기

※ 침구는 주 1회 약 49~54도 이상 물로 세탁 권고 — 미국폐협회·메이오클리닉(위키트리 11/12 보도)
※ {NOTE}

#광고 #쿠팡추천템 #특이한상품 #이불정리 #세탁망 #미니건조기 #소설""",
    "products": [prod(1, PIN, N_PIN, "C", "0187"), prod(2, NET, N_NET, "C", "0188"), prod(3, DRY, N_DRY, "C", "0189")],
})
print("ok")
