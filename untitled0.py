# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:54:02 2024

@author: w
"""

import requests
import json
import pandas as pd
import requests
import jwt



#%%
url = 'http://61.222.220.101:5486/api/ancillary_services_bp/home_page_annual_accillary'


#%%
url = 'http://61.222.220.101:5486/api/users_bp'
# url = 'http://61.222.220.101:5486/api/users_bp/get_info'

#%%
url = 'http://61.222.220.101:5486/api/realtime_value_bp/value/0/99'


#%%
url = 'http://61.222.220.101:5486/api/historical_bp/fp300/'


#%%
url = 'http://61.222.220.101:5486/api/site_info_bp/overview'


#%%
url = 'http://61.222.220.101:5486/api/dropdown_item_bp/ess_bms'


#%%
url = 'http://61.222.220.101:5486/api/event_table_bp/top5/'


#%%
url = 'http://61.222.220.101:5486/api/roles_bp/roles/View1'


#%%
response = requests.get(url)
json_data = json.loads(response.text)
print(response.text)


#%%
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjIxMTkwMiwianRpIjoiYmNmNzQwM2EtOTc5My00NGFmLThmZjctYjU3MTNlOTBkZmI2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InZpZXdlcjEiLCJuYmYiOjE2ODYyMTE5MDIsImV4cCI6MTY4NjM4NDcwMn0.pTxWwZm3Bbv_Pde__v6rv8Py5J6St4tJe8yLwOqfeNk'
    # 'username': 'test_000_'
}

response = requests.get(url, headers=headers)
json_data = json.loads(response.text)
print(response.text)





#%%


# 定義要簽名的資料（payload）
payload = {
    'data': 'example'
}


# 定義密鑰（secret key）
secret_key = 'formosa124'

# 使用jwt.encode函式計算簽名
token = jwt.encode(payload, secret_key, algorithm='HS256')

# 打印簽名後的JWT
print(token)

#%%

decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    
# 打印解碼後的資料
print(decoded_payload)


#%%

x = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NjIxMTkwMiwianRpIjoiYmNmNzQwM2EtOTc5My00NGFmLThmZjctYjU3MTNlOTBkZmI2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InZpZXdlcjEiLCJuYmYiOjE2ODYyMTE5MDIsImV4cCI6MTY4NjM4NDcwMn0.pTxWwZm3Bbv_Pde__v6rv8Py5J6St4tJe8yLwOqfeNk'

secret_key = 'viewer1'

decoded_payload = jwt.decode(x, secret_key, algorithms=['HS256'])
    
# 打印解碼後的資料
print(decoded_payload)