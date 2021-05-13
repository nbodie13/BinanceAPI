import numpy, talib
from numpy import genfromtxt

my_data = genfromtxt('15minutes.csv',delimiter=',')
# print(my_data)

close = my_data[:,4]
# print(close)

rsi = talib.RSI(close)
print(rsi)