#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.escape import json_decode

from blog.http.handlers.base import BaseHandler
from blog.core.controllers.comment import create_comment, get_comments_by_article_ids


class CommentsHandler(BaseHandler):
    def post(self):
        param = json_decode(self.request.body)
        article_id = param['article_id']
        author_name = param['author_name']
        content = param['content']
        parent_id = param['parent_id']
        fields = dict(
            article_id=article_id,
            author_name=author_name,
            content=content,
            parent_id=parent_id
        )
        create_comment(fields)
        self.set_status(204)

    def get(self, article_id):
        article_id = int(article_id)
        comments = get_comments_by_article_ids(article_ids=[article_id])
        comments_id_map = {_.id: _ for _ in comments}
        root_comments = []
        for comment in comments:
            if not comment.parent_id:
                root_comments.append(comment)
            elif comment.parent_id:
                parent_comment = comments_id_map[comment.parent_id]
                comments = parent_comment.setdefault('comments', [])
                comments.append(comment)
        self.render_json(root_comments)
