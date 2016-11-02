'''
此处定义了爬虫的起始页面和程序运行时需要的一些常量。
'''

# 爬取一个页面后的等待时间。
INTERVALS = 2

# 被堵时再次访问的等待时间。
SLEEP_TIME = 40

# 是否开启多线程。
MULTITHREADING = False

# 选择数据库
# 选择使用的数据库，可选择MongoDB和Sqlite

# DATABASE = 'MongoDB'
DATABASE = 'Sqlite'

# 起始页面。
start_urls = [
    'http://www.lagou.com/zhaopin/C/?labelWords=label',
    'http://www.lagou.com/zhaopin/Java/?labelWords=label',
    'http://www.lagou.com/zhaopin/Python/?labelWords=label',
    'http://www.lagou.com/zhaopin/Android/?labelWords=label',
    'http://www.lagou.com/zhaopin/go/?labelWords=label',
    'http://www.lagou.com/zhaopin/html5/?labelWords=label',
    'http://www.lagou.com/zhaopin/PHP/?labelWords=label',
    'http://www.lagou.com/zhaopin/iOS/?labelWords=label',
    'http://www.lagou.com/zhaopin/Hadoop/?labelWords=label',
]