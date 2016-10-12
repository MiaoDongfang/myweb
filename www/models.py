#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import time
from transwarp import db
from transwarp.orm import Model,StringField,IntegerField,TextField,BooleanField,BlobField,VersionField,FloatField

logger=logging.getLogger(__name__)


class User(Model):

    __table__="users"

    id=StringField(primary_key=True,default=db.next_id,ddl='varchar(50)')
    email=StringField(updatable=False,ddl='varchar(50)')
    password=StringField(ddl='varchar(50)')
    name=StringField(ddl='varchar(50)')
    admin=BooleanField()
    image=StringField(ddl='varchar(500)')
    created_at=FloatField(updatable=False,default=time.time)


class Blog(Model):

    __table__="blogs"

    id=StringField(primary_key=True,default=db.next_id,ddl='varchar(50)')
    user_id=StringField(updatable=False,ddl='varchar(50)')
    user_name=StringField(updatable=False,ddl='varchar(50)')  #冗余 后期进行改进
    user_image = StringField(updatable=False, ddl='varchar(500)') #冗余 后期进行改进
    name=StringField(ddl='varchar(200)')
    summary=StringField(ddl='varchar(500)')
    content=TextField()
    created_at=FloatField(updatable=False,default=time.time)


class Comment(Model):

    __table__="comments"

    id=StringField(primary_key=True,default=db.next_id,ddl='varchar(50)')
    user_id = StringField(updatable=False, ddl='varchar(50)')
    user_name = StringField(updatable=False, ddl='varchar(50)')  # 冗余 后期进行改进
    user_image = StringField(updatable=False, ddl='varchar(500)')  # 冗余 后期进行改进
    content=TextField()
    created_at = FloatField(updatable=False, default=time.time)
