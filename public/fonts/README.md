# Social preview font

`aion2-share-ja.woff` is a weight-600 subset of Noto Sans JP from the
[Google Fonts repository](https://github.com/google/fonts/tree/main/ofl/notosansjp),
covered by the accompanying SIL Open Font License.

It includes the Japanese article titles, navigation labels and tool strings. It
is used only by the server-generated social card, so article readers download
no additional font and preview rendering makes no external font request.

After adding Japanese titles or labels, run `python scripts/update-share-font.py`
with `fontTools` installed. The script downloads the original font and license
and recreates the local subset. Generated 2026-10-04.
