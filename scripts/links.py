"""승인 전 링크 입력용 파일 관리.

Claude가 그날 게시물을 만들면 links/<날짜>.md 를 같이 만든다.
사용자는 GitHub 웹/앱에서 그 파일을 열어 '파트너스:' 뒤에 쿠팡 파트너스 링크만 붙여넣는다.

    ## A · 0315news · 2026-10-26
    - A1 KF94 마스크 대용량
      쿠팡: https://www.coupang.com/vp/products/123
      파트너스: https://link.coupang.com/a/xxxx

`python scripts/links.py sync` 가 이 값을 post.json 으로 옮긴다.
`python scripts/links.py make <날짜>` 는 post.json 들로 입력 파일을 만든다.
"""
from __future__ import annotations

import re
import sys

from common import ROOT, iter_posts, load_config, save_post, publish_time

LINKS = ROOT / "links"
ITEM_RE = re.compile(r"^- ([ABC]\d?)-?(\d+)\s")  # "A-1", "A2-1" (예전 "A1"도 읽음)
PARTNER_RE = re.compile(r"^\s*파트너스:\s*(\S*)")
AFFILIATE_OK = re.compile(r"^https://(link\.coupang\.com|coupa\.ng|naver\.me|brandconnect\.naver\.com)/")


def make(date: str) -> str:
    cfg = load_config()
    lines = [f"# {date} 링크 입력",
             "", "각 상품의 '파트너스:' 뒤에 쿠팡 파트너스에서 만든 링크를 붙여넣고 저장(Commit)하세요.",
             "링크가 다 채워진 게시물만 정해진 시간에 발행됩니다.", ""]
    for path, post in iter_posts():
        if post["date"] != date:
            continue
        ch = cfg["channels"][post["channel"]]
        key = path.parent.name
        when = publish_time(post, cfg).strftime("%H:%M")
        lines.append(f"## {key} · {ch['ig_username']} · {post['date']} {when}")
        for prod in post.get("products", []):
            lines.append(f"- {key}-{prod['no']} {prod['name']}")
            lines.append(f"  쿠팡: {prod.get('coupang_url', '')}")
            lines.append(f"  파트너스: {prod.get('affiliate_url', '')}")
        lines.append("")
    LINKS.mkdir(exist_ok=True)
    out = LINKS / f"{date}.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    return str(out)


def parse(text: str) -> dict[tuple[str, int], str]:
    found, cur = {}, None
    for line in text.splitlines():
        m = ITEM_RE.match(line)
        if m:
            cur = (m.group(1), int(m.group(2)))
            continue
        m = PARTNER_RE.match(line)
        if m and cur:
            found[cur] = m.group(1).strip()
    return found


def sync() -> list[str]:
    """links/*.md → post.json. 바뀐 게시물 경로 목록을 돌려준다."""
    changed, warnings = [], []
    for md in sorted(LINKS.glob("*.md")) if LINKS.exists() else []:
        date = md.stem
        entries = parse(md.read_text(encoding="utf-8"))
        for path, post in iter_posts():
            if post["date"] != date:
                continue
            dirty = False
            for prod in post.get("products", []):
                key = path.parent.name
                url = entries.get((key, prod["no"]), "")
                if not url or url == prod.get("affiliate_url"):
                    continue
                if not AFFILIATE_OK.match(url):
                    warnings.append(f"{date} {key}-{prod['no']}: 파트너스 링크 형식이 아님 → {url}")
                    continue
                prod["affiliate_url"] = url
                dirty = True
            if dirty:
                save_post(path, post)
                changed.append(str(path.relative_to(ROOT)))
    for w in warnings:
        print("경고:", w)
    return changed


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "sync"
    if cmd == "make":
        print(make(sys.argv[2]))
    else:
        print("\n".join(sync()) or "변경 없음")
