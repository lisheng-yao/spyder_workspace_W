#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:45:30 2023

@author: yaolisheng
"""

from pymodbus.client.sync import ModbusSerialClient as ModbusClient # pymodbus==2.5.3
import time
# from pymodbus.client.serial import ModbusSerialClient as ModbusClient



# 建立 Modbus RTU 連接
client = ModbusClient(method='rtu', 
                      port='COM5',          # 串行端口，根據您的設備調整
                      baudrate=19200,        # 波特率
                      # parity='N',           # 奇偶校驗，可能是 'N', 'E' 或 'O'
                      # stopbits=1,           # 停止位
                      # bytesize=8,           # 數據位
                      timeout=3)            # 超時設置，單位為秒

try:
    # 嘗試連接
    connection = client.connect()
    
    if connection:
 
        # # while True:
        for i in range(3):
            # 讀取數據 (從地址0開始讀取 count個寄存器)
            response = client.read_holding_registers(address=512, count=512, unit=1)
            # response1 = client.read_holding_registers(address=0, count=120, unit=1)
            # response2 = client.read_holding_registers(address=632, count=120, unit=1)
        

            if not response.isError():
                print("寄存器的值512: ", response.registers)
                # print("寄存器的值632: ", response2.registers)
                # print("寄存器的值0: ", response1.registers)
            else:
                print("讀取錯誤: ", response)

            # 暫停一秒
            time.sleep(1)

    else:
        print("無法連接到 Modbus 伺服器")
finally:
    # 關閉連接
    client.close()