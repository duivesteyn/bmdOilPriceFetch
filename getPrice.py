#!/usr/bin/env python
import bmdOilPriceFetch

#Get and Print WTI Oil Price
def printPrice():
    data = bmdOilPriceFetch.bmdPriceFetch()
    outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
    print(outputString)

printPrice()
