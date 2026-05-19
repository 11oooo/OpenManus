import requests
import json

def start_video_ai():
    print("🚀 جاري الاتصال بسيرفرات الإنتاج العالمي...")
    
    # إعدادات المحرك
    api_key = "946e5d64-edb7-4379-a4a5-3f8adf0b6030"
    url = "https://api.sambanova.ai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # الطلب الاحترافي الذي تريده
    prompt = "I have a portrait image and an audio file. Act as an AI Video Director: Create a video with perfect lip-sync. Change clothing and backgrounds (stage, studio, nature) every 5 seconds. Maintain facial consistency. Provide the API command to execute this on a video generation engine."

    data = {
        "model": "Meta-Llama-3.3-70B-Instruct",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=60)
        result = response.json()
        print("\n✅ تم استلام خطة العمل من المخرج الرقمي:")
        print(result['choices'][0]['message']['content'])
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")

if __name__ == "__main__":
    start_video_ai()
