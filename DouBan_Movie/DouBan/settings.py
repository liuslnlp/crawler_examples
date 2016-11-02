# -*- coding: utf-8 -*-

# Scrapy settings for DouBan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DouBan'

SPIDER_MODULES = ['DouBan.spiders']
NEWSPIDER_MODULE = 'DouBan.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'

ROBOTSTXT_OBEY = True
COOKIES_ENABLED = True
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'DouBan'
MONGODB_DOCNAME = 'Movies'

ITEM_PIPELINES = {
    'DouBan.pipelines.DoubanPipeline': 1,
}




