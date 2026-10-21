"""채널별 프로필 링크 페이지 생성 → docs/<slug>/index.html

인스타 프로필 링크에 https://<주인>.github.io/0315-media/<slug>/ 를 넣는다.
발행된 게시물의 상품을 최신순으로, 게시물 날짜·번호와 함께 보여준다.
"""
from __future__ import annotations

import html

from common import DOCS, iter_posts, load_config

PAGE = """<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · 링크</title>
<style>
:root{{--bg:#f4f5f2;--card:#fff;--fg:#15171a;--muted:#5f6662;--line:#dcdfd9;--accent:#1f5eff}}
@media (prefers-color-scheme:dark){{:root{{--bg:#111312;--card:#1a1d1b;--fg:#ecefea;--muted:#9aa29d;--line:#2d322f;--accent:#7b9dff}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font-family:system-ui,-apple-system,"Apple SD Gothic Neo","Noto Sans KR",sans-serif;line-height:1.5}}
main{{max-width:560px;margin:0 auto;padding:20px 16px 48px}}
h1{{font-size:22px;margin:0 0 4px}} .handle{{color:var(--muted);margin:0 0 16px}}
.ad{{background:var(--fg);color:var(--bg);border-radius:8px;padding:10px 12px;font-size:13px;font-weight:600;margin-bottom:20px}}
h2{{font-size:14px;color:var(--muted);margin:24px 0 8px;font-weight:600}}
a.item{{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;margin-bottom:8px;color:inherit;text-decoration:none}}
.no{{flex:none;width:32px;height:32px;border-radius:8px;background:var(--accent);color:#fff;display:grid;place-items:center;font-weight:700}}
.name{{font-weight:600}} .empty{{color:var(--muted)}}
</style></head><body><main>
<h1>{title}</h1><p class="handle">@{ig}</p>
<div class="ad">{disclosure}</div>
{body}
</main></body></html>
"""


def build() -> list[str]:
    cfg = load_config()
    out = []
    groups: dict[str, list[dict]] = {k: [] for k in cfg["channels"]}
    for _, post in iter_posts():
        if post.get("status") == "published" and post.get("products"):
            groups[post["channel"]].append(post)
    for key, ch in cfg["channels"].items():
        sections = []
        for post in sorted(groups[key], key=lambda p: p["date"], reverse=True)[:30]:
            items = "".join(
                f'<a class="item" href="{html.escape(p["affiliate_url"])}" rel="sponsored nofollow">'
                f'<span class="no">{p["no"]}</span><span class="name">{html.escape(p["name"])}</span></a>'
                for p in post["products"] if p.get("affiliate_url"))
            title = html.escape(post.get("title", ""))
            sections.append(f"<h2>{post['date']} · {title}</h2>{items}")
        body = "".join(sections) or '<p class="empty">아직 올라온 상품이 없어요.</p>'
        page = PAGE.format(title=html.escape(ch["title"]), ig=ch["ig_username"],
                           disclosure=html.escape(cfg["disclosure"].replace("[광고] ", "광고 · ")), body=body)
        target = DOCS / ch["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page, encoding="utf-8")
        out.append(str(target))
    return out


if __name__ == "__main__":
    print("\n".join(build()))
