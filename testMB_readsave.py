#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:45:30 2023

@author: yaolisheng
"""

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import pymysql
import time
# from pymodbus.client.serial import ModbusSerialClient as ModbusClient



# 建立 Modbus RTU 連接
client = ModbusClient(method='rtu', 
                      port='/dev/tty.usbserial-140',  # 串行端口，根據您的設備調整
                      baudrate=9600,        # 波特率
                      parity='N',           # 奇偶校驗，可能是 'N', 'E' 或 'O'
                      stopbits=1,           # 停止位
                      bytesize=8,           # 數據位
                      timeout=1)            # 超時設置，單位為秒

conn = pymysql.connect(
    host='localhost',    # 或者是您的 MySQL 服務器地址
    user='root',     # MySQL 用戶名
    password='0000', # MySQL 密碼
    db='test2',      # 您的數據庫名稱
    charset='utf8mb4'
)


# def create_connection():
#     return pymysql.connect(host='localhost',
#                            user='root',
#                            password='0000',
#                            db='test2',
#                            charset='utf8mb4',
#                            cursorclass=pymysql.cursors.DictCursor)


try:
    # 嘗試連接
    connection = client.connect()
    if connection:
        for i in range(60):
            # 讀取數據 (從地址0開始讀取10個寄存器)
            response = client.read_holding_registers(address=0, count=10, unit=1)

            if not response.isError():
                print("寄存器的值: ", response.registers)

                # 將數據寫入 MySQL
                sql = "INSERT INTO tableMB_save (cell0, cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = tuple(response.registers)
                
                # 將數據寫入 MySQL
                with conn.cursor() as cursor:
                    cursor.execute(sql, val)
                conn.commit()

                print("數據寫入成功")

            else:
                print("讀取錯誤: ", response)

            # 暫停一秒
            time.sleep(1)

    else:
        print("無法連接到 Modbus 伺服器")
finally:
    # 關閉連接
    client.close()
    conn.close()