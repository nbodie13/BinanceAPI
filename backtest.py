import pandas as pd
import pandas_ta as ta
import config
import numpy, talib, os, math

class Account:
    api_key = config.API_KEY
    api_secret = config.API_SECRET
    balance = 100000
    
dataset = 'data/15minutes.csv'
if not os.path.isfile(dataset):
    no_file = "File '%s' not found. Please try again." % dataset
    print(no_file)
else:
    df = pd.read_csv(dataset,index_col=0,
                          names=['open','high','low','close','volume','close time',
                                 'quote asset vol','no. of trades','taker asset vol',
                                 'taker quot asset vol','ignore'])
    # print(df)
    my_data = pd.concat([df.open,df.high,df.low,df.close,df.volume], axis=1)

# my_data['sma'] = my_data.ta.sma(length=10)
# my_data['rsi'] = my_data.ta.rsi(length=10)
# print(my_data)


##########   WORKING BABY   ####################
def strat():
    CustomStrategy = ta.Strategy(
        name="Momo and Volatility",
        description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
        ta=[
            {"kind": "sma", "length": 11},
            {"kind": "sma", "length": 20},
            {"kind": "bbands", "length": 20},
            {"kind": "rsi"},
            {"kind": "macd", "fast": 8, "slow": 21},
            {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
        ]
    )
# To run your "Custom Strategy"
    my_data.ta.strategy(CustomStrategy)
    print(my_data)

if __name__ == '__main__':
    strat()