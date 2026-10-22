"""발행 시간이 지났고 링크가 다 채워진 게시물을 인스타그램에 올린다.

Instagram API (Instagram 로그인 방식) 흐름
  1) 이미지마다 컨테이너 생성: POST /{ig-user-id}/media  image_url, is_carousel_item
  2) 캐러셀 컨테이너 생성:      POST /{ig-user-id}/media  media_type=CAROUSEL, children, caption
  3) 처리 완료 대기:             GET  /{container-id}?fields=status_code
  4) 발행:                       POST /{ig-user-id}/media_publish  creation_id
이미지는 JPEG, 공개 주소(GitHub Pages)에 올라가 있어야 한다.

사용:  python scripts/publish.py            실제 발행
       python scripts/publish.py --dry-run  무엇을 올릴지만 출력
"""
from __future__ import annotations

import os
import sys
import time

import requests

from common import POSTS, iter_posts, load_config, missing_links, now_kst, publish_time, save_post

GRAPH = "https://graph.instagram.com"
TIMEOUT = 30
MAX_ATTEMPTS = 3


class PublishError(RuntimeError):
    pass


def _check(r: requests.Response) -> dict:
    try:
        data = r.json()
    except ValueError:
        raise PublishError(f"HTTP {r.status_code}: {r.text[:300]}")
    if r.status_code >= 400 or "error" in data:
        err = data.get("error", {})
        raise PublishError(f"HTTP {r.status_code}: {err.get('message', data)}")
    return data


def wait_url(url: str, tries: int = 20) -> None:
    """Pages 배포가 끝나 이미지가 열릴 때까지 기다린다(최대 약 5분)."""
    for _ in range(tries):
        try:
            if requests.head(url, timeout=10).status_code == 200:
                return
        except requests.RequestException:
            pass
        time.sleep(15)
    raise PublishError(f"이미지가 공개 주소에 아직 없음: {url}")


def wait_container(cid: str, token: str, tries: int = 20) -> None:
    for _ in range(tries):
        d = _check(requests.get(f"{GRAPH}/{cid}", params={"fields": "status_code", "access_token": token}, timeout=TIMEOUT))
        st = d.get("status_code")
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise PublishError(f"컨테이너 처리 실패: {cid} {st}")
        time.sleep(5)
    raise PublishError(f"컨테이너 처리 대기 시간 초과: {cid}")


def build_caption(post: dict, cfg: dict) -> str:
    cap = post["caption"].strip()
    if post.get("products") and not cap.startswith("[광고]"):
        cap = cfg["disclosure"] + "\n\n" + cap
    return cap[:2200]


def publish(post: dict, folder_rel: str, cfg: dict) -> str:
    ch = cfg["channels"][post["channel"]]
    token = os.environ.get(ch["token_secret"], "")
    user_id = os.environ.get(ch["user_id_secret"], "")
    if not token or not user_id:
        raise PublishError(f"Secrets 없음: {ch['token_secret']} / {ch['user_id_secret']}")

    urls = [f"{cfg['site_base']}/{folder_rel}/{name}" for name in post["slides"]]
    for u in urls:
        if not u.lower().endswith((".jpg", ".jpeg")):
            raise PublishError(f"JPEG만 올릴 수 있음: {u}")
        wait_url(u)

    caption = build_caption(post, cfg)
    base = f"{GRAPH}/{user_id}"
    if len(urls) == 1:
        cid = _check(requests.post(f"{base}/media", data={"image_url": urls[0], "caption": caption, "access_token": token}, timeout=TIMEOUT))["id"]
    else:
        children = []
        for u in urls[:20]:
            d = _check(requests.post(f"{base}/media", data={"image_url": u, "is_carousel_item": "true", "access_token": token}, timeout=TIMEOUT))
            children.append(d["id"])
        for c in children:
            wait_container(c, token)
        cid = _check(requests.post(f"{base}/media", data={
            "media_type": "CAROUSEL", "children": ",".join(children), "caption": caption, "access_token": token}, timeout=TIMEOUT))["id"]
    wait_container(cid, token)
    # 처리 완료 직후에는 "Media ID is not available" 이 잠깐 나올 수 있어 몇 번 다시 시도한다
    for attempt in range(5):
        try:
            return _check(requests.post(f"{base}/media_publish", data={"creation_id": cid, "access_token": token}, timeout=TIMEOUT))["id"]
        except PublishError as e:
            if "not available" not in str(e) or attempt == 4:
                raise
            time.sleep(15)


def due_posts(cfg: dict):
    now = now_kst()
    for path, post in iter_posts():
        if post.get("status") in ("published", "hold"):
            continue
        if post.get("attempts", 0) >= MAX_ATTEMPTS:
            continue  # 3번 실패하면 멈춘다. attempts 를 지우면 다시 시도.
        if publish_time(post, cfg) > now:
            continue
        miss = missing_links(post)
        if miss:
            print(f"대기 {path.parent.name} {post['date']}: 링크 {len(miss)}개 비어 있음")
            continue
        yield path, post


def main() -> int:
    dry = "--dry-run" in sys.argv
    cfg = load_config()
    failures = 0
    for path, post in due_posts(cfg):
        rel = path.parent.relative_to(POSTS.parent).as_posix()
        label = f"{post['date']} {post['channel']}({cfg['channels'][post['channel']]['ig_username']})"
        if dry:
            print(f"발행 예정: {label} · {len(post['slides'])}장")
            continue
        try:
            media_id = publish(post, rel, cfg)
            post["status"] = "published"
            post["result"] = {"media_id": media_id, "published_at": now_kst().isoformat(timespec="seconds")}
            print(f"발행 완료: {label} → {media_id}")
        except (PublishError, requests.RequestException) as e:
            failures += 1
            post["status"] = "failed"
            post["attempts"] = post.get("attempts", 0) + 1
            post["result"] = {"error": str(e), "at": now_kst().isoformat(timespec="seconds")}
            print(f"발행 실패: {label} → {e}")
        save_post(path, post)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
