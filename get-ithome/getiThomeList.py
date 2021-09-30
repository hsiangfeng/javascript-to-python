import requests
from bs4 import BeautifulSoup
import json

r = requests.get('https://ithelp.ithome.com.tw/2021ironman/signup/list')

if r.status_code == 200:
  soup = BeautifulSoup(r.text, 'lxml')
  tags = soup.select('body div.wrapper div.border-frame.clearfix div.contestants-nav ul.list-unstyled.contestants-nav__ul li.contestants-nav__item a.group-nav')
  cacheData = []
  for item in tags:
    if item.find('div', { "class": "group-nav__text"}).text.strip() != "全部參賽鐵人":
      cacheData.append({
        'name': item.find('div', { "class": "group-nav__text"}).text.strip(),
        'num': item.find('div', { "class": "group-nav__num"}).text.strip(),
        'url': item.get('href', None)
      })
  f = open('menu.json', 'w')
  f.write(json.dumps(cacheData))
  f.close()