import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import  *
import re

import gui
import scripts

class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)# Это нужно для инициализации нашего дизайна
        self.comboBox.currentIndexChanged.connect(self.test)

        

    def test(self):
        self.listWidget.clear()
        num = self.comboBox.currentText()
        num = num[6:]
        print(num)
        week = scripts.get_week(num)
        for i in range(len(week)):
            item = QListWidgetItem(week[i])
            #self.listWidget.setCurrentRow(20)
            self.listWidget.addItem(item)





if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    sys.exit(app.exec_())

