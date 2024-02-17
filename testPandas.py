# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 15:47:07 2023

@author: w
"""

import pandas as pd
# print(pd.__version__)

dic = {
    "col 1": [1, 2, 3], 
    "col 2": [10, 20, 30],
    "col 3": list('xyz'),
    "col 4": ['a', 'b', 'c'],
    "col 5": pd.Series(range(3))
}


# DataFrame dic長度要相同
df = pd.DataFrame(dic)
print(df)


#%% rename
rename_dic = {"col 1": "x", "col 2": "10x"}
# print(df.rename(rename_dic, axis=1))


#%% csv

df = pd.read_csv('http://bit.ly/kaggletrain')
# df.head() 預設看前5行
print(df.head())

#%% 記憶體相關


df.info(memory_usage="deep")

dtypes = {"Embarked" : "category"}
cols = ['PassengerId','Name','Sex','Embarked']

df = pd.read_csv('http://bit.ly/kaggletrain', dtype = dtypes, usecols = cols)
df.info(memory_usage="deep")

#%% Series hihi

dic_data = {'name':'apple','birthday':'1996-1-1','luckynumber':7 }

s1 = pd.Series(dic_data)
print(s1)

registration = [True,False,True,True]
registration = pd.Series(registration)
registration
# dtype: bool


dictionary = {'A':'an animal',
              'B':'a color',
              'C':'a fruit'}
dictionary = pd.Series(dictionary)
dictionary
# dtype: object

#%% 合併csv

df1 = pd.read_csv(r"C:\Users\w\Desktop\data\bank1.csv")
# print(df1)
df2 = pd.read_csv(r"C:\Users\w\Desktop\data\bank2.csv")
# print(df2)

# 使用concat函数合并数据表，axis=0表示在垂直方向上合并（往下）
combined_df = pd.concat([df1, df2], axis=0)

# # 重置索引，因为concat后索引会保持原数据表的索引
# combined_df.reset_index(drop=True, inplace=True)


# 如果您想要将合并后的数据表保存为新的CSV文件
# try:
#     combined_df.to_csv(r"C:\Users\w\Desktop\merged_data.csv", index=True)
#     print("合併成功")
# except Exception as e:
#     print("合併失敗:", e)


from glob import glob
files = glob(r"C:\Users\w\Desktop\data\bank*.csv")
print(files)


df = pd.concat([pd.read_csv(f) for f in files])
df.reset_index(drop = True) # 在此處將 inplace 參數設置為 True 以使 reset_index 永久修改 DataFrame

print(df)

# 輸出合併CSV檔
# output_file_path = r"C:\Users\w\Desktop\merged_data2.csv"  # 指定輸出文件的路徑
# df.to_csv(output_file_path, index=False)  # index=False 表示不將行索引寫入到 CSV 文件中


#%% 完整內容

pd.set_option("display.max_columns", None)
df

# T 轉置資料
# 注意轉置後 `head(15)` 代表選擇前 15 個欄位
df.T.head(15)




