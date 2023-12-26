# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 08:57:17 2023

@author: w
"""

import requests as rq
import time
import threading


def get_BTC_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = rq.get(url)
    data = response.json()
    price = data.get("price")
    return price


def print_BTC_price():
    for i in range(100):  # 或者使用 while True: 讓它無限循環
        btc_price = float(get_BTC_price())
        print("比特幣即時價格（BTC/USDT）: {:.3f}".format(btc_price))
        time.sleep(1)  # 1秒更新一次，可以根據需求調整

# 創建並啟動執行緒
thread = threading.Thread(target=print_BTC_price)
thread.start()

