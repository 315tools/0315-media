"""쿠팡 파트너스 Open API 클라이언트 (최종 승인 후 사용).

필요한 Secrets: COUPANG_ACCESS_KEY, COUPANG_SECRET_KEY
- deeplink(): 쿠팡 상품 URL → 파트너스 링크 (채널별 subId)
- search():   키워드 상품 검색  ※ 시간당 호출 제한이 빡빡함(10회로 보고됨). 하루 한 번 몰아서.
- goldbox():  골드박스 상품
- clicks()/orders(): 일별 실적 리포트

※ 아직 실제 키로 호출해 보지 않았다. API가 열리면 첫 호출로 응답 형식을 확인할 것.
"""
from __future__ import annotations

import hashlib
import hmac
import os
import time
from urllib.parse import urlencode

import requests

DOMAIN = "https://api-gateway.coupang.com"
BASE = "/v2/providers/affiliate_open_api/apis/openapi/v1"


def _auth(method: str, path: str, query: str) -> str:
    ak, sk = os.environ["COUPANG_ACCESS_KEY"], os.environ["COUPANG_SECRET_KEY"]
    signed = time.strftime("%y%m%dT%H%M%SZ", time.gmtime())
    msg = signed + method + path + query
    sig = hmac.new(sk.encode(), msg.encode(), hashlib.sha256).hexdigest()
    return f"CEA algorithm=HmacSHA256, access-key={ak}, signed-date={signed}, signature={sig}"


def _call(method: str, path: str, params: dict | None = None, body: dict | None = None) -> dict:
    query = urlencode(params or {})
    full = BASE + path
    r = requests.request(method, DOMAIN + full + (f"?{query}" if query else ""),
                         headers={"Authorization": _auth(method, full, query),
                                  "Content-Type": "application/json;charset=UTF-8"},
                         json=body, timeout=30)
    data = r.json()
    if str(data.get("rCode")) != "0":
        raise RuntimeError(f"쿠팡 API 오류 {r.status_code}: {data.get('rCode')} {data.get('rMessage')}")
    return data


def deeplink(urls: list[str], sub_id: str) -> dict[str, str]:
    d = _call("POST", "/deeplink", body={"coupangUrls": urls, "subId": sub_id})
    return {x["originalUrl"]: x["shortenUrl"] for x in d.get("data", [])}


def search(keyword: str, limit: int = 10, sub_id: str | None = None) -> list[dict]:
    p = {"keyword": keyword, "limit": limit}
    if sub_id:
        p["subId"] = sub_id
    return _call("GET", "/products/search", params=p).get("data", {}).get("productData", [])


def goldbox(sub_id: str | None = None) -> list[dict]:
    return _call("GET", "/products/goldbox", params={"subId": sub_id} if sub_id else None).get("data", [])


def clicks(start: str, end: str) -> list[dict]:
    return _call("GET", "/reports/clicks", params={"startDate": start, "endDate": end}).get("data", [])


def orders(start: str, end: str) -> list[dict]:
    return _call("GET", "/reports/orders", params={"startDate": start, "endDate": end}).get("data", [])
