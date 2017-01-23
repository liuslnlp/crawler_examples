# CSDN Spider
基于Scrapy的CSDN博客爬虫，可稳定抓取CSDN大量博客内容并保存到MongoDB中。
经过检验，可以抓取200W条以上的数据，这个数量还在继续上涨。
## 解决依赖
* pymongo  
  `pip3 install pymongo`
* scrapy  
  `pip3 install scrapy`

## Usage

`$ scrapy crawl csdn`

## 注意事项

* 如何电脑上没有安装MongoDB，可以在`settings.py`中关闭MongoDB的管道，打开Sqlite的管道，这样抓取到的数据就可以保存在Sqlite中了。


  ​