#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 08:48:27 2023

@author: yaolisheng
"""

from PyQt5 import QtWidgets, QtCore
import sys
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# MainWindow.setObjectName("MainWindow")
# MainWindow.setWindowTitle("oxxo.studio")
# MainWindow.resize(300, 200)

# pushButton = QtWidgets.QPushButton(MainWindow)
# pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32))
# pushButton.setObjectName("pushButton")
# pushButton.setText("PushButton")

# MainWindow.show()
# sys.exit(app.exec_())



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')
        self.resize(300, 200)
        self.ui()

    def ui(self):
        pushButton = QtWidgets.QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32))
        pushButton.setObjectName("pushButton")
        pushButton.setText("PushButton")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWidget()
    MainWindow.show()
    sys.exit(app.exec_())