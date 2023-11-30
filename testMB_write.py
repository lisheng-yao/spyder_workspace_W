#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:25:01 2023

@author: yaolisheng
"""

from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method='rtu', 
                      port='/dev/tty.usbserial-140',  # 串行端口，根據您的設備調整
                      baudrate=9600,        # 波特率
                      parity='N',           # 奇偶校驗，可能是 'N', 'E' 或 'O'
                      stopbits=1,           # 停止位
                      bytesize=8,           # 數據位
                      timeout=1)            # 超時設置，單位為秒

try:
    client.connect()
    address = 10          # 起始寄存器地址
    values = [1111, 2222, 3333, 4444]  # 想寫入的一系列值
    response = client.write_registers(address, values, unit=1)
    if not response.isError():
        print("寫入成功")
    else:
        print("寫入錯誤: ", response)
finally:
    client.close()