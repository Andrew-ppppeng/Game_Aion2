"""Archive a public character's localized responses for repeatable UI checks."""
import importlib.util
import json

spec = importlib.util.spec_from_file_location("collector", "scripts/collect-aion2-data.py")
collector = importlib.util.module_from_spec(spec)
spec.loader.exec_module(collector)
cid = "8iCddEXDDnuEC1Z-27KJQFh1WE-LrCLGFXYvv_9qwb8="
for locale in ("ja", "es", "de"):
    identity = {"characterId": cid, "serverId": 2102, "region": "nae", "lang": collector.LOCALES[locale]}
    responses = {}
    for path in ("info", "equipment"):
        source = "https://aion2.plaync.com/api/character/" + path + "?" + collector.urllib.parse.urlencode(identity)
        data, meta = collector.fetch(source, locale + "-" + path)
        responses[path] = {"data": data, "meta": dict(meta, region="nae", locale=locale, freshness="snapshot")}
    slot = responses["equipment"]["data"]["equipment"]["equipmentList"][0]
    source = "https://aion2.plaync.com/api/character/equipment/item?" + collector.urllib.parse.urlencode(dict(identity, id=slot["id"], enchantLevel=slot["enchantLevel"], slotPos=slot["slotPos"]))
    data, meta = collector.fetch(source, locale + "-item")
    fixture = {"character": {"data": {"info": responses["info"]["data"], "equipment": responses["equipment"]["data"], "sources": [responses["info"]["meta"], responses["equipment"]["meta"]]}, "meta": responses["info"]["meta"], "error": None},
               "item": {"data": data, "meta": dict(meta, region="nae", locale=locale, freshness="snapshot"), "error": None}}
    path = collector.ROOT / "tests" / "fixtures" / ("cleric-" + locale + ".json")
    path.write_text(json.dumps(fixture, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Captured " + locale, flush=True)
print("Evidence: " + str(collector.archive), flush=True)
