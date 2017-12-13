#coding=utf-8
__author__ = 'messageoom'

from public import interfaceURL
from public.requests_wrapper import base

post = base.Post()
inurl = interfaceURL
def creat_Customer(conf):
    """
    创建客户
    :return: Customer_ID
    """
    post.request(interfaceURL.add_customer,conf=conf)

def get_List_Customer(conf):
    """
    客户列表
    """
    post.request(interfaceURL.get_list_customer,conf=conf)



def delete_Customer(conf):
    """
    删除客户:
    """
    post.request(interfaceURL.delete_customer,conf=conf)

