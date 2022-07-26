import requests
from bs4 import BeautifulSoup

def spider(index):
    indexlen = len(index)
    for i in range(0,indexlen):
        response = requests.get(index[i])
        soup = BeautifulSoup(response.content, 'html5lib')          
        inf= soup.find('div', class_="test-details")
        info = inf.find_all('p')
        name = '%d.txt' % i
        f = open(name,'w', encoding="utf-8")
        for items in info:
            f.write(items.text)
        f.close
        texxt = '%d has been got' % i
        print(texxt)
