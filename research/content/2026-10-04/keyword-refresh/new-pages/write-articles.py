"""Hand-written, four-language articles. Never overwrite captured source originals."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PAGES = {}
RELATED = {'database': ['map','builds','classes','steam'], 'wings': ['leveling','builds','map','pvp','monetization'], 'global-changes': ['guide','leveling','classes','monetization','server']}

def source(id, title, url, kind, region, version, published=None):
    return {'id': id, 'title': title, 'url': url, 'kind': kind, 'region': region,
            'publishedAt': published, 'version': version}

SOURCES = {
    'database': [
        source('gaming-tools-items', 'AION 2 Global Database: Items', 'https://aion2.gaming.tools/items', 'tool', 'Global', 'Live list opened 2026-10-04, Global 1.0.21.0; individual entries may retain Global Playtest labels; current-client availability is not inferred'),
        source('gaming-tools-detail', 'Abyssal Forge: Weapon Selection Chest (Bound)', 'https://aion2.gaming.tools/items/533700175', 'tool', 'Global', 'Actual detail navigation verified 2026-10-04; choose-one contents and item relationships; Playtest 1.0.21.0 label kept in internal log'),
        source('gaming-tools-skills', 'All AION 2 Skills', 'https://aion2.gaming.tools/skills', 'tool', 'Global', 'Live class/type filter list opened 2026-10-04'),
        source('gaming-tools-quests', 'All AION 2 Quests', 'https://aion2.gaming.tools/quests', 'tool', 'Global', 'Live faction/region/type list opened 2026-10-04'),
        source('metabot-global', 'AION 2 Database and Tools', 'https://metabot.gg/en/aion-2', 'tool', 'Global', 'Catalogue opened 2026-10-04; its methodology identifies global client build 0.0.4387.0, not an independently attested current retail build'),
        source('hub-database', 'AION 2 Item Database', 'https://aion2hub.com/database', 'tool', 'Mixed', 'Global/Korea-Taiwan filters, type/class/grade filters and q=Ludra form query verified 2026-10-04'),
        source('hub-item-example', "Ludra’s Blade of Extinction", 'https://aion2hub.com/database/items/110120003', 'tool', 'Mixed', 'Opened 2026-10-04: page labels Global Launch Scale Test client 2026-09-19 and KR/TW v110 2026-09-09; no live obtainable-content claim'),
        source('shugo-faq', 'AION 2 and Shugo.GG FAQ', 'https://shugo.gg/faq', 'tool', 'Mixed', 'Opened 2026-10-04; Global character options differ from KR/TW item dictionary coverage; some FAQ prose is stale and not copied as current launch timing'),
        source('shugo-status', 'AION 2 Armory', 'https://shugo.gg/', 'tool', 'Mixed', 'Opened 2026-10-04 with degraded character APIs; usable search UI does not establish a successful current profile lookup'),
    ],
    'wings': [
        source('global-official-flight', 'About the Game: Flight', 'https://aion2.plaync.com/en-us/about/index', 'official', 'Global', 'Public Global about-en content API captured 2026-10-04; general flight/customization only'),
        source('global-dungeon-flight', '[AION 2] Dungeon Live Gameplay Showcase', 'https://www.youtube.com/watch?v=S_TjiOh33a4', 'official', 'Global', 'Official showcase 25:42–25:59 confirms wing flight in some dungeon sections; subtitle snapshot retained under research/content/2026-10-02/leveling', '2026-09-04'),
        source('global-settings-firsthand', 'AION 2 Best Settings: Graphics, FPS, Controls and Keybinds', 'https://space4games.com/en/games-en/aion-2-best-settings-guide/', 'player', 'Global', 'Kevin Link firsthand Global LST keyboard menu screenshots; V, Shift, Space, Ctrl+R/F and Alt+C captured 2026-10-04; custom bindings take precedence', '2026-09-28'),
        source('global-starter-firsthand', 'AION 2 Beginner Guide', 'https://space4games.com/en/games-en/aion-2-beginner-guide/', 'player', 'Global', 'Firsthand Global LST early Ascension/Wings and gameplay-wing vs shop-cosmetic distinction captured 2026-10-04; recommended milestone not hard unlock requirement', '2026-09-28'),
        source('global-lesser-wing', 'Lesser Daeva Wings', 'https://metabot.gg/en/aion-2/wings/lesser-daeva-wings', 'tool', 'Global', 'Web page opened 2026-10-04: equipped and owned panels, both faction versions, starter quest links; HTML capture timeout logged separately; no numerical stats or upgrade prices copied'),
        source('global-elyos-wing-quest', 'The Power in the Lake', 'https://metabot.gg/en/aion-2/quests/the-power-in-the-lake', 'tool', 'Global', 'Global client 0.0.4387.0 labelled record opened/captured 2026-10-04: starter wing, Daminu, Poeta, next Fledgling Wings'),
        source('global-asmodian-wing-quest', 'The Being Beneath the Lake', 'https://metabot.gg/en/aion-2/quests/the-being-beneath-the-lake', 'tool', 'Global', 'Global client 0.0.4387.0 labelled record opened 2026-10-04: starter wing, Elvida, Ishalgen, next Spread Your Wings; HTTP archive request timed out, web inspection succeeded'),
        source('founder-pack-cosmetic-original', 'Founder’s Packs', 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6a4d7d47a729ca5877f5e1ef', 'official', 'Global', 'Original image announcement captured through public community API 2026-10-04; Ultimate cosmetic Blazing Sun, no numerical advantage copied'),
        source('founder-cosmetic-change', 'Founder’s Packs Cosmetics Soon Available On All Characters', 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac1229d5657e135c2f5ef65', 'official', 'Global', 'Captured 2026-10-04: Blazing Sun included in planned account/all-server cosmetic sharing; implementation pending after Early Access; membership and two chests excluded', '2026-10-03'),
    ],
    'global-changes': [
        source('global-roster', 'About the Game', 'https://aion2.plaync.com/en-us/about/index', 'official', 'Global', 'Public content API captured 2026-10-04: eight Global class roster, Verteron/Altgard world presentation'),
        source('global-dungeon-showcase', '[AION 2] Dungeon Live Gameplay Showcase', 'https://www.youtube.com/watch?v=S_TjiOh33a4', 'official', 'Global', 'Global level-45 progression; subtitle timestamps retained under research/content/2026-10-02/leveling; regional cap distinction retained', '2026-09-04'),
        source('kr-tw-chapter-one', 'AION 2 Rolls Out Chapter 1: Lands of Sand and Snow', 'https://about.ncsoft.com/en/news/article/aion2_update_260706', 'official', 'KR/TW', 'Official Chapter 1 press release recaptured 2026-10-04: cap50, Brawler, new regional maps and level50 dungeons; a content-stage comparison, not a complete latest-patch manifest', '2026-07-06'),
        source('global-server-access', 'Server Access Schedule and Server List', 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab85cc646be804931c31335', 'official', 'Global', 'Official launch/region schedule reviewed 2026-10-04 in secondary-updates sources; September30 and October5 at13:00UTC'),
        source('founder-cosmetic-change', 'Founder’s Packs Cosmetics Soon Available On All Characters', 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6ac1229d5657e135c2f5ef65', 'official', 'Global', 'Captured 2026-10-04: planned sharing across account/server, completion afterEarlyAccess, one-time rewards excluded', '2026-10-03'),
    ],
}

def article(slug, locale, title, description, summary, answer, sections, visual, body, next_slug):
    meta = {
        'title': title, 'description': description, 'summary': summary, 'quickAnswer': answer,
        'toc': [{'id': key, 'title': value} for key, value in sections],
        'visuals': {'workflow': {'title': visual[0], 'caption': visual[1], 'steps': [
            {'label': label, 'description': text} for label, text in visual[2]
        ]}}, 'inlineNext': [next_slug],
    }
    # SteamDB blocked automated access in this session; explain its scope without
    # presenting the unverified app page as a checked working resource.
    replacements = {
        '[AION 2 SteamDB record](https://steamdb.info/app/3393110/)': 'AION 2 SteamDB record',
        '[AION 2のSteamDBページ](https://steamdb.info/app/3393110/)': 'AION 2のSteamDBページ',
        '[ficha de AION 2 en SteamDB](https://steamdb.info/app/3393110/)': 'ficha de AION 2 en SteamDB',
        '[AION 2 Eintrag in SteamDB](https://steamdb.info/app/3393110/)': 'AION 2 Eintrag in SteamDB',
    }
    for old, new in replacements.items():
        body = body.replace(old,new)
    PAGES.setdefault(slug, {})[locale] = (meta, body.strip() + '\n')

article('database', 'en', 'AION 2 Database: Items, Skills and Character Lookup',
    'Find AION 2 item, skill, quest and drop databases, choose the right region, and distinguish character lookup from SteamDB product information.',
    'Choose a database by the question you need to answer: equipment, skill details, quest steps, a character profile or Steam product records.',
    'Use gaming.tools or MetaBot for Global item, skill and quest records. AION2 Hub adds Global and KR/TW item filters. For a player, use character lookup; SteamDB covers the Steam product rather than in-game drops.',
    [('choose-a-database','Choose a database for your task'),('find-an-item','Find an item and its acquisition route'),('skills-drops-and-quests','Look up skills, drops and quests'),('character-database','Find a character or player profile'),('steamdb-product-record','What SteamDB tells you'),('check-a-record','Check a record before spending resources')],
    ('From a name to a usable answer','Match the region and the exact record before planning your next run.',[
        ('Choose the region','Start with Global, KR or TW; language alone does not identify the game version.'),
        ('Open the exact record','Match the name, faction, item type and level requirement.'),
        ('Follow its acquisition links','Check the quest, monster, chest or recipe rather than stopping at the stat preview.'),
        ('Confirm in game','Check that the content is open and the reward or recipe exists before spending currency.')]),
    '''An **AION 2 database** helps you answer a specific question: what an item does, where it comes from, what a skill changes at the next level, or which quest comes next. A **character database** instead shows a player's profile. Choose the right kind of lookup before searching.

<h2 id="choose-a-database">Choose a database for your task</h2>

| Resource | Useful for | Region check |
| --- | --- | --- |
| [gaming.tools](https://aion2.gaming.tools/items) | Items, skills, quests, NPCs and linked records | Global catalogue; check the version label on the detail page |
| [MetaBot](https://metabot.gg/en/aion-2) | Equipment, skills, monster drops, quests and recipes | Global catalogue; read the acquisition section of the selected record |
| [AION2 Hub](https://aion2hub.com/database) | Item filters by type, class and grade, plus regional item comparisons | Select Global or Korea/Taiwan explicitly; some Global records use test-client data |

An English page can still describe KR/TW. Keep region and patch in view, especially when an item has two entries with the same translated name. A database entry can also exist before its dungeon or reward opens on your server.

<h2 id="find-an-item">Find an item and its acquisition route</h2>

1. Copy the full item name from the client. If you get no match, try a distinctive part of the name and narrow by item type.
2. Select your region, then filter for your class, faction, equipment slot and required level where those controls are available.
3. Open the detail record. Separate **character level**, **item level**, fixed stats and random rolls.
4. Read the acquisition section. Follow the linked monster, quest, chest or recipe to see the actual route.
5. Check whether you receive the item directly or choose it from a reward chest before planning a farming run.

For a concrete example, open [Ludra's Blade of Extinction](https://aion2hub.com/database/items/110120003). Its page separates basic stats, random sub-stats, upgrade previews and acquisition, and includes a KR/TW comparison. Use that layout to compare the same item across regions; avoid treating a comparison value as your own character's stat.

<GuideVisual id="workflow" />

<h2 id="skills-drops-and-quests">Look up skills, drops and quests</h2>

For a skill, start from [gaming.tools Skills](https://aion2.gaming.tools/skills), select the class and skill type, and open the exact ability. Compare its level, cost, cooldown and available specialization rather than copying a build with points you have not unlocked. Use the [build guide](/builds) to turn individual records into a playable setup.

For drops, start from the desired item and work backwards to its acquisition route. A listed probability is not a guaranteed reward. Check difficulty, reward eligibility and any chest selection before using a drop table to choose a run.

For quest steps, open [gaming.tools Quests](https://aion2.gaming.tools/quests), then match your faction and map. Read the previous quest, starting NPC, objective and turn-in separately. If you need a resource's location rather than its stats, use the [map guide](/map) and its gathering filters.

<h2 id="character-database">Find a character or player profile</h2>

Use <a href="/tools/character">character lookup</a> for a named player. Enter the region, exact server and character name. An item catalogue cannot tell you which random rolls that player actually has equipped.

[Shugo.GG](https://shugo.gg/) also offers region-based character search. Check its API status before retrying a missing result: a service outage or a delayed profile update can prevent a valid character from appearing. Its item database has separate regional coverage, so a Global character-search option does not make every item record a Global record.

<h2 id="steamdb-product-record">What SteamDB tells you</h2>

The [AION 2 SteamDB record](https://steamdb.info/app/3393110/) is for **Steam app 3393110**. Use it for the Steam application's history and product information. Use an in-game database for equipment, skills and drops, or the [Steam guide](/steam) for access and platform details.

<h2 id="check-a-record">Check a record before spending resources</h2>

Keep the exact item or skill page bookmarked. Before spending Kina or upgrade materials, compare the name, region, current tooltip and required content with your client. Older test entries, future content and KR/TW records can remain searchable even when their route is unavailable to your Global character.

**Which AION 2 database should a Global beginner use?** Start with gaming.tools or MetaBot for the type of record you need. Use AION2 Hub when you want item filters or a regional comparison.

**Does a database show my character's actual gear?** Use a character profile for equipped gear and rolls. An item record describes the item and its possible values.

**Is an item in the database guaranteed to be obtainable now?** Check its region, content requirements and current in-game reward list first.

<GuideNext slug="builds" />''','builds')

def write_pages():
    for slug, locales in PAGES.items():
        assert set(locales) == {'en','ja','es','de'}, f'{slug}: four locales'
        for locale, (meta, body) in locales.items():
            directory = ROOT / 'src' / 'content' / locale
            with (directory / (slug + '.json')).open('x', encoding='utf-8') as handle:
                json.dump(meta, handle, ensure_ascii=False, indent=2)
                handle.write('\n')
            with (directory / (slug + '.mdx')).open('x', encoding='utf-8') as handle:
                handle.write(body)
        data = {'slug':slug, 'keyword':'aion 2 ' + slug.replace('-',' '), 'checkedAt':'2026-10-04', 'revision':'2026-10-04.keyword-refresh-1', 'regions':['Global'] + (['KR/TW'] if slug in ['database','global-changes'] else []), 'related':RELATED[slug], 'sources':SOURCES[slug]}
        with (ROOT / 'src' / 'content' / 'article-data' / (slug + '.json')).open('x', encoding='utf-8') as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write('\n')
        print(slug, 'created', len(locales), 'localized article pairs')

article('global-changes', 'en', 'AION 2 Global Changes: Launch Differences from KR/TW',
    'Compare AION 2 Global launch progression and classes with KR/TW Chapter 1. Check level caps, Brawler availability, dungeon requirements and Founder changes.',
    'Global starts with level-45 progression and eight classes. Use the correct regional content and upgrade rules before following a KR/TW route.',
    'Global launch has a character-level cap of 45 and eight classes. KR/TW Chapter 1 raised the cap to 50 and added Brawler and later dungeons. Match your guide to Global before investing in a build. Founder cosmetic sharing announced October 3 is awaiting implementation.',
    [('global-vs-kr-tw','Global launch versus KR/TW Chapter 1'),('level-cap-and-content','Level cap and dungeon progression'),('class-roster','Eight Global classes and Brawler'),('regional-builds-and-gear','Use the right skill and gear version'),('global-account-and-packs','Global account, servers and Founder changes'),('before-switching-guides','A checklist before using a regional guide')],
    ('Bring a regional guide onto your Global character','Check availability and requirements before spending points, currency or materials.',[
        ('Identify the edition','Use Global launch, KR or TW and the guide’s actual content stage.'),
        ('Match level and class','Global starts at a cap of 45 with eight classes; Brawler is a later regional addition.'),
        ('Read the client requirements','Check the dungeon entry panel, unlocked skill slots and current item tooltip.'),
        ('Plan the next usable step','Choose content you can enter and a setup you can operate now.')]),
    '''**AION 2 Global changes** affect which progression route and class guide you can use. Global launch starts with **level 45 and eight classes**. KR/TW Chapter 1 is a later content stage with level 50, Brawler and additional dungeons. Begin with the differences that change your next action.

<h2 id="global-vs-kr-tw">Global launch versus KR/TW Chapter 1</h2>

| Feature | Global launch | KR/TW Chapter 1 | What to do on Global |
| --- | --- | --- | --- |
| Character-level cap | 45 | Raised to 50 | Prepare a level-45 endgame route |
| Class roster | Eight classes | Brawler added to the earlier eight | Choose from the Global character-creation roster |
| Progression areas | Early faction progression through Verteron and Altgard | Eltnen and Morheim added | Follow your available main-story objectives |
| Later dungeon progression | Use the Global entry requirements | Citadel of the Fallen Daeva and Abyssal Horn Den require level 50 in Chapter 1 | Do not build a launch farming route around a level-50 entry |

The comparison is between **Global launch and the KR/TW Chapter 1 content stage**, not two identical patches. Later regional additions are useful future context, but their launch timing, entry values and rewards are separate from your Global character's current progression.

<h2 id="level-cap-and-content">Level cap and dungeon progression</h2>

Reach **character level 45** on Global, then use the [leveling guide](/leveling) to move into available endgame activities. Character level, item level and Combat Power are different measurements. A gear requirement is not another character-level cap.

Open the dungeon's entry panel before organizing a group. Check difficulty, character-level requirement, item-level requirement and reward conditions individually. A KR/TW level-50 route does not replace the level-45 objectives in your Global journal.

If a guide moves directly into Eltnen, Morheim or the Chapter 1 level-50 dungeons, stop at the content transition and choose an activity your character can enter. Keep the later route for the relevant content update rather than spending materials for an inaccessible step.

<h2 id="class-roster">Eight Global classes and Brawler</h2>

Global launches with **Gladiator, Templar, Assassin, Ranger, Sorcerer, Spiritmaster, Cleric and Chanter**. See the [class comparison](/classes) for roles and party responsibilities.

**Brawler** was introduced with KR/TW Chapter 1. It uses gauntlets and a Rage-based frontline kit. It is outside the Global launch roster, and a Global arrival date is not announced. A nine-class ranking or Brawler build therefore belongs to a different content stage.

Choose an available class whose role you enjoy. Compare builds for that same class and activity, then match their skills and point budget to what your character has unlocked.

<GuideVisual id="workflow" />

<h2 id="regional-builds-and-gear">Use the right skill and gear version</h2>

Keep region, class, level and activity beside a saved build. Recheck skill levels, Stigma slots, selected specializations and Daevanion boards in your own client. More points or a later unlock can change a rotation even when the class name is identical.

For equipment, match the item name, faction, required level and actual tooltip before copying an upgrade target. Choose Global in a database that offers regional filters. A preview in a data catalogue does not mean the reward is available on your server, and an upgrade calculation is not a guaranteed cost.

Use the [build guide](/builds) for a current, operable setup. Adapt one part at a time so that an unavailable skill or item does not invalidate the rest of your character.

<h2 id="global-account-and-packs">Global account, servers and Founder changes</h2>

Global runs its own regions and faction-specific server lists. Agree on **region, faction and exact server** with friends; use the [server guide](/server) before creating a character. A KR/TW character profile or server choice does not place that character in a Global world.

Use Global access and purchase conditions when planning the launch. The free-to-play opening is **October 5, 2026 at 13:00 UTC**; Founder Advanced Access opened September 30. Check the [Steam guide](/steam) for the appropriate launcher and access window.

The **October 3 Founder cosmetic change** will make included cosmetics usable by all characters on the account across servers. Implementation is still in progress, with completion planned after Early Access. The 30-day membership, Supply Chest and Styling Chest remain one-time rewards. Use the [monetization guide](/monetization) before claiming or purchasing a pack.

<h2 id="before-switching-guides">A checklist before using a regional guide</h2>

1. Check Global, KR or TW and whether the guide describes launch or later chapter content.
2. Match your class, level and the activity you want to complete.
3. Read the current entry and reward conditions in your client.
4. Replace unavailable skills or gear targets with options you have now.
5. Check regional purchase and claim rules before spending currency.

**Is Global level 50 at launch?** No. Its launch character-level cap is 45; KR/TW Chapter 1 raised its regional cap to 50.

**Can I create Brawler on Global at launch?** The Global launch roster contains the eight classes above. Brawler is a KR/TW Chapter 1 addition.

**Can I use a KR/TW guide on Global?** Use shared fundamentals, then match availability, requirements, skills and rewards to your Global client before following specific steps.

<GuideNext slug="guide" />''','guide')

article('global-changes', 'ja', 'AION 2 Globalの変更点：KR/TWとの開始時の違い',
    'AION 2 Global開始時とKR/TW Chapter 1の成長やクラスを比較。レベル上限、Brawler、ダンジョン条件、Founder外観の変更を確認できます。',
    'Globalはレベル45と8クラスから開始します。KR/TWの攻略を使う前に、地域のコンテンツと強化条件を合わせましょう。',
    'Global開始時のキャラクターレベル上限は45で、8クラスが選べます。KR/TW Chapter 1では上限50、Brawlerと後続ダンジョンが追加されました。10月3日発表のFounder外観共有は実装中です。',
    [('global-vs-kr-tw','Global開始時とKR/TW Chapter 1の比較'),('level-cap-and-content','レベル上限とダンジョンの進行'),('class-roster','Globalの8クラスとBrawler'),('regional-builds-and-gear','スキルと装備の版を合わせる'),('global-account-and-packs','Globalのアカウント・サーバー・Founder変更'),('before-switching-guides','別地域の攻略を使う前の確認')],
    ('別地域の攻略を自分のGlobalキャラクターに合わせる','ポイント、通貨、素材を使う前に、利用できる内容と条件を確認します。',[
        ('サービスを確認する','Global開始時、KR、TWと、その攻略のコンテンツ段階を確認します。'),
        ('レベルとクラスを合わせる','Globalの開始時は上限45と8クラス。Brawlerは別地域の後続追加です。'),
        ('クライアントの条件を読む','ダンジョン条件、開放済みスキル枠、現在の装備表示を確認します。'),
        ('今できる次の行動を選ぶ','参加できるコンテンツと、現在操作できる構成で進めます。')]),
    '''**AION 2 Globalの変更点**は、使える成長ルートやクラス攻略に影響します。Global開始時は**レベル45と8クラス**です。KR/TW Chapter 1はレベル50、Brawler、追加ダンジョンがある後の段階なので、まず次の行動に関わる違いを確認しましょう。

<h2 id="global-vs-kr-tw">Global開始時とKR/TW Chapter 1の比較</h2>

| 項目 | Global開始時 | KR/TW Chapter 1 | Globalでの行動 |
| --- | --- | --- | --- |
| キャラクターレベル上限 | 45 | 50に引き上げ | レベル45のエンドゲームを準備 |
| クラス | 8クラス | 従来の8クラスにBrawler追加 | Globalの作成画面にあるクラスを選ぶ |
| 成長地域 | VerteronとAltgardでの序盤の陣営別進行 | EltnenとMorheim追加 | 現在進められるメインストーリーを追う |
| 後続ダンジョン | Globalの参加条件を使用 | Chapter 1のCitadel of the Fallen DaevaとAbyssal Horn Denはレベル50が必要 | 開始時の周回計画をレベル50の入口に合わせない |

比較対象は**Global開始時とKR/TW Chapter 1の段階**で、同一パッチではありません。後続の追加は今後の参考になりますが、実装時期、参加条件、報酬は現在のGlobalキャラクターの進行と分けて考えます。

<h2 id="level-cap-and-content">レベル上限とダンジョンの進行</h2>

Globalでは**キャラクターレベル45**に到達したら、[レベリングガイド](/leveling)から利用できるエンドゲームに進みます。キャラクターレベル、アイテムレベル、Combat Powerは別の数値です。装備条件を追加のキャラクターレベル上限と混同しないようにしましょう。

パーティーを集める前にダンジョンの参加画面を開き、難易度、必要キャラクターレベル、必要アイテムレベル、報酬条件を個別に読みます。KR/TWのレベル50ルートは、Globalのジャーナルにあるレベル45の目標の代わりにはなりません。

攻略がEltnen、Morheim、Chapter 1のレベル50ダンジョンへ進む場合は、そのコンテンツ移行地点で止め、現在参加できる活動を選びます。利用できない次の段階のために素材を使わず、後続ルートは対象の更新まで保存しておきましょう。

<h2 id="class-roster">Globalの8クラスとBrawler</h2>

Global開始時のクラスは**Gladiator、Templar、Assassin、Ranger、Sorcerer、Spiritmaster、Cleric、Chanter**です。役割とパーティーでの仕事は[クラス比較](/classes)を確認してください。

**Brawler**はKR/TW Chapter 1で追加され、ガントレットとRageを使う前衛クラスです。Global開始時のクラスには含まれず、Globalでの追加日は未発表です。9クラスの順位表やBrawlerの構成は別のコンテンツ段階に属します。

現在選べるクラスから好きな役割を選び、同じクラスと活動のビルドを比較します。そのスキルとポイント配分を、自分が開放した内容に合わせましょう。

<GuideVisual id="workflow" />

<h2 id="regional-builds-and-gear">スキルと装備の版を合わせる</h2>

保存した構成には、地域、クラス、レベル、活動を添えておきます。スキルレベル、Stigma枠、選んだ特化、Daevanion盤を自分のクライアントで再確認してください。同じクラスでも、ポイント数や後続の開放によって戦闘手順が変わります。

装備は名前、陣営、必要レベル、実際の表示を合わせてから強化目標をコピーします。地域フィルターがあるデータベースではGlobalを選びましょう。一覧にあることと、そのサーバーで報酬を受け取れることは別です。強化の計算結果も確定費用ではありません。

現在使える構成は[ビルドガイド](/builds)から確認し、一度に一部分ずつ調整します。使えないスキルや装備で構成全体が成立しなくなるのを避けましょう。

<h2 id="global-account-and-packs">Globalのアカウント・サーバー・Founder変更</h2>

Globalには独自の地域と陣営別サーバーがあります。友達と**地域、陣営、正確なサーバー名**を合わせ、作成前に[サーバーガイド](/server)を確認します。KR/TWのキャラクタープロフィールやサーバーを選んでも、そのキャラクターがGlobalのワールドに入るわけではありません。

参加や購入にはGlobalの条件を使います。無料プレイの開始は**2026年10月5日13:00 UTC**、FounderのAdvanced Accessは9月30日に開始しました。ランチャーと参加期間は[Steamガイド](/steam)で確認してください。

**10月3日のFounder外観変更**では、パックに含まれる外観がアカウント内の全キャラクター・全サーバーで使えるようになります。現在は実装中で、Early Access終了後の完了予定です。30日メンバーシップ、Supply Chest、Styling Chestは一度だけの報酬のままです。購入や受け取り前に[課金ガイド](/monetization)を確認しましょう。

<h2 id="before-switching-guides">別地域の攻略を使う前の確認</h2>

1. Global・KR・TWと、開始時か後続チャプターかを確認します。
2. クラス、レベル、クリアしたい活動を合わせます。
3. 現在の参加と報酬条件をクライアントで読みます。
4. 利用できないスキルや装備目標を、今ある選択肢に置き換えます。
5. 通貨を使う前に地域別の購入と受け取り条件を確認します。

**Global開始時の上限は50？** いいえ。キャラクターレベル上限は45です。KR/TW Chapter 1では地域の上限が50に引き上げられました。

**開始時にGlobalでBrawlerを作れる？** Globalの開始時は上記の8クラスです。BrawlerはKR/TW Chapter 1の追加です。

**KR/TW攻略をGlobalで使える？** 共通の基本を使い、具体的な手順の前に利用可能な内容、条件、スキル、報酬をGlobalのクライアントに合わせましょう。

<GuideNext slug="guide" />''','guide')

article('global-changes', 'es', 'Cambios de AION 2 Global: diferencias de lanzamiento con KR/TW',
    'Compara la progresión y clases de AION 2 Global con KR/TW Chapter 1. Revisa el nivel máximo, Brawler, requisitos de mazmorras y cambios de Founder.',
    'Global empieza con progresión hasta nivel 45 y ocho clases. Comprueba el contenido y las reglas de tu región antes de seguir una ruta de KR/TW.',
    'El lanzamiento de Global tiene un nivel máximo de personaje de 45 y ocho clases. KR/TW Chapter 1 subió el máximo a 50 y añadió Brawler y mazmorras posteriores. Adapta la guía a Global antes de invertir. Compartir cosméticos Founder sigue en implementación tras el anuncio del 3 de octubre.',
    [('global-vs-kr-tw','Global de lanzamiento frente a KR/TW Chapter 1'),('level-cap-and-content','Nivel máximo y progresión de mazmorras'),('class-roster','Ocho clases de Global y Brawler'),('regional-builds-and-gear','Usa la versión correcta de habilidades y equipo'),('global-account-and-packs','Cuenta, servidores y cambios de Founder en Global'),('before-switching-guides','Comprueba esto antes de seguir una guía regional')],
    ('Adapta una guía regional a tu personaje Global','Comprueba disponibilidad y requisitos antes de gastar puntos, moneda o materiales.',[
        ('Identifica la edición','Distingue Global de lanzamiento, KR o TW y la etapa real de contenido de la guía.'),
        ('Comprueba nivel y clase','Global empieza con máximo 45 y ocho clases; Brawler es una incorporación regional posterior.'),
        ('Lee los requisitos del cliente','Revisa acceso de mazmorra, ranuras de habilidades desbloqueadas y descripción actual del objeto.'),
        ('Elige el siguiente paso disponible','Usa contenido al que puedes entrar y una configuración que puedas manejar ahora.')]),
    '''Los **cambios de AION 2 Global** determinan qué ruta de progreso y guía de clase puedes seguir. Global empieza con **nivel 45 y ocho clases**. KR/TW Chapter 1 es una etapa posterior con nivel 50, Brawler y más mazmorras. Empieza por las diferencias que cambian tu siguiente acción.

<h2 id="global-vs-kr-tw">Global de lanzamiento frente a KR/TW Chapter 1</h2>

| Característica | Global de lanzamiento | KR/TW Chapter 1 | Qué hacer en Global |
| --- | --- | --- | --- |
| Nivel máximo de personaje | 45 | Aumentado a 50 | Prepara una ruta de endgame de nivel 45 |
| Clases | Ocho clases | Brawler añadido a las ocho anteriores | Elige del listado de creación de Global |
| Zonas de progreso | Progresión inicial de facción por Verteron y Altgard | Eltnen y Morheim añadidos | Sigue los objetivos disponibles de la historia |
| Mazmorras posteriores | Usa los requisitos de entrada de Global | Citadel of the Fallen Daeva y Abyssal Horn Den requieren nivel 50 en Chapter 1 | No bases el farmeo de lanzamiento en una entrada de nivel 50 |

La comparación es entre **Global de lanzamiento y la etapa KR/TW Chapter 1**, no entre dos parches idénticos. Las incorporaciones regionales posteriores sirven de contexto, pero fecha de llegada, requisitos y recompensas son distintos del progreso actual de tu personaje Global.

<h2 id="level-cap-and-content">Nivel máximo y progresión de mazmorras</h2>

Alcanza **nivel de personaje 45** en Global y usa la [guía de leveo](/leveling) para pasar al endgame disponible. Nivel de personaje, nivel de objeto y Combat Power son medidas distintas. Un requisito de equipo no representa otro límite de nivel de personaje.

Abre el panel de entrada antes de reunir un grupo. Comprueba dificultad, nivel de personaje, nivel de objeto y condiciones de recompensa por separado. Una ruta de nivel 50 de KR/TW no sustituye los objetivos de nivel 45 de tu diario Global.

Si una guía pasa directamente a Eltnen, Morheim o las mazmorras de nivel 50 de Chapter 1, detente en esa transición y elige una actividad a la que puedes entrar. Guarda la ruta posterior para su actualización en vez de gastar materiales en un paso inaccesible.

<h2 id="class-roster">Ocho clases de Global y Brawler</h2>

Global se estrena con **Gladiator, Templar, Assassin, Ranger, Sorcerer, Spiritmaster, Cleric y Chanter**. La [comparación de clases](/classes) explica funciones y responsabilidades de grupo.

**Brawler** llegó con KR/TW Chapter 1. Usa guanteletes y una mecánica de Rage de primera línea. No pertenece al listado de lanzamiento de Global y no tiene una fecha Global anunciada. Una clasificación de nueve clases o una build de Brawler describe otra etapa de contenido.

Elige una clase disponible cuya función te guste. Compara builds para esa misma clase y actividad, y ajusta habilidades y presupuesto de puntos a lo que has desbloqueado.

<GuideVisual id="workflow" />

<h2 id="regional-builds-and-gear">Usa la versión correcta de habilidades y equipo</h2>

Guarda región, clase, nivel y actividad junto a cada build. Revisa niveles de habilidad, ranuras de Stigma, especializaciones elegidas y tableros Daevanion en tu cliente. Más puntos o un desbloqueo posterior pueden cambiar la rotación aunque la clase tenga el mismo nombre.

Para equipo, compara nombre, facción, nivel requerido y descripción real antes de copiar una mejora objetivo. Selecciona Global en las bases con filtro regional. Una vista del catálogo no significa que la recompensa esté disponible en tu servidor, y un cálculo de mejora no garantiza el coste.

Usa la [guía de builds](/builds) para una configuración disponible y manejable. Adapta una parte cada vez para que una habilidad u objeto bloqueado no invalide todo el personaje.

<h2 id="global-account-and-packs">Cuenta, servidores y cambios de Founder en Global</h2>

Global tiene sus propias regiones y listas de servidores por facción. Acuerda **región, facción y servidor exacto** con tus amigos; consulta la [guía de servidores](/server) antes de crear el personaje. Un perfil o servidor KR/TW no traslada ese personaje a un mundo Global.

Planifica el acceso y las compras con las condiciones Global. La apertura gratuita es el **5 de octubre de 2026 a las 13:00 UTC**; el Advanced Access de Founder comenzó el 30 de septiembre. Comprueba lanzador y ventana de acceso en la [guía de Steam](/steam).

El **cambio de cosméticos Founder del 3 de octubre** permitirá usar los incluidos en todos los personajes de la cuenta y en todos los servidores. Sigue en implementación y está previsto completarlo después de Early Access. La membresía de 30 días y los cofres Supply y Styling siguen siendo recompensas de una sola entrega. Lee la [guía de monetización](/monetization) antes de comprar o recoger un pack.

<h2 id="before-switching-guides">Comprueba esto antes de seguir una guía regional</h2>

1. Identifica Global, KR o TW y si la guía describe el lanzamiento o un capítulo posterior.
2. Comprueba clase, nivel y actividad que quieres completar.
3. Lee las condiciones actuales de entrada y recompensa en tu cliente.
4. Sustituye habilidades y objetivos de equipo no disponibles por opciones que ya tienes.
5. Revisa compra y recogida regionales antes de gastar moneda.

**¿Global llega al nivel 50 de lanzamiento?** No. Su nivel máximo inicial de personaje es 45; KR/TW Chapter 1 aumentó el máximo regional a 50.

**¿Puedo crear Brawler en Global de lanzamiento?** El listado inicial de Global contiene las ocho clases indicadas. Brawler se añadió en KR/TW Chapter 1.

**¿Puedo seguir una guía de KR/TW en Global?** Usa los fundamentos compartidos, pero adapta disponibilidad, requisitos, habilidades y recompensas a tu cliente Global antes de seguir pasos concretos.

<GuideNext slug="guide" />''','guide')

article('global-changes', 'de', 'AION 2 Global Changes: Launch-Unterschiede zu KR/TW',
    'Vergleiche AION 2 Global zum Launch mit KR/TW Chapter 1: Levelcap, Brawler, Dungeonvoraussetzungen und die Änderungen an Founder-Kosmetik.',
    'Global startet mit Level-45-Fortschritt und acht Klassen. Prüfe regionale Inhalte und Verbesserungsregeln, bevor du einer KR/TW-Route folgst.',
    'Global startet mit Charakterlevelcap 45 und acht Klassen. KR/TW Chapter 1 erhöhte das Cap auf 50 und ergänzte Brawler sowie spätere Dungeons. Gleiche einen Build mit Global ab, bevor du investierst. Die am 3. Oktober angekündigte Founder-Kosmetikfreigabe wird noch umgesetzt.',
    [('global-vs-kr-tw','Global zum Launch gegenüber KR/TW Chapter 1'),('level-cap-and-content','Levelcap und Dungeonfortschritt'),('class-roster','Acht Global-Klassen und Brawler'),('regional-builds-and-gear','Die passende Skill- und Ausrüstungsversion nutzen'),('global-account-and-packs','Global-Account, Server und Founder-Änderungen'),('before-switching-guides','Checkliste vor einem regionalen Guide')],
    ('Einen regionalen Guide an deinen Global-Charakter anpassen','Prüfe Verfügbarkeit und Voraussetzungen vor dem Einsatz von Punkten, Währung oder Materialien.',[
        ('Edition bestimmen','Unterscheide Global zum Launch, KR oder TW und die tatsächliche Inhaltsstufe des Guides.'),
        ('Level und Klasse abgleichen','Global beginnt mit Cap 45 und acht Klassen; Brawler ist eine spätere regionale Ergänzung.'),
        ('Clientvoraussetzungen lesen','Prüfe Dungeoneintritt, freigeschaltete Skillslots und den aktuellen Itemtooltip.'),
        ('Nutzbaren nächsten Schritt planen','Wähle zugängliche Inhalte und einen Build, den du jetzt bedienen kannst.')]),
    '''**AION 2 Global Changes** entscheiden darüber, welche Fortschrittsroute und welchen Klassenguide du nutzen kannst. Global beginnt mit **Level 45 und acht Klassen**. KR/TW Chapter 1 ist eine spätere Inhaltsstufe mit Level 50, Brawler und zusätzlichen Dungeons. Prüfe zuerst die Unterschiede, die deinen nächsten Schritt verändern.

<h2 id="global-vs-kr-tw">Global zum Launch gegenüber KR/TW Chapter 1</h2>

| Merkmal | Global zum Launch | KR/TW Chapter 1 | Dein Schritt auf Global |
| --- | --- | --- | --- |
| Charakterlevelcap | 45 | Auf 50 erhöht | Level-45-Endgame planen |
| Klassen | Acht Klassen | Brawler zu den bisherigen acht ergänzt | Klasse aus der Global-Charaktererstellung wählen |
| Fortschrittsgebiete | Früher Fraktionsfortschritt durch Verteron und Altgard | Eltnen und Morheim ergänzt | Verfügbaren Hauptstoryzielen folgen |
| Spätere Dungeons | Global-Eintrittsvoraussetzungen nutzen | Citadel of the Fallen Daeva und Abyssal Horn Den benötigen in Chapter 1 Level 50 | Launch-Farmroute nicht auf einen Level-50-Eintritt ausrichten |

Verglichen werden **Global zum Launch und die KR/TW-Inhaltsstufe Chapter 1**, nicht zwei identische Patches. Spätere regionale Ergänzungen geben Zukunftskontext; Zeitpunkt, Eintrittswerte und Belohnungen unterscheiden sich aber vom aktuellen Fortschritt deines Global-Charakters.

<h2 id="level-cap-and-content">Levelcap und Dungeonfortschritt</h2>

Erreiche auf Global **Charakterlevel 45** und gehe mit dem [Leveling-Guide](/leveling) zu verfügbaren Endgame-Aktivitäten über. Charakterlevel, Itemlevel und Combat Power sind unterschiedliche Größen. Eine Ausrüstungsvoraussetzung ist kein weiteres Charakterlevelcap.

Öffne vor der Gruppensuche das Eintrittsfenster des Dungeons. Prüfe Schwierigkeit, Charakterlevel, Itemlevel und Belohnungsbedingungen getrennt. Eine KR/TW-Level-50-Route ersetzt nicht die Level-45-Ziele in deinem Global-Journal.

Geht ein Guide direkt nach Eltnen, Morheim oder in die Level-50-Dungeons von Chapter 1, halte an diesem Inhaltsübergang an und wähle eine zugängliche Aktivität. Speichere die spätere Route für das passende Inhaltsupdate, statt Materialien für einen unzugänglichen Schritt auszugeben.

<h2 id="class-roster">Acht Global-Klassen und Brawler</h2>

Global startet mit **Gladiator, Templar, Assassin, Ranger, Sorcerer, Spiritmaster, Cleric und Chanter**. Der [Klassenvergleich](/classes) erklärt Rollen und Aufgaben in der Gruppe.

**Brawler** kam mit KR/TW Chapter 1. Die Klasse kämpft vorne mit Handschuhwaffen und einem Rage-System. Sie gehört nicht zum Global-Launch-Roster; ein Global-Termin ist nicht angekündigt. Ein Ranking mit neun Klassen oder ein Brawler-Build beschreibt daher eine andere Inhaltsstufe.

Wähle eine verfügbare Klasse mit einer Aufgabe, die dir gefällt. Vergleiche Builds für dieselbe Klasse und Aktivität und gleiche Skills sowie Punktebudget mit deinen Freischaltungen ab.

<GuideVisual id="workflow" />

<h2 id="regional-builds-and-gear">Die passende Skill- und Ausrüstungsversion nutzen</h2>

Notiere Region, Klasse, Level und Aktivität neben einem gespeicherten Build. Kontrolliere Skilllevel, Stigmaslots, ausgewählte Spezialisierungen und Daevanion-Boards im eigenen Client. Mehr Punkte oder spätere Freischaltungen können die Rotation trotz identischem Klassennamen verändern.

Gleiche bei Ausrüstung Name, Fraktion, benötigtes Level und tatsächlichen Tooltip ab, bevor du ein Verbesserungsziel übernimmst. Wähle Global in Datenbanken mit Regionalfiltern. Eine Katalogvorschau bedeutet nicht, dass die Belohnung auf deinem Server erhältlich ist; eine Verbesserungskalkulation garantiert keine Kosten.

Nutze den [Build-Guide](/builds) für eine verfügbare, bedienbare Zusammenstellung. Passe einzelne Teile nacheinander an, damit ein gesperrter Skill oder ein fehlendes Item nicht deinen ganzen Charakteraufbau entwertet.

<h2 id="global-account-and-packs">Global-Account, Server und Founder-Änderungen</h2>

Global hat eigene Regionen und fraktionsbezogene Serverlisten. Vereinbare **Region, Fraktion und genauen Server** mit Freunden und lies vor der Erstellung den [Server-Guide](/server). Ein KR/TW-Profil oder eine dortige Serverwahl versetzt den Charakter nicht in eine Global-Welt.

Plane Zugang und Käufe nach den Global-Bedingungen. Der kostenlose Start ist am **5. Oktober 2026 um 13:00 UTC**; Founder Advanced Access begann am 30. September. Den richtigen Launcher und das Zugangsfenster erklärt der [Steam-Guide](/steam).

Die **Founder-Kosmetikänderung vom 3. Oktober** wird enthaltene Kosmetik für alle Charaktere des Accounts auf allen Servern nutzbar machen. Sie wird noch umgesetzt und soll nach Early Access abgeschlossen sein. Die 30-Tage-Mitgliedschaft sowie Supply und Styling Chests bleiben einmalige Belohnungen. Lies den [Monetarisierungs-Guide](/monetization) vor Kauf oder Abholung eines Pakets.

<h2 id="before-switching-guides">Checkliste vor einem regionalen Guide</h2>

1. Prüfe Global, KR oder TW und ob der Guide Launch- oder spätere Kapitelinhalte behandelt.
2. Gleiche Klasse, Level und gewünschte Aktivität ab.
3. Lies aktuelle Eintritts- und Belohnungsbedingungen im Client.
4. Ersetze fehlende Skills und Ausrüstungsziele durch jetzt verfügbare Optionen.
5. Prüfe regionale Kauf- und Abholregeln vor einer Währungsausgabe.

**Ist Global zum Launch bei Level 50?** Nein. Das Charakterlevelcap zum Launch ist 45; KR/TW Chapter 1 erhöhte das regionale Cap auf 50.

**Kann ich Brawler zum Global-Launch erstellen?** Das Launch-Roster enthält die acht genannten Klassen. Brawler ist eine Ergänzung aus KR/TW Chapter 1.

**Kann ich einen KR/TW-Guide auf Global nutzen?** Übernimm gemeinsame Grundlagen und gleiche Verfügbarkeit, Voraussetzungen, Skills und Belohnungen vor konkreten Schritten mit deinem Global-Client ab.

<GuideNext slug="guide" />''','guide')

article('wings', 'en', 'AION 2 Wings: Unlock Flight, Compare Stats and Get Wings',
    'Unlock AION 2 wings through the early story, learn PC flight controls, distinguish equipped and owned effects, and check Blazing Sun cosmetic restrictions.',
    'Learn how to unlock flight, find a wing’s acquisition route, compare equipped and collection effects, and choose appearance separately from combat bonuses.',
    'Continue the opening story through your first Daeva Ascension, then open Wings with Alt+C. Equipped effects come from the pair you wear; owned effects stay active from your collection. Use V for flight and check your current key bindings. Blazing Sun is a Founder cosmetic.',
    [('unlock-wings','Unlock wings through the opening story'),('equipped-and-owned-effects','Equipped effects, owned effects and appearance'),('find-wing-sources','Find out how to get a wing'),('flight-controls','Fly, glide and control your height'),('choose-pve-wings','Choose wings for your PvE role'),('blazing-sun-wings','Blazing Sun Wings and Founder restrictions')],
    ('Choose the effect before the appearance','Treat combat equipment, collection bonuses and the visible wing design as separate choices.',[
        ('Unlock flight','Complete the opening Ascension story and follow its flight tutorial.'),
        ('Read both effect panels','Compare the equipped bonus with the owned bonus.'),
        ('Check the acquisition route','Use the selected wing’s source information before visiting a shop, quest or crafting station.'),
        ('Test the controls','Check takeoff, height adjustment and landing somewhere safe before a long crossing.')]),
    '''**AION 2 wings** serve three purposes: flight, combat or collection bonuses, and appearance. Unlocking flight does not require buying a cosmetic pair. Start with the early story, then use the Wings screen to plan each additional unlock.

<h2 id="unlock-wings">Unlock wings through the opening story</h2>

Follow the opening main story through your first Daeva Ascension. Both factions receive **Lesser Daeva Wings** during this early quest chain. The chain is recommended around level 5; completing the story step matters more than reaching the number alone.

| Faction | Starting area | Starter-wing quest | Next flight-related quest |
| --- | --- | --- | --- |
| Elyos | Poeta | The Power in the Lake, from Daminu | Fledgling Wings |
| Asmodians | Ishalgen | The Being Beneath the Lake, from Elvida | Spread Your Wings |

Complete the Ascension objectives and collect the reward, then continue the flight tutorial. If the flight action is still unavailable, return to the active story objective instead of buying wings to bypass it. Use the [leveling guide](/leveling) when you need the next progression milestone.

<h2 id="equipped-and-owned-effects">Equipped effects, owned effects and appearance</h2>

Open **Wings** from the main menu, or use the default **Alt+C** shortcut. Select a pair and read its effect panels separately.

| Effect | When it applies | What to compare |
| --- | --- | --- |
| Equipped effect | While that pair is equipped | The combat bonuses relevant to your current role |
| Owned effect | While the wing is registered in your collection, even with another pair equipped | Its collection bonuses and any level-dependent changes |
| Appearance | When you choose that visual design | The look you want; a cosmetic skin does not add combat stats by itself |

Changing the equipped pair does not remove the owned effects of other registered wings. Keep useful collection unlocks even when you prefer a different design. Check the selected wing's actual panels rather than assuming every rarity has the same bonuses or enhancement track.

<GuideVisual id="workflow" />

<h2 id="find-wing-sources">Find out how to get a wing</h2>

Select the locked wing you want in the Wings menu and open its source information. Follow the listed quest, shop or crafting route. Read both the reward and its requirements: a wing item, a cosmetic skin and a chest containing a choice are different purchases or rewards.

For a practical collection route, finish the starter story wings first, then check wing rewards in content you already play. Plan a dedicated farm only after you know the exact reward, faction requirement and whether the content is open on Global. For travel to a named area, use the [map guide](/map).

Elyos and Asmodians both have starter wings with the same starter equipped bonus. Later entries can have faction-specific versions or appearances. Match your faction before using another character's acquisition route.

<h2 id="flight-controls">Fly, glide and control your height</h2>

These are the default PC bindings. Custom bindings take precedence; use **Key Settings** if your layout differs.

| Action | Default binding |
| --- | --- |
| Toggle flight | V |
| Sprint or accelerate | Shift |
| Jump and glide | Space |
| Ascend while flying | Ctrl+R |
| Descend while flying | Ctrl+F |
| Open Wings | Alt+C |

Flight and gliding are separate movement actions. Use flight to adjust height and glide to cross from an elevated position. Watch the flight meter and aim for a reachable landing before it runs out. Practice takeoff and descent on safe ground before crossing a deep gap or flying into combat.

Flight availability depends on the area. Some dungeon sections also allow wing travel, so check the action indicator instead of assuming every instance blocks flight. Use the [PvP guide](/pvp) before treating a flight route through hostile territory as ordinary travel.

<h2 id="choose-pve-wings">Choose wings for your PvE role</h2>

Compare the **equipped effect** for the task you are doing now: damage for a damage role, survivability when incoming damage is the problem, or recovery when your role needs it. Compare the complete effect panel rather than choosing by rarity or appearance alone.

Evaluate collection progress separately. An owned bonus remains useful when you equip another pair, so the wing you want to unlock next may differ from the one you want to wear. Before enhancing, read the current materials, cost and result in the selected wing's enhancement panel. Spend according to your [build](/builds) and available resources.

**What are the best wings for PvE?** Choose from wings you can obtain on your region and compare their equipped effects for your role. Your next collection unlock is a separate decision.

**Is there a wings map for every reward?** Start from the selected wing's source information. Quest, shop and crafting rewards require different routes; a map is useful once you know the destination.

<h2 id="blazing-sun-wings">Blazing Sun Wings and Founder restrictions</h2>

**Blazing Sun Wings** are the cosmetic wings included in the Ultimate Founder's Pack. They change appearance rather than providing an additional combat advantage. You can unlock ordinary flight through the story without that pack.

The account-wide Founder cosmetic change announced on **October 3** is still being implemented, with completion planned after Early Access. Blazing Sun is included in that change. Follow the in-game claim instructions when the rollout is available; do not assume every character can already claim it. The 30-day membership and the Supply and Styling Chests remain one-time rewards. See the [monetization guide](/monetization) for pack and claim conditions.

<GuideNext slug="builds" />''','builds')

article('wings', 'ja', 'AION 2の翼：飛行の解放、効果と入手方法',
    'AION 2の翼を序盤の物語で解放し、PCの飛行操作、装着効果と所有効果、Blazing Sunの外観と受け取り条件を確認しましょう。',
    '飛行の解放、翼の入手先、装着効果とコレクション効果の違いを整理。戦闘ボーナスと好みの外観を別々に選べます。',
    '序盤の最初のディーヴァ覚醒を進め、Alt+Cで翼を開きます。装着効果は現在の翼、所有効果はコレクションから適用されます。飛行はVが初期設定です。Blazing SunはFounder特典の外観です。',
    [('unlock-wings','序盤の物語で翼を解放する'),('equipped-and-owned-effects','装着効果・所有効果・外観の違い'),('find-wing-sources','欲しい翼の入手先を調べる'),('flight-controls','飛行・滑空・高度調整'),('choose-pve-wings','PvEの役割に合う翼を選ぶ'),('blazing-sun-wings','Blazing SunとFounder特典の条件')],
    ('効果と外観を別々に選ぶ','装着する翼、コレクションのボーナス、見た目をそれぞれ確認しましょう。',[
        ('飛行を解放する','序盤の覚醒ストーリーをクリアし、飛行チュートリアルを進めます。'),
        ('両方の効果を読む','装着時のボーナスと所有ボーナスを比較します。'),
        ('入手先を確認する','ショップ、クエスト、製作へ向かう前に、選んだ翼の入手情報を調べます。'),
        ('安全な場所で操作する','長い移動の前に、離陸、高度調整、着地を確かめます。')]),
    '''**AION 2の翼**には、飛行、戦闘やコレクションのボーナス、外観という用途があります。飛行を解放するために外観用の翼を買う必要はありません。序盤の物語を進めてから、翼画面で次の入手目標を決めましょう。

<h2 id="unlock-wings">序盤の物語で翼を解放する</h2>

最初のディーヴァ覚醒までメインストーリーを進めます。両陣営とも、この序盤のクエストで**Lesser Daeva Wings**を受け取ります。推奨レベルはおよそ5ですが、数字を満たすだけでなく、該当する物語をクリアする必要があります。

| 陣営 | 開始地域 | 最初の翼を受け取るクエスト | 続く飛行関連クエスト |
| --- | --- | --- | --- |
| Elyos | Poeta | Daminuから受けるThe Power in the Lake | Fledgling Wings |
| Asmodians | Ishalgen | Elvidaから受けるThe Being Beneath the Lake | Spread Your Wings |

覚醒の目標を達成して報酬を受け取り、飛行チュートリアルを進めます。飛行できない場合は、購入で解決しようとせず、進行中の物語の目標を確認してください。次の成長段階は[レベリングガイド](/leveling)で確認できます。

<h2 id="equipped-and-owned-effects">装着効果・所有効果・外観の違い</h2>

メインメニューの**翼**、または初期設定の**Alt+C**から画面を開きます。翼を選び、効果欄を分けて読みましょう。

| 種類 | 適用される条件 | 比較する内容 |
| --- | --- | --- |
| 装着効果 | その翼を装着している間 | 現在の役割に合う戦闘ボーナス |
| 所有効果 | コレクションに登録済みなら別の翼を装着中でも適用 | コレクションのボーナスとレベルによる変化 |
| 外観 | その見た目を選んだとき | 好みのデザイン。外観用スキン自体に戦闘能力値は追加されません |

装着する翼を変えても、ほかの登録済みの翼の所有効果は失われません。好みの見た目が別でも、役立つコレクションを集める意味があります。等級だけで効果や強化段階を決めつけず、選んだ翼の表示を確認してください。

<GuideVisual id="workflow" />

<h2 id="find-wing-sources">欲しい翼の入手先を調べる</h2>

翼メニューで未入手の翼を選び、入手先の情報を開きます。表示されたクエスト、ショップ、製作の手順をたどりましょう。翼を解放するアイテム、外観スキン、選択式の報酬箱は別なので、報酬と条件を両方確認します。

まず序盤の翼を受け取り、普段遊ぶコンテンツの翼報酬を調べると進めやすくなります。専用の周回を始める前に、正確な報酬、陣営条件、Globalでの開放状況を確認してください。目的地への移動には[マップガイド](/map)を使えます。

ElyosとAsmodiansの最初の翼は、装着時のボーナスが同じです。その後の翼には陣営別の種類や外観があるため、ほかのキャラクターの入手手順を使う前に自分の陣営を合わせましょう。

<h2 id="flight-controls">飛行・滑空・高度調整</h2>

以下はPCの初期キーです。変更済みの設定が優先されるので、違う場合は**Key Settings**を確認してください。

| 操作 | 初期キー |
| --- | --- |
| 飛行の切り替え | V |
| ダッシュ・加速 | Shift |
| ジャンプ・滑空 | Space |
| 飛行中の上昇 | Ctrl+R |
| 飛行中の下降 | Ctrl+F |
| 翼画面を開く | Alt+C |

飛行と滑空は別の移動操作です。高度を変えたいときは飛行、高所から渡るときは滑空を使います。飛行ゲージを見ながら、切れる前に届く着地点を決めましょう。深い谷や戦闘区域を渡る前に、安全な場所で離陸と下降を練習してください。

飛行できるかは場所によって変わります。一部のダンジョンでも翼による移動ができるため、すべてのインスタンスで禁止だと決めつけず、操作表示を確認します。敵対地域への移動には[PvPガイド](/pvp)も確認しましょう。

<h2 id="choose-pve-wings">PvEの役割に合う翼を選ぶ</h2>

現在の役割に合わせて**装着効果**を比較します。ダメージ役なら攻撃、被ダメージが問題なら耐久、回復が必要な役割なら回復関連の効果を見ます。等級や見た目だけで選ばず、効果欄全体を読みましょう。

コレクションの進行は別に考えます。ほかの翼を装着しても所有ボーナスは有効なので、次に集める翼と今装着する翼が違っても構いません。強化前には、その翼の強化画面で素材、費用、結果を読み、[ビルド](/builds)と手持ちの資源に合わせて使います。

**PvEで最もよい翼は？** 自分の地域で入手できる翼から、役割に合う装着効果を比較します。次のコレクション目標は別に選びましょう。

**すべての翼を探せるマップはある？** まず欲しい翼の入手情報を確認します。クエスト、ショップ、製作では手順が違い、目的地が分かってからマップが役立ちます。

<h2 id="blazing-sun-wings">Blazing SunとFounder特典の条件</h2>

**Blazing Sun Wings**はUltimate Founder's Packの外観用の翼です。見た目が変わり、追加の戦闘上の有利さは得られません。そのパックを買わなくても、通常の飛行は物語で解放できます。

**10月3日**に発表されたFounder外観のアカウント全体への共有は実装中で、Early Access終了後の完了予定です。Blazing Sunも対象ですが、すべてのキャラクターで今すぐ受け取れるとは限りません。利用開始後にゲーム内の受け取り手順を確認してください。30日メンバーシップ、Supply Chest、Styling Chestは引き続き一度だけの報酬です。パックと受け取り条件は[課金ガイド](/monetization)で確認できます。

<GuideNext slug="builds" />''','builds')

article('wings', 'es', 'Alas de AION 2: vuelo, atributos y cómo conseguirlas',
    'Desbloquea las alas de AION 2 con la historia inicial, aprende los controles de vuelo en PC y distingue efectos equipados, de colección y las alas Blazing Sun.',
    'Aprende a desbloquear el vuelo, encontrar la fuente de cada par y comparar efectos equipados y de colección por separado de la apariencia.',
    'Avanza por la historia inicial hasta tu primera Ascensión a Daeva y abre Alas con Alt+C. Los efectos equipados pertenecen al par que llevas; los efectos de posesión siguen activos en la colección. V activa el vuelo con los controles predeterminados. Blazing Sun es un cosmético Founder.',
    [('unlock-wings','Desbloquea las alas con la historia inicial'),('equipped-and-owned-effects','Efectos equipados, de posesión y apariencia'),('find-wing-sources','Busca cómo conseguir un par de alas'),('flight-controls','Vuela, planea y cambia de altura'),('choose-pve-wings','Elige alas para tu función en PvE'),('blazing-sun-wings','Blazing Sun y condiciones de Founder')],
    ('Elige el efecto antes de la apariencia','Separa el equipo de combate, los bonos de colección y el diseño visible.',[
        ('Desbloquea el vuelo','Completa la Ascensión inicial y sigue el tutorial de vuelo.'),
        ('Lee ambos paneles','Compara el efecto equipado con el efecto de posesión.'),
        ('Comprueba la obtención','Lee la fuente del par elegido antes de visitar tienda, misión o estación de fabricación.'),
        ('Prueba los controles','Practica despegue, altura y aterrizaje en un lugar seguro antes de cruzar una gran distancia.')]),
    '''Las **alas de AION 2** sirven para volar, aportar bonificaciones de combate o colección y cambiar la apariencia. No necesitas comprar un par cosmético para desbloquear el vuelo. Empieza con la historia y planifica las siguientes incorporaciones desde la pantalla Alas.

<h2 id="unlock-wings">Desbloquea las alas con la historia inicial</h2>

Sigue la historia principal hasta tu primera Ascensión a Daeva. Ambas facciones reciben **Lesser Daeva Wings** durante esta cadena inicial. Su nivel recomendado ronda el 5; completar el paso de la historia importa más que alcanzar el número.

| Facción | Zona inicial | Misión de las primeras alas | Siguiente misión relacionada con el vuelo |
| --- | --- | --- | --- |
| Elyos | Poeta | The Power in the Lake, de Daminu | Fledgling Wings |
| Asmodians | Ishalgen | The Being Beneath the Lake, de Elvida | Spread Your Wings |

Completa los objetivos de Ascensión, recoge la recompensa y continúa el tutorial de vuelo. Si la acción sigue bloqueada, vuelve al objetivo activo de la historia en vez de comprar alas para saltártelo. La [guía de leveo](/leveling) te ayuda a encontrar el siguiente hito.

<h2 id="equipped-and-owned-effects">Efectos equipados, de posesión y apariencia</h2>

Abre **Alas** desde el menú principal o con el atajo predeterminado **Alt+C**. Selecciona un par y lee cada panel por separado.

| Efecto | Cuándo se aplica | Qué comparar |
| --- | --- | --- |
| Efecto equipado | Mientras llevas ese par | Bonificaciones de combate para tu función actual |
| Efecto de posesión | Cuando está registrado en tu colección, incluso con otro par equipado | Bonificaciones de colección y cambios según su nivel |
| Apariencia | Al elegir ese diseño | El aspecto que prefieres; un aspecto cosmético no añade estadísticas de combate por sí mismo |

Cambiar el par equipado no elimina los efectos de posesión de otras alas registradas. Conserva los desbloqueos útiles aunque prefieras otro diseño. Revisa los paneles del par seleccionado: no todas las calidades tienen los mismos bonos ni la misma progresión de mejora.

<GuideVisual id="workflow" />

<h2 id="find-wing-sources">Busca cómo conseguir un par de alas</h2>

Selecciona las alas bloqueadas que quieres y abre su información de obtención. Sigue la misión, tienda o fabricación indicada. Lee recompensa y condiciones: un objeto que desbloquea alas, un aspecto y un cofre con elección son recompensas o compras diferentes.

Para avanzar de forma práctica, recoge primero las alas iniciales y consulta los premios de las actividades que ya juegas. Antes de dedicarte a farmear un par, comprueba recompensa exacta, facción requerida y disponibilidad del contenido en Global. La [guía del mapa](/map) ayuda a llegar al destino.

Elyos y Asmodians tienen alas iniciales con el mismo bono equipado. Otros pares pueden tener variantes o apariencias por facción. Comprueba la tuya antes de seguir el recorrido de otro personaje.

<h2 id="flight-controls">Vuela, planea y cambia de altura</h2>

Estos son los controles predeterminados de PC. Si los has cambiado, tu configuración tiene prioridad; revisa **Key Settings**.

| Acción | Tecla predeterminada |
| --- | --- |
| Activar o desactivar vuelo | V |
| Esprintar o acelerar | Shift |
| Saltar y planear | Space |
| Ascender en vuelo | Ctrl+R |
| Descender en vuelo | Ctrl+F |
| Abrir Alas | Alt+C |

Volar y planear son acciones diferentes. Usa el vuelo para cambiar de altura y el planeo para cruzar desde un punto elevado. Vigila el medidor y busca un aterrizaje alcanzable antes de agotarlo. Practica despegue y descenso en suelo seguro antes de cruzar un barranco o entrar en combate aéreo.

La posibilidad de volar depende de la zona. Algunas secciones de mazmorra permiten desplazarte con alas, así que comprueba el indicador en vez de dar por hecho que todas las instancias lo bloquean. Lee la [guía de PvP](/pvp) antes de usar una ruta aérea por territorio hostil.

<h2 id="choose-pve-wings">Elige alas para tu función en PvE</h2>

Compara el **efecto equipado** según tu tarea: daño para una función ofensiva, supervivencia si el problema es el daño recibido o recuperación si tu función la necesita. Lee el panel completo en vez de elegir solo por calidad o apariencia.

Evalúa la colección por separado. El bono de posesión sirve aunque lleves otro par, por lo que las próximas alas que quieras conseguir pueden ser distintas de las que uses. Antes de mejorarlas, revisa materiales, coste y resultado en su panel actual. Gasta según tu [build](/builds) y los recursos disponibles.

**¿Cuáles son las mejores alas para PvE?** Compara los efectos equipados de los pares disponibles en tu región para tu función. El siguiente desbloqueo de colección es otra decisión.

**¿Hay un mapa de todas las recompensas de alas?** Empieza por la información de obtención del par elegido. Misiones, tiendas y fabricación exigen recorridos distintos; el mapa ayuda cuando ya conoces el destino.

<h2 id="blazing-sun-wings">Blazing Sun y condiciones de Founder</h2>

**Blazing Sun Wings** son las alas cosméticas del Ultimate Founder's Pack. Cambian el aspecto, sin añadir ventaja de combate. El vuelo normal se desbloquea mediante la historia sin comprar ese pack.

El cambio para compartir cosméticos Founder en toda la cuenta, anunciado el **3 de octubre**, sigue en implementación y está previsto que termine después de Early Access. Blazing Sun está incluido. Sigue las instrucciones de recogida cuando se active; no asumas que todos tus personajes ya pueden recibirlo. La membresía de 30 días y los cofres Supply y Styling siguen siendo recompensas de una sola entrega. Consulta la [guía de monetización](/monetization) para las condiciones del pack.

<GuideNext slug="builds" />''','builds')

article('wings', 'de', 'AION 2 Wings: Flug freischalten, Werte und Bezugswege',
    'Schalte AION 2 Wings über die frühe Story frei. Lerne die PC-Flugsteuerung, angelegte und Besitz-Effekte sowie die Bedingungen der Blazing Sun Wings kennen.',
    'Erfahre, wie du den Flug freischaltest, Bezugswege für Wings findest und angelegte sowie Sammlungs-Effekte getrennt vom Aussehen vergleichst.',
    'Spiele die Anfangsstory bis zum ersten Daeva-Aufstieg und öffne Wings mit Alt+C. Angelegte Effekte stammen vom getragenen Paar; Besitz-Effekte bleiben durch die Sammlung aktiv. V ist die Standardtaste für Flug. Blazing Sun ist Founder-Kosmetik.',
    [('unlock-wings','Wings über die Anfangsstory freischalten'),('equipped-and-owned-effects','Angelegte Effekte, Besitz-Effekte und Aussehen'),('find-wing-sources','Den Bezugsweg einer Wing finden'),('flight-controls','Fliegen, gleiten und die Höhe ändern'),('choose-pve-wings','Wings für deine PvE-Aufgabe wählen'),('blazing-sun-wings','Blazing Sun und Founder-Bedingungen')],
    ('Erst die Wirkung, dann das Aussehen wählen','Trenne Kampfausrüstung, Sammlungsboni und das sichtbare Wing-Design.',[
        ('Flug freischalten','Beende die erste Aufstiegsstory und folge dem Flugtutorial.'),
        ('Beide Effektfelder lesen','Vergleiche den angelegten Effekt mit dem Besitz-Effekt.'),
        ('Bezugsweg prüfen','Lies die Herkunft, bevor du Shop, Quest oder Handwerksstation aufsuchst.'),
        ('Steuerung testen','Übe Start, Höhenwechsel und Landung sicher, bevor du eine lange Strecke überfliegst.')]),
    '''**AION 2 Wings** erfüllen drei Aufgaben: Flug, Kampf- oder Sammlungsboni und Aussehen. Zum Freischalten des Flugs brauchst du kein kosmetisches Paar zu kaufen. Beginne mit der frühen Story und plane weitere Freischaltungen im Wings-Fenster.

<h2 id="unlock-wings">Wings über die Anfangsstory freischalten</h2>

Folge der Hauptstory bis zu deinem ersten Daeva-Aufstieg. Beide Fraktionen erhalten in dieser frühen Questreihe **Lesser Daeva Wings**. Das empfohlene Level liegt ungefähr bei 5; entscheidend ist der abgeschlossene Storyschritt, nicht nur die Levelzahl.

| Fraktion | Startgebiet | Quest für die ersten Wings | Folgende flugbezogene Quest |
| --- | --- | --- | --- |
| Elyos | Poeta | The Power in the Lake von Daminu | Fledgling Wings |
| Asmodians | Ishalgen | The Being Beneath the Lake von Elvida | Spread Your Wings |

Erledige die Aufstiegsziele, hole die Belohnung und folge dem Flugtutorial. Ist die Flugaktion noch gesperrt, prüfe das aktive Storyziel, statt Wings als Abkürzung zu kaufen. Der [Leveling-Guide](/leveling) hilft beim nächsten Fortschrittsziel.

<h2 id="equipped-and-owned-effects">Angelegte Effekte, Besitz-Effekte und Aussehen</h2>

Öffne **Wings** im Hauptmenü oder mit dem Standardkürzel **Alt+C**. Wähle ein Paar und lies die Effektfelder getrennt.

| Effekt | Wann er gilt | Was du vergleichst |
| --- | --- | --- |
| Angelegter Effekt | Während du dieses Paar trägst | Kampfboni für deine derzeitige Aufgabe |
| Besitz-Effekt | Nach Registrierung in der Sammlung, auch mit einem anderen Paar | Sammlungsboni und Änderungen durch das Level |
| Aussehen | Wenn du das Design auswählst | Dein bevorzugter Look; ein kosmetischer Skin gibt selbst keine zusätzlichen Kampfwerte |

Ein Wechsel des getragenen Paars entfernt nicht die Besitz-Effekte anderer registrierter Wings. Sammle nützliche Freischaltungen auch dann, wenn dir ein anderes Design besser gefällt. Prüfe die konkreten Effektfelder, statt gleiche Boni oder Verbesserungsstufen für jede Qualität anzunehmen.

<GuideVisual id="workflow" />

<h2 id="find-wing-sources">Den Bezugsweg einer Wing finden</h2>

Wähle im Wings-Menü das gesperrte Paar und öffne seine Herkunftsinformation. Folge der angegebenen Quest, dem Shop oder dem Herstellungsweg. Lies Belohnung und Voraussetzungen: Ein Wing-Freischaltitem, ein Skin und eine Auswahltruhe sind verschiedene Käufe oder Belohnungen.

Hole zuerst die Story-Wings und prüfe danach Wing-Belohnungen in Inhalten, die du ohnehin spielst. Plane gezieltes Farmen erst, wenn genaue Belohnung, Fraktionsvoraussetzung und Verfügbarkeit auf Global feststehen. Der [Karten-Guide](/map) hilft bei der Reise zum benannten Gebiet.

Elyos und Asmodians erhalten Starter-Wings mit demselben angelegten Startbonus. Spätere Einträge können fraktionsgebundene Varianten oder Designs haben. Gleiche deine Fraktion ab, bevor du dem Bezugsweg eines anderen Charakters folgst.

<h2 id="flight-controls">Fliegen, gleiten und die Höhe ändern</h2>

Dies sind die Standardbelegungen am PC. Eigene Belegungen haben Vorrang; kontrolliere bei Abweichungen **Key Settings**.

| Aktion | Standardtaste |
| --- | --- |
| Flug umschalten | V |
| Sprinten oder beschleunigen | Shift |
| Springen und gleiten | Space |
| Im Flug steigen | Ctrl+R |
| Im Flug sinken | Ctrl+F |
| Wings öffnen | Alt+C |

Fliegen und Gleiten sind getrennte Bewegungsaktionen. Nutze Flug für Höhenwechsel und Gleiten zum Überqueren von einer erhöhten Position. Behalte die Fluganzeige im Blick und wähle einen erreichbaren Landeplatz, bevor sie leer ist. Übe Start und Sinkflug sicher, bevor du tiefe Schluchten überquerst oder in einen Kampf fliegst.

Ob du fliegen kannst, hängt vom Gebiet ab. Auch manche Dungeonabschnitte erlauben Wing-Reisen. Prüfe deshalb die Aktionsanzeige, statt für jede Instanz ein Flugverbot anzunehmen. Lies den [PvP-Guide](/pvp), bevor du eine Flugroute durch feindliches Gebiet als gewöhnliche Reise behandelst.

<h2 id="choose-pve-wings">Wings für deine PvE-Aufgabe wählen</h2>

Vergleiche den **angelegten Effekt** mit deiner aktuellen Aufgabe: Schaden für eine Schadensrolle, Überleben bei zu hohem eingehendem Schaden oder Erholung, wenn deine Aufgabe das erfordert. Lies das ganze Effektfeld, statt allein nach Qualität oder Aussehen zu wählen.

Betrachte die Sammlung getrennt. Ein Besitzbonus bleibt mit einem anderen Paar aktiv. Das nächste Paar zum Freischalten muss daher nicht das nächste Paar zum Tragen sein. Prüfe vor einer Verbesserung die aktuellen Materialien, Kosten und das Ergebnis im jeweiligen Verbesserungsfenster. Richte den Einsatz nach deinem [Build](/builds) und deinen verfügbaren Ressourcen aus.

**Welche Wings sind die besten für PvE?** Vergleiche die angelegten Effekte der auf deiner Region erhältlichen Paare für deine Aufgabe. Die nächste Sammlungsfreischaltung wählst du getrennt davon.

**Gibt es eine Karte für alle Wing-Belohnungen?** Beginne mit der Herkunft des gewünschten Paars. Quests, Shops und Herstellung brauchen unterschiedliche Wege; eine Karte hilft, sobald das Ziel bekannt ist.

<h2 id="blazing-sun-wings">Blazing Sun und Founder-Bedingungen</h2>

**Blazing Sun Wings** sind die kosmetischen Wings des Ultimate Founder's Pack. Sie ändern das Aussehen und geben keinen zusätzlichen Kampfvorteil. Normalen Flug schaltest du auch ohne dieses Paket über die Story frei.

Die am **3. Oktober** angekündigte Freigabe der Founder-Kosmetik für den gesamten Account wird noch umgesetzt und soll nach Early Access fertig sein. Blazing Sun gehört dazu. Folge nach dem Rollout den Abholhinweisen im Spiel; gehe nicht davon aus, dass bereits jeder Charakter die Wings abholen kann. Die 30-Tage-Mitgliedschaft sowie Supply und Styling Chests bleiben einmalige Belohnungen. Der [Monetarisierungs-Guide](/monetization) erklärt Paket- und Abholbedingungen.

<GuideNext slug="builds" />''','builds')

article('database', 'ja', 'AION 2 データベース：装備・スキル・キャラクター検索',
    'AION 2の装備、スキル、クエスト、ドロップ情報を探す方法を紹介。地域を合わせ、キャラクター検索とSteamDBの用途も確認できます。',
    '装備の入手先、スキルの詳細、クエストの手順、キャラクターの装備、Steamの製品情報から、調べたい内容に合う検索先を選びましょう。',
    'Globalの装備・スキル・クエストはgaming.toolsやMetaBotで検索できます。AION2 HubにはGlobalとKR/TWの装備フィルターがあります。プレイヤーはキャラクター検索、Steam製品情報はSteamDBを使います。',
    [('choose-a-database','目的に合うデータベースを選ぶ'),('find-an-item','装備と入手先を探す'),('skills-drops-and-quests','スキル・ドロップ・クエストを調べる'),('character-database','キャラクターやプレイヤーを検索する'),('steamdb-product-record','SteamDBで分かること'),('check-a-record','素材を使う前に確認する')],
    ('名前から入手方法まで調べる','地域と対象の項目を合わせてから、次の周回や強化を計画しましょう。',[
        ('地域を選ぶ','Global・KR・TWを確認。表示言語だけではゲームの版を判別できません。'),
        ('対象の詳細を開く','名前、陣営、種類、必要レベルを合わせます。'),
        ('入手先のリンクをたどる','能力値だけで止まらず、クエスト、敵、宝箱、製作レシピまで確認します。'),
        ('ゲーム内で確かめる','通貨を使う前に、コンテンツや報酬、レシピが利用できることを確認します。')]),
    '''**AION 2のデータベース**では、装備の効果と入手先、スキルを上げたときの変化、次に進むクエストなどを調べられます。**キャラクターデータベース**は、特定のプレイヤーのプロフィールを見るためのものです。まず調べたい内容を決めましょう。

<h2 id="choose-a-database">目的に合うデータベースを選ぶ</h2>

| サービス | 得意な内容 | 地域の確認 |
| --- | --- | --- |
| [gaming.tools](https://aion2.gaming.tools/items) | 装備、スキル、クエスト、NPCと関連項目 | Globalの一覧。詳細ページのバージョン表示も確認 |
| [MetaBot](https://metabot.gg/en/aion-2) | 装備、スキル、モンスターのドロップ、クエスト、レシピ | Globalの一覧。選んだ項目の入手先を確認 |
| [AION2 Hub](https://aion2hub.com/database) | 種類・クラス・等級の装備フィルターと地域別比較 | GlobalかKorea/Taiwanを選択。一部のGlobal項目はテストクライアントの内容 |

英語のページでもKR/TWの情報が含まれます。同じ訳名の装備が複数ある場合は、地域とパッチを確認してください。データベースに項目があっても、そのダンジョンや報酬が自分のサーバーで開放済みとは限りません。

<h2 id="find-an-item">装備と入手先を探す</h2>

1. クライアントから正式な名前をコピーします。見つからない場合は名前の特徴的な部分で検索し、種類を絞ります。
2. 地域を選び、利用できるフィルターでクラス、陣営、装備部位、必要レベルを合わせます。
3. 詳細を開き、**キャラクターレベル**、**アイテムレベル**、固定能力値、ランダム効果を分けて確認します。
4. 入手先から敵、クエスト、宝箱、レシピのリンクを開きます。
5. 直接ドロップするのか、報酬箱から選ぶのかを確認してから周回先を決めます。

例として[Ludra's Blade of Extinction](https://aion2hub.com/database/items/110120003)を開くと、基本能力値、ランダム効果、強化のプレビュー、入手先、KR/TWとの比較が分かれています。地域比較の値を、自分のキャラクターの能力値として扱わないようにしましょう。

<GuideVisual id="workflow" />

<h2 id="skills-drops-and-quests">スキル・ドロップ・クエストを調べる</h2>

スキルは[gaming.tools Skills](https://aion2.gaming.tools/skills)からクラスと種類を選び、目的のスキルを開きます。レベル、消費、再使用時間、利用可能な特化を比較してください。まだ開放していないポイントを前提にした構成をそのままコピーせず、[ビルドガイド](/builds)で現在のキャラクターに合わせます。

ドロップは欲しい装備から入手先へ逆にたどります。表示された確率は確定報酬ではありません。難易度、報酬を受け取る条件、宝箱の選択肢を確認しましょう。

クエストは[gaming.tools Quests](https://aion2.gaming.tools/quests)で陣営とマップを合わせ、前提クエスト、開始NPC、目標、報告先を別々に確認します。素材の能力値ではなく位置が必要なら、[マップガイド](/map)の採集フィルターを使います。

<h2 id="character-database">キャラクターやプレイヤーを検索する</h2>

特定のプレイヤーを探す場合は<a href="/tools/character">キャラクター検索</a>に地域、正確なサーバー名、キャラクター名を入力します。装備一覧では、そのプレイヤーが実際に装着しているランダム効果までは分かりません。

[Shugo.GG](https://shugo.gg/)にも地域別のキャラクター検索があります。見つからないときはAPIの状態を確認してください。障害やプロフィールの反映待ちで検索できない場合があります。装備データの対応地域は別なので、Globalのキャラクターを検索できても、すべての装備項目がGlobal版になるわけではありません。

<h2 id="steamdb-product-record">SteamDBで分かること</h2>

[AION 2のSteamDBページ](https://steamdb.info/app/3393110/)は**Steamアプリ3393110**の記録です。Steamアプリの履歴と製品情報に使います。装備、スキル、ドロップはゲーム内情報のデータベース、参加条件と対応環境は[Steamガイド](/steam)を確認してください。

<h2 id="check-a-record">素材を使う前に確認する</h2>

調べた装備やスキルの詳細をブックマークしておきましょう。Kinaや強化素材を使う前に、名前、地域、現在のツールチップ、必要なコンテンツをクライアントで照合します。古いテスト項目、将来のコンテンツ、KR/TW項目も検索結果に残ることがあります。

**Global初心者はどのデータベースを使えばよい？** 必要な項目に合わせてgaming.toolsかMetaBotから始め、装備の絞り込みや地域比較にはAION2 Hubを使います。

**実際に装着している装備も分かる？** 装着中の装備とランダム効果はキャラクタープロフィールで確認します。装備の詳細ページは、そのアイテムと取り得る値を説明するものです。

**一覧にある装備は今すぐ入手できる？** 地域、コンテンツの条件、現在のゲーム内報酬一覧を先に確認してください。

<GuideNext slug="builds" />''','builds')

article('database', 'es', 'Base de datos de AION 2: objetos, habilidades y personajes',
    'Encuentra bases de datos de objetos, habilidades, misiones y botín de AION 2. Elige la región correcta y distingue perfiles de personajes de SteamDB.',
    'Elige la consulta según lo que necesitas: equipo, detalles de una habilidad, pasos de una misión, un perfil de personaje o registros del producto de Steam.',
    'Usa gaming.tools o MetaBot para objetos, habilidades y misiones de Global. AION2 Hub añade filtros de Global y KR/TW. Busca jugadores en la consulta de personajes; SteamDB contiene datos del producto de Steam, no del botín.',
    [('choose-a-database','Elige una base de datos para tu objetivo'),('find-an-item','Busca un objeto y su forma de obtención'),('skills-drops-and-quests','Consulta habilidades, botín y misiones'),('character-database','Busca el perfil de un personaje'),('steamdb-product-record','Qué puedes consultar en SteamDB'),('check-a-record','Comprueba la ficha antes de gastar recursos')],
    ('Del nombre a una respuesta útil','Comprueba la región y la ficha exacta antes de planear la siguiente partida.',[
        ('Elige la región','Empieza por Global, KR o TW; el idioma no identifica la versión del juego.'),
        ('Abre la ficha exacta','Comprueba nombre, facción, tipo de objeto y nivel requerido.'),
        ('Sigue los enlaces de obtención','Revisa la misión, enemigo, cofre o receta, además de las estadísticas.'),
        ('Compruébalo en el juego','Confirma que el contenido y la recompensa o receta están disponibles antes de gastar.')]),
    '''Una **base de datos de AION 2** responde preguntas concretas: qué hace un objeto, dónde se consigue, cómo cambia una habilidad al subir de nivel o qué misión sigue. Una **base de datos de personajes** muestra el perfil de un jugador. Elige el tipo de consulta antes de buscar.

<h2 id="choose-a-database">Elige una base de datos para tu objetivo</h2>

| Recurso | Para qué sirve | Comprobación de región |
| --- | --- | --- |
| [gaming.tools](https://aion2.gaming.tools/items) | Objetos, habilidades, misiones, NPC y fichas relacionadas | Catálogo de Global; comprueba la versión de la ficha |
| [MetaBot](https://metabot.gg/en/aion-2) | Equipo, habilidades, botín de monstruos, misiones y recetas | Catálogo de Global; consulta la obtención del objeto elegido |
| [AION2 Hub](https://aion2hub.com/database) | Filtros por tipo, clase y calidad, y comparación regional de objetos | Elige Global o Korea/Taiwan; algunas fichas Global usan datos del cliente de prueba |

Una página en inglés puede describir KR/TW. Comprueba la región y el parche, sobre todo si dos objetos comparten el mismo nombre traducido. Una ficha también puede existir antes de que su mazmorra o recompensa esté disponible en tu servidor.

<h2 id="find-an-item">Busca un objeto y su forma de obtención</h2>

1. Copia el nombre completo del cliente. Si no aparece, busca una parte distintiva y filtra por tipo.
2. Elige la región y filtra por clase, facción, ranura de equipo y nivel requerido cuando esas opciones estén disponibles.
3. Abre la ficha. Distingue **nivel de personaje**, **nivel de objeto**, estadísticas fijas y atributos aleatorios.
4. Lee la sección de obtención. Sigue el enlace del monstruo, misión, cofre o receta para conocer la ruta real.
5. Comprueba si recibes el objeto directamente o lo eliges de un cofre antes de planear una sesión de farmeo.

Por ejemplo, abre [Ludra's Blade of Extinction](https://aion2hub.com/database/items/110120003). Su ficha separa estadísticas básicas, atributos aleatorios, vistas de mejora y obtención, además de la comparación con KR/TW. Esa estructura ayuda a comparar regiones sin confundir sus valores con los de tu personaje.

<GuideVisual id="workflow" />

<h2 id="skills-drops-and-quests">Consulta habilidades, botín y misiones</h2>

Para una habilidad, abre [gaming.tools Skills](https://aion2.gaming.tools/skills), selecciona clase y tipo, y entra en la habilidad exacta. Compara nivel, coste, tiempo de reutilización y especialización disponible. No copies una configuración que exige puntos aún bloqueados; usa la [guía de builds](/builds) para adaptar las fichas a tu personaje.

Para el botín, empieza por el objeto deseado y retrocede hasta su fuente. Una probabilidad indicada no garantiza la recompensa. Comprueba dificultad, requisitos para recibir el botín y opciones de selección del cofre antes de decidir qué repetir.

Para una misión, abre [gaming.tools Quests](https://aion2.gaming.tools/quests) y elige tu facción y mapa. Revisa por separado la misión anterior, el NPC inicial, el objetivo y la entrega. Si necesitas la posición de un recurso, usa la [guía del mapa](/map) y sus filtros de recolección.

<h2 id="character-database">Busca el perfil de un personaje</h2>

Usa la <a href="/tools/character">consulta de personajes</a> para buscar a un jugador concreto. Introduce región, servidor exacto y nombre. Un catálogo de objetos no muestra los atributos aleatorios que ese jugador lleva equipados.

[Shugo.GG](https://shugo.gg/) también permite buscar personajes por región. Si falta un resultado, comprueba el estado de la API antes de repetir: una caída del servicio o una actualización pendiente puede ocultar un personaje válido. La cobertura de su base de objetos es independiente; poder buscar personajes Global no convierte todas sus fichas en datos de Global.

<h2 id="steamdb-product-record">Qué puedes consultar en SteamDB</h2>

La [ficha de AION 2 en SteamDB](https://steamdb.info/app/3393110/) corresponde a la **aplicación 3393110 de Steam**. Sirve para su historial e información de producto. Consulta equipo, habilidades y botín en una base de datos del juego; para acceso y plataformas, usa la [guía de Steam](/steam).

<h2 id="check-a-record">Comprueba la ficha antes de gastar recursos</h2>

Guarda la ficha exacta del objeto o habilidad. Antes de gastar Kina o materiales de mejora, compara nombre, región, descripción actual y contenido requerido con tu cliente. Los registros de pruebas antiguas, contenido futuro y KR/TW pueden seguir apareciendo aunque su ruta no esté disponible para tu personaje Global.

**¿Qué base de datos conviene a un principiante de Global?** Empieza por gaming.tools o MetaBot según la ficha que necesitas. Usa AION2 Hub para filtrar objetos o comparar regiones.

**¿Una base de datos muestra mi equipo real?** El equipo y atributos equipados se ven en el perfil del personaje. Una ficha de objeto describe sus valores posibles.

**¿Todo objeto del catálogo puede conseguirse ahora?** Comprueba primero la región, los requisitos y la lista actual de recompensas del juego.

<GuideNext slug="builds" />''','builds')

article('database', 'de', 'AION 2 Datenbank: Items, Skills und Charaktersuche',
    'Finde AION 2 Datenbanken für Items, Skills, Quests und Drops. Wähle die passende Region und unterscheide Charakterprofile von SteamDB-Produktdaten.',
    'Wähle die Suche nach deiner Frage: Ausrüstung, Skilldetails, Questschritte, ein Charakterprofil oder Produktdaten zur Steam-Anwendung.',
    'Nutze gaming.tools oder MetaBot für Global-Items, Skills und Quests. AION2 Hub bietet Global- und KR/TW-Itemfilter. Spieler findest du über die Charaktersuche; SteamDB beschreibt das Steam-Produkt statt der Beute im Spiel.',
    [('choose-a-database','Wähle eine Datenbank für deine Frage'),('find-an-item','Finde ein Item und seinen Bezugsweg'),('skills-drops-and-quests','Schlage Skills, Drops und Quests nach'),('character-database','Finde ein Charakterprofil'),('steamdb-product-record','Was du in SteamDB findest'),('check-a-record','Prüfe den Eintrag vor dem Materialeinsatz')],
    ('Vom Namen zum nächsten Schritt','Gleiche Region und Eintrag ab, bevor du einen Run oder eine Verbesserung planst.',[
        ('Region wählen','Beginne mit Global, KR oder TW. Die Sprache allein verrät die Spielversion nicht.'),
        ('Genauen Eintrag öffnen','Prüfe Name, Fraktion, Itemtyp und benötigtes Level.'),
        ('Bezugsweg verfolgen','Öffne Quest, Gegner, Truhe oder Rezept statt nur die Werte anzusehen.'),
        ('Im Spiel abgleichen','Prüfe vor einer Ausgabe, ob Inhalt, Belohnung oder Rezept bereits verfügbar sind.')]),
    '''Eine **AION 2 Datenbank** beantwortet konkrete Fragen: Was bewirkt ein Item, woher stammt es, was ändert das nächste Skilllevel oder welche Quest folgt? Eine **Charakterdatenbank** zeigt dagegen das Profil eines Spielers. Wähle zuerst die passende Art der Suche.

<h2 id="choose-a-database">Wähle eine Datenbank für deine Frage</h2>

| Angebot | Nützlich für | Region prüfen |
| --- | --- | --- |
| [gaming.tools](https://aion2.gaming.tools/items) | Items, Skills, Quests, NPCs und verknüpfte Einträge | Global-Katalog; Versionsangabe auf der Detailseite beachten |
| [MetaBot](https://metabot.gg/en/aion-2) | Ausrüstung, Skills, Monsterdrops, Quests und Rezepte | Global-Katalog; Bezugsweg des gewählten Eintrags lesen |
| [AION2 Hub](https://aion2hub.com/database) | Itemfilter nach Typ, Klasse und Qualität sowie regionale Vergleiche | Global oder Korea/Taiwan auswählen; manche Global-Einträge verwenden Testclient-Daten |

Auch eine englische Seite kann KR/TW beschreiben. Prüfe Region und Patch besonders bei mehreren Items mit demselben übersetzten Namen. Ein Eintrag kann bereits existieren, obwohl der zugehörige Dungeon oder seine Belohnung auf deinem Server noch nicht verfügbar ist.

<h2 id="find-an-item">Finde ein Item und seinen Bezugsweg</h2>

1. Kopiere den vollständigen Namen aus dem Client. Fehlt ein Treffer, suche einen markanten Namensteil und grenze den Itemtyp ein.
2. Wähle die Region und nutze verfügbare Filter für Klasse, Fraktion, Ausrüstungsslot und benötigtes Level.
3. Öffne den Eintrag. Trenne **Charakterlevel**, **Itemlevel**, feste Werte und zufällige Eigenschaften.
4. Lies den Bezugsweg. Folge dem verlinkten Monster, der Quest, Truhe oder dem Rezept.
5. Prüfe vor dem Farmen, ob das Item direkt vergeben wird oder aus einer Belohnungstruhe gewählt werden muss.

Als Beispiel dient [Ludra's Blade of Extinction](https://aion2hub.com/database/items/110120003). Die Seite trennt Grundwerte, zufällige Nebenwerte, Verbesserungsvorschau und Bezugsweg und enthält einen KR/TW-Vergleich. Nutze diese Gliederung zum Regionalvergleich, ohne fremde Versionswerte als Werte deines Charakters zu behandeln.

<GuideVisual id="workflow" />

<h2 id="skills-drops-and-quests">Schlage Skills, Drops und Quests nach</h2>

Für Skills öffnest du [gaming.tools Skills](https://aion2.gaming.tools/skills), wählst Klasse und Skilltyp und dann die konkrete Fähigkeit. Vergleiche Level, Kosten, Abklingzeit und verfügbare Spezialisierung. Kopiere keine Verteilung mit noch gesperrten Punkten; der [Build-Guide](/builds) hilft dir, einzelne Einträge zu einer spielbaren Zusammenstellung zu verbinden.

Bei Drops beginnst du mit dem gewünschten Item und verfolgst seinen Bezugsweg rückwärts. Eine angegebene Wahrscheinlichkeit garantiert keine Belohnung. Prüfe Schwierigkeit, Belohnungsberechtigung und eine mögliche Truhenauswahl, bevor du einen Run wiederholst.

Für Questschritte öffnest du [gaming.tools Quests](https://aion2.gaming.tools/quests) und gleichst Fraktion und Karte ab. Lies Vorgängerquest, Start-NPC, Ziel und Abgabe getrennt. Suchst du den Standort einer Ressource statt ihrer Werte, nutze den [Karten-Guide](/map) mit den Sammelfiltern.

<h2 id="character-database">Finde ein Charakterprofil</h2>

Für einen bestimmten Spieler nutzt du die <a href="/tools/character">Charaktersuche</a>. Gib Region, genauen Server und Charakternamen ein. Ein Itemkatalog verrät nicht, welche zufälligen Eigenschaften dieser Spieler tatsächlich angelegt hat.

[Shugo.GG](https://shugo.gg/) bietet ebenfalls eine Charaktersuche nach Region. Prüfe bei fehlenden Treffern zunächst den API-Status: Ein Ausfall oder eine verzögerte Profilaktualisierung kann einen gültigen Charakter verbergen. Die regionale Abdeckung der Itemdaten ist davon getrennt. Eine Global-Charaktersuche macht nicht jeden Itemeintrag zu einem Global-Eintrag.

<h2 id="steamdb-product-record">Was du in SteamDB findest</h2>

Der [AION 2 Eintrag in SteamDB](https://steamdb.info/app/3393110/) gehört zur **Steam-App 3393110**. Er hilft bei der Historie und Produktinformationen der Steam-Anwendung. Ausrüstung, Skills und Drops schlägst du in einer Spieldatenbank nach; Zugang und Plattformen erklärt der [Steam-Guide](/steam).

<h2 id="check-a-record">Prüfe den Eintrag vor dem Materialeinsatz</h2>

Speichere den genauen Item- oder Skilleintrag als Lesezeichen. Vergleiche vor dem Einsatz von Kina oder Verbesserungsmaterialien Name, Region, aktuellen Tooltip und benötigten Inhalt mit deinem Client. Alte Testeinträge, spätere Inhalte und KR/TW-Daten bleiben mitunter auffindbar, obwohl dein Global-Charakter den Bezugsweg noch nicht nutzen kann.

**Welche AION 2 Datenbank eignet sich für Global-Einsteiger?** Beginne mit gaming.tools oder MetaBot für den benötigten Eintrag. AION2 Hub hilft bei Itemfiltern und Regionalvergleichen.

**Zeigt eine Datenbank meine tatsächliche Ausrüstung?** Angelegte Items und Eigenschaften findest du im Charakterprofil. Ein Itemeintrag beschreibt das Item und seine möglichen Werte.

**Ist jedes katalogisierte Item bereits erhältlich?** Prüfe zuerst Region, Inhaltsvoraussetzungen und die aktuelle Belohnungsliste im Spiel.

<GuideNext slug="builds" />''','builds')
