#coding=utf-8
__author__ = 'messageoom'

import ConfigParser
import codecs

class meReadconfig(object):
    """
    专门读取配置文件的，.ini文件格式
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

    def getValue(self, section, option):
        """
        :param section:INI文件中的节
        :param option:INI文件中节中的键
        """
        return self.cf.get(section,option)

    def deleteOption(self,section, option):
        """
        delete option
        :param section:
        :param option:
        """
        self.cf.remove_option(section, option)
