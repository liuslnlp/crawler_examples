from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from settings import URLERROR_SLEEP_TIME, SLEEP_TIME

import time
import lxml
import sqlite3


def getAbst(articleUrl):
    '''
    分析HTML得到标题和摘要
    '''
    time.sleep(SLEEP_TIME)

    try:
        html = urlopen("http://en.wikipedia.org" + articleUrl)
    except URLError:
        print("Sleeping!")
        time.sleep(URLERROR_SLEEP_TIME)
        html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    title = bsObj.find("h1").get_text()
    content = bsObj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    print("Title:", title)
    return (title, content)


def storeAbst(link):
    '''
    储存标题和摘要
    '''
    conn = sqlite3.connect("wikidata.db")
    cur = conn.cursor()
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS pages (id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(200), content text)''')

    title, content = getAbst(link)
    cur.execute("INSERT INTO pages (title, content) VALUES (?, ?)",
                (title, content))
    conn.commit()

    cur.close()
    conn.close()
