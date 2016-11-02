import numpy as np

import sqlite3


class SALARYError(Exception):
    """
    异常类，用来处理薪水解析异常。
    """
    def __init__(self, str):
        self.description = str
    def __str__(self):
        return repr("Error in field \'salary\', The value \'" + self.description + "\'is unable to resolve")


 
def readData(table):
    """
    从数据库中读入数据。
    """
    conn = sqlite3.connect("employData.db")
    cur = conn.cursor()
    data_set = list(cur.execute("SELECT * FROM " + '['+table+']'))
    return np.array(data_set)

 
def dealSalary(raw_str):
    """
    将数据库中提取的原始薪水数据进行解析和加工。
    """
    if '-' in raw_str:
        temp_salary_list = raw_str.split('-')
        min_salary = temp_salary_list[0][:-1]
        max_salary = temp_salary_list[1][:-1]
        return (int(min_salary), int(max_salary))
    elif '以上' in raw_str:
        temp_salary = raw_str.replace("k以上", '')
        return (int(temp_salary), int(temp_salary))
        
    elif '以下' in raw_str:
        temp_salary = raw_str.replace("k以下", '')
        return (int(temp_salary), int(temp_salary))
    else:
        raise SALARYError(raw_str)


def salaryAns(field):
    """
    对薪水进行分析。
    """
    dataSet = readData(field)
    count = 0
    minsalary = 300
    maxsalary = 0
    for data in dataSet:
        tmin, tmax = dealSalary(data[6])
        minsalary = min(minsalary, tmin)
        maxsalary = max(maxsalary, tmax)
        count += (tmin + tmax)
    ave_salary = count/(2*len(dataSet))
    print("Minimum salary: " + str(minsalary)  + 'k')
    print("Maximum salary: " + str(maxsalary)  + 'k')
    print("Average salary: " + str("%.3f" % ave_salary) + 'k')


def getPosition(raw_str):
    """
    将数据库中提取的原始工作地数据进行解析和加工。
    """
    if '·' in raw_str:
        temp_position_list = raw_str.split('·')
        return temp_position_list[0]
    else:
        return raw_str


def positionAns(field):
    """
    对工作地信息进行分析。
    """
    dataSet = readData(field)
    posDic = {}
    for data in dataSet:
        pos = getPosition(data[3])
        if pos in posDic:
            posDic[pos] += 1
        else:
            posDic[pos] = 1
    pocList = []
    for i in posDic:
        pocList.append((i, posDic[i]))
    pocList.sort(key = lambda lis: lis[1], reverse = True)
    print("Distribution of the workplace:", end = ' ')
    for i in range(5):
        print(pocList[i][0] + '(%s)'%pocList[i][1], end = ' ')
    print('\n')


def analyse(field):
    """
    主程序，整合。
    """
    print('--------------------------------{0:^10}--------------------------------'.format(field))
    salaryAns(field)
    positionAns(field)


if __name__ == '__main__':  
    analyse("Java")
    analyse(".Net")
    analyse("Python")
    analyse("Android")
    analyse("iOS")
    analyse("C")
    analyse("PHP")
    analyse("CTO")



