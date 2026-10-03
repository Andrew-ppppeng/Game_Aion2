import type {MDXComponents} from 'mdx/types';
import type {ComponentProps} from 'react';
import {Link} from '@/i18n/navigation';
import {GuideTable} from '@/components/guide-table';

function ContentLink({href = '', children, ...props}: ComponentProps<'a'>) {
  if (href.startsWith('/') && !href.startsWith('//')) return <Link href={href} {...props}>{children}</Link>;
  if (/^https?:\/\//.test(href)) return <a href={href} {...props} target="_blank" rel="noopener noreferrer">{children}</a>;
  return <a href={href} {...props}>{children}</a>;
}

const components: MDXComponents = {
  a: ContentLink,
  table: GuideTable,
};

export function useMDXComponents(): MDXComponents {
  return components;
}
