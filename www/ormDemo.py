#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User,Blog,Comment
from transwarp import db
from transwarp.orm import Model,StringField,IntegerField,TextField,BooleanField,BlobField,VersionField,FloatField,Field
db.create_engine('root','password','awesome')

# u=User(name='test',email='test@test.com',password="password",admin=True,image="/d/sd")
#
# u.insert()

# print u.name

u1 = User.find_first('where email=?', 'test@test.com')
print 'find user\'s name:', u1.name
print u1

# id=StringField(default='123')
# print id
# print id.default

import config

print config.configs['session']