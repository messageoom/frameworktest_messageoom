__author__ = 'messageoom'

import config

test_auth = None
test_admin_auth = None
other_auth = None

class Auth(object):
    scheme = 'http'

    def __init__(self, server, port, cookies=None):
        if cookies:
            self.cookies = cookies
        self.auth = cookies
        authority = "{server}:{port}".format(server=server, port=port)
        self.base_url = "{scheme}://{authority}".format(
            scheme=self.scheme,
            authority=authority,
        )












import csv
import codecs
import random

def random_str(randomlength=7):
    str = ''
    chars = '0123456789'
    length = len(chars) - 1
    from random import Random
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def creatCSVData():
    csvfile = file('importcsv02.csv', 'wb')
    #处理中文乱码
    csvfile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvfile)
    writer.writerow(["姓名", "电话", "QQ", "微信","身份证号","来源：1股先生，2微信推广，3其他"])
    for i in range(60000,60500):
        data = [('MS%s'%i, '1518%s'%random_str(), '', 'MSWeiXin%s'%i, "'5132%s%s"%(random_str(),random_str()), '%s'%random.randint(1, 3))]
        writer.writerows(data)
        csvfile.close()

if __name__ == "__main__":
    creatCSVData()