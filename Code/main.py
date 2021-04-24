import backtrader
import datetime
from strategies import TestStrategy

cerebro = backtrader.Cerebro()



cerebro.broker.set_cash(1000000) # 1 million for testing
data = backtrader.feeds.YahooFinanceData(
    dataname ='oracle.csv',
    fromdat = datetime.datetime(2000,1,1),#data start
    todat = datetime.datetime(2014,1,1),# data end
    reverse=False)

cerebro.adddata(data)

cerebro.addstrategy(TestStrategy)

print('Staring Portfolio Value: %2f' % cerebro.broker.getvalue())

cerebro.run()

print('Final Portfolio Value: %2f' % cerebro.broker.getvalue())
