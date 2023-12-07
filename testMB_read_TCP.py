# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:46:13 2023

@author: w
"""


from pymodbus.client.sync import ModbusTcpClient as ModbusClient


# 連接到 Modbus TCP 伺服器
client = ModbusClient('192.168.1.123', port=502)
client.connect()


# 讀取保持寄存器
response = client.read_holding_registers(1, 10)
# response = client.read_holding_registers(1, 10)
if response.isError():
    print("讀取錯誤")
else:
    print(response.registers)

# 關閉連接
client.close()