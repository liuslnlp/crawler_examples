# 数据分析模块，暂未编写。
import matplotlib.pyplot as plt
import sqlite3

ipdict = dict()

conn = sqlite3.connect("wikidata.db")
cur = conn.cursor()

dataSet = list(cur.execute("select * from ipinfo"))

for data in dataSet:
    ipdict[data[2]] = 0

for data in dataSet:
    ipdict[data[2]] += 1

#print(ipdict)
sub = []

country = list(ipdict.keys())
for i in country:
    sub.append(ipdict[i])

ht = [i for i in range(len(sub))]
plt.bar(ht, sub)
plt.show()