import re
import os

path_tg = 'TMessagesProj/src/main/res/values-tg/strings.xml'
path_en = 'TMessagesProj/src/main/res/values/strings.xml'

def ultimate_factory_restore():
    if not os.path.exists(path_tg) or not os.path.exists(path_en):
        print("❌ Файлҳо ёфт нашуданд!")
        return

    # 1. Хондани файли тоҷикӣ ва тозакунии аввалияи нохунакҳо
    with open(path_tg, 'r', encoding='utf-8') as f:
        content_tg = f.read()
    
    content_tg = content_tg.replace('name=&quot;', 'name="')
    content_tg = re.sub(r'(&quot;>|&quot;\s*>)', '">', content_tg)
    content_tg = content_tg.replace('&quot;/>', '"/>')

    # 2. Ҷамъоварии ҳамаи тарҷумаҳои тоҷикӣ ба луғат (ҳатто бисёрсатраҳо)
    tg_dict = {}
    
    # Пайдо кардани тегҳои пурра <string name="...">матн</string>
    for match in re.finditer(r'<string\s+name="([^"]+)">([\s\S]*?)</string>', content_tg):
        tg_dict[match.group(1)] = match.group(2)

    # Пайдо кардани тегҳои холӣ <string name="..."/>
    for match in re.finditer(r'<string\s+name="([^"]+)"/>', content_tg):
        tg_dict[match.group(1)] = ""

    # 3. Хондани файли англисӣ (Шаблон)
    with open(path_en, 'r', encoding='utf-8') as f:
        en_content = f.read()

    en_lines = en_content.splitlines()
    final_lines = []
    
    # 4. Бозсозии сохтор айнан мисли шаблон
    for line in en_lines:
        # Ҷустуҷӯи калид дар сатри англисӣ
        match_key = re.search(r'name="([^"]+)"', line)
        
        if match_key:
            key = match_key.group(1)
            
            # Агар тарҷумаи тоҷикӣ мавҷуд бошад, онро мечаспӯнем
            if key in tg_dict:
                # Агар дар шаблон сатри холӣ бошад
                if '/>' in line and tg_dict[key] == "":
                    final_lines.append(f'    <string name="{key}"/>')
                else:
                    final_lines.append(f'    <string name="{key}">{tg_dict[key]}</string>')
            else:
                # АГАР ТАРҶУМА НАБОШАД: Матни англисиро умуман нест намекунем!
                # Сатри англисиро айнан мемонем, то калима бурида ё гум нашавад
                final_lines.append(line)
        else:
            # Нигоҳ доштани сатрҳои техникӣ, шарҳҳо ва тегҳои оғозу анҷом (resources)
            final_lines.append(line)

    # 5. Сабти ниҳоӣ ба файли тоҷикӣ
    with open(path_tg, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_lines) + '\n')
        
    print("✅ Заводи мутлақ: Сохтор барқарор шуд, ҳеҷ калимае гум нашуд!")

if __name__ == "__main__":
    ultimate_factory_restore()
