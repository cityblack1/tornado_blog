#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from gevent import monkey; monkey.patch_all()

import logging
import gevent.pywsgi
import os
import tornado.web
import tornado.wsgi

from tornado.log import enable_pretty_logging, LogFormatter
from blog.http.urls import handlers

BASE_LOG_PATH = os.path.join(os.path.dirname(__file__), 'blog/log')
ACCESS_LOG_PATH = os.path.join(BASE_LOG_PATH, 'tornado.access.log')
APP_LOG_PATH = os.path.join(BASE_LOG_PATH, 'tornado.application.log')
GEN_LOG_PATH = os.path.join(BASE_LOG_PATH, 'tornado.general.log')


def set_log():
    enable_pretty_logging()
    fmt = LogFormatter()
    for logger_name in ['tornado.access', 'tornado.application', 'tornado.general']:
        logger = logging.getLogger(logger_name)
        log_file_path = os.path.join(BASE_LOG_PATH, logger_name + '.log')
        log_handler = logging.FileHandler(log_file_path)
        log_handler.setFormatter(fmt)
        logger.addHandler(log_handler)


def get_tornado_application():
    application = tornado.web.Application(handlers, cookie_secret='abc', parse_config_file=True)
    set_log()
    return application


def get_wsgi_application():
    app = get_tornado_application()
    return tornado.wsgi.WSGIAdapter(app)


app = get_wsgi_application()


def run():
    server = gevent.pywsgi.WSGIServer(('', 9000), app)
    server.serve_forever()


if __name__ == '__main__':
    run()
