# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:04:55 2023

@author: w
"""

import numpy as np

arr = np.array([1,2,3,4,5])

newarr = arr.reshape(5,1) # 五個陣列 每個一個

# [[1]
#  [2]
#  [3]
#  [4]
#  [5]]

print(newarr)

#%% dtype 資料轉換

a = np.array([1.1 , 2.2, 3.3 , 0 , -1])
b = np.array(a , dtype = '?')
c = np.array(a, dtype = 'U')
d = np.array(a, dtype = 'S')
e = np.array(a, dtype = 'B')
f = np.array(a, dtype = 'i')

print(a)   # [ 1.1  2.2  3.3  0.  -1. ]
print(b)   # [ True  True  True False  True]
print(c)   # ['1.1' '2.2' '3.3' '0.0' '-1.0']
print(d)   # [b'1.1' b'2.2' b'3.3' b'0.0' b'-1.0']
print(e)   # [  1   2   3   0 255]
print(f)   # [ 1  2  3  0 -1]


#%% astype 資料轉換

a = np.array([1,2,3,4], dtype="int32")
b = a.astype('float32')

print(a)
print(b)

#%% 結構化轉換型態

dt = np.dtype([('a' , 'U5'),( 'b' , 'f'),( 'c' , '?')])
a = np.array([(1.1 ,2.2 ,3.3),(1.1 ,2.2 ,3.3)], dtype=dt)
print(a)


#%% 取得資料型態
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5], dtype='U10')
print(a.dtype)    # int64
print(b.dtype)    # <U10
print(a)
print(b)