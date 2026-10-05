# 共享修改独立只读复核

日期：2026-10-04。结论：**PASS，没有发现需修正的问题。** 本轮没有修改共享源码、消息、规则或其它页面，只新增本记录。

## 已复核范围

与本轮 `before/` 比对并读取当前上下文：

- `src/components/article-page.tsx`
- `src/components/site-shell.tsx`
- `src/components/home-sections.tsx`
- `src/components/tools/item-details.tsx`
- `src/i18n/tool-messages.ts`
- `src/i18n/guide-messages.ts`
- `src/messages/{en,ja,es,de}.json`
- `src/app/[locale]/tools/character/page.tsx`
- `src/app/api/share/[locale]/[slug]/route.tsx`
- `src/lib/share-images.ts`
- `AGENTS.md`

额外只读读取 `src/i18n/messages.ts`、`home.en.json`、工具地区类型、角色工具选择器及 article-data 的 edition 值，用来确认浅合并和显示条件的实际影响。

## 结论依据

1. **默认徽标已去除，非默认范围保持。** article-page 和分享卡都只省略缺省 edition / 精确 `Global`。当前 TW、KR/TW 文章的明确 edition 仍会显示；代码也保留其它非 Global 的明确对比字符串。site-shell 顶部默认 edition、首页 CTA 的 GLOBAL 和角色工具硬编码 Global 已删，其它入口不变。
2. **英文继承完整。** `messages.ts` 的 `{...source, ...en}` 为顶层浅合并。新增 en.footer 的 9 个字段、en.metadata 的 3 个字段与 `home.en.json` 完整对应，所有值非空；footer.about 与 metadata.description 已采用去冗版本，不会被旧源对象里的 Global 文案重新补回。home 对象自身也已改写。四语有效消息的链接 URL 均与合并后的旧值一致。
3. **四语自然且一致。** 手工检查首页标题/介绍/统计、footer、metadata、角色工具简介、装备例子、八职业图标说明及新增规则。去除限定后没有留下缺介词、空标点或指代不明的句子。JSON 和 TS 文本没有发现编码损坏。
4. **真实地区条件未删。** 角色工具仍按 `nae/naw/eu/la/as` 选择地区，当前 region/server 联动逻辑未变。DataUpdated 保留实际地区、读取时间和 UTC，仅删除前面的固定 Global；snapshot 隐藏条件原样。数据类型仍限制服务为 Global，文案简化没有扩大到 KR/TW 查询。
5. **功能路径不变。** 导航、角色参数解析、服务器选项、数据调用、分享图片选图/尺寸/字体/404 行为均未变。分享图哈希增加固定版本前缀 `2:`，保持 URL 结构和 12 位摘要长度，使新版卡面得到新缓存地址。删除的 `ui.edition` 和 `ui.globalNotice` 没有剩余 TS/TSX 引用。

## 必要保留项

- 四语有效消息剩余的公开 Global 字符串仅在 `/topics/global-changes` 的真实地区比较主题名称；它不作为普通页面版本徽标。此处属于本轮规则明确允许的地区对比。
- metadata.keywords 内的原 Global 关键词保持不变，符合本轮禁止改关键词的范围；title、description 与普通公开介绍均已去冗。
- AGENTS 新规则说明默认服务，同时要求保留 KR/TW 专属内容、真实比较、地区选择、统计与兼容性限制，并禁止将区域服内容改写成默认事实；与用户要求一致。

## 检查方式

人工逐项审查统一 diff 和运行上下文；只读 Python 验证四语有效 home/footer/metadata/ui 的键、继承覆盖、URL、keywords、编码和服区残留。对 undefined、Global、KR/TW 与明确比较 edition 的分支逐项核对，并扫描已删除 UI keys 的引用。所有检查通过。

这是源码和文案的独立复核，没有运行构建或浏览器验收；根代理负责最终运行验证。
