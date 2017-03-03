# import urllib2
# response = urllib2.urlopen('http://www.baidu.com')
# print response.getcode()
# cont=response.read()
# print cont

# import urllib2
# request = urllib2.Request('http://www.baidu.com')
# request.add_header('user-agent', 'Mozilla/5.0')
# response = urllib2.urlopen(request)
# print response.getcode()
# cont=response.read()
# print cont

import urllib2,cookielib
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
print response.getcode()
cont=response.read()
print cj
