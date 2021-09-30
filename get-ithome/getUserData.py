import requests
from bs4 import BeautifulSoup
import json
import math

f = open('menu.json', 'r')
data = json.loads(f.read())

for item in data:
  pages = math.ceil(int(item['num']) / 10)
  cacheData = []
  for page in range(pages):
    r = requests.get(f'{item["url"]}&page={page + 1}')
    if r.status_code == 200:
      soup = BeautifulSoup(r.text, 'lxml')
      tags = soup.select('body div.wrapper div.border-frame.clearfix div.contestants-wrapper div.contestants-list.clearfix')
      for tag in tags:
        cacheData.append({
          'id': tag.find('a', { "class": "contestants-expect"}).get('data-id', None),
          'name': tag.find('div', { "class": "contestants-list__name"}).text.strip(),
          'title': tag.find('a', { "class": "contestants-list__title"}).text.strip(),
          'url': tag.find('a', { "class": "contestants-list__title"}).get('href', None),
          'like': tag.find('span', { "class": "contestants-expect__number"}).text.strip()
        })
  print(f'已經取得 {item["name"]} 主題，共 {len(cacheData)} 參賽資料。')
  f = open(f'./data/{item["name"]}.json', 'a')
  f.write(json.dumps(cacheData))
  f.close()