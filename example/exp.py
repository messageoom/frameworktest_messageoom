#coding=utf-8
__author__ = 'messageoom'

import re
import csv
import json
import requests

loginURL = "loginURL"
usernameUrl = "indexURL"
crmCookies = {}
def loginCrm():
    """
    login crm & get cookies
    :return:
    """
    loginData = {"loginusername":"loginusername",
                 "loginpassword":"loginpassword"}
    reLogin = requests.post(url = loginURL,data = loginData)
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

def getCrmUser():
    """
    get crm system user
    :return: getuser
    """
    crmData = {"pagesize":1200}
    usernameData = requests.post(url = usernameUrl,cookies = crmCookies,data = crmData)
    try:
        rejson = usernameData.json()
        dupjson = json.dumps(rejson)
        json.loads(dupjson,encoding='utf-8')
    except:
        print "Module:%s()   %s"%(getCrmUser.__name__,requestError()[0])
    else:
        rejson = usernameData.json()
        userClass = rejson[u'data'][u'data']
        getuser = []
        for i in range(len(userClass)):
            usernameDatas = userClass[i][u'username']
            getuser.append(usernameDatas)
        return getuser

def readECData():
    """
    get EC source data
    :return: column
    """
    with open('filepath\\filename.csv','rb') as csvfile:
        meReader = csv.reader(csvfile)
        column = [row[1] for row in meReader]
        columnhesder = column[0]
        column.remove(columnhesder)
        return column

def cmpData(crmData=None,sourceData=None):
    """
    Compare crmData with sourceData
    :param crmData:
    :param sourceData:
    :return:
    """
    if cmp(crmData,sourceData) == 0:
        print "%s"%requestError()[1]
    else:
        print "%s"%requestError()[2]


    # TODO complete other source data


def requestError():
    requestError = "【Error】:  please check request parameters"
    cmpError = "【Error】:  Incomplete import data"
    cmpYes = "【info】:  complete import data  YES!"
    return requestError,cmpYes,cmpError

if __name__ == "__main__":
    loginCrm()
    getCrmUser()
    cmpData()
