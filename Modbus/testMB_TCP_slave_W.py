# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:55:58 2023

@author: w
"""

from pymodbus.server.sync import StartTcpServer
from pymodbus.server.sync import StartSerialServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from random import randint
import time
import threading
import serial

def run_slave():
    

    global context1
    store1 = {
        1:ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*10000),
            co=ModbusSequentialDataBlock(0, [0]*10000),
            hr=ModbusSequentialDataBlock(0, [0]*10000),
            ir=ModbusSequentialDataBlock(0, [0]*10000)),
        2:ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*10000),
            co=ModbusSequentialDataBlock(0, [0]*10000),
            hr=ModbusSequentialDataBlock(0, [0]*10000),
            ir=ModbusSequentialDataBlock(0, [0]*10000)),
        3:ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*10000),
            co=ModbusSequentialDataBlock(0, [0]*10000),
            hr=ModbusSequentialDataBlock(0, [0]*10000),
            ir=ModbusSequentialDataBlock(0, [0]*10000)), 
        4:ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*10000),
            co=ModbusSequentialDataBlock(0, [0]*10000),
            hr=ModbusSequentialDataBlock(0, [0]*10000),
            ir=ModbusSequentialDataBlock(0, [0]*10000)), 
        5:ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*10000),
            co=ModbusSequentialDataBlock(0, [0]*10000),
            hr=ModbusSequentialDataBlock(0, [0]*10000),
            ir=ModbusSequentialDataBlock(0, [0]*10000)), 
        6:ModbusSlaveContext(
            di=ModbusSequentialDataBlock(0, [0]*10000),
            co=ModbusSequentialDataBlock(0, [0]*10000),
            hr=ModbusSequentialDataBlock(0, [0]*10000),
            ir=ModbusSequentialDataBlock(0, [0]*10000)), 
        
        }
    context1 = ModbusServerContext(slaves=store1, single=False)
    # StartTcpServer(context1, address=('192.168.3.200', 502))
    StartTcpServer(context1, address=(ip, port))
    
    

    
    

if __name__ == "__main__":
    
    ip = input("Enter IP address: ")
    port = int(input("Enter port: "))  # 將埠號轉換為整數
    
    thread = threading.Thread(target=run_slave)
    thread.start()
    
    time.sleep(1)
    while True:
        # context1[0].setValues(3, 512, [1000]*1000)
        context1[1].setValues(4, 512, [randint(3200, 3400) for _ in range(1000)])
        context1[2].setValues(4, 512, [randint(3200, 3400) for _ in range(1000)])
        context1[3].setValues(4, 512, [randint(3200, 3400) for _ in range(1000)])
        context1[4].setValues(4, 512, [randint(3200, 3400) for _ in range(1000)])
        context1[5].setValues(4, 512, [randint(3200, 3400) for _ in range(1000)])
        context1[6].setValues(4, 512, [randint(3200, 3400) for _ in range(1000)])
        # context2[0].setValues(3, 512, [2000]*1000)
        # # context3[0].setValues(3, 512, [randint(3200, 3400) for _ in range(1000)])
        # context3[0].setValues(3, 512, [3000]*1000)
        # time.sleep(1)
                
        print(context1[1].getValues(4, 512, count=10))
        print(context1[2].getValues(4, 512, count=10))
        print(context1[3].getValues(4, 512, count=10))
        print(context1[4].getValues(4, 512, count=10))
        print(context1[5].getValues(4, 512, count=10))
        print(context1[6].getValues(4, 512, count=10))
        time.sleep(0.2)
        # print(context2[0].getValues(3, 512, count=10))
        # print(context3[0].getValues(3, 512, count=10))