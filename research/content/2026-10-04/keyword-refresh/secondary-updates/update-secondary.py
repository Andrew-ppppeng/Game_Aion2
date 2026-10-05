from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[5]
CONTENT = ROOT / 'src/content'
LANGS = ['en', 'ja', 'es', 'de']

def load_meta(lang, slug):
    return json.loads((CONTENT / lang / f'{slug}.json').read_text(encoding='utf-8'))

def save_meta(lang, slug, value):
    (CONTENT / lang / f'{slug}.json').write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def add_section(slug, section_id, titles, bodies, before):
    for i, lang in enumerate(LANGS):
        p = CONTENT / lang / f'{slug}.mdx'
        text = p.read_text(encoding='utf-8')
        assert f'id="{section_id}"' not in text, (slug, section_id)
        marker = f'<h2 id="{before}">'
        section = f'<h2 id="{section_id}">{titles[i]}</h2>\n\n{bodies[i].strip()}\n\n'
        assert marker in text
        if slug == 'server' and before == 'europe-pairings':
            wrapper = '<GuideRegion region="eu">'
            assert wrapper in text
            text = text.replace(wrapper, section + wrapper, 1)
        else:
            text = text.replace(marker, section + marker, 1)
        p.write_text(text, encoding='utf-8')
        meta = load_meta(lang, slug)
        index = next(n for n, item in enumerate(meta['toc']) if item['id'] == before)
        meta['toc'].insert(index, {'id': section_id, 'title': titles[i]})
        save_meta(lang, slug, meta)

def replace_section(slug, section_id, titles, bodies):
    for i, lang in enumerate(LANGS):
        p = CONTENT / lang / f'{slug}.mdx'
        text = p.read_text(encoding='utf-8')
        pattern = rf'<h2 id="{section_id}">.*?(?=<h2 id=|\Z)'
        text, count = re.subn(pattern, f'<h2 id="{section_id}">{titles[i]}</h2>\n\n{bodies[i].strip()}\n\n', text, count=1, flags=re.S)
        assert count == 1
        p.write_text(text, encoding='utf-8')
        meta = load_meta(lang, slug)
        for item in meta['toc']:
            if item['id'] == section_id:
                item['title'] = titles[i]
        save_meta(lang, slug, meta)

add_section('map', 'gathering-map-filters',
    ['Gathering map: show only the resource you need', '採集マップで必要な資源だけを表示する', 'Mapa de recolección: muestra solo el recurso necesario', 'Sammelkarte: nur die gesuchte Ressource anzeigen'], [
'''An **AION 2 gathering map** is a filtered resource map. Open [Aion2T](https://aion2t.com/map), select the zone, click **Hide All**, then enable the relevant resource category. Expand the category and leave only the material you need selected.

| Recipe ingredient | Map layer to inspect |
| --- | --- |
| Metal or ore | Ore |
| Gemstone | Gems |
| Herb | Herbs |
| Vegetable | Vegetables |
| Wood | Logs |

Copy the material name from the recipe or quest. A similar name may refer to a different quality or a quest-only item. A marker shows a possible location, rather than guaranteeing that a node is present or that your proficiency is sufficient.

On [Aion2Maps](https://www.aion2maps.com), type a resource name into search and press **Enter** to highlight matches. Check the map card's **Global/TW** label before using a later-region route. Maps marked **not open at launch** are unavailable on Global at launch.''',
'''**AION 2の採集マップ**は、資源を絞り込んだ地図です。[Aion2T](https://aion2t.com/map)でエリアを選び、**Hide All**を押して必要な分類だけを有効にします。分類を展開し、欲しい素材だけを選んでください。

| レシピの素材 | 確認するレイヤー |
| --- | --- |
| 金属・鉱石 | Ore |
| 宝石 | Gems |
| 薬草 | Herbs |
| 野菜 | Vegetables |
| 木材 | Logs |

レシピやクエストから正確な素材名を確認します。似た名前でも品質やクエスト専用アイテムが異なる場合があります。地点は出現候補であり、資源の存在や自分の採集熟練度を保証しません。

[Aion2Maps](https://www.aion2maps.com)では検索欄に資源名を入力し、**Enter**で一致する地点を強調表示します。後半エリアのルートを使う前に、マップカードの**Global/TW**表示を確認してください。**not open at launch**と表示されたマップはGlobal開始時には利用できません。''',
'''Un **mapa de recolección de AION 2** es un mapa filtrado por recursos. Abre [Aion2T](https://aion2t.com/map), elige la zona, pulsa **Hide All** y activa la categoría necesaria. Despliégala y deja seleccionado solo el material que buscas.

| Ingrediente | Capa que consultar |
| --- | --- |
| Metal o mineral | Ore |
| Gema | Gems |
| Hierba | Herbs |
| Verdura | Vegetables |
| Madera | Logs |

Copia el nombre de la receta o misión. Un nombre parecido puede corresponder a otra calidad o a un objeto exclusivo de misión. El marcador indica una ubicación posible; no garantiza un nodo disponible ni suficiente competencia para recogerlo.

En [Aion2Maps](https://www.aion2maps.com), escribe el recurso y pulsa **Enter** para destacar coincidencias. Comprueba la etiqueta **Global/TW** de la tarjeta antes de usar una ruta de regiones posteriores. Los mapas marcados **not open at launch** no están disponibles al lanzamiento de Global.''',
'''Eine **AION-2-Sammelkarte** ist eine nach Ressourcen gefilterte Karte. Öffne [Aion2T](https://aion2t.com/map), wähle die Zone, klicke auf **Hide All** und aktiviere die benötigte Kategorie. Klappe sie auf und wähle nur dein gesuchtes Material.

| Rezeptzutat | Passende Kartenebene |
| --- | --- |
| Metall oder Erz | Ore |
| Edelstein | Gems |
| Kraut | Herbs |
| Gemüse | Vegetables |
| Holz | Logs |

Übernimm den genauen Namen aus Rezept oder Quest. Ähnliche Namen können andere Qualitätsstufen oder reine Questgegenstände bezeichnen. Ein Marker zeigt einen möglichen Fundort; er garantiert weder ein vorhandenes Vorkommen noch ausreichende Sammelfertigkeit.

Gib in [Aion2Maps](https://www.aion2maps.com) den Ressourcennamen ein und drücke **Enter**, um Treffer hervorzuheben. Prüfe vor Routen in späteren Regionen die **Global/TW**-Kennzeichnung auf der Kartenkarte. Mit **not open at launch** markierte Karten sind zum Global-Start geschlossen.'''
], 'resource-route')

