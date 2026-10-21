"""게시물 폴더의 slides/*.html 을 1080x1350 JPEG(01.jpg, 02.jpg …)로 렌더링하고 post.json 의 slides 를 채운다.

사용: python scripts/render.py docs/posts/2026-10-26/A
(Claude 예약 작업이 매일 실행. Playwright + Chromium 필요)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright


def render(folder: Path) -> list[str]:
    htmls = sorted((folder / "slides").glob("*.html"))
    if not htmls:
        raise SystemExit(f"slides/*.html 없음: {folder}")
    names = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, h in enumerate(htmls, 1):
            pg.goto(h.resolve().as_uri(), wait_until="load")
            pg.wait_for_timeout(200)
            name = f"{i:02d}.jpg"
            pg.screenshot(path=str(folder / name), type="jpeg", quality=92,
                          clip={"x": 0, "y": 0, "width": 1080, "height": 1350})
            names.append(name)
        b.close()
    post_path = folder / "post.json"
    post = json.loads(post_path.read_text(encoding="utf-8"))
    post["slides"] = names
    post_path.write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return names


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(arg, render(Path(arg)))
