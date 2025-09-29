from flask import Flask, request
import requests

app = Flask(__name__)

# 🔹 Your Telegram bot details
TELEGRAM_TOKEN = "8256397498:AAFe7FCI03ID-5gMRSq2p6kqmTfbeCIdTKE"
CHAT_ID = "6565944957"   # Replace with your actual chat/group ID

# ✅ Health check route
@app.route('/')
def home():
    return "✅ TradingView → Telegram bot is running!"

# 🔹 Webhook route for TradingView alerts
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()  # JSON payload from TradingView
        print("Received alert:", data)

        # Build message
        message = (
            f"📢 TradingView Alert\n"
            f"Symbol: {data.get('symbol', 'N/A')}\n"
            f"Signal: {data.get('signal', 'N/A')}\n"
            f"Price: {data.get('price', 'N/A')}"
        )

        # Send to Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        r = requests.post(url, json=payload)

        if r.status_code == 200:
            return "ok", 200
        else:
            return f"Telegram Error: {r.text}", 500

    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


