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

x = [1,2,1,4,5]
f = plt.figure()
plt.subplot()
plt.plot(x)
plt.show()

#%% fig, ax = plt.subplots()

x = [1,2,3,4,5]
y = [1,2,3,4,5]

fig, ax = plt.subplots()
ax.plot(x)
ax.plot(y)
plt.show()

#%%

x = [1,2,3,4,5]
fig = plt.figure(facecolor="pink" , edgecolor = 'black')
plt.subplot()
plt.plot(x)
plt.show()

#%%

x = [1,2,1,4,5]
y = [5,4,5,2,1]
z = [2,3,4,3,2]
fig1 = plt.figure(num=1)
plt.subplot(2,2,1)
plt.plot(x)
fig2 = plt.figure(num=fig1)
plt.subplot(2,2,1)
plt.plot(y)
fig3 = plt.figure(num=1)
plt.subplot(2,2,1)
plt.plot(z)
plt.show()

#%%

x = [1,2,3,4,5]
y = [5,4,3,2,1]
fig = plt.figure()
plt.subplot(221)
plt.plot(x)
plt.subplot(224)
plt.plot(y)
plt.show()


#%%

x = [1,2,3,4,5]
y = [5,4,3,2,1]

fig, ax = plt.subplots(2,2) # 回傳2個物件
ax[0][0].plot(x)
ax[1][1].plot(y)
plt.tight_layout()
plt.show()

#%% 

x = [1,2,3,4,5]
y = [5,4,3,2,1]
fig, ax = plt.subplots()
print(ax)
ax.plot(x)
ax.plot(y)
plt.show()

#%% 圖表標籤

x = [1,2,3,4,5]

fig = plt.figure()
plt.plot(x)
plt.title("test")
plt.xlabel("x")
plt.ylabel("y")





