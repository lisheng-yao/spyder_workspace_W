#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 11:27:41 2023

@author: yaolisheng
"""
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
Form.setWindowTitle('oxxo.studio')
Form.resize(300, 200)

btn1 = QtWidgets.QPushButton(Form)
btn1.setText('按鈕 1')
btn1.move(50,30)                 # 移動到 (50,30)

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('按鈕 2')
btn2.setGeometry(50,60,100,50)   # 移動到 (50,60)，大小 100x50

Form.show()
sys.exit(app.exec_())
                    
                    
                    