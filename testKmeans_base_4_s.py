# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:21:31 2024

@author: w
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# 生成虛擬數據
X, y = make_blobs(n_samples=200, centers=4, random_state=42)
# print(X)
print(y)

# 建立 K-means 模型，指定分為 4 群
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# 計算每個點到其所屬群集中心的距離
distances = kmeans.transform(X)
# print(distances)
# 取得每個點到其所屬群集中心的最小距離
min_distances = np.min(distances, axis=1)

# 設定閾值，超過閾值的點視為離群值
threshold = 3.0
outliers = X[min_distances > threshold]

# 繪製原始數據點和 K-means 分群的結果
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis', edgecolor='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
# print(kmeans.cluster_centers_)


plt.scatter(outliers[:, 0], outliers[:, 1], c='orange', marker='o', s=100, label='Outliers')
# print(outliers)
# print(type(outliers)) # <class 'numpy.ndarray'>

# [[-6.68168628 -6.81047379]
#  [-2.50135734  9.05295553]
#  [ 4.5923149   1.95045129]
#  [-8.81208336  7.39287605]]
# [[  7.71875964   3.0927446 ]
#  [ -5.88161708  -9.77636497]
#  [ -9.91046677   4.40217243]
#  [ -9.37903291  -4.58916702]
#  [-10.00824459   4.4512607 ]
#  [ -1.99414994  12.86701762]
#  [ -5.75046496   7.98989849]]


plt.title('K-means Clustering with Outliers')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()