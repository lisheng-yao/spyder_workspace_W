# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:21:38 2024

@author: w
"""


import random

# a = set()

# for j in range(6):
#     # 生成 6 個在 1 到 49 之間的獨特隨機數字
#     random_numbers = random.sample(range(1, 49))
#     # 將這些隨機數字加入集合中
#     a.add(random_numbers)

# print(a)


i = 0
max_attempts = 1000000  # 設定最大嘗試次數

while i < max_attempts:
    i += 1
    a = random.sample(range(1, 50), 6)
    a_set = set(a)
    if len(a_set) != len(a):
        print("第", i, "次生成的列表有重複")
        break

print("生成的列表:", a)


#%%


num = 49
num_list = []

for i in range(0, num, 1):
  num_list.append(i+1)
  

# random.sample
print(f'Your lucky number: {random.sample(num_list, 6)}') 


#%%


a = [i %  49 +1 for i in range(6)]
print(a)





















