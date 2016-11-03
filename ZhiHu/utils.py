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

from bs4 import BeautifulSoup
from requests import HTTPError, URLRequired

"""
工具包
"""

# 设置文件在setting.json
# 注意：代理设置的格式为 ip:port ，例如： "123.123.123.123:8080"
# 如果不想使用代理，请将proxy的值设为"No"
# 请使用HTTP代理，其他格式的代理将无法被识别


def get_links(session, url, proxy = None):
    """
    Receive a url, and return a BeautifulSoup object
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.',
    }
    try:
        html = session.get(url, proxies = proxy, headers=headers)
        soup = BeautifulSoup(html.text, "lxml")
        return soup
    except URLRequired:
        return None
    except HTTPError:
        print("HTTPError")


    
