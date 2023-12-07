# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:34:43 2023

@author: w
"""

import pandas as pd

url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"

data = pd.read_csv(url)

x = data["YearsExperience"]
y = data["Salary"]

print(x)
print(y)

# print(data)

#%%

import wget

wget.download("https://github.com/GrandmaCan/ML/raw/main/Resgression/ChineseFont.ttf")


#%%


import matplotlib.pyplot as plt
import matplotlib as mpl 
from matplotlib.font_manager import fontManager


url = "https://raw.githubusercontent.com/GrandmaCan/ML/main/Resgression/Salary_Data.csv"

data = pd.read_csv(url)

x = data["YearsExperience"]
y = data["Salary"]

fontManager.addfont("ChineseFont.ttf")
mpl.rc("font" , family = "ChineseFont")

plt.scatter(x, y, marker="x", color="red")
plt.title("年資-薪水")
plt.xlabel("年資")
plt.ylabel("月薪(千)")
plt.show()


#%%

def plt_pred(w,b):
  y_pred = x*w + b
  plt.plot(x, y_pred, color="blue", label="預測線")
  plt.scatter(x, y, marker="x", color="red", label="真實數據")
  plt.title("年資-薪水")
  plt.xlabel("年資")
  plt.ylabel("月薪(千)")
  plt.xlim([0, 12])
  plt.ylim([-60, 140])
  plt.legend()
  plt.show()
    
    
plt_pred(-5, -30)
    
    
    
    
    