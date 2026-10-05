'use client';

import Script from 'next/script';
import {useEffect, useSyncExternalStore} from 'react';
import {analyticsAllowed} from './site-analytics';

const measurementId = 'G-SHV8K5DLSK';

function setDisabled(disabled: boolean) {
  Reflect.set(window, `ga-disable-${measurementId}`, disabled);
}

function subscribe(callback: () => void) {
  const changed = () => {setDisabled(!analyticsAllowed()); callback();};
  window.addEventListener('storage', changed);
  window.addEventListener('aion2-analytics-preference', changed);
  return () => {
    window.removeEventListener('storage', changed);
    window.removeEventListener('aion2-analytics-preference', changed);
  };
}

export function GoogleAnalytics() {
  const allowed = useSyncExternalStore(subscribe, analyticsAllowed, () => false);
  useEffect(() => {setDisabled(!allowed);}, [allowed]);

  if (!allowed) return null;
  // GA4 enhanced measurement handles browser-history pageviews; do not send duplicates here.
  return <>
    <Script id="google-analytics-init" strategy="afterInteractive">{`
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '${measurementId}');
    `}</Script>
    <Script id="google-analytics-script" src={`https://www.googletagmanager.com/gtag/js?id=${measurementId}`} strategy="afterInteractive" />
  </>;
}
