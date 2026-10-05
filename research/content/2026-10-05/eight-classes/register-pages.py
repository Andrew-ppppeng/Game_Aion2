import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
LOCALES = ['en', 'ja', 'es', 'de']
NEW = ['templar', 'assassin', 'sorcerer', 'cleric']
def read(path): return (ROOT/path).read_text(encoding='utf-8')
def write(path, value): (ROOT/path).write_text(value, encoding='utf-8')
def save(path, value): write(path, json.dumps(value, ensure_ascii=False, indent=2)+'\n')

plan = json.loads(read('content-topics.json'))
category = next(x for x in plan['categories'] if x['category']=='class selection')
for slug in NEW:
    if 'aion 2 '+slug not in category['keywords']: category['keywords'].append('aion 2 '+slug)
save('content-topics.json', plan)
identities = json.loads(read('src/content/class-identities.json'))
for entry in identities: entry['href'] = '/'+entry['id']
save('src/content/class-identities.json', identities)
for locale in LOCALES:
    data = json.loads(read('src/messages/'+locale+'.json'))
    for slug in NEW: data['topics'][slug] = next(x['names'][locale] for x in identities if x['id']==slug)
    save('src/messages/'+locale+'.json', data)

source = read('src/lib/articles.ts')
imports = '\n'.join("import data_"+s+" from '@/content/article-data/"+s+".json';" for s in NEW)
imports += '\n'+'\n'.join("import meta_"+l+'_'+s+" from '@/content/"+l+'/'+s+".json';" for l in LOCALES for s in NEW)
source = source.replace('const sharedData = {', imports+'\n\nconst sharedData = {\n'+ '\n'.join("  '"+s+"': data_"+s+',' for s in NEW))
for locale in LOCALES:
    source = source.replace('  '+locale+': {', '  '+locale+': {\n'+ '\n'.join("    '"+s+"': {metadata: meta_"+locale+'_'+s+", load: () => import('@/content/"+locale+'/'+s+".mdx')}," for s in NEW))
write('src/lib/articles.ts', source)
paths = read('src/lib/reading-paths.ts').replace("  classes: ['builds', 'tier-list'],", "  templar: ['builds', 'gladiator'], assassin: ['builds', 'pvp'],\n  sorcerer: ['builds', 'spiritmaster'], cleric: ['cleric-build', 'chanter'],\n  classes: ['builds', 'tier-list'],")
write('src/lib/reading-paths.ts', paths)

official = dict(id='official-class-roster',title='AION 2 official class roster',url='https://aion2.plaync.com/en-us/about/index',kind='official',region='Global',publishedAt=None,version='Official about-en API archived 2026-10-05; eight identities and class roles')
client = dict(id='global-client-skills',title='AION 2 skill and build planner client records',url='https://aion2.gaming.tools/skills',kind='tool',region='Global',publishedAt=None,version='Global client 1.0.21.0; dataset updated 2026-09-30; complete 280 records and en/ja/es/de names archived 2026-10-05 under research/content/2026-10-05/eight-classes; tooltip triggers and specializations, no claim of live damage testing')
independent = dict(id='independent-client-skill-index',title='MetaBot AION 2 Global skill index',url='https://metabot.gg/en/aion-2/skills',kind='tool',region='Global',publishedAt=None,version='Independent Global client extraction 0.0.4387.0; archived 2026-10-05 for terminology and overlapping mechanic checks; different client build, numeric balance comparisons not published')
videos = {'templar':'f3gxUdec82U','assassin':'DNfd1lZtQkI','sorcerer':'C6-9zLLRiDE','cleric':'A3pZDSt4ceU','gladiator':'WlxLOTs62dM','ranger':'UOuiJT9E1xA','spiritmaster':'v9MYphrcvic','chanter':'EsxGbxt0k-4'}
for slug in [x['id'] for x in identities]+['cleric-build','builds','classes']:
    target = 'src/content/article-data/'+slug+'.json'
    if (ROOT/target).exists(): data=json.loads(read(target))
    else: data=dict(slug=slug,keyword='aion 2 '+slug.replace('-',' '),regions=['Global'],related=['classes','builds','pvp'],sources=[])
    data.update(checkedAt='2026-10-05',revision='2026-10-05.eight-class-skills-1')
    data.pop('edition',None)
    for item in [official,client,independent]:
        if item['id'] not in [x['id'] for x in data['sources']]: data['sources'].append(item)
    if slug in videos:
        data['sources'].append(dict(id='2026-10-05-class-practice',title=slug.title()+' skill, Stigma and rotation walkthrough',url='https://www.youtube.com/watch?v='+videos[slug],kind='player',region='Mixed',publishedAt=None,version='Complete auto-English captions read with timestamps; client patch varies, used for practical input order only where current Global client mechanics agree; internal transcript ledger'))
    if slug=='cleric-build': data['related']=['cleric','builds','chanter','pvp']
    if slug=='builds': data['related']=[x['id'] for x in identities]
    if slug=='classes': data['related']=['builds']+[x['id'] for x in identities]
    save(target,data)
print('Registered all eight detail destinations and four-language navigation.')
