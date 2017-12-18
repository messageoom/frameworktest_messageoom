#coding=utf-8
__author__ = 'messageoom'

from tests import interfaceURL
from public.requests_wrapper.base import Post

post = Post()
def call_number(conf):
    """
    拨打客户电话
    """
    post.request(interfaceURL.call_number, conf=conf)

def get_record(conf):
    """
    最近联系通话记录列表
    """
    post.request(interfaceURL.get_call_record,conf=conf)#,expected_response_data="data")

def get_Call_Record_All(conf):
    """
    通话记录列表
    """
    post.request(interfaceURL.get_Call_Record_All,conf=conf)

def delete_Record(conf):
    """
    删除通话记录
    """
    post.request(interfaceURL.delete_Record,conf=conf)