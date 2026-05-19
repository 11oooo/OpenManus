#!/bin/bash
RUN_ID="26118738490"
echo "🛰️ جاري انتظار اكتمال إنتاج الفيديو السحابي... (المهمة: $RUN_ID)"

gh run watch $RUN_ID

echo "📥 جاري سحب الفيديو الناتج من السحاب..."
mkdir -p ~/OpenManus/logs
# سحب الـ Artifact الذي سميناه video-production
gh run download $RUN_ID --name video-production -D ~/OpenManus/logs

if [ -f ~/OpenManus/logs/final_video.mp4 ]; then
    echo "✅ تم النصر المؤزر!"
    cp ~/OpenManus/logs/final_video.mp4 /sdcard/Download/
    echo "🎬 الفيديو الآن في مجلد التنزيلات باسم: final_video.mp4"
else
    echo "⚠️ لم أجد الفيديو بعد. سأعرض لك السجلات لنرى أين تعثر المحرك:"
    gh run view $RUN_ID --log
fi
