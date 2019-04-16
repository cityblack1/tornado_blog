#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.core.models.tag import TagDAO


def get_tags_by_article_ids(article_ids):
    tags = TagDAO.get_all_tags_by_article_ids(article_ids)
    tag_ids = [_.id for _ in tags]
    tags_ = TagDAO.get_by_ids(tag_ids)
    tags_map = {_.id: _ for _ in tags_}
    for tag in tags:
        tag.name = tags_map[tag.tag_id].name
    return tags


def get_tags_by_ids(ids):
    return TagDAO.get_by_ids_v2(ids)