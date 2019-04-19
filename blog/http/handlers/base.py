#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.escape import json_encode
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def render_json(self, value):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json_encode(value))

    def _request_summary(self):
        return "%s %s (%s)" % (self.request.method, self.request.uri,
                               self.request.headers.get('remote-user-ip', self.request.remote_ip))
