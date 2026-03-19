from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# PDF'deki Hizmetler ve Eğitim Verileri [cite: 37-48]
SERVICES = [
    {
        "title": "Dubai Emlak Eğitimi",
        "desc": "Piyasa yapısı, RERA lisansı ve Komisyon sistemi.",
        "tag": "Emlak"
    },
    {
        "title": "Hukuk & Şirket Kurulum",
        "desc": "Mainland/Free Zone yapıları ve sözleşme yönetimi.",
        "tag": "Hukuk"
    },
    {
        "title": "Kariyer Mentorluk",
        "desc": "Profil analizi ve Dubai iş ağına giriş stratejileri.",
        "tag": "Kariyer"
    }
]

@app.route('/')
def home():
    # index.html artık 'templates/' içinde olduğu için render_template kullanılır
    return render_template('index.html', services=SERVICES)

@app.route('/egitmenler')
def egitmenler():
    # Bir sonraki adımda yapacağımız sayfa
    return render_template('egitmenler.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)