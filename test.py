#!/usr/bin/env python
import bmdOilPriceFetch

def printOilPrice():
    '''Get and Print WTI Oil Price'''

    data = bmdOilPriceFetch.bmdPriceFetch()
    outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
    print(outputString)

def printAStockPrice():
    '''Get and Print the Price of a Company Stock (Yahoo! Finance Format)'''

    ticker='AAPL'
    data = bmdOilPriceFetch.bmdPriceFetch(ticker)
    outputString = "The price of " + ticker + " is $" + str("%.2f" % data['regularMarketPrice'])
    print(outputString)

# Main body
if __name__ == '__main__':
    printOilPrice()
    printAStockPrice()