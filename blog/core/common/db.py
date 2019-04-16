#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urlparse

from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import NoSuchTableError, InternalError


class Tables(object):
    def __init__(self,
                 mysql_url='mysql+pymysql://root:123456@localhost:3306/blog?charset=utf8mb4',
                 master_max_overflow=2,
                 master_pool_size=2,
                 master_pool_recycle=1800):
        self.master = create_engine(self._format_mysql_url(mysql_url),
                                    encoding='utf-8',
                                    max_overflow=master_max_overflow,
                                    pool_size=master_pool_size,
                                    pool_recycle=master_pool_recycle)
        self._initialize_meta()

    def _initialize_meta(self):
        self.meta = MetaData()
        self.meta.reflect(self.master)

    def _format_mysql_url(self, orig_url):
        """Encode the URL and insert the driver name into the URL scheme."""
        if not orig_url:
            return orig_url
        url = orig_url
        if isinstance(url, unicode):
            url = url.encode('utf-8')
        res = urlparse.urlparse(url)
        if '+' in res.scheme:
            return url
        scheme = '+'.join((res.scheme.split('+')[0], 'pymysql'))
        return urlparse.urlunparse((scheme, res.netloc, res.path, res.params,
                                    res.query, res.fragment))

    def __getattr__(self, name):
        try:
            return self.meta.tables[name]
        except KeyError:
            raise NoSuchTableError(name)

    def execute(self, *args, **kwargs):
        try:
            return self.master.execute(*args, **kwargs)
        except InternalError as e:
            # (1054, 'unknown column field')
            if e.orig.args[0] == 1054:
                self._initialize_meta()
                return self.master.execute(*args, **kwargs)
            raise


db = Tables()
