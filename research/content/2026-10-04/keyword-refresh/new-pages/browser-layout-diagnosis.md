# Browser home-layout wait diagnosis

Date: 2026-10-04. Local production server: `http://127.0.0.1:3031`, old build held by root for diagnosis. Browser: installed system Chrome through Playwright. Product code and the existing browser test were not changed by this diagnosis.

## Result

The home-layout loop can be verified using document/content readiness. Waiting for global `networkidle` in this loop repeatedly times out even when the document is complete and the expected interface is present. Installing or resuming the fake clock does not account for the failure.

## Reproduction

Temporary script: `.qa/keyword-refresh-network-diag.mjs`; full request evidence: `.qa/keyword-refresh-network-diag.json`.

Three separate browser contexts reproduced the relevant suite sequence: initial home, coupon interactions where applicable, classes page, Japanese language switch, and home viewport changes. Each used a 12-second navigation limit rather than the original 30-second limit to collect the repeated failure efficiently.

| Context mode | Result | Failure location | Document at failure |
| --- | --- | --- | --- |
| Original fake clock and coupon flow | Timeout | English 768px, third layout navigation | `readyState=complete`, `lang=en`, `h1=AION 2` |
| Fake clock omitted | Timeout | English 768px, third layout navigation | `readyState=complete`, `lang=en`, `h1=AION 2` |
| Original flow, then clock resumed | Timeout | English 768px, third layout navigation | `readyState=complete`, `lang=en`, `h1=AION 2` |

The requests still tracked at failure include Next route-tree prefetches to `/races`, `/map`, `/macro-guide`, and `/twitch-drops`, with `next-router-prefetch: 1`, `next-router-segment-prefetch: /_tree`, and `rsc: 1`. A width-750 optimized `/media/atreia.jpg` request is also tracked. Some modes additionally retain Japanese route-prefetch requests from the preceding language switch. The request list is evidence that network-idle is not reached; it does not by itself distinguish an unfinished server response from a canceled or superseded browser request whose completion was not reflected in the tracked lifecycle.

## Proposed wait verified twice

Temporary script: `.qa/keyword-refresh-layout-ready-diag.mjs`; result: `.qa/keyword-refresh-layout-ready-diag.json`.

The second script retains the original initial-home, coupon copy/denied-copy/expiry, sidebar count/status, four journey cards, classes-language-switch, and current-navigation assertions. Only home-layout navigation uses `waitUntil: 'domcontentloaded'`. Each layout then waits for its exact localized `home.hero.title` and visible `.hero-buttons`, checks the `html` language, checks horizontal overflow, and checks all hero-button bounds. The Japanese home title is `AION2`, as defined in its message file.

Both runs passed all 11 original home layouts: English 1440/1024/768/390/320, Japanese/Spanish/German 390, and Japanese/Spanish/German 1440. Durations including the retained preceding assertions were 5.346s and 4.691s. All layout document snapshots were `readyState=complete`; there were no page errors or same-origin HTTP responses at or above 400 in either run.

## Minimal recommendation

Change only the home-layout loop's navigation wait to `domcontentloaded`, followed by explicit localized H1 and hero-button visibility assertions. Preserve its existing language, overflow, and button-bounds checks. The initial-home and classes navigation waits do not need to change for this specific fix. No change to product prefetch behavior or coupon timers is supported by this diagnosis.

This diagnosis covers the home loop and its prerequisites; the complete article suite still needs root's final run against the rebuilt product.
