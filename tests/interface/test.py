__author__ = 'messageoom'

from config import globalparam
from public.requests_wrapper import base

def getcalllist_001():
    path = 'http://crm.guxiansheng.cn/admin/call/call/crmAdmin?c=call&a=getCallRecord'
    cookies = globalparam.cookies
    print cookies
    base.Post().request(cookies=cookies,path=path)
    print "getlist------------------"
getcalllist_001()
def getcalllist_002():
    print "getlist------------------"
def getcalllist_003():
    """
    kdjhkdnhkdnhkd
    :param test
    """
    print "getlist------------------"