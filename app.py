from flask import Flask, render_template, send_from_directory, request, redirect
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SERVICES = [
    {"title": "Dubai Emlak Eğitimi", "desc": "Piyasa yapısı, RERA lisansı ve Komisyon sistemi. [cite: 37, 38]", "tag": "Emlak"},
    {"title": "Hukuk & Şirket Kurulum", "desc": "Mainland/Free Zone yapıları ve sözleşme yönetimi. [cite: 39, 40]", "tag": "Hukuk"},
    {"title": "Kariyer Mentorluk", "desc": "Profil analizi ve Dubai iş ağına giriş stratejileri. [cite: 41, 42]", "tag": "Kariyer"},
    {"title": "Sertifika Programları", "desc": "Tamamlama belgesiyle profilini güçlendir. [cite: 44, 45]", "tag": "Eğitim"},
    {"title": "Ekosistem Üyeliği", "desc": "Kapalı topluluk ve komisyon hesabına erişim. [cite: 47, 48]", "tag": "Network"},
    {"title": "Ücretsiz Webinar", "desc": "Canlı oturumlarla Dubai'den haberler. [cite: 49, 50]", "tag": "Canlı"}
]

INSTRUCTORS = [
    {
        "name": "Ahmet Yılmaz",
        "title": "Senior Broker",
        "level": "K5",
        "category": "Emlak",
        "image": "https://via.placeholder.com/400x500", # EKSİK OLAN RESİM EKLENDİ
        "intro": "Dubai premium segmentinde, lüks konut satışı ve yatırımcı yönetimi uzmanı.",
        "courses": [
            {"title": "Dubai'de Gayrimenkul Yatırımı", "price": "1.250 AED", "type": "Video Kurs", "link": "#"},
            {"title": "Lüks Konut Portföy Yönetimi", "price": "2.500 AED", "type": "Mentorluk", "link": "#"}
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html', services=SERVICES)

@app.route('/egitimler')
def egitimler():
    # FİLTRELEME MANTIĞI EKLENDİ
    category_filter = request.args.get('category')
    if category_filter:
        filtered_list = [i for i in INSTRUCTORS if i['category'] == category_filter]
    else:
        filtered_list = INSTRUCTORS
    return render_template('egitimler.html', instructors=filtered_list)

@app.route('/basvuru', methods=['POST'])
def basvuru():
    # Form verilerini burada yakalayabiliriz (Şimdilik ana sayfaya dönüyor)
    return redirect('/')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)