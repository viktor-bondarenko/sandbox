import collections
import csv

import requests

symbols = []
Stock = collections.namedtuple('Stock',
                                   ['symbol', 'name', 'lastSale', 'marketCap', 'ipoYear', 'sector', 'industry',
                                    'SummaryQuote', 'garbage'])


def get_stocks_from_http(exchange_name):
    url = 'https://www.nasdaq.com/screening/companies-by-name.aspx'
    stocks = dict()
    params = {"letter": "0", "exchange": exchange_name, "render": "download"}
    response = requests.get(url, params)
    rows = response.content.split("\r\n")
    reader = csv.reader(rows)
    header = True
    for row in reader:
        if header:
            header = False
            continue
        try:
            stock = Stock._make(row)
        except BaseException as err:
            print err
            continue
        stocks[stock.symbol.strip()] = stock
    return stocks

def merge(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.iteritems():
        value_from_first_dict = dict1.get(key)
        if value_from_first_dict:
            print "first map already has it {} -> {}".format(key, value_from_first_dict)
            print "{}".format(value)
        else:
            result[key] = value
    return result



def get_stocks_universal(file_name, tupleFunction, delimiter=","):
    stocks = dict()
    with open(file_name, 'rb') as f:
        reader = csv.reader(f, delimiter=delimiter)
        for row in reader:
            try:
                stock = tupleFunction(row)
            except BaseException as err:
                print err
                continue
            stocks[stock.symbol.strip()] = stock
    return stocks


nasdaq = get_stocks_universal('dict.csv', Stock._make)

print nasdaq.keys().__len__()
les_10 = filter(lambda item: item.lastSale <= 10, nasdaq.values())
print les_10.__len__()

# nasdaq = get_stocks_from_http('nasdaq')
# nyse = get_stocks_from_http('nyse')
# amex = get_stocks_from_http('amex')
#
# print "nasdaq = {}".format(nasdaq.__len__())
# print "nyse = {}".format(nyse.__len__())
# print "amex = {}".format(amex.__len__())
#
# all = merge(nasdaq, nyse)
# all = merge(all, amex)
#
# all_from_http = set(nasdaq.keys()) | set(nyse.keys()) | set(amex.keys())
#
# print "all_from_http = {}".format(all_from_http.__len__())
# print "meged = {}".format(all.keys().__len__())

# new_dict =  merge(dict(PIH=Stock._make(['PIH', '1347 Property Insurance Holdings, Inc.', '6.9', '$41.29M', '2014', 'Finance', 'Property-Casualty Insurers', 'https://www.nasdaq.com/symbol/pih', ''])
#                  , TURN=Stock._make(['TURN', '180 Degree Capital Corp.', '2.035', '$63.33M', 'n/a', 'Finance', 'Finance/Investors Services', 'https://www.nasdaq.com/symbol/turn', ''])),
#             dict(PIH=Stock._make(['PIH', '1347 Property Insurance Holdings, Inc.', '7.9', '$41.29M', '2014', 'Finance', 'Property-Casualty Insurers', 'https://www.nasdaq.com/symbol/pih', '']),
#                  FCCY=Stock._make(['FCCY', '1st Constitution Bancorp (NJ)', '19.752', '$159.65M', 'n/a', 'Finance', 'Savings Institutions', 'https://www.nasdaq.com/symbol/fccy', ''])))
#
# with open('dict.csv', 'wb') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in all.items():
#         writer.writerow(value)


