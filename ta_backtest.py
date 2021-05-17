import numpy, talib, os, math
from numpy import asmatrix, genfromtxt, NaN

#import data and get closing price; comment out if pulling functions from this file.
dataset = 'data/15minutes.csv'
if not os.path.isfile(dataset):
    no_file = "File '%s' not found. Please try again." % dataset
    print(no_file)
else:
    my_data = genfromtxt(dataset,delimiter=',')
    close = my_data[:,4]

####### SCALE DATA #######
def scale_data(dataset, scale_factor):
    # Scale the dataset if you don't want to use the given data timeframe
    if scale_factor > len(dataset):
        return("Scale factor too great, please reduce")
    if scale_factor != 1:
        j = 0
        new_data = []
        for val in dataset:
            rem = j % scale_factor
            j += 1
            if rem == 0:
                new_data.append(val)
        dataset = new_data
    return dataset

####### Simple Moving Average #######
def sma(dataset, period = 9, scale_factor = 1):
    # Scale the dataset if you don't want to use the give data timeframe
    dataset = scale_data(dataset,scale_factor)

    # Error if period is too large
    if period > len(dataset):
        return("Period too large. Reduce period or gather more data.")

    # Calculate the simple moving average of dataset
    i = 0
    sma = []
    this_window = []
    while i < period-1:
        sma.append(math.nan)
        this_window.append(dataset[i])
        i += 1
    while i < len(dataset):
        this_window.append(dataset[i])
        sma.append(sum(this_window)/period)
        this_window.pop(0)
        i += 1
    return sma
    # Get results of SMA function
    # sma_ = sma(close,9)
    # print(sma_)
    # print(len(sma_))

####### Exponential Moving Average #######
def ema(dataset, period = 10, scale_factor=1):
 # Scale the dataset if you don't want to use the give data timeframe
    dataset = scale_data(dataset,scale_factor)

    # Error if period is too large
    if period > len(dataset):
        return("Period too large. Reduce period or gather more data.")

    # Calculate the exponential moving average of dataset
    i = 0
    ema = []
    this_window = []
    multiplier = 2/(period+1)
    while i < period-1:
        ema.append(math.nan)
        this_window.append(dataset[i])
        i += 1
    if i == period-1:
        this_window.append(dataset[i])
        ema.append(sum(this_window)/period)
        i += 1
    while i >= period and i < len(dataset):
        ema.append((dataset[i]-ema[-1])*multiplier+ema[-1])
        i += 1
    return ema

    # Get results of EMA function
    # ema_ = ema(close,10)
    # print(ema_)
    # print(len(ema_))

####### Moving Average Convergence Divergence #######
def macd(dataset, period = 9, fastlength = 12, slowlength = 26, scale_factor = 1):

    # Scale the dataset if you don't want to use the give data timeframe
    dataset = scale_data(dataset,scale_factor)

    # Error if period is too large
    if period > len(dataset):
        return("Period too large. Reduce period or gather more data.")
    
    i = 0
    dif = []
    ema_d = []
    ema_fast = ema(dataset,fastlength)
    ema_slow = ema(dataset,slowlength)
    while i < len(dataset):
        if i >= slowlength:
            dif.append(ema_fast[i] - ema_slow[i])
        i += 1
    ema_d = ema(dif,period)
    print(ema_d)
    return dif, ema_d

    # Get results of EMA function
    # macd_ = macd(close)
    # print(macd_[1])
    # print(len(ema_))

