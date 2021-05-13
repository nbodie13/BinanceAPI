import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='us')

# info = client.get_account()
# balances = info['balances']
# print(balances)

prices = client.get_all_tickers()

# for price in prices:
#     print(price)

candles = client.get_historical_klines("BTCUSD", Client.KLINE_INTERVAL_15MINUTE, "1 day ago UTC")

candlesticks = []
for data in candles:
    candlestick = {
        "time": data[0] / 1000,
        "open": data[1],
        "high": data[2],
        "low": data[3],
        "close": data[4]
    }

    candlesticks.append(candlestick)

print(candlesticks)

# csvfile = open('15minutes.csv', 'w', newline='')

# candlestick_writer = csv.writer(csvfile, delimiter=',')

# for candlestick in candles:
#     # print(candlestick)

#     candlestick_writer.writerow(candlestick)

# # print(len(candles))

# csvfile.close()