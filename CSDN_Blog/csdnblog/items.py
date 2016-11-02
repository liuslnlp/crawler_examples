# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnblogItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    read_num = scrapy.Field()
    tags = scrapy.Field()
    digg_num = scrapy.Field()
    bury_num = scrapy.Field()
