"""Capture a few public examples for offline UI verification; preserve raw evidence."""
import importlib.util
import json

spec = importlib.util.spec_from_file_location("collector", "scripts/collect-aion2-data.py")
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)
profiles = {
    "cleric": ("8iCddEXDDnuEC1Z-27KJQFh1WE-LrCLGFXYvv_9qwb8=", 2102),
    "chanter": ("65H2cAiY3daYz2B_Y5QZpknvCY4bUmBds5h0PSebIto=", 1102),
    "starter-cleric": ("65H2cAiY3daYz2B_Y5QZpt4oIiEaymR7nLSWEtFUAjQ=", 1102),
    "starter-chanter": ("eK4259aPQgDGnngd2n2_DFyf57YaKt4u8qb9eL3orBM=", 1103),
}
fixtures = collector.ROOT / "tests" / "fixtures"
fixtures.mkdir(parents=True, exist_ok=True)
observed = set()
for label, (cid, server) in profiles.items():
    identity = {"characterId": cid, "serverId": server, "region": "nae", "lang": "en-US"}
    values = {}
    for path in ("info", "equipment"):
        source = "https://aion2.plaync.com/api/character/" + path + "?" + collector.urllib.parse.urlencode(identity)
        data, meta = collector.fetch(source, label + "-" + path)
        values[path] = {"data": data, "meta": dict(meta, region="nae", locale="en", freshness="snapshot")}
    equipped = values["equipment"]["data"].get("equipment", {}).get("equipmentList", [])
    if not equipped:
        print(label + ": no equipment", flush=True)
        continue
    item = equipped[0]
    observed.add(item["id"])
    source = "https://aion2.plaync.com/api/character/equipment/item?" + collector.urllib.parse.urlencode(dict(identity, id=item["id"], enchantLevel=item["enchantLevel"], slotPos=item["slotPos"]))
    data, meta = collector.fetch(source, label + "-item")
    values["item"] = {"data": data, "meta": dict(meta, region="nae", locale="en", freshness="snapshot"), "error": None}
    values["character"] = {"data": {"info": values["info"]["data"], "equipment": values["equipment"]["data"], "sources": [values["info"]["meta"], values["equipment"]["meta"]]}, "meta": values["info"]["meta"], "error": None}
    (fixtures / (label + ".json")).write_text(json.dumps(values, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(label + ": observed weapon " + str(item["id"]), flush=True)

collector.fetch("https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6abd5fe5fa7da41c727d63c6", "coupon-deadline")
# Only IDs observed above; no guessed range or whole-database crawl.
path = collector.ROOT / "src" / "content" / "game-data" / "items.json"
items = json.loads(path.read_text(encoding="utf-8"))
extras = sorted(observed - {i["id"] for i in items})
for item_id in extras:
    record = {"id": item_id, "locales": {}, "regionChecks": {}}
    expected = None
    for region in collector.REGIONS:
        for locale, official_locale in collector.LOCALES.items():
            query = collector.urllib.parse.urlencode({"id": item_id, "enchantLevel": 0, "lang": official_locale, "region": region})
            source = "https://aion2.plaync.com/" + official_locale.lower() + "/api/gameconst/item?" + query
            data, meta = collector.fetch(source, f"extra-{item_id}-{region}-{locale}", allow_empty=region == "as")
            if data is None:
                record["regionChecks"].setdefault(region, {})[locale] = dict(meta, valid=False, reason="empty-response")
                continue
            if data.get("id") != item_id or not data.get("mainStats"):
                raise ValueError("Invalid observed item")
            signature = collector.numeric_signature(data)
            if expected is None:
                expected = signature
            if signature != expected:
                raise ValueError("Conflicting item variants")
            record["regionChecks"].setdefault(region, {})[locale] = dict(meta, valid=True)
            if region == "nae":
                record["locales"][locale] = {"item": data, "meta": meta}
    items.append(record)
temporary = path.with_suffix(".tmp")
temporary.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
temporary.replace(path)
print("Supplemental verified IDs: " + repr(extras), flush=True)
print("Evidence: " + str(collector.archive), flush=True)