replace_section('map', 'map-troubleshooting',
    ['Find cave nodes and back up collection progress', '洞窟の地点を探し、収集進捗を保存する', 'Encuentra nodos en cuevas y guarda el progreso', 'Höhlenvorkommen finden und Fortschritt sichern'], [
'''| Problem | What to try |
| --- | --- |
| The marker is at your position, but the node is missing | Check the marker card's height and nearby cave entrances or ramps |
| Rock or a roof hides the location in Aion2Maps | Hold **Alt** for the see-through lens, or change **Roofs over paths** in Settings |
| Several floors overlap | Use **Floor slice** or **PgUp/PgDn** to inspect vertical layers |
| No resources appear | Confirm the zone, resource layer and search; clear a previous search if necessary |
| A node is absent | Skip it and continue; a map marker is not a live spawn indicator |
| A completed collectible remains on the route | Mark it complete with **F** in Aion2Maps and compare with in-game progress |

Aion2Maps stores progress in the current browser. Before clearing browser data or moving to another device, open **Settings → Your progress → Export progress** and keep the file. Use **Import…** in the destination browser to restore it. Keep a separate note of completed zones during long sessions.

Use [gathering](/gathering) for node requirements, promotion blocks and comparing material yield.

<GuideNext slug="gathering" />''',
'''| 問題 | 対応 |
| --- | --- |
| マーカーの位置にいるのに資源がない | 地点カードの高さと、近くの洞窟入口・坂を確認する |
| Aion2Mapsで岩や屋根に隠れる | **Alt**を押して透過レンズを使うか、設定の**Roofs over paths**を変更する |
| 複数の階層が重なる | **Floor slice**または**PgUp/PgDn**で上下の層を調べる |
| 資源が表示されない | エリア・資源レイヤー・検索を確認し、前の検索を必要に応じて解除する |
| 採集地点に資源がない | 次へ進む。マーカーはリアルタイムの出現情報ではない |
| 回収済みの収集物が残る | Aion2Mapsで**F**を押して完了にし、ゲーム内進捗と照合する |

Aion2Mapsの進捗は現在のブラウザに保存されます。ブラウザデータを消す前や別端末へ移る前に、**Settings → Your progress → Export progress**でファイルを保存してください。移行先のブラウザでは**Import…**で復元します。長い収集では完了エリアを別にも記録しましょう。

採集条件、昇格で止まる場合、収量の比較は[採集ガイド](/gathering)へ。

<GuideNext slug="gathering" />''',
'''| Problema | Qué probar |
| --- | --- |
| Estás en el marcador, pero no ves el nodo | Comprueba su altura en la tarjeta y entradas de cueva o rampas cercanas |
| Rocas o tejados lo ocultan en Aion2Maps | Mantén **Alt** para usar la lente transparente o cambia **Roofs over paths** en Settings |
| Hay varios pisos superpuestos | Usa **Floor slice** o **PgUp/PgDn** para revisar las alturas |
| No aparecen recursos | Revisa zona, capa y búsqueda; elimina la búsqueda anterior si hace falta |
| Falta un nodo | Continúa: el marcador no informa de apariciones en tiempo real |
| Un coleccionable completado sigue en la ruta | Márcalo con **F** en Aion2Maps y compáralo con el progreso del juego |

Aion2Maps guarda el progreso en el navegador actual. Antes de borrar sus datos o cambiar de dispositivo, abre **Settings → Your progress → Export progress** y conserva el archivo. Usa **Import…** en el navegador de destino para restaurarlo. Anota también las zonas completadas durante sesiones largas.

Consulta [recolección](/gathering) para requisitos, promociones y comparación de rendimiento.

<GuideNext slug="gathering" />''',
'''| Problem | Lösung |
| --- | --- |
| Du stehst am Marker, siehst aber kein Vorkommen | Prüfe die Höhe auf der Markerkarte und nahe Höhleneingänge oder Rampen |
| Fels oder Dächer verdecken es in Aion2Maps | Halte **Alt** für die Durchsichtlinse oder ändere **Roofs over paths** in Settings |
| Mehrere Stockwerke überlagern sich | Prüfe die Ebenen mit **Floor slice** oder **PgUp/PgDn** |
| Keine Ressourcen sichtbar | Zone, Ressourcenebene und Suche prüfen; alte Suche gegebenenfalls löschen |
| Ein Vorkommen fehlt | Weitergehen: Kartenmarker sind keine Live-Anzeige vorhandener Ressourcen |
| Abgeschlossener Fund bleibt in der Route | In Aion2Maps mit **F** markieren und mit dem Spielstand vergleichen |

Aion2Maps speichert Fortschritt im aktuellen Browser. Öffne vor dem Löschen von Browserdaten oder einem Gerätewechsel **Settings → Your progress → Export progress** und bewahre die Datei auf. Stelle sie im Zielbrowser mit **Import…** wieder her. Notiere bei langen Sitzungen zusätzlich abgeschlossene Zonen.

Der [Sammelguide](/gathering) behandelt Anforderungen, Aufstiegsblockaden und Materialertrag.

<GuideNext slug="gathering" />'''
])

# Remove the obsolete sync-code control from the tool comparison.
replacements = {
    'en': ('Voxel terrain view and progress sync code', 'Voxel terrain, height cards and progress export/import'),
    'ja': ('ボクセル地形表示、進捗同期コード', 'ボクセル地形、高さカード、進捗の書き出し・読み込み'),
    'es': ('Terreno voxel y código de sincronización', 'Terreno voxel, alturas y exportación/importación del progreso'),
    'de': ('Voxel-Gelände und Fortschritts-Synchronisierungscode', 'Voxel-Gelände, Höhenkarten und Export/Import des Fortschritts'),
}
for lang, (old, new) in replacements.items():
    p = CONTENT / lang / 'map.mdx'
    text = p.read_text(encoding='utf-8')
    if old in text:
        p.write_text(text.replace(old, new), encoding='utf-8')

