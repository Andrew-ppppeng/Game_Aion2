"""Read-only sanity check for the final local production preview."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.request import urlopen

class Cards(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "data-video-id" in data:
            self.ids.add(data["data-video-id"])

base = "http://127.0.0.1:3100"
pages = {slug: urlopen(f"{base}/{slug}", timeout=20).read().decode("utf-8") for slug in ["beginner-videos", "crafting", "daily-weekly-checklist"]}
cards = Cards()
cards.feed(pages["beginner-videos"])
assert len(cards.ids) == 17
assert "6 Ore" in pages["crafting"]
assert "old Duty-tab" not in pages["daily-weekly-checklist"]
json.loads((Path(__file__).parent / "completion.json").read_text(encoding="utf-8"))
print("Final production preview passed: 17 video cards, exact recipe text, trimmed daily guide and valid audit.")
