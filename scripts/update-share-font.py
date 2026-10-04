"""Rebuild the Japanese social-card font subset (requires fontTools).

Run after adding Japanese titles or navigation labels:
    python scripts/update-share-font.py
The site serves this local subset; social previews need no Google Fonts request.
"""

from io import BytesIO
import json
from pathlib import Path
import urllib.request

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "https://raw.githubusercontent.com/google/fonts/main/ofl/notosansjp/NotoSansJP%5Bwght%5D.ttf"
LICENSE = "https://raw.githubusercontent.com/google/fonts/main/ofl/notosansjp/OFL.txt"


def strings(value):
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return "".join(strings(item) for item in value.values())
    if isinstance(value, list):
        return "".join(strings(item) for item in value)
    return ""


text = strings(json.loads((ROOT / "src/messages/ja.json").read_text(encoding="utf-8")))
for path in (ROOT / "src/content/ja").glob("*.json"):
    text += json.loads(path.read_text(encoding="utf-8"))["title"]
text += (ROOT / "src/i18n/tool-messages.ts").read_text(encoding="utf-8")
text += "AION 2 Wiki Global / 0123456789"

with urllib.request.urlopen(SOURCE, timeout=60) as response:
    font = TTFont(BytesIO(response.read()))
font = instantiateVariableFont(font, {"wght": 600}, inplace=True)
options = subset.Options()
options.flavor = "woff"
options.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
subsetter = subset.Subsetter(options=options)
subsetter.populate(text=text)
subsetter.subset(font)
font.flavor = "woff"
directory = ROOT / "public/fonts"
directory.mkdir(exist_ok=True)
font.save(directory / "aion2-share-ja.woff")
with urllib.request.urlopen(LICENSE, timeout=60) as response:
    (directory / "OFL-NotoSansJP.txt").write_bytes(response.read())
print(f"Saved Japanese share font: {(directory / 'aion2-share-ja.woff').stat().st_size} bytes")
