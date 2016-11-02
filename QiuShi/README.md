# QiuShi Spider  
糗事百科（http://www.qiushibaike.com/）  是一个实时更新的笑话网站，会在主页实时显示出最新，最热门的笑话。我们在这里利用Python来制作一个爬虫，该爬虫可以定时对糗事百科进行扫描，将其前五页的笑话打包，并推送到自己的手机，只要该爬虫运行在一个稳定的服务端上，就可以长期运行。
 
## 需要额外安装的库  
* BeautifulSoup   
`$ pip3 install bs4`
* requests  
`$ pip3 install requests`
* lxml  
`$ pip3 install lxml`  
  
## Usage  
* 在自己的手机上装一个可接收实时推送的邮箱软件（如网易邮箱大师）。    
* 在`setting.py`中设置好收发件的邮箱和SMTP服务器。  
* 然后再运行`main.py`，并保证机器常开，程序不会终止运行。  
