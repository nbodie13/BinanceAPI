import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET, tld='us')

info = client.get_account()
my_balances = info['balances']



# my_bal = []

# for d in my_balances:
#     my_bal.append([d['asset'],float(d['free'])])
# for el in my_bal:
#     print(el[0],el[1])

# ________________________________________________________________________________________________________

# status = client.get_all_orders(symbol='ADAUSD')

# print(status)

# from binance.enums import *
# order = client.create_test_order(
#     symbol='BNBBTC',
#     side=SIDE_BUY,
#     type=ORDER_TYPE_LIMIT,
#     timeInForce=TIME_IN_FORCE_GTC,
#     quantity=100,
#     price='0.01158')

# print(order)
# test = my_balances

# for balances in my_balances
#     balance_writer.writerow(balances)

print(my_balances)


# for candlestick in candles:
#     # print(candlestick)

#     candlestick_writer.writerow(candlestick)

# # print(len(candles))

# csvfile.close()