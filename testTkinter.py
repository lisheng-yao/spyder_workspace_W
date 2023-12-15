#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:48:06 2023

@author: yaolisheng
"""

import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')        # 設定標題
root.iconbitmap('favicon.ico')  # 設定 icon ( 格式限定 .ico )

# 如果是 Mac 使用下面這行，可以使用 gif 或 png
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='icon.gif'))
root.mainloop()