#! /usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import lxml.html

from spider.curl import curllib

curl = curllib.CurlLib()
html = curl.get("http://www.baidu.com")['response']
tree = lxml.html.fromstring(html)
fixed_html = lxml.html.tostring(tree, pretty_print=True)
print(fixed_html)