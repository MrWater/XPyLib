import spider.curl.curllib as lib
import spider.cookie.cookiespool as cookiespool

c = lib.CurlLib()
print(c.get("http://music.163.com/#/user/home?id=19564840")['response'].decode("utf8"))