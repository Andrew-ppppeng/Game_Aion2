'use client';

import {useEffect, useRef, useState, useSyncExternalStore} from 'react';
import {Check, Copy, ExternalLink, Gift} from 'lucide-react';
import {useLocale, useTranslations} from 'next-intl';
import {Link} from '@/i18n/navigation';
import {couponAnnouncement, coupons, getCouponStatus} from '@/lib/coupons';

function subscribeClock(onChange: () => void) {
  const interval = window.setInterval(onChange, 30_000);
  window.addEventListener('focus', onChange);
  return () => {
    window.clearInterval(interval);
    window.removeEventListener('focus', onChange);
  };
}

export function CouponCard() {
  const t = useTranslations('ui');
  const locale = useLocale();
  const status = useSyncExternalStore(subscribeClock, () => getCouponStatus(Date.now()), () => 'announced');
  const [copyState, setCopyState] = useState<'idle' | 'copied' | 'failed'>('idle');
  const resetTimer = useRef<ReturnType<typeof setTimeout> | undefined>(undefined);
  useEffect(() => () => clearTimeout(resetTimer.current), []);

  if (coupons.length === 0) return null;
  const code = coupons[0];
  const expires = new Intl.DateTimeFormat(locale, {
    month: 'short', day: 'numeric', year: 'numeric', hour: '2-digit', minute: '2-digit', timeZone: 'UTC',
  }).format(new Date(couponAnnouncement.expiresAt));

  async function copyCode() {
    clearTimeout(resetTimer.current);
    try {
      await navigator.clipboard.writeText(code);
      setCopyState('copied');
      resetTimer.current = setTimeout(() => setCopyState('idle'), 2500);
    } catch {
      setCopyState('failed');
    }
  }

  return (
    <section className="coupon-card" aria-label={t('couponEyebrow')}>
      <div className="coupon-heading">
        <span><Gift size={14} aria-hidden="true" />{t('couponEyebrow')}</span>
        <span className={`coupon-state ${status}`}>{t(status === 'expired' ? 'couponExpired' : 'couponAvailable')}</span>
      </div>
      <div className="coupon-code-row">
        <code>{code}</code>
        <button type="button" onClick={copyCode} aria-label={copyState === 'copied' ? t('copied') : t('copyCode')}>
          {copyState === 'copied' ? <Check size={15} /> : <Copy size={15} />}
        </button>
      </div>
      <span className="sr-only" role="status">{copyState === 'copied' ? t('copied') : ''}</span>
      {copyState === 'failed' && <p className="copy-error" role="alert">{t('copyFailed')}</p>}
      <p className="coupon-expiry">{t('expires')}: <time dateTime={couponAnnouncement.expiresAt}>{expires} UTC</time></p>
      <div className="coupon-bottom">
        <Link href="/code">{t('viewCodes')} <ExternalLink size={11} aria-hidden="true" /></Link>
      </div>
    </section>
  );
}
