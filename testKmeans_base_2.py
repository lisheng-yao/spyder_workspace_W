# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:41:09 2023

@author: w
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data = pd.read_csv(r'C:\Users\w\spyder_workspace_W\data\Picture_data_2.csv')  # 将'your_data.csv'替换为实际文件路径

#　過濾電壓資料
keywords = ["Module", "Cell", "Voltage"]
filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
df = data[filtered_columns]
df = df.drop(['Rack_Max_Voltage_Module_Cell_index','Rack_Min_Voltage_Module_Cell_index'], axis=1)

# 過濾溫度資料
keywords = ["Module", "Cell", "Temperature"]
filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
df2 = data[filtered_columns]
df2 = df2.drop(columns = ['Rack_Max_Temperature_Module_Cell_index','Rack_Min_Temperature_Module_Cell_index'])

x_min, x_max = 3175, 3375  
y_min, y_max = 440, 520 

all_data = []

for i in range(0,10):
    d1 = df[i:i+1].T
    d2 = df2[i:i+1].T.loc[df2[i:i+1].T.index.repeat(4)].set_index(df[i:i+1].T.index)
    # print(d2)
    
    # d2.to_csv(r'C:\Users\w\Desktop\data\df2.csv')
    
    X = pd.concat([d1,d2],axis=1)
    X.columns = ["Voltage","Temperature"]
    all_data.append(X)
    
    model = KMeans(n_clusters=3, init='k-means++', n_init=10, random_state=42) #預計分為三群，迭代次數由模型自行定義
    model.fit(X) #建立模型
    plt.scatter(X['Voltage'],X['Temperature'], c = model.labels_) # c=model.labels_:代表資料點的顏色，由模型分類出來的結果，來進行分類和定義。 
    plt.xlabel('Voltage')
    plt.ylabel('Temperature')
    plt.show()
    
    
    
    
# 將累積的數據合併為一個 DataFrame
final_df = pd.concat(all_data)

final_df.to_csv(r'C:\Users\w\Desktop\data\123.csv')