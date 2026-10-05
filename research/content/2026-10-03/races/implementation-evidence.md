# aion 2 races: implementation evidence

Checked: 2026-10-03. Target and sources: Global. Locales: en, ja, es, de.

## Sources actually read
- Official about page: https://aion2.plaync.com/en-us/about/index . Web extraction is JavaScript-limited. Refetched the previously observed official content API URL; HTTP 200 and complete response archived at ../class-launch-sources/about-en-source.json.
- Confirmed two factions, Elyos and Asmodians, the separate eight-class roster, Verteron/Altgard world identities and named example locations. Reviewed official locale archives for canonical labels: ja 天族/魔族; es Elios/Asmodianos; de Elyos/Asmodier. No old AION racial skill copied.
- https://aion2.plaync.com/en-us/board/notice/view?articleId=6abab930eea53f5d6dbcf939 : refetched public API HTTP 200; full body read and archived at ../class-launch-sources/matchmaking-source.json. Separate faction servers, temporary opposing pairings and cross-faction opponents verified.
- https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd2d50a279104f7d9d5ee2 : refetched public API HTTP 200; archived at ../class-launch-sources/transfer-source.json. October 14 start, same-faction transfer, initial EA-to-EA restriction and cross-server instances verified.

## Decisions and limitations
- One substantial page serves the original races keyword by explaining actual faction decisions, friend coordination, opponents and transfer limits. No new keyword invented.
- No unsupported racial damage bonus, population ranking, universal faction winner or cross-faction/cross-region grouping claim. Official cross-server instance claim does not prove those additional capabilities.
- Independent Global faction-change procedure/price/cooldown remains unverified. The same-faction transfer notice cannot be used to claim faction changes.
- Reusable three-step workflow is an editorial decision aid, not an in-game screenshot. All translations keep canonical faction names, evidence links and page anchors.
