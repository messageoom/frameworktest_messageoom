#coding=utf-8
__author__ = 'messageoom'

from public import interfaceURL
from public.requests_wrapper.base import Post

post = Post()
def get_record(conf):
    """
    最近联系通话记录列表
    """
    post.request(interfaceURL.get_call_record,conf=conf)

def get_Call_Record_All(conf):
    """
    通话记录列表
    """
    post.request(interfaceURL.get_Call_Record_All,conf=conf)

