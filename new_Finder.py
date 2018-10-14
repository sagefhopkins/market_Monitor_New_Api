import urllib
import requests
import webbrowser
import re
import scrapy
from scrapy.crawler import CrawlerProcess

class NewsSpider(scrapy.Spider):
    name = 'News Spider'

    def __init__(self, name):
        self.start_urls = [ name ]
        super(NewsSpider, self).__init__()

    def parse(self, response):
        pass

def search_Url(name):
    url = 'https://www.google.com/search?q=' + urllib.quote_plus(name)
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })
    process.crawl( NewsSpider, url)
    process.start()


"""
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
"""
