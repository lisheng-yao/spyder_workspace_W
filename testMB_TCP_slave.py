# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:47:18 2023

@author: w
"""

from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import random
import threading
import time

# 初始化數據庫
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [0]*10)
)

context = ModbusServerContext(slaves=store, single=True)

# 更新寄存器的值
def update_registers(context):
    while True:
        #  0 到 9 的每個寄存器
        for address in range(10):
            value = random.randint(0, 65535)  # 寄存器存儲 0 到 65535 之間的隨機值
            context[0].setValues(3, address, [value])
            print(value)
        time.sleep(1)  # 每秒更新一次

# 創執行續更新函数
thread = threading.Thread(target=update_registers, args=(context,))
thread.start()

# 運行同步執行續，監聽本機 502 端口
StartTcpServer(context, address=("192.168.1.200", 502))