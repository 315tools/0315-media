"""상품 후보 찾기 (쿠팡 파트너스 API, GitHub Actions 에서 실행)

입력: requests/<날짜>.json
  {"searches": [{"key": "A", "keyword": "가습기", "limit": 8}, ...],
   "urls": [{"key": "C", "url": "https://www.coupang.com/vp/products/123"}]}   (urls 는 선택)
  key 는 링크에 붙일 채널(A·B·C) — config/channels.json 의 sub_id 로 실적이 채널별로 나뉜다.
출력: catalog/<날짜>.json  — 검색어별 후보 목록
  각 후보: productId, name, price, isRocket, isFreeShipping, rank, image(assets/products/<id>.jpg),
           coupang_url, affiliate_url(링크 생성 실패 = 판매자 제한이면 null)
※ 검색 API 는 시간당 호출 수가 적다(약 10회). 하루 검색어는 8개 이하로.
"""
from __future__ import annotations

import json
import sys
import time

import requests

import coupang
from common import ROOT, load_config

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130 Safari/537.36"}


def save_image(pid: int, url: str) -> str | None:
    target = ROOT / "assets" / "products" / f"{pid}.jpg"
    if target.exists() and target.stat().st_size > 1000:
        return str(target.relative_to(ROOT))
    try:
        r = requests.get(url, headers=UA, timeout=30)
        r.raise_for_status()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(r.content)
        return str(target.relative_to(ROOT))
    except Exception as e:  # noqa: BLE001
        print("사진 실패", pid, e)
        return None


def link(url: str, sub_id: str) -> str | None:
    try:
        return next(iter(coupang.deeplink([url], sub_id).values()), None)
    except Exception as e:  # noqa: BLE001  판매자 제한 상품 등
        print("링크 실패", url, str(e)[:120])
        return None


def run(date: str) -> None:
    cfg = load_config()
    req = json.loads((ROOT / "requests" / f"{date}.json").read_text(encoding="utf-8"))
    out_path = ROOT / "catalog" / f"{date}.json"
    out = json.loads(out_path.read_text(encoding="utf-8")) if out_path.exists() else {"searches": {}, "urls": []}
    for s in req.get("searches", []):
        kw, key = s["keyword"], s.get("key", "C")
        if kw in out["searches"]:
            continue
        sub = cfg["channels"][key]["sub_id"]
        try:
            items = coupang.search(kw, limit=min(int(s.get("limit", 8)), 10), sub_id=sub)
        except Exception as e:  # noqa: BLE001
            out["searches"][kw] = {"key": key, "error": str(e)[:200], "items": []}
            continue
        seen, rows = set(), []
        for it in items:
            pid = it.get("productId")
            if pid in seen:
                continue
            seen.add(pid)
            curl = f"https://www.coupang.com/vp/products/{pid}"
            rows.append({
                "productId": pid, "name": it.get("productName"), "price": it.get("productPrice"),
                "isRocket": it.get("isRocket"), "isFreeShipping": it.get("isFreeShipping"), "rank": it.get("rank"),
                "image": save_image(pid, it.get("productImage", "")),
                "coupang_url": curl, "affiliate_url": link(curl, sub),
            })
            time.sleep(0.5)
        out["searches"][kw] = {"key": key, "items": rows}
        time.sleep(2)
    for u in req.get("urls", []):
        if any(x["url"] == u["url"] for x in out["urls"]):
            continue
        sub = cfg["channels"][u.get("key", "C")]["sub_id"]
        out["urls"].append({"key": u.get("key", "C"), "url": u["url"], "affiliate_url": link(u["url"], sub)})
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n = sum(len(v["items"]) for v in out["searches"].values())
    ok = sum(1 for v in out["searches"].values() for x in v["items"] if x["affiliate_url"])
    print(f"검색어 {len(out['searches'])}개, 후보 {n}개, 링크 생성 {ok}개")


if __name__ == "__main__":
    dates = sys.argv[1:] or sorted(p.stem for p in (ROOT / "requests").glob("*.json"))[-1:]
    for d in dates:
        run(d)
