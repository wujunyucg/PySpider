import requests

url_ip="http://httpbin.org/ip"
url_get="http://httpbin.org/get"

def use_simple_request():
    response=requests.get(url_ip)
    print "Headers"
    print response.headers
    print "response body"
    print response.text

def uss_params_request():
    params={'param1':'hello','param2':'world'} 
    response=requests.get(url_get,params=params)
    print "Headers"
    print response.headers
    print "state Code"
    print response.status_code
    print "response body"
    print response.json()
    
    
if __name__=='__main__':
    uss_params_request()
    use_simple_request()

