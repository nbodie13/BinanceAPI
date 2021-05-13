import backtrader as bt

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)
            # self.log('Buy create, %.2f' % self.dataclose[0])
        if self.rsi > 70 and self.position:
            self.close()

cerebro = bt.Cerebro()

cerebro.broker.set_cash(1000000)

# data = bt.feeds.GenericCSVData(dataname='BTCUSD-1m-data-2019-flatup.csv', dtformat=2)
# data = bt.feeds.GenericCSVData(dataname='1day_youtube_test.csv', dtformat=2)
data = bt.feeds.GenericCSVData(dataname='BTCUSD-1m-data-2019-flatup-truncated.csv', dtformat=2)

cerebro.addstrategy(RSIStrategy)

cerebro.adddata(data)

cerebro.run()

cerebro.plot()