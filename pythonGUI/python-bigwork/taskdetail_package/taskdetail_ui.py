# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskdetail.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(527, 530)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(220, 60, 81, 16))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 484, 493))
        self.label.setStyleSheet(u"border-image: url(:/images/images/\u5c0f\u4e2d\u578b\u5e95\u5c42\u767d.png);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 36, 181, 26))
        self.label_2.setStyleSheet(u"font-weight:bold;\n"
"font-size:20px;")
        self.scrollArea_4 = QScrollArea(Form)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(50, 90, 431, 401))
        self.scrollArea_4.setStyleSheet(u"background-color:transparent;\n"
"border:0px;")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 431, 401))
        self.gridLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 431, 81))
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
"border-radius:0px;\n"
"border-bottom-right-radius:5px;\n"
"border-top-right-radius:5px")
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

        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_10, 2, 2, 1, 1)

        self.frame = QFrame(self.gridLayoutWidget_3)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-bottom:1px solid #eaeaea;\n"
"};")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(31, 3, 51, 21))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"border-radius:10px;\n"
"background-color:#1890FF;\n"
"color:white;\n"
"font-weight:bold;")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(87, 3, 51, 21))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"border-radius:10px;\n"
"background-color:#EF8113;\n"
"color:white;\n"
"font-weight:bold;")

        self.gridLayout_4.addWidget(self.frame, 1, 2, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setColumnStretch(2, 3)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.pushButton_10 = QPushButton(Form)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(420, 34, 21, 21))
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"border-image: url(:/icons/icons/\u6700\u5c0f\u5316.png);")
        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(450, 30, 27, 27))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"border-image: url(:/icons/icons/\u5173\u95ed.png);")
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(180, 65, 141, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5ef6\u5b89\u8defxx\u5bbf\u820d", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1\u5b8c\u6210\u60c5\u51b5\u4e00\u89c8\u8868", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u63d0\u4ea4\u65f6\u95f4", None))
        self.label_64.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210\u7387", None))
        self.label_62.setText(QCoreApplication.translate("Form", u"\u5bdd\u5ba4\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"6602", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"6603", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u67e5\u770b", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u64a4\u56de", None))
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u4efb\u52a1xxxxxx'x\uff08\u6d4b\u8bd5\u6587\u672c\uff09", None))
    # retranslateUi

