# !/user/bin/python
# -*- coding:utf-8 -*-

import urllib
import http.client
import spider.cookie.cookiespool as cookiespool

from http import cookiejar

class CurlLib:
	"""
	This is the main class of spider, 
	provides get and post method for html request
	"""

	def set_proxy(model, address, port):
		proxy = urllib.request.ProxyHandler({model: address+port})
		opener = urllib.request.build_opener(proxy)
		urllib.request.install_opener(opener)

	def get(self, url, cookies={}, print_response=False):
		"""
		Http-Get method
		"""

		ret = {'response':'', 'location':''}

		if not isinstance(cookies, dict):
			return ret

		cookie = cookiejar.CookieJar()
		req = urllib.request.Request(url)
		s = url[url.find('/')+2:]

		if str.__contains__(s, ':'):
			s = s[:s.find(':')-1]
		else:
			s = s[:s.find('/')-1]

		for c in cookies.keys():
			cookie.set_cookie(__make_cookie(c, cookies[c], s))

		cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
		opener = urllib.request.build_opener(cookie_processor)
		urllib.request.install_opener(opener)

		response = urllib.request.urlopen(req)
		ret['response'] = response.read()
		headers = http.client.HTTPResponse.getheaders(response)

		for header in headers:
			if header[0] == 'Location':
				ret['location'] = header[1]
			elif header[0] == 'Set-Cookie':
				print(header[1])
				cookiespool.CookiesPool().set(header[1])

		if print_response:
			print(ret['response'])

		return ret

	def __make_cookie(name, value, domain):
	    return cookielib.Cookie(
	        version=0,
	        name=name,
	        value=value,
	        port=None,
	        port_specified=False,
	        domain="xxxxx",
	        domain_specified=True,
	        domain_initial_dot=False,
	        path="/",
	        path_specified=True,
	        secure=False,
	        expires=None,
	        discard=False,
	        comment=None,
	        comment_url=None,
	        rest=None
	    )


		

