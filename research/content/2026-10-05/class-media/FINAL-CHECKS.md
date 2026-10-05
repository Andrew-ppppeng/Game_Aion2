# Final checks — class media, 2026-10-05

Final preview: http://localhost:3005 . Isolated production output: `.qa/class-media-final`. The temporary Next.js additions to tsconfig were restored from the exact original backup; the existing line-ending-only working-tree change was left outside this task's commit.

- Production build passed: 164 generated pages.
- Full ESLint and TypeScript checks passed with `npm run check`.
- Content check passed: 140 localized articles, 40 provenance-tracked artwork/poster assets, 280 exact locally stored skill icons with SHA-256 checks, valid class relationships, and all 36 PNG exports with SHA-256 checks. No missing download assets, mixed-class skill nodes or absent translations.
- Smoke check passed: 160 page checks, 140 published articles and 148 sitemap entries; navigation, redirects, language alternates and resources remain intact.
- Dedicated class browser check passed: 36 class/Builds pages across four languages; Classes galleries also tested in all four languages. All 35 skill names and icon images per class, open/collapsed skill groups, real diagram anchors, eight gallery choices, eight build-map choices, mutually exclusive specialization effects, 320px width and enlarged text were verified. No local resource failures or browser exceptions.
- Actual PNG download was performed and saved: suggested filename, successful completion and exact image bytes were checked against the local Templar export.
- Full browser check passed: all 140 articles, artwork captions, language links and preserved query/hash, keyboard zoom/focus, responsive diagrams, navigation and existing interactions; no runtime errors. Asset download URLs remain shared `/media/` paths while article links remain localized.
- YouTube checks: all eight official oEmbed records identify AION 2 Official; all eight live embed documents return 200 with player configuration. A separate browser test performed a real Templar play action without an iframe fixture: video readyState=4, paused=false, time≈1.99s, and no player errors. The screenshot and raw result are retained. Automated four-language interaction checks stub only the external iframe to keep CI independent of video-service availability; that stub is not used by the site or the live playback test.
- Static exports omit click/save instructions, radio controls and highlighted default choices. The PNGs describe the alternatives without implying that an example's default selection is recommended or that a saved image follows a reader's current UI selection.

Screenshots: `.qa/classes/templar-map-desktop.png`, `.qa/classes/templar-skills-en.png`, and `research/content/2026-10-05/class-media/live-player.png`. The four-language full-size diagram artifacts are under `public/media/guides/`; byte/source manifests are under `src/content/`.

No keyword expansion, new balance ranking, optimal endgame allocation, game-UI screenshot claim, or numerical DPS claim was added.
