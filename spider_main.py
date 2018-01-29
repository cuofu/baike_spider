#!/usr/bin/env python
# coding:utf-8
import html_downloader
import html_outputer
import html_parser
import url_manager
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


class SpiderMain(object):
    def __init__(self):  # 初始化
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)  # 新的列表
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 30:
                    break
                count += 1
            except:
                print('爬取失败')

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"  # 入口url
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)  # 启动爬虫
