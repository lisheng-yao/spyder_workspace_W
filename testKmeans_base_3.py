# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 14:57:30 2023

@author: w
"""


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv(r'C:\Users\w\Desktop\data\123.csv')  # 替换为您的文件路径

# 按每16行分割数据
n = 16  # 每组数据的行数
grouped_data = [data[i:i + n] for i in range(0, data.shape[0], n)]



# 为每组数据应用 K-Means 聚类并绘图
for i, group in enumerate(grouped_data):
    X = group[['Voltage', 'Temperature']]
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
    kmeans.fit(X)

    plt.figure(figsize=(10, 6),dpi=100)
    plt.scatter(X['Voltage'], X['Temperature'], c=kmeans.labels_, cmap='viridis')
    plt.title(f'K-Means Clustering of Voltage and Temperature - Group {i+1}')
    plt.xlabel('Voltage')
    plt.ylabel('Temperature')
    plt.xlim(3280, 3375)
    plt.ylim(440, 520)
    
    plt.colorbar(label='Cluster Label')
    plt.show()
