import urllib2


class HtmlDownloader(object):
    
    
    def __init__(self):
        pass
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode()!=200:
            return None
        print 200
        return response.read()
    
    



