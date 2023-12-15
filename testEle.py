#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 09:58:19 2023

@author: yaolisheng
"""

# ====================== 充放電圖表練習2 ============================
import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
df = pd.read_csv('/Users/yaolisheng/Desktop/data/充放電/111/A/2023-09-26_ID_04_Cell_All.csv',
                 parse_dates=['Time'], date_format='%H:%M:%S')

# 計算經過的時間（以分鐘為單位）
df['Elapsed Time (minutes)'] = (
    df['Time'] - df['Time'].min()).dt.total_seconds() / 60

# 提取需要繪製的列
columns_to_plot = ['Cell_00', 'Cell_01', 'Cell_02',
                   'Cell_03', 'Cell_04', 'Cell_05', 'Cell_06', 'Cell_07']

# 繪製每個 Cell 的折線圖
for column in columns_to_plot:
    plt.plot(df['Elapsed Time (minutes)'], df[column], label=column)

# 設定圖表標題和標籤
plt.title('Cell Values Over Time')
plt.xlabel('Elapsed Time (minutes)')
plt.ylabel('Cell Values (V)')

# 添加圖例
plt.legend()

# 顯示圖表
plt.show()
