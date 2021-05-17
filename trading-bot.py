import websocket, json, pprint

pair = 'btcusdt'
timeframe = '1m'
SOCKET = 'wss://stream.binance.com:9443/ws/%s@kline_%s' % (pair, timeframe)

closes = []
i = 0

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
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)
        i += 1
        if i > 20:
            closes.pop(0)

ws = websocket.WebSocketApp(SOCKET, on_open = on_open, on_close = on_close, on_message = on_message)
ws.run_forever()