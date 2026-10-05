import json
from pathlib import Path
root=Path('src/content')
classes=[x['id'] for x in json.loads((root/'class-identities.json').read_text(encoding='utf-8'))]
for locale in ['en','ja','es','de']:
 for class_id in classes:
  path=root/locale/f'{class_id}.mdx'
  text=path.read_text(encoding='utf-8')
  text=text.replace('<GuideVisual id="topic" />',f'<div className="class-media-pair">\n<GuideVisual id="topic" />\n<GuideClassVideo classId="{class_id}" />\n</div>')
  text=text.replace(f'<GuideSkillFocus classId="{class_id}" />',f'<GuideSkillMap classId="{class_id}" />\n\n<GuideSkillFocus classId="{class_id}" />')
  path.write_text(text,encoding='utf-8')
 # Preserve existing headings and anchors. All new visual controls fit existing sections.
 path=root/locale/'builds.mdx'
 text=path.read_text(encoding='utf-8')
 text=text.replace('<GuideVisual id="workflow" />','<GuideVisual id="workflow" />\n\n<GuideSpecializationTree />')
 text=text.replace('<GuideVisual id="topic" />','<GuideVisual id="topic" />\n\n<GuideBuildMaps />')
 path.write_text(text,encoding='utf-8')
 path=root/locale/'classes.mdx'
 text=path.read_text(encoding='utf-8').replace('<GuideClasses />','<GuideClasses />\n\n<GuideClassVideos />')
 path.write_text(text,encoding='utf-8')
 path=root/locale/'cleric-build.mdx'
 text=path.read_text(encoding='utf-8').replace('<GuideVisual id="topic" />','<div className="class-media-pair">\n<GuideVisual id="topic" />\n<GuideClassVideo classId="cleric" />\n</div>\n\n<GuideSkillMap classId="cleric" />')
 path.write_text(text,encoding='utf-8')
for slug in classes+['classes','builds','cleric-build']:
 path=root/'article-data'/f'{slug}.json'
 data=json.loads(path.read_text(encoding='utf-8'))
 data['revision']=data['revision']+'-media'
 if slug in classes:
  videos=json.loads((root/'class-videos.json').read_text(encoding='utf-8'))
  data['sources'].append(dict(id='2026-10-05-official-class-video',title='Official class combat showcase',url='https://www.youtube.com/watch?v='+videos[slug]['videoId'],kind='official',region='Global',publishedAt=None,version='Embedded on the official About the Game page, JS asset package 1.0.0; captions and timestamps retained internally; used for animation preview only'))
 path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Updated 44 localized class/build pages and revision metadata.')
