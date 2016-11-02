import sqlite3
from pymongo import MongoClient
from settings import DATABASE

def storeBySqlite(table, name, industry, position, requirement, welfare, salary):
    """
    将数据存入sqlite数据库。
    """
    conn = sqlite3.connect("employData.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS " + table +
                " (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(90), industry text, position text, requirement text, welfare text, salary text)")
    try:
        cur.execute("INSERT INTO " + table +
                     " (name, industry, position, requirement, welfare, salary) VALUES (?,?,?,?,?,?)", (name, industry, position, requirement, welfare, salary))
        conn.commit()
    finally:
        cur.close()
        conn.close()


if DATABASE == 'MongoDB':
    client = MongoClient()
    db = client['lagou']


def storeByMongo(table, name, industry, position, requirement, welfare, salary):
    """
    将数据存入MongoDB。
    """
    global db
    col = db[table]
    data = {"name":name, "industry":industry, "position":position, "requirement":requirement, "welfare":welfare, "salary":salary}
    try:
        col.insert_one(data)
    except:
        pass

if DATABASE == 'MongoDB':
    store = storeByMongo
elif DATABASE == 'Sqlite':
    store = storeBySqlite

