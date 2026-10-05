# Player content review — world guides

Review date: 2026-10-04 (Asia/Shanghai). Scope: spacetime-rift, character-creation, presets, map, gathering, guide, races, macro-guide, notmeter; English, Japanese, Spanish and German MDX and locale JSON.

This pass edits the evidence already recorded in the repository. It does not add an in-game test, run NotMeter, purchase an appearance change or validate a new recurring rift schedule. Original source records remain in `src/content/article-data/` and the pre-edit files remain in `before/src/content/`.

## Editorial decisions

- Lead with the player's task: choosing, entering, configuring, gathering, progressing or troubleshooting. Remove source comparisons, demonstrations, review dates and statements about what a screenshot does not prove.
- Retain useful outbound actions: Style Shop, maps, timers, download repositories, official notices, support and community destinations. Remove links used only to explain evidence provenance.
- Keep TOC IDs across all four languages. Keep each topic's component order synchronized. Remove the rift page's unrelated code / Drops / maintenance `GuideTimers` component.
- Simplify every image caption to its content or purpose. Describe the character-creation Style Shop image as a browsing and sharing interface.
- Keep the actual restrictions that change player decisions: region/faction/server coordination, entry versus stay time, hostile NPCs, paid appearance application, node access, same-faction transfers, desktop compatibility and account policy.

## Topic-specific source context and unknowns

### spacetime-rift

The Global server pairing notice supports opposing-server matchmaking. Historical KR/KR-TW timing reports disagree: RedCloud describes four-hour openings and a five-minute entry window; Madsin describes three-hour openings, ten-minute entry and a one-hour stay. Neither schedule becomes a Global schedule in the edited page. Their numbers and comparison commentary are removed from the player page. The Kisk arrangement comes from the latter regional demonstration and is omitted. Current client entry and remaining-stay indicators remain the practical instruction. Timer countdowns were not independently synchronized against a live Global opening.

### character-creation and presets

The official introduction supports the two factions, eight classes and over 200 customization options. The official transfer notice supports October 14, 2026 and same-faction transfers with an initial EA-to-EA restriction. October 3 Style Shop capture verifies public region, period and sort controls, not an in-game application. Existing-character download, refresh, application and upload steps come from KobraGX's Global tutorial. Initial-creation import, exact appearance-slot counts, application prices, name limits, character slots and deletion waits remain unverified in the underlying record. The page supplies the offered creation controls or manual settings rather than promising a website import. Steam's screenshot path is retained as a launcher-specific path, with PURPLE using its own folder.

### map

Keep faction zones as Verteron / Altgard and do not claim a new mandatory spawn or starting itinerary. October 3 Aion2T filtering captures support Hide All → Herbs → Aria. Historical map-filter tutorials support finding the Content layer; localized menu wording may vary. Aion2Maps' Global-coordinate and progress-sync descriptions come from its creator. Full coordinate coverage, live spawn presence, respawn intervals and every recovery scenario were not independently tested. The page retains height checks, possible locations, compact routes and progress preservation.

### gathering

Kevin Link's Global Advance Access account describes early-level gathering around character level 10–11; the edited page states early-level access without inventing a universal exact unlock level. KR's January 28, 2026 anti-bot level-45 unlock is kept with a short KR label. Global Asmodian promotion details come from the same first-hand report: Novice 50, Alzirr in Safe Haven, Splendent Ruby (Bound) from Ruby nodes in Calderon Canyon, distinct from Radiant Ruby Gemstone. This is preserved as region/faction-specific guidance, not a universal Elyos path. KR/TW Odyle recommendations, exact point distributions and uncertain subtitle item spellings are omitted. The ten-minute route is a suggested player comparison, with no promised yield or drop rate.

### guide and races

The Global launch announcement supports Steam / PURPLE and the announced October 5, 2026 free-to-play launch. The official Global dungeon showcase supports the launch level cap of 45. TW-specific rewards, item values and checkpoint guarantees are omitted rather than reclassified as Global facts. Exploration checks remain conditional on encountering the content. Official pairing and transfer notices support separate faction servers, periodically updated enemies, cross-server instances and same-faction transfers. No racial damage advantage, population winner, faction-change procedure or cross-region cooperation is invented. Bahamut's earlier direct-access 403 belongs in the log; the public page simply links the TW discussion board.

### macro-guide

