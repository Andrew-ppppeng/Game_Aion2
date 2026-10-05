"""Append-only public-source capture for the SEO implementation batch."""
import hashlib
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent / "sources"
OUT.mkdir(parents=True, exist_ok=True)
SOURCE_URLS = {
    "server-transfer": "https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6abd2d50a279104f7d9d5ee2",
    "launch-access": "https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6ab85cc646be804931c31335",
    "latest-announcements": "https://api-global-community.plaync.com/aion2_global/board/notice_en/article/search/moreArticle?size=30",
    "steam-appdetails": "https://store.steampowered.com/api/appdetails?appids=3393110&l=english&cc=us",
    "steam-current-players": "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid=3393110",
    "steam-player-docs": "https://partner.steamgames.com/doc/webapi/ISteamUserStats",
    "global-download-entry": "https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en",
}

def capture(item):
    name, url = item
    target = OUT / f"{name}.json"
    if target.exists():
        print(name, "already archived; unchanged", flush=True)
        return
    checked = datetime.now(timezone.utc).isoformat(timespec="seconds")
    try:
        response = requests.get(url, timeout=30)
        try:
            body = response.json()
        except ValueError:
            body = response.text
        record = {"url": url, "checkedAt": checked, "status": response.status_code,
                  "finalUrl": response.url, "region": "Global", "gameVersion": None,
                  "body": body}
    except requests.RequestException as error:
        record = {"url": url, "checkedAt": checked, "region": "Global", "gameVersion": None,
                  "error": type(error).__name__ + ": " + str(error)}
    target.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    print(name, record.get("status", "unavailable"), flush=True)
    if name == "steam-current-players" and isinstance(record.get("body"), dict):
        print(json.dumps({"checkedAt": checked, "response": record["body"]}, ensure_ascii=False), flush=True)
    if name == "server-transfer" and isinstance(record.get("body"), dict):
        article = record["body"].get("article", {})
        html = article.get("content", {}).get("content", "")
        print(BeautifulSoup(html, "html.parser").get_text(" ", strip=True), flush=True)

def protect_originals():
    baseline = OUT.parent / "protected-originals.json"
    if baseline.exists():
        return
    paths = [ROOT / "keywords.json", ROOT / "keywords-priority-20.json"]
    for folder in [ROOT / "discord", ROOT / "research" / "youtube", ROOT / "research" / "localization"]:
        paths.extend(path for path in folder.rglob("*") if path.is_file())
    records = {str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
               for path in sorted(set(paths))}
    baseline.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print("protected originals", len(records), flush=True)

if __name__ == "__main__":
    protect_originals()
    with ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(capture, SOURCE_URLS.items()))
