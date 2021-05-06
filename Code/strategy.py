# This file is used to handle the strategy of the trade decisions. Here we outline a basic trade strategy.
import datetime
import math

import backtrader as bt
import pandas as pd


#-----------------------------------------------------Trade Strategy Classes-----------------------------------------------------

# Create a Test Strategy (Not a terribly profitable trading algorithm **great personality though)
class BestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def notify_order(self,order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                        'BUY EXECUTED, Price: %.2f, Cost: %.2f, Comm: %2f' %
                        (order.executed.price,
                        order.executed.value,
                        order.executed.comm))

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log(
                        'SELL EXECUTED, Price: %2f, Cost: %2f, Comm: %2f' %
                        (order.executed.price,
                        order.executed.value,
                        order.executed.comm))
        elif order.status in [order.Canceled, order.Margin,
                                      order.Rejected]:  # unsuccessful order for whatever reason e.g. broker refusals or connectivity issues
            self.log('Order canceled/margin/rejected')

            self.bar_executed = len(self)

        self.order = None

    def notify_trade(self, trade):

        if not trade.isclosed:
            return

        self.log(
            'OPERATION PROFIT, GROSS %2f, NET %.2F' %
            (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        self.log('Close, %.2f' % self.dataclose[0])

        print(self.order)
        print(self.position)
        print(len(self));
        if self.order:
            return
        if not self.position:
            if self.dataclose[0] < self.dataclose[-1]:
                # "0" close < "-1" close

                if self.dataclose[-1] < self.dataclose[-2]:
                    # "-1" close < "-2" close

                    self.log("Buy CREATED, %.2f" % self.dataclose[0])
                    self.buy()
                    # BUY MARKER
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log('SELL CREATED {}'.format(self.dataclose[0]))
                self.sell()
class GoldenCross(bt.Strategy):


    params = dict(fast=50, slow=200, order_percentage = 0.95, ticker = "SPY")

    def __init__(self):

        self.TI = self.Trend_Indicator(self.datas[0])

    def next(self):
        if self.position.size ==0:
            if self.crossover >0:
                amount_to_invest = (self.params.order_percentage * self.broker.cash)
                self.size = math.floor(amount_to_invest/self.data.close)

                print("Buy {} Share of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))

                self.buy(size=self.size)

        if self.position.size >0:
            if self.crossover<0:
                print("Sell {} Share of {} at {}".format(self.size, self.params.ticker, self.data.close[0]))
                self.close()
#-----------------------------------------------------DataFeed/API CONFIG-----------------------------------------------------------
# # Grabs Data from 01/01/2015 -> Today
data = bt.feeds.YahooFinanceData(

        dataname = pd.read_csv("data.csv"),
        fromdate = datetime.datetime(2015, 1, 1),
        todate = datetime.date.today(),
        reverse = False
    )

cerebro = bt.Cerebro(stdstats = False)
cerebro.addobserver(bt.observers.BuySell)
cerebro.addstrategy(BestStrategy)
cerebro.adddata(data)
cerebro.broker.setcash(100000)
cerebro.run()

print("Final portfolio value: " + str(cerebro.broker.getvalue()))
final_portfolio_value = cerebro.broker.getvalue()
