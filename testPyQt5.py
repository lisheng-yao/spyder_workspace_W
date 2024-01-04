# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:22:19 2024

@author: w
"""

from PyQt5 import QtWidgets, QtGui 
import sys

app = QtWidgets.QApplication(sys.argv)


Form = QtWidgets.QWidget()
Form.setWindowTitle('pyqt_法國我')
Form.resize(300,200)


label1 = QtWidgets.QLabel(Form)
label1.setText('安安')
label1.move(50,50)

label2 = QtWidgets.QLabel(Form)
label2.setText('安安2')
label2.move(50,100)

label = QtWidgets.QLabel(Form)
label.setGeometry(20, 20, 200, 150)
label.setWordWrap(True)

img = QtGui.QImage('123.jpg')            # 讀取圖片
img.move(100,100)
label.setPixmap(QtGui.QPixmap.fromImage(img))  # 加入圖片






Form.show()
sys.exit(app.exec_())



