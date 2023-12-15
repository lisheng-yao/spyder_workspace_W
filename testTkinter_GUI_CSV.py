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
        # 處理 CSV 檔案的邏輯
        file_name = file_path.split('/')[-1]
        file_label.config(text=f"已上傳檔案：{file_name}") # 更新標籤以顯示檔案名稱
        print(f"選擇的檔案：{file_path}")
        
def on_close():
    print("結束執行")
    window.destroy()
    

# 創建 Tkinter 視窗
window = tk.Tk()
window.title('CSV 上傳')
window.geometry('380x400')
window.resizable(True,True)
window.iconbitmap(r'C:\Users\w\Desktop\logo\logo2.ico')



# 添加按鈕以選擇並上傳 CSV 檔案
upload_button = tk.Button(window, text="上傳 CSV", command=upload_csv)
upload_button.pack(pady=20)
# 添加用於顯示檔案名稱的標籤
file_label = tk.Label(window, text="尚未選擇檔案")
file_label.pack(pady=10)

# 綁定視窗關閉事件
window.protocol("WM_DELETE_WINDOW", on_close)

window.mainloop()
