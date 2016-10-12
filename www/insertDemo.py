#!/usr/bin/env python
# -*- coding: utf-8 -*-

import models
from transwarp import db


db.create_engine("root", 'password', 'awesome')

blog1=models.Blog(
    user_id="100",
    user_name=u'苗东方',
    name=u"这是一条测试数据",
    summary="This is a test blog",
    content='''
    Test your Internet connection bandwidth to locations around the world with this interactive broadband speed test from Ookla.
    Test.com is a software solution for you to easily create, administer and manage training courses and certification tests, in up to 22 languages.
    '''
)
blog1.insert()