add_section('gathering', 'route-results',
    ['Check why a gathering route fails', '採集ルートがうまくいかない理由を確認する', 'Comprueba por qué falla una ruta', 'Warum eine Sammelroute scheitert'], [
'''A resource map solves **where to look**; the node tooltip and your Essence Extraction progress determine **what you can gather**. Use the [gathering map filters](/map#gathering-map-filters) to find a small cluster, then test the nodes in game.

| Result during the run | Next action |
| --- | --- |
| Node is visible but gathering is unavailable | Read its exact requirement and compare it with your current proficiency |
| Attempts repeatedly fail | Check the node difficulty and your selected success-related skills before extending the route |
| The collected item does not match the quest | Compare the full name, quality and **Bound** status; do not buy a similarly named substitute |
| Most time is spent moving | Reduce the number of stops and remove repeated climbs or long detours |
| The proficiency bar stops | Check the current stage cap and promotion quest before grinding more nodes |

Keep one short record: **material needed / useful quantity / minutes / failures**. Repeat the route only if it advances the recipe or promotion you are working on. The best route for your character depends on faction, accessible nodes and current proficiency; a distant high-tier material can be a poor beginner route.''',
'''資源マップは**探す場所**を示し、採集地点の説明とEssence Extractionの進捗が**採れるもの**を決めます。[採集マップの絞り込み](/map#gathering-map-filters)で小さな集まりを探してから、ゲーム内で試しましょう。

| 結果 | 次の行動 |
| --- | --- |
| 資源は見えるが採集できない | 正確な条件を読み、現在の熟練度と比較する |
| 失敗が続く | 地点の難度と成功率関連スキルを確認してからルートを伸ばす |
| クエストの素材と違うものが採れた | 完全な名前・品質・**Bound**を確認し、似た素材を代用品として買わない |
| 移動に時間がかかりすぎる | 地点を減らし、繰り返す登りや大きな迂回を外す |
| 熟練度が増えなくなった | さらに採る前に段階上限と昇格クエストを確認する |

**必要な素材／役立つ個数／時間／失敗数**だけを記録します。取り組んでいるレシピや昇格に役立つルートを繰り返してください。適したルートは種族、到達可能な地点、熟練度で変わります。遠い高級素材は初心者向きとは限りません。''',
'''El mapa de recursos indica **dónde buscar**; el requisito del nodo y Essence Extraction determinan **qué puedes recoger**. Usa los [filtros del mapa](/map#gathering-map-filters) para localizar un grupo pequeño y pruébalo en el juego.

| Resultado | Siguiente acción |
| --- | --- |
| Ves el nodo, pero no puedes recogerlo | Compara su requisito exacto con tu competencia actual |
| Fallas muchos intentos | Revisa dificultad y habilidades de éxito antes de ampliar la ruta |
| El objeto no coincide con la misión | Compara nombre completo, calidad y estado **Bound**; no compres un sustituto de nombre parecido |
| Pasas demasiado tiempo desplazándote | Reduce paradas, subidas repetidas y desvíos largos |
| La competencia deja de subir | Comprueba el límite de etapa y la misión de promoción antes de seguir |

Anota **material necesario / cantidad útil / minutos / fallos**. Repite solo si avanzas en tu receta o promoción. La mejor ruta depende de facción, acceso y competencia; un material avanzado y lejano puede ser mala opción para empezar.''',
'''Die Ressourcenkarte beantwortet **wo du suchen solltest**; Vorkommen-Tooltip und Essence Extraction entscheiden **was du sammeln kannst**. Finde mit den [Kartenfiltern](/map#gathering-map-filters) eine kleine Gruppe und teste sie im Spiel.

| Ergebnis | Nächster Schritt |
| --- | --- |
| Vorkommen sichtbar, Sammeln nicht möglich | Genaue Anforderung mit deiner aktuellen Fertigkeit vergleichen |
| Viele Fehlversuche | Schwierigkeit und ausgewählte erfolgsbezogene Fertigkeiten prüfen, bevor du die Route erweiterst |
| Gegenstand passt nicht zur Quest | Vollständigen Namen, Qualität und **Bound**-Status prüfen; keinen ähnlich benannten Ersatz kaufen |
| Zu viel Reisezeit | Weniger Stopps, wiederholte Anstiege und lange Umwege entfernen |
| Fertigkeitsbalken steigt nicht weiter | Stufenlimit und Aufstiegsquest prüfen, bevor du weiter sammelst |

Notiere **benötigtes Material / nutzbare Menge / Minuten / Fehlschläge**. Wiederhole die Route, wenn sie dein Rezept oder den Aufstieg voranbringt. Die passende Route hängt von Fraktion, erreichbaren Vorkommen und Fertigkeit ab; ein weit entferntes hochwertiges Material eignet sich nicht automatisch für Anfänger.'''
], 'promotion-and-value')

add_section('server', 'global-server-regions',
    ['Global server regions, Steam and PURPLE', 'Globalの地域とSteam・PURPLE', 'Regiones Global, Steam y PURPLE', 'Global-Regionen, Steam und PURPLE'], [
'''| Global region selector | Choose it for |
| --- | --- |
| NA West / NA East | North American groups; agree on the coast before the server name |
| Europe | European groups and play hours |
| South America | South American groups |
| Asia | Japan-based Global hosting; compare latency from your country |

Players in Southeast Asia should compare their connection to **Asia** with the region their friends use. The Asia label identifies the Global regional pool; it does not mean the Taiwan service. **KR/TW characters and progress do not transfer to Global.**

Steam and PURPLE players share Global servers and in-game content. Your group can use different launchers, provided everyone chooses the same region, faction and server. Using the same character on both launchers requires account linking; simply playing with a friend on the other launcher does not.''',
'''| Globalの地域選択 | 選ぶ目的 |
| --- | --- |
| NA West / NA East | 北米の仲間。サーバー名の前に東西をそろえる |
| Europe | 欧州の仲間と活動時間 |
| South America | 南米の仲間 |
| Asia | 日本に設置されたGlobal地域。自分の国からの遅延を比較する |

東南アジアのプレイヤーは**Asia**への接続と仲間の地域を比較しましょう。AsiaはGlobalの地域枠で、台湾サービスではありません。**KR/TWのキャラクターと進行状況はGlobalへ移せません。**

SteamとPURPLEはGlobalのサーバーとゲーム内容を共有します。地域・種族・サーバーが同じなら、仲間と異なるランチャーを使えます。同じキャラクターを両ランチャーで使う場合はアカウント連携が必要ですが、別ランチャーの仲間と遊ぶだけなら不要です。''',
'''| Selector Global | Para quién |
| --- | --- |
| NA West / NA East | Grupos norteamericanos; acordad la costa antes del nombre del servidor |
| Europe | Grupos y horarios europeos |
| South America | Grupos sudamericanos |
| Asia | Alojamiento Global en Japón; compara la latencia desde tu país |

Si juegas desde el sudeste asiático, compara tu conexión a **Asia** con la región de tus amigos. Asia es el grupo regional Global, no el servicio de Taiwán. **Los personajes y el progreso KR/TW no se transfieren a Global.**

Steam y PURPLE comparten servidores y contenido Global. Podéis usar lanzadores distintos si elegís la misma región, facción y servidor. Para usar tu mismo personaje en ambos lanzadores necesitas vincular cuentas; para jugar con un amigo del otro lanzador, no.''',
'''| Global-Regionswahl | Passend für |
| --- | --- |
| NA West / NA East | Nordamerikanische Gruppen; zuerst die Küste, dann den Servernamen abstimmen |
| Europe | Europäische Gruppen und Spielzeiten |
| South America | Südamerikanische Gruppen |
| Asia | Global-Hosting in Japan; Latenz aus deinem Land vergleichen |

Spieler aus Südostasien sollten ihre Verbindung zu **Asia** mit der Region ihrer Freunde vergleichen. Asia ist der Global-Serverpool und nicht der Taiwan-Dienst. **KR/TW-Charaktere und Fortschritt werden nicht nach Global übertragen.**

Steam und PURPLE teilen Global-Server und Spielinhalte. Verschiedene Launcher sind möglich, wenn Region, Fraktion und Server übereinstimmen. Derselbe Charakter auf beiden Launchern benötigt Kontoverknüpfung; gemeinsames Spielen mit Freunden auf dem anderen Launcher nicht.'''
], 'europe-pairings')

