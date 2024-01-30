# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 08:34:28 2023

@author: w
"""

from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.WARNING) # 可設置為debug、CRITICAL


# 連接到 Modbus TCP 伺服器
client = ModbusClient('192.168.3.222', port=502, timeout=10)  # 超時設置為10秒
connection = client.connect()



if connection:
    # 讀取保持寄存器
    response = client.read_holding_registers(address=512, count=10, unit=1)
    # response = client.read_holding_registers(0, )
    
    if not response.isError():
        print(response.registers)
    else:
        log.error(response)
else:
    log.error("無法連接到 Modbus 伺服器")

client.close()