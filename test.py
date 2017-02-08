import re
import sqlite3
import json
import threading
import time

import spider.curl.curllib as lib
import spider.cookie.cookiespool as cookiespool

cnt = 0

def func():
	c = lib.CurlLib()
	
	while(True):
		html = c.get("http://geek.csdn.net/service/news/get_news_list?jsonpcallback=jQuery20308831259299392232_1486523402180&username=&from=-&size=1&type=hackernewsv2_new&_=1486523402181")['response']
		html = html[html.find('(')+1:-1]
		data = json.loads(html)
		f = data['from']
		match = re.findall(r'<a href="(.*?)" class="title".*?>(.*?)</a>', data['html'])

		conn = sqlite3.connect('./头条.db')
		conn.execute('create table if not exists toutiao(id integer primary key AUTOINCREMENT, url text unique,title varchar(50))')

		for m in match:
			sql = 'insert into toutiao values(null, \'%s\', \'%s\');' % (m[0], m[1])

			try:
				conn.execute(sql)
			except Exception as e:
				continue

		conn.commit()

		global cnt
		cnt += 1
		print("完成" + str(cnt))
		time.sleep(10)

	conn.close()

t = threading.Thread(target=func)
t.start()
t.join()
