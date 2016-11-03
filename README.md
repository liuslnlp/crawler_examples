# Spider Hub

总结了一下自己学习爬虫过程中做过的小项目。  

## 运行环境

Windows/Linux/Mac OS       

Python 3.5.2

## 可能会用到的第三方库

* requests
* bs4
* pillow
* lxml
* pymongo
* scrapy
* Numpy
* redis
* pillow
* matplotlib

## 可能要用到的其他程序

* MongoDB
* Redis

## 内容

* Baidu_Picture : 百度贴吧图片爬虫，可以爬取给定帖子内的全部图片。
* CSDN_Blog : CSDN博客爬虫， 基于scrapy，可以从起始URL开始，抓取博客的标题、内容、作者、修改日期、标签等信息保存到数据库中，并进入下一页继续抓取。
* DouBan_Movie : 豆瓣电影爬虫，基于scrapy，可以抓取豆瓣电影TOP 250并保存在MongoDB中。
* IT_Juzi : IT橘子爬虫，可以从IT桔子网站上抓取近期融资的公司和最近的融资大事件)。
* QiuShi : 糗事百科爬虫，可以定时抓取糗事百科上的笑话，并将其推送到手机。
* TaoBao_Lady : 淘女郎爬虫，可抓取淘女郎的信息和照片。
* Lagou : 拉勾网爬虫，可爬取拉勾网的招聘信息并生成报告。
* ZhiHu : 知乎网爬虫，可以抓取知乎用户的个人信息，提供了分布式版本。
* Wikipedia :  维基百科爬虫，可以抓取维基百科的词条贡献者的IP，并统计出他们的国家分布，提供了分布式版本。


**详细的说明请点开具体的文件夹查看**

## 目录树

```
├─Baidu_Picture
│  └─pic
├─CSDN_Blog
│  └─csdnblog
│      └─spiders           
├─DouBan_Movie
│  └─DouBan
│      └─spiders
├─IT_Juzi
├─Lagou
├─QiuShi
├─TaoBao_Lady
│  └─pic
├─Wikipedia
│  ├─分布式
│  │  ├─Client
│  │  └─Server
│  └─单机多线程
└─ZhiHu
```

