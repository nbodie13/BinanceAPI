from time import time
from binance.enums import KLINE_INTERVAL_1MINUTE
import websocket, json, pprint, talib, numpy
import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='us')

pair = 'btcusdt'
timeframe = 1
SOCKET = 'wss://stream.binance.com:9443/ws/%s@kline_%dm' % (pair, timeframe)
kline_int = 'Client.KLINE_INTERVAL_%dMINUTE' % (timeframe)
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

# minutes = str(timeframe*RSI_PERIOD)
# print(minutes)
candles = client.get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1MINUTE,"14 minutes ago")
print(candles)
closes = []

# def on_open(ws):
#     print('opened connection')

# def on_close(ws):
#     print('closed connection')

# def on_message(ws, message):
#     # print('received message')
#     json_message = json.loads(message)
#     # pprint.pprint(json_message)

#     candle = json_message['k']
#     is_candle_closed = candle['x']
#     close = candle['c']

#     if is_candle_closed:
#         # print("candle closed at {}".format(close))
#         closes.append(float(close))
#         print(closes)

#         if len(closes) >= 20:
#             closes.pop(0)

# ws = websocket.WebSocketApp(SOCKET, on_open = on_open, on_close = on_close, on_message = on_message)
# ws.run_forever()