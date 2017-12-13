#coding=utf-8
__author__ = 'messageoom'
import time,os
from prettytable import PrettyTable
import smtplib
from config import globalparam
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CASE_COUNT = 0
SUCCESSFUL_COUNT = 0
FAILED_COUNT = 0

logpath = globalparam.getLogPath()
readconf = globalparam.read_config

def log_start():
    """
    Start log
    :return:
    """
    try:
        consoleMsg = 'Start to execute: (%s)\n'%time.strftime('%Y-%m-%d %H:%M:%S',
                                                           time.localtime(time.time()))
        logMsg =  'Start to execute(%s)\n'%time.strftime('%Y-%m-%d %H:%M:%S',
                                                      time.localtime(time.time()))
        print consoleMsg
        #logpath = globalparam.getLogPath()
        logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        with open(logname, 'wb') as f:
            f.write('%s\n' % logMsg)
    except IOError as e:
        raise IOError(e)

def log_end():
    try:
        #consoleMsg = 'End to executed:%-20d/%d(%-10s)'%(SUCCESSFUL_COUNT,CASE_COUNT,time.strftime('%Y-%m-%d %H:%M:%S',
        #                                                                                         time.localtime(time.time())))
        logMsg = 'End to executed: %d/%-5d(%s)'%(SUCCESSFUL_COUNT,CASE_COUNT,time.strftime('%Y-%m-%d %H:%M:%S',
                                                                                              time.localtime(time.time())))
        print logMsg
        #logpath = globalparam.getLogPath()
        logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        with open(logname, 'a') as f:
            f.write('%s\n' % logMsg)
    except IOError as e:
        raise IOError(e)



def creatTable():
    """
    Create a use case to perform the log table
    :return:
    """
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
        #logpath = globalparam.getLogPath()
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


def sendmail(addrs=readconf.getValue('Email','to_addrs')):
    """
    :param addrs: Review email address default：from .ini file
    :return:
    """
    # 第三方 SMTP 服务
    mail_host = readconf.getValue('Email','mail_host')
    mail_user = readconf.getValue('Email','mail_user')
    mail_pass = readconf.getValue('Email','mail_pass')
    sender = mail_user # 发件人
    if addrs is None:
        return
    else:
        to_addrs = addrs.split(',')#["{}".format(addrs)]  # 接收邮件

        msg_multil = MIMEMultipart()

        message = MIMEText('{}'.format( readconf.getValue('Email','MIMEText')), 'plain', 'utf-8')
        msg_multil['From'] = "{}".format(sender)
        msg_multil['To'] = to_addrs[0]#Header("%s"%to_addrs,)
        subject = '{}'.format( readconf.getValue('Email','subject'))
        msg_multil['Subject'] = Header(subject, 'utf-8')
        msg_multil.attach(message)
        #加入测试相关附件
        logname = os.path.join(logpath, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        data = MIMEText(open(logname,'rb').read(), 'base64', 'utf-8')
        data["Content-Disposition"] = 'attachment; filename="2017-12-13.log"'
        msg_multil.attach(data)

        try:
            smtpObj = smtplib.SMTP_SSL()
            smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(mail_user, to_addrs, msg_multil.as_string())
            smtpObj.quit()
            print "测试报告已发送至此邮件: {}".format(to_addrs)
        except smtplib.SMTPException as e:
            raise e
