#!/bin/bash
# Ислоҳи комил ва заводии strings.xml
FILE_PATH="TMessagesProj/src/main/res/values-tgl/strings.xml"

# 1. Санҷиши мавҷудияти файл
if [ ! -f "$FILE_PATH" ]; then
    echo "❌ Файл ёфт нашуд: $FILE_PATH"
    exit 1
fi

# 2. Ислоҳи аломатҳои XML (Тартиби бехатар)
sed -i '' 's/&/&amp;/g' "$FILE_PATH"
sed -i '' 's/</&lt;/g' "$FILE_PATH"
sed -i '' 's/>/&gt;/g' "$FILE_PATH"
sed -i '' 's/"/&quot;/g' "$FILE_PATH"
sed -i '' "s/'/&apos;/g" "$FILE_PATH"

# 3. Техникаи фоизҳо (Пешгирии хатои AAPT2)
# Фоизҳои танҳо -> %% ва фоизҳои коди -> %1$s
sed -i '' 's/%/%%/g' "$FILE_PATH"
sed -i '' -E 's/%%([0-9]\$[ds])/%\1/g' "$FILE_PATH"

# 4. Назорати ниҳоӣ (Техникӣ)
OPEN=$(grep -o "<string" "$FILE_PATH" | wc -l)
CLOSE=$(grep -o "</string>" "$FILE_PATH" | wc -l)

if [ "$OPEN" -eq "$CLOSE" ] && [ "$OPEN" -gt 0 ]; then
    echo "✅ Файл бомуваффақият аз 'Завод' гузашт. $OPEN сатр ислоҳ шуд."
else
    echo "❌ ХАТАР: Сохтор вайрон аст! (Кушода: $OPEN, Пӯшида: $CLOSE)"
    exit 1
fi
