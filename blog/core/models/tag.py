#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy.sql import select, and_, func, between

from blog.core.common.db import db
from blog.utils.tools import to_object_dict


class TagDAO(object):

    @classmethod
    @to_object_dict
    def get_all_tags_by_article_ids(cls, article_ids):
        t = db.article_tag
        sql = select([t]).where(t.c.article_id.in_(article_ids))
        sql = sql.order_by(t.c.id.desc())
        return db.execute(sql).fetchall()

    @classmethod
    @to_object_dict
    def get_by_ids(cls, ids):
        t = db.tag
        sql = select([t]).where(t.c.id.in_(ids))
        sql = sql.order_by(t.c.id.desc())
        return db.execute(sql).fetchall()

    @classmethod
    @to_object_dict
    def get_by_ids_v2(cls, ids):
        t = db.article_tag
        sql = select([t]).where(t.c.id.in_(ids))
        sql = sql.order_by(t.c.id.desc())
        return db.execute(sql).fetchall()
