# Service guides: Global as the default context

Reviewed 2026-10-04. Scope: `code`, `download`, `maintenance`, `monetization`, `player-count`, `server`, `server-transfer`, `steam`, `twitch-drops`, `database`, and `global-changes`, in English, Japanese, Spanish, and German.

All 44 localized articles and 88 MDX/metadata files were reviewed against `before/src/content/`. 84 files changed. The four `player-count.json` files already contained no redundant Global wording and were retained. Existing content, important restrictions, statistics and factual dates were not reinterpreted.

## Changes

- Removed repetitive default-region wording from headings, SEO descriptions, summaries, quick answers, paragraphs, FAQ, alt text, captions, and diagrams.
- Coupon copy now says coupon/client/account without repeating Global throughout redemption instructions. The region comparison still states that Global, Korea and Taiwan have separate promotions.
- Download copy now directly describes PC requirements and Steam/PURPLE installation. Kept the actual PURPLE service selection, launcher-region setting, separate Taiwan installer and cross-service progress restriction.
- Maintenance and monetization copy now directly describes maintenance windows, access, membership and rewards.
- Player-count copy keeps Steam/PURPLE and regional-client statistical scope, while removing Global from the ordinary server-guide link and client wording. Numeric figures and their dated reading were unchanged.
- Server and transfer pages now use plain server/region/transfer terminology. Removed the generic instruction to apply Global transfer conditions, because the immediately preceding sentence already lists the conditions to read.
- Steam copy now uses main game, public access, supported platform and current availability. Its default-platform table now says no mobile client, as requested by the root reviewer; regional-release comparisons remain separately labeled.
- Twitch copy now directly names Drops and launch rewards. Kept the explicit exclusion of Korea/Taiwan accounts.
- Database copy no longer repeatedly labels default catalogues or beginners Global. Regional filter choices and test-client data distinctions remain.
- `global-changes` keeps its required title and Global-versus-KR/TW comparison, while simplifying repetitive phrases such as your Global character/journal and ordinary next-action headings.
- Japanese coupon caption describes the pictured three reward types, keeping useful detail after removing the region label.

## Why the remaining region wording stays

| Theme | Retained wording and practical reason |
| --- | --- |
| code | Global/Korea/Taiwan promotions differ. The comparison heading and explanatory sentence prevent using a code for the wrong service. |
| download | Select the Global AION 2 service in PURPLE; use Global in the launcher-region control where the listed Southeast Asian availability issue applies. The Taiwan installer, Steam product and non-transferable KR/TW progress require explicit service distinctions. Diagram/checklist labels retain the actual service choice. |
| maintenance | Global, Korea and Taiwan have separate maintenance schedules; a notice from another service does not establish this service's outage. |
| server | Asia is the Global regional pool, distinct from Taiwan. KR/TW character progress does not transfer into it. |
| steam | The Global/Japan/Taiwan section, service-table label and Japanese Global-site link identify the actual service and distinguish it from KR/TW release information. Ordinary platform/access descriptions no longer repeat Global. |
| twitch-drops | Campaign eligibility is restricted to Global players and excludes Korean/Taiwan accounts; this affects reward delivery. |
| database | AION2 Hub's Global/Korea-Taiwan filter is an actual product control. Its Global test-client entries and KR/TW comparison values are meaningful differences. The region-selection diagram must name the service choices. |
| global-changes | Global is the explicit comparison object and established topic/keyword. Level 45 versus KR/TW level 50, eight classes versus Brawler, later dungeons, separate accounts/servers, and matching the database service all require retained region labels. |

`monetization`, `player-count`, and `server-transfer` retain no ordinary visible Global qualifiers in the reviewed files. Internal asset IDs, component IDs, anchor IDs and URLs were preserved regardless of wording.

## Verification

- Compared all 88 files with the supplied before snapshot.
- MDX links, anchors, component declarations/order, numeric tokens and table column counts were unchanged.
- JSON source arrays, IDs, asset IDs, keywords, slugs, URLs and `inlineNext` values were unchanged.
- All JSON parses; files remain UTF-8. No replacement-character or corrupted-question-mark matches were found in the owned files.
- Metadata and localized prose were reread to fix grammar after removing qualifiers, including the German Windows-client summary and English server-pool quick answer.
- Root is responsible for the final whole-site content test and production build. No shared UI or article-data was edited in this task.

