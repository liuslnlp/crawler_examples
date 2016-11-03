#    Copyright 2016 WiseDoge

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import redis
import requests
import time
import re
import json
import dbAPI
import random
import utils
import threading
import datetime
from Error import WebError, SettingError


# 读取用户名，数据库设置。
val = json.load(open("setting.json"))

# 设置一个用户名，便于区分从机。
slave_name = val['user']

# 初始化随机数种子
random.seed(datetime.datetime.now())



class Crawler(threading.Thread):
    """
    爬虫类。
    """

    def __init__(self, thread_grade, proxy = None):
        """
        connect to Redis.init session and proxy.
        """
        self.thread_grade = thread_grade
        self.conn = redis.Redis(host=val['redis']['host'], port=val['redis']['port'])
        self.session = requests.Session()
        self.proxy = {"http":proxy}
        threading.Thread.__init__(self)

    def get_task(self):
        """
        get task URL from Redis queue and translate it into UTF-8 encoding.
        """
        _url = self.conn.blpop("UrlQueue")
        self.url = _url[1].decode("utf-8")

    def get_info(self, bsObj):
        """
        Receive a BeautifulSoup object, and return a dictionary including user`s information.
        Raise Exception:
            - WebError: 
        """

        # 对于没有followees的用户来说，没有此标签。
        try:
            followees = bsObj.find("a", {"class": "item", "href": re.compile(
                "followees")}).find("strong").get_text()
        except AttributeError:
            followees = "0"
        
        # 对于没有followers的用户来说，没有此标签。
        try:
            followers = bsObj.find("a", {"class": "item", "href": re.compile(
                "followers")}).find("strong").get_text()
        except AttributeError:
            followers = "0"

        # 如果没有Name，说明爬虫已经被Ban（爬虫被Ban时，不会显示403错误，而是打开另一个网页），此时抛出异常，结束爬虫。
        try:
            name = bsObj.find("div", {"class": "title-section"}
                            ).find("span", {"class": "name"}).get_text()
        except AttributeError:
            print(self.proxy)
            raise WebError

        try:
            presentation = bsObj.find("div", {"class": "bio ellipsis"}).get_text()
        except AttributeError:
            presentation = "NODATA"

        try:
            items = bsObj.find("div", {"class": "items"})
        except AttributeError:
            data = {
                "Name": "NODATA",
                "Presentation": "NODATA",
                "Location_item": "NODATA",
                "Business_item": "NODATA",
                "Employment_item": "NODATA",
                "Position_item": "NODATA",
                "Education_item": "NODATA",
                "Education_extra_item": "NODATA",
                "Followees": followees,
                "Followers": followers,
            }
            return data

        try:
            location_item = items.find(
                "span", {"class": "location item"}).get_text()
        except AttributeError:
            location_item = "NODATA"
        try:
            business_item = items.find(
                "span", {"class": "business item"}).get_text()
        except AttributeError:
            business_item = "NODATA"
        try:
            employment_item = items.find(
                "span", {"class": "employment item"}).get_text()
        except AttributeError:
            employment_item = "NODATA"
        try:
            position_item = items.find(
                "span", {"class": "position item"}).get_text()
        except AttributeError:
            position_item = "NODATA"
        try:
            education_item = items.find(
                "span", {"class": "education item"}).get_text()
        except AttributeError:
            education_item = "NODATA"
        try:
            education_extra_item = items.find(
                "span", {"class": "education-extra item"}).get_text()
        except AttributeError:
            education_extra_item = "NODATA"

        data = {
            "Name": name,
            "Presentation": presentation,
            "Location_item": location_item,
            "Business_item": business_item,
            "Employment_item": employment_item,
            "Position_item": position_item,
            "Education_item": education_item,
            "Education_extra_item": education_extra_item,
            "Followees": followees,
            "Followers": followers,
        }

        return data
        
    def run(self):
        """
        启动线程。
        """
        while True:
            self.get_task()

            # 输出正在抓取的URL
            print("Thread #" + str(self.thread_grade) + ": " + self.url)

            soup = utils.get_links(self.session, self.url, self.proxy)

            if not soup:
                print("Url Error")
                continue
            data_dict = self.get_info(soup)

            # 储存到数据库
            dbAPI.store_by_mongodb(data_dict)

            # 控制抓取速度
            time.sleep(val['sleep'])

def mode_no_proxy(thread_num):
    """
    无代理模式
    """
    threads = []
    for i in range(thread_num):
        thread = Crawler(i + 1)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def mode_multi(thread_num, proxy_list):
    """
    开启代理，多线程。
    """
    threads = []
    list_len = len(proxy_list)
    if thread_num < list_len:
        raise SettingError("The number of threads must be greater than the number of agents, please reset")
    for i in range(list_len):
        thread = Crawler(i + 1, proxy_list[i])
        thread.start()
        threads.append(thread)
    if thread_num > list_len:
        thread_num = thread_num - list_len
        for i in range(thread_num):
            next_index = random.randint(0, list_len - 1)
            thread = Crawler(list_len + i + 1, proxy_list[next_index])
            thread.start()
            threads.append(thread)
    for thread in threads:
        thread.join()


def main():
    global slave_name

    # 记录登录时间
    conn = redis.Redis(host=val['redis']['host'], port=val['redis']['port'])
    conn.rpush("users", slave_name + " " + time.ctime())

    # 启动
    if val['proxy_on']:
        mode_multi(val['thread_num'], val['proxies'])
    else:
        mode_no_proxy(val['thread_num'])

if __name__ == '__main__':
    main()
