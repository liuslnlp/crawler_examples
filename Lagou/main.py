from spider import getBsObj, getInfo
from settings import start_urls, MULTITHREADING, INTERVALS

import time
import dbAPI
import threading

def runSingleSpider(start_url):
    """
    对一个起始网页进行抓取。
    """
    table = '[' + start_url.split('/')[4] + ']'
    while len(start_url) > 0:
        bsObj = getBsObj(start_url)
        start_url = getInfo(bsObj, table)
        time.sleep(INTERVALS)

class Spider(threading.Thread):
    """
    将runSingleSpider函数包装为线程。
    """
    def __init__(self, url, thread_num):
        threading.Thread.__init__(self)
        self.start_url = url
        self.thread_num = thread_num
    
    def run(self):
        runSingleSpider(self.start_url)
        print("Thread #" + str(self.thread_num) + " finished!")

 
def main():
    """
    多线程模式主函数。
    """
    threads = []
    print("Running!")
    flag = 1
    for start_url in start_urls:
        Spider_thread = Spider(start_url, flag)
        threads.append(Spider_thread)
        flag += 1
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print("Finished!")
 
def _main():
    """
    单线程模式主函数。
    """
    print("Running!")
    for start_url in start_urls:
        runSingleSpider(start_url)
    print("Finished!")


if __name__ == '__main__': 
    if MULTITHREADING == True:
        main()
    else:
        _main()
        