add_section('server', 'queues-and-population',
    ['Queues, server population and latency', '待機列・サーバー人口・遅延', 'Colas, población del servidor y latencia', 'Warteschlangen, Serverbevölkerung und Latenz'], [
'''A queue means the server is limiting new logins at that moment. It does not reveal an exact player count or maximum capacity. [Steam concurrent players](/player-count) measure the Steam app across servers and exclude PURPLE; they cannot tell you how many players are on Europe Siel.

Members in good standing use a **priority queue** when a server is full. Both queues advance as space opens; membership does **not** guarantee immediate entry. Disciplinary action or suspected Terms of Service violations can remove priority access.

For an EU server-location decision, choose **Europe** in the client and compare latency during your usual play hours. Do not infer the physical hosting city from a server's fantasy name. If your group changes servers to avoid a queue, keep the same region and faction and review [transfer restrictions](/server-transfer).''',
'''待機列は、その時点で新しいログインが制限されていることを示します。正確な人数や最大収容人数はわかりません。[Steamの同時接続数](/player-count)は全サーバーのSteam利用者で、PURPLEは含まず、Europe Sielの人数には換算できません。

規約違反などの問題がないメンバーシップ利用者は、満員時に**優先待機列**へ入ります。空きが出ると両方の列が進み、メンバーシップは即時入場を**保証しません**。処分や規約違反の疑いで優先権を失う場合があります。

EUの接続先を選ぶ場合はクライアントで**Europe**を選び、普段遊ぶ時間の遅延を比較してください。架空のサーバー名から設置都市は判断できません。待機列を避けるため移る場合も地域と種族をそろえ、[移転条件](/server-transfer)を確認しましょう。''',
'''Una cola indica que el servidor limita nuevos accesos en ese momento. No revela una población exacta ni su capacidad máxima. Los [jugadores simultáneos de Steam](/player-count) suman todos los servidores Steam y excluyen PURPLE; no indican cuántos juegan en Europe Siel.

Los miembros sin problemas disciplinarios entran en una **cola prioritaria** cuando el servidor está lleno. Ambas colas avanzan cuando queda espacio; la membresía **no** garantiza acceso inmediato. Las sanciones o sospechas de incumplir las condiciones pueden retirar esa prioridad.

Para elegir conexión europea, selecciona **Europe** y compara la latencia a tus horas habituales. No deduzcas la ciudad del centro de datos del nombre ficticio del servidor. Si cambiáis para evitar colas, mantened región y facción y revisad las [restricciones de transferencia](/server-transfer).''',
'''Eine Warteschlange bedeutet, dass neue Logins gerade begrenzt werden. Sie verrät weder die genaue Spielerzahl noch die maximale Kapazität. [Gleichzeitige Steam-Spieler](/player-count) werden über alle Steam-Server gezählt und enthalten keine PURPLE-Spieler; daraus lässt sich die Bevölkerung von Europe Siel nicht bestimmen.

Mitglieder ohne einschlägige Regelverstöße erhalten bei vollen Servern eine **Prioritätswarteschlange**. Beide Warteschlangen rücken bei freien Plätzen vor; Mitgliedschaft garantiert **keinen** sofortigen Zugang. Disziplinarmaßnahmen oder vermutete Verstöße gegen die Nutzungsbedingungen können die Priorität aufheben.

Wähle für europäische Verbindungen **Europe** und vergleiche die Latenz zu deinen üblichen Spielzeiten. Ein Fantasiename verrät keine Rechenzentrumsstadt. Wenn eure Gruppe zur Queue-Vermeidung wechselt, behaltet Region und Fraktion bei und prüft [Transferbeschränkungen](/server-transfer).'''
], 'transfer-rules')

add_section('steam', 'europe-launch-time',
    ['Europe release date and local launch times', '欧州の開始日と現地時刻', 'Fecha y hora de lanzamiento en Europa', 'Europa-Startdatum und lokale Uhrzeiten'], [
'''Europe joins the **October 5, 2026 Global public opening**. The scheduled 13:00 UTC opening converts to:

| Time zone on October 5 | Public opening |
| --- | --- |
| UTC | 13:00 |
| UK — BST | 14:00 |
| Central Europe — CEST | 15:00 |
| Eastern Europe — EEST | 16:00 |

Free public entry begins after the transition maintenance. Advanced Access is a separate entitlement and ends at 05:00 UTC that day. Choose **Europe** as your [server region](/server#europe-pairings) before creating a character.''',
'''欧州も**2026年10月5日のGlobal正式サービス**に参加します。予定の13:00 UTCは次の現地時刻です。

| 10月5日の時間帯 | 正式サービス開始 |
| --- | --- |
| UTC | 13:00 |
| 英国 — BST | 14:00 |
| 中央欧州 — CEST | 15:00 |
| 東欧 — EEST | 16:00 |

無料の一般入場は移行メンテナンス後に始まります。Advanced Accessは別の権利で、同日の05:00 UTCに終了します。キャラクター作成前に[サーバー地域](/server#europe-pairings)で**Europe**を選んでください。''',
'''Europa participa en la **apertura pública Global del 5 de octubre de 2026**. La hora prevista de 13:00 UTC equivale a:

| Zona horaria el 5 de octubre | Apertura pública |
| --- | --- |
| UTC | 13:00 |
| Reino Unido — BST | 14:00 |
| Europa central — CEST | 15:00 |
| Europa oriental — EEST | 16:00 |

El acceso público gratuito empieza tras el mantenimiento de transición. Advanced Access es un permiso separado y termina ese día a las 05:00 UTC. Elige **Europe** como [región del servidor](/server#europe-pairings) antes de crear tu personaje.''',
'''Europa nimmt am **öffentlichen Global-Start am 5. Oktober 2026** teil. Die geplanten 13:00 UTC entsprechen:

| Zeitzone am 5. Oktober | Öffentlicher Start |
| --- | --- |
| UTC | 13:00 |
| Vereinigtes Königreich — BST | 14:00 |
| Mitteleuropa — CEST | 15:00 |
| Osteuropa — EEST | 16:00 |

Der kostenlose öffentliche Zugang beginnt nach der Übergangswartung. Advanced Access benötigt eine separate Berechtigung und endet an diesem Tag um 05:00 UTC. Wähle vor der Charaktererstellung **Europe** als [Serverregion](/server#europe-pairings).'''
], 'global-and-regional-versions')

