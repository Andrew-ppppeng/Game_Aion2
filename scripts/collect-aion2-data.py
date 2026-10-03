"""Refresh the explicitly curated Global items; preserve every source response.

Run: python scripts/collect-aion2-data.py
This is a bounded, manually triggered collector, not a full database crawler.
"""
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGIONS = ["nae", "naw", "eu", "la", "as"]
LOCALES = {"en": "en-US", "ja": "ja-JP", "es": "es-ES", "de": "de-DE"}
# Observed on Global characters; inclusion is an example, not a best-in-slot claim.
ITEM_IDS = [110730048, 110830047, 115030041, 115030040, 210130038,
            210230052, 210330038, 210440047, 210530038, 210630038,
            210740043, 215230001, 310140035, 310230052, 310240035,
            310340035, 310430047, 310440018, 310900001, 311030001,
            110760001, 110860001]
now = datetime.datetime.now(datetime.timezone.utc)
archive = ROOT / "research" / "api" / now.strftime("%Y-%m-%d") / now.strftime("run-%H%M%S-%f")
archive.mkdir(parents=True)
manifest = []

def fetch(url, label, allow_empty=False):
    time.sleep(1)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={
                    "User-Agent": "Mozilla/5.0", "Accept": "application/json"}), timeout=20) as response:
                body = response.read()
                meta = {"sourceUrl": url, "service": "Global", "gameVersion": None,
                        "fetchedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        "status": response.status, "contentType": response.headers.get("Content-Type"),
                        "sha256": hashlib.sha256(body).hexdigest(), "bodyFile": label + f"-a{attempt}.body"}
            (archive / meta["bodyFile"]).write_bytes(body)
            (archive / (label + f"-a{attempt}.meta.json")).write_text(json.dumps(meta, indent=2), encoding="utf-8")
            manifest.append(meta)
            (archive / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
            if not body and allow_empty:
                return None, meta
            return json.loads(body), meta
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
            if isinstance(error, urllib.error.HTTPError) and error.code in (403, 429):
                raise RuntimeError("Upstream refused requests; collection stopped") from error
            if attempt == 2:
                raise
            time.sleep(3)

def numeric_signature(item):
    # Labels are localized. Numeric values and semantic IDs must agree.
    fields = ["id", "grade", "level", "levelValue", "equipLevel", "enchantLevel",
              "maxEnchantLevel", "maxExceedEnchantLevel", "subStatCount", "subStatRandom",
              "magicStoneSlotCount", "godStoneSlotCount", "tradable", "storable"]
    result = {k: item.get(k) for k in fields}
    for field in ("mainStats", "subStats"):
        result[field] = [{k: row.get(k) for k in ("id", "minValue", "value", "extra", "exceed")}
                         for row in item.get(field, [])]
    return json.dumps(result, sort_keys=True)

def main():
    items = []
    for item_id in ITEM_IDS:
        record = {"id": item_id, "locales": {}, "regionChecks": {}}
        expected = None
        for region in REGIONS:
            for locale, official_locale in LOCALES.items():
                query = urllib.parse.urlencode({"id": item_id, "enchantLevel": 0,
                                                "lang": official_locale, "region": region})
                url = "https://aion2.plaync.com/" + official_locale.lower() + "/api/gameconst/item?" + query
                payload, meta = fetch(url, f"item-{item_id}-{region}-{locale}", allow_empty=region == "as")
                if payload is None:
                    record["regionChecks"].setdefault(region, {})[locale] = dict(meta, valid=False, reason="empty-response")
                    continue
                if payload.get("id") != item_id or not payload.get("name") or not payload.get("mainStats"):
                    raise ValueError(f"Invalid item response: {item_id} / {region} / {locale}")
                signature = numeric_signature(payload)
                if expected is None:
                    expected = signature
                if signature != expected:
                    raise ValueError(f"Regional/localized numeric conflict: {item_id} / {region} / {locale}")
                record["regionChecks"].setdefault(region, {})[locale] = dict(meta, valid=True)
                if region == "nae":
                    record["locales"][locale] = {"item": payload, "meta": meta}
        items.append(record)
        valid_regions = [r for r, checks in record["regionChecks"].items() if all(c.get("valid") for c in checks.values())]
        print(f"Verified {len(items)}/{len(ITEM_IDS)} items in {','.join(valid_regions)}; all 4 languages checked", flush=True)
    metadata = {}
    for region in REGIONS:
        metadata[region] = {}
        for key in ("servers", "classes", "pcdata"):
            url = f"https://aion2.plaync.com/en-us/api/gameinfo/{key}?lang=en-US&region={region}"
            payload, meta = fetch(url, f"meta-{region}-{key}")
            metadata[region][key] = {"data": payload, "meta": meta}
    # Source bodies for the separately reviewed event records.
    for article_id in ["6ab30633fa7da41c727d632c", "6ab3018d49d41d00dc124ba6",
                       "6ab85cc646be804931c31335", "6abd32006b722c561dc6a8fc",
                       "6abd5fe5fa7da41c727d63c6"]:
        fetch("https://api-global-community.plaync.com/aion2_global/board/notice_en/article/" + article_id,
              "notice-" + article_id)
    output = ROOT / "src" / "content" / "game-data"
    output.mkdir(parents=True, exist_ok=True)
    # Publish only after the complete collection and conflict checks succeeded.
    for filename, data in [("items.json", items), ("meta.json", metadata)]:
        temp = output / (filename + ".tmp")
        temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temp.replace(output / filename)
    print(f"Published {len(items)} verified items. Raw responses: {archive}", flush=True)

if __name__ == "__main__":
    main()
