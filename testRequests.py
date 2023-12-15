#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:29:35 2023

@author: yaolisheng
"""

import requests
from bs4 import BeautifulSoup

#%% 爬取第一個靜態網頁內容

url = 'https://water.taiwanstat.com/'
web = requests.get(url)
web.encoding='utf-8'       # 因為該網頁編碼為 utf-8，加上 .encoding 避免亂碼
print(web.text)


#%% 透過 API 爬取第一個開放資料

data = requests.get('https://data.kcg.gov.tw/dataset/6f29f6f4-2549-4473-aa90-bf60d10895dc/resource/30dfc2cf-17b5-4a40-8bb7-c511ea166bd3/download/lightrailtraffic.json')
data2 = data.content.decode('utf-8-sig')

print(data2)


#%% Response 物件的屬性與方法 


url = 'https://water.taiwanstat.com/'
web = requests.get(url)

print('● 資源的 URL 位址 :',web.url)
print('● 回應的狀態 ( int ) :',web.status_code)
print('● 回應訊息的 cookies ( dict ) :',web.cookies)
print('● 請求歷史 ( list ) :',web.history)
# print('● 回應訊息的內容 ( bytes ) :',web.content)
# print('● 原始回應訊息串流 ( bytes ) :',web.raw)
# print('● 回應訊息的內容字串 ( str ) :',web.text)
# print('● 回應訊息的標頭 ( dict ) :',web.headers)
# print('● 回應訊息進行 JSON 解碼後回傳 ( dict ):',web.json())
# print('● 是否有例外發生 :',web.rasise_for_status())



#%%

url = 'https://water.taiwanstat.com/'
web = requests.get(url)
soup = BeautifulSoup(web.text, "html.parser")
reservoir = soup.select('.reservoir')                      # 取得所有 class 為 reservoir 的 tag
for i in reservoir:
  print(i.find('div', class_='name').get_text(), end=' ')  # 取得內容的 class 為 name 的 div 文字
  print(i.find('h5').get_text(), end=' ')                  # 取得內容 h5 tag 的文字
  # print(i.find('h5', class_='state red').get_text(), end=' ')                  # 取得內容 h5 tag 的文字
  print()

#%% 傳遞參數

import requests
url = 'https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec'


params ={'name' : 'ooxx'}
age = 1


for _ in range(10):
    params['age'] = str(age)
    response = requests.get(url, params=params)
    print(response.status_code)
    age += 1



# 重置 age 用於 while 
age = 0

# 使用 while 重新發送
while age > 11:
    params['age'] = str(age)
    response = requests.get(url, params=params)
    print(response.text)
    age += 1
    
     
    

#%% 壓力測試

import threading

def send_request(url, params):
    import requests
    while True:
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                print(response.text)
            else:
                print(f"錯誤代碼: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"請求異常: {e}")


url = 'https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec'
params = {'name': 'ooxx', 'age': '18'}

threads = 8  # 根据需要调整线程数

for i in range(threads):
    t = threading.Thread(target=send_request, args=(url, params))
    t.start()

