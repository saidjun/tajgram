import re
import os

# Роҳи файл ба таври автоматикӣ санҷида мешавад
path = 'TMessagesProj/src/main/res/values-tg/strings.xml'
if not os.path.exists(path):
    path = 'TMessagesProj_App/src/main/res/values-tg/strings.xml'

def shield_xml():
    if not os.path.exists(path):
        print(f"❌ Файл ёфт нашуд: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    fixed_lines = []
    for line in lines:
        # Агар сатр теги хулоса ё resources бошад, ба он даст намезанем
        if '<resources>' in line or '</resources>' in line or '
