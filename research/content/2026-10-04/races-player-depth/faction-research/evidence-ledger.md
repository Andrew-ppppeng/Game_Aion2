# AION 2 faction differences — official research ledger

Research date: 2026-10-04, Asia/Shanghai. This is an internal evidence record, not player-facing copy. No `src` file was changed by this researcher.

## Scope and source classes

This pass freshly fetched official Global promotional material, official community notice APIs, NC corporate press releases, and one official Global game-data item API. It also cross-checks the already archived AION 2 Official Global dungeon broadcast, newly located by the independent reviewer. It does not infer game rules from AION 1, fan wikis, gold sellers, forum assertions, or the absence of a sentence in an official introduction.

Fresh raw bodies, request metadata, retrieval times and regions are beside this log. `fetch-manifest.json`, `context-fetch-manifest.json` and `browser-manifest.json` identify requests and outcomes. The About API and image originals fetched in parallel are preserved in `../visual-research/`; their exact evidence paths are listed below. No old raw research was overwritten.

## Global facts ready for player copy

| Subject | Direct fact / usable wording | Precise evidence |
| --- | --- | --- |
| Faction worlds | Elyos explore Verteron; Asmodians explore Altgard. | [Global About](https://aion2.plaync.com/en-us/about/index), decoded `jsonData.elyos[0].description[0]` and `jsonData.asmodians[0].description[0]` in `../visual-research/global-about-content-api-20261004T073838Z.json`. [Official content API](https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en). Global; current launch introduction; static resource version `aion2-global/1.0.0`; retrieved 2026-10-04 07:38:38 UTC by visual researcher. |
| Elyos landmarks | Dawn Legion Base is the concealed command center in Cantas Valley. Ellun River Marsh has the ruined Barrier Tower; Aullaeu Village lies by Tolbas Forest; Altamia Canyon contains the former Zumion Temple. | Same About data, `elyos[0]`, `[2]`, `[3]`, `[4]`. Matching sections in [Tale of Two Worlds](https://aion2.ncsoft.jp/en/teaser), newly saved `global-two-worlds-rendered.txt` and `.html`; Global; retrieved 2026-10-04 07:40:42 UTC. These describe locations, not mandatory quest order or spawn coordinates. |
| Asmodian landmarks | Safe Haven is the settlement in northern Altgard. Dredgion Crash Site is a corrupted canyon. Sanctum Outpost is a Balaur stronghold. Moslan Forest and Nornir Assembly connect the Elim and Nornir refugee story. | Same About data, `asmodians[0]` through `[4]`; matching official Two Worlds sections in the freshly saved render. |
| Different story enemies | Elyos story material centers on Ishtar's invasion and Daevas used to create Surana. Asmodian material centers on Fafnir and Daeva souls imprisoned in jewels as Fafnites. | About decoded `lore.elyos[3]`, `[4]` and `lore.asmodians[3]`, `[4]`. This supports different narrative focus; it does not supply named quest rewards, complete campaign order, or a first playable spawn. |
| Faction servers and opposing players | Each faction has its own servers. Abyss and Spacetime Rift opponents come from the opposing server assigned to yours. Pairings change periodically. | [Advanced Access Server Matchmaking](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939); raw `global-pairing.json`, `article.content.content`; paragraphs under “What is Server Matchmaking?” and “Will My Server Pairing Always Be the Same?”. `article.contentMeta.timestamps`: published 2026-09-29 01:05 UTC, updated 2026-10-02 14:09 UTC. Fresh API fetch 2026-10-04 07:39:00 UTC. Global; Advance Access / launch notice. |
| Dungeon cooperation | Global dungeon parties can include players from another faction and other servers. Use the My Faction Only checkbox when creating a party to restrict recruitment to your own faction. | [AION 2 Official dungeon showcase](https://www.youtube.com/watch?v=S_TjiOh33a4&t=3662s); archive `research/content/2026-10-02/leveling/S_TjiOh33a4-transcript.json` and `.txt`, 61:02–61:25. The hosts explicitly say Global launch, opposite faction, different servers, and My Faction Only. New precise evidence file `../independent-review/global-dungeon-party-evidence.json`; official-channel identity and Sept 4 broadcast announcement established there. Original snapshot retained; today's attempted YouTube re-open was throttled, so this is not logged as a fresh replay. Restrict claim to dungeons; it does not establish cross-region parties or shared open-world quests. |
| Transfer conditions | Global server transfers remain within the same faction. They begin October 14, 2026. Initially EA characters transfer only between EA servers, and initial transfers are free. | [Information on Server Transfer](https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2); raw `global-transfers.json`, `article.content.content`. `article.contentMeta.timestamps`: published 2026-09-30 15:40 UTC, updated Sept 30 18:32 UTC. Fresh fetch 2026-10-04 07:39:00 UTC. Global; launch transfer announcement, not permanent pricing. |
| Shared equipment example | Clash Rune is usable by both factions. | [Official Global EU item API](https://aion2.plaync.com/en-us/api/gameconst/item?id=310900001&enchantLevel=0&lang=en-US&region=eu), raw `global-clash-rune-example.json`: `id=310900001`, `name=Clash Rune`, `raceName=All`. Fresh fetch 2026-10-04 07:43:45 UTC. This verifies one item only; it does not prove universal equivalence of every faction's gear or stats. It is probably too narrow to add to a faction overview. |

Useful editorial structure: compare worlds, landmarks, narrative enemies and faction visuals, then separate open-world/PvP alignment from dungeon cooperation. The existing Class row can link to `/classes` without presenting a racial power ranking. Do not invent a faction advantage to fill the table.

## Regional facts that must not become Global launch claims

| Evidence | Region / version context | Supported fact and scope |
| --- | --- | --- |
| [NC March 11 update](https://about.ncsoft.com/en/news/article/aion2_update_260311); `nc-march-cross-faction.html`, `-text.txt`, request metadata | March 11, 2026 live regional service, before Global launch. Retrieved Oct 4. | Cross-faction PvE party cooperation was added. Do not use this date to date Global availability; the Global broadcast above is the appropriate Global evidence. |
| [NC March 25 update](https://about.ncsoft.com/en/news/article/aion2_update_260325); `nc-chaotic-abyss.*` | March 25, 2026 regional update, before Global launch. | Chaotic Abyss uses server-level West/East forces irrespective of faction, while Rifts retain race-based matching. Do not replace the Global launch notice's faction-server Abyss pairing with this different regional system. |
| [NC July 1 Korean original](https://about.ncsoft.com/news/article/Aion2_update_20260701) and [July 6 English release](https://about.ncsoft.com/en/news/article/aion2_update_260706); `nc-kr-new-regions-original.*`, `nc-new-regions.*` | Chapter 1 regional service: level 50 / ninth class Brawler. | Eltnen is the new Elyos region and Morheim the new Asmodian region. Do not advertise either as a Global launch progression zone from this evidence. The Korean original gives July 1 as update date; July 6 is the English release publication date. |
| [Official KR Expedition guidebook](https://aion2.plaync.com/ko-kr/guidebook/view?title=%EC%9B%90%EC%A0%95) | Current KR guide indexed by web search; five-player party wording. | Indexed text supports same-party Elyos/Asmodian Expedition play and all-faction / same-faction recruitment settings. The browser visit redirected to a search page with no results; the newly saved render does not independently verify its indexed article body. Use the Global broadcast for the public Global page. |

Region sanity checks: [Nov 18, 2025 official KR/TW launch release](https://about.ncsoft.com/news/article/aion2_update_251118), saved `nc-kr-tw-launch-context.*`, names the November 19 KR/TW launch. [Oct 1, 2026 Global release](https://about.ncsoft.com/news/article/A2_update_20261001), saved `nc-global-launch-context.*`, names September 30 Global EA and October 5 launch. English corporate news written before that Global launch is not automatically Global patch documentation.

## Popular claims without sufficient Global official basis

- **Poeta / Ishalgen are the exact Global first playable spawn points.** The official lore names them as territories attacked by Ishtar / Fafnir. That text does not establish a character's spawn, mandatory first quest or exact tutorial sequence. Use the confirmed world regions Verteron / Altgard.
- **Elyos and Asmodians have different racial damage bonuses or faction-exclusive versions of class skills.** No official Global evidence located in this pass. Likewise, no basis was found for saying every skill and item is mechanically identical. Keep the public page focused on documented differences; do not substitute “not announced” with a universal equality claim.
- **Fire Temple / Kromede, Draupnir / Bakarma or a listed Expedition dungeon is restricted permanently to one faction.** Global About and teaser present four Expedition entries together, and the official Global broadcast permits opposite-faction dungeon parties. No Global faction-entry restriction was found. Do not borrow AION 1 access restrictions.
- **Every white wing belongs only to Elyos, every black wing only to Asmodians; all later wings are universally shared; starter-wing names and quest requirements are fixed.** Official artwork can support a caption about the depicted wing color, but it does not establish these blanket equipment rules. A single `raceName=All` rune also cannot prove wing compatibility.
- **Asmodians necessarily have AION 1 claws, back mane, red-eye combat transformation or fixed blue-grey skin.** AION 1 artbook and old game pages are excluded. Use AION 2 customization or inspected AION 2 official imagery for appearance descriptions.
- **One faction has better rewards, faster leveling, stronger bosses or a guaranteed population advantage.** No official Global comparative data found. Different world names and plot enemies do not establish those rankings.
- **Cross-faction dungeons imply shared open-world questing, same Legion, a transfer changing faction, or cross-region grouping.** The cited Global evidence supports none of these extensions. Same region/faction/server remains the practical coordination choice for ordinary shared questing.

## Official image URLs for actual faction content

The visual researcher fetched originals; checksums, sizes, dimensions, retrieval timestamps and region/version are in `../visual-research/image-manifest-20261004T073944Z.json`. Use the separate visual report for inspection findings. Simple literal captions should be used on the public page; provenance remains here.

- Dawn Legion Base: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-1.webp
- Cantas Valley: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-2.webp
- Ellun River Marsh: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-3.webp
- Aullaeu Village: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-4.webp
- Altamia Canyon: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-5.webp
- Safe Haven: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-1.webp
- Dredgion Crash Site: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-2.webp
- Sanctum Outpost: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-3.webp
- Moslan Forest: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-4.webp
- Nornir Assembly: https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-5.webp

Use the separate visual research report for emblem and character-art assignments; do not label an inspected decorative artwork as a tested default equipment item.

## Retrieval limits recorded accurately

Steam appdetails and ISteamNews API requests failed with `RemoteDisconnected`; their failure metadata is saved. Web Steam store open led to the age gate. No new Steam body is claimed. Public Global guidebook `/en-us/guidebook/index` returned an HTTP 200 response but redirected to the NC error/500 page; this is not a usable guidebook destination. The official About API, official teaser, official notices, NC news and the preserved official broadcast provide multiple independent official material types without relying on these failed endpoints.
