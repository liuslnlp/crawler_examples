from urllib.request import urlopen
from pymongo import MongoClient

# 抽取出照片的网址，下载，保存在pic文件夹中
def downPic():
    client = MongoClient()
    db = client.TaoBao 
    col = db.TaoLady
    for data in col.find():
        name = data['realName']
        url = "http:" + data['avatarUrl']
        pic = urlopen(url)
        with open("pic/" + name + ".jpg", "wb") as file:
            print(name)
            file.write(pic.read())


if __name__ == '__main__':
    downPic()