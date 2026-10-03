'use client';

import Image from 'next/image';
import {useEffect, useRef, useState} from 'react';
import {Expand, X} from 'lucide-react';
import type {Locale} from '@/i18n/routing';
import {guideMessages} from '@/i18n/guide-messages';

export function GuideImage({src, alt, width, height, locale, portrait = false}: {
  src: string; alt: string; width: number; height: number; locale: Locale; portrait?: boolean;
}) {
  const [open, setOpen] = useState(false);
  const dialog = useRef<HTMLDialogElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);
  const m = guideMessages[locale];
  useEffect(() => {
    if (!open) return;
    const previous = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    dialog.current?.showModal();
    return () => {document.body.style.overflow = previous;};
  }, [open]);
  function close() {
    dialog.current?.close();
    setOpen(false);
    trigger.current?.focus();
  }
  return <>
    <button ref={trigger} type="button" className={`guide-image-button${portrait ? ' portrait' : ''}`} aria-label={`${m.enlarge}: ${alt}`} aria-haspopup="dialog" onClick={() => setOpen(true)}>
      <Image src={src} width={width} height={height} alt={alt} sizes={portrait ? '(max-width: 639px) 45vw, 230px' : '(max-width: 639px) 100vw, (max-width: 1100px) 80vw, 800px'} />
      <span className="guide-image-zoom"><Expand size={16} aria-hidden="true" /><span>{m.enlarge}</span></span>
    </button>
    {open && <dialog ref={dialog} className="guide-image-dialog" aria-label={alt} onCancel={close} onClose={() => {setOpen(false); trigger.current?.focus();}} onClick={(event) => {if (event.target === event.currentTarget) close();}} onKeyDown={(event) => {
      if (event.key !== 'Tab') return;
      const buttons = event.currentTarget.querySelectorAll<HTMLButtonElement>('button:not([disabled])');
      const first = buttons[0];
      const last = buttons[buttons.length - 1];
      if (event.shiftKey && document.activeElement === first) {event.preventDefault(); last?.focus();}
      else if (!event.shiftKey && document.activeElement === last) {event.preventDefault(); first?.focus();}
    }}>
      <button type="button" className="guide-image-close" autoFocus onClick={close} aria-label={m.close}><X size={22} aria-hidden="true" /></button>
      <div className="guide-image-expanded"><Image src={src} width={width} height={height} alt={alt} unoptimized /><p>{alt}</p></div>
    </dialog>}
  </>;
}
