# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'dormlist.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QPushButton, QScrollArea, QSizePolicy, QWidget)
import dormlist_package.resource_dormlist as resource_dormlist
import dormlist_package.dormlist_data as dormlist_data


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


class Ui_Dormlist(My_Window):
    def __init__(self, parent, dormid, floor, dormname):
        super().__init__()
        self.dormid = dormid
        self.floor = floor
        self.dormname = dormname
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(545, 538)
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        Form.setWindowIcon(QIcon("./icons/logo.png"))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 484, 493))
        self.label.setStyleSheet(
            u"border-image: url(:/images/images/\u5c0f\u4e2d\u578b\u5e95\u5c42\u767d.png);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 50, 151, 26))
        self.label_2.setStyleSheet(u"font-weight:bold;\n"
                                   "font-size:20px;")
        if self.floor != "其余楼层":
            self.label_2.setText(str(self.floor) + "楼情况一览表")
        else:
            self.label_2.setText(self.floor + "情况一览表")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 80, 81, 16))
        self.label_3.setText(self.dormname)

        if self.floor != "其余楼层":
            roominf_list = dormlist_data.getfloorforminf(self.dormid, self.floor)
        else:
            roominf_list = dormlist_data.getotherfloordorminf(self.dormid)
        self.scrollArea_4 = QScrollArea(Form)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(60, 110, 431, 401))
        self.scrollArea_4.setStyleSheet(u"background-color:transparent;\n"
                                        "border:0px;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(
            u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 431, 401))
        self.gridLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 421, 27 * (len(roominf_list) + 1)))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.gridLayoutWidget_3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "border:0px;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_63, 0, 1, 1, 1)

        self.label_64 = QLabel(self.gridLayoutWidget_3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_64, 0, 2, 1, 1)

        self.label_62 = QLabel(self.gridLayoutWidget_3)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border:0px;\n"
                                    "border-radius:0px;\n"
                                    "border-bottom-left-radius:5px;\n"
                                    "border-top-left-radius:5px;\n"
                                    "font-size:12px;")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_62, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color:#a0021f;\n"
                                   "border-image: url();\n"
                                   "color:white;\n"
                                   "font-weight:bold;\n"
                                   "border-radius:0px;\n"
                                   "border-bottom-right-radius:5px;\n"
                                   "border-top-right-radius:5px")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 0, 3, 1, 1)

        for i in range(len(roominf_list)):
            self.label_5 = QLabel(self.gridLayoutWidget_3)
            self.label_5.setObjectName(u"label_5")
            if i != len(roominf_list) - 1:
                self.label_5.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
            self.label_5.setAlignment(Qt.AlignCenter)
            self.label_5.setText(str(roominf_list[i][0]))

            self.gridLayout_4.addWidget(self.label_5, i + 1, 0, 1, 1)

            self.label_6 = QLabel(self.gridLayoutWidget_3)
            self.label_6.setObjectName(u"label_6")
            if i != len(roominf_list) - 1:
                self.label_6.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
            self.label_6.setAlignment(Qt.AlignCenter)
            self.label_6.setText(str(roominf_list[i][1]))

            self.gridLayout_4.addWidget(self.label_6, i + 1, 1, 1, 1)

            self.label_7 = QLabel(self.gridLayoutWidget_3)
            self.label_7.setObjectName(u"label_7")
            if i != len(roominf_list) - 1:
                self.label_7.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
            self.label_7.setAlignment(Qt.AlignCenter)
            self.label_7.setText(str(round(roominf_list[i][2],2) * 100) + "%")

            self.gridLayout_4.addWidget(self.label_7, i + 1, 2, 1, 1)

            self.frame = QFrame(self.gridLayoutWidget_3)
            self.frame.setObjectName(u"frame")
            if i != len(roominf_list) - 1:
                self.frame.setStyleSheet(u"QFrame{\n"
                                         "	border-bottom:1px solid #eaeaea;\n"
                                         "};")
            self.frame.setFrameShape(QFrame.StyledPanel)
            self.frame.setFrameShadow(QFrame.Raised)
            self.label_11 = QLabel(self.frame)
            self.label_11.setObjectName(u"label_11")
            self.label_11.setGeometry(QRect(10, 3, 41, 21))
            if roominf_list[i][2] * 100 == 100:
                self.label_11.setStyleSheet(u"border-radius:10px;\n"
                                            "background-color:#2DAE48;\n"
                                            "color:white;\n"
                                            "font-weight:bold;")
                self.label_11.setText("优秀")
            elif roominf_list[i][2] * 100 >= 90:
                self.label_11.setStyleSheet(u"border-radius:10px;\n"
                                            "background-color:#1890FF;\n"
                                            "color:white;\n"
                                            "font-weight:bold;")
                self.label_11.setText("正常")
            elif roominf_list[i][2] * 100 >= 70:
                self.label_11.setStyleSheet(u"border-radius:10px;\n"
                                            "background-color:#EF8113;\n"
                                            "color:white;\n"
                                            "font-weight:bold;")
                self.label_11.setText("一般")
            elif roominf_list[i][2] * 100 >= 60:
                self.label_11.setStyleSheet(u"border-radius:10px;\n"
                                            "background-color:#FB477C;\n"
                                            "color:white;\n"
                                            "font-weight:bold;")
                self.label_11.setText("预警")
            elif roominf_list[i][2] * 100 > 0:
                self.label_11.setStyleSheet(u"border-radius:10px;\n"
                                            "background-color:#EF1313;\n"
                                            "color:white;\n"
                                            "font-weight:bold;")
                self.label_11.setText("警告")
            else:
                self.label_11.setStyleSheet(u"border-radius:10px;\n"
                                            "background-color:#C0C0C0;\n"
                                            "color:white;\n"
                                            "font-weight:bold;")
                self.label_11.setText("为零")

            self.label_11.setAlignment(Qt.AlignCenter)

            self.gridLayout_4.addWidget(self.frame, i + 1, 3, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setColumnStretch(2, 1)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(460, 50, 27, 27))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(
            u"border-image: url(:/icons/icons/\u5173\u95ed.png);")
        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(430, 54, 21, 21))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(
            u"border-image: url(:/icons/icons/\u6700\u5c0f\u5316.png);")

        self.retranslateUi(Form)

        self.pushButton_9.clicked.connect(Form.close)
        self.pushButton_10.clicked.connect(Form.showMinimized)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_63.setText(QCoreApplication.translate(
            "Form", u"\u5bdd\u5ba4\u6570\u91cf", None))
        self.label_64.setText(QCoreApplication.translate(
            "Form", u"\u5b8c\u6210\u7387", None))
        self.label_62.setText(QCoreApplication.translate(
            "Form", u"\u5bdd\u5ba4\u53f7", None))
        self.label_4.setText(QCoreApplication.translate(
            "Form", u"\u8bc4\u4ef7\u6307\u6807", None))
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
    # retranslateUi


if __name__ == "__main__":
    import sys
    import os

    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication()
    my_window = My_Window()
    ui = Ui_Dormlist(my_window)
    my_window.show()
    app.exec()
