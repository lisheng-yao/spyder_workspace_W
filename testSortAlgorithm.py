# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 14:14:40 2023

@author: w
"""

import numpy as np


# 演算法題目是1-2+3-4+5-6...+N


def test(N):
    sum = 0
    
    for i in range(1,N+1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
            
    return sum

print(test(10))

#%% 氣泡排序

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr


a = np.random.randint(10,size=10)
# print(a)

bubbleSort(a)