replace_section('steam', 'platform-and-controller-support',
    ['Console release, Steam Deck and controller support', '家庭用ゲーム機・Steam Deck・コントローラー対応', 'Consolas, Steam Deck y soporte de mando', 'Konsolen, Steam Deck und Controller-Unterstützung'], [
'''**The supported Global platform is Windows PC through Steam or PURPLE.** Steam and PURPLE share the same content and servers.

| Platform or control method | Current Global status |
| --- | --- |
| Windows PC — Steam / PURPLE | Officially supported |
| PlayStation / Xbox | No confirmed console release date |
| Mobile | No Global mobile client |
| Linux / Steam Deck | No official platform support; possible launchability is not supported compatibility |
| Controller | Playable, but not officially supported |

For a controller setup, test movement, targeting, menus and emergency skills before group content. Keep keyboard and mouse available. A Steam download or successful launch on another device does not guarantee working anti-cheat, controls or future compatibility.''',
'''**Globalが正式対応するのは、SteamまたはPURPLEのWindows PCです。**両者は同じ内容とサーバーを利用します。

| 環境・操作方法 | Globalの現在の状態 |
| --- | --- |
| Windows PC — Steam / PURPLE | 正式対応 |
| PlayStation / Xbox | 家庭用ゲーム機版の開始日は未発表 |
| モバイル | Globalのモバイル版なし |
| Linux / Steam Deck | 正式対応なし。起動できても対応環境とは限らない |
| コントローラー | 操作可能だが正式サポート対象外 |

コントローラーでは、グループ参加前に移動、ターゲット、メニュー、緊急スキルを試し、キーボードとマウスも用意しましょう。別端末でSteamからダウンロード・起動できても、不正対策、操作、今後の互換性を保証しません。''',
'''**Global admite oficialmente Windows PC mediante Steam o PURPLE.** Ambos comparten contenido y servidores.

| Plataforma o control | Estado actual de Global |
| --- | --- |
| Windows PC — Steam / PURPLE | Soporte oficial |
| PlayStation / Xbox | Sin fecha confirmada para consolas |
| Móvil | Sin cliente móvil Global |
| Linux / Steam Deck | Sin soporte oficial; poder iniciarlo no garantiza compatibilidad |
| Mando | Se puede jugar, pero no tiene soporte oficial |

Prueba movimiento, objetivos, menús y habilidades de emergencia antes de jugar en grupo con mando. Ten teclado y ratón disponibles. Descargar o iniciar Steam en otro dispositivo no garantiza antitrampas, controles ni compatibilidad futura.''',
'''**Global unterstützt offiziell Windows PC über Steam oder PURPLE.** Beide teilen Inhalte und Server.

| Plattform oder Eingabe | Aktueller Global-Status |
| --- | --- |
| Windows PC — Steam / PURPLE | Offiziell unterstützt |
| PlayStation / Xbox | Kein bestätigtes Konsolen-Startdatum |
| Mobilgeräte | Kein Global-Mobilclient |
| Linux / Steam Deck | Keine offizielle Unterstützung; möglicher Start garantiert keine Kompatibilität |
| Controller | Spielbar, aber nicht offiziell unterstützt |

Teste mit Controller vor Gruppeninhalten Bewegung, Ziele, Menüs und Notfallfähigkeiten. Halte Tastatur und Maus bereit. Ein Download oder erfolgreicher Start über Steam auf einem anderen Gerät garantiert weder Anti-Cheat-Funktion noch Steuerung oder zukünftige Kompatibilität.'''
])

add_section('guide', 'how-to-play-by-region',
    ['How to play now in NA, Europe or Taiwan', '北米・欧州・台湾で今から遊ぶには', 'Cómo jugar ahora desde NA, Europa o Taiwán', 'Jetzt in NA, Europa oder Taiwan spielen'], [
'''| Where you want to play | Client and first choice |
| --- | --- |
| US / North America | Global Steam or PURPLE; agree on **NA West** or **NA East** |
| Europe | Global Steam or PURPLE; select **Europe** |
| Taiwan service | Use the [Taiwan official PURPLE download](https://tw.ncsoft.com/aion2/download/index) and that service's account conditions |

For Global, entry before **October 5 at 13:00 UTC** requires Advanced Access entitlement; the transition maintenance runs from 05:00 to 13:00 UTC. Public launch is free-to-play. Installation alone does not grant early access.

**Playing with friends:** share the region, faction and exact server name. Steam and PURPLE players can play together. You do not need to link launchers to join a friend; linking is for accessing your own same character on both. Solo play is also available.

**Moving from Taiwan or Korea:** Global uses separate progression. Your KR/TW character does not carry over. Follow the [regional setup section](/download#taiwan-client) for the Taiwan installation entry.''',
'''| 遊びたいサービス | クライアントと最初の選択 |
| --- | --- |
| 米国・北米 | GlobalのSteamまたはPURPLE。**NA West**か**NA East**をそろえる |
| 欧州 | GlobalのSteamまたはPURPLE。**Europe**を選ぶ |
| 台湾サービス | [台湾公式PURPLEダウンロード](https://tw.ncsoft.com/aion2/download/index)と、そのサービスのアカウント条件を使う |

Globalの**10月5日13:00 UTC**より前の入場にはAdvanced Access権利が必要で、同日05:00〜13:00 UTCは移行メンテナンスです。一般公開は基本無料です。インストールだけでは先行入場できません。

**仲間と遊ぶ場合：**地域・種族・正確なサーバー名を共有します。SteamとPURPLEの利用者は一緒に遊べます。仲間と遊ぶためのランチャー連携は不要で、自分の同じキャラクターを両方で使う場合に必要です。ソロでも遊べます。

**台湾・韓国から移る場合：**Globalの進行状況は別です。KR/TWのキャラクターは引き継げません。台湾のインストール入口は[地域別セットアップ](/download#taiwan-client)へ。''',
'''| Servicio deseado | Cliente y primera elección |
| --- | --- |
| Estados Unidos / Norteamérica | Steam o PURPLE Global; acordad **NA West** o **NA East** |
| Europa | Steam o PURPLE Global; selecciona **Europe** |
| Servicio de Taiwán | Usa la [descarga oficial PURPLE de Taiwán](https://tw.ncsoft.com/aion2/download/index) y sus condiciones de cuenta |

Para entrar a Global antes del **5 de octubre a las 13:00 UTC** necesitas permiso Advanced Access; el mantenimiento de transición va de 05:00 a 13:00 UTC. La apertura pública es gratuita. Instalar el juego no concede acceso anticipado.

**Con amigos:** compartid región, facción y nombre exacto del servidor. Steam y PURPLE pueden jugar juntos. No necesitas vincular lanzadores para reunirte con un amigo; la vinculación permite usar tu mismo personaje en ambos. También puedes jugar en solitario.

**Desde Taiwán o Corea:** Global tiene progreso separado. Tu personaje KR/TW no se transfiere. Consulta la [configuración regional](/download#taiwan-client) para el instalador de Taiwán.''',
'''| Gewünschter Dienst | Client und erste Auswahl |
| --- | --- |
| USA / Nordamerika | Global über Steam oder PURPLE; **NA West** oder **NA East** abstimmen |
| Europa | Global über Steam oder PURPLE; **Europe** wählen |
| Taiwan-Dienst | [Offiziellen Taiwan-PURPLE-Download](https://tw.ncsoft.com/aion2/download/index) und dessen Kontobedingungen verwenden |

Vor **5. Oktober, 13:00 UTC** braucht Global eine Advanced-Access-Berechtigung; die Übergangswartung dauert 05:00–13:00 UTC. Der öffentliche Start ist kostenlos. Installation allein gewährt keinen frühen Zugang.

**Mit Freunden:** Region, Fraktion und exakten Servernamen teilen. Steam- und PURPLE-Spieler können gemeinsam spielen. Für Freunde auf dem anderen Launcher ist keine Verknüpfung nötig; sie dient dem Zugriff auf deinen eigenen selben Charakter in beiden. Solospiel ist ebenfalls möglich.

**Wechsel aus Taiwan oder Korea:** Global hat eigenen Fortschritt. Dein KR/TW-Charakter wird nicht übertragen. Den Taiwan-Installer findest du unter [regionale Einrichtung](/download#taiwan-client).'''
], 'main-story-first')

# Add a live, explicitly community-run regional Discord, without claiming a TW official server.
discord_rows = [
    '| [AION 2 Community Discord](https://discord.gg/AION2) | Community-run regional discussion, including KR/TW; check the service before following advice | Global / KR / TW |',
    '| [AION 2 Community Discord](https://discord.gg/AION2) | KR/TWを含む地域別交流。案内を使う前にサービスを確認。コミュニティ運営 | Global / KR / TW |',
    '| [Discord AION 2 Community](https://discord.gg/AION2) | Comunidad con conversaciones KR/TW; comprueba el servicio antes de seguir consejos | Global / KR / TW |',
    '| [AION 2 Community Discord](https://discord.gg/AION2) | Community-geführte Diskussionen einschließlich KR/TW; Dienst vor Anwendung prüfen | Global / KR / TW |',
]
for i, lang in enumerate(LANGS):
    p = CONTENT / lang / 'guide.mdx'
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    idx = next(n for n, line in enumerate(lines) if 'https://discord.gg/aion2official' in line)
    lines.insert(idx + 1, discord_rows[i])
    p.write_text('\n'.join(lines) + '\n', encoding='utf-8')

