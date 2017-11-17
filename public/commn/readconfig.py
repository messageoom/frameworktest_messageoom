#coding=utf-8
__author__ = 'messageoom'

import ConfigParser
import codecs

class meReadconfig(object):
    """
    专门读取配置文件的，.ini文件格式
    """

    def getValue(self,section=None,option=None):
        """
        :param section:INI文件中的节
        :param option:INI文件中节中的键
        """
        inipath = "../config/config.ini"
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(inipath)
        return self.cf.get(section,option)

# TODO 优化获取value时产生的异常
"""

    def __init__(self, filename):
        # configpath = os.path.join(prjDir,filename)
        configpath = filename
        # print(configpath)
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = ConfigParser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self, env, name):

        #[projectConfig]
        #project_path=E:/Python-Project/UItestframework
        #:param env:[projectConfig]
        #:param name:project_path
        #:return:E:/Python-Project/UItestframework

        return self.cf.get(env,name)

"""


