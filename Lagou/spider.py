from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
from settings import SLEEP_TIME

import dbAPI
import lxml
import time


def getBsObj(url):
    """
    访问网址，返回一个BeautifulSoup对象。
    """
    try:
        html = urlopen(url)
    except URLError:
        print("Sleeping!")
        time.sleep(SLEEP_TIME)
        html = urlopen(url)
    except:
        return None

    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj


def getInfo(obj, table_name):
    """
    解析HTML代码，选出有价值数据，并存入数据库，选出下一次抓取的起点。
    """
    if obj == None:
        print("Error!")
        exit()

    global getInfo_tempUrl

    for company in obj.findAll("li", {"class": "con_list_item"}):
        # 公司名
        name = company.attrs['data-company']
        # 公司类型
        t_industry = company.find("div", {"class": "industry"}).get_text()
        tt_industry = t_industry.replace(" ", '')
        industry = tt_industry.replace("\n", '')
        # 公司位置
        position = company.find("a", {"class": "position_link"}).find(
            "span", {"class": "add"}).find("em").get_text()
        # 要求
        t_requirement = company.find("div", {"class": "p_bot"}).find(
            "div", {"class": "li_b_l"}).get_text()
        requirement = t_requirement.replace("\n", '')
        # 福利
        welfare = company.find("div", {"class": "list_item_bot"}).find(
            "div", {"class": "li_b_l"}).get_text()
        # 薪水
        salary = company.find("span", {"class": "money"}).get_text()
        
        # 存入数据库
        dbAPI.store(table_name, name, industry, position, requirement, welfare, salary)

    nexturl = ''
    for i in obj.findAll("a"):
        if i.get_text() == '下一页':
            temp_url = i.attrs['href']
            if '//www.lagou.com/' in temp_url:
                url = 'http:' + temp_url
                nexturl = url
                break
    return nexturl



