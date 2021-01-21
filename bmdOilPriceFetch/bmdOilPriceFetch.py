#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bmdOilPriceFetch
# efficient collection of Oil Price / Stock Data from Yahoo Finance API. Data is returned as a dictionary. 
# bmd 2021

"""Quickest and Simplest Oil Price Lookup I can come up with in Python"""

import requests
import time

def getData(ticker):
    """Gets Yahoo Finance Stock Data via a simple API. No Page Scraping. the y! ticker for WTI is "CL=F" """
    start_seconds=int(time.time()) - 86400                                          #start_date = pd.Timestamp.today() - pd.DateOffset(1), 
    end_seconds=int(time.time()) +86400                                             #end_date = pd.Timestamp.today() + pd.DateOffset(1))
    site = "https://query1.finance.yahoo.com/v8/finance/chart/" + ticker
    params = {"period1": start_seconds, "period2": end_seconds,"interval": "1d"}
    resp = requests.get(site, params = params)

    if not resp.ok:
        raise AssertionError(resp.json())

    data = resp.json()

    return data

def bmdPriceFetch(ticker="CL=F"):
    """Compile Oil Price Data into Nice Dictionary for the User"""
    data = getData(ticker) 
    keyOutputData = {} 

    #Build up the simple dictionary from the input data
    keyOutputData["close"] = data["chart"]["result"][0]["indicators"]["quote"][0]["close"][-1]
    keyOutputData["high"] = data["chart"]["result"][0]["indicators"]["quote"][0]["high"][-1]
    keyOutputData["low"] = data["chart"]["result"][0]["indicators"]["quote"][0]["low"][-1]
    keyOutputData["open"] = data["chart"]["result"][0]["indicators"]["quote"][0]["open"][-1]
    keyOutputData["volume"] = data["chart"]["result"][0]["indicators"]["quote"][0]["volume"][-1]
    keyOutputData["regularMarketPrice"] = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
    keyOutputData["lastClose"] = data["chart"]["result"][0]["meta"]["chartPreviousClose"]
    keyOutputData["metadata"] = data["chart"]["result"][0]["meta"]

    return keyOutputData

if __name__ == "__main__":
    bmdPriceFetch()