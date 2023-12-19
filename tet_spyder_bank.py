# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:15:37 2023

@author: w
"""

# 分析 CSV
import requests

url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'
rs = requests.get(url)
rs.encoding = 'utf-8'
rt = rs.text
rts = rt.split('\n')

for i in rts:
    try:
        a = i.split(',')
        print(a[0] , ':' , a[1] , a[2])
    except:
        break
    
#%% 分析txt

# 打開文件並讀取內容
with open(r'C:\Users\w\Downloads\ExchangeRate@202312191422.txt', 'r' , encoding='utf-8') as file:
    lines = file.readlines()
    # print(lines)
    # ['\ufeff幣別        匯率             現金        即期        遠期10天        遠期30天        遠期60天        遠期90天       遠期120天       遠期150天       遠期180天 匯率             現金        即期        遠期10天        遠期30天        遠期60天        遠期90天       遠期120天       遠期150天       遠期180天\n', 'USD         本行買入     30.95000    31.30000        31.27000        31.16700        31.04500        30.93500        30.82000        30.72500        30.62000 本行賣出     31.62000    31.40000        31.37600        31.28100        31.17300        31.07500        30.97000        30.88500        30.80500\n'

# 初始化一個字典來保存幣別和現金匯率
currency_rates = {}

# 解析每一行
for line in lines:
    parts = line.split()  # 以空格分割每一行 
    # print(parts)
    # ['\ufeff幣別', '匯率', '現金', '即期', '遠期10天', '遠期30天', '遠期60天', '遠期90天', '遠期120天', '遠期150天', '遠期180天', '匯率', '現金', '即期', '遠期10天', '遠期30天', '遠期60天', '遠期90天', '遠期120天', '遠期150天', '遠期180天']
    
    if len(parts) > 2 and parts[1] == "本行買入":
        # 將幣別和現金買入價格添加到字典中
        currency = parts[0]
        cash_buy_rate = parts[2]
        currency_rates[currency] = cash_buy_rate
        
        # print(currency_rates)
        # {'USD': '30.95000'}
        # {'USD': '30.95000', 'HKD': '3.86500'}

# 顯示結果
for currency, rate in currency_rates.items():
    print(f"{currency}: {rate}")

