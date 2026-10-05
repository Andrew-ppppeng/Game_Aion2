from concurrent.futures import ThreadPoolExecutor
from capture import capture

EXTRA = {
    'global-firsthand-settings-corrected': ('https://space4games.com/en/games-en/aion-2-best-settings-guide/', 'Global'),
    'metabot-lesser-wings-retry': ('https://metabot.gg/en/aion-2/wings/lesser-daeva-wings', 'Global'),
    'metabot-methodology-retry': ('https://metabot.gg/en/aion-2/methodology', 'Global'),
    'metabot-elyos-starter-quest': ('https://metabot.gg/en/aion-2/quests/the-power-in-the-lake', 'Global'),
    'metabot-asmodian-starter-quest': ('https://metabot.gg/en/aion-2/quests/the-being-beneath-the-lake', 'Global'),
    'metabot-weapons': ('https://metabot.gg/en/aion-2/weapons', 'Global'),
    'metabot-skills': ('https://metabot.gg/en/aion-2/skills', 'Global'),
    'hub-query-example': ('https://aion2hub.com/database?q=Ludra', 'Mixed'),
    'hub-kr-filter': ('https://aion2hub.com/database?region=kr', 'KR/TW'),
    'steamdb-app': ('https://steamdb.info/app/3393110/', 'Global'),
}

with ThreadPoolExecutor(max_workers=5) as executor:
    for result in executor.map(capture, EXTRA.items()):
        print(*result, flush=True)
