import spider.curl.curllib as lib
import spider.cookie.cookiespool as cookiespool

c = lib.CurlLib()

c.get("https://login.taobao.com/member/login.jhtml")