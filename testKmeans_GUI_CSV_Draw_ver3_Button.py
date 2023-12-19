# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 11:17:37 2023

@author: w
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        file_name = file_path.split('/')[-1]
        file_label.config(text=f"已上傳檔案：{file_name}")
        global data
        data = pd.read_csv(file_path)
        process_data(data)
        draw_button.config(state=tk.NORMAL)
        next_button.config(state=tk.NORMAL)

def process_data(data):
    global df, df2
    # 數據處理邏輯
    keywords = ["Module", "Cell", "Voltage"]
    filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
    df = data[filtered_columns]
    df = df.drop(columns=['Rack_Max_Voltage_Module_Cell_index', 'Rack_Min_Voltage_Module_Cell_index'])

    keywords = ["Module", "Cell", "Temperature"]
    filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
    df2 = data[filtered_columns]
    df2 = df2.drop(columns=['Rack_Max_Temperature_Module_Cell_index', 'Rack_Min_Temperature_Module_Cell_index'])

def draw_plot(index):
    if index < min(len(df.columns), len(df2.columns)):  # 檢查索引是否在數據範圍內
        d1 = df.iloc[:, index:index+1]
        d2 = df2.iloc[:, index:index+1].loc[df2.iloc[:, index:index+1].index.repeat(4)].set_index(df.iloc[:, index:index+1].index)
        X = pd.concat([d1, d2], axis=1)
        X.columns = ["Voltage", "Temperature"]

        fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
        ax.scatter(X['Voltage'], X['Temperature'], c=X['Temperature'], cmap='rainbow')
        ax.set_xlabel('Voltage')
        ax.set_ylabel('Temperature')
        ax.set_title('Scatter Plot with Custom Colormap')
        ax.set_xlim(3175, 3375)
        ax.set_ylim(440, 520)

        def update_gui():
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 在主線程中更新 GUI
        window.after(0, update_gui)

def start_drawing():
    global index
    index = 0
    draw_next_plot()

def draw_next_plot():
    global index
    threading.Thread(target=draw_plot, args=(index,)).start()
    index += 1

def on_close():
    print("結束執行")
    window.destroy()

# 創建全局變量
data, df, df2 = None, None, None
index = 0

# 創建 Tkinter 窗口
window = tk.Tk()
window.title('CSV 上傳與數據可視化')
window.geometry('600x600')

upload_button = tk.Button(window, text="上傳 CSV", command=upload_csv)
upload_button.pack(pady=20)

draw_button = tk.Button(window, text="開始繪製圖表", command=start_drawing, state=tk.DISABLED)
draw_button.pack(pady=10)

next_button = tk.Button(window, text="繪製下一張圖表", command=draw_next_plot, state=tk.DISABLED)
next_button.pack(pady=10)

file_label = tk.Label(window, text="尚未選擇檔案")
file_label.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", on_close)
window.mainloop()
