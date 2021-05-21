from time import time
import websocket, json, pprint, numpy
import config
import pandas_ta as ta
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='us')

pair = "btcusdt"
# dhm = days, hours, or minutes
dhm = "m"
# timeframe = how many days hours or minutes
timeframe = 1
SOCKET = 'wss://stream.binance.com:9443/ws/%s@kline_%dm' % (pair.lower(), timeframe)
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

def last_data(data, range):
    return data[-range:]

# establish arguments for historical data
time_per = timeframe * RSI_PERIOD
time_frame = str(timeframe)+dhm
# collect historical data, record closes for analysis
candles = client.get_historical_klines(pair.upper(),time_frame,'now')
print(len(candles))
candles = last_data(candles,20)
print(len(candles))
closes = [float(candle[4]) for candle in candles]

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    # print('received message')
    json_message = json.loads(message)
    # pprint.pprint(json_message)

    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']

    if is_candle_closed:
        while len(closes) >= RSI_PERIOD:
            closes.pop(0)
        # print("candle closed at {}".format(close))
        closes.append(float(close))
        print(len(closes))

ws = websocket.WebSocketApp(SOCKET, on_open = on_open, on_close = on_close, on_message = on_message)
ws.run_forever()