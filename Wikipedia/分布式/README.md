# Wikipedia Spider（V 2.0.0）
基于Python的Wikipedia爬虫。 可以爬取维基百科每个词条的标题和摘要，记录下词条贡献者的IP，用API查出贡献者的国家，最后将以上数据存入Sqlite数据库。    
## 模块说明  
### Server
* `RunServer.py` ：运行服务端程序。  
* `ServerLog.py` ：用于记录日志和错误。
* `settings.py`  ：常量设置模块，用来设置启示页面，休眠时间等。  

### Client
* `GetLocal.py`  ：IP爬取和分析模块，用于爬取词条的贡献者IP并分析出贡献者所在的国家。    
* `settings.py`  ：常量设置模块，用来设置启示页面，休眠时间等。  
* `RunSpider.py` ：运行客户端程序。  

## 其他
* `Analysis.py`  ：数据分析。  

## 原理  
*******************
### 服务端（生产者端）

运行`RunServer.py`，服务端程序负责获取起始页的HTML代码并转化为BeautifulSoup对象，从中获取Link，将Link存入Redis队列尾部，依次循环。  

### 客户端（消费者端）

运行`RunSpider.py`，客户端将连接至Redis，从队列头部取出Link，并从队列中敲除，然后进行抓取，将结果存入数据库。

