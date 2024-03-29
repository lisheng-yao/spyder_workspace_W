# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_matplotlib_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import random

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(766, 575)
        MainWindow.setStyleSheet("QMainWindow\n"
"{\n"
"background-color: #5B5B5B;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color:    #FF8000;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        ## click event lambda　and normal
        # self.pushButton = QtWidgets.QPushButton(self.frame_2, clicked = lambda: self.plotOnCanvas())
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.clicked.connect(self.plotOnCanvas)
        
        
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        # create a horizontal latout
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        ## Canvas Here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        ## end of canvas
        ## Add Canvas
        self.horizontalLayout_4.addWidget(self.canvas)
        ## end of horizontal layout
        
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "給我印出來"))
        
    def plotOnCanvas(self):
        ##clear the canvas
        self.figure.clear()
        
        # 讀檔案
        data = pd.read_csv(r'C:\Users\w\Desktop\data\123.csv')

        # 每256行分割
        n = 256 
        grouped_data = [data[i:i + n] for i in range(0, data.shape[0], n)]



    
        for i, group in enumerate(grouped_data):
            X = group[['Voltage', 'Temperature']]
            kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
            kmeans.fit(X)
            
            # 使用 self.figure 和 self.canvas 來繪製圖形
            ax = self.figure.add_subplot(111)
            sc = ax.scatter(X['Voltage'], X['Temperature'], c=kmeans.labels_, cmap='viridis')
            ax.scatter(X['Voltage'], X['Temperature'], c=kmeans.labels_, cmap='viridis')
            ax.set_title(f'K-Means Clustering of Voltage and Temperature - Group {i+1}')
            ax.set_xlabel('Voltage')
            ax.set_ylabel('Temperature')
            ax.set_xlim(3280, 3375)
            ax.set_ylim(440, 520)
           
            # 添加顏色條
            cbar = self.figure.colorbar(sc, ax=ax, label='Cluster Label')

            # plt.figure(figsize=(10, 6),dpi=100)
            # plt.scatter(X['Voltage'], X['Temperature'], c=kmeans.labels_, cmap='viridis')
            # plt.title(f'K-Means Clustering of Voltage and Temperature - Group {i+1}')
            # plt.xlabel('Voltage')
            # plt.ylabel('Temperature')
            # plt.xlim(3280, 3375)
            # plt.ylim(440, 520)
    
            # plt.colorbar(label='Cluster Label')
        self.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
