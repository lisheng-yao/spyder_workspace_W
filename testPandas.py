# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:47:07 2023

@author: w
"""

import pandas as pd
# print(pd.__version__)

dic = {
    "col 1": [1, 2, 3], 
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}


# DataFrame dic長度要相同
df = pd.DataFrame(dic)
print(df)


#%% rename
rename_dic = {"col 1": "x", "col 2": "10x"}
# print(df.rename(rename_dic, axis=1))


#%% csv

df = pd.read_csv('http://bit.ly/kaggletrain')
# df.head() 預設看前5行
print(df.head())

#%% 記憶體相關


df.info(memory_usage="deep")

dtypes = {"Embarked" : "category"}
cols = ['PassengerId','Name','Sex','Embarked']

df = pd.read_csv('http://bit.ly/kaggletrain', dtype = dtypes, usecols = cols)
df.info(memory_usage="deep")

#%% Series hihi

dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 }

s1 = pd.Series(dic_data)
print(s1)

registration = [True,False,True,True]
registration = pd.Series(registration)
registration
# dtype: bool


dictionary = {'A':'an animal',
              'B':'a color',
              'C':'a fruit'}
dictionary = pd.Series(dictionary)
dictionary
# dtype: object