add_section('monetization', 'quna-use-and-budget',
    ['What Quna does, how to get it and how much to spend', 'Qunaの用途・入手方法・予算', 'Para qué sirve Quna, cómo conseguirla y cuánto gastar', 'Quna: Verwendung, Erwerb und Budget'], [
'''**Quna is premium currency.** Use it for Quna-priced shop items, the premium Battle Pass track or buying Kina through the player Exchange. You can obtain it through a Quna purchase or by selling Kina to another player on the Exchange. **Exchange access requires active membership.** Direct player-to-player item trading is disabled; use the Market for player item trades.

There is no purchase required to enter the public-launch base game. For a spending plan, separate these costs:

- **Access:** public launch is free; an eligible pack is needed only for the remaining Advanced Access window.
- **Trading:** membership unlocks Market and Exchange access; the US-dollar reference is $15 per month.
- **Quna purchases:** compare the offered Quna amount with the final local-currency checkout price. A player Exchange rate is not the cash price of a Quna pack.
- **Progression:** premium-pass rewards include upgrade materials and currency; cosmetics have no combat stats.

Buy for a specific item or benefit instead of budgeting an assumed amount to “win.” Membership provides priority queue access for accounts in good standing when servers are full, but it does not guarantee immediate login.''',
'''**Qunaはプレミアム通貨**です。Quna価格のショップ商品、Battle Passのプレミアム枠、プレイヤーExchangeでKinaを買うために使います。Quna購入のほか、Exchangeで他プレイヤーにKinaを売って入手できます。**Exchangeには有効なメンバーシップが必要**です。直接のプレイヤー間アイテム取引は無効で、売買にはMarketを使います。

一般公開の基本ゲームへの入場に購入は不要です。予算は次のように分けてください。

- **入場：**正式サービスは無料。残りのAdvanced Access期間には対象パックが必要。
- **取引：**メンバーシップでMarketとExchangeが利用可能。米ドル基準は月15ドル。
- **Quna購入：**数量と現地通貨の最終価格を比較。プレイヤー間の交換率はQunaパックの現金価格とは別。
- **成長：**プレミアムパスには強化素材と通貨。外見アイテムには戦闘ステータスなし。

「勝つため」の想定額ではなく、欲しい商品や特典を決めて買いましょう。満員時には問題のないメンバーシップ利用者が優先待機列へ入りますが、即時ログインは保証されません。''',
'''**Quna es la moneda prémium.** Sirve para productos con precio Quna, la vía prémium del Battle Pass o comprar Kina en el Exchange. Puedes comprar Quna u obtenerla vendiendo Kina a otro jugador en el Exchange. **El Exchange requiere membresía activa.** El intercambio directo de objetos entre jugadores está desactivado; usa el Market.

No necesitas comprar para entrar al juego base en su apertura pública. Separa estos gastos:

- **Acceso:** lanzamiento público gratuito; un pack válido solo es necesario para el tiempo restante de Advanced Access.
- **Comercio:** membresía para Market y Exchange; referencia de 15 USD al mes.
- **Quna:** compara cantidad ofrecida y precio final en tu moneda. La tasa entre jugadores no equivale al precio en efectivo de un pack Quna.
- **Progresión:** la vía prémium incluye materiales y monedas; los cosméticos no tienen estadísticas de combate.

Compra por un objeto o beneficio concreto, sin asumir una cantidad necesaria para «ganar». La membresía da cola prioritaria a cuentas sin problemas disciplinarios cuando hay saturación, pero no garantiza acceso inmediato.''',
'''**Quna ist Premiumwährung.** Nutze sie für entsprechend bepreiste Shopartikel, den Premium-Battle-Pass oder den Kauf von Kina im Spieler-Exchange. Quna gibt es per Kauf oder durch den Verkauf von Kina an andere Spieler im Exchange. **Der Exchange benötigt aktive Mitgliedschaft.** Direkter Spieler-zu-Spieler-Gegenstandstausch ist deaktiviert; nutze den Market.

Zum öffentlichen Start benötigt das Basisspiel keinen Kauf. Trenne dein Budget nach Zweck:

- **Zugang:** öffentlicher Start kostenlos; ein berechtigtes Paket ist nur für die restliche Advanced-Access-Zeit nötig.
- **Handel:** Mitgliedschaft für Market und Exchange; Referenzpreis 15 US-Dollar pro Monat.
- **Quna:** Menge und endgültigen Preis in deiner Währung vergleichen. Spieler-Wechselkurse sind nicht der Barpreis eines Quna-Pakets.
- **Fortschritt:** Premium-Pass enthält Aufwertungsmaterialien und Währung; Kosmetik hat keine Kampfwerte.

Kaufe für einen konkreten Gegenstand oder Vorteil, statt einen angenommenen Betrag zum „Gewinnen“ einzuplanen. Regelkonforme Mitglieder erhalten bei vollen Servern eine Prioritätswarteschlange, aber keinen garantierten sofortigen Login.'''
], 'founder-packs')

