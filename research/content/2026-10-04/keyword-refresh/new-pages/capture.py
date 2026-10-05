"""Append-only public-page snapshots for new article review; no private endpoints."""
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import requests
from bs4 import BeautifulSoup

OUT = Path(__file__).resolve().parent
SOURCES = {
    'official-global-about': ('https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en', 'Global'),
    'official-global-notices': ('https://api-global-community.plaync.com/aion2_global/board/notice_en/article/search/moreArticle?size=100', 'Global'),
    'official-global-founder-update': ('https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6ac1229d5657e135c2f5ef65', 'Global'),
    'official-global-founder-original': ('https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6a4d7d47a729ca5877f5e1ef', 'Global'),
    'official-kr-chapter-one': ('https://about.ncsoft.com/en/news/article/aion2_update_260706', 'KR/TW'),
    'metabot-home': ('https://metabot.gg/en/aion-2', 'Global'),
    'metabot-items': ('https://metabot.gg/en/aion-2/items', 'Global'),
    'metabot-methodology': ('https://metabot.gg/en/aion-2/methodology', 'Global'),
    'metabot-wings': ('https://metabot.gg/en/aion-2/wings', 'Global'),
    'metabot-lesser-wings': ('https://metabot.gg/en/aion-2/wings/lesser-daeva-wings', 'Global'),
    'metabot-sealing-wings': ('https://metabot.gg/en/aion-2/wings/sealing-wings', 'Global'),
    'hub-database': ('https://aion2hub.com/database', 'Mixed'),
    'hub-item-example': ('https://aion2hub.com/database/items/110120003', 'Mixed'),
    'shugo-database': ('https://shugo.gg/database', 'Mixed'),
    'shugo-faq': ('https://shugo.gg/faq', 'Mixed'),
    'shugo-home': ('https://shugo.gg/', 'Mixed'),
    'global-firsthand-settings': ('https://space4games.com/en/games-en/aion-2-settings/', 'Global'),
    'global-firsthand-beginner': ('https://space4games.com/en/games-en/aion-2-beginner-guide/', 'Global'),
    'global-comparison-candidate': ('https://aion2maps.com/guides/global-differences/', 'Mixed'),
}

def capture(item):
    name, (url, region) = item
    target = OUT / (name + '.json')
    if target.exists():
        return name, 'preserved'
    record = {'requestedUrl': url, 'retrievedAt': datetime.now(timezone.utc).isoformat(timespec='seconds'), 'region': region, 'gameVersion': None}
    try:
        response = requests.get(url, timeout=25)
        record.update(status=response.status_code, finalUrl=response.url)
        try:
            record['body'] = response.json()
            article = record['body'].get('article', {}) if isinstance(record['body'], dict) else {}
            html = article.get('content', {}).get('content', '')
        except ValueError:
            record['body'] = response.text
            html = response.text
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            for element in soup(['script', 'style', 'nav', 'header', 'footer']):
                element.decompose()
            with (OUT / (name + '.txt')).open('x', encoding='utf-8') as handle:
                handle.write(soup.get_text('\n', strip=True))
        with target.open('x', encoding='utf-8') as handle:
            json.dump(record, handle, ensure_ascii=False, indent=2)
        return name, record['status']
    except Exception as error:
        record['error'] = str(error)
        with target.open('x', encoding='utf-8') as handle:
            json.dump(record, handle, ensure_ascii=False, indent=2)
        return name, type(error).__name__

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=6) as executor:
        for result in executor.map(capture, SOURCES.items()):
            print(*result, flush=True)
