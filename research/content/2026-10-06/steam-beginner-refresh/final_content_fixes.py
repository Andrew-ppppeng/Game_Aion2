import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
copy = {
 'en': {
  'download': "The base game is now free-to-play. Advanced Access ended on October 5, 2026; you do not need to buy that expired access benefit to install and play. Use [Steam and launch information](/steam) for account setup and [monetization](/monetization) for current paid options.",
  'tier': 'In this early launch comparison, Spiritmaster is S+, while Gladiator and Chanter are S. Use it to shortlist classes, then choose the tank, healer, support or damage role your intended activity needs.',
  'ranger_heading': 'Worked choice: improve a Ranger attempt',
  'spirit': 'Spiritmaster combines an active spirit with short Four Elements opportunities. Keep a spirit summoned and use Elemental Fusion when Four Elements appears. Compare this summon-and-proc loop with the ranged attacks below.',
  'gifts': 'Launch gifts are separate from this coupon. Create an account and log in before **December 2, 2026 at 07:30 UTC** to receive **Advance: Pet Chest** and **Advance: Wishlist Chest** automatically through in-game mail. Claim that mail before **December 9, 2026 at 07:30 UTC**.\n\nThe October 5 gift, **Customization Voucher (Bound)**, is used through **ESC → Closet** to change character skins.',
 },
 'ja': {
  'download': '本編は現在基本プレイ無料です。先行アクセスは2026年10月5日に終了しており、インストールとプレイのために終了済みの先行利用権を買う必要はありません。アカウント設定は[Steamと開始情報](/steam)、現在の有料サービスは[課金システム](/monetization)を確認してください。',
  'tier': '開始時のこの比較ではスピリット マスターがS+、グラディエーターとチャンターがSです。候補を絞ってから、遊びたい活動に必要なタンク、回復、支援、攻撃の役割を選んでください。',
  'ranger_heading': '選択例：レンジャーの失敗を改善する',
  'spirit': 'スピリット マスターは召喚中の精霊と短いFour Elementsの機会を組み合わせます。精霊を維持し、Four Elementsが出たらElemental Fusionを使います。この召喚と発動条件の連携を、以下の遠距離攻撃と比較してください。',
  'gifts': '開始記念の贈り物はこのクーポンとは別です。**2026年12月2日07:30 UTC**までにアカウントを作成してログインすると、**Advance: Pet Chest**と**Advance: Wishlist Chest**がゲーム内メールに自動配布されます。そのメールは**2026年12月9日07:30 UTC**までに受け取ってください。\n\n10月5日の贈り物**Customization Voucher (Bound)**は、**ESC → Closet**でキャラクターの外見を変えるために使います。',
 },
 'es': {
  'download': 'El juego base ya es gratuito. El acceso anticipado terminó el 5 de octubre de 2026; no necesitas comprar ese beneficio vencido para instalar y jugar. Consulta [Steam y el lanzamiento](/steam) para configurar la cuenta y [monetización](/monetization) para las opciones de pago actuales.',
  'tier': 'En esta comparación inicial, Espiritualista tiene S+ y Gladiador y Cantor tienen S. Úsala para reducir candidatos y elige después el rol de tanque, sanación, apoyo o daño que necesite tu actividad.',
  'ranger_heading': 'Ejemplo: mejorar un intento con Arquero',
  'spirit': 'Spiritmaster combina un espíritu activo con ventanas breves de Four Elements. Mantén un espíritu invocado y usa Elemental Fusion cuando aparezca Four Elements. Compara este ciclo de invocación y activaciones con los ataques a distancia siguientes.',
  'gifts': 'Los regalos de lanzamiento son independientes del cupón. Crea una cuenta e inicia sesión antes del **2 de diciembre de 2026 a las 07:30 UTC** para recibir **Advance: Pet Chest** y **Advance: Wishlist Chest** automáticamente por correo del juego. Reclama ese correo antes del **9 de diciembre de 2026 a las 07:30 UTC**.\n\nEl regalo del 5 de octubre, **Customization Voucher (Bound)**, se usa en **ESC → Closet** para cambiar el aspecto del personaje.',
 },
 'de': {
  'download': 'Das Hauptspiel ist jetzt kostenlos. Advanced Access endete am 5. Oktober 2026; du musst diesen abgelaufenen Zugang nicht kaufen, um zu installieren und zu spielen. Lies [Steam und Spielstart](/steam) für die Kontoeinrichtung sowie [Monetarisierung](/monetization) für aktuelle Kaufoptionen.',
  'tier': 'In diesem frühen Startvergleich liegt Beschwörer bei S+, Gladiator und Kantor bei S. Grenze damit Kandidaten ein und wähle anschließend die Tank-, Heil-, Unterstützungs- oder Schadensrolle für deine Aktivität.',
  'ranger_heading': 'Beispiel: einen Waldläufer-Versuch verbessern',
  'spirit': 'Spiritmaster verbindet einen aktiven Geist mit kurzen Four-Elements-Fenstern. Halte einen Geist beschworen und nutze Elemental Fusion, sobald Four Elements erscheint. Vergleiche diese Beschwörungs- und Auslöserfolge mit den folgenden Fernkampfangriffen.',
  'gifts': 'Startgeschenke sind unabhängig von diesem Coupon. Erstelle ein Konto und melde dich vor dem **2. Dezember 2026 um 07:30 UTC** an, um **Advance: Pet Chest** und **Advance: Wishlist Chest** automatisch per Spielpost zu erhalten. Hole diese Post vor dem **9. Dezember 2026 um 07:30 UTC** ab.\n\nDas Geschenk vom 5. Oktober, **Customization Voucher (Bound)**, wird über **ESC → Closet** für das Aussehen des Charakters verwendet.',
 },
}
for locale, c in copy.items():
 path = ROOT / f'src/content/{locale}/download.mdx'
 body = path.read_text(encoding='utf-8')
 parts = body.split('\n\n')
 for i, paragraph in enumerate(parts):
  if "Founder's Pack" in paragraph and '/monetization)' in paragraph: parts[i] = c['download']
 path.write_text('\n\n'.join(parts), encoding='utf-8', newline='\n')
 path = ROOT / f'src/content/{locale}/tier-list.mdx'
 body = path.read_text(encoding='utf-8')
 body = re.sub(r'<h3>[^\n]*B[^\n]*S</h3>', '<h3>' + c['ranger_heading'] + '</h3>', body)
 marker = re.search(r'<h2 id="spiritmaster-and-ranger">[^\n]+</h2>', body)
 if c['spirit'] not in body: body = body[:marker.end()] + '\n\n' + c['spirit'] + body[marker.end():]
 path.write_text(body, encoding='utf-8', newline='\n')
 meta_path = ROOT / f'src/content/{locale}/tier-list.json'
 meta = json.loads(meta_path.read_text(encoding='utf-8')); meta['quickAnswer'] = c['tier']
 meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
 path = ROOT / f'src/content/{locale}/code.mdx'
 body = path.read_text(encoding='utf-8')
 parts = body.split('\n\n')
 for i, paragraph in enumerate(parts):
  if 'Battle Enhancement Scroll (Engraved)' in paragraph and '×5' in paragraph: parts[i] = c['gifts']
 path.write_text('\n\n'.join(parts), encoding='utf-8', newline='\n')

path = ROOT / 'src/content/article-data/code.json'
record = json.loads(path.read_text(encoding='utf-8'))
for source in [
 {'id': 'steam-launch-rewards-20261004', 'title': 'AION 2 Launch Rewards', 'url': 'https://steamcommunity.com/games/3393110/announcements/detail/712288224875118658', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-10-04', 'version': 'Official Steam snapshot read 2026-10-06; login deadline Dec1 23:30 PST = Dec2 07:30 UTC, mail expiry Dec8 23:30 PST = Dec9 07:30 UTC. Both reward chests delivered automatically.'},
 {'id': 'steam-customization-gift-20261005', 'title': 'Customization Voucher to all players', 'url': 'https://steamcommunity.com/games/3393110/announcements/detail/712288224875120755', 'kind': 'official', 'region': 'Global', 'publishedAt': '2026-10-05', 'version': 'Official Steam snapshot read 2026-10-06; Customization Voucher (Bound), ESC > Closet; no claim deadline inferred.'},
]:
 if not any(s['id'] == source['id'] for s in record['sources']): record['sources'].append(source)
path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
