# !/user/bin/env python
# -*- coding:utf-8 -*-

import threading

class CookiesPool:
	"""This is a pool for storing and reading cookies"""

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

	def get(self, *cookie_key):
		"""Get values according to keys"""
		cks = {}

		for k in cookie_key:
			if dict.__contains__(self.__cookies, k):
				cks[k] = self.__cookies[k]

		return cks

	def set(self, cookies_str):
		"""Get right cookies from cookies string"""
		arr = cookies_str.split(',')

		for item in arr:
			key = item[:item.find('=')]
			value = item[item.find('=')+1:]

			if str.__contains__(value, '; path'):
				value = value[:value.find('; path')]
			if str.__contains__(value, ';path'):
				value = value[:value.find(';path')]

			self.__cookies[key] = value