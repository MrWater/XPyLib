#! /usr/bin/env python
# -*- coding:utf-8 -*-

# TODO: Add exception judgement

import urllib
import http.client
import re

import spider.cookie.cookiespool as cookiespool

from http import cookiejar

class CurlLib:
	"""
	This is the main class of spider, 
	provides get and post method for html request
	"""

	def set_proxy(model, address, port):
		"""
		Set the proxy

		Params:
			model: the model of proxy, e.g. http
			address: the ip of proxy
			port: the port of proxy

			e.g. set_proxy('http', '127.0.0.0', '8000')
		"""

		proxy = urllib.request.ProxyHandler({model: address+port})
		opener = urllib.request.build_opener(proxy)
		urllib.request.install_opener(opener)

	def get(self, url, cookies={}, print_response=False):
		"""
		Http-Get method

		Params:
			url: target url 
			cookie: e.g. {'JESSIONID', '********'}
			print_response: whether to print the response or not

		Return:
			dict:{ 'response':'****', 'location':'***'}
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
		temp = response.read()
		match = re.search(r'<meta.*?charset=(.*?)"', str(temp))
		# TODO: need to modify with thinking over the reponse type that maybe json, text, html, .etc and deciding the correct charset
		ret['response'] = temp.decode(match.group(1)) if match != None else temp.decode('utf8')  

		headers = http.client.HTTPResponse.getheaders(response)

		for header in headers:
			if header[0] == 'Location':
				ret['location'] = header[1]
			elif header[0] == 'Set-Cookie':
				cookiespool.CookiesPool().set(header[1])

		if print_response:
			print(ret['response'])

		return ret

	def post(self, url, data, cookies={}, print_response=False):
		"""
		Http-Post method

		Params:
			url:target url 
			data:the reqeust data. e.g. {'id':'1', 'password':'2'}
			cookie: e.g. {'JSESSIONID', '********'}
			print_response: whether to print the response or not

		Return:
			dict:{ 'response':'****', 'location':'***'}
		"""

		ret = {'response':'', 'location':''}

		if not isinstance(cookies, dict):
			return ret

		cookie = cookiejar.CookieJar()
		req = urllib.request.Request(url, urllib.parse.urlencode(data).encode())
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
		temp = response.read()
		match = re.search(r'<meta.*?charset="(.*?)"', str(temp))
		ret['response'] = temp.decode(match.group(1))

		headers = http.client.HTTPResponse.getheaders(response)

		for header in headers:
			if header[0] == 'Location':
				ret['location'] = header[1]
			elif header[0] == 'Set-Cookie':
				cookiespool.CookiesPool().set(header[1])

		if print_response:
			print(ret['response'])

		return ret

	def __make_cookie(name, value, domain):
		"""
		Make a cookie with name, value and domain

		Return:
			cookiejar.Cookie
		"""

		return cookiejar.Cookie(
	        version=0,
	        name=name,
	        value=value,
	        port=None,
	        port_specified=False,
	        domain=domain,
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


		

