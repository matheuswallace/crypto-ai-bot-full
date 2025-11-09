DEPLOY GUIDE (Railway)

1. Push this repository to GitHub.
2. Go to https://railway.app and 'New Project' -> 'Deploy from GitHub' and select this repo.
3. Add the following Environment Variables in Railway:
   - BINANCE_API_KEY
   - BINANCE_API_SECRET
   - BINANCE_TESTNET=true
   - MODE=SIMULATION
   - DEFAULT_SYMBOL=BTC/USDT
   - DEFAULT_ORDER_SIZE=0.001
   - TELEGRAM_BOT_TOKEN (optional)
   - TELEGRAM_CHAT_ID (optional)
   - MODEL_PATH=models/model.joblib
   - OPENAI_API_KEY (optional)
4. Deploy. Railway will install requirements and run the Procfile commands (worker + web).
5. Monitor logs. Train model: `python model/train.py` (can be run locally or as one-off job).
