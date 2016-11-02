# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field()
    info = scrapy.Field()
    star = scrapy.Field()
    evaNum = scrapy.Field()
    quote = scrapy.Field()
