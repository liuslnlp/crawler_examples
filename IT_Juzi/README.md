# IT JuZi Spider
IT橘子是一家内容包括：公司、创业者、细分领域、投资机构、投资者、投资事件、新闻等的网站，该爬虫可以对该网站上的公司，和投资事件两个部分的数据进行抓取，并保存到MongoDB中。  
## 需要额外安装的库
* requests  
`pip3 install requests`  
* BeautifulSoup  
`pip3 install bs4`  
* lxml  
`pip3 install lxml`  
* pymongo(需要提前安装MongoDB)   
`pip3 install pymongo`

## 使用方法  
直接在`main`函数中设定好抓取的范围，然后运行`main.py`,抓取的信息将保存在`MongoDB`中的`companies`和`eventies`两个集合中。  

