# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:58:35 2023

@author: w
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)   # 產生 0～10 總共 100 連續數字
y =  np.sin(x)     # 使用 NumPy 的廣播方式，產生 sin 數值的陣列 y

print(x)
print(y)

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)  # 繪製折線圖

ax.set(xlim=(0, 8), xticks=np.arange(0, 8),  # 設定座標軸
      ylim=(-3, 3), yticks=np.arange(-3, 3))

plt.show()    # 顯示圖表


#%% 隱性建立 figure

x = [1,2,3,4,5]
plt.plot(x)
plt.show()

#%% 顯性建立 figure

x = [1,2,3,4,5]
f = plt.figure()
plt.subplot()
plt.plot(x)
plt.show()

#%% figure 的兩種使用方法
#%%  plt.figure()

x = [1,2,3,4,5]
f = plt.figure()
plt.subplot()
plt.plot(x)
plt.show()

#%% fig, ax = plt.subplots()

x = [1,2,3,4,5]
fig, ax = plt.subplots()
ax.plot(x)
plt.show()