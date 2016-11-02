# CSDN Spider
基于Scrapy的CSDN博客爬虫，可稳定抓取CSDN大量博客内容并保存到MongoDB中。
## 解决依赖
* pymongo  
  `pip3 install pymongo`
* scrapy  
  `pip3 install scrapy`

## Usage

`$ scrapy crawl csdn`

## 注意事项

* 如何电脑上没有安装MongoDB，可以在`settings.py`中关闭MongoDB的管道，打开Sqlite的管道，这样抓取到的数据就可以保存在Sqlite中了。

* 刚开始抓取时的速度会非常快，但是当抓取的数据在60W条左右的时候会越来越慢（会降到1条/S左右）。

  ​