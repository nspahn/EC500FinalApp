import backtrader as bt
import datetime
from strategies import TestStrategy, BetterStrategy, BestStrategy

#from fDataDisplay import DisplayStockData

import yfinance as yf
import csv
import numpy as np





#-----------------------------------------------------Input Validation-----------------------------------------------------
def ValidSymbol(TestSymbol): # input validation for stock symbols
    try:
        return TestSymbol in open('nasdaq_screener_1.csv') or open('nasdaq_screener_2.csv')
    except ValueError:
        print("You must enter a valid stock symbol on the NASDAQ")
        return False




#-----------------------------------------------------BackTesting Function-----------------------------------------------------
def Backtesting():
    testedSymbol = input("What stock symbol should we test this strategy on?\n")
    print("What Range of Time do you want ot backtest" + testedSymbol + "?")
    dataRange = input("[1] Day, [2] Month, [3] Year, [4] Max")


    cerebro = bt.Cerebro()

    cerebro.broker.set_cash(1000000) # 1 million for testing
    data = bt.feeds.YahooFinanceData(
        dataname ='oracle.csv',
        fromdat = datetime.datetime(2000,1,1),#data start
        todat = datetime.datetime(2001,1,1),# data end
        reverse=False)

    cerebro.adddata(data)

    cerebro.addstrategy(TestStrategy)

    cerebro.addsizer(bt.sizers.FixedSize, stake = 100)

    print('Staring Portfolio Value: %2f' % cerebro.broker.getvalue())

    cerebro.run()

    print('Final Portfolio Value: %2f' % cerebro.broker.getvalue())

    cerebro.plot()


if __name__ == "__main__":
    #-----------------------------------------------------Welcome Page Console-----------------------------------------------------
    print("Welcome to my Backtrader enabled Trading Strategy Testing App\n")
    print("What part of our application are you lookign to use today?")

    userChoice = input("[1] Back Testing, [2] Set Price-Alert, [3] Display Current Stock Data")
    if userChoice == "1":
        Backtesting()
    else:
        print("EFLAG")