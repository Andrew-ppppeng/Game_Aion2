"""Build an auditable index from manually reviewed observations, not keyword inference."""
from pathlib import Path
import csv, json

ROOT = Path(__file__).resolve().parent
review = {
 '1wzxot9': ('progression', '45级完成任务后仍不能采集深渊羽毛，缺少解锁条件排查。', '/leveling; /map'),
 '1wzxoeo': ('progression', '制作装备是否能继承到下一档，担心现在投入以后重做。', '/leveling; /monetization'),
 '1wzxjf3': ('group-content', '满级后不知道哪些活动能与朋友组队，并把高装备分归因于付费。', '/guide; /leveling'),
 '1wzxgri': ('settings-performance', '5070用户询问是否能关闭放大器；已试配置修改仍有颗粒感。', '/download; /guide'),
 '1wzxgl2': ('group-content', '征服副本队友不了解石化救援，导致反复失败及复活成本。机制尚需独立核验。', '/builds; /guide'),
 '1wzxbs8': ('progression', '火神殿武器保底究竟要多少次；评论对双倍领取、能量和次数口径混淆。', '/leveling'),
 '1wzx9to': ('settings-performance', '建议关闭攻击时设置主目标；与10月4日热门设置帖建议开启相冲突。', '/guide'),
 '1wzwnxm': ('settings-performance', '守护星高亮目标后技能仍攻击旧目标，询问选敌设置；帖内视频未独立播放核验。', '/guide'),
 '1wzwfmf': ('settings-performance', '5080用户报告扫描线与阴影颗粒感，寻求设置修复。', '/download'),
 '1wzw9bo': ('payment-claims', '10月7日玩家提醒创始者外观已经能供小号领取。规则另以官方补丁核验。', '/monetization'),
 '1wzw66r': ('payment-claims', '质疑订阅与其他付费叠加，想知道订阅实际价值。', '/monetization'),
 '1wzvcdm': ('outage-troubleshooting', '更新后两种货币余额变成相同数值；这是玩家报告，原因未知。', '/maintenance; /monetization'),
 '1wzv8ku': ('outage-troubleshooting', 'Azphel玩家无法移动后不能重新连接；不能据此确定官方宕机。', '/maintenance; /download'),
 '1wzv1um': ('settings-performance', '9070 XT用户报告画面模糊。', '/download'),
 '1wzurdi': ('payment-claims', '围绕市场会员门槛展开讨论。', '/monetization'),
 '1wzupnk': ('outage-troubleshooting', '牧师仅副本内技能延迟，延迟显示仍绿色，普通网络教程无法解释。', '/download'),
 '1wzuiok': ('outage-troubleshooting', '市场售出并结算后未收到Kina，重新登录无效。', '/maintenance; /monetization'),
 '1wzu55z': ('presets', '寻找可按参考图制作角色预设的人，单个玩家表达付费意愿。', '/presets'),
 '1wzu015': ('payment-claims', '不确定Twitch掉宝是否绑定单一角色，因此暂不领取。', '/twitch-drops'),
 '1wztv10': ('account-policy', '担心长期不登录会删除角色；帖子把可能处理说成自动处理，官方全文未核验。', '/steam'),
 '1wztsx2': ('server-selection', '希望找到主要使用英语的欧洲服务器，准备转服。', '/server; /server-transfer'),
 '1wztkzt': ('payment-claims', '创始者礼包只能看到称号，找不到武器箱，询问领取范围与步骤。', '/monetization'),
 '1wztko8': ('pvp-balance', '近战玩家抱怨战场远程爆发及平衡。站点不能解决数值平衡。', '/builds'),
 '1wztamd': ('pvp-balance', '欧洲服玩家抱怨深渊阵营压制，影响任务和羽毛采集。', '/server; /map'),
 '1wztakg': ('settings-performance', '9070 XT和14600KF用户报告城内40至45帧及卡顿。', '/download'),
 '1wzt8bf': ('payment-claims', '订阅与不订阅的朋友进度差距扩大，具体次数与购买限制未独立核实。', '/monetization; /leveling'),
 '1wzt690': ('settings-performance', '6800 XT用户报告画面质量差。', '/download'),
 '1wzt355': ('progression', '询问是否值得买全所有命令类条目，体现资源分配需求。', '/leveling'),
 '1wxfhbm': ('settings-performance', '详细设置说明获较高互动；评论补充姓名板与体力显示关系，部分建议存在场景差异。', '/guide; /download'),
 '1wvyubw': ('presets', '巫师角色滑条分享获较高互动，评论希望更方便地下载和套用。', '/presets'),
}

