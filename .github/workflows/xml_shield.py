import re
import os

path_tg = 'TMessagesProj/src/main/res/values-tg/strings.xml'
path_en = 'TMessagesProj/src/main/res/values/strings.xml'

def ultimate_factory_restore():
    if not os.path.exists(path_tg) or not os.path.exists(path_en): return
    
    with open(path_tg, 'r', encoding='utf-8') as f:
        content = f.read().replace('name=&quot;', 'name="').replace('&quot;>', '">').replace('&quot;/>', '"/>')
    
    tg_dict = {}
    for match in re.finditer(r'<string name="([^"]+)">([^<]*)</string>', content):
        tg_dict[match.group(1)] = match.group(2)

    with open(path_en, 'r', encoding='utf-8') as f:
        en_lines = f.readlines()

    final = []
    for line in en_lines:
        m = re.search(r'<string name="([^"]+)">', line)
        if m and m.group(1) in tg_dict:
            final.append(f'    <string name="{m.group(1)}">{tg_dict[m.group(1)]}</string>\n')
        else:
            final.append(line)

    with open(path_tg, 'w', encoding='utf-8') as f:
        f.writelines(final)
    print("✅ Иҷро шуд!")

if __name__ == "__main__":
    ultimate_factory_restore()
