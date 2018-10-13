import urllib
import requests
import webbrowser
import re
from bs4 import BeautifulSoup


def search_Url(name):
    name = urllib.quote_plus(name)
    search = 'https://www.google.com/search?q=' + name
    url_Search = requests.get(search)
    print search
    soup = BeautifulSoup(url_Search.text)
    all_Links = soup.findAll('a')

    for link in all_Links:
        if link.get('href')
