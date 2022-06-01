# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtWidgets, QtGui

'''
 Pyqt 动态的添加控件
'''


class DynAddObject(QWidget):
    def __init__(self, parent=None):
        super(DynAddObject, self).__init__(parent)
        self.resize(300, 300)
        addButton = QtWidgets.QPushButton(u"添加控件")
        self.area = QtWidgets.QScrollArea()
        self.area.setWidgetResizable(True)
        self.layout = QtWidgets.QGridLayout()
        self.area.setLayout(self.layout)
        self.layout.addWidget(addButton, 1, 0)
        self.setLayout(self.layout)
        addButton.clicked.connect(self.add)

    def add(self):
        for i in range(2):
            btncont = self.layout.count()
            widget = QtWidgets.QPushButton(str(btncont), self)
            self.layout.addWidget(widget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = DynAddObject()
    form.show()
    app.exec_()
