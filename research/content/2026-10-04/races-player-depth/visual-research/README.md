# AION 2 Global faction world visuals

Research date: 2026-10-04. Scope: original official AION 2 images and their corresponding Global world descriptions. Files were saved in this new research directory; existing archives, `src/content/guide-assets.json`, and `public/` were not modified.

## Source and version

- Publisher: NC. Region: Global, English introduction.
- Official page: https://aion2.plaync.com/en-us/about/index
- Official content endpoint: https://aion2.plaync.com/en-us/conti/getContent?service=aion2global&alias=about-en
- Content API `version`: **3**. This is an introduction-content revision, not a gameplay patch number.
- Official static package: `https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/`. Static package version **1.0.0**, not a gameplay patch number.
- Raw files: `global-about-page-20261004T073838Z.html`, `global-about-content-api-20261004T073838Z.json`, `20261004T073913Z-global-about-main.js`, and `20261004T073913Z-global-about-style.css`.
- Images were downloaded unchanged on 2026-10-04 around 07:39:45–07:39:46 UTC. `image-manifest-20261004T073944Z.json` contains exact download URLs, dates, HTTP status, dimensions, file sizes, and SHA-256 hashes.
- Existing corroborating archive: `research/content/2026-10-03/class-launch-sources/about-en-source.json`. Existing `world-elyos` / `world-asmodians` guide assets are thumbnail 1: Dawn Legion Base / Safe Haven.

## How image names were matched to locations

The official JavaScript World component receives the faction, reads the `elyos` or `asmodians` array from the content API, and selects a location title and description using the current slide index. Its five thumbnails use index + 1 in `thumb-item--N`. The official stylesheet maps those classes to `elyos-thumb-N.webp` and `asmodians-thumb-N.webp` respectively. Therefore thumbnail 2 corresponds to API array item 2, thumbnail 4 to item 4, etc.; the associations were not inferred from visual appearance.

The raw API contains damaged punctuation in several apostrophes and a dash. Original bytes are preserved. The summaries below paraphrase the readable location information and do not treat the damaged characters as gameplay information.

## Recommended images

All four recommended scenes are **824 × 464 pixels**, landscape WebP images with no embedded language label. Each was visually inspected. Their actual scenes support named-location descriptions, rather than universal claims about either faction's lighting, moral alignment, appearance presets, or power.

| Priority | Location | Exact original image URL | Local original file | What the picture shows and useful comparison |
| --- | --- | --- | --- | --- |
| 1 | Elyos — Cantas Valley, Verteron | https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-2.webp | `20261004T073944Z-elyos-thumb-2.webp` | A broad rocky valley beneath a warm sky, red and pale ground cover, and distinctive elevated vegetation. It adds a concrete landscape beyond the existing hidden legion base. |
| 1 | Asmodians — Moslan Forest, Altgard | https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-4.webp | `20261004T073944Z-asmodians-thumb-4.webp` | A misty forest with bare branching trees and damaged ground. The official description of a forest destroyed by fire explains this particular scene. |
| 2 | Asmodians — Nornir Assembly, Altgard | https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/asmodians-thumb-5.webp | `20261004T073944Z-asmodians-thumb-5.webp` | A sunlit green settlement among tall rock pillars decorated with turquoise markings, paths, and a blue central feature. This provides an attractive inhabited Asmodian location and demonstrates its environmental variety. |
| 2 | Elyos — Altamia Canyon, Verteron | https://assets.playnccdn.com/static-about-game/aion2-global/1.0.0/img/world/elyos-thumb-5.webp | `20261004T073944Z-elyos-thumb-5.webp` | Large overgrown architectural ruins, broken arches, vegetation, and massive terrain above. It adds an architectural environment distinct from Cantas Valley's open ground. |

Suggested two-image addition: **Cantas Valley + Moslan Forest**, placed beside the corresponding named-region descriptions. If four scenes fit the page, add **Altamia Canyon + Nornir Assembly** to show variety within both factions. Do not describe all Elyos areas as bright or all Asmodian areas as dark: the inspected Nornir Assembly and existing Safe Haven images contradict that simplification.

