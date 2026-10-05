"""Append audit results without changing keyword libraries or raw archives."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat(timespec='seconds')
baseline = json.loads((OUT / 'protected-originals.json').read_text(encoding='utf-8'))
changed = []
for name, digest in baseline.items():
    path = ROOT / name
    actual = hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None
    if actual != digest:
        changed.append({'path': name, 'expectedSha256': digest, 'actualSha256': actual})
audit = {'checkedAt': now, 'protectedFiles': len(baseline), 'changed': changed,
         'keywordLibrariesUnchanged': not any(item['path'] in ('keywords.json', 'keywords-priority-20.json') for item in changed)}
with (OUT / 'protected-originals-verification.json').open('x', encoding='utf-8') as file:
    json.dump(audit, file, ensure_ascii=False, indent=2)
    file.write('\n')

community = {
 'reviewRecordedAt': now,
 'reviewDate': '2026-10-03',
 'method': 'Public web source reads and existing original Discord archive; observations below are review notes rather than an HTML snapshot.',
 'sources': [
  {'url': 'https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/', 'region': 'Global', 'version': 'Developer-pinned official Discord invitation', 'publicationDate': '2026-04-20', 'observations': ['nc_community marked developer', 'Links discord.gg/aion2official', 'Official post has translations including Japanese, Spanish and German']},
  {'url': 'https://www.twitch.tv/aion2official', 'region': 'Global', 'version': 'Official broadcast channel', 'publicationDate': None, 'archive': 'research/discord/aion2_news.json', 'observations': ['Archived Global announcement links this channel alongside @AION2Official YouTube', 'No current stream schedule inferred']},
  {'url': 'https://www.reddit.com/r/Aion2/', 'region': 'Mixed', 'version': 'Community landing page', 'publicationDate': None, 'observations': ['Page identity r/Aion2 read in web source', 'Questions, guides and third-party tools present', 'Individual post game version and author must be checked separately']},
  {'url': 'https://forum.gamer.com.tw/B.php?bsn=82913', 'region': 'TW', 'version': 'Community board identity only', 'publicationDate': None, 'identitySource': 'https://forum.gamer.com.tw/C.php?bsn=82913&snA=3807', 'observations': ['Indexed native Bahamut post labels AION2 board with bsn=82913', 'Direct board read returned 403 Forbidden', 'No current Global instructions extracted or endorsed']},
  {'url': 'https://steamcommunity.com/app/3393110/allnews/?l=dutch', 'region': 'Global', 'version': 'Indexed launch FAQ fragment only', 'publicationDate': None, 'observations': ['Search returned NC statement that controller is playable but not officially supported', 'Opening the news feed showed recent posts and omitted that older FAQ', 'Specific news page was unavailable in browser region; not used as fully read launch FAQ', 'Public guide retains bounded support description instead of supplying an untested configuration']}
 ],
 'regionalEntryReview': 'research/content/2026-10-03/class-launch-sources/tw-entry-web-review.json'
}
with (OUT / 'community-source-review.json').open('x', encoding='utf-8') as file:
    json.dump(community, file, ensure_ascii=False, indent=2)
    file.write('\n')
print(json.dumps(audit, ensure_ascii=False))
assert not changed, 'Protected originals changed; inspect report before claiming preservation.'
