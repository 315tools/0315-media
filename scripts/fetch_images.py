"""상품 대표 이미지 내려받기: config/product_images.json (쿠팡 상품번호 → 이미지 주소) → assets/products/<번호>.jpg

쿠팡 이미지 서버는 작업 공간에서 막혀 있어 GitHub Actions 에서 실행한다. 이미 받은 파일은 건너뛴다.
"""
from __future__ import annotations

import json
import sys

import requests

from common import ROOT

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36",
      "Referer": "https://www.coupang.com/"}


def main() -> int:
    mapping = json.loads((ROOT / "config" / "product_images.json").read_text(encoding="utf-8"))
    out = ROOT / "assets" / "products"
    out.mkdir(parents=True, exist_ok=True)
    bad = 0
    for pid, url in mapping.items():
        target = out / f"{pid}.jpg"
        if target.exists() and target.stat().st_size > 1000:
            continue
        try:
            r = requests.get(url, headers=UA, timeout=30)
            r.raise_for_status()
            if not r.headers.get("content-type", "").startswith("image/"):
                raise ValueError(r.headers.get("content-type"))
            target.write_bytes(r.content)
            print("받음", pid, len(r.content))
        except Exception as e:  # noqa: BLE001
            print("실패", pid, e)
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
