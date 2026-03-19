from flask import Flask, render_template, send_from_directory, request, redirect
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ... SERVICES ve INSTRUCTORS verileri aynı kalabilir ...

@app.route('/')
def home():
    return render_template('index.html', services=SERVICES)

@app.route('/egitimler')
def egitimler():
    # FILTRELEME MANTIĞI EKLENDİ [cite: 66, 67]
    category_filter = request.args.get('category')
    if category_filter:
        filtered_list = [i for i in INSTRUCTORS if i['category'] == category_filter]
    else:
        filtered_list = INSTRUCTORS
    return render_template('egitimler.html', instructors=filtered_list)

@app.route('/basvuru', methods=['POST'])
def basvuru():
    # Form verileri burada yakalanır [cite: 95-102]
    # Gelecekte buraya e-posta gönderme kodu eklenebilir.
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