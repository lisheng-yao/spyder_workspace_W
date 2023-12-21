# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 08:44:38 2023

@author: w
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame([[1]*4 , [2]*4 , [3]*4], columns=["col1", "col2" , "col3" , "col4"])
df2 = pd.DataFrame([[1.1]*4 , [2.1]*4 , [3.1]*4], columns=["col5", "col6" , "col7" , "col8"])


marged_data = pd.concat([df1, df2] , axis = 1)


# 去除console的index
print(marged_data.to_string(index=False))

# 去除CSV的index
marged_data.to_csv(r"C:\Users\w\Desktop\data\m.csv" , index = False)


# print(df.mean(axis = 1 ))

# print(df.mean(axis = 0 ))

# print(df1.drop("col3" , axis=1 ))
# print(df1.drop(index=0 , axis=0 ))