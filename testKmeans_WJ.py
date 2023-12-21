# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:44:45 2023

@author: w
"""

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
# 1. 读取CSV文件
data = pd.read_csv(r'C:\Users\w\Downloads\Picture_data_2.csv')  # 将'your_data.csv'替换为实际文件路径


# 关键词列表
keywords = ["Module", "Cell", "Voltage"]
filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
# print(filtered_columns)
print(data[filtered_columns])
df = data[filtered_columns]
# print(df)
df = df.drop(columns = ['Rack_Max_Voltage_Module_Cell_index','Rack_Min_Voltage_Module_Cell_index'])
# df.to_csv(r'C:\Users\w\Desktop\data\MV.csv', index = False) 
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
    d2 = df2[i:i+1].T.loc[df2[i:i+1].T.index.repeat(4)].set_index(df[i:i+1].T.index)

#     X = pd.concat([d1,d2],axis=1)
#     X.columns = ["Voltage","Temperature"]
    
#     # 3. 执行K均值聚类
#     # kmeans = KMeans(n_clusters=5)  # 假设要分为3个簇
#     # kmeans.fit(X)
#     # # 4. 获取聚类结果
#     # X['Cluster'] = kmeans.labels_  # 将聚类结果添加到数据中
    
#     # 5. 可视化聚类结果
#     plt.figure(figsize=(5, 5),dpi=100)

#     # cmap = LinearSegmentedColormap.from_list('custom_cmap', [(0, 'blue'), (1, 'red')])
#     plt.scatter(X['Voltage'], X['Temperature'], c=X['Temperature'], cmap='rainbow')
#     plt.xlabel('Voltage')
#     plt.ylabel('Temperature')
#     plt.title('Scatter Plot with Custom Colormap')
#     plt.xlim(x_min, x_max)  # 固定 X 轴范围
#     plt.ylim(y_min, y_max)  # 固定 Y 轴范围
#     plt.show()