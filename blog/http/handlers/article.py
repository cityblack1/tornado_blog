#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.core.service.article import get_all
from blog.http.handlers.base import BaseHandler
from blog.core.controllers import category as category_ctl, tag as tag_ctl, article as article_ctl
from blog.utils.tools import get_datetime_from_date_str


class ArticlesHandler(BaseHandler):
    def get(self):
        self.render_json(get_all())


class PartArticlesHandler(BaseHandler):
    def get(self, part, part_id):
        article_ids = []
        if part == 'category':
            categories = category_ctl.get_categories_by_ids([int(part_id)])
            article_ids = [_.article_id for _ in categories]
        elif part == 'tag':
            tags = tag_ctl.get_tags_by_ids([int(part_id)])
            article_ids = [_.article_id for _ in tags]
        elif part == 'date':
            date_start = get_datetime_from_date_str(part_id)
            if date_start.month != 12:
                date_end = date_start.replace(month=date_start.month + 1)
            else:
                date_end = date_start.replace(month=1, year=date_start.year + 1)
            articles = article_ctl.get_articles_by_date(date_start, date_end)
            article_ids = [_.id for _ in articles]
        return self.render_json(get_all(article_ids))


class SearchArticlesHandler(BaseHandler):
    def get(self):
        pass
