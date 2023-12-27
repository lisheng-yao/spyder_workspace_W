# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 08:26:17 2023

@author: w
"""

import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filepath = filedialog.askopenfilename()
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r", encoding='utf-8') as input_file:
        text = input_file.read()
    txt_edit.insert(tk.END, text)
    window.title(f"Simple Python IDE - {filepath}")

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension="txt")
    if not filepath:
        return
    with open(filepath, "w", encoding='utf-8') as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Python IDE - {filepath}")

# 創建tk物件
window = tk.Tk()
window.title("Simple Python IDE")

# 介面布局
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# 文本編輯器
txt_edit = tk.Text(window, bg='#4F4F4F',fg='white')

# 按鈕框架
fr_buttons = tk.Frame(window, bg='#3C3C3C')

# 創建按鈕
btn_open = tk.Button(fr_buttons, text="Open", command=open_file, width=17)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)

# gird 布局管理器
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()