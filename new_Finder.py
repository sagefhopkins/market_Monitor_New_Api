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
    num = 1
    arr = []

#This formats the urls so they are complete, however after each is generated we need to ensure only the second value is the list create is taken because that is the real url, the other one
#is a google cache and is not helpful
    for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        result = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        #final = re.search(r'\'(.*)\', \'(.*?)\'', str(result), '')
        #print final.result(1)
        arr.insert(num ,result)
        num = num + 1
    print 'Array Number 10' + str(arr[10])
