# Browser tail screenshot image diagnosis

Date: 2026-10-04. Local final-build server: `http://127.0.0.1:3031`. Browser: system Chrome through Playwright. This work did not modify product code, source images, or `scripts/browser-check.mjs` and did not repeat the 124-article suite.

## Reproduction and image state

Temporary reproduction script: `.qa/keyword-refresh-home-image-diag.mjs`; report: `.qa/keyword-refresh-home-image-diag.json`.

The original home screenshot sequence was reproduced in separate desktop 1440×1000 and mobile 390×844 contexts: install `page.clock` at `2026-10-02T11:00:00Z`, navigate home with `networkidle`, scroll `.about-visual` into view, assert its image visibility, then wait for every document image to be complete with a positive natural width.

Desktop passed the all-image check and both screenshots. Mobile failed. The failing image is actually visible, so excluding hidden images does not resolve the issue:

- Element: `.about-visual img`.
- Element `src`: `/_next/image?url=%2Fmedia%2Fatreia.jpg&w=3840&q=75` (fallback src; selected request width is 384).
- `currentSrc=""`, `loading="lazy"`, `complete=false`, `naturalWidth=0`, `naturalHeight=0`.
- Bounds after scrolling: x=23, y=366.625, width=344, height=198; no hidden ancestor; within the viewport.
- Pending image request: `/_next/image?url=%2Fmedia%2Fatreia.jpg&w=384&q=75`.

No-clock and resumed-clock comparisons also failed, as did changing the image to `loading="eager"` in the temporary browser DOM. The first three mode durations were 6.819s, 6.682s, and 6.982s. A separate persisted no-clock rerun failed in 6.714s. Temporary mode script/report: `.qa/keyword-refresh-home-image-mode-diag.mjs` and `.qa/keyword-refresh-home-image-mode-diag.json` (the persisted report contains that no-clock rerun).

## HTTP format comparison

Direct HTTP probes to the same width-384 optimization URL, against the same process:

| Accept header | Result |
| --- | --- |
| Default PowerShell request / general image acceptance | 200; `image/jpeg`; 10,014 bytes; 130ms |
| `image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8` | Timed out after 10,120ms |
| `image/webp,image/*,*/*;q=0.8` | Timed out after 10,098ms |

Root independently found the same JPEG-versus-WebP response difference for width 384 and width 750. The browser's stalled request therefore correlates with the optimized format response path, rather than being explained by a hidden image or a fake clock alone.

## Native Sharp probe

Temporary script/report: `.qa/keyword-refresh-sharp-image-probe.mjs` and `.qa/keyword-refresh-sharp-image-probe.json`. The source was read and encoded into memory only; no source asset was edited.

`public/media/atreia.jpg` metadata: JPEG, 1920×1080, sRGB, three channels, no alpha.

| Operation | Result |
| --- | --- |
| Metadata | 7ms |
| Resize 384 and WebP quality 75 | 23ms; 7,724 bytes |
| Resize 750 and WebP quality 75 | 47ms; 19,724 bytes |
| Resize 384 and JPEG quality 75 | 17ms; 11,749 bytes |

The standalone Sharp encoder works. The diagnosis has not established the exact cause within the running Next optimization/cache/request path. The fresh-process check below separates the old process state from an asset or encoder failure.

## Verified fallback candidate

Temporary script/report: `.qa/keyword-refresh-home-raw-image-diag.mjs` and `.qa/keyword-refresh-home-raw-image-diag.json`.

In the temporary browser DOM only, the about image's `srcset`/`sizes` were removed and its `src` set to `/media/atreia.jpg`, simulating an `unoptimized` Next image. The original clock, home `networkidle`, scrolling, image visibility, and **every-document-image completion** assertion remained. Both desktop and mobile passed, including full-page and fold screenshots, in 2.198s and 1.961s.

This was a verified narrow fallback candidate if the optimized response issue persisted: serve the existing about image as its original JPEG while retaining the image readiness assertion. It increases transferred image bytes relative to resized WebP. The fresh-process check passed, so this candidate was not needed and was not applied to product code. Skipping the visible image or deleting the image completion assertion is not supported by the evidence.

## Fresh process confirmation

Root started the same final build in a new Next process at `http://127.0.0.1:3032`. The previously failing optimized WebP requests at width 384 and 750 both returned 200, with 7,724 and 19,724 bytes, in approximately 0.172s.

The original, unmodified-image tail reproduction was then rerun with `QA_BASE_URL=http://127.0.0.1:3032`. Both desktop and mobile passed the original every-document-image completion predicate and produced full-page/fold screenshots. The fake clock was installed at the same October 2 time; no image DOM properties were changed. There were no unloaded images in either result.

Fresh report: `.qa/keyword-refresh-home-image-diag-fresh-3032.json`. The shared latest report `.qa/keyword-refresh-home-image-diag.json` now also contains the fresh 3032 run; the original 3031 image-state evidence is retained in the earlier sections of this log and the no-clock 3031 mode report.

Conclusion: the old process exhibited an image-optimization response problem consistent with stale inflight/cache state; restarting restored the optimized responses and the screenshot helper. This does not establish a permanent framework defect or the exact trigger. No product image-loading change or removal of the all-image readiness assertion is justified by the completed fresh-process check. Root will run the complete acceptance suite on 3032.
