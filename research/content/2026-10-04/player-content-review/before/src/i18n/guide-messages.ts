import type {Locale} from './routing';

const en = {
  enlarge: 'Enlarge image', close: 'Close image', illustration: 'Guide diagram', next: 'Your next step',
  contents: 'Contents', source: 'Image source', reset: 'Reset checklist', complete: 'completed',
  checklistNote: 'Your checklist stays in this browser. It does not change your in-game progress.',
  swipe: 'Swipe or scroll sideways to see the full table', filter: 'Choose your main role',
  classNote: 'Choose by the responsibility you enjoy. These are playstyle matches, not performance rankings. Classes can fulfil more than one role.',
  all: 'Show all', frontline: 'Frontline', melee: 'Melee damage', ranged: 'Ranged damage', healing: 'Healing & recovery', support: 'Melee support',
  faction: 'Choose a faction route', elyos: 'Elyos', asmodians: 'Asmodians', region: 'Filter server region',
  eu: 'Europe', naWest: 'NA West', naEast: 'NA East', latam: 'South America', asia: 'Asia',
  roster: 'Official class portraits', inspect: 'Compare roles below', snapshot: 'Dated snapshot; check the official notice for updates.',
  iconTable: 'Eight Global class icons', classIcon: 'Class icon', englishName: 'English name', localName: 'Class name',
  iconNote: 'Match the emblem to its class name. Open an icon to inspect the original 90 × 94 image; these are official Global emblems.',
};
type GuideMessages = {[K in keyof typeof en]: string};

export const guideMessages = {
  en,
  ja: {
    enlarge: '画像を拡大', close: '画像を閉じる', illustration: 'ガイドの説明図', next: '次のステップ',
    contents: '目次', source: '画像の出典', reset: 'チェックをリセット', complete: '完了',
    checklistNote: 'チェック内容はこのブラウザーに保存されます。ゲーム内の進行状況は変更されません。',
    swipe: '左右にスクロールすると表全体を確認できます', filter: '主に担当したい役割を選ぶ',
    classNote: '好きな役割を基準に選びましょう。強さのランキングではなく、プレイスタイルの目安です。複数の役割をこなせるクラスもあります。',
    all: 'すべて表示', frontline: '前衛', melee: '近接攻撃', ranged: '遠距離攻撃', healing: '回復・蘇生', support: '近接サポート',
    faction: '種族の育成ルートを選ぶ', elyos: '天族', asmodians: '魔族', region: 'サーバー地域で絞り込む',
    eu: 'ヨーロッパ', naWest: '北米西部', naEast: '北米東部', latam: '南米', asia: 'アジア',
    roster: '公式クラスイラスト', inspect: '本文で役割を比較する', snapshot: '確認日時点の情報です。更新は公式告知をご確認ください。',
    iconTable: 'Global版の8クラスのアイコン', classIcon: 'クラスアイコン', englishName: '英語名', localName: '日本語名',
    iconNote: '紋章とクラス名を照合できます。アイコンを開くと、公式Global版の元画像（90 × 94）を確認できます。',
  },
  es: {
    enlarge: 'Ampliar imagen', close: 'Cerrar imagen', illustration: 'Diagrama de la guía', next: 'Tu siguiente paso',
    contents: 'Índice', source: 'Fuente de la imagen', reset: 'Reiniciar lista', complete: 'completados',
    checklistNote: 'La lista se guarda en este navegador. No cambia tu progreso dentro del juego.',
    swipe: 'Desliza o desplázate horizontalmente para ver toda la tabla', filter: 'Elige tu función principal',
    classNote: 'Elige según la responsabilidad que disfrutes. Son orientaciones de estilo de juego, no clasificaciones de rendimiento. Una clase puede cumplir varias funciones.',
    all: 'Mostrar todo', frontline: 'Primera línea', melee: 'Daño cuerpo a cuerpo', ranged: 'Daño a distancia', healing: 'Curación y recuperación', support: 'Apoyo cuerpo a cuerpo',
    faction: 'Elige la ruta de tu facción', elyos: 'Elios', asmodians: 'Asmodianos', region: 'Filtrar región del servidor',
    eu: 'Europa', naWest: 'Norteamérica oeste', naEast: 'Norteamérica este', latam: 'Sudamérica', asia: 'Asia',
    roster: 'Ilustraciones oficiales de las clases', inspect: 'Compara las funciones en la guía', snapshot: 'Información de la fecha indicada; consulta el anuncio oficial para ver cambios.',
    iconTable: 'Iconos de las ocho clases de Global', classIcon: 'Icono de clase', englishName: 'Nombre en inglés', localName: 'Nombre en español',
    iconNote: 'Relaciona cada emblema con su clase. Abre un icono para consultar la imagen original de 90 × 94; son los emblemas oficiales de Global.',
  },
  de: {
    enlarge: 'Bild vergrößern', close: 'Bild schließen', illustration: 'Schaubild zum Guide', next: 'Dein nächster Schritt',
    contents: 'Inhalt', source: 'Bildquelle', reset: 'Checkliste zurücksetzen', complete: 'erledigt',
    checklistNote: 'Die Checkliste wird in diesem Browser gespeichert. Sie verändert deinen Fortschritt im Spiel nicht.',
    swipe: 'Seitlich wischen oder scrollen, um die ganze Tabelle zu sehen', filter: 'Wähle deine bevorzugte Hauptrolle',
    classNote: 'Wähle nach der Verantwortung, die dir Spaß macht. Dies sind Hinweise zum Spielstil, keine Leistungsrangliste. Klassen können mehrere Rollen übernehmen.',
    all: 'Alle anzeigen', frontline: 'Frontlinie', melee: 'Nahkampfschaden', ranged: 'Fernkampfschaden', healing: 'Heilung und Erholung', support: 'Nahkampfunterstützung',
    faction: 'Wähle den Levelweg deiner Fraktion', elyos: 'Elyos', asmodians: 'Asmodier', region: 'Serverregion filtern',
    eu: 'Europa', naWest: 'NA West', naEast: 'NA Ost', latam: 'Südamerika', asia: 'Asien',
    roster: 'Offizielle Klassenillustrationen', inspect: 'Rollen im Guide vergleichen', snapshot: 'Stand zum angegebenen Datum; Änderungen stehen in der offiziellen Ankündigung.',
    iconTable: 'Symbole der acht Global-Klassen', classIcon: 'Klassensymbol', englishName: 'Englischer Name', localName: 'Deutscher Name',
    iconNote: 'Ordne jedes Symbol seiner Klasse zu. Öffne ein Symbol, um das Originalbild mit 90 × 94 Pixeln zu sehen; es sind die offiziellen Global-Symbole.',
  },
} satisfies Record<Locale, GuideMessages>;
