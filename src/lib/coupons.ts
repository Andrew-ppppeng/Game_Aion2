import homepage from '../../home.en.json';

// Global announcement window. Not a claim of successful in-game redemption.
export const couponAnnouncement = {
  expiresAt: '2026-10-14T06:00:00Z',
  source: 'https://aion2.plaync.com/en-us/board/notice/view?articleId=6abd5fe5fa7da41c727d63c6',
  region: 'Global',
  checkedAt: '2026-10-02',
};

export const coupons = homepage.sidebarCodes.filter((code) => /^[A-Z0-9]+$/.test(code));

export function getCouponStatus(now: number): 'announced' | 'expired' {
  if (now >= Date.parse(couponAnnouncement.expiresAt)) return 'expired';
  return 'announced';
}
