# 基于 selenium python搭建web项目的测试框架

* [1. 概述](#1)
    * [1.1 <span >selenium 安装</span>](#1.1)
    * [1.2 <span >pychram git配置 </span>](#1.2)
    * [1.3 <span >selenium 介绍</span>](#1.3)
    * [1.4 <span >用到的三方包</span>](#1.4)

* [2. 框架介绍](#2)
    * [2.1 <span> </span>](#2.1)

* [3. 注意事项](#3)
    * [3.1 <span>python seleium处理中文时加u</span>](#3.1)



<h2 id="1">一 概述</h2>
* TODO

<h3 id="1.1">1.1 selenium 安装</h3>
* TODO

<h3 id="1.2">1.2 selenium 介绍</h3>
* TODO

<h3 id="1.3">1.3 用到的三方包</h3>
* NumPy
    * > NumPy数组是一个多维数组对象，称为ndarray。其由两部分组成：1.实际的数据 2.描述这些数据的元数据

* HTMLTestRunner
    * > HTMLTestRunner是Python标准库的unittest模块的扩展。 它生成易于使用的HTML测试报告。
* unittest
    * > python 单元测试框架
* sqlite3
    * > sqlite3模块（轻量级数据库），用于满足框架中存放日志及报告的需求，



<h2 id="1">二 框架介绍</h2>
```
│  README.md                        ---------------框架介绍文档
│  run.py                           ---------------运行主函数
│
├─config                            ---------------存放配置文件及全局变量
│      config.ini
│      globalparam.py
│      __init__.py
│
├─public                            ---------------封装的公共方法
│  │  __init__.py
│  │
│  └─commn
│          basepage.py
│          log.py
│          logDB.py
│          readconfig.py
│          utils.py
│          __init__.py
│
├─report                            ----------------存放测试报告及日志记录
│  │  MsAutoTestResult.html
│  │
│  └─log
│          2017-07-24.log
│          2017-07-27.log
│          2017-08-07.log
│
└─testcase                          ----------------测试用例
        test_login.py
        test_login.pyc
        test_post_article.py
        __init__.py
```
