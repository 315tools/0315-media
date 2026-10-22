"""카드 디자인 공용 틀 (make_<날짜>.py 에서 import)"""
import base64
import json
from pathlib import Path

ROOT = Path("/home/claude/0315-media")
AD = "광고 · 쿠팡 파트너스 활동으로 수수료를 제공받습니다"
DISC = "[광고] 이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받습니다."
FONT = "'Noto Sans CJK KR','Noto Color Emoji',sans-serif"
BASE = f"""*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:{FONT};position:relative;-webkit-font-smoothing:antialiased;word-break:keep-all}}
.ad{{position:absolute;left:0;right:0;top:0;height:64px;display:flex;align-items:center;padding:0 56px;font-size:27px;font-weight:700;z-index:5}}"""


def img(pid):
    """쿠팡 상품 대표 이미지(assets/products/<상품번호>.jpg)를 data URI로"""
    data = (ROOT / "assets" / "products" / f"{pid}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(data).decode()


def page(css, body):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE}{css}</style></head><body>{body}</body></html>'


def write(date, folder, slides, post):
    """folder: A·B·C(점심, slot 1) / A2·B2·C2(퇴근길, slot 2)"""
    d = ROOT / "docs" / "posts" / date / folder
    (d / "slides").mkdir(parents=True, exist_ok=True)
    for old in (d / "slides").glob("*.html"):
        old.unlink()
    for i, html in enumerate(slides, 1):
        (d / "slides" / f"{i:02d}.html").write_text(html, encoding="utf-8")
    post.update({"channel": folder[0], "slot": 2 if folder.endswith("2") else 1, "date": date, "slides": [], "result": {}})
    (d / "post.json").write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")