add_section('monetization', 'founder-cosmetic-access',
    ['Founder cosmetics and one-time rewards', 'Founder外見と一度限りの報酬', 'Cosméticos Founder y recompensas de una sola entrega', 'Founder-Kosmetik und einmalige Belohnungen'], [
'''The Founder cosmetic change will let your account use its included cosmetics on **all characters across all servers**. Implementation is still pending and is planned for after Advanced Access; do not assume a newly created character can already claim them.

The eligible cosmetics depend on the purchased tier: Standard's title, Deluxe's armor and weapon skins, and Ultimate's additional armor skin, Black Dragon pet and Blazing Sun wings. **The 30-day membership, Supply Chest, Styling Chest and their contents remain one-time rewards.**

If this changes the tier you want, PURPLE supports an upgrade to a higher pack. For Steam, the announced route is to buy the higher tier on the same account and request a refund for the lower pack through support; the exact process is still pending. Check the process with [support](https://help.plaync.com/faq/aion2global) before paying twice.''',
'''Founder外見の変更では、対象外見を**全サーバーの全キャラクター**で使えるようになります。実装はまだ準備中で、Advanced Access終了後の予定です。新キャラクターで既に受け取れるとは考えないでください。

対象は購入した段階によって異なります。Standardの称号、Deluxeの防具・武器外見、Ultimateの追加防具外見・Black Dragonペット・Blazing Sunウイングです。**30日メンバーシップ、Supply Chest、Styling Chestと中身は一度限りの報酬のままです。**

上位パックへ変更したい場合、PURPLEではアップグレードが可能です。Steamは同じアカウントで上位を買い、下位の返金をサポートに依頼する案内ですが、詳細手順は準備中です。二重支払い前に[サポート](https://help.plaync.com/faq/aion2global)で手順を確認してください。''',
'''El cambio de cosméticos Founder permitirá usarlos en **todos los personajes y servidores** de tu cuenta. Sigue pendiente de implementación, prevista después de Advanced Access; no des por hecho que un personaje nuevo ya puede reclamarlos.

Depende del pack comprado: título Standard, aspectos de armadura y arma Deluxe, y armadura adicional, mascota Black Dragon y alas Blazing Sun Ultimate. **La membresía de 30 días, Supply Chest, Styling Chest y sus contenidos siguen siendo recompensas de una sola entrega.**

PURPLE permite subir a un pack superior. Para Steam, la vía anunciada consiste en comprar el superior en la misma cuenta y solicitar al soporte el reembolso del inferior; el proceso exacto sigue pendiente. Consulta el procedimiento con [soporte](https://help.plaync.com/faq/aion2global) antes de pagar dos veces.''',
'''Die Founder-Kosmetikänderung soll enthaltene Kosmetik auf **allen Charakteren und Servern** deines Kontos verfügbar machen. Die Umsetzung steht noch aus und ist nach Advanced Access geplant; rechne bei einem neuen Charakter noch nicht mit verfügbarer Abholung.

Das Paket bestimmt die Kosmetik: Standard-Titel, Deluxe-Rüstungs- und Waffen-Skins sowie zusätzliche Ultimate-Rüstung, Black-Dragon-Pet und Blazing-Sun-Flügel. **30-Tage-Mitgliedschaft, Supply Chest, Styling Chest und deren Inhalte bleiben einmalige Belohnungen.**

PURPLE erlaubt ein Upgrade auf ein höheres Paket. Für Steam ist der Kauf des höheren Pakets auf demselben Konto und eine Support-Erstattung des günstigeren angekündigt; der genaue Ablauf steht noch aus. Kläre ihn beim [Support](https://help.plaync.com/faq/aion2global), bevor du zweimal bezahlst.'''
], 'passes-and-progression')

