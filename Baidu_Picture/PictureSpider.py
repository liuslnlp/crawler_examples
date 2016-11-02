import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

#将网址加工成BeautifulSoup对象，便于进行后续处理
def getObj(url): 
    page = urlopen(url)
    html = page.read()
    bsobj = BeautifulSoup(html)
    return bsobj

#从BeautifulSoup对象中挑出图片列表
def getImg(bsobj):
    imglist = bsobj.findAll("img")
    return imglist

#找出网页的最后一页的页码，便于确定spider的终止条件
def getLast(bsobj):
    htmllist = bsobj.findAll("a")
    for html in htmllist:
        if html.get_text() == "尾页":
            lasthtml = html.attrs['href']
            for i in range(len(lasthtml)):
                if lasthtml[i] == '=':
                    return int(lasthtml[i+1:])
            

imgName = 0
pageNum = 1

#将HTML改成需要的下载的帖子的网址即可
html = "http://tieba.baidu.com/p/4618317103"
MAXN = getLast(getObj(html))

for pageNum in range(1, MAXN + 1):
    chtml = html + ("?pn=%d" % pageNum)
    imgList = getImg(getObj(chtml))
    for imgPath in imgList:
        print("正在下载第%d张" % imgName)
        f = open("pic/"+str(imgName)+".jpg", 'wb')
        f.write((urlopen(imgPath.attrs['src'])).read())
        f.close()
        imgName += 1    


print("All Done!!!!!!!!!")
