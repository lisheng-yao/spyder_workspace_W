#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:39:20 2023

@author: yaolisheng
"""

import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pymysql

# 连接到 MySQL 数据库
def create_connection():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='0000',
                           db='test2',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

# 查询数据库并返回结果
def query_data():
    conn = create_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM table1")
            return cursor.fetchall()  # 返回所有记录
    finally:
        conn.close()

# 加载 UI 文件
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('test_qt_model.ui', self)  # 加载设计好的UI布局
        self.pushButton.clicked.connect(self.display_data)  # 将按钮点击事件绑定到 display_data 函数

    # 显示数据到表格中
    def display_data(self):
        data = query_data()  # 获取数据
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['id', 'name', 'price'])

        for row_data in data:
            row = []
            for item in row_data.values():
                cell = QStandardItem(str(item))
                row.append(cell)
            model.appendRow(row)

        self.tableView.setModel(model)

# 程序入口
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
