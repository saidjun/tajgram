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

    # 2. Ҷамъоварии тарҷумаҳо бо Regex-и калон (ҳатто матнҳои бисёрсатраро мегирад)
    tg_dict = {}
    
    # Ҷустуҷӯи тегҳои муқаррарӣ ва бисёрсатра <string name="...">матн</string>
    pattern_full = r'<string\s+name="([^"]+)">([\s\S]*?)</string>'
    for match in re.finditer(pattern_full, content_tg):
        key = match.group(1)
        value = match.group(2)
        tg_dict[key] = value

    # Ҷустуҷӯи тегҳои холӣ <string name="..."/>
    pattern_empty = r'<string\s+name="([^"]+)"/>'
    for match in re.finditer(pattern_empty, content_tg):
        key = match.group(1)
        tg_dict[key] = ""

    # 3. Бозсозии сохтор дар асоси шаблони англисӣ (Айнан мисли заводӣ)
    with open(path_en, 'r', encoding='utf-8') as f:
        en_content = f.read()

    # Мо файли англисиро хат ба хат коркард мекунем
    en_lines = en_content.splitlines()
    final_lines = []
    
    for line in en_lines:
        # Пайдо кардани калид дар сатри англисӣ
        match_key = re.search(r'<string\s+name="([^"]+)"', line)
        
        if match_key:
            key = match_key.group(1)
            # Агар тарҷумаи тоҷикӣ дошта бошем, онро мегузорем (бо нигоҳ доштани сохтори бисёрсатра)
            if key in tg_dict:
                # Агар сатри англисӣ холӣ маҳкам шуда бошад ва тарҷумаи мо ҳам холӣ бошад
                if '/>' in line and tg_dict[key] == "":
                    final_lines.append(f'    <string name="{key}"/>')
                else:
                    final_lines.append(f'    <string name="{key}">{tg_dict[key]}</string>')
            else:
                # Агар тарҷума набошад, худи сатри англисиро мегузорем
                final_lines.append(line)
        else:
            # Сатрҳое, ки тег надоранд (масалан <?xml>, <resources>, шарҳҳо ва ғайра)
            final_lines.append(line)

    # 4. Сабти ниҳоӣ ба файли тоҷикӣ
    with open(path_tg, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_lines) + '\n')
        
    print("✅ Заводи комил: Ҳамаи калимаҳо ва калидҳо 100% ҷобаҷо шуданд!")

if __name__ == "__main__":
    ultimate_factory_restore()
