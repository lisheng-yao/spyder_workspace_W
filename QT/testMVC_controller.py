# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:46:24 2024

@author: w
"""
import testMVC
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow
import random



class TestMVC_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = testMVC.Ui_MainWindow()
        self.view.setupUi(self)
        self.view.retranslateUi(self)
        
        
        self.view.pushButton.clicked.connect(self.button_click)
        self.click_count = 0
        
    def button_click(self):
        self.click_count += 1
        self.view.pushButton.setText(str(self.click_count))
        
        
        # 生成隨機位置
        random_a = random.randint(60, 680)
        random_b = random.randint(30, 550)
        
        # 更新按钮位置
        self.view.pushButton.setGeometry(random_a, random_b, 111, 41)
        print( "x: " + str(random_a)  +   " y : " +str(random_b) )


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = TestMVC_controller()
    controller.show()
    sys.exit(app.exec_())
            