"""쿠팡 파트너스 API 연결 확인 → reports/api_test.json (키 값은 기록하지 않음)"""
from __future__ import annotations

import json
import traceback

import coupang
from common import ROOT

out = {}
for name, fn in [
    ("deeplink", lambda: coupang.deeplink(["https://www.coupang.com/vp/products/9192743442"], "ig0315pick")),
    ("search", lambda: [{k: p.get(k) for k in ("productId", "productName", "productPrice", "productImage", "productUrl", "isRocket")}
                        for p in coupang.search("문풍지", limit=3)]),
]:
    try:
        out[name] = {"ok": True, "result": fn()}
    except Exception as e:  # noqa: BLE001
        out[name] = {"ok": False, "error": str(e)[:300], "trace": traceback.format_exc()[-500:]}
(ROOT / "reports").mkdir(exist_ok=True)
(ROOT / "reports" / "api_test.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v["ok"] for k, v in out.items()}))
