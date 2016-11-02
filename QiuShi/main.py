from bs4 import BeautifulSoup
from email.mime.text import MIMEText

import requests
import smtplib
import lxml
import time
import settings

def sendEmail(title, text):
    """
    以title为标题，text为内容，发送邮件。
    """
    msg = MIMEText(text)
    msg['Subject'] = title
    msg['From'] = settings.FROM_MAIL
    msg['To'] = settings.TO_MAIL
    s = smtplib.SMTP(settings.SMTP_SERVER)
    s.login(settings.FROM_MAIL_USERNAME, settings.FROM_MAIL_PASSWORD)
    s.send_message(msg)
    s.quit()


def sendToMe(data_list):
    """
    将一次抓取的内容进行整理和去重，以时间为标题，发送。
    """
    email_text  = ''
    for i in data_list:
        email_text += (i + "\n\n")
    try:
        sendEmail(time.ctime(), email_text)
    except:
        with open("log.log","a") as file:
            file.write("Send email error on " + time.ctime() + "\n")
        print("Error on",time.ctime())
        return
    print("Success",time.ctime())

def crawl(url):
    """
    从给定的URL中提取出内容，并以列表的形式返回。
    """
    try:
        html = requests.get(url)
    except:
        with open("log.log","a") as file:
            file.write("Http error on " + time.ctime())
        time.sleep(60)
        return None
    soup = BeautifulSoup(html.text, 'lxml')
    data_list = []
    for cont in soup.find_all("div", {"class":"content"}):
        raw_data = cont.get_text()
        data = raw_data.replace("\n","")
        data_list.append(data)
    return data_list
    
def main():
    """
    主程序，将前5页的URL传给爬虫，并收集抓取的数据，传给发送函数。
    """
    data_list = []
    for i in range(1,settings.PAGES + 1):
        url = 'http://www.qiushibaike.com/text/page/%s/'%str(i)
        temp_data = crawl(url)
        data_list.extend(temp_data)
    sendToMe(data_list)
    

if __name__ == '__main__':
    while True:
        main()
        time.sleep(settings.INTERVALS)