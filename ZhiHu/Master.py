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

from Error import NoFolloweeError
import login
import redis
import random
import datetime
import utils
import requests
import json


# 加载设置
val = json.load(open("setting.json"))

# 初始化随机数种子
random.seed(datetime.datetime.now())

# 保存Cookies
session = requests.session()

# 连接至Redis
conn = redis.Redis(host=val['redis']['host'], port=val['redis']['port'])


def put_into_queue(info_list):
    """
    构造一个set，负责去重。info_list内的内容如果不在集合内，就压入任务队列，否则舍去。
    """
    for info in info_list:
        flag = conn.sadd("UrlSet", info)
        if flag:
            conn.rpush("UrlQueue", info)


def get_next_url(url_list):
    """
    从url_list内随机抽取出一个url返回。
    """
    next_index = random.randint(0, len(url_list) - 1)
    next_url = url_list[next_index]
    return next_url


def get_my_url():
    """
    获取自己的主页作为起始也页面返回。
    """
    myself_soup = utils.get_links(
        session, "https://www.zhihu.com/settings/profile")
    my_url = myself_soup.find(
        "div", {"id": "js-url-preview", "class": "url-preview"})
    return "https://www." + my_url.get_text()


def get_followees(user_url):
    """
    获取一个用户的关注列表，如果关注人数很多，网站只会显示部分，其余的部分会AJAX动态刷新。我们只抓取初始的那部分。
    """
    user_followees_url = user_url + "/followees"
    followees_list = []
    followees_soup = utils.get_links(session, user_followees_url)
    for i in followees_soup.find_all("span", {"class": "author-link-line"}):
        followee_url = i.find("a").attrs['href']
        followees_list.append(followee_url)
    if followees_list:
        return followees_list
    raise NoFolloweeError


def crawl(url):
    """
    广度优先，执行抓取，如果抛出NoFolloweeError错误，就从UrlSet中随机选一个网址进行抓取。
    """
    followees = get_followees(url)
    one = get_next_url(followees)
    try:
        test_list = get_followees(one)
        put_into_queue(followees)
        print(one)
        crawl(one)
    except NoFolloweeError:
        next_random_url = conn.srandmember("UrlSet", 1)[0].decode("utf-8")
        crawl(next_random_url)


def main_from_me():
    """
    主程序，以自己的主页为起点，开始抓取。
    """
    account = input('Please input your account\n>  ')
    secret = input("input your secret\n>  ")
    login.login(session, secret, account)
    my_url = get_my_url()
    crawl(my_url)


def main_from_one(start_url):
    """
    主程序，以给定的主页为起点，开始抓取。如果程序因为某些原因中断的话，可以记录下最后一个URL，下一次再运行的时候可以从此处继续。
    """
    account = input('Please input your account\n>  ')
    secret = input("input your secret\n>  ")
    login.login(session, secret, account)
    crawl(start_url)

if __name__ == "__main__":
    main_from_me()
