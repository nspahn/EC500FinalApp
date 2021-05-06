#This function handles the printing of the function.

from main import ValidSymbol

# -----------------------------------------------------Stock Display Data Function-----------------------------------------------------
def DisplayStockData():
    symbolList = [] # List of symbols to display
    tickerNum = input("How many tickers do you want to display?") # means to display multiple tickers
    for x in range (1, tickerNum):
        testedSymbol = input("Enter a stock symbol to display\n") # means to get ticker to display
        if ValidSymbol(testedSymbol):
            list.append(tickerNum, symbolList)