# Metadata communicates the refreshed player tasks, without adding new keyword strings.
metadata = {
 'map': [
  ('AION 2 Map: Gathering Resources and 3D Routes', 'Filter AION 2 gathering maps by resource, find cave nodes and heights, plan compact routes, and export collection progress.', 'Find one resource with Aion2T filters; use Aion2Maps for cave access and height. Select your faction’s zone and back up progress before changing browsers.', 'For a gathering map, select your zone in Aion2T, use Hide All and enable only the resource needed. Use Aion2Maps for cave height, floor slices and exporting collection progress.'),
  ('AION 2 マップ：採集資源と3Dルート', 'AION 2の採集資源を絞り込み、洞窟の高さを確認し、短いルートと収集進捗の保存を進める。', 'Aion2Tで資源を絞り、Aion2Mapsで洞窟入口と高さを確認。種族のエリアを選び、ブラウザ変更前に進捗を保存します。', 'Aion2Tでエリアを選び、Hide Allから必要な資源だけを表示します。洞窟の高さ、階層表示、進捗の書き出しはAion2Mapsを使います。'),
  ('Mapa de AION 2: recursos y rutas de recolección', 'Filtra recursos de AION 2, encuentra nodos en cuevas y alturas, crea rutas compactas y exporta tu progreso de colección.', 'Filtra un recurso con Aion2T y revisa altura y acceso con Aion2Maps. Elige la zona de tu facción y guarda el progreso antes de cambiar de navegador.', 'Elige tu zona en Aion2T, pulsa Hide All y activa solo el recurso necesario. Usa Aion2Maps para alturas, pisos y exportación del progreso.'),
  ('AION 2 Karte: Sammelressourcen und 3D-Routen', 'Filtere AION-2-Sammelressourcen, finde Höhlenvorkommen und Höhen, plane kurze Routen und exportiere deinen Sammelfortschritt.', 'Filtere eine Ressource mit Aion2T; prüfe Höhleneingänge und Höhen in Aion2Maps. Wähle deine Fraktionszone und sichere Fortschritt vor Browserwechseln.', 'Wähle in Aion2T die Zone, klicke Hide All und aktiviere nur die gesuchte Ressource. Aion2Maps hilft mit Höhen, Ebenenschnitt und Fortschrittsexport.'),
 ],
 'server': [
  ('AION 2 Global Servers: Regions, Lists and Queues', 'Choose AION 2 Global servers in NA, Europe, South America or Asia. Compare faction pairings, queues, cross-launcher play and transfer restrictions.', 'Agree on region, faction and server name. Steam and PURPLE share servers; understand queues and transfer limits before moving to join friends.', 'Global has NA West, NA East, Europe, South America and Asia server pools. Steam and PURPLE players share them. Choose the same region, faction and server for open-world play with friends.'),
  ('AION 2 Globalサーバー：地域・一覧・待機列', 'AION 2 Globalの北米・欧州・南米・Asia地域、種族の組み合わせ、待機列と移転条件を確認。', '地域・種族・サーバー名をそろえます。SteamとPURPLEは同じサーバーを使い、待機列と移転制限を確認して仲間と合流します。', 'GlobalはNA West、NA East、Europe、South America、Asiaの地域枠です。SteamとPURPLEは共通サーバー。仲間と同じ地域・種族・サーバーを選びます。'),
  ('Servidores AION 2 Global: regiones, listas y colas', 'Elige región y servidor AION 2 Global en NA, Europa, Sudamérica o Asia. Compara facciones, colas, juego Steam/PURPLE y transferencias.', 'Acordad región, facción y servidor. Steam y PURPLE comparten servidores; revisa colas y transferencias antes de reunirte con amigos.', 'Global tiene NA West, NA East, Europe, South America y Asia. Steam y PURPLE comparten servidores. Para mundo abierto con amigos, elegid misma región, facción y servidor.'),
  ('AION 2 Global-Server: Regionen, Listen und Queues', 'Wähle AION-2-Global-Server in NA, Europa, Südamerika oder Asia. Vergleiche Fraktionspaarungen, Queues, Steam/PURPLE und Transferregeln.', 'Region, Fraktion und Servernamen abstimmen. Steam und PURPLE teilen Server; Queues und Transfergrenzen vor einem Wechsel zu Freunden prüfen.', 'Global bietet NA West, NA East, Europe, South America und Asia. Steam und PURPLE teilen Server. Für gemeinsame offene Welt müssen Region, Fraktion und Server übereinstimmen.'),
 ],
 'steam': [
  ('AION 2 Steam: Europe Launch Time and Platforms', 'Find AION 2 Steam app 3393110, Europe launch times, Windows requirements, console release status, Steam Deck and controller support.', 'Install the official Steam game, check Europe’s local opening time and distinguish Windows support from controller or other-platform compatibility.', 'The Global Steam app is 3393110. Europe’s public opening is planned for October 5, 2026 at 13:00 UTC / 15:00 CEST. Official support is Windows PC via Steam or PURPLE; controllers are playable but not officially supported.'),
  ('AION 2 Steam：欧州開始時刻と対応環境', 'AION 2のSteam App 3393110、欧州開始時刻、Windows動作環境、家庭用版・Steam Deck・コントローラー対応を確認。', 'Steam正式版を入れ、欧州の現地開始時刻を確認。Windowsの正式対応と他端末・コントローラーの互換性を区別します。', 'GlobalのSteam Appは3393110。欧州一般公開は2026年10月5日13:00 UTC／15:00 CEST予定。正式対応はSteam・PURPLEのWindows PC。コントローラーは操作可能ですが正式サポート対象外です。'),
  ('AION 2 Steam: apertura europea y plataformas', 'Encuentra AION 2 Steam app 3393110, hora europea, requisitos Windows, estado de consolas, Steam Deck y soporte de mando.', 'Instala el juego oficial y comprueba la hora europea. Distingue soporte Windows de compatibilidad con otros dispositivos y mando.', 'La app Steam Global es 3393110. Europa abre el 5 de octubre de 2026 a las 13:00 UTC / 15:00 CEST. Soporte oficial en Windows PC con Steam o PURPLE; el mando es jugable sin soporte oficial.'),
  ('AION 2 Steam: Europa-Start und Plattformen', 'Finde AION 2 Steam-App 3393110, Europa-Startzeiten, Windows-Anforderungen und den Status von Konsolen, Steam Deck und Controllern.', 'Installiere das offizielle Spiel und prüfe Europas lokale Startzeit. Unterscheide Windows-Support von Kompatibilität mit anderen Geräten und Controllern.', 'Global-Steam-App: 3393110. Europa-Start geplant für 5. Oktober 2026 um 13:00 UTC / 15:00 CEST. Offizieller Support für Windows PC via Steam/PURPLE; Controller spielbar, aber nicht offiziell unterstützt.'),
 ],
 'guide': [
  ('AION 2 Beginner Guide: How to Play with Friends', 'Learn how to play AION 2 in NA or Europe, choose the right regional client, join friends, follow the story and find Global or Taiwan communities.', 'Choose your service, client, region, faction and server. Steam and PURPLE can play together; TW/KR progress is separate. Start the story and solve one progression blocker at a time.', 'Install Global through Steam or PURPLE and choose the same region, faction and server as your friends. Public access is planned for October 5, 2026 at 13:00 UTC. Taiwan uses its separate regional client and progress.'),
  ('AION 2 初心者ガイド：始め方と仲間との遊び方', 'AION 2の北米・欧州での始め方、地域別クライアント、仲間との合流、ストーリー、台湾コミュニティを確認。', 'サービス・クライアント・地域・種族・サーバーを選びます。SteamとPURPLEは一緒に遊べますがKR/TWの進行は別。物語を進め、育成の課題を1つずつ解消します。', 'GlobalはSteamまたはPURPLEを使い、仲間と地域・種族・サーバーをそろえます。一般公開は2026年10月5日13:00 UTC予定。台湾は別のクライアントと進行状況です。'),
  ('Guía inicial AION 2: cómo jugar con amigos', 'Aprende a jugar AION 2 desde NA o Europa, elegir cliente regional, reunirte con amigos y encontrar comunidades Global o Taiwán.', 'Elige servicio, cliente, región, facción y servidor. Steam y PURPLE juegan juntos; KR/TW tiene progreso separado. Sigue la historia y resuelve un bloqueo cada vez.', 'Instala Global con Steam o PURPLE y elige misma región, facción y servidor que tus amigos. Apertura pública prevista el 5 de octubre de 2026 a las 13:00 UTC. Taiwán tiene cliente y progreso separados.'),
  ('AION 2 Einsteigerguide: mit Freunden spielen', 'Lerne AION 2 in NA oder Europa zu starten, regionale Clients auszuwählen, Freunde zu treffen und Global- oder Taiwan-Communitys zu finden.', 'Dienst, Client, Region, Fraktion und Server wählen. Steam und PURPLE spielen gemeinsam; KR/TW-Fortschritt bleibt getrennt. Folge der Geschichte und löse jeweils eine Fortschrittsblockade.', 'Installiere Global über Steam oder PURPLE und wähle Region, Fraktion und Server deiner Freunde. Öffentlicher Start geplant für 5. Oktober 2026, 13:00 UTC. Taiwan nutzt eigenen Client und Fortschritt.'),
 ],
 'monetization': [
  ('AION 2 Monetization: Quna, Membership and Costs', 'Understand AION 2 Quna uses, purchases and Kina exchange, membership trading access, free play, paid progression and Founder cosmetic restrictions.', 'Separate free access, trading membership, Quna purchases and character passes. Check one-time Founder rewards and the pending account-wide cosmetic change.', 'Global public access is free-to-play. Quna buys shop items, the premium pass or Kina through the player Exchange. Market and Exchange require membership. Paid progression rewards and cosmetics have different effects.'),
  ('AION 2 課金：Quna・メンバーシップ・費用', 'AION 2のQuna用途、購入・Kina交換、会員の取引条件、無料プレイ、有料成長とFounder報酬制限を確認。', '無料入場、取引メンバーシップ、Quna購入、キャラクターのパスを分けます。一度限りのFounder報酬と準備中の外見共有を確認しましょう。', 'Global正式サービスは基本無料。Qunaはショップ商品、プレミアムパス、ExchangeでKinaを買うために使います。MarketとExchangeにはメンバーシップが必要。有料成長報酬と外見の効果は異なります。'),
  ('Monetización AION 2: Quna, membresía y costes', 'Conoce usos de Quna, compras e intercambio Kina, requisitos de membresía, juego gratuito, progresión de pago y límites de recompensas Founder.', 'Distingue acceso gratis, membresía comercial, Quna y pases por personaje. Comprueba recompensas únicas y el cambio cosmético para toda la cuenta aún pendiente.', 'Global público es gratuito. Quna compra productos, pase prémium o Kina en el Exchange. Market y Exchange requieren membresía. Las recompensas de progresión y los cosméticos tienen efectos distintos.'),
  ('AION 2 Monetarisierung: Quna, Mitgliedschaft, Kosten', 'Verstehe Quna-Verwendung, Kauf und Kina-Tausch, Mitgliedschaft für Handel, kostenloses Spiel, bezahlten Fortschritt und Founder-Beschränkungen.', 'Trenne freien Zugang, Handelsmitgliedschaft, Quna und Charakter-Pässe. Prüfe einmalige Founder-Belohnungen und die ausstehende kontoweite Kosmetikänderung.', 'Global ist zum öffentlichen Start kostenlos. Quna kauft Shopartikel, Premium-Pass oder Kina im Exchange. Market und Exchange brauchen Mitgliedschaft. Fortschrittsbelohnungen und Kosmetik wirken unterschiedlich.'),
 ],
}
for slug, variants in metadata.items():
    for i, lang in enumerate(LANGS):
        meta = load_meta(lang, slug)
        for key, value in zip(['title', 'description', 'summary', 'quickAnswer'], variants[i]):
            meta[key] = value
        save_meta(lang, slug, meta)

for slug in ['map', 'gathering', 'server', 'steam', 'guide', 'monetization']:
    p = CONTENT / 'article-data' / f'{slug}.json'
    data = json.loads(p.read_text(encoding='utf-8'))
    data['checkedAt'] = '2026-10-04'
    data['revision'] = '2026-10-04.keyword-refresh-1'
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

print('Updated six existing themes in four languages; builds waits for live planner interaction.')