# ── A · 기사형 생활뉴스
NAVY, RED, INK, MUTE, BG = "#0f2a4a", "#d7263d", "#14181f", "#5b6573", "#ffffff"
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
ol.prod img{{flex:none;width:112px;height:112px;object-fit:contain;background:#fff;border-radius:12px;border:2px solid #e3e8ef}}
.src{{position:absolute;left:72px;right:72px;bottom:96px;font-size:24px;color:{MUTE};border-top:2px solid #e3e8ef;padding-top:16px}}
.foot{{position:absolute;left:72px;right:72px;bottom:40px;display:flex;justify-content:space-between;font-size:28px;font-weight:700;color:{MUTE}}}"""


def a_slide(i, n, inner, src="", datelabel=""):
    return page(A_CSS, f"""<div class="ad">{AD}</div>
<div class="mast"><div class="brand">0315 <b>생활뉴스</b></div><div class="date">{datelabel} · {i}/{n}</div></div>
<div class="body">{inner}</div>{f'<div class="src">{src}</div>' if src else ''}
<div class="foot"><span>@0315news</span><span>{'옆으로 →' if i < n else ''}</span></div>""")


# ── B · 투표형 공감짤
B_CSS = """body{background:#ffe14d;color:#16181c}.ad{background:#16181c;color:#fff}
.q{position:absolute;left:64px;right:64px;top:120px}
.q small{display:inline-block;background:#16181c;color:#ffe14d;font-size:32px;font-weight:900;padding:8px 20px;border-radius:8px;margin-bottom:22px}
.q h1{font-size:86px;font-weight:900;letter-spacing:-3px;line-height:1.15}
.q p{font-size:36px;font-weight:700;margin-top:16px;color:#3a3a2a}
.opts{position:absolute;left:64px;right:64px;top:520px;display:flex;flex-direction:column;gap:22px}
.o{background:#fff;border:5px solid #16181c;border-radius:22px;padding:26px 30px;display:flex;align-items:center;gap:26px;box-shadow:0 8px 0 #16181c}
.o b{flex:none;width:78px;height:78px;border-radius:50%;background:#16181c;color:#ffe14d;font-size:44px;display:grid;place-items:center}
.o .ph{margin-left:auto;display:flex;gap:10px;flex:none}.o .ph img{width:104px;height:104px;object-fit:contain;background:#fff;border:3px solid #16181c;border-radius:14px}
.o span{font-size:46px;font-weight:900;letter-spacing:-1px;line-height:1.25}.o em{display:block;font-style:normal;font-size:30px;font-weight:700;color:#6b6b5a}
.foot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;align-items:center;font-size:34px;font-weight:900}
.foot span:last-child{font-size:30px;color:#3a3a2a}"""

# ── C · 상품소개
C_CSS = """body{background:#1b1d22;color:#fff}.ad{background:#fff;color:#111}
.hook{position:absolute;left:0;right:0;top:250px;text-align:center}.hook span{background:#000;color:#fff;font-size:44px;font-weight:800;padding:10px 26px;border-radius:6px}
.big{position:absolute;left:40px;right:40px;top:330px;text-align:center;font-weight:900;letter-spacing:-4px;line-height:1.12;text-shadow:0 6px 0 rgba(0,0,0,.35)}
.big .y{color:#ffe14d}.trio{position:absolute;left:64px;right:64px;bottom:160px;display:flex;gap:24px;justify-content:center}
.trio img{width:260px;height:260px;object-fit:contain;background:#fff;border-radius:24px;padding:16px}
.num{position:absolute;left:64px;top:110px;font-size:120px;font-weight:900;color:#ffe14d;letter-spacing:-4px}
.code{position:absolute;right:64px;top:140px;background:#ffe14d;color:#111;font-size:36px;font-weight:900;padding:10px 22px;border-radius:10px}
.photo{position:absolute;left:50%;top:250px;width:470px;height:470px;margin-left:-235px;background:#fff;border-radius:28px;padding:24px;box-shadow:0 18px 40px rgba(0,0,0,.45)}
.photo img{width:100%;height:100%;object-fit:contain;display:block}
.pname{position:absolute;left:64px;right:64px;top:760px;font-size:62px;font-weight:900;letter-spacing:-2px;line-height:1.2}
.pts{position:absolute;left:64px;right:64px;top:930px;display:flex;flex-direction:column;gap:12px}
.pts div{font-size:40px;font-weight:700;line-height:1.35;padding-left:56px;position:relative}.pts div:before{content:'✔';position:absolute;left:0;color:#ffe14d}
.meta{position:absolute;left:64px;right:64px;bottom:150px;display:flex;gap:16px;flex-wrap:wrap}
.meta span{background:#2c3038;border-radius:999px;padding:12px 24px;font-size:32px;font-weight:700}
.foot{position:absolute;left:64px;right:64px;bottom:56px;display:flex;justify-content:space-between;font-size:30px;font-weight:700;color:#b9bec8}
.howto{position:absolute;left:64px;right:64px;top:260px;display:flex;flex-direction:column;gap:30px}
.howto h2{font-size:84px;font-weight:900;letter-spacing:-2px}.howto h2 .y{color:#ffe14d}
.step{display:flex;gap:26px;align-items:center;background:#2c3038;border-radius:18px;padding:30px}
.step b{flex:none;width:76px;height:76px;border-radius:50%;background:#ffe14d;color:#111;font-size:44px;display:grid;place-items:center}
.step p{font-size:44px;font-weight:700;line-height:1.35}.step small{display:block;font-size:30px;color:#b9bec8;font-weight:600}"""


def c_foot(right="옆으로 →"):
    return f'<div class="foot"><span>@0315_pick</span><span>{right}</span></div>'


def c_prod(no, code, pid, name, pts, meta):
    return page(C_CSS, f"""<div class="ad">{AD}</div>
<div class="num">{no:02d}</div><div class="code">품번 {code}</div>
<div class="photo"><img src="{img(pid)}"></div><div class="pname">{name}</div>
<div class="pts">{''.join(f'<div>{p}</div>' for p in pts)}</div>
<div class="meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>{c_foot()}""")

