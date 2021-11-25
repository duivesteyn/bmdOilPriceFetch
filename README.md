# bmdOilPriceFetch

A **Fast** and **Efficient** way to get the **current** Oil Price from Yahoo Finance API in Python. Data is returned as a dictionary. 

I've found a lack of good simple ways to get the oil price from a free online API, so I designed one myself based upon Yahoo Finance. 

It simply returns a dictionary with the current market data for Oil (WTI Front Month).

It also accepts a parameter <code>ticker</code> which will get the market data for that ticker on Yahoo Finance. i.e bmdPriceFetch() 

![](https://github.com/duivesteyn/bmdOilPriceFetch/raw/main/screenshot.png)


# Example Usage
An example usage file is included called test.py. It contains the basics for running this code. It is in essense: 
```py
    from bmdOilPriceFetch import bmdPriceFetch

    def printOilPrice():
    """Get and Print WTI Oil Price"""

        data = bmdPriceFetch()
        outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
        print(outputString)

    def printAStockPrice(ticker='AAPL'):
    """Get and Print the Price of a Company Stock (Yahoo! Finance Format)"""

        data = bmdPriceFetch(ticker)
        outputString = "The price of " + ticker + " is $" + str("%.2f" % data['regularMarketPrice'])
        print(outputString)

    printOilPrice()
    printAStockPrice()
```

# Example Output Data
The output is a dictionary:
```json
    {   'close': 53.650001525878906, 
        'high': 53.650001525878906, 
        'lastClose': 52.98, 
        'low': 53.060001373291016,
        'open': 53.130001068115234,
        'regularMarketPrice': 53.65,
        'volume': 2664,
        'metadata': {

            'chartPreviousClose': 52.98,
            'currency': 'USD',
            'currentTradingPeriod': {

                'post': {

                    'end': 1611205140,
                    'gmtoffset': -18000,
                    'start': 1611205140,
                    'timezone': 'EST'},

                    'pre': {

                        'end': 1611118800,
                        'gmtoffset': -18000,
                        'start': 1611118800,
                        'timezone': 'EST'},

                    'regular': {

                        'end': 1611205140,
                        'gmtoffset': -18000,
                        'start': 1611118800,
                        'timezone': 'EST'}},

            'dataGranularity': '1d',
            'exchangeName': 'NYM',
            'exchangeTimezoneName': 'America/New_York',
            'firstTradeDate': 967003200,
            'gmtoffset': -18000,
            'instrumentType': 'FUTURE',
            'priceHint': 2,
            'range': '',
            'regularMarketPrice': 53.65,
            'regularMarketTime': 1611142219,
            'symbol': 'CL=F',
            'timezone': 'EST',
            'validRanges': [

                '1d',
                '5d',
                '1mo',
                '3mo',
                '6mo',
                '1y',
                '2y',
                '5y',
                '10y',
                'ytd',
                'max']}}
```

# Changelog

* v0.6  2021-11-25  Minor Readability Improvements.
* v0.5  2021-07-11  Yahoo! Finance API decided they want a user agent. Added.
* v0.4  2021-06-21  Bugfix. ^GSPC Lookup didnt work on weekends for Close. Made more fault tolerant.
* v0.3  2021-02-06  Released as a package.
* v0.2  2021-01-22  Minor tidy up, allows input of any Stock. Execution Time around 500ms. Code= 45 Lines
* v0.1  2021-01-20  Initial Revision. Execution Time around 500ms. Code= 47 Lines


# Credits

designed in 2021 by bmd.