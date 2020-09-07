import urllib3
from bs4 import BeautifulSoup
import re

Newlines = re.compile(r'[\r\n]\s+')

def getPageText(url):
    http = urllib3.PoolManager()
    # given a url, get page content
    response = http.request('GET', url)
    # parse as html structured document
    bs = BeautifulSoup(response.data)
    # kill javascript content
    for s in bs.findAll('script'):
        s.replaceWith('')
    # find body and extract text
    txt = bs.find('body').getText('\n')
    # remove multiple linebreaks and whitespace
    return Newlines.sub('\n', txt)

def main():
    urls = [
        'https://lemnos.vc',
        'https://www.zettavp.com/',
        'https://lsvp.com',
        'https://bolt.io/',
        'http://unionlabs.com/',
    ]
    txt = [getPageText(url) for url in urls]
    print(len(txt))
    file1 = open("myfile.txt","w")
    file1.writelines(txt)

if __name__=="__main__":
    main()
