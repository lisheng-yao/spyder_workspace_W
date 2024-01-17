# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:46:24 2024

@author: w

"""
import testMVC
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QTableWidgetItem
import pandas as pd
import random



class TestMVC_controller(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = testMVC.Ui_MainWindow()
        self.view.setupUi(self)
        self.view.retranslateUi(self)
        self.view.pushButton.clicked.connect(self.button_click)
        self.view.upload.clicked.connect(self.upload_click)
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
        
        
        
    def upload_click(self):
        options = QFileDialog.Options() # 配置文件對話框物件
        file_path, _ = QFileDialog.getOpenFileName(None, "未上傳檔案", "", "CSV Files (*.csv);;All Files (*)", options=options)
    
        if file_path:
            print(f"已選擇檔案：{file_path}")
            self.view.label.setText(f"已選擇檔案：{file_path}")
            self.data_preview(file_path)
            print(self)
    
    
    def data_preview(self,file_path):
        data = pd.read_csv(file_path)
        # print(data)
        self.view.tableWidget.setColumnCount(len(data.columns))
        self.view.tableWidget.setRowCount(min(100, len(data)))  # 限制顯示前100筆資料
        # 設置表頭
        self.view.tableWidget.setHorizontalHeaderLabels(data.columns)
       
        for row in range(min(100,len(data))):
            for col in range(len(data.columns)):
                item = str(data.iloc[row,col])
                self.view.tableWidget.setItem(row,col,QTableWidgetItem(item))
        
    

    # def change_algorithm(self)





























if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = TestMVC_controller()
    controller.show()
    sys.exit(app.exec_())
            