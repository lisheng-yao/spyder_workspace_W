# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:28:32 2024

@author: w
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 讀取CSV文件
df = pd.read_csv(r'C:\Users\w\Desktop\台塑\20231228_CHT\UPS2-1\Log\20231007_log.csv')

# 將Timestamp轉換為datetime對象，忽略無效的數據
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce', format='%Y/%m/%d %H:%M:%S')
# print(df['Timestamp'])

# 過濾掉無效的時間戳數據
df = df.dropna(subset=['Timestamp'])
# print(df)


# 過濾數據，只保留2023/10/8 00:00:00之後的數據
df_filtered = df[df['Timestamp'] >= '2023-10-07 00:00:00']
# print(df_filtered)

# 按每分鐘進行分組並計算每分鐘的次
df_resampled = df_filtered.resample('1T', on='Timestamp').count()
df_resampled.to_csv(r"C:\Users\w\Desktop\data\errortime1007.csv" )

# 繪製長條圖
plt.figure(figsize=(10, 6))
plt.bar(df_resampled.index, df_resampled['Information'], width=0.8)

# 設置 x 軸標籤格式
plt.gca().xaxis.set_major_locator(MaxNLocator(prune='both'))

plt.title('RS485 RTU Communication Errors Per Minute')
plt.xlabel('Timestamp')
plt.ylabel('Error Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()