# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Flower import dict_of_flowers, Flower


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 488)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("background-color: rgb(255, 242, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 396, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(40, 90, 311, 51))
        self.b1.setStyleSheet("background-color: rgb(255, 198, 255);")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(40, 170, 311, 51))
        self.b2.setStyleSheet("background-color: rgb(255, 198, 255);")
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(40, 250, 311, 51))
        self.b3.setStyleSheet("background-color: rgb(255, 198, 255);")
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(40, 330, 311, 51))
        self.b4.setStyleSheet("background-color: rgb(255, 198, 255);")
        self.b4.setObjectName("b4")
        self.profit = QtWidgets.QLabel(self.centralwidget)
        self.profit.setGeometry(QtCore.QRect(0, 420, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.profit.setFont(font)
        self.profit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.profit.setObjectName("profit")
        self.profit_c = QtWidgets.QLabel(self.centralwidget)
        self.profit_c.setGeometry(QtCore.QRect(200, 420, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.profit_c.setFont(font)
        self.profit_c.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.profit_c.setObjectName("profit_c")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 382, 488))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_1.addWidget(self.label_2, 1, 0, 1, 1)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 20, 381, 31))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        """self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spinBox = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)"""
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 381, 181))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spinBox_2 = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_2.setObjectName("spinBox_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_2)
        self.spinBox_3 = QtWidgets.QSpinBox(self.formLayoutWidget_2)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(20, 440, 93, 28))
        self.pushButton1.setObjectName("pushButton1")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(270, 440, 93, 28))
        self.pushButton2.setObjectName("pushButton2")

        self.gridLayoutWidget_2 = QtWidgets.QVBoxLayout()
        self.gridLayoutWidget_2 .setContentsMargins(0, 50, 381, 181)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        """
        self.dishesLayout = QtWidgets.QGridLayout()
        self.dishesLayout.setContentsMargins(0, 0, 0, 0)
        self.dishesLayout.setObjectName("dishesLayout")
        """
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.gridLayoutWidget.hide()
        self.formLayoutWidget.hide()
        self.formLayoutWidget_2.hide()
        self.pushButton.hide()
        self.pushButton1.hide()
        self.pushButton2.hide()
        self.add_funct()
        #self.gridLayoutWidget_2.hide()
        self.profit_num = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application"))
        self.label.setText(_translate("MainWindow", "Цветочный магазин"))
        self.b1.setText(_translate("MainWindow", "составить и продать букет"))
        self.b2.setText(_translate("MainWindow", "докупить цветы"))
        self.b3.setText(_translate("MainWindow", "узнать информацию о всех цветах"))
        self.b4.setText(_translate("MainWindow", "купить новый вид цветка"))
        self.profit.setText(_translate("MainWindow", "Доход"))
        self.profit_c.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        # self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Название"))
        self.label_5.setText(_translate("MainWindow", "Цвет"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.label_7.setText(_translate("MainWindow", "Количество"))
        self.pushButton.setText(_translate("MainWindow", "ОК"))
        self.pushButton1.setText(_translate("MainWindow", "Назад"))
        self.pushButton2.setText(_translate("MainWindow", "Ок"))

    def add_funct(self):
        self.b4.clicked.connect(lambda: self.push_b4())
        self.b3.clicked.connect(lambda: self.push_b3())
        self.b2.clicked.connect(lambda: self.push_b2())
        self.b1.clicked.connect(lambda: self.push_b1())

    def push_b4(self):

        self.label.hide()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.profit.hide()
        self.profit_c.hide()

        self.formLayoutWidget_2.show()
        self.pushButton.show()
        self.pushButton1.show()

        self.pushButton.clicked.connect(lambda: self.c_start())
        self.pushButton1.clicked.connect(lambda: self.start())

    def push_b3(self):
        self.label_2.setText('')
        for key, value in dict_of_flowers.items():
            for i, j in value.items():
                self.label_2.setText(self.label_2.text() + i + str(j) + '\n')
        self.label_2.setText(self.label_2.text() + ' ' + '\n')

        self.label.hide()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.profit.hide()
        self.profit_c.hide()

        self.gridLayoutWidget.show()
        self.pushButton.show()

        self.pushButton.clicked.connect(lambda: self.start())

    def push_b2(self):
        self.label.hide()
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.profit.hide()
        self.profit_c.hide()

        self.pushButton.show()
        self.pushButton1.show()
        # self.gridLayoutWidget_2.show()

        i = -1
        for key in dict_of_flowers.keys():
            i += 1
            print(i)
            layout_dish = QtWidgets.QHBoxLayout()

            dish = QtWidgets.QCheckBox(key.__str__())
            dish.dish_name = key

            count_dish = QtWidgets.QSpinBox()
            count_dish.setEnabled(False)
            count_dish.setMinimum(1)
            dish.counter = count_dish

            count_dish.dish_to_count = dish
            #count_dish.valueChanged.connect(self.counter_value_changed)

            layout_dish.addWidget(dish)
            layout_dish.addWidget(count_dish)

            self.dishesLayout.addLayout(layout_dish, i, 1, 1, 1)


        # self.pushButton.clicked.connect(lambda: self.c_start())
        self.pushButton1.clicked.connect(lambda: self.start())


    def push_b1(self):
        pass

    def start(self):
        self.label.show()
        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.profit.show()
        self.profit_c.show()
        self.gridLayoutWidget.hide()
        self.formLayoutWidget.hide()
        self.formLayoutWidget_2.hide()
        self.pushButton.hide()
        self.pushButton1.hide()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.spinBox_2.clear()
        self.spinBox_3.clear()

    def c_start(self):
        dict_of_flowers[self.lineEdit.text()] = {'Название: ': self.lineEdit.text(),
                                                 'Цвет: ': self.lineEdit_2.text(),
                                                 'Цена: ': self.spinBox_2.value(),
                                                 'Количество: ': self.spinBox_3.value()}
        # print(self.sender())
        self.profit_num = self.profit_num - self.spinBox_2.value() * self.spinBox_3.value()
        self.profit_c.setText(str(self.profit_num))
        self.start()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())