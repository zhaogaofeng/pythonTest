import requests
from bs4 import BeautifulSoup
r = requests.get("https://python123.io/ws/demo.html")
r.encoding = r.apparent_encoding
demo=r.text
soup=BeautifulSoup(demo,"html.parser")

print(soup.a.prettify())

