import re
import os

path_tg = 'TMessagesProj/src/main/res/values-tg/strings.xml'
path_en = 'TMessagesProj/src/main/res/values/strings.xml'

def ultimate_factory_restore():
    if not os.path.exists(path_tg) or not os.path.exists(path_en):
        return

    # 1. Хондани тарҷумаҳои тоҷикӣ ва ислоҳи аломатҳо
    with open(path_tg, 'r', encoding='utf-8') as f:
        content = f.read().replace('name=&quot;', 'name="').replace('&quot;>', '">').replace('&quot;/>', '"/>')
    
    # Ҷамъоварӣ дар луғат (Key -> Value)
    tg_dict = {}
    for m in re.finditer(r'<string name="([^"]+)">([^<]*)</string>', content):
        tg_dict[m.group(1)] = m.group(2)

    # 2. Бозсозӣ аз рӯи шаблони англисӣ (айнан мисли "завод")
    with open(path_en, 'r', encoding='utf-8') as f:
        en_lines = f.readlines()

    final_lines = []
    for line in en_lines:
        m = re.search(r'<string name="([^"]+)">', line)
        if m:
            key = m.group(1)
            val = tg_dict.get(key, None)
            if val is not None:
                final_lines.append(f'    <string name="{key}">{val}</string>\n')
            else:
                final_lines.append(line)
        else:
            final_lines.append(line)

    # 3. Сабти файл бо сохтори комил
    with open(path_tg, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    
    print("✅ Заводи сохтор: Файли тоҷикӣ айнан мисли англисӣ навсозӣ шуд.")

if __name__ == "__main__":
    ultimate_factory_restore()
