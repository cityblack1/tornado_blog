#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.core.models.article import ArticleDAO


def get_all_articles():
    return ArticleDAO.get_all_articles()


def get_articles_by_ids(ids):
    return ArticleDAO.get_articles_by_ids(ids)


def get_articles_by_date(start, end):
    return ArticleDAO.get_articles_by_date(start, end)


def get_articles_by_search(search_text):
    return ArticleDAO.get_articles_by_search(search_text)
