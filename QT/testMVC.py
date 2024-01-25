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
        MainWindow.resize(2125, 895)
        MainWindow.setToolTip("")
        MainWindow.setStyleSheet("QPushButton \n"
"{\n"
"color : \'black\';\n"
"background-color:#FF7400;\n"
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
"}\n"
"\n"
"\n"
"QMainWindow \n"
"\n"
"{\n"
"background-color:#4F4A46;\n"
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
"QFileDialog{\n"
"\n"
"    background-color: #23211A;\n"
"\n"
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
"}\n"
"\n"
"#graphicsView_logo\n"
"\n"
"{\n"
"    background-color:#4F4A46;\n"
"    border: none; /* 移除表頭的邊框 */\n"
"}\n"
"\n"
"#graphicsView_plot\n"
"{\n"
"\n"
"background-color: #23211A; \n"
"\n"
"}\n"
"\n"
"#graphicsView_DBSCAN ,  #graphicsView_NCC , #stackedWidget_layout, #graphicsView_bird\n"
"\n"
"{\n"
"\n"
"background-color: #23211A;\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1290, 80, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(30, 60, 93, 28))
        self.upload.setObjectName("upload")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 70, 931, 16))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 391, 241))
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
        self.stackedWidget.setGeometry(QtCore.QRect(10, 370, 441, 521))
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
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 371, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_n_clusters = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_n_clusters.setObjectName("label_n_clusters")
        self.verticalLayout.addWidget(self.label_n_clusters)
        self.lineEdit_n_clusters = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_n_clusters.setObjectName("lineEdit_n_clusters")
        self.verticalLayout.addWidget(self.lineEdit_n_clusters)
        self.label_init = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_init.setObjectName("label_init")
        self.verticalLayout.addWidget(self.label_init)
        self.comboBox_init = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
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
        self.spinBox_max_iter.setMinimum(1)
        self.spinBox_max_iter.setMaximum(99999)
        self.spinBox_max_iter.setProperty("value", 300)
        self.spinBox_max_iter.setObjectName("spinBox_max_iter")
        self.verticalLayout.addWidget(self.spinBox_max_iter)
        self.label_tol = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_tol.setObjectName("label_tol")
        self.verticalLayout.addWidget(self.label_tol)
        self.spinBox_tol = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_tol.sizePolicy().hasHeightForWidth())
        self.spinBox_tol.setSizePolicy(sizePolicy)
        self.spinBox_tol.setObjectName("spinBox_tol")
        self.verticalLayout.addWidget(self.spinBox_tol)
        self.label_metric = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_metric.setObjectName("label_metric")
        self.verticalLayout.addWidget(self.label_metric)
        self.comboBox_metric = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_metric.sizePolicy().hasHeightForWidth())
        self.comboBox_metric.setSizePolicy(sizePolicy)
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.comboBox_metric.addItem("")
        self.comboBox_metric.addItem("")
        self.verticalLayout.addWidget(self.comboBox_metric)
        self.label_random_seed = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_random_seed.setObjectName("label_random_seed")
        self.verticalLayout.addWidget(self.label_random_seed)
        self.spinBox_random_seed = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_random_seed.sizePolicy().hasHeightForWidth())
        self.spinBox_random_seed.setSizePolicy(sizePolicy)
        self.spinBox_random_seed.setMaximum(999999)
        self.spinBox_random_seed.setProperty("value", 100)
        self.spinBox_random_seed.setObjectName("spinBox_random_seed")
        self.verticalLayout.addWidget(self.spinBox_random_seed)
        self.label_data_group = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_data_group.setObjectName("label_data_group")
        self.verticalLayout.addWidget(self.label_data_group)
        self.lineEdit_data_group = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_data_group.setObjectName("lineEdit_data_group")
        self.verticalLayout.addWidget(self.lineEdit_data_group)
        self.label_threshold = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_threshold.setObjectName("label_threshold")
        self.verticalLayout.addWidget(self.label_threshold)
        self.lineEdit_threshold = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_threshold.setObjectName("lineEdit_threshold")
        self.verticalLayout.addWidget(self.lineEdit_threshold)
        self.pushButton_plot = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.verticalLayout.addWidget(self.pushButton_plot)
        self.stackedWidget.addWidget(self.page_KMeans)
        self.page_DBSCAN = QtWidgets.QWidget()
        self.page_DBSCAN.setObjectName("page_DBSCAN")
        self.label_4 = QtWidgets.QLabel(self.page_DBSCAN)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 151, 41))
        self.label_4.setObjectName("label_4")
        self.graphicsView_DBSCAN = QtWidgets.QGraphicsView(self.page_DBSCAN)
        self.graphicsView_DBSCAN.setGeometry(QtCore.QRect(90, 110, 256, 192))
        self.graphicsView_DBSCAN.setObjectName("graphicsView_DBSCAN")
        self.stackedWidget.addWidget(self.page_DBSCAN)
        self.page_NCC = QtWidgets.QWidget()
        self.page_NCC.setObjectName("page_NCC")
        self.label_5 = QtWidgets.QLabel(self.page_NCC)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 141, 16))
        self.label_5.setObjectName("label_5")
        self.graphicsView_NCC = QtWidgets.QGraphicsView(self.page_NCC)
        self.graphicsView_NCC.setGeometry(QtCore.QRect(90, 100, 256, 192))
        self.graphicsView_NCC.setObjectName("graphicsView_NCC")
        self.stackedWidget.addWidget(self.page_NCC)
        self.graphicsView_logo = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_logo.setGeometry(QtCore.QRect(550, 40, 411, 101))
        self.graphicsView_logo.setObjectName("graphicsView_logo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 180, 601, 641))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView_plot = QtWidgets.QGraphicsView(self.layoutWidget)
        self.graphicsView_plot.setObjectName("graphicsView_plot")
        self.verticalLayout_2.addWidget(self.graphicsView_plot)
        self.pushButton_model_export = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_model_export.setObjectName("pushButton_model_export")
        self.verticalLayout_2.addWidget(self.pushButton_model_export)
        self.graphicsView_bird = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_bird.setGeometry(QtCore.QRect(1160, 180, 371, 591))
        self.graphicsView_bird.setObjectName("graphicsView_bird")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1550, 180, 561, 611))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget_layout = QtWidgets.QStackedWidget(self.verticalLayoutWidget_2)
        self.stackedWidget_layout.setObjectName("stackedWidget_layout")
        self.verticalLayout_3.addWidget(self.stackedWidget_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_last = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_last.setObjectName("pushButton_last")
        self.horizontalLayout.addWidget(self.pushButton_last)
        self.pushButton_next = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.stackedWidget_layout.raise_()
        self.layoutWidget.raise_()
        self.stackedWidget.raise_()
        self.pushButton.raise_()
        self.upload.raise_()
        self.label.raise_()
        self.tableWidget.raise_()
        self.label_2.raise_()
        self.comboBox.raise_()
        self.label_3.raise_()
        self.pushButton_3.raise_()
        self.label_upload_model.raise_()
        self.graphicsView_logo.raise_()
        self.graphicsView_bird.raise_()
        self.verticalLayoutWidget_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_layout.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "按的到嗎?"))
        self.upload.setText(_translate("MainWindow", "上傳CSV"))
        self.label.setText(_translate("MainWindow", "未上傳檔案"))
        self.label_2.setText(_translate("MainWindow", "資料預覽"))
        self.comboBox.setItemText(0, _translate("MainWindow", "KMeans"))
        self.comboBox.setItemText(1, _translate("MainWindow", "DBSCAN"))
        self.comboBox.setItemText(2, _translate("MainWindow", "NCC"))
        self.label_3.setText(_translate("MainWindow", "算法選擇 / 參數調整"))
        self.pushButton_3.setText(_translate("MainWindow", "匯入模型"))
        self.label_upload_model.setText(_translate("MainWindow", "未匯入模型 (選擇性)"))
        self.label_n_clusters.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">簇的數量 (n_clusters):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定要將數據分割成的簇的數量。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：使用者可能需要根據數據的性質和業務需求選擇適當的簇數量。可以嘗試不同的簇數量，然後使用一些評估指標（如輪廓系數、肘部法則等）來選擇最佳的簇數量。</li></ul></body></html>"))
        self.label_n_clusters.setText(_translate("MainWindow", "分群數 (n_clusters)"))
        self.lineEdit_n_clusters.setPlaceholderText(_translate("MainWindow", "輸入正整數"))
        self.label_init.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">初始中心點的選擇方法 (init):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定初始簇中心點的選擇方法。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：常用的選擇方法有&quot;k-means++&quot;，它會智能地選擇初始中心點，有助於加速算法的收斂</li></ul></body></html>"))
        self.label_init.setText(_translate("MainWindow", "初始中心點的選擇方法 (init)"))
        self.comboBox_init.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">初始中心點的選擇方法 (init):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定初始簇中心點的選擇方法。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：常用的選擇方法有&quot;k-means++&quot;，它會智能地選擇初始中心點，有助於加速算法的收斂</li></ul></body></html>"))
        self.comboBox_init.setItemText(0, _translate("MainWindow", "k-means++"))
        self.comboBox_init.setItemText(1, _translate("MainWindow", "random"))
        self.comboBox_init.setItemText(2, _translate("MainWindow", "uniform"))
        self.comboBox_init.setItemText(3, _translate("MainWindow", "zeros"))
        self.label_max_iter.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">最大迭代次數 (max_iter):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定算法運行的最大迭代次數。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：根據數據的複雜性和規模，選擇一個適當的迭代次數。如果算法在指定次數內沒有收斂，可以嘗試增加這個值。</li></ul></body></html>"))
        self.label_max_iter.setText(_translate("MainWindow", "最大迭代次數 (max_iter)"))
        self.spinBox_max_iter.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">最大迭代次數 (max_iter):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定算法運行的最大迭代次數。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：根據數據的複雜性和規模，選擇一個適當的迭代次數。如果算法在指定次數內沒有收斂，可以嘗試增加這個值。</li></ul></body></html>"))
        self.label_tol.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">收斂閾值 (tol):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定算法收斂的閾值，即當簇中心點的變化小於此閾值時，算法停止迭代。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：根據需要調整。較小的值可能會導致更精確的收斂，但也可能增加運行時間。</li></ul></body></html>"))
        self.label_tol.setText(_translate("MainWindow", "收斂閾值 (tol)"))
        self.spinBox_tol.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">收斂閾值 (tol):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定算法收斂的閾值，即當簇中心點的變化小於此閾值時，算法停止迭代。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：根據需要調整。較小的值可能會導致更精確的收斂，但也可能增加運行時間。</li></ul></body></html>"))
        self.label_metric.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">距離度量 (metric):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定計算數據點之間距離的度量方式，如歐氏距離、曼哈頓距離等。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：根據數據的特點選擇合適的距離度量方式。</li></ul></body></html>"))
        self.label_metric.setText(_translate("MainWindow", "距離度量 (metric)"))
        self.comboBox_metric.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">距離度量 (metric):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定計算數據點之間距離的度量方式，如歐氏距離、曼哈頓距離等。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：根據數據的特點選擇合適的距離度量方式。</li></ul></body></html>"))
        self.comboBox_metric.setItemText(0, _translate("MainWindow", "lloyd"))
        self.comboBox_metric.setItemText(1, _translate("MainWindow", "elkan"))
        self.label_random_seed.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">隨機數種子 (random_state):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定隨機數生成器的種子，以確保每次運行都得到相同的結果。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：在調試和複現實驗結果時使用，可以使結果更可控。</li></ul></body></html>"))
        self.label_random_seed.setText(_translate("MainWindow", "隨機數種子 (random_seed)"))
        self.spinBox_random_seed.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">隨機數種子 (random_state):</span></p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">描述：指定隨機數生成器的種子，以確保每次運行都得到相同的結果。</li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">推薦：在調試和複現實驗結果時使用，可以使結果更可控。</li></ul></body></html>"))
        self.label_data_group.setText(_translate("MainWindow", "單圖表資料數量"))
        self.label_threshold.setToolTip(_translate("MainWindow", "設定閾值距離，超過閾值的點視為離群值"))
        self.label_threshold.setText(_translate("MainWindow", "設定離散域值(threshold)"))
        self.lineEdit_threshold.setToolTip(_translate("MainWindow", "設定閾值距離，超過閾值的點視為離群值"))
        self.pushButton_plot.setText(_translate("MainWindow", "開始繪圖"))
        self.label_4.setText(_translate("MainWindow", "尚未支援該功能"))
        self.label_5.setText(_translate("MainWindow", "尚未支援該功能"))
        self.pushButton_model_export.setText(_translate("MainWindow", "匯出模型"))
        self.pushButton_last.setText(_translate("MainWindow", "上一張"))
        self.pushButton_next.setText(_translate("MainWindow", "下一張"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
