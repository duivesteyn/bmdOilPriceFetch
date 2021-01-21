from bmdOilPriceFetch import bmdOilPriceFetch
import pprint

#Get and Print WTI Oil Price
data = bmdOilPriceFetch.bmdPriceFetch()
#pprint.pprint(data)
outputString = 'The price of WTI is $' + str("%.2f" % data['regularMarketPrice'])
print(outputString)
