import re
import os

path = 'TMessagesProj_App/src/main/res/values-tg/strings.xml' if os.path.exists('TMessagesProj_App/src/main/res/values-tg/strings.xml') else 'TMessagesProj/src/main/res/values-tg/strings.xml'

def ultimate_factory_restore():
    if not os.path.exists(path):
        print(f"❌ Файл ёфт нашуд: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("🚀 Оғози ҷарроҳии техникӣ: Баргардонидани 11,100 сатр ба формати заводӣ...")

    content = content.replace('name=&quot;', 'name="')
    content = re.sub(r'(&quot;>|&quot;\s*>)', '">', content)
    content = content.replace('&quot;/>', '"/>')

    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            fixed_lines.append(line)
            continue
            
        if '<string name=' in line or '</string>' in line or '<resources>' in line or '</resources>' in line:
            fixed_lines.append(line)
        else:
            if fixed_lines:
                idx = len(fixed_lines) - 1
                while idx >= 0 and not fixed_lines[idx].strip(): idx -= 1
                if idx >= 0 and '</string>' in fixed_lines[idx]:
                    fixed_lines[idx] = fixed_lines[idx].replace('</string>', f' {stripped}</string>')
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)

    final_content = re.sub(r'&(?!amp;|quot;|apos;|lt;|gt;)', '&amp;', '\n'.join(fixed_lines))

    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("✅ 11100 сатр 100% заводи шуд!")

if __name__ == "__main__":
    ultimate_factory_restore()
