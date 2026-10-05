"""Archive this refresh's public primary sources without overwriting prior logs."""
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

OUT = Path(__file__).resolve().parent
SOURCES = {
    "steam-appdetails": ("https://store.steampowered.com/api/appdetails?appids=3393110&cc=us&l=english", "Global"),
    "global-about": ("https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en", "Global"),
    "chapter-one": ("https://about.ncsoft.com/en/news/article/aion2_update_260706", "KR/TW"),
    "notmeter": ("https://notmeter.com/", "Mixed"),
    "notmeter-releases": ("https://api.github.com/repos/Not4You-Dev/NotMeter-Releases/releases", "Mixed"),
    "operation-policy": ("https://www.plaync.com/policy/operation/aion2global/en", "Global"),
    "purple-region": ("https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6abd3200a279104f7d9d5eeb", "Global"),
    "windows-dxdiag": ("https://support.microsoft.com/en-us/windows/hardware/display-graphics/microsoft-basic-display-adapter-in-windows", "Windows 10/11"),
}

def collect(item):
    key, (url, region) = item
    checked = datetime.now(timezone.utc).isoformat(timespec="seconds")
    record = {"url": url, "checkedAt": checked, "region": region, "gameVersion": None}
    try:
        response = requests.get(url, timeout=25)
        record.update(status=response.status_code, finalUrl=response.url)
        try:
            record["body"] = response.json()
        except ValueError:
            record["body"] = response.text
            with (OUT / f"{key}-text.txt").open("x", encoding="utf-8") as file:
                file.write(BeautifulSoup(response.text, "html.parser").get_text(" ", strip=True))
    except requests.RequestException as error:
        record["error"] = type(error).__name__ + ": " + str(error)
    with (OUT / f"{key}.json").open("x", encoding="utf-8") as file:
        json.dump(record, file, ensure_ascii=False, indent=2)
    print(key, record.get("status", record.get("error")), flush=True)

with ThreadPoolExecutor(max_workers=5) as pool:
    list(pool.map(collect, SOURCES.items()))
