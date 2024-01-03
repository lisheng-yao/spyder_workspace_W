# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:31:12 2023

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
        next_button.config(state=tk.NORMAL)

def draw_next_plot():
    global data, current_index, canvas

    if current_index >= 200:  #  200是假設的最大圖表數量
        print("所有圖表已顯示完畢")
        return

    threading.Thread(target=process_and_visualize, args=(current_index,)).start()
    current_index += 1
    
    
def draw_plot(direction):
    global data, current_index, canvas

    if direction == "next" and current_index < 200:  # 假設的最大圖表數量
        current_index += 1
    elif direction == "previous" and current_index > 0:
        current_index -= 1
    else:
        print("沒有更多圖表可以顯示")
        return
    
    threading.Thread(target=process_and_visualize, args=(current_index,)).start()
    

def process_and_visualize(index):
    # ...（省略數據處理部分）

# 功能按鈕新增中    
# def on_previous_button_click():
    # draw_plot("previous")

# def on_next_button_click():
#     draw_plot("next")

    # 數據處理邏輯
    keywords = ["Module", "Cell", "Voltage"]
    filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
    df = data[filtered_columns]
    df = df.drop(columns=['Rack_Max_Voltage_Module_Cell_index', 'Rack_Min_Voltage_Module_Cell_index'])

    keywords = ["Module", "Cell", "Temperature"]
    filtered_columns = [col for col in data.columns if all(keyword in col for keyword in keywords)]
    df2 = data[filtered_columns]
    df2 = df2.drop(columns=['Rack_Max_Temperature_Module_Cell_index', 'Rack_Min_Temperature_Module_Cell_index'])

    d1 = df[index:index+1].T
    d2 = df2[index:index+1].T.loc[df2[index:index+1].T.index.repeat(4)].set_index(df[index:index+1].T.index)
    X = pd.concat([d1, d2], axis=1)
    X.columns = ["Voltage", "Temperature"]

    if canvas is not None:
        canvas.get_tk_widget().pack_forget()

    fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
    ax.scatter(X['Voltage'], X['Temperature'], c=X['Temperature'], cmap='rainbow')
    ax.set_xlabel('Voltage')
    ax.set_ylabel('Temperature')
    ax.set_title('Scatter Plot with Custom Colormap')
    ax.set_xlim(3175, 3375)
    ax.set_ylim(440, 520)

    def update_gui():
        global canvas
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    window.after(0, update_gui)

def on_close():
    print("結束執行")
    window.destroy()

# 創建 Tkinter 視窗
window = tk.Tk()
window.title('CSV 上傳與數據可視化')
window.geometry('600x600')

upload_button = tk.Button(window, text="上傳 CSV", command=upload_csv)
upload_button.pack(pady=20)

next_button = tk.Button(window, text="繪製下一張圖表", command=draw_next_plot, state=tk.DISABLED)
next_button.pack(pady=10)

file_label = tk.Label(window, text="尚未選擇檔案")
file_label.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", on_close)

data = None
current_index = 0
canvas = None

window.mainloop()