from flask import Flask, jsonify, render_template_string
from model.predict import predict
from data.binance_client import fetch_candles
import os

app = Flask(__name__)
TEMPLATE = """<!doctype html><title>Crypto AI Bot</title><h1>Crypto AI Bot — Dashboard (simulação)</h1>
<p>Symbol: {{symbol}}</p><p>Model prediction: {{pred}}</p><h3>Últimos closes</h3><pre>{{closes}}</pre>"""

@app.route('/')
def index():
    symbol = os.getenv('DEFAULT_SYMBOL','BTC/USDT')
    pred = predict()
    df = fetch_candles(symbol, timeframe='5m', limit=20)
    closes = df['close'].tolist()
    return render_template_string(TEMPLATE, symbol=symbol, pred=pred, closes=closes)

@app.route('/api/predict')
def api_predict():
    return jsonify(predict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
