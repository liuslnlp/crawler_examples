#    Copyright 2016 WiseDoge

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import pymongo
import json
from Error import MongoClientError


# 加载设置
val = json.load(open("setting.json"))

"""
接受一个数据dict，存入数据库。
example:
{'Business_item': '计算机软件', 'Education_extra_item': '软件学院', 
 'Presentation': '专业造轮子,拉黑抢前排。http://gaclib.net',
 'Employment_item': 'Microsoft Office', 'Location_item': '西雅图（Seattle）', 
 'Education_item': '华南理工大学', 'Name': 'vczh', 'Position_item': 'Developer',
 'Followees': "1742", 'Followees': "404583"}
"""

# MongoDB
try:
    client = pymongo.MongoClient(
        host=val['mongodb']['host'], port=val['mongodb']['port'])
except:
    raise MongoClientError
db = client['Zhihu']
col = db['Users']


def store_by_mongodb(data_dict):
    col.insert_one(data_dict)


# MySQL
# ......


# Sqlite
# ......
