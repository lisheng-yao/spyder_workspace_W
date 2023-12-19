# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:15:37 2023

@author: w
"""

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