from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Eğitmen ve Eğitim Veri Kümesi 
INSTRUCTORS = [
    {
        "id": 1,
        "name": "Ahmet Yılmaz",
        "title": "Senior Broker",
        "level": "K5",
        "category": "Emlak",
        "tags": ["#Dubai", "#LüksKonut"],
        "intro": "Dubai premium segmentinde 10 yıllık deneyim.",
        "image": "https://via.placeholder.com/300", # Gerçek fotolarla değiştirilecek
        "courses": [
            {"title": "Lüks Konut Satış Stratejileri", "price": "1500 AED", "type": "Video Kurs", "link": "https://gumroad.com/example1"},
            {"title": "Yatırımcı İlişkileri Yönetimi", "price": "2000 AED", "type": "Mentorluk", "link": "https://gumroad.com/example2"}
        ]
    },
    {
        "id": 2,
        "name": "Canan Demir",
        "title": "Şirket Kurulum Uzmanı",
        "level": "H2",
        "category": "Hukuk",
        "tags": ["#FreeZone", "#Setup"],
        "intro": "Mainland ve Free Zone kurulum süreçlerinde tam destek.",
        "image": "https://via.placeholder.com/300",
        "courses": [
            {"title": "Dubai'de Şirket Kurma Rehberi", "price": "900 AED", "type": "Video Kurs", "link": "https://gumroad.com/example3"}
        ]
    }
]

@app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/egitmenler')
def egitmenler():
    # Filtreleme mantığı için hazırlık
    category = request.args.get('category')
    filtered_instructors = INSTRUCTORS
    
    if category:
        filtered_instructors = [i for i in INSTRUCTORS if i['category'] == category]
        
    return render_template('egitmenler.html', instructors=filtered_instructors)

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)