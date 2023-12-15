#%%
import json
import requests

target_url = 'https://www.cwb.gov.tw/Data/js/TableData_36hr_County_C.js'

res = requests.get(target_url)

# 針對回應處理
res = res.text.split("'10018':")[1].split(",\n    '10004':")[0]

# 把字串轉換成json字串(單引號改成雙引號)
res = res.replace("\'", "\"")

# 使用json把長得像List的字串轉回List

res_json = json.loads(res)

print(res_json[0]['Wx'])

#%%

from datetime import date

# print(datetime.datetime.now())
print(date.today())




#%%
def hi(name):
    print(name,'安安你好')
    
input_name = input('請輸入使用者名稱')
hi(input_name)


#%%
a = range(2,100)                            # 產生 2～100 的串列
print(*a)

numbers = []                                # 優化
for i in range(1, 5):
    numbers.append(str(i))

result = ','.join(numbers)
print(result)

#%%
def natural():
    n = 1
    while True:
        yield n
        n += 1
        
obj = natural()

for i in range(10):
    print(next(obj))
    print(next(obj))
    
#%%

def count():                # 建立一個 count 函式
    a = []                    # 函式內有區域變數 a 是串列
    def avg(val):             # 建立內置函式 avg ( 閉包 )
        a.append(val)           # 將參數數值加入變數 a
        print(a)                # 印出 a
        return sum(a)/len(a)    # 回傳 a 串列所有數值的平均
    return avg                # 回傳 avg

test = count()
test(10)      # 將 10 存入 a
test(11)
test(12)

#%%
def a(msg):
    i = '!!!'         # ------------------------ 閉包開始
    def b():          # A 函式內定義了 B 函式
        print(msg + i)  # B 函式使用了 A 函式的變數
    return b          # 將 B 函式當作回傳值 ------- 閉包結束
s = a('hello')
s()                 # hello
        


