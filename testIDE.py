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

window = tk.Tk()
window.title("Simple Python IDE")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window, bg='#4F4F4F',fg='white')
fr_buttons = tk.Frame(window, bg='#3C3C3C')
btn_open = tk.Button(fr_buttons, text="Open", command=open_file, width=17)
btn_save = tk.Button(fr_buttons, text="Save", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=15)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()