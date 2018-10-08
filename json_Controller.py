import urllib as url
import json
import re
import io
from colorama import init, Fore, Style, Back
import time

#Imports JSON data from web API, and returns data
def json_Import_Cur():
    whileloop = 1
    while whileloop == 1:
        try:
            url_Api = "https://api.iextrading.com/1.0/tops/last?&format=json"
            response = url.urlopen(url_Api)
            data = json.loads(response.read())
            whileloop = 0
            return data
        except IOError:
            print "Issue encountered on json_Import_Cur"
            time.sleep(20)
        except ValueError:
            print api
            print response
            time.sleep(20)
