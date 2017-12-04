__author__ = 'messageoom'

import MySQLdb

def selectDB():
    conn= MySQLdb.connect(host='192.168.0.XX',
                          port = 3306,
                          user='root',
                          passwd='messageoom',
                          db ='messageoom',)
    cur = conn.cursor()
    # 查询
    testData = cur.execute('SELECT * FROM crm_customer_employee WHERE employee_id = (SELECT id FROM crm_admin WHERE username = "joelww")')
    #reAll = cur.fetchall()
    results = cur.fetchone()
    print results