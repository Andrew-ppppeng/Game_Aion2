import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
LOCALES=['en','ja','es','de']
ids=json.loads((ROOT/'src/content/class-identities.json').read_text(encoding='utf8'))
intro={
'en':'Every class guide below includes active-skill triggers, a complete skill list, early upgrade priorities, Stigma swaps, a manual loop and solo, party and PvP adjustments.',
'ja':'各ガイドは発動条件、全スキル一覧、序盤の強化、スティグマ交換、手動連携、ソロ・パーティー・PvPの調整を扱います。',
'es':'Cada guía incluye condiciones de activación, lista completa de habilidades, mejoras iniciales, cambios de estigmas, ciclo manual y ajustes para solo, party y PvP.',
'de':'Jeder Guide enthält Auslöser, die vollständige Fertigkeitenliste, frühe Verbesserungen, Stigma-Wechsel, einen manuellen Ablauf sowie Solo-, Gruppen- und PvP-Anpassungen.'}
for loc in LOCALES:
 p=ROOT/f'src/content/{loc}/classes.mdx';s=p.read_text(encoding='utf8')
 s=re.sub(r'<h2 id="class-icons">.*?(?=<h2 id="choose-a-role">)', '',s,flags=re.S)
 s=s.replace('<GuideClasses />','<span id="class-icons" />\n\n<GuideClasses />')
 # Link class names in the comparison table to actual detail destinations.
 for entry in ids:
  for name in set([entry['names'][loc],entry['names']['en']]):
   s=s.replace('| '+name+' |','| ['+name+'](/'+entry['id']+') |')
 marker='<h2 id="class-skills-and-gameplay">'
 start=s.index('\n\n',s.index(marker))+2
 end=s.index('\n\n',start)
 links=' · '.join('['+x['names'][loc]+'](/'+x['id']+')' for x in ids)
 s=s[:start]+intro[loc]+'\n\n'+links+'\n\n'+{
 'en':'Use [builds](/builds) to compare the eight starting loops and budget skill points; [Cleric builds](/cleric-build) focuses on healing and damage slot changes.',
 'ja':'[ビルド](/builds)で8職の起手とポイントを比較。[クレリックビルド](/cleric-build)は回復・攻撃枠の交換を詳しく扱います。',
 'es':'[Builds](/builds) compara ocho ciclos y presupuestos; [builds de Clérigo](/cleric-build) detalla cambios de curación y daño.',
 'de':'[Builds](/builds) vergleicht acht Abläufe und Punkte; [Kleriker-Builds](/cleric-build) erklärt Heilungs- und Schadensplätze.'}[loc]+s[end:]
 # A base Cleric cleanse is available without a cleanse specialization.
 s=s.replace('a cleanse-capable skill if unlocked','Radiant Recovery for cleansing')
 p.write_text(s,encoding='utf8')
 mpath=p.with_suffix('.json');m=json.loads(mpath.read_text(encoding='utf8'))
 m['toc']=[{'id':id,'title':title} for id,title in re.findall(r'<h2 id="([a-z0-9-]+)">(.*?)</h2>',s)]
 mpath.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf8')

