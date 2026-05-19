#!/bin/bash
RUN_ID="26117599304"
echo "📡 جاري مراقبة الاختراق السحابي (تجاوز Daytona)... المهمة: $RUN_ID"

# الانتظار حتى اكتمال المهمة
gh run watch $RUN_ID

# التحقق من الحالة
STATUS=$(gh run view $RUN_ID --json conclusion -q '.conclusion')

if [ "$STATUS" == "success" ]; then
    echo "✅ تم النصر! المحرك أنتج الفيديو بنجاح."
    echo "📥 جاري سحب الفيديو لمجلد التنزيلات..."
    gh run download $RUN_ID --name video-production -D /sdcard/Download
    echo "🎉 الفيديو الآن في: /sdcard/Download"
else
    echo "❌ تعثرت المهمة مجدداً. جاري استخراج سجلات الخطأ لتحليلها..."
    gh run view $RUN_ID --log | tail -n 40
fi
