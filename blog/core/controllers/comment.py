#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.core.models.comment import CommentDAO


def get_comments_by_article_ids(article_ids):
    comments = CommentDAO.get_all_comments_by_article_ids(article_ids)
    return comments


def create_comment(fields):
    return CommentDAO.create_comment(fields)
