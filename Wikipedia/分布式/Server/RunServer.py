from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from settings import URLERROR_SLEEP_TIME, START_PAGE, SLEEP_TIME


import random
import datetime
import re
import lxml
import time
import redis
import ServerLog

# 初始化随机数种子
random.seed(datetime.datetime.now())

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

# 设置页面
links = getLinks(START_PAGE) 
newLink = START_PAGE


# 连接至Redis
conn = redis.Redis()

# 抓取摘要
def RunServer():
    global conn, links, newLink
    while(len(links) > 0):
        print(newLink)
        conn.rpush("link_queue", newLink.encode('utf-8'))
        newLink = links[random.randint(0, len(links)-1)].attrs["href"]
        time.sleep(SLEEP_TIME)
        links = getLinks(newLink)


if __name__ == '__main__':
    ServerLog.writeLog("Start!")
    print("Start!\n-----------------------------")
    RunServer()
