import json
import requests
from requests import exceptions
url='https://api.github.com'
def build_uri(endpoint):
    return '/'.join([url,endpoint])
def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)
def request_method():
    response=requests.get(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'))
    print better_print(response.text)
def params_request():
    response=requests.get(build_uri('users'),params={'since':11})
    print better_print(response.text)
    print response.request.headers
    print response.url
    
def json_request():
#     response=requests.patch(build_uri('user'),auth=('imoocdemo','imoocdemo123'),json={'name':'babymooc2','email':'fsf@imooc.org'})
    response=requests.post(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),json=['agfeagr@sds.com'])
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code
def timeout_request():
    try:
        respomse=requests.post(build_uri('user/emails'),timeout=10)
        respomse.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print respomse.text
        
if __name__=='__main__':
#     request_method()
#     params_request()
#     json_request()
    timeout_request()
    
