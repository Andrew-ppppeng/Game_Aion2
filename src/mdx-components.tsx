import type {MDXComponents} from 'mdx/types';

const components: MDXComponents = {
  table: (props) => <div className="mdx-table-wrap"><table {...props} /></div>,
};

export function useMDXComponents(): MDXComponents {
  return components;
}
