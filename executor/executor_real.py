import os, time
import ccxt
from model.predict import predict
from config import settings

MODE = settings.MODE
SYMBOL = settings.DEFAULT_SYMBOL
SIZE = settings.DEFAULT_ORDER_SIZE

def get_exchange():
    api = settings.BINANCE_API_KEY
    sec = settings.BINANCE_API_SECRET
    if settings.BINANCE_TESTNET:
        return ccxt.binance({'apiKey': api, 'secret': sec, 'enableRateLimit': True,
                             'urls': {'api': 'https://testnet.binance.vision/api'}})
    return ccxt.binance({'apiKey': api, 'secret': sec, 'enableRateLimit': True})

def place_market_order(side, amount):
    if MODE == 'SIMULATION':
        print(f"[SIM] Would place {side} {amount} {SYMBOL}")
        return {'status':'simulated','side':side,'amount':amount}
    ex = get_exchange()
    try:
        market = ex.create_market_order(SYMBOL, side.lower(), amount)
        return market
    except Exception as e:
        print('Order failed:', e)
        return {'error':str(e)}

def main_loop():
    print('Executor started in', MODE, 'mode for', SYMBOL)
    while True:
        pred = predict()
        if 'prob_up' in pred:
            p = pred['prob_up']
            print('Model prob up:', p)
            if p > 0.6:
                place_market_order('BUY', SIZE)
            elif p < 0.4:
                place_market_order('SELL', SIZE)
            else:
                print('No confident signal.')
        else:
            print('No model available.')
        time.sleep(60)

if __name__ == '__main__':
    main_loop()
