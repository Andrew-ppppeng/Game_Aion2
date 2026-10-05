import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
EDITS = {
    'en': {
        'Its collection bonuses and any level-dependent changes': 'The collection bonuses listed for that wing',
        "rather than assuming every rarity has the same bonuses or enhancement track.": "rather than assuming every rarity has the same bonuses.",
        "Before enhancing, read the current materials, cost and result in the selected wing's enhancement panel. Spend according to your [build](/builds) and available resources.": "Check the required activity and acquisition cost before pursuing a new pair. Prioritize unlocks that support your [build](/builds) and fit your available resources.",
    },
    'ja': {
        'コレクションのボーナスとレベルによる変化': 'その翼に表示されるコレクションのボーナス',
        '等級だけで効果や強化段階を決めつけず、': '等級だけで効果を決めつけず、',
        '強化前には、その翼の強化画面で素材、費用、結果を読み、[ビルド](/builds)と手持ちの資源に合わせて使います。': '新しい翼を集める前に、必要な活動と入手費用を確認し、[ビルド](/builds)と手持ちの資源に合う目標を優先します。',
    },
    'es': {
        'Bonificaciones de colección y cambios según su nivel': 'Bonificaciones de colección indicadas para ese par',
        'no todas las calidades tienen los mismos bonos ni la misma progresión de mejora.': 'no todas las calidades tienen los mismos bonos.',
        'Antes de mejorarlas, revisa materiales, coste y resultado en su panel actual. Gasta según tu [build](/builds) y los recursos disponibles.': 'Antes de buscar un par nuevo, comprueba la actividad requerida y su coste de obtención. Prioriza los desbloqueos que ayuden a tu [build](/builds) y encajen con tus recursos.',
    },
    'de': {
        'Sammlungsboni und Änderungen durch das Level': 'Die für dieses Paar angegebenen Sammlungsboni',
        'statt gleiche Boni oder Verbesserungsstufen für jede Qualität anzunehmen.': 'statt gleiche Boni für jede Qualität anzunehmen.',
        'Prüfe vor einer Verbesserung die aktuellen Materialien, Kosten und das Ergebnis im jeweiligen Verbesserungsfenster. Richte den Einsatz nach deinem [Build](/builds) und deinen verfügbaren Ressourcen aus.': 'Prüfe vor einem neuen Paar die benötigte Aktivität und die Bezugskosten. Priorisiere Freischaltungen, die deinen [Build](/builds) unterstützen und zu deinen verfügbaren Ressourcen passen.',
    },
}

for locale, replacements in EDITS.items():
    path = ROOT / 'src' / 'content' / locale / 'wings.mdx'
    body = path.read_text(encoding='utf-8')
    for old, new in replacements.items():
        assert body.count(old) == 1, (locale, old)
        body = body.replace(old, new)
    path.write_text(body,encoding='utf-8')
    print(locale, 'removed unsupported wing enhancement instructions')
