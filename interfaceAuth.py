#coding=utf-8
__author__ = 'messageoom'
import re
import os
import ConfigParser
import requests
from config.readconfig import meReadconfig

def loginSys():
    """
    login system & get cookies
    """
    global crm_coikies
    crmCookies = {}
    config_file_path = os.path.split(os.path.realpath(__file__))[0]
    configPathFile = os.path.join(config_file_path,'config//config.ini')
    read_config = meReadconfig(configPathFile)
    URL = read_config.getValue(section='BaseData',option='baseurl')
    loginData = {"loginusername": read_config.getValue(section='BaseData',option='username'),
                 "loginpassword": read_config.getValue(section='BaseData',option='password')}
    try:
        reLogin = requests.post(url = URL,data = loginData)
        originalCookie = str(reLogin.cookies)
        getCookieRegex = '([^ ]+)=([^ ]+)'
        cookies = re.findall(getCookieRegex,originalCookie)
        for i in range(len(cookies)):
            keys = cookies[i][0]
            values = cookies[i][1]
            cookieValue = {keys:values}
            crmCookies.update(cookieValue)
            i+=1

    except:
        print "pleace ckeck requests params for login"
    else:
        #将crm_coikies写入配置文件
        cfg = ConfigParser.ConfigParser()
        cfg.read(configPathFile)
        if cfg.has_section("Auth") is True:
            cfg.set("Auth","cookies",crmCookies)
            cfg.write(open(configPathFile, "w"))
        else:
            print "add section"
            # TODO
            #cfg.add_section('Auth')

loginSys()

"""
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
        """