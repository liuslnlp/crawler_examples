from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from settings import URLERROR_SLEEP_TIME, NUMBER_OF_THREADS

import GetLocal 
import random
import datetime
import re
import lxml
import threading, queue
import time
import redis

# 分析网站的源码并返回内链
def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org"+articleUrl)
    except HTTPError:
        ServerLog.writeLog("HTTPError")
        return None
    except URLError:
        ServerLog.writeLog("URLError")
        print("Sleeping!")
        time.sleep(URLERROR_SLEEP_TIME)
        html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


# 抓取IP
def crawlIP():
    # 连接至Redis
    conn = redis.Redis()
    while True:
        temp =  conn.blpop("link_queue") 
        linkUrl = temp[1].decode('utf-8')
        linkObj = getLinks(linkUrl)
        GetLocal.storeIPinfo(linkObj)



if __name__ == '__main__':
    print("Start!\n-----------------------------")
    crawlIP()