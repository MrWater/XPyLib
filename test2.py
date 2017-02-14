# !/user/bin/python
# -*-coding:utf8-*-

from bs4 import BeautifulSoup

from spider.curl import curllib

curl = curllib.CurlLib()
html = curl.get("http://www.baidu.com")['response']
soup = BeautifulSoup(html, 'html.parser')
fixed_html = soup.prettify()
print(fixed_html)