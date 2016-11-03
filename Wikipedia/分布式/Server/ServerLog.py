import time

'''
将信息写入ServerLog.log中作为记录。
例如：writeLog("URLError")

ServerLog.log:
[Wed Jul 27 12:28:13 2016] URLError
'''

def writeLog(message):
    with open("ServerLog.log", "a") as logFile:
        logFile.write('[' + time.asctime() + ']' + ' ' + message + '\n')