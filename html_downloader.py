#!/usr/bin/env python
# coding:utf-8
from urllib import request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        resp = request.urlopen(url)

        if resp.getcode() != 200:
            return None

        return resp.read()
