#!/usr/bin/env python3
# coding: utf-8
#
# duivesteyn // Python // bmdOilPriceFetch
# https://github.com/duivesteyn/bmdOilPriceFetch
#
# Testing Scripts for BMD Oil Price Fetch. Code that gets data from Yahoo Finance
#
from bmdOilPriceFetch import bmdPriceFetch

def printOilPrice():
    '''Get and Print WTI Oil Price'''

    data = bmdPriceFetch()
    outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
    print(outputString)

def printAStockPrice():
    '''Get and Print the Price of a Company Stock (Yahoo! Finance Format)'''

    ticker='AAPL'
    data = bmdPriceFetch(ticker)
    outputString = "The price of " + ticker + " is $" + str("%.2f" % data['regularMarketPrice'])
    print(outputString)

# Main body
if __name__ == '__main__':
    printOilPrice()
    printAStockPrice()