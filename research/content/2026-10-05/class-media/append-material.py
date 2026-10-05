from pathlib import Path
path=Path('关键词素材.md')
addition='''

## 2026-10-05 — 职业与 Builds 图片、视频补充

- 玩家任务：识别真实技能图标；看到触发条件与后续技能；区分基础触发、需选择的特化、恢复和手动应对；观察职业攻击与移动；手机可读并可保存高清图。
- 官方八职业视频入口：https://aion2.plaync.com/en-us/about/index 。在官方 JS 1.0.0 中逐职业定位视频 ID；八条 YouTube oEmbed 均显示 AION 2 Official。已保存可用字幕与精确时间点；字幕仅为少量角色语音或不可用，不用于推断技能机制。
- 完整来源、日期、地区、版本与截图检索限制：`research/content/2026-10-05/class-media/RESEARCH.md`。原始 HTML、JS、视频元数据、字幕、缩略图及首次失败记录均保留。
- 未找到适合默认版本的可用完整官方技能树截图。KR 指南接口与 NCER 页面不作为默认服技能树。自行制作的是技能关系图，以已核实的 Global 客户端 1.0.21.0 机制表达条件，不伪装官方界面，也不编造最优加点。
- Gladiator：Keen Strike → Ruinous Blow 的已选 Lv12 冷却特化；Knockdown → Overhead Slam；Stagger → Sword Aura Rampage。
- Templar：Shield Smite/Warding Strike → 2秒 Judgment；Pummel → Punishment 的已选 Lv12 冷却特化；Block → Debilitating Smash。
- Assassin：目标 Insignia → Insignia Explosion；Critical → Heart Gore；Quick Slice → Insignia Explosion 的已选 Lv12 冷却特化。
- Ranger：Marking Shot 的 Precision → Suppressing Arrow/Deadshot；Slow/Root → Burst Arrow；Critical → Drill Dart，并保留其自身暴击回 MP 条件。
- Chanter：Impactful Crush/Spinning Strike → 2秒 Dark Crush；Onslaught → Spinning Strike 的已选 Lv12 特化；Parry → Heat Wave Blow。
- Cleric：Chain of Torment → Condemnation；Condemnation 自身暴击 + 已选 Lv12 重置；队伍受伤/可解除减益 → Radiant Recovery 手动应对。
- Sorcerer：Flame Arrow + Fire Mark passive → Blaze；Firestorm → Hellfire 的已选 Lv12 特化；Frost → Frost Burst。
- Spiritmaster：4次精灵技能 → Four Elements/Fusion；召唤/精灵技能 → Dimensional Control 短窗口；Water Spirit 命中 → MP 恢复。
- Builds：可切换八职业图；Hellfire 的技能 Lv8 三选一分支，分别为 +30% skill speed、命中后10秒火伤、移动施法。保留达到门槛后必须选择、同槽不同时生效的限制。
- 资产：280张真实技能图标 + 8张官方视频预览 + 四语32张职业图、4张特化图。图标原始 URL/日期/版本/SHA-256：`src/content/skill-icons.json`；图像导出记录：`src/content/class-diagram-images.json`。
- 页面继续保留完整技能名、等级、原有锚点与详细玩法；研究来源仅存内部，不展示到玩家正文。
'''
with path.open('a',encoding='utf-8') as handle: handle.write(addition)
