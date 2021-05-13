import pyotp
import robin_stocks.robinhood as rh
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def RSI(xlst):
    # Relative Strength Index 0-100
    # rsi < 30 : oversold
    # rsi > 70 : overbought
    changes = [(xlst[i][1]-xlst[i][0])/xlst[i][0] for i in range(0,len(xlst))]
    gains = []
    losses = []
    for x in changes:
        if x > 0:
            gains.append(x)
        elif x < 0:
            losses.append(x)
        else:
            gains.append(x)
            losses.append(x)
    avgGain = sum(gains)/len(gains)
    avgLoss = sum(losses)/len(losses)*-1 # make positive

    rsi = round(100 - 100/(1 + avgGain/avgLoss),2)
    return rsi


def SO(xlst):
    # Stochastic Oscillator 0-100
    # so < 20 : overselling
    # so > 80 : overbuying
    C = xlst[-1][-1] # most recent close price
    L = min(xlst[:,1])
    H = max(xlst[:,0])

    so = round(100*(C-L)/(H-L),2)
    return so


def WR(xlst):
    # Williams %R 0-(-100)
    # "inverse" of SO
    # wr < -80 : oversold
    # so > -20 : overbought
    C = xlst[-1][-1] # most recent close price
    L = min(xlst[:,1])
    H = max(xlst[:,0])

    wr = round(-100*(H-C)/(H-L),2)
    return wr


def getLAST14(x):
    LAST14 = x[-14:]

    #Relative Strength Index
    LAST14OC = np.array([[float(LAST14[i]['open_price']), float(LAST14[i]['close_price'])] for i in range(0,14)])
    LAST14RSI = RSI(LAST14OC[:,0:2])
    
    #Stochastic Oscillator
    LAST14COC = np.array([[float(LAST14[i]['high_price']), float(LAST14[i]['low_price']), float(LAST14[i]['close_price'])] for i in range(0,14)])
    LAST14SO = SO(LAST14COC)

    #Williams R%
    LAST14WR = WR(LAST14COC)

    return LAST14RSI, LAST14SO, LAST14WR


def fixTime(x):
    x = datetime.fromisoformat(x[:-1])
    x.strftime('%Y-%m-%d %H:%M:%S')
    return x





if __name__ == '__main__':
    login = rh.login('username', 'password')
    my_crypto = rh.get_crypto_positions()

    ETHDATA = rh.crypto.get_crypto_historicals('ETH', '5minute', 'day')

    mostRecentTime = fixTime(ETHDATA[-1]['begins_at'])

    for i in range(14,len(ETHDATA)):
        indicators = getLAST14(ETHDATA[i-14:i])
        nextClose = round(float(ETHDATA[i]['close_price']),2)
        currentClose = round(float(ETHDATA[i-1]['close_price']),2)
        pctChange = round((nextClose - currentClose)/currentClose,4)
        time = fixTime(ETHDATA[i]['begins_at'])
        vals = (currentClose, nextClose)
        print(time, vals, pctChange, indicators)

    print('Most recent data point:',mostRecentTime)

