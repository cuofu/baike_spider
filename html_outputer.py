#!/usr/bin/env python
# coding:utf-8
from urllib.parse import unquote


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write("<meta charset='utf-8'>")
            fout.write('<body>')
            fout.write('<table>')

            for data in self.datas:
                fout.write('<tr>')
                fout.write(unquote('<td>%s</td>' % data['url']))
                fout.write('<td>%s</td>' % data['title'])
                fout.write('<td>%s</td>' % data['summary'])
                fout.write('</tr>')

            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')
