import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtWidgets, Qt

from Flower import dict_of_flowers

from test3 import Ui_MainWindow


class FlowerTermianl(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


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
        self.pushButton2.show()

        self.pushButton2.clicked.connect(lambda: self.start())

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
        # self.gridLayoutWidget_2.show()

        for key in dict_of_flowers.keys():
            print(key)
            label_3 = QtWidgets.QLabel()
            label_3.setObjectName(f"label_{key}")
            label_3.setText(key)
            # self.gridLayoutWidget_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
            spinBox = QtWidgets.QSpinBox()
            spinBox.setObjectName("spinBox")
            # layout_dish.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox)

            self.gridLayoutWidget_2.addWidget(label_3)
            self.gridLayoutWidget_2.addWidget(spinBox)

        self.pushButton1.clicked.connect(lambda: self.start())
        # self.pushButton.clicked.connect(lambda: self.c_start())
        #self.pushButton1.clicked.connect(lambda: self.start())

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
        self.pushButton2.hide()
        # self.gridLayoutWidget_2.hide()

    def c_start(self):
        dict_of_flowers[self.lineEdit.text()] = {'Название: ': self.lineEdit.text(),
                                                 'Цвет: ': self.lineEdit_2.text(),
                                                 'Цена: ': self.spinBox_2.value(),
                                                 'Количество: ': self.spinBox_3.value()}
        print(self.sender())
        self.profit_num = self.profit_num - self.spinBox_2.value() * self.spinBox_3.value()
        self.profit_c.setText(str(self.profit_num))
        self.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlowerTermianl()
    ex.show()
    app.exec_()
    exit()


