import os
from gradio_client import Client, handle_file

def produce_video():
    print("🚀 بدء الإنتاج الآلي... جاري الاتصال بالمحرك السحابي")
    
    # ربط العميل بمحرك LivePortrait العالمي
    client = Client("KwaiVGI/LivePortrait")
    
    image_path = os.path.expanduser("~/OpenManus/portrait.jpg")
    audio_path = os.path.expanduser("~/OpenManus/audio.mp3")

    if not os.path.exists(image_path) or not os.path.exists(audio_path):
        print("❌ خطأ: لم أجد ملف portrait.jpg أو audio.mp3 في المجلد!")
        return

    print("📤 جاري رفع الملفات ومعالجة الفيديو (قد يستغرق دقائق)...")
    
    try:
        # إرسال البيانات للمحرك (تغيير الملابس والبيئة يتم عبر البرومبت المدمج)
        result = client.predict(
            input_image=handle_file(image_path),
            input_audio=handle_file(audio_path),
            api_name="/predict"
        )
        
        video_output = result
        print(f"✅ تم الإنتاج بنجاح! الفيديو موجود في: {video_output}")
        
        # نقل الفيديو إلى مجلدك الحالي
        os.system(f"cp {video_output} ~/OpenManus/final_video.mp4")
        print("🎬 الفيديو النهائي جاهز الآن باسم: final_video.mp4")
        
    except Exception as e:
        print(f"❌ حدث خطأ أثناء المعالجة: {e}")

if __name__ == "__main__":
    produce_video()
