# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'studentmainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import functools

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGraphicsView,
                               QGridLayout, QGroupBox, QLabel, QLayout,
                               QMainWindow, QPushButton, QScrollArea, QSizePolicy,
                               QStackedWidget, QWidget)
import resource_studentmainwindow_test
import PySide6


class Ui_Student_MainWindow(object):
    def __init__(self):
        super().__init__()

    def setupUi(self, Student_MainWindow):
        if not Student_MainWindow.objectName():
            Student_MainWindow.setObjectName(u"Student_MainWindow")
        Student_MainWindow.resize(1055, 671)
        self.centralwidget = QWidget(Student_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 40, 928, 619))
        self.frame.setStyleSheet(u"QFrame {\n"
                                 "border-image: url(:/images/images/\u5e95\u5c42.png);\n"
                                 "}")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 257, 619))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
                                      "	background-image: url(:/images/images/\u4e3b\u754c\u9762\u5de6\u5e95\u5c42.png);\n"
                                      "	border:0px;\n"
                                      "}")
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 40, 136, 47))
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
                                    "	border-radius:0px;\n"
                                    "	background-image:url();\n"
                                    "}")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 0, 47, 47))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(
            u"border-image: url(:/icons/icons/\u9ed8\u8ba4\u5934\u50cf.png);")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 2, 41, 16))
        self.label.setStyleSheet(u"font-size:15px;\n"
                                 "font-family:'Microsoft Yahei';\n"
                                 "")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 26, 91, 16))
        self.label_2.setStyleSheet(u"font-size:15px;\n"
                                   "font-family:'Microsoft Yahei';")
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 110, 227, 106))
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
                                      "	border-radius:15px;\n"
                                      "	background-image: url(:/images/images/\u6b21\u6570\u7ea2\u5e95\u77e9\u5f62.png);\n"
                                      "	box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);\n"
                                      "}")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(33, 17, 84, 19))
        self.label_3.setStyleSheet(u"border-image:url();\n"
                                   "color:white;\n"
                                   "font-size:14px;\n"
                                   "font-weight:bold;\n"
                                   "")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 60, 16, 19))
        self.label_4.setStyleSheet(u"border-image:url();\n"
                                   "color:white;\n"
                                   "font-size:14px;\n"
                                   "font-weight:bold;\n"
                                   "")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(48, 40, 121, 41))
        self.label_5.setStyleSheet(u"border-image:url();\n"
                                   "color:white;\n"
                                   "font-size:40px;\n"
                                   "font-weight:bold;\n"
                                   "")
        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(30, 240, 190, 39))
        self.groupBox_4.setStyleSheet(u"background-image:url();")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 10, 19, 19))
        self.label_6.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/icon\uff0f\u6838\u9178\u68c0\u6d4b\u70b9.png);")
        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 0, 190, 39))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:#FFFFFF;\n"
                                        "font-size:14px;\n"
                                        "")
        self.pushButton_2.raise_()
        self.label_6.raise_()
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(30, 290, 190, 39))
        self.groupBox_5.setStyleSheet(u"background-image:url();")
        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 10, 19, 19))
        self.label_7.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/\u6570\u636e\u7edf\u8ba11.png);")
        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 0, 190, 39))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(30, 340, 190, 39))
        self.groupBox_6.setStyleSheet(u"background-image:url();")
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 10, 19, 19))
        self.label_8.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/\u6570\u636e\u7edf\u8ba11.png);")
        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 0, 190, 39))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(50, 400, 139, 32))
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 141, 16))
        self.label_9.setStyleSheet(u"border-image: url();\n"
                                   "color:#D6D6D6;\n"
                                   "font-size:12px;")
        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 18, 141, 16))
        self.label_10.setStyleSheet(u"border-image: url();\n"
                                    "color:#D6D6D6;\n"
                                    "font-size:12px;")
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(30, 450, 190, 39))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"background-color:black;\n"
                                        "color:white;\n"
                                        "border-radius:12px;\n"
                                        "box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);\n"
                                        "font-weight:bold;\n"
                                        "font-size:15px;")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 530, 113, 35))
        self.label_11.setStyleSheet(u"border-image: url(:/icons/icons/\u8d44\u6e90 1.png);\n"
                                    "")
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(50, 570, 146, 41))
        self.label_12.setStyleSheet(u"font-size:10px;\n"
                                    "font-family:'Microsoft Yahei Light';\n"
                                    "border-image: url();\n"
                                    "color:#A9A9A9;")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(830, 20, 27, 27))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(
            u"border-image: url(:/icons/icons/\u6700\u5c0f\u5316.png);")
        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(870, 20, 27, 27))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(
            u"border-image: url(:/icons/icons/\u5173\u95ed.png);")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(257, 10, 671, 611))
        self.stackedWidget.setStyleSheet(u"background-color:white;\n"
                                         "border-radius:15px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_13 = QLabel(self.page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 40, 221, 31))
        self.label_13.setStyleSheet(u"font-weight:bold;\n"
                                    "font-size:24px;\n"
                                    "color:#3D3D3D;")
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 90, 671, 521))
        self.scrollArea.setStyleSheet(u"border-radius:15px;\n"
                                      "\n"
                                      "QScrollBar::vertical {\n"
                                      "    background: transparent;\n"
                                      "    width:5px;\n"
                                      "    margin: 0 0 0 0;\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::handle:vertical {\n"
                                      "    border-radius: 3px;\n"
                                      "	background: rgba(255,255,255,0.1);\n"
                                      "}\n"
                                      "\n"
                                      "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                      "    border: 1px solid grey;\n"
                                      "    width: 3px;\n"
                                      "    height: 3px;\n"
                                      "    background: white;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(False)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(
            u"scrollAreaWidgetContents")
        scrollheight = 211 + 218 * 2
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 671, scrollheight))
        self.scrollAreaWidgetContents.setStyleSheet(u"border-radius:15px;")
        current_height = -10
        for i in range(3):
            self.frame_8 = QFrame(self.scrollAreaWidgetContents)
            self.frame_8.setObjectName(u"frame_8")
            self.frame_8.setGeometry(QRect(10, current_height, 651, 218))
            self.frame_8.setStyleSheet(u"border-radius:0px;\n"
                                       "border:1px solid #D8D8D8;\n"
                                       "")
            current_height += 220
            self.label_16 = QLabel(self.frame_8)
            self.label_16.setObjectName(u"label_16")
            self.label_16.setGeometry(QRect(30, 20, 45, 45))
            self.label_16.setStyleSheet(u"background-color:#a0021f;\n"
                                        "border-image: url();\n"
                                        "border-radius:4px;\n"
                                        "color:white;\n"
                                        "font-size:15px;")
            self.label_16.setAlignment(Qt.AlignCenter)
            self.label_16.setText(QCoreApplication.translate("Student_MainWindow", u"\u4e0a\u4f20\n"
                                                                                   "\u4efb\u52a1", None))
            self.label_17 = QLabel(self.frame_8)
            self.label_17.setObjectName(u"label_17")
            self.label_17.setGeometry(QRect(90, 21, 321, 20))
            self.label_17.setStyleSheet(u"color:#3D3D3D;\n"
                                        "font-size:15px;")
            self.label_17.setText(QCoreApplication.translate(
                "Student_MainWindow", u"5\u670818\u65e5\u6297\u539f\u4e0a\u4f20\u4efb\u52a1", None))
            self.groupBox_8 = QGroupBox(self.frame_8)
            self.groupBox_8.setObjectName(u"groupBox_8")
            self.groupBox_8.setGeometry(QRect(490, 21, 115, 22))
            self.groupBox_8.setStyleSheet(u"background-image:url();\n"
                                          "border-radius:20px;")
            self.label_20 = QLabel(self.groupBox_8)
            self.label_20.setObjectName(u"label_20")
            self.label_20.setGeometry(QRect(25, 4, 15, 15))
            self.label_20.setStyleSheet(u"border-image:url();\n"
                                        "border-image: url(:/icons/icons/\u4e0a\u4f20.png);\n"
                                        "background-color:transparent;")
            pushButton_11 = QPushButton(self.groupBox_8)
            pushButton_11.setObjectName(u"pushButton_11")
            pushButton_11.setGeometry(QRect(0, 0, 115, 22))
            pushButton_11.setStyleSheet(u"border:0px;\n"
                                        "border-radius:10px;\n"
                                        "font-size:12px;\n"
                                        "color:#000000;\n"
                                        "background-color:#D8D8D8;\n"
                                        "")
            pushButton_11.setText(QCoreApplication.translate(
                "Student_MainWindow", u"      \u4e0a\u4f20\u56fe\u7247", None))
            pushButton_11.clicked.connect(functools.partial(self.test, i))
            pushButton_11.raise_()
            self.label_20.raise_()
            self.label_21 = QLabel(self.frame_8)
            self.label_21.setObjectName(u"label_21")
            self.label_21.setGeometry(QRect(90, 44, 321, 20))
            self.label_21.setStyleSheet(u"color:#D6D6D6;\n"
                                        "font-size:15px;")
            self.label_21.setText(QCoreApplication.translate(
                "Student_MainWindow", u"\u53d1\u5e03\u4eba\uff1a\u5f85\u586b\u5145", None))
            self.label_22 = QLabel(self.frame_8)
            self.label_22.setObjectName(u"label_22")
            self.label_22.setGeometry(QRect(500, 46, 101, 18))
            self.label_22.setStyleSheet(u"color:#D6D6D6;\n"
                                        "font-size:12px;\n"
                                        "border-image: url();")
            self.label_22.setText(QCoreApplication.translate(
                "Student_MainWindow", u"\u5b8c\u6210\u72b6\u6001\uff1a\u5f85\u586b\u5145", None))
            self.graphicsView = QGraphicsView(self.frame_8)
            self.graphicsView.setObjectName(u"graphicsView")
            self.graphicsView.setGeometry(QRect(50, 80, 121, 121))
            self.graphicsView.setStyleSheet(u"border-image: url(:/images/images/\u5f85\u4e0a\u4f20\u56fe\u7247.png);\n"
                                            "border-radius:5px;")
            self.graphicsView_2 = QGraphicsView(self.frame_8)
            self.graphicsView_2.setObjectName(u"graphicsView_2")
            self.graphicsView_2.setGeometry(QRect(190, 80, 121, 121))
            self.graphicsView_2.setStyleSheet(
                u"border-image: url(:/images/images/\u5f85\u4e0a\u4f20\u56fe\u7247.png);\n"
                "border-radius:5px;")
            self.graphicsView_3 = QGraphicsView(self.frame_8)
            self.graphicsView_3.setObjectName(u"graphicsView_3")
            self.graphicsView_3.setGeometry(QRect(330, 80, 121, 121))
            self.graphicsView_3.setStyleSheet(
                u"border-image: url(:/images/images/\u5f85\u4e0a\u4f20\u56fe\u7247.png);\n"
                "border-radius:5px;")
            self.graphicsView_4 = QGraphicsView(self.frame_8)
            self.graphicsView_4.setObjectName(u"graphicsView_4")
            self.graphicsView_4.setGeometry(QRect(470, 80, 121, 121))
            self.graphicsView_4.setStyleSheet(
                u"border-image: url(:/images/images/\u5f85\u4e0a\u4f20\u56fe\u7247.png);\n"
                "border-radius:5px;")
            self.line = QFrame(self.frame_8)
            self.line.setObjectName(u"line")
            self.line.setGeometry(QRect(10, 216, 611, 1))
            self.line.setStyleSheet(u"color:black;\n"
                                    "background-color:#D8D8D8;\n"
                                    "border-image: url();")
            self.line.setFrameShape(QFrame.HLine)
            self.line.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(30, 40, 241, 31))
        self.label_14.setStyleSheet(u"font-weight:bold;\n"
                                    "font-size:24px;\n"
                                    "color:#3D3D3D;")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(0, 90, 671, 521))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(
            u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 671, 521))
        self.label_38 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(30, 0, 96, 21))
        self.label_38.setStyleSheet(u"font-size:16px;\n"
                                    "font-weight:bold;")
        self.label_39 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(340, 0, 111, 21))
        self.label_39.setStyleSheet(u"font-size:16px;\n"
                                    "font-weight:bold;")
        self.label_40 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 230, 96, 21))
        self.label_40.setStyleSheet(u"font-size:16px;\n"
                                    "font-weight:bold;")
        self.label_41 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(30, 30, 258, 171))
        self.label_42 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(350, 30, 199, 171))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(29, 259, 601, 71))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.gridLayoutWidget)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_47, 1, 0, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;\n"
                                    "border-bottom-left-radius:5px;\n"
                                    "border-top-left-radius:5px")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;\n"
                                    "")
        self.label_45.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_45, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(30, 0, 75, 24))

        self.gridLayout_2.addWidget(self.frame_2, 1, 3, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_48, 1, 1, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;\n"
                                    "border-bottom-right-radius:5px;\n"
                                    "border-top-right-radius:5px")
        self.label_46.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_46, 0, 3, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_49, 1, 2, 1, 1)

        self.label_44 = QLabel(self.gridLayoutWidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_44, 0, 1, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_50, 2, 0, 1, 1)

        self.label_51 = QLabel(self.gridLayoutWidget)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_51, 2, 1, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_52, 2, 2, 1, 1)

        self.frame_3 = QFrame(self.gridLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_15 = QPushButton(self.frame_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(30, 0, 75, 24))

        self.gridLayout_2.addWidget(self.frame_3, 2, 3, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.gridLayout_2.setColumnStretch(3, 2)
        self.gridLayout_2.setColumnMinimumWidth(0, 3)
        self.gridLayout_2.setColumnMinimumWidth(1, 2)
        self.gridLayout_2.setColumnMinimumWidth(2, 2)
        self.gridLayout_2.setColumnMinimumWidth(3, 2)
        self.gridLayout_2.setRowMinimumHeight(0, 1)
        self.gridLayout_2.setRowMinimumHeight(1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(30, 40, 241, 31))
        self.label_15.setStyleSheet(u"font-weight:bold;\n"
                                    "font-size:24px;\n"
                                    "color:#3D3D3D;")
        self.stackedWidget.addWidget(self.page_2)
        self.stackedWidget.raise_()
        self.groupBox_2.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        Student_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Student_MainWindow)

        self.pushButton_2.clicked.connect(self.click_to_page1)
        self.pushButton_3.clicked.connect(self.click_to_page2)
        self.pushButton_4.clicked.connect(self.click_to_page3)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Student_MainWindow)

    # setupUi
    def test(self, num):
        print(num)

    def click_to_page1(self):
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_2.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:#FFFFFF;\n"
                                        "font-size:14px;\n"
                                        "color:black;\n"
                                        "")
        self.pushButton_3.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:transparent;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.pushButton_4.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:transparent;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.label_6.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/icon\uff0f\u6838\u9178\u68c0\u6d4b\u70b9.png);")
        self.label_7.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/数据统计1.png);")
        self.label_8.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/SQL审核(1).png);")

    def click_to_page2(self):
        self.stackedWidget.setCurrentIndex(1)
        self.pushButton_3.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:#FFFFFF;\n"
                                        "font-size:14px;\n"
                                        "color:black;\n"
                                        "")
        self.pushButton_2.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:transparent;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.pushButton_4.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:transparent;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.label_6.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/icon\uff0f\u6838\u9178\u68c0\u6d4b\u70b9(1).png);")
        self.label_7.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/数据统计.png);")
        self.label_8.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/SQL审核.png);")

    def click_to_page3(self):
        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_4.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:#FFFFFF;\n"
                                        "font-size:14px;\n"
                                        "color:black;\n"
                                        "")
        self.pushButton_2.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:transparent;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.pushButton_3.setStyleSheet(u"border:0px;\n"
                                        "border-radius:12px;\n"
                                        "background-color:transparent;\n"
                                        "font-size:14px;\n"
                                        "color:#D6D6D6;\n"
                                        "")
        self.label_6.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/icon\uff0f\u6838\u9178\u68c0\u6d4b\u70b9(1).png);")
        self.label_7.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/数据统计1.png);")
        self.label_8.setStyleSheet(u"border-image:url();\n"
                                   "border-image: url(:/icons/icons/SQL审核(1).png);")

    def retranslateUi(self, Student_MainWindow):
        Student_MainWindow.setWindowTitle(QCoreApplication.translate(
            "Student_MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6b22\u8fce\uff0c", None))
        self.label_2.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u5f90\u653f\u6770\u767b\u5f55", None))
        self.groupBox_3.setTitle("")
        self.label_3.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u60a8\u5df2\u63d0\u4ea4\u6297\u539f", None))
        self.label_4.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6b21", None))
        self.label_5.setText(QCoreApplication.translate(
            "Student_MainWindow", u"0", None))
        self.groupBox_4.setTitle("")
        self.label_6.setText("")
        self.pushButton_2.setText(QCoreApplication.translate(
            "Student_MainWindow", u"    \u6297\u539f\u56fe\u7247\u63d0\u4ea4", None))
        self.groupBox_5.setTitle("")
        self.label_7.setText("")
        self.pushButton_3.setText(QCoreApplication.translate(
            "Student_MainWindow", u"    \u5386\u53f2\u6570\u636e\u7edf\u8ba1", None))
        self.groupBox_6.setTitle("")
        self.label_8.setText("")
        self.pushButton_4.setText(QCoreApplication.translate(
            "Student_MainWindow", u"    \u697c\u680b\u6570\u636e\u7ba1\u7406", None))
        self.groupBox_7.setTitle("")
        self.label_9.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6240\u5c5e\u697c\u680b\uff1a\u5f85\u586b\u5145", None))
        self.label_10.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6240\u5c5e\u5bbf\u820d\uff1a\u5f85\u586b\u5145", None))
        self.pushButton_5.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u9000\u51fa\u767b\u5f55", None))
        self.label_11.setText("")
        self.label_12.setText(
            QCoreApplication.translate("Student_MainWindow", u"COPYRIGHT@2021-2022 \u5f90\u653f\u6770\n"
                                                             "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\u2014\u8bfe\u7a0b\u8bbe\u8ba1\n"
                                                             "Python PySide6\u5b9e\u73b0", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.label_13.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6b63\u5728\u8fdb\u884c\u7684\u4efb\u52a1\u5217\u8868", None))
        self.groupBox_8.setTitle("")
        self.label_20.setText("")
        self.label_14.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u5386\u53f2\u63d0\u4ea4\u6570\u636e\u7edf\u8ba1\u5206\u6790", None))
        self.label_38.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u63d0\u4ea4\u65f6\u95f4\u7edf\u8ba1", None))
        self.label_39.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6708\u5ea6\u63d0\u4ea4\u7387\u7edf\u8ba1", None))
        self.label_40.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u63d0\u4ea4\u5386\u53f2\u8be6\u60c5", None))
        self.label_41.setText("")
        self.label_42.setText("")
        self.label_47.setText(QCoreApplication.translate(
            "Student_MainWindow", u"5\u670818\u65e5\u6297\u539f\u63d0\u4ea4", None))
        self.label_43.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u6d3b\u52a8\u4efb\u52a1\u540d\u79f0", None))
        self.label_45.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u63d0\u4ea4\u72b6\u6001", None))
        self.pushButton_8.setText(QCoreApplication.translate(
            "Student_MainWindow", u"PushButton", None))
        self.label_48.setText(QCoreApplication.translate(
            "Student_MainWindow", u"2022-05-21 06:25:30", None))
        self.label_46.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u63d0\u4ea4\u56fe\u7247\u67e5\u770b", None))
        self.label_49.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u5f85\u5ba1\u67e5", None))
        self.label_44.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u63d0\u4ea4\u65f6\u95f4", None))
        self.label_50.setText(QCoreApplication.translate(
            "Student_MainWindow", u"TextLabel", None))
        self.label_51.setText(QCoreApplication.translate(
            "Student_MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate(
            "Student_MainWindow", u"TextLabel", None))
        self.pushButton_15.setText(QCoreApplication.translate(
            "Student_MainWindow", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate(
            "Student_MainWindow", u"\u697c\u680b\u6297\u539f\u7efc\u5408\u7ba1\u7406\u5e73\u53f0", None))
    # retranslateUi


if __name__ == "__main__":
    import sys
    import os

    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication(sys.argv)
    RegistWindow = QMainWindow()
    ui = Ui_Student_MainWindow()
    ui.setupUi(RegistWindow)
    RegistWindow.show()
    app.exec()
