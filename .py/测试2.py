import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
data = soup.select('.title b')
for i in range(1):
    print(data[i].text)
