# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:46:24 2024

@author: w

"""
import testMVC
from PyQt5 import  QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.datasets import load_iris



class TestMVC_controller(QMainWindow):
    def __init__(self):
        super().__init__() # 呼叫父類別(QMainWindow)的 __init__ 方法
        self.view = testMVC.Ui_MainWindow()
        self.view.setupUi(self)
        self.view.retranslateUi(self)
        self.view.pushButton.clicked.connect(self.button_click)
        self.view.upload.clicked.connect(self.upload_click)
        self.view.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.set_logo()
        self.view.pushButton_plot.clicked.connect(self.plot_click)
        self.plot_layout = QtWidgets.QVBoxLayout(self.view.graphicsView_plot)
        self.click_count = 0
        
    #    
    def button_click(self):
        self.click_count += 1
        self.view.pushButton.setText(str(self.click_count))
        
        # 生成隨機位置
        random_a = random.randint(60, 680)
        random_b = random.randint(30, 550)
        # 更新按钮位置
        self.view.pushButton.setGeometry(random_a, random_b, 111, 41)
        print( "x: " + str(random_a)  +   " y : " +str(random_b) )
        
        
    #    
    def upload_click(self):
        options = QFileDialog.Options() # 配置文件對話框物件
        file_path, _ = QFileDialog.getOpenFileName(None, "未上傳檔案", "", "CSV Files (*.csv);;All Files (*)", options=options)
    
        if file_path:
            print(f"已選擇檔案：{file_path}")
            self.view.label.setText(f"已選擇檔案：{file_path}")
            self.data_preview(file_path)
    
    #
    def data_preview(self,file_path):
        data = pd.read_csv(file_path)
        # print(data)
        self.view.tableWidget.setColumnCount(len(data.columns))
        self.view.tableWidget.setRowCount(min(100, len(data)))  # 限制顯示前100筆資料
        # 設置表頭
        self.view.tableWidget.setHorizontalHeaderLabels(data.columns)
        # 更改左上角背景色
        self.view.tableWidget.setStyleSheet("QTableCornerButton::section { background-color: #23211A; border: 1px solid white; }")
        # 更改索引列格線顏色
        self.view.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section { background-color: #23211A; border: 1px solid white; }")
        # 更改水平表頭格線顏色
        self.view.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section { background-color: #23211A; border: 1px solid white; }")
        # 更改垂直滾動條的顏色
        self.view.tableWidget.verticalScrollBar().setStyleSheet("QScrollBar:vertical {  background: white; width: 10px; } QScrollBar::handle:vertical { background: #33363D; }")
        # 更改水平滾動條的顏色
        self.view.tableWidget.horizontalScrollBar().setStyleSheet("QScrollBar:horizontal { background: white; height: 10px; } QScrollBar::handle:horizontal { background: #33363D; }")
       
        for row in range(min(100,len(data))):
            for col in range(len(data.columns)):
                item = str(data.iloc[row,col])
                self.view.tableWidget.setItem(row,col,QTableWidgetItem(item))
        

    # 
    def on_combobox_changed(self, index):
        self.view.stackedWidget.setCurrentIndex(index)
    
        
    #    
    def set_logo(self):
        print('logo已設定')
        scene = QtWidgets.QGraphicsScene()
        img = QtGui.QPixmap(r'C:\Users\w\spyder_workspace_W\QT\logo\logo_normal.png')
        img = img.scaled(400,80)
        scene.addPixmap(img)
        self.view.graphicsView_logo.setScene(scene)
        
        print('準備起飛')
        scene2 = QtWidgets.QGraphicsScene()
        img2 = QtGui.QPixmap(r'C:\Users\w\spyder_workspace_W\QT\logo\bird.jpg')
        img2 = img2.scaled(360,480)
        scene2.addPixmap(img2)
        self.view.graphicsView_bird.setScene(scene2)

    # 從這裡開始
    def plot_click(self):
        

        
        RawData = load_iris()
        df = pd.DataFrame(RawData['data'],columns= RawData['feature_names'])
        
        lineEdit_n_clusters = self.view.lineEdit_n_clusters.text()
        comboBox_init = self.view.comboBox_init.currentText()
        spinBox_max_iter = self.view.spinBox_max_iter.value()
        spinBox_tol = self.view.spinBox_tol.value()
        comboBox_metric = self.view.comboBox_metric.currentText()
        spinBox_random_seed = self.view.spinBox_random_seed.value()
        
        
        try:
            n_clusters = int(lineEdit_n_clusters)
        except ValueError:
            print("請輸入正整數")
            return

        model = KMeans(n_clusters=n_clusters,
                   init=comboBox_init,
                   n_init='auto',
                   max_iter=spinBox_max_iter,
                   tol=float(1e-4),
                   algorithm=comboBox_metric,
                   random_state=spinBox_random_seed)
        
        model.fit(df)
        
        fig ,ax = plt.subplots()
        ax.scatter(df['petal length (cm)'],df['petal width (cm)'], c = model.labels_) #根據花瓣的長度、寬度，來畫出之間關係。c=model.labels_:代表資料點的顏色，由模型分類出來的結果，來進行分類和定義。 
        ax.set_xlabel('petal length')
        ax.set_ylabel('petal width')
        # ax.show()
        
        self.plot_to_graphics_view(fig)
    
    #
    def plot_to_graphics_view(self, figure):
        # 清除原本的圖
        layout = self.view.graphicsView_plot.layout() # 取得佈局 (layout)物件
    
        if layout is not None:
            QtWidgets.QApplication.processEvents()  # 暫停一下，讓事件處理發生
            while layout.count(): # 檢查是否有部件
                item = layout.takeAt(0) # 將部件設定為
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()
                    
            canvas = FigureCanvas(figure)
            canvas.setParent(self.view.graphicsView_plot)
            self.plot_layout.addWidget(canvas)
        







if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = TestMVC_controller()
    controller.show()
    sys.exit(app.exec_())
            