# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 13:59:56 2023

@author: w
"""

import pyautogui

print(pyautogui.position()) # 印出滑鼠位置
print(pyautogui.size())

pyautogui.moveTo(100 , 100 , duration = 5 ) #用5秒移動到x=100，y=100的位置
