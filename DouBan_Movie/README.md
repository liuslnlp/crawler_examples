# DouBan Spider
基于Scrapy框架的爬虫，可抓取豆瓣电影Top 250，并保存到MongoDB中。  
## 运行环境
Python 3.5.1  
Scrapy 1.1.1
## 需要安装的第三方包
scrapy  
`pip install scrapy`
## 配置方法
将`setting.py`的以下信息根据需要进行修改   
```
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'DouBan'
MONGODB_DOCNAME = 'Movies'
```
## 运行方法 
将文件夹定位到DouBan下，然后   
`scrapy crawl doubanSpider`