cleanses={
'en':[
('Select the cleanse option if unlocked','Base skill heals the party and removes one debuff; rank 8 can remove more'),
('Select Radiant Recovery’s cleanse option when unlocked. Keep that control separate from damage so you can remove a harmful effect promptly.','Radiant Recovery heals you and party members within 40m and removes one debuff without a specialization. At rank 8, choose increased cleansing when one removal is insufficient, an extra use for successive recovery, or lower cooldown for frequent casts. Keep it separate from damage.'),
('Whether your selected skill includes the required cleanse','Whether the effect is removable, the ally is within 40m, or several effects need removal'),
('Assuming Radiant Recovery cleanses without the cleanse option','Assuming one cleanse removes every effect, including effects that cannot be removed'),
('a cleanse-capable option','Radiant Recovery'),
('Party damage/protection buff','Light of Protection'),
('Identify party protection by the offense and protection effects it supplies.','Light of Protection’s damage boost does not stack with Chanter Undefeated Mantra; the higher skill level applies, with Mantra taking precedence at equal levels.'),
('Equip resurrection early; improve its casting option as your party needs develop.','Summon Resurrection restores a fallen party member within 40m. Its rank-5 option shortens casting; use a safe window.'),
('Check whether your selected option supports the critical-hit reset','Chain of Torment on target; select the rank-12 critical-hit reset'),
('Select the movement-speed option if available','Use its party healing over time; rank 12 adds movement speed'),
],
'ja':[
('開放済みなら解除設定を選ぶ','基本で味方回復と減益1個解除。ランク8で解除数を強化可能'),
('Radiant Recoveryの解除設定を開放したら選びます。攻撃と別の操作に置き、有害効果へすぐ対応できるようにしましょう。','Radiant Recoveryは基本で本人と40m内の味方を回復し、減益1個を解除します。ランク8では解除数、追加使用、再使用短縮から必要な効果を選びます。攻撃と別操作にします。'),
('選択済みスキルに必要な解除があるか','解除可能か、40m内か、複数効果の解除が必要か'),
('解除設定なしにRadiant Recoveryで解除できると思い込む','解除できない効果や複数効果も1回ですべて消えると考える'),
],
'es':[
('Selecciona disipación si está desbloqueada','Cura y elimina un perjuicio de base; rango 8 puede quitar más'),
('Selecciona la disipación de Radiant Recovery cuando esté desbloqueada. Sepárala del daño para eliminar efectos dañinos rápidamente.','Radiant Recovery cura a ti y a la party a 40m y elimina un perjuicio sin especialización. En rango 8 elige más disipación, uso adicional o menor recarga según la necesidad. Sepárala del daño.'),
('Si la habilidad seleccionada incluye la disipación necesaria','Si el efecto es eliminable, el aliado está a 40m o hay varios efectos'),
('Suponer que Radiant Recovery disipa sin la opción de disipación','Suponer que una disipación elimina todo, incluidos efectos no eliminables'),
],
'de':[
('Freigeschaltete Reinigungsoption auswählen','Heilt und entfernt regulär einen Debuff; Rang 8 kann mehr entfernen'),
('Wähle Radiant Recoverys Reinigung nach der Freischaltung. Halte sie getrennt von Angriffen für schnelle Reaktionen auf schädliche Effekte.','Radiant Recovery heilt dich und Gruppenmitglieder innerhalb 40m und entfernt ohne Spezialisierung einen Debuff. Auf Rang 8 mehr Reinigung, zusätzliche Nutzung oder kürzere Abklingzeit nach Bedarf wählen. Getrennt vom Schaden halten.'),
('Ob die gewählte Fertigkeit die benötigte Reinigung enthält','Ob der Effekt entfernbar ist, das Mitglied innerhalb 40m steht oder mehrere Effekte bestehen'),
('Radiant Recovery ohne Reinigungsoption als Reinigung voraussetzen','Annehmen, dass eine Reinigung alle, auch nicht entfernbare Effekte beseitigt'),
]}
extra={
'en':'''For the complete skill list, use the [Cleric class guide](/cleric). Healing Light heals you and automatically selects the lowest-HP party member within 40m; it does not normally follow your enemy target. Light of Regeneration supplies party healing over time. Keep direct recovery for immediate damage, Radiant Recovery for removable effects, and resurrection for a safe recovery window.

Earth’s Retribution restores MP and its selected rank-12 Discharge effect shortens Bolt. Chain of Torment enables Condemnation; the latter’s rank-12 critical reset only works when its hit is critical. Healing Enhancement converts attack into Heal Boost, so attack contributes to healing as well as damage.''',
'ja':'''全スキルは[クレリック](/cleric)へ。Healing Lightは本人と40m内でHPが最も低い味方を自動回復し、通常は敵ターゲットに従いません。Light of Regenerationは持続回復。即時の被害には直接回復、解除可能な効果にはRadiant Recovery、安全な時間に復活を使います。

Earth’s RetributionはMPと、ランク12のDischarge特化でBolt短縮。Chain of TormentがCondemnationを開き、ランク12のリセットにはクリティカルが必要。Healing Enhancementは攻撃力からHeal Boostを得ます。Light of Protectionの火力はUndefeated Mantraと重複せず、高ランク優先、同ランクはMantraです。''',
'es':'''La lista completa está en [Clérigo](/cleric). Healing Light te cura y elige automáticamente al miembro con menos HP a 40m; normalmente no sigue tu objetivo enemigo. Light of Regeneration aporta curación periódica. Usa curación directa ante daño inmediato, Radiant Recovery ante efectos eliminables y resurrección en una ventana segura.

Earth’s Retribution recupera MP y su opción Discharge de rango 12 reduce Bolt. Chain of Torment abre Condemnation; su reinicio de rango 12 exige un crítico. Healing Enhancement convierte ataque en Heal Boost. Light of Protection no acumula su daño con Undefeated Mantra: gana el rango mayor y Mantra a igualdad.''',
'de':'''Die vollständige Liste steht beim [Kleriker](/cleric). Healing Light heilt dich und automatisch das Gruppenmitglied mit niedrigsten HP innerhalb 40m; normalerweise folgt es nicht deinem Gegnerziel. Light of Regeneration liefert laufende Heilung. Direkte Heilung für sofortigen Schaden, Radiant Recovery für entfernbare Effekte und Wiederbelebung im sicheren Fenster nutzen.

Earth’s Retribution stellt MP her und verkürzt Bolt mit der Rang-12-Discharge-Option. Chain of Torment öffnet Condemnation; dessen Rang-12-Reset benötigt einen kritischen Treffer. Healing Enhancement wandelt Angriff in Heal Boost um. Light of Protection stapelt seinen Schadensbuff nicht mit Undefeated Mantra: höherer Rang gilt, bei Gleichstand Mantra.'''}
aliases={'Chains of Torment':'Chain of Torment',"Earth's Punishment":'Earth Punishment','Earth’s Punishment':'Earth Punishment','Light of Regen':'Light of Regeneration','Summon Ancient Spirit':'Summon: Ancient Spirit','Focusing Block':'Focused Block','Focus Eye':'Focused Eye','Drilling Dart':'Drill Dart'}
for loc in LOCALES:
 p=ROOT/f'src/content/{loc}/cleric-build.mdx';s=p.read_text(encoding='utf8')
 s=re.sub(r'\*\*[^\n]*TW[^\n]*\*\*[^\n]*\n\n','',s)
 for a,b in cleanses[loc]:
  assert a in s,(loc,a)
  s=s.replace(a,b)
 s=s.replace('<h2 id="gear-and-daevanion">',extra[loc]+'\n\n<h2 id="gear-and-daevanion">')
 s=s.replace('| Resurrection |','| Summon Resurrection |').replace('Healing Light and Resurrection','Healing Light and Summon Resurrection')
 for a,b in aliases.items():
  # Avoid changing the complete name Light of Regeneration twice.
  s=re.sub(re.escape(a)+r'(?![A-Za-z])',lambda m:b,s)
 p.write_text(s,encoding='utf8')
 # Apply spelling fixes consistently to class metadata and diagrams, too.
 for slug in ['cleric-build','chanter','gladiator','ranger','spiritmaster','cleric']:
  q=ROOT/f'src/content/{loc}/{slug}.json';text=q.read_text(encoding='utf8')
  for a,b in aliases.items():text=re.sub(re.escape(a)+r'(?![A-Za-z])',lambda m:b,text)
  q.write_text(text,encoding='utf8')
for slug in ['ranger','spiritmaster','sorcerer','templar','assassin','cleric','gladiator','chanter']:
 for loc,aliases in [('es',{'Explorador':'Arquero','Maestro espiritual':'Espiritualista'}),('de',{'Jäger':'Waldläufer'})]:
  for ext in ['mdx','json']:
   p=ROOT/f'src/content/{loc}/{slug}.{ext}';s=p.read_text(encoding='utf8')
   for a,b in aliases.items():s=s.replace(a,b)
   p.write_text(s,encoding='utf8')
print('Merged class icons, linked all eight guides, corrected Cleric recovery in four languages.')
