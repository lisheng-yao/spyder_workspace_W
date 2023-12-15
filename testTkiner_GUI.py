# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:51:49 2023

@author: w
"""

import tkinter as tk

window = tk.Tk()
window.title('GUI_test')
window.geometry('380x400')
window.resizable(True, True)
window.iconbitmap(r'C:\Users\w\Desktop\logo\logo2.ico')

test = tk.Button(text="測試")
test.pack(side="top")

window.mainloop()