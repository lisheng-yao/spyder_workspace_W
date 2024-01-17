# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 16:06:50 2023

@author: w
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

RawData = load_iris()
df = pd.DataFrame(RawData['data'],columns= RawData['feature_names'])



from sklearn.cluster import KMeans

# x = df.iloc[:,:] # x為所有特徵資料
# x



model = KMeans(n_clusters=2, init='k-means++', n_init=10, random_state=42) #預計分為三群，迭代次數由模型自行定義
model.fit(df) #建立模型
plt.scatter(df['petal length (cm)'],df['petal width (cm)'], c = model.labels_) #根據花瓣的長度、寬度，來畫出之間關係。c=model.labels_:代表資料點的顏色，由模型分類出來的結果，來進行分類和定義。 
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()

#%%


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_scaled = scaler.fit_transform(df) # X 是包含特徵數據的數組

model = KMeans(n_clusters=2, init='k-means++', n_init=10, random_state=42)
model.fit(x_scaled)

plt.scatter(x_scaled[:,2], x_scaled[:,Temperature], c=model.3labels_) # 使用縮放後的特徵
plt.xlabel('petal length (scaled)')
plt.ylabel('petal width (scaled)')
plt.show()

# 我不知道現在哪一家
# 但我知道你是個婊子


#%%

DistanceList = []
for i in range(1,11): #測試將資料分為1~10群
    KM = KMeans(n_clusters=i, init='k-means++', n_init=10, random_state=42)
    KM.fit(df) #建立模型
    DistanceList.append(KM.inertia_) #求出每個Cluster內的資料與其中心點之平方距離和，並用List記錄起來
plt.plot(range(1,11), DistanceList)
plt.show()