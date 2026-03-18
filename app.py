from flask import Flask, send_from_directory
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def home():
    # index.html'i ana dizinden servis et [cite: 46]
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(BASE_DIR, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)