# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class DoubanmoviePipeline(object):
    """
    MongoDB储存管道。
    """

    def __init__(self):
        client = MongoClient()
        db = client['doubanMovies']
        self.col = db['MOVIE']

    def process_item(self, item, spider):
        csdnInfo = dict(item)
        self.col.insert(csdnInfo)
        return item
