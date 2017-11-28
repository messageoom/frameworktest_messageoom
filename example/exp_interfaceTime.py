#coding=utf-8
__author__ = 'messageoom'

import re
import csv
import json
import requests

loginURL = "http://120.78.228.181/admin/index/login"

getleftAllURL = "http://120.78.228.181/admin/customers/customer/crmAdmin?c=customer&a=getAllNum"
geetleftURL = "http://120.78.228.181/admin/customers/customer/crmAdmin?c=customer&a=get_list_left"
getuserURL = "http://crm.guxiansheng.cn/admin/customers/customer/crmAdmin?c=customer&a=get_list"
interfaceUrl = "http://120.78.228.181/admin/cooper/customer_cooper_situation/crmAdmin?c=customer_cooper_situation&a=get_list"
crmCookies = {}
def interfaceTime():
    requestData = {"customer_id":65}
    re = requests.post(url = interfaceUrl, data = requestData, cookies = crmCookies)
    interfaceTime = re.elapsed.microseconds
    interface_seconds = interfaceTime/(1000*1000.0)
    print re.content
    print "%s 该接口发送第一个字节到解析完成总耗时：  %s 秒"%("interfaceTime",interface_seconds)


def loginCrm():
    """
    login crm & get cookies
    :return:
    """
    loginData = {"loginusername":"18782107004",
                 "loginpassword":"107004"}
    reLogin = requests.post(url = loginURL,data = loginData)
    # reLogin.eapseld.microseconds 发送第一个字节和完成解析报头之间的时间
    #interfaceTime = reLogin.elapsed.microseconds
    #interface_seconds = interfaceTime/(1000*1000.0)
    #print "该接口发送第一个字节到解析完成总耗时：  %s 秒"%interface_seconds
    #print reLogin.content
    #print reLogin.status_code

    try:
        rejson = reLogin.json()
        #remrejson = str(rejson).replace("u", "")
        dupjson = json.dumps(rejson)
        json.loads(dupjson,encoding='utf-8')
    except:
        print "Module:%s()   %s"%(loginCrm.__name__,requestError()[0])
    else:
        originalCookie = str(reLogin.cookies)
        global crmCookies
        getCookieRegex = '([^ ]+)=([^ ]+)'
        cookies = re.findall(getCookieRegex,originalCookie)
        for i in range(len(cookies)):
            keys = cookies[i][0]
            values = cookies[i][1]
            cookieValue = {keys:values}
            crmCookies.update(cookieValue)
            i+=1

def requestError():
    requestError = "【Error】:  please check request parameters"



def getleftAll():
    re = requests.post(url = getleftAllURL, cookies = crmCookies)
    interfaceTime = re.elapsed.microseconds
    interface_seconds = interfaceTime/(1000*1000.0)
    print re.content
    print "[%s]该接口发送第一个字节到解析完成总耗时：  %s 秒"%(getleftAll.__name__ ,interface_seconds)

def getleft():
    re = requests.post(url = geetleftURL, cookies = crmCookies)
    interfaceTime = re.elapsed.microseconds
    interface_seconds = interfaceTime/(1000*1000.0)
    print re.content
    print "[%s]该接口发送第一个字节到解析完成总耗时：  %s 秒"%(getleft.__name__ ,interface_seconds)

def gretuserlist():
    interfaceTime = re.elapsed.microseconds
    interface_seconds = interfaceTime/(1000*1000.0)
    print re.content
    print "[%s]该接口发送第一个字节到解析完成总耗时：  %s 秒"%(gretuserlist.__name__ ,interface_seconds)


if __name__ == "__main__":
    loginCrm()
    #interfaceTime()
    getleftAll()
    getleft()
    gretuserlist()