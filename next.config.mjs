import createMDX from '@next/mdx';
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./src/i18n/request.ts');
const withMDX = createMDX({options: {remarkPlugins: ['remark-gfm']}});

export default withNextIntl(withMDX({
  distDir: process.env.NEXT_DIST_DIR || '.next',
  outputFileTracingIncludes: {
    '/api/share/*': ['./public/media/guides/**/*', './public/fonts/*'],
  },
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'mdx'],
  poweredByHeader: false,
  devIndicators: false,
  agentRules: false,
}));
