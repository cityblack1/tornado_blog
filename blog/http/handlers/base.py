#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.escape import json_encode
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def render_json(self, value):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json_encode(value))