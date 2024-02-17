# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:02:51 2024

@author: w
"""

import pandas as pd 

dic = {
    "col 1": [1, 2, 3], 
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}


df = pd.DataFrame(dic)

print(df)

print(f'df的型別是: {type(df)}')
print(f'dic的型別是: {type(dic)}')




# {}回傳是什麼東西
# df是什麼東西
