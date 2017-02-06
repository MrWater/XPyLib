# !/user/bin/env python
# -*- coding:utf-8 -*-

class Curl:
	"""This is the main class of spider, 
	provides get and post method for html request"""

	def get(self, url, cookies, bool print_response=false):
		"""Http-Get method"""

		ret = {'response':'', 'location':''}

		

