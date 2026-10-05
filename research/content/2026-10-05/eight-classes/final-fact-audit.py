import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
locales=['en','ja','es','de']
skills=json.loads((ROOT/'src/content/class-skills.json').read_text(encoding='utf8'))
p=ROOT/'src/content/class-skill-focus.json';focus=json.loads(p.read_text(encoding='utf8'))
notes={
'Defiance':[
'Removes Stun, Knockdown, Airborne, Grab, Frost and Fear, then grants status immunity for 5s. Cooldown reduction does not affect it; keep this control break manual.',
'スタン、転倒、空中拘束、つかみ、凍結、恐怖を解除し、5秒の状態異常免疫を得ます。再使用短縮の影響は受けません。独立操作にします。',
'Elimina aturdimiento, derribo, elevación, agarre, congelación y miedo; da inmunidad a estados durante 5s. No recibe reducción de recarga. Mantén control manual.',
'Entfernt Betäubung, Niederschlag, Luftbindung, Griff, Frost und Furcht, danach 5s Statusimmunität. Abklingverkürzung wirkt nicht; separat bedienen.'],
'Judgment':[
'Follow up within 2s of Shield Smite, Warding Strike or Shield Rush, or within 3s of Doom Shield. Spend this window before activating another trigger.',
'Shield Smite、Warding Strike、Shield Rush後は2秒、Doom Shield後は3秒以内に使用。次の発動スキルの前に追撃します。',
'Úsalo en los 2s tras Shield Smite, Warding Strike o Shield Rush, o 3s tras Doom Shield. Consume la ventana antes de otro disparador.',
'Innerhalb 2s nach Shield Smite, Warding Strike oder Shield Rush, beziehungsweise 3s nach Doom Shield. Vor neuem Auslöser verbrauchen.'],
'Savage Roar':[
'Engraves one Insignia for 10s. Build target stacks before Insignia Explosion; another target does not inherit them.',
'10秒のInsigniaを1層刻みます。対象の層をためてからInsignia Explosion。別の対象に層は移りません。',
'Graba una Insignia durante 10s. Acumula en el objetivo antes de Insignia Explosion; otro objetivo no hereda marcas.',
'Graviert eine Insignia für 10s. Zielstapel vor Insignia Explosion aufbauen; andere Ziele übernehmen sie nicht.'],
'Impactful Crush':[
'Opens Dark Crush for 2s. Use the follow-up within that window before spending another trigger.',
'2秒間Dark Crushを使用可能にします。次の発動スキルの前に追撃を使います。',
'Abre Dark Crush durante 2s. Úsalo en esa ventana antes de gastar otro disparador.',
'Öffnet Dark Crush für 2s. Folgeangriff vor einem weiteren Auslöser nutzen.'],
'Spinning Strike':[
'Grants a critical-damage buff and opens Dark Crush for 2s. Its single-target option suits bosses; its cooldown option creates more trigger windows.',
'クリティカルダメージ強化と2秒のDark Crush発動。単体特化はボス向け、再使用短縮は発動時間を増やします。',
'Mejora daño crítico y abre Dark Crush durante 2s. La opción individual ayuda en jefes; menor recarga abre más ventanas.',
'Gibt kritischen Schadensbuff und öffnet Dark Crush für 2s. Einzelzieloption für Bosse, Abklingoption für häufigere Fenster.']}
for cls,entries in focus.items():
 for entry in entries:
  name=next(x['names']['en'] for x in skills[cls] if x['id']==entry['id'])
  if name in notes:entry['text']=dict(zip(locales,notes[name]))
p.write_text(json.dumps(focus,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Final audit: explicit control breaks, exact trigger windows and Insignia duration.')
