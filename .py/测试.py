import requests
from bs4 import BeautifulSoup
def getHTML(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
    
def parsePage(html):
    soup = BeautifulSoup(url, "html.parser")
    soup.find_next_siblings('tbody')
    res = soup.text
    
def printInfo(res):
    print(res)
    pass
def main():
    url = 'https://python123.io/ws/demo.html'
    html = getHTML(url)
    parsePage(url)
    printInfo(res)
main()
