#coding=utf-8
__author__ = 'messageoom'

import os
from public.commn.readconfig import meReadconfig

# 读取配置文件
config_file_path = os.path.split(os.path.realpath(__file__))[0]
#read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# 项目参数设置
prj_path = meReadconfig().getValue('projectConfig','project_path')
# 日志路径
log_path = os.path.join(prj_path, 'report', 'log')
# 截图文件路径
img_path = os.path.join(prj_path, 'report', 'image')
# 测试报告路径
report_path = os.path.join(prj_path, 'report', 'testreport')
# default browser
browser = 'chrome'

# 测试数据路径
data_path = os.path.join(prj_path, 'data', 'testdata')

# web测试项目主页
base_url = "http://merchants.guxiansheng.cn"
# google 浏览器驱动路径
chromedriverpath = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"