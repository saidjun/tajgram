import re, os

# Ин ҷо роҳи файлро ба `'TMessagesProj/src/main/res/values-tg/strings.xml'`-и худ иваз кун, агар папкааш дигар бошад
path = 'TMessagesProj/src/main/res/values-tg/strings.xml'

def shield_xml():
    if not os.path.exists(path):
        print(f"❌ Файл ёфт нашуд: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Муҳофизати кодҳои заводӣ (Placeholders)
    ph = {}
    def hide(m):
        k = f'___PH{len(ph)}___'
        ph[k] = m.group(0)
        return k
    c = re.sub(r'%[0-9]*\$?[sdf]|\\n|\\t', hide, c)

    # 2. Ислоҳи синтаксис (XML Safe Mode)
    c = re.sub(r'&(?!amp;|quot;|apos;|lt;|gt;)', '&amp;', c)
    c = c.replace("'", "&apos;").replace('"', "&quot;")

    # 3. Баргардонидани кодҳои заводӣ
    for k, v in ph.items():
        c = c.replace(k, v)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("✅ XML Factory Reset: Ислоҳ бо муваффақият анҷом ёфт!")

if __name__ == "__main__":
    shield_xml()
