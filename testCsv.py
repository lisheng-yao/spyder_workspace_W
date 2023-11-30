#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 08:48:54 2023

@author: yaolisheng
"""


#%%
import os
import csv
print("當前工作目錄：", os.getcwd()) # 當前工作目錄


csvfile = open('csv-demo.csv')
r = csv.reader(csvfile)
# print(type(r)) ＃ r資料型別
for row in list(r):
    print(row)

#%% writerow

csvfile = open('csv-demo.csv' , 'a+')
r = csv.writer(csvfile)

r.writerow('') 
r.writerow(['banana',5,'yellow',20])

#%% weiterows

csvfile = open('csv-demo.csv' , 'a+')
r = csv.writer(csvfile)
data = [
    ['banana',6,'yellow',20],
    ['papaya',7,'orange',30]
      ]
r.writerows(data)


#%% 刪除data方法

with open('csv-demo.csv') as file:
    r = csv.reader(file)
    data = list(r)
    
del data[5:9]

with open('csv-demo.csv','w') as file:
    w = csv.writer(file)
    w.writerows(data)
    
#%% DictReader(csvfile)
import csv

csvfile = open('csv-demo.csv', 'r')   # 開啟 CSV 檔案模式為 r
data = csv.DictReader(csvfile)        # 以字典方式讀取資料

for i in data:
    print(i['name'],i['id'],i['color'],i['price'])   # 分別印出不同鍵的值
    # print(i)    

#%% DictReader(csvfile) 字設定key

csvfile = open('csv-demo.csv', 'r')   # 開啟 CSV 檔案模式為 r
keys = ['a','b','c','d']  # 手動設定字典的鍵
data = csv.DictReader(csvfile, fieldnames=keys) # 設定 fieldnames 為 keys

for i in data:
    print(i)

#%% DictWriter(csvfile, fieldnames)

fieldnames = ['name','id','color','price']    # 定義要寫入資料的鍵

with open('csv-demo.csv','w') as csvfile:
    data = csv.DictWriter(csvfile, fieldnames=fieldnames)  # 設定 data 為寫入資料
    data.writeheader()  # 寫入欄位名稱
    data.writerow({'name':'papaya','id':8,'color':'orange','price':30})  # 寫入資料















