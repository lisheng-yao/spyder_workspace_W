# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:49:18 2023

@author: w
"""

from pymodbus.server.sync import StartSerialServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer
import random
import threading
import time
import serial

# 初始化数据库
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [0]*10000)
)

context = ModbusServerContext(slaves=store, single=True)

# 更新寄存器的值
def update_registers(context):
    while True:
        # 0 到 9 的每个寄存器
        for address in range(10):
            value = random.randint(0, 65535)  # 寄存器存储 0 到 65535 之间的随机值
            context[0].setValues(3, address, [value])
            print(f'Register {address} value: {value}')
        time.sleep(1)  # 每秒更新一次


if __name__ == "__main__":
# 创建线程更新函数
    thread = threading.Thread(target=update_registers, args=(context,))
    thread.start()
    
    # 配置串行端口参数
    serial_params = {
        'port': 'COM4',  # 修改为您的串行端口
        'baudrate': 9600,
        'bytesize': 8,
        'parity': 'N',
        'stopbits': 1,
        'xonxoff': 0,
        'rtscts': 0,
        'timeout': 1  # 可根据需要设置
    }
    
    # 运行同步线程，监听指定的串行端口
    StartSerialServer(context, framer=ModbusRtuFramer, **serial_params)
