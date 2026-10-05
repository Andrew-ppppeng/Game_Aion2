"""Derive inventories from preserved captures; does not fetch or change raw sources."""
import csv, datetime, json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
ROOT=pathlib.Path(__file__).resolve().parent
RAW=ROOT/"raw"
def save_csv(name, rows, fields):
    with (ROOT/name).open("w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore");w.writeheader();w.writerows(rows)
sources=[]
for path in sorted(RAW.glob("*.meta.json")):
    meta=json.loads(path.read_text(encoding="utf-8"))
    row={k:meta.get(k,"") for k in ("label","url","final_url","kind","retrieved_at_utc","status","content_type","bytes","sha256","error")}
    row["body_file"]=("raw/"+meta["label"]+".body") if (RAW/(meta["label"]+".body")).exists() else ""
    sources.append(row)
save_csv("source-index.csv",sources,list(sources[0]))
(ROOT/"source-index.json").write_text(json.dumps(sources,ensure_ascii=False,indent=2),encoding="utf-8")
rows=json.loads((ROOT/"competitors-input.json").read_text(encoding="utf-8"))
for row in rows:
    label=row.pop("registration_label")
    meta=json.loads((RAW/(label+".meta.json")).read_text(encoding="utf-8")) if label else {}
    reg=next((e["eventDate"] for e in meta.get("events",[]) if e.get("eventAction")=="registration"),"")
    row.update(registration_utc=reg,registration_source=meta.get("url",""),checked_at="2026-10-03")
save_csv("competitors.csv",rows,list(rows[0]))
(ROOT/"competitors.json").write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
api=[]
for source in sources:
    if not source["label"].startswith("api-"): continue
    source=dict(source); semantic="request_failed"; keys=[]
    path=ROOT/source["body_file"] if source["body_file"] else None
    if source["status"]==200 and path and path.exists():
        try:
            data=json.loads(path.read_text(encoding="utf-8"))
            keys=list(data) if isinstance(data,dict) else ["list"]
            semantic="json_received"
            if isinstance(data,dict) and data.get("id")==0: semantic="empty_item_id_zero"
            elif isinstance(data,dict) and "rankingList" in data and not data["rankingList"]: semantic="empty_ranking_no_season"
        except (ValueError,UnicodeError): semantic="non_json_http_200"
    source["semantic_result"]=semantic;source["top_keys"]=";".join(keys);api.append(source)
save_csv("api-verification.csv",api,list(api[0]))
print(json.dumps({"competitors":len(rows),"raw_source_captures":len(sources),"api_routes_probed":len(api),"retrieved_at_min":min(r["retrieved_at_utc"] for r in sources),"retrieved_at_max":max(r["retrieved_at_utc"] for r in sources)},ensure_ascii=False))

