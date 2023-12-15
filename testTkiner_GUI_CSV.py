# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:31:21 2023

@author: w
"""

import tkinter as tk
from tkinter import filedialog

def upload_csv():
    # 使用 filedialog 打開檔案選擇對話框
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        # 這裡可以添加處理 CSV 檔案的邏輯
        print(f"選擇的檔案：{file_path}")

# 創建 Tkinter 視窗
window = tk.Tk()
window.title('CSV 上傳介面')
window.geometry('380x400')

# 添加按鈕以選擇並上傳 CSV 檔案
upload_button = tk.Button(window, text="上傳 CSV", command=upload_csv)
upload_button.pack(pady=20)

window.mainloop()
