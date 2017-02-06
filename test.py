import spider.cookie.cookiespool as cookie

c = cookie.CookiesPool()
c.set("jessionid=123123123; path=")
print(c.get())