records = []
with (ROOT / 'reddit-browser-observation.tsv').open(encoding='utf-8') as f:
 for row in csv.DictReader(f, delimiter='\t'):
  post_id = row['permalink'].split('/')[4]
  reviewed = review.get(post_id)
  records.append(dict(id='R-' + post_id, platform='Reddit', url='https://www.reddit.com' + row['permalink'], title=row['title'], posted_at=row['created_at_utc'], date_confidence='exact DOM timestamp; seconds precision', region='Global discussion context; user testimony', version='October 2026 launch; exact client build unspecified', access='visible post text; selected threads also have comment extracts' if reviewed else 'screening index only', theme=reviewed[0] if reviewed else 'not-used-in-analysis', player_need=reviewed[1] if reviewed else 'Excluded from thematic conclusions: meme, promotion, ambiguous or insufficiently reviewed.', site_pages=reviewed[2] if reviewed else '', raw_files=['reddit-browser-observation.tsv'], score_snapshot=int(row['score']), comment_count_snapshot=int(row['comments']), fact_status='Demand evidence; not confirmation of mechanics'))

# Dates labelled search-derived are weaker than DOM or original HTML timestamps.
extra = [
 ('R-roadmap','Reddit','https://www.reddit.com/r/Aion2/comments/1wvue3p/roadmap_fresh_45/','Roadmap fresh 45','2026-10-02; search-derived date','Global','progression','满级路线、装备门槛、能量花费、旧装备和符文处置引发连续追问。','/leveling','raw/web-08-reddit-week-sampling.json'),
 ('R-newguide','Reddit','https://www.reddit.com/r/Aion2/comments/1wy4oib/best_new_player_guideeverything_i_learned_from/','New player guide discussion','2026-10-05; October 6 comments; search-derived dates','Global','progression','玩家追问换主号、旧装备、货币、PVP装备、额外奖励次数；攻略正文不等于机制已核实。','/leveling; /guide','raw/web-05-deep-read-progression-market.json'),
 ('R-marketdata','Reddit','https://www.reddit.com/r/Aion2/comments/1wyrc6m/aion_2_market_data/','AION 2 market data','2026-10-06; search-derived date','Global, project coverage unverified','market-tool','评论明确要求不限数量收藏夹，在一页查看多个物品价格。仅一个明确功能请求。','existing budget planner','raw/web-05-deep-read-progression-market.json'),
 ('R-patch','Reddit','https://www.reddit.com/r/Aion2/comments/1wzs3qz/aion_2_global_october_7_maintenance_patch_notes/','October 7 maintenance discussion','2026-10-07; date in post title/search','Global','payment-claims','创始者外观如何补领、小号领取、缺失箱子仍引发困惑。','/monetization; /maintenance','raw/web-09-deep-read-steam-feedback.json'),
 ('R-patch2','Reddit','https://www.reddit.com/r/Aion2/comments/1wzpkt7/notice_patch_notes_oct_6_pdt_oct_7_cest/','October 6 PDT / October 7 CEST patch','2026-10-07; title/search date','Global','patch-actions','玩家关注订阅范围、皮革掉落、翅膀转换限额；需求应转成更新后可做的操作。','/maintenance; /monetization','raw/web-10-official-patch-builds.json'),
 ('R-buildgap','Reddit','https://www.reddit.com/r/Aion2/comments/1wzr5ux/understanding_global_class_imbalance/','Understanding class imbalance','2026-10-07; search-derived date','Global vs KR/TW comparisons','builds','旧赛季攻略难套当前装备阶段；职业效率百分比属于玩家主张，不能写入事实。','/builds; eight class guides','raw/web-10-official-patch-builds.json'),
 ('R-sorc','Reddit','https://www.reddit.com/r/Aion2/comments/1wyumod/my_aion_2_sorceror_build/','Sorcerer build','2026-10-06; search-derived date','Global','builds','想知道技能、被动、加护盘如何分配，并混淆不同付费产品。','/builds; /sorcerer','raw/web-06-steam-errors-week-search.json'),
 ('R-disconnect','Reddit','https://www.reddit.com/r/Aion2/comments/1wz6pd2/game_keeps_disconnecting_after_working_fine_for_a/','Repeated disconnects','2026-10-06; search-derived date','Global','outage-troubleshooting','此前可以游玩，随后反复断开连接。','/download; /maintenance','raw/web-06-steam-errors-week-search.json'),
 ('R-europe','Reddit','https://www.reddit.com/r/Aion2/comments/1wz59e0/unable_to_join_the_game_on_europe_servers/','Cannot join Europe servers','2026-10-06; search-derived date','Global / Europe','outage-troubleshooting','角色选择后断开连接，需要按错误阶段诊断。','/download; /maintenance','raw/web-08-reddit-week-sampling.json'),
 ('R-restart','Reddit','https://www.reddit.com/r/Aion2/comments/1wzgecs/should_i_restart_on_a_global_server/','Restart or transfer','2026-10-06; search-derived date','Global / Advanced Access pools','server-selection','是否要重练以及奖励、原服务器和转服池限制。','/server-transfer','raw/web-06-steam-errors-week-search.json'),
 ('R-cosmetics','Reddit','https://www.reddit.com/r/Aion2/comments/1wz0591/cosmetics_from_an_f2p_perspective_can_you_unlock/','F2P cosmetics','2026-10-06; search-derived date','Global','presets','想知道哪些外观可以通过游玩获得。','/presets; /monetization','raw/web-03-focused-search.json'),
 ('R-appearancecost','Reddit','https://www.reddit.com/r/Aion2/comments/1wzc6wv/could_we_skip_the_part_where_the_player_base/','Appearance change costs','2026-10-06; search-derived date','Global','presets','对发型、化妆、染色等付费修改成本不满，需解释预览与实际应用区别。','/character-creation; /presets','raw/web-03-focused-search.json'),
 ('R-sitefeedback','Reddit','https://www.reddit.com/r/Aion2/comments/1wwb561/created_a_website_for_aion_2_would_appreciate/','Player feedback on another guide site','2026-10-03; October 6 reply; search-derived dates','Global','guide-format','一条反馈嫌文字太多，更想要装备搭配或计算器；不能据此判断全体玩家偏好。','/builds; existing tools','raw/web-09-deep-read-steam-feedback.json'),
 ('R-airoadmap','Reddit','https://www.reddit.com/r/Aion2/comments/1wvl2ix/removed/','Removed roadmap: surviving comments','2026-10-02; search-derived date','Global','guide-format','评论批评AI路线和错误图标；原帖已删除，未恢复正文。','/leveling; /guide','raw/web-08-reddit-week-sampling.json'),
 ('S-dxgi','Steam Community','https://steamcommunity.com/app/3393110/discussions/6/583935635494139006/','DXGI_ERROR_INVALID_CALL','Parent 2026-09-30; visible replies October 1–2; later relative reply unanchored','Global / Steam','outage-troubleshooting','玩家报告启动错误，部分以刷新率变更恢复；不能保证通用有效。','/download','raw/web-09-deep-read-steam-feedback.json'),
 ('S-subscope','Steam Community','https://steamcommunity.com/app/3393110/discussions/6/583935635494124713/','Subscription scope','Parent 2026-09-30; visible replies October 1','Global / Steam','payment-claims','账号、服务器、角色三种付费范围混淆；只读取可见首页，87条累计评论不等于全已读。','/monetization','raw/web-12-settings-presets-account.json'),
 ('S-subtier','Steam Community','https://steamcommunity.com/app/3393110/discussions/6/583935635494153349/','Included membership tier','2026-10-01; Steam displayed date','Global / Steam','payment-claims','礼包包含基础还是高级会员、会员与通行证是否同类。','/monetization','raw/web-12-settings-presets-account.json'),
 ('K-abyss','Inven','https://www.inven.co.kr/board/aion2/6388/280426','Abyss performance','2026-10-07 23:08 KST; original HTML','KR','settings-performance','优化更新后仍在深渊技能延迟；只能作KR补充信号。','/download','raw/inven-abyss-optimization.html'),
 ('K-amd','Inven','https://www.inven.co.kr/board/aion2/6388/280418','AMD driver warning','2026-10-07 21:35 KST; original HTML','KR','settings-performance','更新AMD驱动后客户端仍提示更新。','/download','raw/inven-amd-prompt.html'),
 ('K-return','Inven','https://www.inven.co.kr/board/aion2/6388/280412','Returning player','2026-10-07 20:49 KST; original HTML','KR','progression','半年后回归询问追赶、通行证和公会；生命周期不同于刚开服Global。','/leveling','raw/inven-returning-player.html'),
 ('K-event','Inven','https://www.inven.co.kr/board/aion2/6388/280398','Artifact time','2026-10-07 19:26 KST; original HTML','KR','timers','询问活动时间；不移植KR时间表到Global。','existing event timers','raw/inven-artifact-time.html'),
 ('K-global','Inven','https://www.inven.co.kr/board/aion2/6388/280362','KR player tries Global','2026-10-07 17:01 KST; original HTML','KR poster, Global experience','progression','重做探索、资源与装备成长负担；老服玩家视角可能偏向效率。','/leveling','raw/inven-global-experience.html'),
 ('B-bundle','Bahamut','https://forum.gamer.com.tw/C.php?bsn=82913&snA=6260','Paid bundle confusion','October 6–7 relative displays at October 7 capture; local board context','TW/KR context from comments; exact server unspecified','payment-claims','重复礼包外观与客服回复冲突，玩家对购买前说明缺乏信任；不采纳诈骗或退款规则指控，不移植其规则到Global。','/monetization','raw/bahamut-paid-bundle-confusion.html'),
 ('B-assassin','Bahamut','https://forum.gamer.com.tw/C.php?bsn=82913&snA=6253','Assassin DPS question','2026-10-04 05:43 edit time; original HTML','TW / KR-TW build context','builds','刺客伤害与护法比较，询问装备和技能；不能推导Global职业排行。','/builds; /assassin','raw/bahamut-assassin-dps.html'),
 ('B-sorc','Bahamut','https://forum.gamer.com.tw/C.php?bsn=82913&snA=6252','Sorcerer PvP/PvE allocation','2026-10-02 07:31:05 CST; original HTML','TW','builds','新手搜到旧加护盘，想要当前PVE及PVP点法。','/builds; /sorcerer','raw/bahamut-sorcerer-board.html'),
]
for ident, platform, url, title, date, region, theme, need, pages, raw in extra:
 records.append(dict(id=ident, platform=platform, url=url, title=title, posted_at=date, date_confidence='See posted_at: search-derived / relative dates are not exact timestamps', region=region, version='October 2026 discussion; exact client build unspecified', access='readable thread/body/comment excerpt; pagination not exhaustively read', theme=theme, player_need=need, site_pages=pages, raw_files=[raw], fact_status='Demand evidence; not confirmation of mechanics'))

for record in records:
 if record['id'] in {'R-sorc','R-disconnect','R-restart','R-cosmetics','R-appearancecost'}:
  record['access'] = 'search excerpt only; lower confidence than full thread'

(ROOT / 'evidence.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
fields = ['id','platform','url','title','posted_at','date_confidence','region','version','access','theme','player_need','site_pages','raw_files','fact_status']
with (ROOT / 'evidence.csv').open('w', encoding='utf-8-sig', newline='') as f:
 writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
 writer.writeheader()
 for record in records:
  writer.writerow({**record, 'raw_files': '; '.join(record['raw_files'])})
print(json.dumps({'indexed_records':len(records), 'used_as_demand_evidence':sum(r['theme']!='not-used-in-analysis' for r in records), 'screening_only':sum(r['theme']=='not-used-in-analysis' for r in records)}, ensure_ascii=False))
