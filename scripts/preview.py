"""하루치 게시물 미리보기 HTML 만들기: python scripts/preview.py 2026-10-22 출력경로.html"""
from __future__ import annotations

import base64
import html
import io
import json
import sys

from PIL import Image

from common import DOCS, load_config


def build(date: str, out: str) -> None:
    cfg = load_config()
    secs = []
    items = []
    for ckey, ch in cfg["channels"].items():
        times = ch.get("times") or [ch["default_time"]]
        for slot, folder in ((1, ckey), (2, ckey + "2")):
            d = DOCS / "posts" / date / folder
            if not (d / "post.json").exists():
                continue
            p = json.loads((d / "post.json").read_text(encoding="utf-8"))
            t = p.get("time") or times[min(p.get("slot", slot), len(times)) - 1]
            items.append((t, folder, ch, d, p))
    for t, key, ch, d, p in sorted(items, key=lambda x: x[0]):
        imgs = []
        for s in p["slides"]:
            im = Image.open(d / s).convert("RGB").resize((720, 900))
            b = io.BytesIO()
            im.save(b, "JPEG", quality=80)
            imgs.append("data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode())
        slides = "".join(f'<img src="{u}" alt="{key} {i + 1}장">' for i, u in enumerate(imgs))
        prods = "".join(
            f'<li><span class="n">{x["no"]}</span><span class="pn">{html.escape(x["name"])}</span>'
            f'<a href="{html.escape(x.get("affiliate_url") or x["coupang_url"])}" target="_blank" rel="noopener">링크 확인</a></li>'
            for x in p["products"])
        status = {"published": "발행됨", "failed": "실패"}.get(p.get("status"), "예정")
        secs.append(f'''<article class="post">
<header class="ph"><div class="av">{key}</div><div><b>@{ch["ig_username"]}</b><small>{html.escape(ch["title"])}</small></div><span class="time">{status} {t}</span></header>
<div class="car" tabindex="0" aria-label="슬라이드 {len(imgs)}장, 옆으로 넘겨 보기">{slides}</div>
<p class="cnt">{len(imgs)}장 · 옆으로 넘겨 보세요</p>
<pre class="cap">{html.escape(p["caption"])}</pre>
<h3>연결 상품</h3><ol class="pl">{prods}</ol>
</article>''')
    m, dd = int(date[5:7]), int(date[8:10])
    page = f'''<title>{m}/{dd} 인스타 발행 미리보기</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap">
<style>
/* 세로 피드: 인스타 게시물을 발행 순서대로 */
:root{{--bg:#eef0f3;--card:#fff;--fg:#16181d;--muted:#606773;--line:#d9dde3;--accent:#2f5bea;--chip:#e7ecfb;
--sans:"Noto Sans KR",system-ui,-apple-system,"Apple SD Gothic Neo",sans-serif}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#0f1114;--card:#181b20;--fg:#e9ecf1;--muted:#99a1ad;--line:#2b3038;--accent:#8aa6ff;--chip:#222a3d;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#0f1114;--card:#181b20;--fg:#e9ecf1;--muted:#99a1ad;--line:#2b3038;--accent:#8aa6ff;--chip:#222a3d;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--sans);line-height:1.55}}
main{{max-width:520px;margin:0 auto;padding-block:24px 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:28px}}
h1{{font-size:22px;margin:0;text-wrap:balance}} .lead{{margin:4px 0 0;color:var(--muted);font-size:14px}}
.post{{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;min-width:0}}
.ph{{display:flex;align-items:center;gap:10px;padding:12px 14px}}
.ph b{{display:block;font-size:15px}} .ph small{{color:var(--muted);font-size:12px}}
.av{{width:36px;height:36px;border-radius:50%;background:var(--accent);color:var(--card);display:grid;place-items:center;font-weight:700;flex:none}}
.time{{margin-left:auto;background:var(--chip);color:var(--accent);font-weight:700;font-size:13px;padding:4px 10px;border-radius:999px;font-variant-numeric:tabular-nums}}
.car{{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;background:var(--line)}}
.car img{{flex:0 0 100%;width:100%;aspect-ratio:4/5;scroll-snap-align:start;display:block;max-width:100%}}
.car:focus-visible{{outline:2px solid var(--accent);outline-offset:-2px}}
.cnt{{margin:8px 14px 0;font-size:12px;color:var(--muted)}}
.cap{{white-space:pre-wrap;word-break:keep-all;overflow-wrap:anywhere;font-family:var(--sans);font-size:14px;margin:10px 14px 0;padding-top:10px;border-top:1px solid var(--line)}}
h3{{font-size:12px;letter-spacing:.06em;color:var(--muted);margin:16px 14px 6px}}
.pl{{list-style:none;margin:0 0 14px;padding:0 14px;display:grid;gap:6px}}
.pl li{{display:flex;align-items:center;gap:10px;font-size:14px;min-width:0}}
.n{{flex:none;width:22px;height:22px;border-radius:6px;background:var(--chip);color:var(--accent);font-weight:700;font-size:12px;display:grid;place-items:center}}
.pn{{flex:1;min-width:0}} .pl a{{color:var(--accent);font-size:13px;flex:none}}
</style>
<main><div><h1>{m}월 {dd}일 발행 게시물</h1><p class="lead">세 채널(점심·퇴근길)에 올라갈 실제 이미지와 캡션입니다. 이미지는 옆으로 넘겨 보세요.</p></div>
{"".join(secs)}</main>'''
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
