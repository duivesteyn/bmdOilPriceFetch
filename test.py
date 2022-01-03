#!/usr/bin/env python3
# coding: utf-8
#
# duivesteyn // Python // bmdOilPriceFetch
# https://github.com/duivesteyn/bmdOilPriceFetch
#
# Testing Scripts for BMD Oil Price Fetch. Code that gets data from Yahoo Finance
#
from bmdOilPriceFetch import bmdPriceFetch
import logging

def printOilPrice():
    '''Get and Print WTI Oil Price'''

    data = bmdPriceFetch()
    if data is not None:
        outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
        logging.info(outputString)
    else:
        raise ValueError('Data Error Talking to Server - printOilPrice')

def printAStockPrice():
    '''Get and Print the Price of a Company Stock (Yahoo! Finance Format)'''

    ticker='AAPL'
    data = bmdPriceFetch(ticker)
    if data is not None:
        outputString = "The price of " + ticker + " is $" + str("%.2f" % data['regularMarketPrice'])
        logging.info(outputString)
    else:
        raise ValueError(f'Data Error Talking to Server - {ticker}')

def printAStockPriceThatDoesntExist():
    '''Get and Print the Price of a Company Stock (Yahoo! Finance Format)'''

    ticker='DONTKNOWTHISCODEDOH'
    data = bmdPriceFetch(ticker)
    if data is not None:
        outputString = "The price of " + ticker + " is $" + str("%.2f" % data['regularMarketPrice'])
        logging.info(outputString)
    else:
        raise ValueError(f'Data Error Talking to Server - {ticker}')

# Main body
if __name__ == '__main__':
    printAStockPrice()