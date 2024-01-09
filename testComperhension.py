# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:44:40 2024

@author: w
"""

# comperhension

a = [ i for i in range(10) ]
b = ( i for i in range(10) )


print(a)
print(b)


c = [ i*i for i in range(1,10)]

print(c)

# 有一個 a 串列，接著要建立一個 b 串列，b 串列每個內容項目是 a 串列的最大值減去其他項目的值

a = [10,20,30,40,50,60,70,80,90]
b = []
for i in a:
    b.append(max(a)-i)
print(b)

b = [max(a)-i for i in a]
print(b)




#%%

a = []

for i in 'abc':
    for j in range(1,4):
        a.append(i + str(j))
# print(a)


a = [i+str(j) for i in 'abc' for j in range(1,4)]
print(a)

list = []
tuple()
d = {1:'v',2:'b'}


#%%

a = '123'
b = a[::2]
print(b)

#%%

def gg(max):
    s = set()
    for n in range(2,max):
        if all(n%i>0 for i in s):
            s.add(n)
            yield n 
print(*gg(100))
    


print(a)
