#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:09:52 2023

@author: yaolisheng
"""

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.exceptions import ModbusException

# 配置 Modbus RTU 客户端
client = ModbusClient(method='rtu', port='/dev/ttyUSB0', baudrate=9600, timeout=3)

# 連接到串行端口
connection = client.connect()
if connection:
    try:
        # 從地址 1 的設備上讀取保持寄存器 40001-40002
        response = client.read_holding_registers(address=1, count=2, unit=1)
        if response.isError():
            print("讀取錯誤")
        else:
            print("寄存器值:", response.registers)
    except ModbusException as e:
        print(f"Modbus 異常: {e}")
    finally:
        # 關閉連接
        client.close()
else:
    print("連接失敗")
    
#%%

try:
    a = int(input('輸入 0～9：'))
    if a>10:
        assert False, '數字不在範圍內'
    print(a)
except AssertionError as msg:
    print(msg)
except :
    print('有錯誤喔～')
print('繼續執行')








