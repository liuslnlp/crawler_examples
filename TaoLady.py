from pymongo import MongoClient

import requests
import json

# 发送请求，得到JSON数据，将其加工并转化为Python的字典类型返回
def getInfo(pageNum):
    tao_data = {"viewFlag":"A", "currentPage": pageNum}
    try:
        r = requests.post("https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8", data = tao_data)
    except:
        return None
    raw_datas = json.loads(r.text)
    datas = raw_datas['data']['searchDOList']
    return datas

# 连接到MongoDB， 将信息保存
def main():
    client = MongoClient()
    db = client.TaoBao 
    col = db.TaoLady
    
    # 淘女郎一共有410页，所以我们抓取从1到第411页的内容。
    for pageNum in range(1, 411):
        print(pageNum)
        datas = getInfo(pageNum)
        if datas:
            col.insert_many(datas)


if __name__ == '__main__':
    main()


