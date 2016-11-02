from pymongo import MongoClient
from threading import Thread
from spider import getLinks, crawlCompany, crawlEvent

import time

# Initialize MongoDB
client = MongoClient()
db = client['IT_Juzi']
col1 = db['companies']
col2 = db['eventies']


class CompanySpider(Thread):

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        super().__init__()        
        
    def run(self):
        for i in range(self.begin, self.end):
            print("Companies page %s" % str(i))
            url = "http://www.itjuzi.com/company?page=%s" % str(i)
            bsObj = getLinks(url)
            data = crawlCompany(bsObj)
            col1.insert_many(data)
            time.sleep(4)
        

class EventSpider(Thread):
    
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
        super().__init__()
    
    def run(self):
        for i in range(self.begin, self.end):
            print("Eventies page %s" % str(i))
            url = "https://www.itjuzi.com/investevents?page=%s" % str(i)
            bsObj = getLinks(url)
            data = crawlEvent(bsObj)
            col2.insert_many(data)
            time.sleep(4)


def main():
    """
    主函数
    """
    print("Start!")
    companyThread = CompanySpider(195, 3342)
    eventThread = EventSpider(1, 1531)
    
    companyThread.start()
    eventThread.start()

    companyThread.join()
    eventThread.join()
    print("Success!")
if __name__ == '__main__':
    main()
