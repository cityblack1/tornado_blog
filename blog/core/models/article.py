#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy.sql import select, and_, func, between

from blog.core.common.db import db
from blog.utils.tools import to_object_dict


class ArticleDAO(object):

    @classmethod
    @to_object_dict
    def get_all_articles(cls):
        t = db.article
        sql = select([t]).order_by(t.c.id.desc())
        return db.execute(sql).fetchall()

    @classmethod
    @to_object_dict
    def get_articles_by_ids(cls, ids):
        t = db.article
        sql = select([t]).where(t.c.id.in_(ids)).order_by(t.c.id.desc())
        return db.execute(sql).fetchall()

    @classmethod
    @to_object_dict
    def get_articles_by_date(cls, start, end):
        t = db.article
        sql = select([t]).order_by(t.c.id.desc())
        sql = sql.where(and_(
            t.c.created >= str(start),
            t.c.created <= str(end)
        ))
        return db.execute(sql).fetchall()

    @classmethod
    @to_object_dict
    def get_articles_by_search(cls, search_text):
        t = db.article
        if isinstance(search_text, unicode):
            search_text.encode('utf-8')
        sql = select([t]).where(t.c.title.like('%' + search_text + '%')).order_by(t.c.id.desc())
        return db.execute(sql).fetchall()
