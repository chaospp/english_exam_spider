import requests
from lxml import etree
import re

def getindex(nj, km, tx, nd):
    index = {}
    url = 'https://www.xintiku.com/kaoti/nianji_'+nj+'-kemu_'+km+'-tixing_'+tx+'-nandu_'+nd+'/'
    response = requests.get(url)
    selector = etree.HTML(response.text)
    li = selector.xpath('/html/body/section[3]/div[2]/ul/li')
    licount = len(li)
    for i in range(1,licount+1):
        xp = '/html/body/section[3]/div[2]/ul/li[%d]/p[@class="footnote"]/a/@href' % i
        inurl = selector.xpath(xp)
        for item in inurl:
            if item == []:
                break    
            else:
                index[i-1] = item
    return index