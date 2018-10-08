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



def import_Market_Data():
    data = jsc.json_Import_Cur()
    for data_item in data:
        for key, value in data_item.items():
            print('key {} value {}').format(key, value)
