# 数据分析模块，暂未编写。
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

ipdict = dict()

conn = sqlite3.connect("wikidata.db")
cur = conn.cursor()

dataSet = list(cur.execute("select * from ipinfo"))

for data in dataSet:
    ipdict[data[2]] = 0

for data in dataSet:
    ipdict[data[2]] += 1

# print(ipdict)
count = []

country = list(ipdict.keys())
for i in country:
    count.append(ipdict[i])

y_pos = np.arange(len(country))
plt.barh(y_pos, count, align='center', alpha=0.4)
plt.yticks(y_pos, country)
for count, y_pos in zip(count, y_pos):
    plt.text(count, y_pos, count,  horizontalalignment='center', verticalalignment='center', weight='bold') 
plt.subplots_adjust(bottom = 0, top = 2) 
plt.ylim(len(country), 0)
plt.ylabel('country')
plt.xlabel('count')
plt.show()
