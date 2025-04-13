# app.py (Deliberately insecure for testing)
from flask import Flask
import requests  # Old version for CVE testing

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)  # Debug mode enabled (security risk!)