# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 811)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 201, 16))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 40, 861, 721))
        self.listWidget.setObjectName("listWidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(730, 10, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 10, 121, 20))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "?????????????????? ????????????: ??6??-307??-19"))
        self.comboBox.setItemText(1, _translate("MainWindow", "???????????? 1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "???????????? 2"))
        self.comboBox.setItemText(3, _translate("MainWindow", "???????????? 3"))
        self.comboBox.setItemText(4, _translate("MainWindow", "???????????? 4"))
        self.comboBox.setItemText(5, _translate("MainWindow", "???????????? 5"))
        self.comboBox.setItemText(6, _translate("MainWindow", "???????????? 6"))
        self.comboBox.setItemText(7, _translate("MainWindow", "???????????? 7"))
        self.comboBox.setItemText(8, _translate("MainWindow", "???????????? 8"))
        self.comboBox.setItemText(9, _translate("MainWindow", "???????????? 9"))
        self.comboBox.setItemText(10, _translate("MainWindow", "???????????? 10"))
        self.comboBox.setItemText(11, _translate("MainWindow", "???????????? 11"))
        self.comboBox.setItemText(12, _translate("MainWindow", "???????????? 12"))
        self.comboBox.setItemText(13, _translate("MainWindow", "???????????? 13"))
        self.comboBox.setItemText(14, _translate("MainWindow", "???????????? 14"))
        self.comboBox.setItemText(15, _translate("MainWindow", "???????????? 15"))
        self.comboBox.setItemText(16, _translate("MainWindow", "???????????? 16"))
        self.comboBox.setItemText(17, _translate("MainWindow", "???????????? 17"))
        self.comboBox.setItemText(18, _translate("MainWindow", "???????????? 18"))
        self.label_2.setText(_translate("MainWindow", "?????????????????? ????????????:"))