Suggested concise English captions:

- `Cantas Valley in Verteron.`
- `Moslan Forest in Altgard.`
- `Nornir Assembly in Altgard.`
- `Altamia Canyon in Verteron.`

## World descriptions corresponding to every official image

These are paraphrases of the Global introduction API. They describe named locations and story context; they do not establish exclusive resources, faction bonuses, class availability differences, movement speed, combat strength, or current quest rewards.

| Image file suffix | Faction / region | Location | Official introduction information, paraphrased |
| --- | --- | --- | --- |
| `elyos-thumb-1.webp` | Elyos / Verteron | Dawn Legion Base | Hidden in a secluded ravine within Cantas Valley and used as the Dawn Legion's secret command center. |
| `elyos-thumb-2.webp` | Elyos / Verteron | Cantas Valley | A former important Odylium area for Daeva. Depletion left the land abandoned; the Dawn Legion searches for remaining traces. |
| `elyos-thumb-3.webp` | Elyos / Verteron | Ellun River Marsh | A ruined downstream marsh occupied by Illusion Cavaliers while they rebuild Verteron's fallen Barrier Tower. |
| `elyos-thumb-4.webp` | Elyos / Verteron | Aullaeu Village | A settlement at the edge of Tolbas Forest, populated by servants of the Balaur and connected with the forest's unrest. |
| `elyos-thumb-5.webp` | Elyos / Verteron | Altamia Canyon | An eastern Verteron canyon once containing Zumion Temple, submerged and later exposed again under the Notos Legion's watch. |
| `asmodians-thumb-1.webp` | Asmodians / Altgard | Safe Haven | A northern Altgard refuge formerly used by criminals; after the Dredgion's fall, it remains untouched by Balaur assaults. |
| `asmodians-thumb-2.webp` | Asmodians / Altgard | Dredgion Crash Site | A Fafnir Legion Dredgion crashed into this scorched canyon. Leaking Drakana corrupted the land and left it isolated. |
| `asmodians-thumb-3.webp` | Asmodians / Altgard | Sanctum Outpost | Formerly a sanctuary of Zikel, now a Balaur stronghold where captured Daeva are transformed into Fafnites. |
| `asmodians-thumb-4.webp` | Asmodians / Altgard | Moslan Forest | A former Elim and Nornir sanctuary burned by Hystan's flames, with wounded Elim remaining among the ashes. |
| `asmodians-thumb-5.webp` | Asmodians / Altgard | Nornir Assembly | A hidden settlement built by refugees from Moslan Forest, protected by ancient magic and guided by Urd of the Three Sisters of Fate. |

## Additional original art saved

- `img/factions/char-l.webp` — **1094 × 1151**, transparent promotional character composition placed on the left of the official faction introduction, aligned with the Elyos label and emblem.
- `img/factions/char-r.webp` — **1301 × 1246**, transparent promotional character composition placed on the right of the same introduction, aligned with the Asmodians label and emblem.
- `img/factions/emblem-elyos.webp` and `emblem-asmodians.webp` — **884 × 880** each, official faction symbols.

The character compositions show the official marketing presentation of the factions. They are not recommended as proof of required player appearance or racial anatomy. The scene images are the stronger choice for the requested geography comparison. The faction character files and symbols were also downloaded unchanged and recorded in the image manifest.

## Alternatives and remaining limits

- The Steam official store was checked, but its browser-facing page led to an age gate. A direct appdetails request did not yield an additional archived response in this run. It is not needed for the recommendation because the official Global introduction provides ten unambiguous faction/location associations.
- No higher-resolution still counterpart for the world thumbnails was observed in the current official stylesheet or JavaScript. The four recommended original stills are 824 × 464; they should not be described as full-resolution cinematic frames.
- All saved images belong to the **AION 2 Global** official introduction package. No AION 1 image and no generated image were used.

