# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 01:29:47 2020

@author: Administrator
"""

import pymysql

db = pymysql.connect(host='localhost',user='root',password='',port=3306)
cursor = db.cursor()
cursor.execute('use job')
sengName = 'Pyth123123on'
cmpName = 'douyu'
detail = 'dsf,dafds'
url = 'dsafdasdf'
sql = 'insert into shixiseng(sengName,comName,detail,url) values(%s,%s,%s,%s);'
cursor.execute(sql,(sengName,cmpName,detail,url))
db.commit()

cursor.execute(sql)
cursor.close
