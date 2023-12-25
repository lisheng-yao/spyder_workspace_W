# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 14:06:53 2023

@author: w
"""

import matplotlib.pyplot as plt
import random
fig = plt.figure(figsize=(10,8))
ax = plt.subplot(projection='3d')
x = [random.randint(0,100) for i in range(150)]
y = [random.randint(0,100) for i in range(150)]
z = [random.randint(0,100) for i in range(150)]
ax.scatter(x,y,z,s=90,c=z,cmap='Reds')
ax.scatter(y,z,x,s=90,c=x,cmap='Blues')
ax.scatter(z,x,y,s=90,c=y,cmap='Greens')
plt.show()

#%%


fig = plt.figure(figsize=(10,8))
ax = plt.subplot(projection='3d')
x1 = [random.randint(0,100) for i in range(5000)]
x2 = [random.randint(100,200) for i in range(5000)]
x3 = [random.randint(200,300) for i in range(5000)]
y = [random.randint(0,100) for i in range(5000)]
z = [random.randint(0,100) for i in range(5000)]
ax.scatter(x1,y,z,s=30,c=z,cmap='Reds')
ax.scatter(x2,y,z,s=30,c=z,cmap='Blues')
ax.scatter(x3,y,z,s=30,c=z,cmap='Greens')
plt.show()


#%%


fig = plt.figure(figsize=(8,6)) 
ax = plt.subplot(projection='3d') 
x = [random.randint(0,100) 
for i in range(200)] # 取得 200 個 0～100 的隨機整數 
y = [random.randint(0,100) for i in range(200)] # 取得 200 個 0～100 的隨機整數 
z = [random.randint(0,100) for i in range(200)] # 取得 200 個 0～100 的隨機整數 
ax.scatter(x,y,z,s=50) 
plt.show()

#%%

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(projection='3d')
plt.show()