# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:46:24 2024

@author: w

"""
import testMVC
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QTableWidgetItem, QStackedWidget, QComboBox
import pandas as pd
import random



class TestMVC_controller(QMainWindow):
    def __init__(self):
        super().__init__() # 呼叫父類別(QMainWindow)的 __init__ 方法
        self.view = testMVC.Ui_MainWindow()
        self.view.setupUi(self)
        self.view.retranslateUi(self)
        self.view.pushButton.clicked.connect(self.button_click)
        self.view.upload.clicked.connect(self.upload_click)
        self.view.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
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
        
    # 
    def on_combobox_changed(self, index):
        self.view.stackedWidget.setCurrentIndex(index)



# 1.你有反應是1月底的沒辦法做完(某個東西)，DDL阻塞問題5分鐘能解決，卻重構了多次，gpt使用缺點
# 2.我目前工作應著重在軟體工程師學習，並協助你完成任務，而不是只有ai
# 3.你有提到台塑對不起我或你之類?但應該先做出東西再來談
# 4.跟你討論的工作、學習方向，須更考慮到能為團隊或主管做什麼
# 5.規劃的ai功能不應該是我們這樣決定的，應該要以市場需求為出發點
# 6.要更理解產業內容才可以找到市場與需求


# 寒號鳥相反，積極主動、負責任、勤奮努力
# 我一直以來都有反應，希望能為團隊帶來助111益並從中學習到技能
# 會選擇在台北一個月領不到3萬多，寧願生活品質，想得到的絕對不只是福利
# 1.討論需要建立可視化紀錄，讓主管更新掌握
# 2.



# 在跟W討論時，沒有著重在這些
# 作為RD我的資質不好，但我邏輯尚可




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = TestMVC_controller()
    controller.show()
    sys.exit(app.exec_())
            