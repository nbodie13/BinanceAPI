import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='us')

# info = client.get_account()
# balances = info['balances']
# print(balances)

# prices = client.get_all_tickers()

# for price in prices:
#     print(price)

# candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 day ago UTC")
# candles = client.get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1HOUR,"1 Jan, 2015","now")
# candles = client.get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1DAY,"2015-01-01T00:00:00.000Z")
candles = client.get_historical_klines("BTCUSDT",Client.KLINE_INTERVAL_1DAY,"1 Jan, 2020","12 Jul, 2020")

csvfile = open('1day.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

for candlestick in candles:
    # print(candlestick)
    candlestick[0] = candlestick[0] / 1000
    # dividing by 1000 puts the unix time in seconds, not milliseconds for backtrader
    candlestick_writer.writerow(candlestick)

# print(len(candles))

csvfile.close()