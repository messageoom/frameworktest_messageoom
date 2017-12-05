#coding=utf-8
__author__ = 'messageoom'
import time,os
from config import globalparam
from prettytable import PrettyTable

CASE_COUNT = 0
SUCCESSFUL_COUNT = 0
FAILED_COUNT = 0


def log_start():
    """
    Start log
    :return:
    """
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
table = creatTable()
def log_result():
    """
    Output the results to the console and log files
    :return:
    """
    print table
    try:
        logpath = globalparam.getLogPath()
        logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        with open(logname, 'a') as f:
            f.write('%s\n' % table)

    except IOError as e:
        raise IOError(e)

def log_execute(case, result):
    """
    The log files are executing
    :param case:
    :param result:
    :return:
    """
    global CASE_COUNT, SUCCESSFUL_COUNT, FAILED_COUNT
    test_time = time.strftime('%Y-%m-%d %H:%M:%S',
                              time.localtime(time.time()))
    try:
        CASE_COUNT += 1
        if result == 'SUCCESSFUL':
            SUCCESSFUL_COUNT += 1
        else:
            FAILED_COUNT += 1
        table.add_row(["%s"%case,"%s"%test_time,"%s"%result])
        #logpath = globalparam.getLogPath()
        #logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        #with open(logname, 'a') as f:
        #    f.write('%s\n' % table)

    except IOError as e:
        raise IOError(e)