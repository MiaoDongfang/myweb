#!/usr/bin/env python
# -*- coding: utf-8 -*-

def now():
    print '2016-09-16'

# f=now
# f()
# print f.__name__
# print now.__name__

# def log(func):
#     def wrapper(*args,**kw):
#         print "call %s()"% func.__name__
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print '2016-09-16'
#
# now()

# now=log(now)
# now()
# log(now)()
# 带参数的decorator
# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kw):
#             print "%s %s()"%(text,func.__name__)
#             return func(*args,**kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print "2016-09-16"
#
# # log('execute')(now)()
# now()
# print now.__name__

class _Log:
    def __enter__(self):
        print "begin"

    def __exit__(self,exctype, excvalue, traceback):
        print "end"

import functools

# def log():
#     return _Log()

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        with _Log():
            return func(*args,**kw)
    return wrapper

# def with_connection(func):
#
#     @functools.wraps(func)
#     def _wrapper(*args,**kw):
#         with _Log():
#             return func(*args,**kw)
#     return _wrapper

@log
def now():
    print "2016-09-16"

now()
print now.__name__