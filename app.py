from flask import Flask, render_template, send_from_directory, request, redirect
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Müşteri tasarımındaki 10 Hizmet (Galaxy Verisi)
SERVICES = [
    {"num": "01", "title": "Dubai Emlak Eğitimi", "sub": "RERA · Piyasa", "tag": "Eğitim", "depth": 0.05, "icon": '<path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'},
    {"num": "02", "title": "Hukuk & Şirket", "sub": "UAE · Free Zone", "tag": "Hukuk", "depth": 0.65, "icon": '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>'},
    {"num": "03", "title": "Kariyer Mentorluk", "sub": "Yol Haritası", "tag": "Mentorluk", "depth": 0.20, "icon": '<path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/>'},
    {"num": "04", "title": "İçerik Prodüksiyon", "sub": "4K Video · Kurgu", "tag": "Prodüksiyon", "depth": 0.75, "icon": '<polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2"/>'},
    {"num": "05", "title": "Sosyal Medya", "sub": "Meta · Google", "tag": "Pazarlama", "depth": 0.10, "icon": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>'},
    {"num": "06", "title": "Lead & CRM", "sub": "Funnel · Ödeme", "tag": "Satış", "depth": 0.55, "icon": '<polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>'},
    {"num": "07", "title": "Ekosistem Üyeliği", "sub": "Ağ · Komisyon", "tag": "Ekosistem", "depth": 0.30, "icon": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/>'},
    {"num": "08", "title": "Sertifika & Webinar", "sub": "Online · Canlı", "tag": "Sertifika", "depth": 0.85, "icon": '<rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/>'},
    {"num": "09", "title": "Partner Programı", "sub": "%50 Paylaşım", "tag": "Partner", "depth": 0.40, "icon": '<line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/>'},
    {"num": "10", "title": "Marka & Kimlik", "sub": "Görsel · Kurumsal", "tag": "Marka", "depth": 0.22, "icon": '<circle cx="12" cy="12" r="3"/><path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4"/>'},
]

# Dinamik Eğitim Verileri
COURSES = {
    "Emlak": [
        {"num": "01", "title": "Dubai Emlak Temelleri", "desc": "Dubai piyasa yapısı, RERA lisansı ve komisyon sistemi.", "tag": "Online · 8 Hafta", "level": "Temel", "price": "$299"},
        {"num": "02", "title": "Satış & Komisyon Uzmanlığı", "desc": "Müşteri yönetimi ve yüksek komisyonlu projeleri kapama.", "tag": "Online · 6 Hafta", "level": "Profesyonel", "price": "$499"},
        {"num": "03", "title": "Lüks Segment & Off-Plan", "desc": "Lüks konut ve off-plan yatırımcı yönetimi.", "tag": "Online · 5 Hafta", "level": "İleri", "price": "$699"},
        {"num": "04", "title": "Birebir Mentorluk", "desc": "Sahada aktif broker ile birebir strateji seansları.", "tag": "Canlı · 12 Hafta", "level": "Mentorluk", "price": "$1.499"},
        {"num": "05", "title": "Online Sertifika Programı", "desc": "Kendi hızında ilerle, Dubai emlak dünyasına gir.", "tag": "Self-Paced · 4 Hafta", "level": "Temel", "price": "$199"}
    ],
    "Hukuk": [
        {"num": "01", "title": "UAE Hukuk Sistemine Giriş", "desc": "Emirates hukuku ve temel yasal çerçeve.", "tag": "Online · 6 Hafta", "level": "Temel", "price": "$349"},
        {"num": "02", "title": "Şirket Kurulum & Free Zone", "desc": "Free zone vs mainland karşılaştırması ve lisans türleri.", "tag": "Online · 5 Hafta", "level": "Profesyonel", "price": "$449"},
        {"num": "03", "title": "Danışmanlık & Referral Modeli", "desc": "Türkiye'den UAE'ye müşteri yönlendirme sistemi.", "tag": "Canlı + Online · 8 Hafta", "level": "İleri", "price": "$799"}
    ]
}

@app.route('/')
def home():
    return render_template('index.html', services=SERVICES, courses=COURSES)

@app.route('/basvuru', methods=['POST'])
def basvuru():
    # Müşterinin formundan gelen verileri burada yakalıyoruz 
    return "Başvurunuz alındı! 48 saat içinde döneceğiz."

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)