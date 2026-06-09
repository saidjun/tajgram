import re
import os

path_tg = 'TMessagesProj/src/main/res/values-tg/strings.xml'
path_en = 'TMessagesProj/src/main/res/values/strings.xml'

def total_factory_reset():
    if not os.path.exists(path_tg) or not os.path.exists(path_en):
        print("❌ Файлҳо ёфт нашуданд!")
        return

    # 1. Хондани файли вайроншудаи тоҷикӣ
    with open(path_tg, 'r', encoding='utf-8') as f:
        bad_content = f.read()

    # Тозакунии аввалияи аломатҳои кова
    bad_content = bad_content.replace('name=&quot;', 'name="').replace('&quot;>', '">').replace('&quot;/>', '"/>')
    bad_content = bad_content.replace('name=&amp;quot;', 'name="').replace('&amp;quot;>', '">')

    # 2. Ҷамъоварии ҳамаи тарҷумаҳои зиндамонда ба луғат
    tg_strings = {}
    
    # Пайдо кардани тегҳои солим ва бисёрсатра
    full_pattern = r'<string\s+name="([^"]+)">([\s\S]*?)</string>'
    for match in re.finditer(full_pattern, bad_content):
        tg_strings[match.group(1)] = match.group(2)

    # Пайдо кардани тегҳои холӣ
    empty_pattern = r'<string\s+name="([^"]+)"/>'
    for match in re.finditer(empty_pattern, bad_content):
        tg_strings[match.group(1)] = ""

    # 3. Хондани шаблони заводии Англисӣ
    with open(path_en, 'r', encoding='utf-8') as f:
        en_content = f.read()

    en_lines = en_content.splitlines()
    clean_lines = []

    # 4. Сохтани файли нав дақиқ "как англисӣ"
    for line in en_lines:
        match_key = re.search(r'name="([^"]+)"', line)
        
        if match_key:
            key = match_key.group(1)
            
            # Агар тарҷумаи тоҷикӣ дошта бошем, онро мечаспӯнем
            if key in tg_strings:
                if '/>' in line and tg_strings[key] == "":
                    clean_lines.append(f'    <string name="{key}"/>')
                else:
                    clean_lines.append(f'    <string name="{key}">{tg_strings[key]}</string>')
            else:
                # Агар тарҷума вайрон ё нест шуда бошад, матни англисиро мемонем (кафолати бехатарӣ)
                clean_lines.append(line)
        else:
            # Сатрҳои техникӣ (xml, resources, шарҳҳо)
            clean_lines.append(line)

    # 5. Сабти файли тозаву соз
    with open(path_tg, 'w', encoding='utf-8') as f:
        f.write('\n'.join(clean_lines) + '\n')

    print("🚀 ✅ Заводи Мутлақ: Файли тоҷикӣ пурра табобат шуд ва сохтораш айнан мисли англисӣ шуд!")

if __name__ == "__main__":
    total_factory_reset()
