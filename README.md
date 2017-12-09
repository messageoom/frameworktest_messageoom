## 基于requests selenium python搭建的web项目测试框架
@ author messageoom
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
* requests; selenium; NumPy; sqlite3; HTMLTestRunner; ConfigParser; MySQLdb
  * >以上三方包出 HTMLTestRunner 不能用pip install来安装外，其余都可使用pip安装。将HTMLTestRunner.py文件下载后放置python\lib下即可。
* NumPy
  * > NumPy数组是一个多维数组对象，称为ndarray。其由两部分组成：1.实际的数据 2.描述这些数据的元数据

* HTMLTestRunner
  * > HTMLTestRunner是Python标准库的unittest模块的扩展。 它生成易于使用的HTML测试报告。
* unittest
  * > python 单元测试框架
* sqlite3
  * > sqlite3模块（轻量级数据库），用于满足框架中存放日志及报告的需求，



<h2 id="1">二 框架概览</h2>
```

│  config.py
│  interfaceAuth.py
│  list.txt
│  README.md
│  run.py
│          
├─config
│      config.ini
│      globalparam.py
│      globalparam.pyc
│      readconfig.py
│      readconfig.pyc
│      __init__.py
│      
├─example
│      exp_completeData.py
│      exp_interfaceTime.py
│      meInspect.py
│      
├─mCase
│      test_login.py
│      test_post_article.py
│      __init__.py
│      
├─public
│  │  __init__.py
│  │  
│  ├─commn
│  │      basepage.py
│  │      log.py
│  │      logDB.py
│  │      __init__.py
│  │      
│  └─requests_wrapper
│          admin_api.py
│          base.py
│          user_api.py
│          __init__.py
│          
├─tests
│  │  __init__.py
│  │  
│  ├─interface
│  │      test.py
│  │      __init__.py
│  │      
│  └─webUI
│          test_login.py
│          test_post_article.py
│          __init__.py
│          
└─tools
        interfaceTime.py
        
```
