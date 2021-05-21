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
    my_data = pd.read_csv(dataset,index_col=0,
                          names=['timestamp','open','high','low','close','vol','close time',
                                 'quote asset vol','no. of trades','taker asset vol',
                                 'taker quot asset vol','ignore'])
    print(my_data)