Keybind location, hold-to-repeat and bottom-first stack priority derive from Karsten Scholz's September 30, 2026 Global menu walkthrough. This wiki has not reproduced those steps inside the game. aLuckyRO's lower-level live-server delay discussion does not establish a universal Global delay table and is omitted. The page keeps reachable reactive skills, one-stack troubleshooting and comparable manual/macro attempts without claiming a damage benchmark. NC's policy does not grant blanket permission for external input automation.

### notmeter

The maintainer website's October 3 snapshot provides KR, TW and Global searches, filtering, Windows/Npcap steps and DPS/nDPS descriptions. The distribution repository then labeled v1.0.246 (August 29, 2026) latest, with no Global-specific compatibility body. That dated release label is removed from player copy; current supported release selection remains actionable. No executable or packet capture has been tested here. Desktop service/patch compatibility remains a check before installation. Confirmed NC approval was not found in the source record and is retained as one short material account-policy limitation. General policy wording is not treated as a tool-specific prohibition or permission.

## Preserved source registry

The following source links, dates, regions and version notes are copied from the unchanged article-data records. Missing publication dates remain unspecified.

### spacetime-rift

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [Advanced Access Server Matchmaking](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939) | Global | 2026-09-29 | Current notice body captured 2026-10-02; temporary faction server pairing |
| [AION 2 RIFT Guide — DON'T MISS This Character Progression!](https://www.youtube.com/watch?v=gVtMCNJgMn4) | KR/TW | Unspecified | MR4KTV's pre-Global exploration and guard/death demonstration; exact regional build unverified |
| [Aion 2: Space Time Rift Timer - Never Miss a Rift Again!](https://www.youtube.com/watch?v=8rK7Wo37_X8) | KR | Unspecified | RedCloud's Korean Cleric demonstration reporting four-hour interval and five-minute entry; not a verified Global timetable |
| [[AION 2] Complete systems and contents overview (September 14th 2026)](https://www.youtube.com/watch?v=Tn7WKMXt5Wo) | Mixed | Unspecified | Madsin's overview reporting three-hour interval, ten-minute entry, one-hour stay, and Kisk behavior in its discussed version |
| [Aion 2 Spacetime Rift Timer - When Does Spacetime Rift Open \| Talentbuilds.com](https://talentbuilds.com/aion2/spacetimerift) | Mixed | Unspecified | Checked 2026-10-02; text extraction has loading schedules and pre-launch region wording; no Global countdown independently confirmed |
| [AION 2 Tracker — Global Release Update 🌍](https://www.reddit.com/r/Aion2/comments/1wv1wrx/aion_2_tracker_global_release_update/) | Global | Unspecified | Tool author reports Global Early Access experience and revised timers; not an official schedule |
| [AION 2 Tracker](https://aion2tracker.net/) | Mixed | Unspecified | Linked from author's Global update; individual countdowns not independently validated against client |

### character-creation

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [About the Game](https://aion2.plaync.com/en-us/about/index) | Global | Unspecified | Global eight-class, two-faction and customization introduction checked 2026-10-02 |
| [Information on Server Transfer](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2) | Global | 2026-09-30 | Global Advance Access server-transfer announcement |
| [AION 2: Character Customization Guide \| Create Your Perfect Character](https://www.youtube.com/watch?v=i82EC5vzq8I) | Mixed | Unspecified | Wiggles' pre-launch customization demonstration; exact Global panel labels not independently tested |
| [Style Shop](https://aion2.plaync.com/en-us/styleshop/popular) | Global | Unspecified | Public Global Style Shop region/period/sort UI checked in browser 2026-10-03; screenshot saved under presets; not initial-creation import evidence |
| [[Guide] Download & Upload Your Favorite Customizations](https://www.reddit.com/r/Aion2/comments/1wuf6ve/guide_download_upload_your_favorite_customizations/) | Global | Unspecified | Existing-character workflow; initial-creation import not confirmed |

### presets

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [Style Shop](https://aion2.plaync.com/en-us/styleshop/popular) | Global | Unspecified | Public Global Style Shop region/period/sort controls verified in browser 2026-10-03, signed out; screenshot and AX saved; no in-game import or purchase test |
| [[Guide] Download & Upload Your Favorite Customizations](https://www.reddit.com/r/Aion2/comments/1wuf6ve/guide_download_upload_your_favorite_customizations/) | Global | Unspecified | KobraGX launch-period player report, checked 2026-10-02 |
| [AION2 Operation Policies](https://aion2.plaync.com/en-us/board/rules/view?articleId=6aac4c8fab04307987fe2b4c) | Global | 2026-09-18 | Style Shop policy section; no independent confirmation of application price |
| [Free Preset Jinx](https://www.reddit.com/r/Aion2/comments/1wq4fef/free_preset_jinx/) | Global | Unspecified | Vitality27 manual slider screenshots dated 2026-09-25; screen coordinates are approximate |
| [AION 2: Character Customization Guide \| Create Your Perfect Character](https://www.youtube.com/watch?v=i82EC5vzq8I) | Mixed | Unspecified | Pre-launch editing walkthrough; not evidence for Style Shop importing |

### map

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [About the Game](https://aion2.plaync.com/en-us/about/index) | Global | Unspecified | Global English world introduction checked 2026-10-02 |
| [Aion 2 Interactive World Map — Zones, Monsters & Resources \| Aion2t.com](https://aion2t.com/map) | Mixed | Unspecified | Global-mode Verteron selector and Hide All → Herbs → Aria filter interaction verified in browser 2026-10-03; screenshot and AX saved; no live-node or respawn verification |
| [3D Interactive Voxel Maps for Aion 2 generated from the Global Client Data](https://www.reddit.com/r/Aion2/comments/1wtsfhn/3d_interactive_voxel_maps_for_aion_2_generated/) | Global | Unspecified | Midir21's Global preload-data tool introduction, checked 2026-10-02 |
| [Aion2Maps](https://www.aion2maps.com) | Global | Unspecified | Tool page retrieved 2026-10-02; full progress recovery not tested |
| [Aion2Hub Maps](https://aion2hub.com/maps) | Mixed | Unspecified | Community directory and player demonstration; current marker coverage not fully tested |
| [[Aion 2] Plan Your 💰💰 Routes Easy With This Interactive Map!](https://www.youtube.com/watch?v=k7Ud_YkU_SI) | KR/TW | Unspecified | Historical player walkthrough; no current Global marker-limit claim |
| [Aion 2 How To Make Feathers Appear ON THE BIG MAP](https://www.youtube.com/watch?v=rlYdxp4XTFM) | KR/TW | Unspecified | Historical player UI walkthrough; exact Global labels and reward totals not verified |

### gathering

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [AION 2 Introduced Strengthened Anti-Bot Measures](https://about.ncsoft.com/en/news/article/aion2_update_260128) | KR | 2026-01-28 | Korean anti-bot update; not a Global gathering unlock rule |
| [AION 2 GATHERING Guide — What to Gather & Why You NEED It for Endgame!](https://www.youtube.com/watch?v=g5wt6NOSjVU) | KR/TW | Unspecified | Mr4KTV pre-Global tutorial; Global promotion names and point allocation unverified |
| [[AION 2] Complete systems and contents overview (September 14th 2026)](https://www.youtube.com/watch?v=Tn7WKMXt5Wo) | KR/TW | Unspecified | Pre-Global gathering-system overview dated September 14 in its title; publication date unverified |
| [Aion 2 Interactive World Map — Zones, Monsters & Resources \| Aion2t.com](https://aion2t.com/map) | Mixed | Unspecified | Global-mode Verteron Herbs → Aria filter interaction checked in browser 2026-10-03; screenshot saved; no live-node availability or game unlock test |
| [3D Interactive Voxel Maps for Aion 2 generated from the Global Client Data](https://www.reddit.com/r/Aion2/comments/1wtsfhn/3d_interactive_voxel_maps_for_aion_2_generated/) | Global | Unspecified | Author-reported Global coordinate dataset; not a verified respawn schedule |
| [AION 2 Essence Extraction: How to Reach Professional](https://space4games.com/en/games-en/aion-2-essence-extraction-guide/) | Global | 2026-10-01 | Kevin Link's personal Global Advance Access gameplay; page updated October 2, 2026, checked October 3; reported early access and Asmodian promotion, not an independent wiki in-game test |

### guide

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [엔씨〈아이온2〉, 얼리 액세스 시작 ··· 스팀 글로벌 판매 1위 달성](https://about.ncsoft.com/news/article/A2_update_20261001) | Global | 2026-10-01 | Global launch announcement |
| [About the Game](https://aion2.plaync.com/en-us/about/index) | Global | Unspecified | Global eight-class introduction checked 2026-10-02 |
| [AION 2 Made Me Learn These 10 Things the Hard Way](https://www.youtube.com/watch?v=C73KG9MvqUk) | TW | Unspecified | Taiwan player retrospective; progression values not transplanted to Global |
| [[AION 2] Complete systems and contents overview (September 14th 2026)](https://www.youtube.com/watch?v=Tn7WKMXt5Wo) | KR/TW | Unspecified | Pre-Global systems overview dated September 14 in its title; publication date unverified; author explicitly notes unconfirmed Global settings |
| [[AION 2] Dungeon Live Gameplay Showcase](https://www.youtube.com/watch?v=S_TjiOh33a4) | Global | 2026-09-04 | Global pre-launch showcase; launch max level 45 confirmed in transcript |
| [AION 2 Beginner Guide: 11 Tips You Should Know Before You Start](https://space4games.com/en/games-en/aion-2-beginner-guide/) | Global | 2026-09-28 | Kevin Link's own Global Launch Scale Test observations mixed with explicitly labeled Korean experience; test UI labels not guaranteed unchanged at launch; snapshot checked 2026-10-03 |
| [AION 2 Official Discord Server](https://steamcommunity.com/app/3393110/discussions/6/802345327968609673/) | Global | 2026-04-20 | NC developer-pinned Discord invitation; checked 2026-10-03 |
| [AION2Official Twitch channel](https://www.twitch.tv/aion2official) | Global | Unspecified | Channel linked by archived Global broadcast announcement in research/discord/aion2_news.json; no stream timetable inferred |
| [r/Aion2](https://www.reddit.com/r/Aion2/) | Mixed | Unspecified | Community resource index checked 2026-10-03; individual posts not official game rules |
| [AION2 Bahamut board](https://forum.gamer.com.tw/B.php?bsn=82913) | TW | Unspecified | Board identity confirmed in indexed Bahamut post; direct board returned 403 on 2026-10-03; no current instructions extracted |

### races

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [About the Game : AION 2-NC](https://aion2.plaync.com/en-us/about/index) | Global | Unspecified | Official Global content API rechecked 2026-10-03: eight class identities and two factions; source archived in class-launch-sources/about-en-source.json |
| [Advanced Access Server Matchmaking](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939) | Global | 2026-09-29 | Public Global community API response refetched 2026-10-03 and archived in class-launch-sources; faction/server rules only, no live population inferred |
| [Information on Server Transfer](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2) | Global | 2026-09-30 | Public Global community API response refetched 2026-10-03 and archived in class-launch-sources; faction/server rules only, no live population inferred |

### macro-guide

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [Aion 2: Makro – Karsten Scholz's launch-period menu walkthrough](https://mein-mmo.de/aion-2-makro-mehr-schaden/) | Global | 2026-09-30 | Launch-period walkthrough with menu screenshots; priority and hold behavior are attributed to the author, not reproduced by this site |
| [AION 2 Cleric Guide For Skills & Stigmas \| Daevanion & Macros Setup \| Ultimate Beginners Guide](https://www.youtube.com/watch?v=UPjsUVC0DtA) | Mixed | Unspecified | Existing live-server low-level character modelling Global progression; delay advice does not establish current Global timing |
| [AION 2 Global Operation Policy](https://www.plaync.com/policy/operation/aion2global/en) | Global | Unspecified | Policy read October 3, 2026; general unauthorized-program rules, no permission inferred for external input automation |

### notmeter

| Source | Region | Published | Version / context |
| --- | --- | --- | --- |
| [NotMeter maintainer website and installation panel](https://notmeter.com/) | Mixed | Unspecified | October 3, 2026 website snapshot: Korean interface with KR, TW and Global search; desktop Global operation not tested |
| [Not4You-Dev NotMeter-Releases](https://github.com/Not4You-Dev/NotMeter-Releases/releases) | Mixed | Unspecified | Public distribution repository; latest label v1.0.246 published August 29, 2026; release body has no Global compatibility details |
| [Npcap Windows Packet Capture Library and Driver](https://npcap.com/) | Mixed | Unspecified | Windows driver documentation; current version need not match the maintainer-linked installer |
| [AION 2 Global Operation Policy](https://www.plaync.com/policy/operation/aion2global/en) | Global | Unspecified | Current policy read October 3, 2026; general unauthorized-program rules, no specific NotMeter approval found |
