"""인스타 장기 토큰(60일)을 새로 받아 GitHub Secrets 를 갱신한다. 매달 1일 Actions 가 실행.

필요: 각 채널 IG_TOKEN_* Secrets, 그리고 Secrets 를 고칠 수 있는 GH_PAT (fine-grained, 이 저장소 Secrets 쓰기 권한)
"""
from __future__ import annotations

import os
import subprocess
import sys

import requests

from common import load_config


def main() -> int:
    cfg = load_config()
    repo = os.environ["GITHUB_REPOSITORY"]
    bad = 0
    for key, ch in cfg["channels"].items():
        name = ch["token_secret"]
        tok = os.environ.get(name)
        if not tok:
            print(f"{key}: {name} 없음, 건너뜀")
            continue
        r = requests.get("https://graph.instagram.com/refresh_access_token",
                         params={"grant_type": "ig_refresh_token", "access_token": tok}, timeout=30)
        d = r.json()
        if "access_token" not in d:
            bad += 1
            print(f"{key}: 갱신 실패 → {d.get('error', d)}")
            continue
        subprocess.run(["gh", "secret", "set", name, "--repo", repo, "--body", d["access_token"]], check=True,
                       env={**os.environ, "GH_TOKEN": os.environ["GH_PAT"]})
        print(f"{key}: 갱신 완료, {int(d.get('expires_in', 0)) // 86400}일 유효")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
