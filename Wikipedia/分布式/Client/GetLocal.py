from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from settings import URLERROR_SLEEP_TIME, SLEEP_TIME

import sqlite3
import json
import datetime
import random
import re
import lxml
import time

# 判断一个IP的所在地
def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except URLError:
        print("Sleeping!")
        time.sleep(URLERROR_SLEEP_TIME)
        response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    except:
        return 'Unknown'
    responseJson = json.loads(response)
    return responseJson.get("country_code") # 返回国家代号

# 从网页中抽取出贡献者的IP
def getHistoryIPs(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url:", historyUrl)

    time.sleep(SLEEP_TIME)

    try:
        html = urlopen(historyUrl)
    except HTTPError:
        return None
    except URLError:
        print("Sleeping!")
        time.sleep(URLERROR_SLEEP_TIME)
        html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "lxml")
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})

    addressList = set()
    for ipAddress in ipAddresses:
        print(pageUrl+": "+ipAddress.get_text())
        addressList.add(ipAddress.get_text())
    return addressList #返回一个IP列表

# 得到所有IP的国家代号
def getIPinfo(ipList):
    countrys = []
    for ipAddress in ipList:
        country = getCountry(ipAddress)
        countrys.append(country)
    return (ipList, countrys)

'''
为了调试方便，这里使用的是Sqlite数据库，但是对于一个真正的分布式系统来说，应该使用MongoDB或者Mysql。
'''
# 储存IP信息
def storeIPinfo(objList):
    conn = sqlite3.connect("wikidata.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ipinfo (id INTEGER PRIMARY KEY AUTOINCREMENT, ip varchar(200), country varchar(200))''')

    for bsObj in objList:
        pageUrl = bsObj.attrs["href"]
        historyIPs = getHistoryIPs(pageUrl)
        ipList, countrys = getIPinfo(historyIPs)
        for ipAddress, country in zip(ipList, countrys):
            cur.execute("INSERT INTO ipinfo (ip, country) VALUES (?, ?)", (ipAddress, country))
            conn.commit()

    cur.close()
    conn.close()
            