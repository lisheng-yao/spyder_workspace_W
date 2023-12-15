# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 17:08:39 2023

@author: w
"""

from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusSocketFramer
import random
import threading
import time

# 初始化数据库
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [0]*10000)
)

context = ModbusServerContext(slaves=store, single=True)

# 更新寄存器的值
def update_registers(context):
    while True:
        # 0 到 9 的每个寄存器
        # for address in range(10):
            value = random.randint(0, 65535)  # 寄存器存储 0 到 65535 之间的随机值
            context[1].setValues(3, 512, [value])
            print(f'Register 512 value: {value}')
            time.sleep(1)  # 每秒更新一次

# 创建线程更新函数
thread = threading.Thread(target=update_registers, args=(context,))
thread.start()

# 配置网络参数
tcp_params = {
    'address': ("192.168.3.200", 502)  # 监听所有地址，5020端口，您可以根据需要更改端口号
}

# 运行同步TCP服务器，监听指定的网络端口
StartTcpServer(context, framer=ModbusSocketFramer, **tcp_params)