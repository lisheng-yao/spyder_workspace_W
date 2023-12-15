# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:46:13 2023

@author: w
"""


from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.WARNING) # 可設置為debug、CRITICAL


# 連接到 Modbus TCP 伺服器
client = ModbusClient('192.168.3.123', port=502, timeout=10)  # 超時設置為15秒
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


#%% wirite


try:
    if connection:
        values = [0000 ,1111 ,2222]
        response = client.write_registers(address=0, values=values, unit=1)
        if not response.isError():
            print("寫入成功")
        else:
            print("寫入錯誤: ", response)
finally:
    client.close()
    
    
#%% saveDataBase

import pymysql
import time

conn = pymysql.connect(
    host='localhost',    # 或者是您的 MySQL 服務器地址
    user='root',     # MySQL 用戶名
    password='0000', # MySQL 密碼
    db='test2',      # 您的數據庫名稱
    charset='utf8mb4'
)



try:
    # 嘗試連接
    connection = client.connect()
    if connection:
        for i in range(3):
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






















