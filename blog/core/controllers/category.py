#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.core.models.category import CategoryDAO


def get_categories_by_article_ids(article_ids):
    categories = CategoryDAO.get_all_categories_by_article_ids(article_ids)
    category_ids = [_.id for _ in categories]
    categories_ = CategoryDAO.get_by_ids(category_ids)
    categories_map = {_.id: _ for _ in categories_}
    for category in categories:
        category.name = categories_map[category.category_id].name
    return categories


def get_categories_by_ids(ids):
    return CategoryDAO.get_by_ids_v2(ids)
