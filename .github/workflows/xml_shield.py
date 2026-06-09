import re
import os

path_tg = 'TMessagesProj/src/main/res/values-tg/strings.xml'
path_en = 'TMessagesProj/src/main/res/values/strings.xml'

def ultimate_factory_restore():
    if not os.path.exists(path_tg):
        print("❌ Файл ёфт нашуд")
        return

    with open(path_tg, 'r', encoding='utf-8') as f:
        content_tg = f.read()

    content_tg = content_tg.replace('name=&quot;', 'name="')
    content_tg = re.sub(r'(&quot;>|&quot;\s*>)', '">', content_tg)
    content_tg = content_tg.replace('&quot;/>', '"/>')

    lines_tg = content_tg.split('\n')
    fixed_lines_tg = []
    
    for line in lines_tg:
        stripped = line.strip()
        if not stripped: continue
        if '<string name=' in line or '</string>' in line or '<resources>' in line or '</resources>' in line:
            fixed_lines_tg.append(line)
        else:
            if fixed_lines_tg:
                idx = len(fixed_lines_tg) - 1
                while idx >= 0 and not fixed_lines_tg[idx].strip(): idx -= 1
                if idx >= 0 and '</string>' in fixed_lines_tg[idx]:
                    fixed_lines_tg[idx] = fixed_lines_tg[idx].replace('</string>', f' {stripped}</string>')
                else:
                    fixed_lines_tg.append(line)
            else:
                fixed_lines_tg.append(line)

    tg_translations = {}
    for line in fixed_lines_tg:
        match = re.search(r'<string name="([^"]+)">([^<]*)</string>', line)
        if match:
            key, text = match.groups()
            tg_translations[key] = text
        elif re.search(r'<string name="([^"]+)"/>', line):
            key = re.search(r'<string name="([^"]+)"/>', line).group(1)
            tg_translations[key] = ""

    if os.path.exists(path_en):
        with open(path_en, 'r', encoding='utf-8') as f:
            lines_en = f.readlines()
        
        final_lines = []
        for line_en in lines_en:
            s_en = line_en.strip()
                        # ИСЛОҲ: Ин қисмро ҳамин тавр бигзор, он дароз нест ва бурида намешавад
            if (s_en.startswith('<?xml') or 
                s_en.startswith('<resources') or 
                s_en.startswith('</resources>') or 
                s_en.startswith('
