# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'confirmmessagebox.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import PySide6
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal,QThread)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QWidget, QMainWindow, QMessageBox, QDialog)
import confirmmessagebox_package.resource_confirmmessagebox as resource_confirmmessagebox
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class My_Window(QDialog):
    # 为窗口增加功能
    def __init__(self):
        super().__init__()
        self.Move = None
        self.Point = None

    def mousePressEvent(self, event):  # 事件开始
        if event.button() == Qt.LeftButton:
            self.Move = True  # 设定bool为True
            self.Point = event.globalPos() - self.pos()  # 记录起始点坐标
            # print(self.Point)
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 移动时间
        if Qt.LeftButton and self.Move:  # 切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPos() - self.Point)  # 移动到鼠标到达的坐标点！
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 结束事件
        self.Move = False


class Ui_ConfirmMessageBox(My_Window):
    dialogSignal = Signal(int, str)

    def __init__(self, parent,msg):
        super().__init__()
        self.msg=msg
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(543, 396)
        Form.setWindowIcon(QIcon("./icons/logo.png"))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        self.label_erroricon = QLabel(Form)
        self.label_erroricon.setObjectName(u"label_erroricon")
        self.label_erroricon.setGeometry(QRect(103, 136, 31, 31))
        self.label_erroricon.setStyleSheet(
            u"border-image:url(:/icon/icons/\u5929\u732b\u63d0\u793a-\u63d0\u793a (1).png)")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(356, 222, 108, 45))
        self.pushButton.setStyleSheet(u"background-color:#ef8113;\n"
                                      "color:white;\n"
                                      "font-size:20px;\n"
                                      "font-family:'Microsoft Yahei';\n"
                                      "font-weight:bold;\n"
                                      "border-radius:15px;")
        self.errortext = QLabel(Form)
        self.errortext.setObjectName(u"errortext")
        self.errortext.setGeometry(QRect(106, 178, 331, 21))
        self.errortext.setStyleSheet(u"color:black;\n"
                                     "font-size:16px;\n"
                                     "font-family:'Microsoft Yahei'")
        self.errortext.setText(self.msg)
        self.label_backwhite = QLabel(Form)
        self.label_backwhite.setObjectName(u"label_backwhite")
        self.label_backwhite.setGeometry(QRect(66, 112, 441, 181))
        self.label_backwhite.setStyleSheet(
            u"background-image: url(:/images/images/\u9519\u8bef\u7a97\u53e3\u5e95\u767d.png);")
        self.errortitle = QLabel(Form)
        self.errortitle.setObjectName(u"errortitle")
        self.errortitle.setGeometry(QRect(140, 140, 160, 26))
        self.errortitle.setStyleSheet(u"color:black;\n"
                                      "font-family:'Microsoft Yahei';\n"
                                      "font-size:20px;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(235, 222, 108, 45))
        self.pushButton_2.setStyleSheet(u"background-color:#1A73E8;\n"
                                        "color:white;\n"
                                        "font-size:20px;\n"
                                        "font-family:'Microsoft Yahei';\n"
                                        "font-weight:bold;\n"
                                        "border-radius:15px;")
        self.label_backwhite.raise_()
        self.label_erroricon.raise_()
        self.pushButton.raise_()
        self.errortext.raise_()
        self.errortitle.raise_()
        self.pushButton_2.raise_()
        self.pushButton.clicked.connect(self.reject)
        self.pushButton_2.clicked.connect(self.accept)

        Form.setWindowTitle("确认窗口")
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def accept(self):  # 点击ok是发送内置信号
        print("accept")
        self.dialogSignal.emit(0, "传的对")
        self.destroy()

    def reject(self):  # 点击cancel时，发送自定义信号
        print('reject')
        self.dialogSignal.emit(1, "清空")
        self.destroy()

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_erroricon.setText("")
        self.pushButton.setText(QCoreApplication.translate(
            "Form", u"\u53d6\u6d88", None))
        self.label_backwhite.setText("")
        self.errortitle.setText(QCoreApplication.translate(
            "Form", u"\u6765\u81ea\u5ba2\u6237\u7aef\u7684\u63d0\u793a", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    import os

    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication(sys.argv)
    RegistWindow = My_Window()
    ui = Ui_ConfirmMessageBox(RegistWindow)
    RegistWindow.show()
    app.exec()
