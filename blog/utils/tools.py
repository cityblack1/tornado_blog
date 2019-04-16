#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from functools import wraps

from sqlalchemy.engine.result import RowProxy
from tornado.util import ObjectDict


TARGET = (RowProxy, dict)


def _to_object_dict(ret):
    if isinstance(ret, list):
        for i in range(len(ret)):
            ret[i] = _to_object_dict(ret[i])
    elif isinstance(ret, TARGET):
        ret = ObjectDict(ret)
        for k, v in ret.iteritems():
            if isinstance(v, datetime):
                ret[k] = str(v)
    return ret


def to_object_dict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret = func(*args, **kwargs)
        return _to_object_dict(ret)
    return wrapper


def get_datetime_from_date_str(date_str, fmt='%Y-%m'):
    return datetime.strptime(date_str, fmt)