"""Read-only source extraction. Editorial selection and summaries are written manually."""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]

def discord():
    records = []
    out = ROOT / "research" / "discord"
    out.mkdir(parents=True, exist_ok=True)
    for path in sorted((ROOT / "discord" / "extracted").glob("*/*-page-*.html")):
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        channel = path.parent.name
        channel_records = []
        last_author = ""
        for node in soup.select("div.message[data-message-id]"):
            author = node.select_one(".author")
            if author:
                last_author = author.get_text(" ", strip=True)
            timestamp = node.select_one(".timestamp, .grouped-timestamp")
            body = node.select_one(".message-text")
            record = {"channel": channel, "message_id": node["data-message-id"], "author": last_author,
                      "timestamp": timestamp.get_text(" ", strip=True) if timestamp else "",
                      "text": body.get_text("\n", strip=True) if body else "",
                      "links": [a.get("href") for a in node.select(".message-text a[href], .embed a[href], .attachment a[href]")],
                      "source": str(path.relative_to(ROOT)).replace("\\", "/")}
            channel_records.append(record)
        records.extend(channel_records)
        (out / f"{channel}.json").write_text(json.dumps(channel_records, ensure_ascii=False, indent=2), encoding="utf-8")
        (out / f"{channel}.txt").write_text("\n\n".join(f"[{r['message_id']}] {r['timestamp']} {r['author']}\n{r['text']}\nLINKS: {' '.join(r['links'])}" for r in channel_records), encoding="utf-8")
        print(channel, "messages=", len(channel_records), "first=", channel_records[0]["timestamp"] if channel_records else "", "last=", channel_records[-1]["timestamp"] if channel_records else "")
    (out / "all_messages.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

def transcript(ids):
    from youtube_transcript_api import YouTubeTranscriptApi
    api = YouTubeTranscriptApi()
    out = ROOT / "research" / "youtube"
    out.mkdir(parents=True, exist_ok=True)
    for video_id in ids:
        try:
            listing = api.list(video_id)
            items = list(listing)
            chosen = next((t for t in items if t.language_code == "en" and not t.is_generated), None)
            chosen = chosen or next((t for t in items if t.language_code.startswith("en")), None) or items[0]
            fetched = chosen.fetch()
            metadata = {"video_id": video_id, "url": f"https://www.youtube.com/watch?v={video_id}",
                        "language": fetched.language, "language_code": fetched.language_code,
                        "is_generated": fetched.is_generated, "snippets": fetched.to_raw_data()}
            (out / f"{video_id}.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
            lines = [f"[{int(s.start)//60:02d}:{int(s.start)%60:02d}] {s.text}" for s in fetched]
            (out / f"{video_id}.txt").write_text("\n".join(lines), encoding="utf-8")
            print(video_id, "OK", fetched.language, "auto=", fetched.is_generated, "segments=", len(lines))
        except Exception as error:
            print(video_id, "FAILED", type(error).__name__, str(error)[:450])

def youtube_search():
    from yt_dlp import YoutubeDL
    data = json.loads((ROOT / "keywords-priority-20.json").read_text(encoding="utf-8"))
    keywords = [k for c in data["categories"] for k in c["keywords"]]
    out = ROOT / "research" / "youtube"
    out.mkdir(parents=True, exist_ok=True)
    def fetch(keyword):
        try:
            with YoutubeDL({"quiet": True, "extract_flat": True, "skip_download": True, "socket_timeout": 20}) as ydl:
                result = ydl.extract_info("ytsearch3:" + keyword, download=False)
            entries = [{"id": v.get("id"), "title": v.get("title"), "url": v.get("url"), "views": v.get("view_count"), "duration": v.get("duration")} for v in result.get("entries", [])]
            print(keyword, json.dumps(entries, ensure_ascii=False), flush=True)
            return {"keyword": keyword, "entries": entries}
        except Exception as error:
            print(keyword, "FAILED", type(error).__name__, flush=True)
            return {"keyword": keyword, "error": str(error)[:400]}
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, keywords))
    (out / "search_results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    if sys.argv[1] == "discord":
        discord()
    elif sys.argv[1] == "transcript":
        transcript(sys.argv[2:])
    elif sys.argv[1] == "youtube-search":
        youtube_search()
