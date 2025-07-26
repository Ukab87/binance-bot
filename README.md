1. Binance Webhook Trading Bot

This bot allows you to **automatically place real trades on Binance** by simply sending a webhook with trading instructions (like `buy BTCUSDT`). It's fast, secure, and can be deployed to the cloud or run locally.

---

Features

- ✅ Place **real market orders** via webhook
- ✅ Simple **JSON payload format**
- ✅ Built-in **security token check**
- ✅ Ready for **Render cloud deployment**
- ✅ Supports **local development** with `.env` for API keys

---

Files Included

| File               | Purpose                                          |
|--------------------|--------------------------------------------------|
| `app.py`           | Main Python server that listens for webhooks     |
| `requirements.txt` | Python dependencies                              |
| `render.yaml`      | Render.com deployment config                     |
| `.gitignore`       | Prevents secret files like `.env` from uploading |
| `README.md`        | This instruction file                            |

---

How to Use This Bot

Clone the Project

```bash
git clone https://github.com/YOUR_USERNAME/binance-bot.git
cd binance-bot
2. 🔐 Create Your .env File

2. Create a file named .env in the project folder with the following content:

.env

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
WEBHOOK_TOKEN=your_secure_token_here

You can get your API key from Binance API Management.

3. Run Locally (for Testing)

Make sure Python is installed.

bash

pip install -r requirements.txt
python app.py


The bot will run at:
http://localhost:5000/webhook

4. Deploy to Render (Live Server)
Already included: render.yaml for automatic deployment

Go to Render

Click “New Web Service”

Connect your GitHub repo

Render auto-detects render.yaml and deploys your bot

Add your .env variables under "Environment"

5. Webhook Usage
Webhook Endpoint
POST requests only


https://your-deployed-url.com/webhook?token=your_secure_token_here

6. JSON Payload Format
Send the webhook with a JSON body:

json

{
  "action": "buy",
  "symbol": "BTCUSDT",
  "price": 29100,
  "time": "2025-07-26T08:03:00Z"
}

action: buy or sell

symbol: Binance symbol like BTCUSDT

price: Used for logging (not for limit orders)

time: Optional timestamp

7. Security
This bot uses a token-based protection to avoid unauthorized access.

You must include ?token=your_token in the URL or set up the header if required.

Keep your .env file safe and never commit it.

8. Notes: 
Make sure your Binance API key has "Enable Spot & Margin Trading" permission.

Do not share your deployed URL or webhook token publicly.