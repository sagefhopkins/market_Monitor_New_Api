from decimal import Decimal, ROUND_HALF_UP
import ConfigParser
import io
import json_Controller as jsc
import database_Controller as dbc
import time
from colorama import init, Fore, Back, Style
import threading
import re
import json
from sys import stdout



def import_Stock_Market_Data():
    data = jsc.json_Import_Cur('stock_Market')
    for data_item in data:
        for key, value in data_item.items():
            if key == 'symbol':
                ticker = value
                print ('Ticker = {}').format(ticker)
            elif key == 'price':
                price = value
                print ('Price = {}').format(price)
                dbc.insert_Stock(ticker, price, time.strftime('%Y-%m-%d %H:%M:%S'))

def import_Currency_Market_Data():
    data = jsc.json_Import_Cur('currency_Market')
    for ticker, price in data['rates'].iteritems():
        print ('Ticker = {}').format(ticker)
        print ('Price = {}').format(price)
        dbc.insert_Currency(ticker, price, time.strftime('%Y-%m-%d %H:%M:%S'))

def import_Commoditiy_Market_Data():
    data = jsc.json_Import_Cur('commodity_Market')
    exchange = jsc.json_Import_Cur('currency_Market')
    for ticker, price in exchange['rates'].iteritems():
        if ticker == 'INR':
            exchange_Rate = price
    for data_item in data:
        for key, value in data_item.items():
            if key == 'state':
                state = value
                print ('State = {}').format(state)
            elif key == 'commodity':
                commodity = value
                print ('Commodity = {}').format(commodity)
            elif key == 'arrival_date':
                date = value
                print ('Date = {}').format(date)
            elif key == 'min_price':
                tmp_min = value
                min = (float(tmp_min)/float(exchange_Rate))
                print ('Min = {}').format(min)
            elif key == 'max_price':
                tmp_max = value
                max = (float(tmp_max)/float(exchange_Rate))
                print ('Max = {}').format(max)
                dbc.insert_Commodity(commodity, state, min, med, max, time.strftime('%Y-%m-%d %H:%M:%S'))
            elif key == 'modal_price':
                tmp_med = value
                med = (float(tmp_med)/float(exchange_Rate))
                print ('Med = {}').format(med)
