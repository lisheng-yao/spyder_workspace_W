# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:28:52 2023

@author: w
"""

from pymodbus.client.sync import ModbusSerialClient as ModbusClient # pymodbus==2.5.3
import time



# 建立 Modbus RTU 連接
client = ModbusClient(method='rtu', 
                      port='COM4 ',          # 串行端口，根據您的設備調整
                      baudrate=19200,        # 波特率
                      # parity='N',           # 奇偶校驗，可能是 'N', 'E' 或 'O'
                      # stopbits=1,           # 停止位
                      # bytesize=8,           # 數據位
                      timeout=3)            # 超時設置，單位為秒

try:
    
   if client.connect():
    # 設定起始地址和要讀取的總寄存器數
    start_address = 512
    total_registers = 250  # 假設我們想讀取250個寄存器
    max_registers_per_read = 125  # 每次讀取限制
    address = start_address

    # 分批讀取
    while total_registers > 0:
        count = min(total_registers, max_registers_per_read)
        response = client.read_holding_registers(address, count, unit=1)
        
        if not response.isError():
            print(f"寄存器值從 {address}: ", response.registers)
        else:
            print(f"讀取錯誤從 {address}: ", response)
        
        # 更新地址和剩餘的寄存器數
        address += count
        total_registers -= count
    else:
        print("無法連接到 Modbus 伺服器")
finally:
    # 關閉連接
    client.close()