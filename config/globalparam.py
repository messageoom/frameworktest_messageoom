#coding=utf-8
__author__ = 'messageoom'

import os
import time
from config.readconfig import meReadconfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
confile = os.path.join(config_file_path,'config.ini')
read_config = meReadconfig(confile)
# get cookies
#cookies = read_config.getValue('Auth','cookies')
# 项目参数设置
prj_path = read_config.getValue('projectConfig','project_path')
def getLogPath():
    """
    creat log path
    """
    log_path = os.path.join(prj_path, 'report', 'log')
    if os.path.exists(log_path):
        return log_path
        pass
    else:
        os.makedirs(log_path)
        return log_path
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# web测试项目主页
base_url = "base_url"

# default browser
browser = 'chrome'
# google 浏览器驱动路径
chromedriverpath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
