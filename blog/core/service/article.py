#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blog.core.controllers import (
    article as article_ctl,
    comment as comment_ctl,
    category as category_ctl,
    tag as tag_ctl
)


# hack by cityblack1，因为懒得设计接口了，并且这个博客只是为了找工作应付
# 所以所有的数据都在一个接口返回即可
# 是不是很机智？
# 反正也没人能看到这段代码
# 如果你看到了，说明你是真正的粉丝
def get_all(need_article_ids=None):
    articles = article_ctl.get_all_articles()
    article_map = {_.id: _ for _ in articles}
    article_ids = [_.id for _ in articles]
    comments = comment_ctl.get_comments_by_article_ids(article_ids)
    tags = tag_ctl.get_tags_by_article_ids(article_ids)
    tags_map = {_.tag_id: _ for _ in tags}
    categories = category_ctl.get_categories_by_article_ids(article_ids)
    categories_map = {_.category_id: _ for _ in categories}
    comments_id_map = {_.id: _ for _ in comments}
    date_map = {}
    for comment in comments:
        if not comment.parent_id:
            article = article_map[comment.article_id]
            comments = article.setdefault('comments', [])
            comments.append(comment)
        elif comment.parent_id:
            parent_comment = comments_id_map[comment.parent_id]
            comments = parent_comment.setdefault('comments', [])
            comments.append(comment)
    for article in articles:
        if 'comments' not in article or not isinstance(article.comments, list):
            article.comments = []
        article.comment = len(article.comments)
        date_str = article.created[:7 ]
        date_num = date_map.get(date_str, 0)
        date_map[date_str] = date_num + 1
        article['created'] = article['created'][:10]
    dates = sorted([dict(date=k, num=v) for k, v in date_map.items()], reverse=True)
    for tag in tags:
        article_id = tag.article_id
        tag_name = tag.name
        tag_id = tag.tag_id
        article = article_map[article_id]
        tags_ = article.setdefault('tags', [])
        tags_.append(tag_name)
        tag_ids_ = article.setdefault('tag_ids', [])
        tag_ids_.append(tag_id)
        tag_num = tags_map[tag_id].get('num', 0)
        tags_map[tag_id]['num'] = tag_num + 1
    tags = sorted(tags_map.values(), key=lambda _: _.tag_id, reverse=True)
    for tag in tags:
        del tag['id']
    for category in categories:
        article_id = category.article_id
        category_name = category.name
        category_id = category.category_id
        article = article_map[article_id]
        article.category = category_name
        article.category_id = category_id
        category_num = categories_map[category_id].get('num', 0)
        categories_map[category_id]['num'] = category_num + 1
    categories = sorted(categories_map.values(), key=lambda _: _.category_id, reverse=True)
    for cate in categories:
        del cate['id']
    if need_article_ids is not None:
        articles = [_ for _ in articles if _.id in need_article_ids]
    return dict(
        articles=articles,
        dates=dates,
        tags=tags,
        categories=categories
    )
