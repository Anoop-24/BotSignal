from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8256397498:AAFe7FCI03ID-5gMRSq2p6kqmTfbeCIdTKE"
CHAT_ID = "8256397498"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = f"📢 TradingView Alert:\n{data}"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, json=payload)
    
    return "ok", 200

if __name__ == '__main__':
    app.run(port=5000)
