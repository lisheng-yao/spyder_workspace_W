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
        MainWindow.resize(723, 603)
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
"\n"
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
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 0, 111, 41))
        self.pushButton.setObjectName("pushButton")
        
        self.upload = QtWidgets.QPushButton(self.centralwidget)
        self.upload.setGeometry(QtCore.QRect(50, 50, 93, 28))
        self.upload.setObjectName("upload")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 60, 931, 16))
        self.label.setObjectName("label")
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(150, 130, 451, 361))
        self.graphicsView.setObjectName("graphicsView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "按的到嗎"))
        self.upload.setText(_translate("MainWindow", "上傳CSV"))
        self.label.setText(_translate("MainWindow", "未上傳檔案"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
