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

from PIL import Image
import requests
import time
import re


# Request headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.'
}


def get_xsrf(session):
    """
    xsrf 是一个动态变化的参数，提交请求时必须提交xsrf，此函数用来获取xsrf。
    """
    index_url = 'http://www.zhihu.com'

    # 获取登录时需要用到的_xsrf
    html = session.get(index_url, headers=headers)
    pattern = r'name="_xsrf" value="(.*?)"'
    
    # 这里的_xsrf 返回的是一个list
    _xsrf = re.findall(pattern, html.text)
    return _xsrf[0]


def get_captcha(session):
    """
    获取验证码。
    """
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)

    img = Image.open('captcha.jpg')
    img.show()
    img.close()

    captcha = input("please input the captcha\n>")
    return captcha


def login(session, secret, account):
    """
    通过输入的用户名判断是否是手机号。
    """
    if re.match(r"^1\d{10}$", account):
        print("Phone login \n")
        post_url = 'http://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': get_xsrf(session),
            'password': secret,
            'remember_me': 'true',
            'phone_num': account,
        }
    else:
        print("E-mail login \n")
        post_url = 'http://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': get_xsrf(session),
            'password': secret,
            'remember_me': 'true',
            'email': account,
        }
    try:
        # 不需要验证码直接登录成功
        login_page = session.post(post_url, data=postdata, headers=headers)
        print(login_page.status)
        print(login_page.text)
    except:
        # 需要输入验证码后才能登录成功
        postdata["captcha"] = get_captcha(session)
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = eval(login_page.text)
        print(login_code['msg'])


if __name__ == '__main__':
    """
    测试。
    """
    session = requests.session()
    account = input('Please input your account\n>  ')
    secret = input("input your secret\n>  ")
    login(session, secret, account)

