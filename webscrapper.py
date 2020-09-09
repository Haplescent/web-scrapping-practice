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
    websitename = re.sub(r'.+\/\/|www.|\..+', '', url)
    print(websitename)
    
    # remove multiple linebreaks and whitespace
    txt = Newlines.sub('\n', txt)
    tempfile = open(websitename,"w+")
    tempfile.writelines(txt)
    return txt

def main():
    urls = [

    ]
    txt = [getPageText(url) for url in urls]
    print(len(txt))
    
    file1 = open("everything.txt","w")
    file1.writelines(txt)

if __name__=="__main__":
    main()
