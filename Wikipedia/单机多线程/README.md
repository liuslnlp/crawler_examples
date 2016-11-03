# Wikipedia Spider
基于Python的Wikipedia爬虫。 可以爬取维基百科每个词条的标题和摘要，记录下词条贡献者的IP，用API查出贡献者的国家，最后将以上数据存入Sqlite数据库。
## 模块说明  
* `GetAbstract.py` ：摘要抓取模块，用于抓取词条的标题和摘要。
* `GetLocal.py`  ：IP爬取和分析模块，用于爬取词条的贡献者IP并分析出贡献者所在的国家。
* `Coordinate.py` ： 爬虫的入口，用于设置起始网页和运行爬虫。
* `manage.py`  ：管理模块，用于查看爬取进度和数据库的数据量。  
* `settings.py`  ：常量设置模块，用来设置线程数，启示页面，休眠时间等。


* `Analysis.py`  ：分析，统计词条贡献者的国家分布。  

## 原理  
*******************
运行`Coordinate.py`，Python将创建N+1个线程，主线程负责获取起始页的HTML代码并转化为BeautifulSoup对象，从中获取标题和摘要，存入数据库，并将标题作为link放入缓冲队列`links_queue`中，同时提取出一个随机内链，作为下一次循环的起始页，开始下一次循环；同时其他N个线程不断地从缓冲队列`links_queue`中获取link将其转化为BeautifulSoup对象，从而从中提取出贡献者的IP，然后调用*freegeoip*的API查询IP的归属地，最后将IP和其归属地存入数据库。  
![image](/Frame Diagram.png)  

