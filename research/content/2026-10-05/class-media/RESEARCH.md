# Class media and skill diagrams — 2026-10-05

## Player tasks checked before editing

1. See each class's weapon motion and movement before choosing it.
2. Recognize the real icon next to a skill name while reading the explanation.
3. See which condition opens a follow-up and which relationships require a selected specialization.
4. Understand that a rank threshold unlocks choices, and does not apply all alternatives.
5. Read diagrams at phone width, select a node to find its explanation, and save a larger image.
6. Switch class diagrams in Builds without scrolling past all eight full diagrams.

## Official media

Source: https://aion2.plaync.com/en-us/about/index

The live official JS asset `https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/js/main.js` contains the eight class videos in `Ko`, in the same order as the official Global class roster. Saved unmodified as `about-main.js`. The eight YouTube oEmbed responses identify the publisher as **AION 2 Official**. Raw responses and local thumbnail originals are retained. Public previews are 960px WebP copies of the corresponding actual thumbnails. Public source/provenance records are in `src/content/guide-assets.json`; no credit or research discussion appears in article copy.

| Class | Video |
| --- | --- |
| Gladiator | https://www.youtube.com/watch?v=ndri5XpnRK4 |
| Templar | https://www.youtube.com/watch?v=Zs6HnL2N5Hk |
| Assassin | https://www.youtube.com/watch?v=jUW24SLKK3I |
| Ranger | https://www.youtube.com/watch?v=C6INRqEqv3Y |
| Chanter | https://www.youtube.com/watch?v=rtOt3KvmYCI |
| Cleric | https://www.youtube.com/watch?v=RU-4yiNNnY0 |
| Sorcerer | https://www.youtube.com/watch?v=jh1ydFq6FI0 |
| Spiritmaster | https://www.youtube.com/watch?v=LJq1QGRJSLI |

Complete available captions were fetched and read. Chanter has only repeated voice lines at 00:06–00:17; Sorcerer has incomplete voice lines at 00:04–00:13; Assassin has one voice sound at 00:28. The other five clips have no captions. Exact snippets/timestamps and unavailable-caption errors are saved in `official-class-videos.json` and the individual `*-captions.json` files. The clips are used solely for combat-animation previews; no build, timing, cooldown or skill-mechanic claim is inferred from those clips. Existing complete instructional transcripts remain in the preceding eight-classes research directory.

Video iframes are created only after a player clicks Play, using the original official video ID on youtube-nocookie.com. Each card retains the actual watch link. Changing the gallery class resets the previous player. No autoplay occurs on first render.

## Official skill screenshot search and limits

- The English `/en-us/guidebook/view?title=Skills` request returns NC's generic error page rather than a skill guide.
- The KR guidebook UI and its version-2.1.2 JS are archived; the skill-title endpoint returns an empty body, including with `gwLocale=ko_KR`. Browser access redirects to a search page without skill images. Responses and screenshots are retained; none is published as a working screenshot.
- NC Lounge https://lounge.plaync.com/feed/51926?country=KR&locale=ko-KR is an **NCER AI-generated** article from 2025-12-22; it explicitly says its information can differ from the game. It contains two generic publication/tag images rather than a usable skill tree. Not adopted as verified skill evidence or published imagery.
- A live screenshot attempt for https://aion2.gaming.tools/build-planner encountered Cloudflare's security check. The challenge screenshot is retained locally, excluded from product assets. No protection bypass was attempted.

No usable official full skill-tree screenshot suitable for the default service was established by this search. Author-created diagrams therefore visualize the already verified client mechanics; they are titled **Skill connections**, not presented as screenshots of the game's tree or an official point allocation. PNG exports are screenshots of the corresponding site components.

## Skill icons and relationship facts

The previously archived 280 client records from https://aion2.gaming.tools/skills provide each skill's iconPath. The same exact WebP files are stored at `public/media/skills/{id}.webp`. `skill-icon-sources.json` retains the first-pass network failures; `skill-icon-sources-final.json` records successful retries or an exact shared iconPath from another skill. `src/content/skill-icons.json` stores dimensions, original URL, source URL, date, region, client version and SHA-256 for all 280 final images. No invented icons or arbitrary skill/image pairings.

Region: Global. Client data version: 1.0.21.0, updated 2026-09-30. Cross-check details and source conflicts remain in `../eight-classes/RESEARCH.md` and raw client records.

| Class | Diagram relationships and conditions |
| --- | --- |
| Gladiator | Keen Strike on-hit Ruinous Blow cooldown reduction requires selected rank-12 option; Mocking Blade knockdown opens Overhead Slam; Sword Aura Rampage requires Stagger. Immune-target proc is preserved. |
| Templar | Shield Smite or Warding Strike opens Judgment for 2s; Pummel shortens Punishment only with selected rank-12 option; Block opens Debilitating Smash. |
| Assassin | Savage Roar engraves target-bound Insignia, up to five stacks for Insignia Explosion; a critical hit opens Heart Gore; Quick Slice cooldown reduction needs selected rank-12 option. |
| Ranger | Marking Shot's Precision enables Suppressing Arrow and boosts Deadshot; Snare Shot's Slow enables Burst Arrow; a crit opens Drill Dart, but its own crit supplies its MP recovery. |
| Chanter | Impactful Crush or Spinning Strike opens Dark Crush for 2s; Onslaught cooldown reduction needs selected rank-12 option; Heat Wave Blow follows Parry or the selected approach-trigger specialization. |
| Cleric | Chain of Torment must remain active for Condemnation; only Condemnation's own crit with the selected rank-12 reset removes its cooldown; Radiant Recovery is shown as a manual response, healing and removing one debuff in its base effect. |
| Sorcerer | Flame Arrow plus Fire Mark passive applies the required mark for Blaze; Firestorm on-hit Hellfire cooldown reduction needs selected rank-12 option; Frost enables Frost Burst, preserving immune-target proc. |
| Spiritmaster | Four spirit-skill activations give Four Elements for Fusion, not four different summoned spirits; summon/spirit action gives the brief Dimensional Control window; Water's landed spirit attacks restore MP. |

Hellfire rank-8 branch options are exactly those in `15060000.json`: +30% skill speed; fire damage over 10s on hit; mobile casting. The interactive example permits only one selection in that slot. It makes no assertion about purchased/bonus rank split, final slot unlocking, or optimal DPS.

## Deliverables and validation

- Eight localized class pages, Classes, Builds and Cleric Build: 44 article bodies updated across en/ja/es/de.
- Eight official combat previews; all 280 icon images locally served; each class has three practical relationships with clickable skill destinations.
- 32 localized class-map PNGs and four localized Hellfire specialization PNGs. `scripts/generate-class-skill-map-images.mjs` reproduces them from the actual site components; it keeps every pixel of the component and does not alter screenshots. `src/content/class-diagram-images.json` records the provenance and hashes.
- Mobile maps become vertical; active/passive/Stigma tables retain all names and level information; legacy page headings and anchors are preserved.
- The unrelated Chanter illustration in Builds is replaced by the functional Hellfire specialization tree.
- Validation results are recorded in FINAL-CHECKS.md after browser checks.
