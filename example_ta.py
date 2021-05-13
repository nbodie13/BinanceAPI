import numpy
import talib

close = numpy.random.random(100)

print(close)

moving_average = talib.SMA(close, timeperiod=10)

print(moving_average)

rsi = talib.RSI(close)

print(rsi)