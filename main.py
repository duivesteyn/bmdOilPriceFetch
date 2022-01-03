#!/usr/bin/env python3
# coding: utf-8
#
# duivesteyn // Python // bmdOilPriceFetch
# https://github.com/duivesteyn/bmdOilPriceFetch
#
# Simple Example!
#
from bmdOilPriceFetch import bmdPriceFetch

def main():
    """Get and Print WTI Oil Price"""

    data = bmdPriceFetch()
    if data is not None:
        outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
        print(outputString)

def printAStockPrice(ticker='XOM'):
    """Get and Print the Price of a Company Stock (Yahoo! Finance Format)"""

    data = bmdPriceFetch(ticker)
    if data is not None:
        outputString = "The price of " + ticker + " is $" + str("%.2f" % data['regularMarketPrice'])
        print(outputString)


if __name__ == '__main__':
    main()
    #printAStockPrice()