'use client';

import {useRef, useState} from 'react';

type Props = {template: string; label: string; copyLabel: string; copiedLabel: string; selectLabel: string};

export function FeedbackTemplate({template, label, copyLabel, copiedLabel, selectLabel}: Props) {
  const field = useRef<HTMLTextAreaElement>(null);
  const [status, setStatus] = useState('');
  async function copy() {
    try {
      await navigator.clipboard.writeText(template);
      setStatus(copiedLabel);
    } catch {
      field.current?.focus();
      field.current?.select();
      setStatus(selectLabel);
    }
  }
  return <div className="feedback-template">
    <textarea ref={field} aria-label={label} value={template} readOnly rows={7} style={{width: '100%', padding: '14px', font: 'inherit', color: 'inherit', background: 'transparent', border: '1px solid var(--border)', borderRadius: 8}} />
    <button type="button" className="button button-secondary" onClick={copy}>{copyLabel}</button>
    <p role="status">{status}</p>
  </div>;
}
