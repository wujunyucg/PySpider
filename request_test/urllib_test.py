import urllib2
import urllib

url_ip="http://httpbin.org/ip"
url_get="http://httpbin.org/get"
def use_simple_urllib2():
    response=urllib2.urlopen(url_ip)
    print "Headers"
    print response.info()
    print "response body"
    print "".join([line for line in response.readlines()])

def uss_params_urllib2():
    params=urllib.urlencode({'param1':'hello','param2':'world'})
    print 'request params'
    print params
    response=urllib2.urlopen('?'.join([url_get,'%s'])% params)
    print "Headers"
    print response.info()
    print "state Code"
    print response.getcode()
    print "response body"
    print "".join([line for line in response.readlines()])
    
    
if __name__=='__main__':
    uss_params_urllib2()
#     use_simple_urllib2()

