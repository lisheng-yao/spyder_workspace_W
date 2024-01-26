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
import numpy as np
import random
import os



class TestMVC_controller(QMainWindow):
    def __init__(self):
        super().__init__() # 呼叫父類別(QMainWindow)的 __init__ 方法
        self.view = testMVC.Ui_MainWindow()
        self.view.setupUi(self)
        self.view.retranslateUi(self)
        self.view.pushButton.clicked.connect(self.button_click)
        self.view.upload.clicked.connect(self.upload_click)
        self.view.comboBox.currentIndexChanged.connect(self.on_combobox_changed)
        self.view.pushButton_next.clicked.connect(self.show_next_plot)
        self.view.pushButton_last.clicked.connect(self.show_last_plot)
        
        
        
        self.set_logo()
        self.view.pushButton_plot.clicked.connect(self.plot_click)
        self.plot_layout = QtWidgets.QVBoxLayout(self.view.graphicsView_plot)
        self.click_count = 0
        self.file_path = None
        
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
            self.file_path = file_path
    # 
    def data_preview(self,file_path):
        data = pd.read_csv(file_path , encoding = 'utf-8')
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
        
    
        
    # 圖片處理
    # def set_logo(self):
    #     scene = QtWidgets.QGraphicsScene()
        
    #     # 取得執行路徑
    #     script_dir = os.path.dirname(os.path.realpath(__file__))
        
    #     relative_path_logo = os.path.join("logo", "logo.png")
    #     img_path = os.path.join(script_dir, relative_path_logo)
           
    #     img = QtGui.QPixmap(img_path)
    #     img = img.scaled(400,80)
    #     scene.addPixmap(img)
    #     self.view.graphicsView_logo.setScene(scene)
    #     print('logo已設定')
        
        
        
    #     scene2 = QtWidgets.QGraphicsScene()
    #     relative_path_bird = os.path.join("logo" , "bird.jpg")
    #     img_path_bird = os.path.join(script_dir, relative_path_bird)
        
    #     img2 = QtGui.QPixmap(img_path_bird)
    #     img2 = img2.scaled(360,480)
    #     scene2.addPixmap(img2)
    #     self.view.graphicsView_bird.setScene(scene2)
    #     print('準備起飛')
        
        
        
    # 圖片處理2
    def set_logo(self):
        self.load_and_set_image("logo/logo.png", self.view.graphicsView_logo, (400, 80), 'logo已設定')
        self.load_and_set_image("logo/bird.jpg", self.view.graphicsView_bird, (360, 480), '準備起飛')

    def load_and_set_image(self, relative_path, graphics_view, size, log_message):
        scene = QtWidgets.QGraphicsScene()
        
        # 取得執行路徑 dirname取得目錄
        script_dir = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(script_dir, relative_path)
        img = QtGui.QPixmap(img_path)
        
        # 统一缩放
        img = img.scaled(*size)
        
        scene.addPixmap(img)
        graphics_view.setScene(scene)
        print(log_message)
        
        
    
    # kmeans處理
    def plot_click(self):
        
        file_path = self.file_path
        data = pd.read_csv(file_path)
        # print(f'安安測試路徑 {file_path}')
        
        # kmeans GUI input
        lineEdit_n_clusters = self.view.lineEdit_n_clusters.text()
        comboBox_init = self.view.comboBox_init.currentText()
        spinBox_max_iter = self.view.spinBox_max_iter.value()
        spinBox_tol = self.view.spinBox_tol.value()
        comboBox_metric = self.view.comboBox_metric.currentText()
        spinBox_random_seed = self.view.spinBox_random_seed.value()
        
        # 分群條件 GUI input
        data_group = self.view.lineEdit_data_group.text()
        threshold_input = self.view.lineEdit_threshold.text()
        
        
        if data_group and data_group.isdigit():
            grouped_data = [data[i:i + int(data_group)] for i in range(0, data.shape[0], int(data_group))]
        else:
            print("請輸入有效分群")
            return
        
        
        
        try:
            n_clusters = int(lineEdit_n_clusters)
        except ValueError:
            print("請輸入正整數")
            return

        # 用於存儲所有生成的 figures
        list_of_figures = []    
    
        for i, group in enumerate(grouped_data):
            X = group[['Voltage', 'Temperature']]
            # print(X)
            
            kmeans = KMeans(n_clusters=n_clusters,
                       init=comboBox_init,
                       n_init='auto',
                       max_iter=spinBox_max_iter,
                       tol=float(1e-4),
                       algorithm=comboBox_metric,
                       random_state=spinBox_random_seed)
        
            kmeans.fit(X)
            
            
            # 計算每個點到所屬中心的距離
            distances = kmeans.transform(X)
            # 取得每個點到其所屬群集中心的最小距離
            min_distances = np.min(distances, axis=1)
            # 設定閾值，超過閾值的點視為離群值
            outliers = X[min_distances > int(threshold_input)]
            print(outliers)
            
            

            fig ,ax = plt.subplots()
            ax.scatter(X['Voltage'], X['Temperature'], c=kmeans.labels_, cmap='viridis', edgecolor='k')
            ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
            ax.scatter(outliers['Voltage'], outliers['Temperature'], c='orange', marker='o', s=100, label='Outliers')
            
            for index, row in outliers.iterrows():
                plt.annotate(index, (row['Voltage'], row['Temperature']), textcoords="offset points", xytext=(0,5), ha='center', fontsize=7)
            

            plt.title(f'K-means Clustering with Outliers - Group {i + 1}')
            plt.xlabel('Voltage')
            plt.ylabel('Temperature')
            plt.xlim(3280, 3360)
            plt.ylim(440, 510)
            plt.legend()
            
            
            plt.show()
            
            list_of_figures.append(fig)    
        
            self.plot_to_graphics_view(fig)
        
           
        self.update_stacked_widget(list_of_figures) ######################
        
        
    
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
        


    # 動態添加一個新的QWidget到QStackedWidget
    def add_page_to_stacked_widget(self, figure):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(widget)
        layout.addWidget(FigureCanvas(figure))
        self.view.stackedWidget_layout.addWidget(widget)
    
    
    # 新繪圖之前，清除所有已經存在stackedWidget的QWidget
    def clear_stacked_widget(self):
        # widget = None  # 在函數開始時設置預設值
        if self.view.stackedWidget_layout.count() > 0:
            for i in reversed(range(self.view.stackedWidget.count())):
                widget = self.view.stackedWidget.widget(i)
                self.view.stackedWidget.removeWidget(widget)
                widget.deleteLater()
            
            # for i in range(self.view.stackedWidget_layout.count()):
            #     widget = self.view.stackedWidget_layout.widget(i)
                
            #     print(f'開始清除 {i}')
            #     # if widget is not None:
            #     widget.setParent(None)
            #     widget.deleteLater()
            #     self.view.stackedWidget_layout.removeWidget(widget) 
        pass    

    #
    def update_stacked_widget(self, list_of_figures):
        self.clear_stacked_widget() 
        for figure in list_of_figures:
            self.add_page_to_stacked_widget(figure)
    
        self.view.stackedWidget_layout.setCurrentIndex(0)  # 顯示第一張圖片



    # 上一張
    def show_last_plot(self):
        current_index = self.view.stackedWidget_layout.currentIndex()
        new_index = (current_index - 1) % self.view.stackedWidget_layout.count()
        self.view.stackedWidget_layout.setCurrentIndex(new_index)


    # 下一張
    def show_next_plot(self):
        current_index = self.view.stackedWidget_layout.currentIndex()
        new_index = (current_index + 1) % self.view.stackedWidget_layout.count()
        print(f'current_index = {current_index} , new_index = {new_index}')
        self.view.stackedWidget_layout.setCurrentIndex(new_index)









if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = TestMVC_controller()
    controller.show()
    sys.exit(app.exec_())
            