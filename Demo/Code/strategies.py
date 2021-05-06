# This file is used to handle the stratagies funcitno of the app. Here we outline 3 seperate trading strategies that we can backtest stock data with. The trading stratagies could be more complicated but here are example stratagies


import backtrader

# Create a TestStratey
class TestStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None

    def notify_order(self,order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXCECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXCECUTED {}'.format(order.executed.price))
            self.bar_executed = len(self)

        self.order = None
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
                    #BUY MARKER
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log('SELL CREATED {}'.format(self.dataclose[0]))
                self.sell()

class BetterStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None

    def notify_order(self,order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXCECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXCECUTED {}'.format(order.executed.price))
            self.bar_executed = len(self)

        self.order = None
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
                    #BUY MARKER
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log('SELL CREATED {}'.format(self.dataclose[0]))
                self.sell()

class BestStrategy(backtrader.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function for this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.order = None

    def notify_order(self,order):
        if order.status in [order.Submitted, order.Accepted]:
            return
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXCECUTED {}'.format(order.executed.price))
            elif order.issell():
                self.log('SELL EXCECUTED {}'.format(order.executed.price))
            self.bar_executed = len(self)

        self.order = None
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
                    #BUY MARKER
        else:
            if len(self) >= (self.bar_executed + 5):
                self.log('SELL CREATED {}'.format(self.dataclose[0]))
                self.sell()