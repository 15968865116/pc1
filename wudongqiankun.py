import requests
from bs4 import BeautifulSoup


b=[]
url='http://www.jueshitangmen.info/wudongqiankun/2.html'
r=requests.get(url)
r.raise_for_status()
print r.status_code
r.encoding=r.apparent_encoding
html=r.text
soup=BeautifulSoup(html,"html.parser")
b=soup.find_all('p')

for i in b:
    print i
