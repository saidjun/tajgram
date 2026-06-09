import re
import os

path_tg = 'TMessagesProj/src/main/res/values-tg/strings.xml'
path_en = 'TMessagesProj/src/main/res/values/strings.xml'

def real_factory_shield():
    if not os.path.exists(path_tg) or not os.path.exists(path_en):
        print("❌ Файлҳо ёфт нашуданд!")
        return

    # 1. Хондани файли тоҷикии ту
    with open(path_tg, 'r', encoding='utf-8') as f:
        content_tg = f.read()

    # Тозакунии аввалияи аломатҳои кова дар тегҳо
    content_tg = content_tg.replace('name=&quot;', 'name="').replace('&quot;>', '">').replace('&quot;/>', '"/>')
    content_tg = content_tg.replace('name=&amp;quot;', 'name="').replace('&amp;quot;>', '">')

    # 2. Ҷамъоварии тарҷумаҳои тоҷикӣ ба луғат (Бо нигоҳ доштани ситорачаҳо ва аломатҳо)
    tg_database = {}
    
    # Пайдо кардани ҳамаи тегҳои муқаррарӣ ва бисёрсатра
    pattern_full = r'<string\s+name="([^"]+)">([\s\S]*?)</string>'
    for match in re.finditer(pattern_full, content_tg):
        tg_database[match.group(1)] = match.group(2)

    # Пайдо кардани тегҳои холӣ
    pattern_empty = r'<string\s+name="([^"]+)"/>'
    for match in re.finditer(pattern_empty, content_tg):
        tg_database[match.group(1)] = ""

    # 3. Хондани шаблони Англисӣ (ки 100 функсияи навро дорад)
    with open(path_en, 'r', encoding='utf-8') as f:
        en_content = f.read()

    en_lines = en_content.splitlines()
    clean_output = []

    # 4. Рӯйбардории сохтор ДАҚИҚ МИСЛИ АНГЛИСӢ
    for line in en_lines:
        match_key = re.search(r'name="([^"]+)"', line)
        
        if match_key:
            key = match_key.group(1)
            
            # Агар тарҷумаи тоҷикӣ дошта бошем, онро мечаспӯнем
            if key in tg_database:
                if '/>' in line and tg_database[key] == "":
                    clean_output.append(f'    <string name="{key}"/>')
                else:
                    clean_output.append(f'    <string name="{key}">{tg_database[key]}</string>')
            else:
                # Агар функсияи нав бошад ва дар тоҷикӣ набошад, сатри англисиро мемонем
                clean_output.append(line)
        else:
            # Сатрҳои техникӣ ва шарҳҳо
            clean_output.append(line)

    # 5. Сабти файл бо сохтори заводии 100% соз
    with open(path_tg, 'w', encoding='utf-8') as f:
        f.write('\n'.join(clean_output) + '\n')

    print("🚀 ✅ Заводи Мутлақ: 100 функсияи нав илова шуданд ва сохтори файл тасҳеҳ шуд!")

if __name__ == "__main__":
    real_factory_shield()
