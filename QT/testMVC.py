# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testMVC.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1036, 723)
        MainWindow.setStyleSheet("QPushButton \n"
"{\n"
"\n"
"color : \'black\';\n"
"background-color:#FF7400;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"        color: :#FF7400;\n"
"        background: #FFFF00;\n"
"    }\n"
"\n"
"QLabel\n"
"{\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QMainWindow \n"
"\n"
"{\n"
"\n"
"background-color:#4F4A46;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget {\n"
"    background-color: #23211A; /* 表格的背景色 */\n"
"    color: white; /* 字體顏色 */\n"
"    gridline-color: white; /* 格線顏色 */\n"
"    font-size: 10px; /* 字體大小 */\n"
"}\n"
"\n"
"\n"
"\n"
"QTableWidget::header {\n"
"    font-size: 12px; /* 表頭字體大小 */\n"
"    background-color: #23211A; /* 表頭的背景色 */\n"
"    color: white; /* 表頭字體顏色 */\n"
"    border: none; /* 移除表頭的邊框 */\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    font-size: 12px; /* 行和列索引字體大小 */\n"
"    background-color: #23211A; /* 行和列索引的背景色 */\n"
"    color: white; /* 行和列索引字體顏色 */\n"
"    border: none; /* 移除行和列索引的邊框 */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(30, 60, 93, 28))
        self.upload.setObjectName("upload")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 70, 931, 16))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 371, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 58, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 400, 391, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 380, 161, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 670, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 20, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_upload_model = QtWidgets.QLabel(self.centralwidget)
        self.label_upload_model.setGeometry(QtCore.QRect(140, 30, 571, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_upload_model.sizePolicy().hasHeightForWidth())
        self.label_upload_model.setSizePolicy(sizePolicy)
        self.label_upload_model.setObjectName("label_upload_model")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 370, 441, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stackedWidget.setToolTip("")
        self.stackedWidget.setAccessibleDescription("")
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_KMeans = QtWidgets.QWidget()
        self.page_KMeans.setObjectName("page_KMeans")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_KMeans)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 371, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_n_clusters = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_n_clusters.setObjectName("label_n_clusters")
        self.verticalLayout.addWidget(self.label_n_clusters)
        self.spinBox_n_clusters = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_n_clusters.sizePolicy().hasHeightForWidth())
        self.spinBox_n_clusters.setSizePolicy(sizePolicy)
        self.spinBox_n_clusters.setObjectName("spinBox_n_clusters")
        self.verticalLayout.addWidget(self.spinBox_n_clusters)
        self.label_init = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_init.setObjectName("label_init")
        self.verticalLayout.addWidget(self.label_init)
        self.comboBox_init = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_init.sizePolicy().hasHeightForWidth())
        self.comboBox_init.setSizePolicy(sizePolicy)
        self.comboBox_init.setObjectName("comboBox_init")
        self.comboBox_init.addItem("")
        self.comboBox_init.addItem("")
        self.comboBox_init.addItem("")
        self.comboBox_init.addItem("")
        self.verticalLayout.addWidget(self.comboBox_init)
        self.label_max_iter = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_max_iter.setObjectName("label_max_iter")
        self.verticalLayout.addWidget(self.label_max_iter)
        self.spinBox_max_iter = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_max_iter.setObjectName("spinBox_max_iter")
        self.verticalLayout.addWidget(self.spinBox_max_iter)
        self.label_tol = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_tol.setObjectName("label_tol")
        self.verticalLayout.addWidget(self.label_tol)
        self.spinBox_tol = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_tol.setObjectName("spinBox_tol")
        self.verticalLayout.addWidget(self.spinBox_tol)
        self.label_metric = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_metric.setObjectName("label_metric")
        self.verticalLayout.addWidget(self.label_metric)
        self.comboBox_metric = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_metric.sizePolicy().hasHeightForWidth())
        self.comboBox_metric.setSizePolicy(sizePolicy)
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.verticalLayout.addWidget(self.comboBox_metric)
        self.label_random_seed = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_random_seed.setObjectName("label_random_seed")
        self.verticalLayout.addWidget(self.label_random_seed)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.spinBox)
        self.stackedWidget.addWidget(self.page_KMeans)
        self.page_DBSCAN = QtWidgets.QWidget()
        self.page_DBSCAN.setObjectName("page_DBSCAN")
        self.label_4 = QtWidgets.QLabel(self.page_DBSCAN)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 151, 41))
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.page_DBSCAN)
        self.page_NCC = QtWidgets.QWidget()
        self.page_NCC.setObjectName("page_NCC")
        self.label_5 = QtWidgets.QLabel(self.page_NCC)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 58, 15))
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_NCC)
        self.stackedWidget.raise_()
        self.pushButton.raise_()
        self.upload.raise_()
        self.label.raise_()
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_upload_model.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "按的到嗎"))
        self.upload.setText(_translate("MainWindow", "上傳CSV"))
        self.label.setText(_translate("MainWindow", "未上傳檔案"))
        self.label_2.setText(_translate("MainWindow", "資料預覽"))
        self.comboBox.setItemText(0, _translate("MainWindow", "KMeans"))
        self.comboBox.setItemText(1, _translate("MainWindow", "DBSCAN"))
        self.comboBox.setItemText(2, _translate("MainWindow", "NCC"))
        self.label_3.setText(_translate("MainWindow", "算法選擇 / 參數調整"))
        self.pushButton_2.setText(_translate("MainWindow", "匯出模型"))
        self.pushButton_3.setText(_translate("MainWindow", "匯入模型"))
        self.label_upload_model.setText(_translate("MainWindow", "未匯入模型 (選擇性)"))
        self.label_n_clusters.setText(_translate("MainWindow", "分群數 (n_clusters)"))
        self.label_init.setText(_translate("MainWindow", "初始中心點的選擇方法 (init)"))
        self.comboBox_init.setItemText(0, _translate("MainWindow", "k-means++ (預設)"))
        self.comboBox_init.setItemText(1, _translate("MainWindow", "random"))
        self.comboBox_init.setItemText(2, _translate("MainWindow", "uniform"))
        self.comboBox_init.setItemText(3, _translate("MainWindow", "zeros"))
        self.label_max_iter.setText(_translate("MainWindow", "最大迭代次數 (max_iter)"))
        self.label_tol.setText(_translate("MainWindow", "收斂閾值 (tol)"))
        self.label_metric.setText(_translate("MainWindow", "距離度量 (metric)"))
        self.comboBox_metric.setItemText(0, _translate("MainWindow", "euclidean (預設)"))
        self.comboBox_metric.setItemText(1, _translate("MainWindow", "manhattan"))
        self.comboBox_metric.setItemText(2, _translate("MainWindow", "cosine"))
        self.comboBox_metric.setItemText(3, _translate("MainWindow", "precomputed"))
        self.label_random_seed.setText(_translate("MainWindow", "隨機數種子 (random_seed)"))
        self.label_4.setText(_translate("MainWindow", "開發中"))
        self.label_5.setText(_translate("MainWindow", "開發中"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
