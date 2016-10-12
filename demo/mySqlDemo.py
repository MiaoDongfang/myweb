#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import mysql.connector

conn=mysql.connector.connect(user = "root", password="miao19931021", database="test", host='119.29.145.94',port='3306', use_unicode=True)
cursor=conn.cursor()
cursor.execute("insert into 'user'('id','name') values (%s，%s)",['2','dongfang'])
print cursor.rowcount
cursor.execute('select * from user')
conn.commit()
cursor.close()
conn.close()

