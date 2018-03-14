import collections
import csv

import requests

symbols = []
Stock = collections.namedtuple('Stock',
                               ['symbol', 'name', 'price', 'marketCap', 'ipoYear', 'sector', 'industry', 'SummaryQuote',
                                'garbage'])
StockHttp = collections.namedtuple('StockHttp',
                                   ['symbol', 'name', 'lastSale', 'marketCap', 'ipoYear', 'sector', 'industry',
                                    'SummaryQuote', 'garbage'])
StockNasdaqListed = collections.namedtuple('StockNasdaqListed',
                                           ['symbol', 'name', 'marketCategory', 'testIssue', 'financialStatus',
                                            'roundLot', "ETF", "nextShares"])
StockNasdaqTraded = collections.namedtuple('StockNasdaqTraded',
                                           ["nasdaqTraded", "symbol", "securityName", "listingExchange",
                                            "marketCategory", "ETF", "roundLotSize", "testIssue", "financialStatus",
                                            "cqsSymbol", "nasdaqSymbol", "nextShares"])


def get_stocks_universal(file_name, tupleFunction, delimiter=","):
    stocks = dict()
    with open(file_name, 'rb') as f:
        header = True
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            if header:
                header = False
                continue
            try:
                print row
                stock = tupleFunction(row)
            except BaseException as err:
                print err
                continue
            if not stock.symbol.startswith("File Creation Time:"):
                if 'ETF' in stock.__dict__.keys():
                    if stock.ETF == 'N' and (stock.financialStatus == 'N' or not stock.financialStatus):
                        stocks[stock.symbol.strip()] = stock
                    else:
                        if stock.symbol == "CEL":
                            print stock
                else:
                    stocks[stock.symbol.strip()] = stock
    return stocks


nasdaq = get_stocks_universal('/Users/vbondarenko/Documents/inv/companylist.csv', StockHttp._make)
# nyse = get_stocks_universal('/Users/vbondarenko/Documents/inv/nyse.csv', StockHttp._make)
# amex = get_stocks_universal('/Users/vbondarenko/Documents/inv/amex.csv', StockHttp._make)

# all1 = get_stocks_universal('/Users/vbondarenko/Documents/inv/nasdaqlisted.txt', StockNasdaqListed._make, "|")
# all2 = get_stocks_universal('/Users/vbondarenko/Documents/inv/nasdaqtraded.txt', StockNasdaqTraded._make, "|")

# print "nasdaq = {}".format(nasdaq.__len__())
# print "nyse = {}".format(nyse.__len__())
# print "amex = {}".format(amex.__len__())
# print "nasdaq listed = {}".format(all1.__len__())
# print "nasdaq traded = {}".format(all2.__len__())

# print "{}-{}={}".format("nasdaq", "nyse", (set(nasdaq) - set(nyse)).__len__())
# print "{}-{}={}".format("nyse", "nasdaq", (set(nyse) - set(nasdaq)).__len__())

# print "{}-{}={}".format("nasdaq", "all1", (set(nasdaq) - set(all1)).__len__())
# print "{}-{}={}".format("all1", "nasdaq", (set(all1) - set(nasdaq)).__len__())

# print set(nasdaq.keys()) & set(nyse.keys())
# print set(nasdaq.keys()) & set(all1.keys())

# print (set(nasdaq.keys()) | set(all1.keys())).__len__()

# all_from_ftp = set(all1.keys()) | set(all2.keys())
# all_from_http = set(nasdaq.keys()) | set(nyse.keys()) | set(amex.keys())

# print "all_from_http = {}".format(all_from_http.__len__())
# print "all_from_ftp = {}".format(all_from_ftp.__len__())

# print all_from_ftp - all_from_http
# print all_from_http - all_from_ftp
# print "ftp - http {}".format((all_from_ftp - all_from_http).__len__())
# print "http - ftp {}".format((all_from_http - all_from_ftp).__len__())
# print "all = {}".format((all_from_ftp | all_from_http).__len__())

# nasdaq_url = "https://www.nasdaq.com/screening/companies-by-name.aspx"
# params = {"letter": "0", "exchange": "nasdaq", "render": "download"}
# response = requests.get(nasdaq_url, params)
# print response.status_code

# rows = response.content.split("\r\n")
# reader = csv.reader(rows)
# for row in reader:
#     print row

