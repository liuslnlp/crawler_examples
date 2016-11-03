import sqlite3


def showIpInfo():
    '''
    查看数据库中ipinfo表的信息
    '''
    conn = sqlite3.connect("wikidata.db")
    cur = conn.cursor()
    List = cur.execute("SELECT * FROM ipinfo")
    for data in List.fetchall():
        print(data)
    cur.close()
    conn.close()


def showPages():
    '''
    查看数据库中pages表的信息
    '''
    conn = sqlite3.connect("wikidata.db")
    cur = conn.cursor()
    List = cur.execute("SELECT * FROM pages")
    for data in List.fetchall():
        print(data)
    cur.close()
    conn.close()


def showDataNum():
    '''
    查询pages页和ipinfo页的记录数
    '''
    conn = sqlite3.connect("wikidata.db")
    cur = conn.cursor()
    maxID = cur.execute("SELECT max(id) FROM ipinfo")
    ipNum = list(maxID)[0][0]
    maxID = cur.execute("SELECT max(id) FROM pages")
    urlNum = list(maxID)[0][0]

    print("The amount of pages data:", urlNum)
    print("The amount of IP data:", ipNum)

if __name__ == '__main__':
    # showPages()
    # showIpData()
    showDataNum()
