# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 10:47:46 2024

@author: w
"""

import yfinance as yf
import pandas  as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

Bit = yf.Ticker("BTC-USD")
# 指定開始日期
Bit_hist = Bit.history(period="max")

# Bit_hist.to_csv(r'C:\Users\w\Desktop\data\btc.csv', index='True')

Bit_hist.plot(y = ['Open','Close'],kind='line',subplots=True)



# 计算每100天的移动平均
Bit_hist['MAVG'] = Bit_hist['Close'].rolling(window=100).mean()

# 绘制原始数据和移动平均线
plt.figure(figsize=(10, 6))
plt.plot(Bit_hist.index, Bit_hist['Close'], label='Close', color='blue')
plt.plot(Bit_hist.index, Bit_hist['MAVG'], label='(MAVG)', color='red')
plt.title('Close price vs MAVG')
plt.xlabel('Date')
plt.ylabel('UST')
plt.legend()
plt.show()



#%%

import seaborn as sb

# 获取比特币的历史数据
Bit2 = yf.Ticker("BTC-USD").history(period="max")

# 指定要绘制的特征
features = ['Open', 'Close', 'High', 'Low', 'Volume']

# 创建子图
plt.subplots(figsize=(20,10))

# 绘制箱线图
for i, col in enumerate(features):
    plt.subplot(2, 3, i+1)
    sb.boxplot(Bit2[col])

# 显示图形
plt.show()
