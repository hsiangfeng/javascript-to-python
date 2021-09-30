import requests
import json

username = str(input('請輸入你要查詢的使用者帳號：'))

r = requests.get(f'https://api.github.com/users/{username}/starred')

if r.status_code == 200:
  starList = open('starList.json', 'w+')
  starList.write(json.dumps(r.json()))
  starList.close()
else:
  print('取得 API 過程發生錯誤。')