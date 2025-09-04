import requests
import os

# --- الإعدادات ---
# غيّر اسم المولد هنا إلى الذي تريده
GENERATOR_NAME = "fantasy-character" 
# اسم الملف الذي سيتم حفظ النتائج فيه
OUTPUT_FILE = "latest_result.txt"

def fetch_and_save():
    """
    تجلب نتيجة جديدة من Perchance وتحفظها في ملف.
    """
    print(f"Fetching a new result from the '{GENERATOR_NAME}' generator...")
    
    try:
        url = f"https://perchance.org/api/generateList.php?generator={GENERATOR_NAME}&count=1"
        response = requests.get(url, timeout=15)
        response.raise_for_status() # التأكد من عدم وجود خطأ
        
        data = response.json()
        
        if data and len(data) > 0:
            result = data[0]
            print(f"Success! Result: {result}")
            
            # كتابة النتيجة في الملف
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"Result saved to {OUTPUT_FILE}")
            
        else:
            print("No results returned from the generator.")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_save()
