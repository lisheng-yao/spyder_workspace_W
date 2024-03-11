import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


excel_path = r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\0305max.xlsx'
df = pd.read_excel(excel_path, engine='openpyxl')
print(df)



# df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # 確保Timestamp是日期時間格式
df_pivot = df.pivot(index='Timestamp', columns='RACK', values='Rack_Max_Cell_Temperature')
print(df_pivot)


plt.figure(figsize=(15, 7))  # 設置圖表大小

# 為每列畫出單獨的線條
for column in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[column], label=column)

# 格式化x軸上的時間戳記
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gcf().autofmt_xdate()  # 自動格式化日期顯示以便更佳

# 添加標題和標籤
# plt.title('Rack Temperatures Over Time')
# plt.xlabel('Timestamp')
# plt.ylabel('Rack_Max_Cell_Temperature (°C)')

# 添加圖例
plt.legend()

# plt.savefig(r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\container1_temperature_plot.png')
plt.show()

#%%

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 從Excel檔案載入數據
excel_path = r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\0305 (1).xlsx'
df = pd.read_excel(excel_path, engine='openpyxl')

# 假設Excel檔案具有如前所示的正確格式
# 我們將進行轉置表格，以在列上獲得唯一的機架，並在索引上獲得時間戳記
df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # 確保Timestamp是日期時間格式
df_pivot = df.pivot(index='Timestamp', columns='RACK', values='Rack_Temperature')

# 接下來讓我們繪製數據
plt.figure(figsize=(15, 7))  # 設置圖表大小

# 為每列畫出單獨的線條
for column in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[column], label=column)

# 格式化x軸上的時間戳記
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gcf().autofmt_xdate()  # 自動格式化日期顯示以便更佳

# 添加標題和標籤
plt.title('Rack Temperatures Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Rack_Temperature (°C)')

# 添加圖例
plt.legend()

# 顯示圖表
plt.show()


#%%


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


excel_path = r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\0305maxT(1).csv'
df = pd.read_excel(excel_path, engine='openpyxl')


# 我們將進行轉置表格，以在列上獲得唯一的機架，並在索引上獲得時間戳記
# df['Timestamp'] = pd.to_datetime(df['Timestamp'])  # 確保Timestamp是日期時間格式
df_pivot = df.pivot(index='Timestamp', columns='RACK', values='Rack_Max_Cell_Temperature')


plt.figure(figsize=(15, 7))  # 設置圖表大小

# 為每列畫出單獨的線條
for column in df_pivot.columns:
    plt.plot(df_pivot.index, df_pivot[column], label=column)

# 格式化x軸上的時間戳記
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gcf().autofmt_xdate()  # 自動格式化日期顯示以便更佳

# 添加標題和標籤
plt.title('Rack Temperatures Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Rack_Max_Cell_Temperature (°C)')

# 添加圖例
plt.legend()

plt.savefig(r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\container2_temperature_plot.png')
plt.show()

#%% 自寫版

import pandas as pd
import matplotlib.pyplot as plt



excel_path = r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\0305max.xlsx'
df = pd.read_excel(excel_path , engine='openpyxl')


df['Timestamp']
df_pivot = df.pivot(index='Timestamp' , columns='RACK' , values='Rack_Max_Cell_Temperature')

plt.figure(figsize=(15,7))


for column in df_pivot.columns:
    plt.plot(df_pivot.index , df_pivot[column] , label=column)


plt.gcf().autofmt_xdate()


plt.title('Rack Temperatures Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Rack_Temperature (°C)')
plt.legend()

plt.show()

#%%
import pandas as pd


csv_path = r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\0305maxT(1).csv'
df = pd.read_csv(csv_path)

df_pivot = df.pivot(index='Timestamp', columns='RACK', values='Rack_Max_Cell_Temperature')

# df_pivot_sorted = df_pivot.sort_index(axis=1)
columns_order = [f'rack{i}_Temperature' for i in range(1, 19)]
df_pivot_ordered = df_pivot[columns_order]

# 对DataFrame中的所有值先减200再除以10
df_pivot_ordered_transformed = (df_pivot_ordered - 200) / 10


df_pivot_ordered_transformed.to_csv(r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\Temperture_log_container1.csv')


#%%

import pandas as pd


csv_path = r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\0305maxT(6).csv'
df = pd.read_csv(csv_path)

df_pivot = df.pivot(index='Timestamp', columns='RACK', values='Rack_Max_Cell_Temperature')

# print(df_pivot)

columns_order = [f'rack {i}' for i in range(1, 19)]
df_pivot_ordered = df_pivot[columns_order]
df_pivot_ordered.columns = [f'rack{i}_Temperature' for i in range(1, 19)]
# print(df_pivot_ordered)

df_pivot_ordered_transformed = (df_pivot_ordered - 200) / 10

df_pivot_ordered_transformed.to_csv(r'C:\Users\w\Desktop\彰濱240304\溫升降溫\報告用\Temperture_log_container6.csv')


