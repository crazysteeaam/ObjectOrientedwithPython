# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'piccheck.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import PySide6
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
                               QSizePolicy, QWidget)
import piccheck_package.resource_piccheck as resource_piccheck
import piccheck_package.piccheck_data as piccheck_data
import requests
from PIL import Image, ImageQt
import io
import asyncio
import aiohttp


class My_Window(QWidget):
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


class Ui_PicCheck(My_Window):
    def __init__(self, parent, taskid, roomid):
        super().__init__()
        self.taskid = taskid
        self.roomid = roomid
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(565, 554)
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        Form.setWindowIcon(QIcon("./icons/logo.png"))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 484, 493))
        self.label.setStyleSheet(
            u"border-image: url(:/images/images/\u5c0f\u4e2d\u578b\u5e95\u5c42\u767d.png);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 50, 140, 26))
        self.label_2.setStyleSheet(u"font-weight:bold;\n"
                                   "font-size:20px;")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(83, 89, 402, 351))
        self.frame.setStyleSheet(u"background-color:#EFEFEF;\n"
                                 "border-radius:15px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        urllist = piccheck_data.get_picurl(self.taskid, self.roomid)
        task_list = []

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 201, 174))
        self.label_3.setStyleSheet(u"color:#A79B9B;\n"
                                   "font-size:15px;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:0px;\n"
                                   "border-top-left-radius:15px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        if len(urllist) >= 1:
            task_list.append(self.visible_pic(urllist[0][0], self.label_3))
        else:
            self.label_3.setText(QCoreApplication.translate(
                "Form", u"\u6682\u65e0", None))

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 174, 201, 174))
        self.label_4.setStyleSheet(u"color:#A79B9B;\n"
                                   "font-size:15px;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:0px;\n"
                                   "border-bottom-left-radius:15px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        if len(urllist) >= 3:
            task_list.append(self.visible_pic(urllist[2][0], self.label_4))
        else:
            self.label_4.setText(QCoreApplication.translate(
                "Form", u"\u6682\u65e0", None))

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(201, 174, 201, 174))
        self.label_5.setStyleSheet(u"color:#A79B9B;\n"
                                   "font-size:15px;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:0px;\n"
                                   "border-bottom-right-radius:15px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        if len(urllist) >= 4:
            task_list.append(self.visible_pic(urllist[3][0], self.label_5))
        else:
            self.label_5.setText(QCoreApplication.translate(
                "Form", u"\u6682\u65e0", None))

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(201, 0, 201, 174))
        self.label_6.setStyleSheet(u"color:#A79B9B;\n"
                                   "font-size:15px;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:0px;\n"
                                   "border-top-right-radius:15px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        if len(urllist) >= 2:
            task_list.append(self.visible_pic(urllist[1][0], self.label_6))
        else:
            self.label_6.setText(QCoreApplication.translate(
                "Form", u"\u6682\u65e0", None))

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(230, 454, 108, 45))
        self.pushButton_2.setStyleSheet(u"background-color:#1A73E8;\n"
                                        "color:white;\n"
                                        "font-size:20px;\n"
                                        "font-family:'Microsoft Yahei';\n"
                                        "font-weight:bold;\n"
                                        "border-radius:15px;")

        asyncio.run(asyncio.wait(task_list))
        self.pushButton_2.clicked.connect(Form.close)
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    async def visible_pic(self, url, widget):
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                # print(resp.status)
                res = await resp.read()
                image = Image.open(io.BytesIO(res))
        width, height = image.size
        if width <= height:
            image = image.resize((widget.width(), int(widget.width() / width * height)), Image.LANCZOS)
        else:
            image = image.resize((int(widget.height() / height * width), widget.height()), Image.LANCZOS)
        image = image.crop((0, 0, widget.width(), widget.height()))
        image = image.convert('RGB')
        image = ImageQt.ImageQt(image)
        pixmap = QPixmap.fromImage(image)
        widget.setPixmap(pixmap)
        widget.setScaledContents(True)
        widget.setText("")
        widget.setStyleSheet(u"color:#A79B9B;\n"
                             "font-size:15px;\n"
                             "font-weight:bold;\n"
                             "border-radius:0px;\n"
                             "border-top-right-radius:15px;\n"
                             "background-color:transparent;")

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "Form", u"\u63d0\u4ea4\u56fe\u7247\u67e5\u770b\u5668", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("Form", u"\u5173\u95ed", None))
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
    ui = Ui_PicCheck(RegistWindow)
    RegistWindow.show()
    app.exec()
