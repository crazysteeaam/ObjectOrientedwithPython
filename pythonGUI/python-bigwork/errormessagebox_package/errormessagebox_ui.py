# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'errormessagebox.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QWidget, QMainWindow)
import errormessagebox_package.resource_errormessagebox as resource_errormessagebox
import os
import PySide6
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Ui_ErrorMessageBox(QWidget):
    def __init__(self,msg):
        super().__init__()
        print("ok")
        self.msg=msg

    def setupUi(self,parent):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(696, 396)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon("./icons/logo.png"))
        self.label_backwhite = QLabel(self)
        self.label_backwhite.setObjectName(u"label_backwhite")
        self.label_backwhite.setGeometry(QRect(110, 90, 441, 181))
        self.label_backwhite.setStyleSheet(
            u"background-image: url(:/images/images/\u9519\u8bef\u7a97\u53e3\u5e95\u767d.png);")
        self.label_erroricon = QLabel(self)
        self.label_erroricon.setObjectName(u"label_erroricon")
        self.label_erroricon.setGeometry(QRect(150, 120, 23, 23))
        self.label_erroricon.setStyleSheet(u"border-image: url(:/icons/icons/\u9519\u8bef.png);")
        self.errortitle = QLabel(self)
        self.errortitle.setObjectName(u"errortitle")
        self.errortitle.setGeometry(QRect(184, 118, 160, 26))
        self.errortitle.setStyleSheet(u"color:black;\n"
                                      "font-family:'Microsoft Yahei';\n"
                                      "font-size:20px;")
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(400, 200, 108, 45))
        self.pushButton.setStyleSheet(u"background-color:#1A73E8;\n"
                                      "color:white;\n"
                                      "font-size:20px;\n"
                                      "font-family:'Microsoft Yahei';\n"
                                      "font-weight:bold;\n"
                                      "border-radius:15px;")
        self.errortext = QLabel(self)
        self.errortext.setObjectName(u"errortext")
        self.errortext.setGeometry(QRect(150, 156, 331, 21))
        self.errortext.setStyleSheet(u"color:black;\n"
                                     "font-size:16px;\n"
                                     "font-family:'Microsoft Yahei'")
        self.errortext.setText(self.msg)

        self.retranslateUi()

        self.setWindowTitle("错误提示窗口")
        QMetaObject.connectSlotsByName(self)
        self.setWindowTitle("警告")

        self.pushButton.clicked.connect(self.close)

    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_backwhite.setText("")
        self.label_erroricon.setText("")
        self.errortitle.setText(
            QCoreApplication.translate("Form", u"\u6765\u81ea\u5ba2\u6237\u7aef\u7684\u63d0\u793a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.errortext.setText(self.msg)


if __name__ == "__main__":
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication()
    my_window = QMainWindow()
    ui = Ui_ErrorMessageBox(my_window)
    my_window.show()
    app.exec()
