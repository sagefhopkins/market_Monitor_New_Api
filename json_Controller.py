import urllib as url
import json
import re
import io
from colorama import init, Fore, Style, Back
import time

#Imports JSON data from web API, and returns data
def json_Import_Cur(type):
    if type == 'stock_Market':
        try:
            url_Api = "https://api.iextrading.com/1.0/tops/last?&format=json"
            response = url.urlopen(url_Api)
            data = json.loads(response.read())
            return data
        except IOError:
            print "Issue encountered on json_Import_Cur"
            time.sleep(20)
        except ValueError:
            print response
            time.sleep(20)
    elif type == 'currency_Market':
        try:
            url_Api = "https://api.exchangeratesapi.io/latest?base=USD&symbols=JPY,BGN,CZK,DKK,GBP,HUF,PLN,RON,SEK,CHF,ISK,NOK,HRK,RUB,TRY,AUD,BRL,CAD,CNY,HKD,IDR,ILS,INR,KRW,MXN,MYR,NZD,PHP,SGD,THB,ZAR"
            response = url.urlopen(url_Api)
            data = json.loads(response.read())
            return data
        except IOError:
            print 'Issue encountered on json_Import_Cur'
            time.sleep(20)
        except ValueError:
            print response
            time.sleep(20)
    elif type == 'commodity_Market':
        try:
            url_Api = "https://data.gov.in/node/86943/datastore/export/json"
            response = url.urlopen(url_Api)
            data = json.loads(response.read())
            return data
        except IOError:
            print 'Issue encountered on json_Import_Cur'
            time.sleep(20)
        except ValueError:
            print response
            time.sleep(20)


def json_Search_Api(search):
    try:
        api_Url = ('https://www.gigablast.com/search?q={0}&userid=199&code=1015035357&format=json').format(search)
        response = url.urlopen(api_Url)
        data = json.loads(response.read())
        return data
    except IOError:
        print 'Issue encountered on json_Import_Cur'
        time.sleep(20)
    except ValueError:
        print response
        time.sleep(20)
