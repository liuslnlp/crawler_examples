# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings
from sqlite3 import connect

class CsdnblogPipeline(object):
    """
    MongoDB储存管道。
    """

    def __init__(self):
        # 数据库的host和port保存在settings.py中
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        client = MongoClient(host=host, port=port)
        db = client['CSDN']
        self.col = db['csdn']

    def process_item(self, item, spider):
        csdnInfo = dict(item)
        self.col.insert(csdnInfo)
        return item


class CsdnblogBySqlitePipeline(object):
    """
    SQLite储存管道，默认关闭，如果电脑上没有安装MongoDB，可在设置中启用
    此管道。
    """

    def __init__(self):
        self.db = connect("csdn.db")
        self.cur = self.db.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS blog (
            title VARCHAR(100) PRIMARY KEY,
            author VARCHAR(100),
            content TEXT,
            tag VARCHAR(200),
            date VARCHAR(100),
            digg_num VARCHAR(100),
            bury_num VARCHAR(100),
            read_num VARCHAR(100)
        )''')
    
    def store(self, title, author, content, tag, date, digg_num, bury_num, read_num):
        arg = (title, author, content, tag, date, digg_num, bury_num, read_num)
        insert_sql = "INSERT INTO blog (title, author, content, tag, date, digg_num, bury_num, read_num) values(?,?,?,?,?,?,?,?)"
        self.cur.execute(insert_sql, arg)
        self.db.commit()

    def process_item(self, item, spider):
        csdnInfo = dict(item)
        title = csdnInfo['title']
        content = csdnInfo['content']
        date = csdnInfo['date']
        author = csdnInfo['author']
        digg_num = csdnInfo['digg_num']
        bury_num = csdnInfo['bury_num']
        read_num = csdnInfo['read_num']
        tags = csdnInfo['tags']
        tag = ','.join(tags)
        self.store(title, author, content, tag, date, digg_num, bury_num, read_num)
        return item 

        