from flask import Flask, request, jsonify
from binance.client import Client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
WEBHOOK_TOKEN = os.getenv("WEBHOOK_TOKEN")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
app = Flask(__name__)

@app.route('/')
def home():
    return 'Binance Webhook Bot is running ✅'

@app.route('/webhook', methods=['POST'])
def webhook():
    token = request.args.get('token')
    if token != WEBHOOK_TOKEN:
        return jsonify({'error': 'Unauthorized'}), 401

    try:
        data = request.get_json(force=True)
        action = data.get("action", "").lower()
        symbol = data.get("symbol", "").upper()
        price = float(data.get("price"))
        time_str = data.get("time")

        if action not in ["buy", "sell"]:
            return jsonify({'error': 'Invalid action'}), 400

        order = client.create_order(
            symbol=symbol,
            side=Client.SIDE_BUY if action == "buy" else Client.SIDE_SELL,
            type=Client.ORDER_TYPE_MARKET,
            quantity=0.001  # ⚠️ Replace with dynamic sizing or client spec
        )

        print(f"Executed {action.upper()} for {symbol} at {datetime.utcnow()}")

        return jsonify({"side": action.upper(), "status": "success", "symbol": symbol.lower()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
