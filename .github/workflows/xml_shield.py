import re
import os

path = 'TMessagesProj/src/main/res/values-tg/strings.xml'
if not os.path.exists(path):
    path = 'TMessagesProj_App/src/main/res/values-tg/strings.xml'

def ultimate_factory_restore():
    if not os.path.exists(path):
        print(f"❌ Файл ёфт нашуд: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("🚀 Оғози ҷарроҳии техникӣ: Баргардонидани 11,100 сатр ба формати заводӣ...")

    # 1. Танзими пешу кафо: Ҳамаи номҳои атрибутҳоро аз &quot; тоза карда, ба " заводии Android меорем
    content = content.replace('name=&quot;', 'name="')
    content = re.sub(r'(&quot;>|&quot;\s*>)', '">', content)
    content = content.replace('&quot;/>', '"/>')

    # 2. Ислоҳи сатрҳои кандашуда ва дар ҳаво муаллақ монда (мисли сатри 33-36 ва ғайра)
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            fixed_lines.append(line)
            continue
            
        # Агар сатр сохтори заводии XML-ро дошта бошад, бетағйир мемонад
        if '<string name=' in line or '</string>' in line or '<resources>' in line or '</resources>' in line or '
