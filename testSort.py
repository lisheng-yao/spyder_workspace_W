#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 00:28:09 2023

@author: yaolisheng
"""

#%% 選擇排序（Selection sort）

def selectionSort(a):
    n = len(a)
    for i in range(n - 1):
        min = i
        for j in range(i+1 , n):
            if a[j] > a[min]:
                min = j 
        a[i],a[min] = a[min],a[i] # 賦值交換位置
        print(a)

a = [2 , 0 , 3 , 6, 2 ,1 ,10 ,9 ,3]
selectionSort(a)

                

#%% 氣泡排序 （Bubble Sort）

def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0 , len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j] ,arr[j + 1] = arr[ j + 1] , arr[j]
                print(arr)
    return arr

arr = [2 , 0 , 3 , 6, 2 ,1 ,10 ,9 ,3]
bubbleSort(arr)

#%% 插入排序

def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0  and arr[preIndex] > current:
            arr[preIndex + 1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex +1 ] = current
        print(arr)
        
    return arr
    
arr = [2 , 0 , 3 , 6, 2 ,1 ,10 ,9 ,3]
insertionSort(arr)

#%% 希爾排序

def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1
    while gap > 0:
        for i in range(gap,len(arr)):
            temp = arr[i]
            j = i-gap
            while j >=0 and arr[j] > temp:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
        print(arr)
    return arr

arr = [2 , 0 , 3 , 6, 2 ,1 ,10 ,9 ,3]
shellSort(arr)

#%% 歸併排序
import math

def mergeSort(arr):
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    print(arr)
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0));
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result

arr = [2 , 0 , 3 , 6, 2 ,1 ,10 ,9 ,3]
mergeSort(a)








