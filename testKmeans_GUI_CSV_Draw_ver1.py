# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:30:51 2023

@author: w
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_name = file_path.split('/')[-1]
        file_label.config(text=f"已上傳檔案：{file_name}")
        perform_clustering(file_path)

def perform_clustering(file_path):
    data = pd.read_csv(file_path)
    # 假設 CSV 檔案有兩列數據適合用於 KMeans
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(data)
    data['Cluster'] = kmeans.labels_

    # 在 Tkinter GUI 中顯示結果
    fig, ax = plt.subplots()
    scatter = ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=data['Cluster'], cmap='viridis')
    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def on_close():
    print("結束執行")
    window.destroy()

# 創建 Tkinter 視窗
window = tk.Tk()
window.title('CSV 上傳與聚類分析')
window.geometry('600x600')

upload_button = tk.Button(window, text="上傳 CSV", command=upload_csv)
upload_button.pack(pady=20)

file_label = tk.Label(window, text="尚未選擇檔案")
file_label.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()