# !/user/bin/python
# -*- coding:utf-8 -*-

# TODO: Add exception judgement

import threading

class CookiesPool:
	"""
	This is a pool for storing and reading cookies
	"""

	__lock = threading.Lock()
	__instance = None
	__cookies = {}

	def __init__(self):
		pass

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None:
			cls.__lock.acquire()

			if cls.__instance is None:
				cls.__instance = super(CookiesPool, cls).__new__(cls, *args, **kwargs)

			cls.__lock.release()

		return cls.__instance

	def __str__(self):
		s = ''

		for key in self.__cookies.keys():
			s += key + ' = ' + self.__cookies[key] + '\n'

		return s

	def get(self, *cookie_key):
		"""
		Get values according to keys

		Params:
			*cookie_key: a tuple that contains keys for getting cookie

		Returns
			dict: e.g. {'JESSIONID':'*********'}
		"""

		cks = {}

		for k in cookie_key:
			if dict.__contains__(self.__cookies, k):
				cks[k] = self.__cookies[k]

		return cks

	def set(self, cookies_str):
		"""
		Get right cookies from cookies string
		
		Params:
			cookie_str: it is always the string gotten from response headers that likes 'jessionid:123saf123sfs; path='
		"""

		key = cookies_str[:cookies_str.find('=')]
		value = cookies_str[cookies_str.find('=')+1:]

		if str.__contains__(value, ';'):
			value = value[:value.find(';')]

		self.__cookies[key] = value