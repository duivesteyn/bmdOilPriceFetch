#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bmdOilPriceFetch
# efficient collection of Oil Price / Stock Data from Yahoo Finance API. Data is returned as a dictionary. 
# bmd 2021

"""Quickest and Simplest Oil Price Lookup I can come up with in Python"""

import requests
import time
import logging
import sys

def getData(ticker):
    """Gets Yahoo Finance Stock Data via a simple API. No Page Scraping. the y! ticker for WTI is "CL=F" """
    start_seconds=int(time.time()) - 86400                                          #start_date = pd.Timestamp.today() - pd.DateOffset(1), 
    end_seconds=int(time.time()) + 86400                                            #end_date = pd.Timestamp.today() + pd.DateOffset(1))
    site = "https://query2.finance.yahoo.com/v8/finance/chart/" + ticker
    headers = { 
    'User-Agent'      : 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1', 
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header 
    'Connection'      : 'close'
}
    params = {"period1": start_seconds, "period2": end_seconds,"interval": "1d"}
    logging.info(params)
    resp = requests.get(site, params = params, headers = headers)

    if not resp.ok:
        raise AssertionError(resp.json())

    data = resp.json()

    return data

def bmdPriceFetch(ticker="CL=F"):
    """Compile Price Data into Nice Dictionary for the User. Default is WTI Oil Front Month Contract (CL=F). Can specify custom ticker in Yahoo Finance Format!"""
    data = getData(ticker) 
    itemsToCollect = ["close","high","low","open","volume"]                         #Collect data from the API Call. Not all items have these datasets at all times (i.e. weekends or when market closed)
    keyOutputData = {} 

    if data:
        indicatorData = data["chart"]["result"][0]["indicators"]["quote"][0]
        for item in itemsToCollect:
            if item in indicatorData: keyOutputData[item] = indicatorData[item][-1] #Add data if it exists (Doesnt always exist for indexes like ^GSPC)
        keyOutputData["regularMarketPrice"] = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
        keyOutputData["lastClose"] = data["chart"]["result"][0]["meta"]["chartPreviousClose"]
        keyOutputData["metadata"] = data["chart"]["result"][0]["meta"]
    return keyOutputData

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    data = bmdPriceFetch()
    print(data)