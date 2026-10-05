# AION 2 Twitch Drops review implementation

- Review date: 2026-10-04. Region: Global. Notice last updated 2026-10-02, not a new game patch.
- Rechecked official source: https://aion2.plaync.com/en-us/board/notice/view?articleId=6ab30633fa7da41c727d632c
- Public official API: https://api-global-community.plaync.com/aion2_global/board/notice_en/article/6ab30633fa7da41c727d632c
- New raw response: `war-for-atreia-review.json`. Earlier research and original sources retained.
- The article body limits these rewards to participating War For Atreia creators listed at https://www.warforatreia.com/ . It states that a point threshold unlocks the upcoming campaign for all 60 creators. No numeric point threshold or currently achieved unlock state is supplied in the checked body.
- First period: October 2, 12:00 PDT / 21:00 CEST through October 4, 23:59 PDT / October 5, 08:59 CEST. UTC conversion: 2026-10-02T19:00:00Z through 2026-10-05T06:59:00Z.
- Second period announced October 7-9; third October 12-14. Precise hours remain unannounced. Dates do not establish that the required threshold has been reached.
- Copied factual reward identities and quantities into three separate localized tables. The first period uses Appearance Change Voucher; the second uses Customization Voucher. Kept the official distinction and Bound labels.
- Regular Advanced Access and Global-launch Drops retain their separate existing reward tables and unspecified cutoff-hour limit. Moved GuideTimers into the War For Atreia section, with explicit campaign scope.
- Added source metadata and the `war-for-atreia` section consistently across English, Japanese, Spanish and German.
