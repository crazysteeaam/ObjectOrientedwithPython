# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'regist.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QGroupBox, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QWidget, QDialog)
from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import regist_package.resource_regist as resource_regist
import regist_package.regist_data as regist_data
import errormessagebox_package.errormessagebox_ui as errormessagebox_ui
import PySide6
import ctypes
import re

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class My_Window(QMainWindow):
    # 为窗口增加功能
    def __init__(self):
        super().__init__()
        self.Move = None
        self.Point = None

    def mousePressEvent(self, event):  # 事件开始
        if event.button() == Qt.LeftButton:
            self.Move = True  # 设定bool为True
            self.Point = event.globalPos() - self.pos()  # 记录起始点坐标
            print(self.Point)
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 移动时间
        if Qt.LeftButton and self.Move:  # 切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPos() - self.Point)  # 移动到鼠标到达的坐标点！
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 结束事件
        self.Move = False


class Ui_RegistWindow(My_Window):
    def __init__(self, parent):
        super().__init__()
        self.msg = ""
        self.domlist = []
        self.get_domlist()
        self.setupUi(self)
        self.setWindowTitle("注册窗口")
        self.add_shadow()

    def setupUi(self, RegistWindow):
        if not RegistWindow.objectName():
            RegistWindow.setObjectName(u"RegistWindow")
        RegistWindow.resize(944, 739)
        RegistWindow.setWindowIcon(QIcon("./icons/logo.png"))
        RegistWindow.move(360, 225)
        RegistWindow.setWindowFlags(Qt.FramelessWindowHint)
        RegistWindow.setAttribute(Qt.WA_TranslucentBackground)
        self.centralwidget = QWidget(RegistWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        RegistWindow.setCentralWidget(self.centralwidget)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 921, 631))
        self.label.setStyleSheet(
            u"background-image: url(:/images/images/\u6ce8\u518c\u5e95\u5c42.png);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(177, 120, 611, 410))
        self.frame.setStyleSheet(u"border-radius:15px;\n"
                                 "box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 611, 411))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.label_8 = QLabel(self.groupBox_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(15, 10, 256, 41))
        self.label_8.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:15px;")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.groupBox_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(35, 17, 40, 26))
        self.label_13.setStyleSheet(u"font-size:20px;\n"
                                    "font-weight:bold;\n"
                                    "color:#3d3d3d;")
        self.lineEdit_3 = QLineEdit(self.groupBox_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(85, 17, 181, 26))
        self.lineEdit_3.setStyleSheet(u"font-size:20px;")

        self.gridLayout.addWidget(self.groupBox_8, 1, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.groupBox_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(35, 10, 256, 41))
        self.label_4.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:15px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupBox_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(55, 17, 40, 26))
        self.label_7.setStyleSheet(u"font-size:20px;\n"
                                   "font-weight:bold;\n"
                                   "color:#3d3d3d;")
        self.lineEdit = QLineEdit(self.groupBox_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(115, 17, 171, 26))
        self.lineEdit.setStyleSheet(u"font-size:20px;")

        self.gridLayout.addWidget(self.groupBox_9, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-weight:light;\n"
                                   "font-family:'Microsoft Yahei Light'")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 2)

        self.groupBox_7 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(15, 10, 256, 41))
        self.label_9.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:15px;")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.comboBox = QComboBox(self.groupBox_7)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(15, 20, 255, 22))
        self.comboBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox.setStyleSheet(u"QComboBox{\n"
                                    "	border:1px solid white;\n"
                                    "	font-size:15px;\n"
                                    "	combobox-popup: 0;\n"
                                    "	padding-left:110px;\n"
                                    "	background-color: white;\n"
                                    "}\n"
                                    "QComboBox::down-arrow {\n"
                                    "	image: url(:/icons/icons/_\u4e0b\u62c9\u7bad\u5934\u5c0f.png);\n"
                                    "	height:22px;\n"
                                    "	width:22px;\n"
                                    "	padding-right:9px;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView{\n"
                                    "	outline: 0px solid gray;\n"
                                    "	padding-left: 8px;\n"
                                    "	padding-top: 20px;\n"
                                    "	background-color:#ffffff;\n"
                                    "	color: #AFADAD;\n"
                                    "	box-shadow: none;\n"
                                    "}\n"
                                    "QComboBox QAbstractItemView::item{\n"
                                    "	min-height: 30px;\n"
                                    "	selection-color:white;\n"
                                    "	selection-background-color: #B6B6B6;\n"
                                    "	outline: 0px solid gray;\n"
                                    "}\n"
                                    "QComboBox::drop-down{\n"
                                    "	border:0px solid white;\n"
                                    "	background-color: rgb(255, 255, 255);\n"
                                    "}\n"
                                    "QComboBox QAbstractScrollArea QScrollBar:vertical{\n"
                                    "	width: 6px;\n"
                                    "	height:100px;\n"
                                    "	background-color: transparent;\n"
                                    "}\n"
                                    "QComboBox QAbstractScrollArea QScrollBar::handle:vertical{\n"
                                    "	background: #B6B6B6;\n"
                                    "}\n"
                                    "QComboBox QScrollBar::add-line::vertical{\n"
                                    "	border:none;\n"
                                    "}\n"
                                    "QComboBox QScrollBar::sub-line::vertical{\n"
                                    "	border:none;\n"
                                    "}\n"
                                    "QListView::item:hover{\n"
                                    "	background-color:#B6B6B6;\n"
                                    "}")
        self.comboBox.addItems(self.domlist)
        self.comboBox.setMaxVisibleItems(5)
        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(35, 17, 81, 26))
        self.label_14.setStyleSheet(u"font-size:20px;\n"
                                    "font-weight:bold;\n"
                                    "color:#3d3d3d;")
        self.gridLayout.addWidget(self.groupBox_7, 2, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(35, 10, 256, 41))
        self.label_5.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:15px;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(55, 17, 40, 26))
        self.label_11.setStyleSheet(u"font-size:20px;\n"
                                    "font-weight:bold;\n"
                                    "color:#3d3d3d;")
        self.lineEdit_2 = QLineEdit(self.groupBox_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)  # 密码框隐藏
        self.lineEdit_2.setGeometry(QRect(115, 17, 171, 26))
        self.lineEdit_2.setStyleSheet(u"font-size:20px;")

        self.gridLayout.addWidget(self.groupBox_6, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(35, 10, 256, 41))
        self.label_6.setStyleSheet(u"background-color:white;\n"
                                   "border-radius:15px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(55, 17, 81, 26))
        self.label_12.setStyleSheet(u"font-size:20px;\n"
                                    "font-weight:bold;\n"
                                    "color:#3d3d3d;")
        self.lineEdit_4 = QLineEdit(self.groupBox_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)  # 密码框隐藏
        self.lineEdit_4.setGeometry(QRect(145, 17, 141, 26))
        self.lineEdit_4.setStyleSheet(u"font-size:20px;")

        self.gridLayout.addWidget(self.groupBox_4, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 20, 159, 41))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"background-color:black;\n"
                                        "border-radius:15px;\n"
                                        "color:white;\n"
                                        "font-size:20px;\n"
                                        "font-weight:bold;")

        self.gridLayout.addWidget(self.groupBox_2, 4, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.gridLayoutWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.pushButton_3 = QPushButton(self.groupBox_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(130, 20, 159, 41))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color:#a0021f;\n"
                                        "border-radius:15px;\n"
                                        "color:white;\n"
                                        "font-size:20px;\n"
                                        "font-weight:bold;")

        self.gridLayout.addWidget(self.groupBox_5, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(15, 10, 256, 41))
        self.label_10.setStyleSheet(u"background-color:white;\n"
                                    "border-radius:15px;")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(35, 17, 61, 26))
        self.label_15.setStyleSheet(u"font-size:20px;\n"
                                    "font-weight:bold;\n"
                                    "color:#3d3d3d;")
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(105, 17, 161, 26))
        self.lineEdit_5.setStyleSheet(u"font-size:20px;")

        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:#a0021f;\n"
                                   "font-family:'Microsoft Yahei';\n"
                                   "font-size:32px;\n"
                                   "font-weight:bold;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setGeometry(QRect(870, 30, 26, 26))
        self.pushButton.setStyleSheet(u"background-color:transparent;\n"
                                      "border-image: url(:/icons/icons/\u5173\u95ed1.png);\n"
                                      "border:0px;")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setGeometry(QRect(830, 30, 26, 26))
        self.pushButton_2.setStyleSheet(u"background-color:transparent;\n"
                                        "border-image: url(:/icons/icons/\u6700\u5c0f\u53161 (1).png);\n"
                                        "border:0px;")

        # 绑定按钮组件
        # 关闭窗口
        self.pushButton.clicked.connect(self.close)
        # 最小化按钮
        self.pushButton_2.clicked.connect(self.showMinimized)
        # 重置按钮
        self.pushButton_4.clicked.connect(self.reset)
        # 注册按钮
        self.pushButton_3.clicked.connect(self.regist)
        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)

    def add_shadow(self):
        # 添加阴影
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0, 0)  # 偏移
        self.effect_shadow.setBlurRadius(6)  # 阴影半径
        self.effect_shadow.setColor(Qt.gray)  # 阴影颜色
        self.centralwidget.setGraphicsEffect(self.effect_shadow)  # 将设置套用到widget窗口中

    def reset(self):
        # 重置按钮
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")

    def get_domlist(self):
        # 获取domlist
        self.domlist = regist_data.get_domlist()

    def regist(self) -> bool:
        # 注册按钮功能
        input_domname = self.comboBox.currentText()
        input_name = self.lineEdit.text()
        input_studentcode = self.lineEdit_3.text()
        input_domroom = self.lineEdit_5.text()
        input_password = self.lineEdit_2.text()
        input_password_again = self.lineEdit_4.text()
        if input_name == "" or input_studentcode == "" or input_password == "" or input_password_again == "" or input_domname == "" or input_domroom == "":
            self.error = errormessagebox_ui.Ui_ErrorMessageBox("有项目为空！")
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False
        if not self.validate_input(input_name, input_studentcode, input_password, input_password_again,
                                   input_domroom):
            self.error = errormessagebox_ui.Ui_ErrorMessageBox(self.msg)
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False
        if not regist_data.check_roominlist(input_domname,input_domroom):
            self.error = errormessagebox_ui.Ui_ErrorMessageBox("房间在当前楼栋不存在！")
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False
        print("注册验证成功!")
        rsaobject = RSA_encrypt()
        input_password = rsaobject.encrypt_data(input_password)
        print(input_password)
        regist_data.start_regist(input_name, input_studentcode, input_password, input_domname,
                                 input_domroom)
        self.hide()
        self.error = errormessagebox_ui.Ui_ErrorMessageBox("注册成功！")
        self.error.setupUi(QMainWindow())
        self.error.show()
        return True

    def validate_input(self, input_name: str, input_studentcode: str, input_password: str, input_password_again: str,
                       input_domroom: str) -> bool:
        # 前端代码，负责验证值是否合法
        if input_password != input_password_again:
            self.msg = "两次输入的密码不一致！"
            return False
        pattern = re.compile("^\d{9}$", re.S)
        if not re.findall(pattern, input_studentcode):
            self.msg = "学号不合法！"
            return False
        pattern = re.compile("^[A-z\\u4e00-\\u9fa5]*$", re.S)
        if not re.findall(pattern, input_name):
            self.msg = "姓名中不能含有数字或标点符号！"
            return False
        pattern = re.compile("^\d{4,5}$", re.S)
        if not re.findall(pattern, input_domroom):
            self.msg = "寝室号必须是4位或5位数字！"
            return False
        return True

    def retranslateUi(self):
        # 赋值控件
        self.setWindowTitle(QCoreApplication.translate(
            "RegistWindow", u"MainWindow", None))
        self.label.setText("")
        self.groupBox_8.setTitle("")
        self.label_8.setText("")
        self.label_13.setText(QCoreApplication.translate(
            "RegistWindow", u"\u5b66\u53f7", None))
        self.lineEdit_3.setPlaceholderText(
            QCoreApplication.translate("RegistWindow", u"\u8bf7\u8f93\u5165\u5b66\u53f7", None))
        self.groupBox_9.setTitle("")
        self.label_4.setText("")
        self.label_7.setText(QCoreApplication.translate(
            "RegistWindow", u"\u59d3\u540d", None))
        self.lineEdit.setPlaceholderText(
            QCoreApplication.translate("RegistWindow", u"\u8bf7\u8f93\u5165\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("RegistWindow", u"\n"
                                                                        "COPYRIGHT@2021-2022 \u5f90\u653f\u6770\n"
                                                                        "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\u2014\u8bfe\u7a0b\u8bbe\u8ba1",
                                                        None))
        self.groupBox_7.setTitle("")
        self.label_9.setText("")
        self.label_14.setText(QCoreApplication.translate(
            "RegistWindow", u"\u6240\u5c5e\u697c\u680b", None))
        self.comboBox.setPlaceholderText(
            QCoreApplication.translate("RegistWindow", u"\u8bf7\u9009\u62e9\u697c\u680b", None))
        self.groupBox_6.setTitle("")
        self.label_5.setText("")
        self.label_11.setText(QCoreApplication.translate(
            "RegistWindow", u"\u5bc6\u7801", None))
        self.lineEdit_2.setPlaceholderText(
            QCoreApplication.translate("RegistWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.groupBox_4.setTitle("")
        self.label_6.setText("")
        self.label_12.setText(QCoreApplication.translate(
            "RegistWindow", u"\u786e\u8ba4\u5bc6\u7801", None))
        self.lineEdit_4.setPlaceholderText(
            QCoreApplication.translate("RegistWindow", u"\u518d\u6b21\u8f93\u5165\u5bc6\u7801", None))
        self.pushButton_4.setText(QCoreApplication.translate(
            "RegistWindow", u"\u91cd\u7f6e", None))
        self.groupBox_5.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate(
            "RegistWindow", u"\u6ce8\u518c", None))
        self.groupBox.setTitle("")
        self.label_10.setText("")
        self.label_15.setText(QCoreApplication.translate(
            "RegistWindow", u"\u5bdd\u5ba4\u53f7", None))
        self.lineEdit_5.setPlaceholderText(
            QCoreApplication.translate("RegistWindow", u"\u8bf7\u8f93\u5165\u5bdd\u5ba4\u53f7", None))
        self.label_3.setText(QCoreApplication.translate(
            "RegistWindow", u"\u7528\u6237\u6ce8\u518c", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.lineEdit_3.setPlaceholderText("请输入11位学号")


class RSA_encrypt(object):
    # 前端代码，加密密码
    def get_key(self, key_file):
        with open(key_file) as f:
            data = f.read()
            key = RSA.importKey(data)
        return key

    def encrypt_data(self, msg):
        public_key = self.get_key('./rsa_public_key.pem')
        cipher = PKCS1_cipher.new(public_key)
        encrypt_text = base64.b64encode(cipher.encrypt(bytes(msg.encode("utf8"))))
        return encrypt_text.decode('utf-8')


if __name__ == "__main__":
    import sys
    import os

    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication(sys.argv)
    RegistWindow = QMainWindow()
    ui = Ui_RegistWindow()
    ui.setupUi(RegistWindow)
    RegistWindow.show()
    app.exec()
