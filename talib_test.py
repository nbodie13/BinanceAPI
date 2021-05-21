import talib as ta
import numpy as np

closes = [39056.07, 39265.12, 39256.6, 39419.2, 39542.38, 39466.74, 39372.14, 39294.12, 
          39403.73, 39351.55, 39296.22, 39324.97, 39376.97, 39644.39, 39578.06, 39525.53, 
          39540.8, 39560.27, 39483.42, 39436.29, 39490.01]
closes = np.array(closes)


output = ta.EMA(closes, timeperiod=5)
print(output)
print(len(output))