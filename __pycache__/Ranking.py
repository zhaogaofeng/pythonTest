import requests
import re
import bs4
from bs4 import BeautifulSoup
# 输入URL获取到对应的HTML


def getHtmlText(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status
        response.encoding = response.apparent_encoding

    except Exception as e:
        raise e


# 从HTML文本中获取到大学信息并存入数组中


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string])

# 打印存储大学信息的数组


def printUnivlist(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}").format("排名", "学校", "分数")
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^6}\t{:^10}").format(u[0], u[1], u[2])

uinfo = []
url = "http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html"
html = getHtmlText(url)
fillUnivList(uinfo, html)
printUnivlist(uinfo, 10)
print("s")
