import requests

def download_image():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36'}
    url="http://easyread.ph.126.net/tfuX2Io4XL0OwmG6itI5kA==/7916756398872722482.jpg"
    response=requests.get(url,headers=headers,stream=True)
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
    print response.status_code
    print response.headers    

if __name__=="__main__":
    download_image()