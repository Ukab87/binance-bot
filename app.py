from flask import Flask, request, jsonify
import hmac, hashlib
import requests
import os
from dotenv import load_dotenv
import os
app = Flask(__name__)


load_dotenv()
# Binance credentials from environment
API_KEY = os.environ.get("BINANCE_API_KEY")
API_SECRET = os.environ.get("BINANCE_SECRET")
if not API_KEY or not API_SECRET:
    raise ValueError("Binance API key/secret not set. Check your .env file.")
@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
    except Exception as e:
        return jsonify({"error": f"Failed to parse JSON: {str(e)}"}), 400

    if not data:
        return jsonify({"error": "No JSON received"}), 400

    print("Received:", data)

    if "action" not in data:
        return jsonify({"error": "Missing 'action' key"}), 400

    action = data["action"]
    symbol = data["symbol"].replace("BINANCE:", "").replace("/", "").lower()
    price = float(data["price"])

    if action == "buy":
        return market_order(symbol, "BUY")
    elif action == "sell":
        return market_order(symbol, "SELL")
    else:
        return jsonify({"error": "Invalid action"}), 400
def market_order(symbol, side):
    print(f"✅ MOCK ORDER: {side} {symbol}")
    return {"status": "success", "symbol": symbol, "side": side}
#def market_order(symbol, side):
    #url = "https://api.binance.com/api/v3/order"
    #headers = {
    #    'X-MBX-APIKEY': API_KEY
    #}

    payload = {
        'symbol': symbol.upper(),
        'side': side,
        'type': 'MARKET',
        'quantity': 0.01  # placeholder
    }

    # You must sign it!
    import time
    import urllib.parse

    payload['timestamp'] = int(time.time() * 1000)
    query_string = urllib.parse.urlencode(payload)
    signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    payload['signature'] = signature

    r = requests.post(url, headers=headers, params=payload)

    return jsonify({"status": "sent", "response": r.json()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
