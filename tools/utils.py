#coding=utf-8
__author__ = 'messageoom'
import time,os
from config import globalparam
from prettytable import PrettyTable

CASE_COUNT = 0
SUCCESSFUL_COUNT = 0
FAILED_COUNT = 0


def log_start():
    try:
        consoleMsg = 'start execution: (%s)'%time.strftime('%Y-%m-%d %H:%M:%S',
                                                           time.localtime(time.time()))
        logMsg =  'start execution(%s)'%time.strftime('%Y-%m-%d %H:%M:%S',
                                                      time.localtime(time.time()))
        print consoleMsg
        logpath = globalparam.getLogPath()
        logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        with open(logname, 'wb') as f:
            f.write('%s\n' % logMsg)
    except IOError as e:
        raise IOError(e)


def creatTable():
    x = PrettyTable(["EXECUTE CASE", "EXECUTE TIME", "EXECUTE RESULT"])
    x.align["EXECUTE CASE"] = "l"  # Left align city names
    x.padding_width = 2  # One space between column edges and contents (default)
    return x
def log_result(case, result):
    global CASE_COUNT, SUCCESSFUL_COUNT, FAILED_COUNT
    table = creatTable()
    test_time = time.strftime('%Y-%m-%d %H:%M:%S',
                              time.localtime(time.time()))
    table.add_row(["%s"%case,"%s"%test_time,"%s"%result])
    try:
        CASE_COUNT += 1
        if result == 'SUCCESSFUL':
            SUCCESSFUL_COUNT += 1
        else:
            FAILED_COUNT += 1
        logpath = globalparam.getLogPath()
        logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        with open(logname, 'a') as f:
            f.write('%s\n' % table)
        return table
    except IOError as e:
        raise IOError(e)


log_start()
#log_result("test1","SUCCESSFUL")
#log_result("test1","FAILED")

for i in range(2):
    print log_result("test%s"%i,"FAILED").add_row(["test%s"%i,"%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"FAILED%s"%i])




