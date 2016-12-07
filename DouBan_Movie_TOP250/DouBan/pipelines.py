# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings

class DoubanPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        name = settings['MONGODB_DBNAME']
        client = MongoClient(host=host,port=port)
        db = client[name]
        self.col = db[settings['MONGODB_DOCNAME']]
    def process_item(self, item, spider):
        movieInfo = dict(item)
        self.col.insert(movieInfo)
        return item
