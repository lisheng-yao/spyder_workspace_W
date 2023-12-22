# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:56:46 2023

@author: w
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
# 1. 读取CSV文件
data = pd.read_csv(r'C:\Users\w\spyder_workspace_W\data\Picture_data_2.csv')  # 将'your_data.csv'替换为实际文件路径


# 关键词列表
keywords = ["Module", "Cell", "Voltage"]
filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
# print(filtered_columns)
# 用過濾出來的字當column 產新的df
df = data[filtered_columns]
# print(df)

# dorp固定名稱欄位
df = df.drop(['Rack_Max_Voltage_Module_Cell_index','Rack_Min_Voltage_Module_Cell_index'], axis=1)
df.to_csv(r'C:\Users\w\Desktop\data\MVax.csv', index = False)
# 印出過濾後資料

keywords = ["Module", "Cell", "Temperature"]
filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
df2 = data[filtered_columns]
df2 = df2.drop(columns = ['Rack_Max_Temperature_Module_Cell_index','Rack_Min_Temperature_Module_Cell_index'])
df2.to_csv(r'C:\Users\w\Desktop\data\MT.csv', index = False) 
# 印出過濾後資料

x_min, x_max = 3175, 3375  
y_min, y_max = 440, 520 


for i in range(0,200):
    d1 = df[i:i+1].T
    # print(d1)
    d2 = df2[i:i+1].T.loc[df2[i:i+1].T.index.repeat(4)].set_index(df[i:i+1].T.index)
    print(d2)