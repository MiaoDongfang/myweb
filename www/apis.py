#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json
import functools
import logging
from transwarp.web import ctx

logger=logging.getLogger(__name__)

def dumps(obj):
    return json.dumps(obj)

class APIError(StandardError):

    def __init__(self,error,data='',message=''):
        super(APIError, self).__init__()
        self.error=error
        self.data=data
        self.message=message

class APIValueError(APIError):
    def __init__(self,field,message=''):
        super(APIValueError, self).__init__("value: Invalues",field,message)


class APIResourseNotFoundError(APIError):
    def __init__(self,field,message=''):
        super(APIResourseNotFoundError, self).__init__("value:not found",field,message)


class APIPermissionError(APIError):
    def __init__(self,message=''):
        super(APIPermissionError, self).__init__("permission:forbidden","permission",message)


def api(func):

    @functools.wraps(func)
    def wrapper(*args,**kw):
        try:
            r=dumps(func(*args,**kw))
        except APIError,e:
            r=json.dumps(dict(error=e.error,data=e.data,message=e.message))
        except Exception,e:
            logger.exception(e)
            r = json.dumps(dict(error='internalerror', data=e.__class__.__name__, message=e.message))

        ctx.response.content_type = 'application/json'
        return r
    return wrapper



