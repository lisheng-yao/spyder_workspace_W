# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:04:22 2023

@author: w
"""

set = {'a':1 , 'b':2 }

print(len(set))

#%%


import time

n = 10 
for i in range(n+1):
    print(f'\r {n-i}' , end=' ')
    time.sleep(0.5)
    
print("\r boom!!!")

#%%


def a (x):
    return x + 1

b =  map(a, [1,2,3,4,5])
c =  map(lambda x : x + 1 , [1,2,3,4,5])

print(list(b))
print(tuple(c))

#%%

def hello(title):
    print(title)
    
hello("Hi")
(lambda title : print(title))('Hi lambda')


#%%

def a(x,y):
    return x + y

b = lambda x,y : x + y

print(a(1,2))
print(b(1,2))

#%%

def x(n):
    a = list(range(n))
    return a 

y = lambda n:[i for i in range(n)]


print(y(5))



#%%

def x1 (n):
    a = list(range(n))
    return a 

y = lambda n: [i for i in range(n)]

print(y(5))


#%%

def y (n):
    if n <= 10 :
        return True
    
    else:
        
        return False

z = lambda n: True if n <= 10 else False


print(z(10))
print(y(10))


#%%

def s (x):
    return x*x

a = [1,2,3,4,5,6,7,8,9]
b = map(lambda x : x*x ,a)

print(list(b))

#%%

a = [[1,2],[4,3],[5,1],[9,2],[3,7]]
b = sorted(a, key = lambda x: x[1])
print(list(b))    # [[5, 1], [1, 2], [9, 2], [4, 3], [3, 7]]



#%%

a = ['1','2',3,'4']

print(a)

b = list(map(int , a))
print(b)

#%%

c = filter(lambda x : x>2 ,[1,2,3,4,5])

print(list(c))

d = [1,2,3,4]
d.append(5)

print(d)

#%%


a = [[1,8],[2,1],[5,2],[3,5],[9,3]]
b = sorted(a, key=lambda x: x[0])

print(list(b))


#%%


a = [6,1,2,3,4,5]
b = sorted(a)
print(b)


#%%


def a (x):
    return x[0]

b = [[1,8],[2,1],[5,2],[3,5],[9,3]]

c = sorted(b , key=a)

print(list(c))

#%%


a = [1,2,3,4,5]
b = [0,1,2,3,4]
c = []

print(all(a))

if not all(b):
    print("oh ya baby!")
    
print(any(b))
print(any(c))
    
#%%


f = open(r'C:\Users\w\Desktop\新文字文件.txt','r')
a = f.read()
print(a)
f.close()

#%%

f = open(r'C:\Users\w\Desktop\新文字文件.txt','at+')
a = f.read()

for i in range(100):
        f.write('\nhello')
        
print(a)
f.close()

#%%
f = open(r'C:\Users\w\Desktop\新文字文件.txt', 'at+')

# 將文件指針移到開頭，然後讀取內容
f.seek(0)
a = f.read()

# 追加新內容
for i in range(100):
    f.write('\nhello')

# 顯示讀取到的內容
print(a)

f.close()

#%%




