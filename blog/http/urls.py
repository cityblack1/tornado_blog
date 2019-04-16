#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.http.handlers.article import ArticlesHandler, PartArticlesHandler, SearchArticlesHandler
from blog.http.handlers.comment import CommentsHandler

handlers = [
    (r'/api/articles', ArticlesHandler),

    # (r'/api/articles', ArticlesHandler),
    # (r'/api/articles', ArticlesHandler),

    (r'/api/comments', CommentsHandler),
    (r'/api/comments/article/(\d+)', CommentsHandler),
    (r'/api/(\w+)/(.*)', PartArticlesHandler),
    (r'/api/search/(.*)', SearchArticlesHandler),

]