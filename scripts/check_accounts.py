"""연결 확인(읽기 전용): 각 채널 토큰으로 계정 정보와 남은 발행 한도를 조회한다. 게시물은 올리지 않는다."""
from __future__ import annotations

import os
import sys

import requests

from common import load_config

GRAPH = "https://graph.instagram.com"


def main() -> int:
    cfg = load_config()
    bad = 0
    for key, ch in cfg["channels"].items():
        tok, uid = os.environ.get(ch["token_secret"], ""), os.environ.get(ch["user_id_secret"], "")
        if not tok or not uid:
            print(f"[{key}] {ch['ig_username']}: Secrets 없음")
            bad += 1
            continue
        me = requests.get(f"{GRAPH}/me", params={"fields": "user_id,username,account_type", "access_token": tok}, timeout=30).json()
        if "error" in me:
            print(f"[{key}] {ch['ig_username']}: 토큰 오류 → {me['error'].get('message')}")
            bad += 1
            continue
        ok_user = me.get("username") == ch["ig_username"]
        ok_id = str(me.get("user_id")) == uid
        lim = requests.get(f"{GRAPH}/{uid}/content_publishing_limit",
                           params={"fields": "quota_usage,config", "access_token": tok}, timeout=30).json()
        quota = (lim.get("data") or [{}])[0]
        print(f"[{key}] {me.get('username')} ({me.get('account_type')}) "
              f"아이디일치={'O' if ok_user else 'X'} 사용자ID일치={'O' if ok_id else 'X'} "
              f"오늘사용={quota.get('quota_usage', '?')} 한도={quota.get('config', {}).get('quota_total', '?')}"
              + (f" 한도조회오류={lim['error'].get('message')}" if "error" in lim else ""))
        if not (ok_user and ok_id):
            bad += 1
    print("결과:", "전부 정상" if bad == 0 else f"문제 {bad}건")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
