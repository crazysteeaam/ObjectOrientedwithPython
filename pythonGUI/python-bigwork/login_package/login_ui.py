# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QWidget)
from Crypto import Random
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
import login_package.resource_login as resource_login
import login_package.login_data as login_data
import errormessagebox_package.errormessagebox_ui as errormessagebox_ui
import regist_package.regist_ui as regist_ui
import sys
import PySide6.QtWidgets as QtWidgets
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


class Ui_LoginWindow(QMainWindow):
    def __init__(self, app, window):
        super().__init__()
        self.m_flag = None
        self.m_Position = None
        self.ui = app
        self.loginwindow = window
        self.setupUi(window)  # 初始化UI
        self.add_shadow()  # 添加窗口阴影

    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(986, 695)
        LoginWindow.setWindowIcon(QIcon("./icons/logo.png"))
        LoginWindow.setWindowFlags(Qt.FramelessWindowHint)
        LoginWindow.setAttribute(Qt.WA_TranslucentBackground)
        LoginWindow.move(350, 200)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_backwhite = QLabel(self.centralwidget)
        self.label_backwhite.setObjectName(u"label_backwhite")
        self.label_backwhite.setGeometry(QRect(30, 40, 910, 619))
        self.label_backwhite.setStyleSheet(u"border-image: url(:/images/images/\u5e95\u5c42.png);\n"
                                           "box-shadow: 2px 2px 2px 1px rgba(0, 0, 0, 0.2);")
        self.leftpic = QLabel(self.centralwidget)
        self.leftpic.setObjectName(u"leftpic")
        self.leftpic.setGeometry(QRect(30, 40, 545, 619))
        self.leftpic.setStyleSheet(
            u"border-image: url(:/images/images/\u5fae\u4fe1\u56fe\u7247_20220503191141.png);")
        self.label_donghualogo = QLabel(self.centralwidget)
        self.label_donghualogo.setObjectName(u"label_donghualogo")
        self.label_donghualogo.setGeometry(QRect(630, 150, 248, 76))
        self.label_donghualogo.setStyleSheet(
            u"border-image: url(:/icons/icons/\u8d44\u6e90 1.png);")
        self.label_bigtitle = QLabel(self.centralwidget)
        self.label_bigtitle.setObjectName(u"label_bigtitle")
        self.label_bigtitle.setGeometry(QRect(680, 250, 160, 26))
        self.label_bigtitle.setStyleSheet(u"font-size:20px;\n"
                                          "font-weight:bold;\n"
                                          "font-family:'Microsoft Yahei';\n"
                                          "color:#a0021f;")
        self.label_student_input_back = QLabel(self.centralwidget)
        self.label_student_input_back.setObjectName(
            u"label_student_input_back")
        self.label_student_input_back.setGeometry(QRect(620, 310, 279, 45))
        self.label_student_input_back.setStyleSheet(u"border-radius:15px;\n"
                                                    "background-color:#f1f1f1;")
        self.label_password_input_back = QLabel(self.centralwidget)
        self.label_password_input_back.setObjectName(
            u"label_password_input_back")
        self.label_password_input_back.setGeometry(QRect(620, 380, 279, 45))
        self.label_password_input_back.setStyleSheet(u"border-radius:15px;\n"
                                                     "background-color:#f1f1f1;")
        self.label_student_input_label = QLabel(self.centralwidget)
        self.label_student_input_label.setObjectName(
            u"label_student_input_label")
        self.label_student_input_label.setGeometry(QRect(640, 320, 40, 26))
        self.label_student_input_label.setStyleSheet(u"color:#3d3d3d;\n"
                                                     "font-family:'Microsoft Yahei';\n"
                                                     "font-weight:bold;\n"
                                                     "font-size:20px;")
        self.label_password_input_label = QLabel(self.centralwidget)
        self.label_password_input_label.setObjectName(
            u"label_password_input_label")
        self.label_password_input_label.setGeometry(QRect(640, 390, 40, 26))
        self.label_password_input_label.setStyleSheet(u"color:#3d3d3d;\n"
                                                      "font-family:'Microsoft Yahei';\n"
                                                      "font-weight:bold;\n"
                                                      "font-size:20px;")
        self.pushButton_regist = QPushButton(self.centralwidget)
        self.pushButton_regist.setObjectName(u"pushButton_regist")
        self.pushButton_regist.setGeometry(QRect(630, 480, 123, 45))
        self.pushButton_regist.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_regist.setStyleSheet(u"background-color:black;\n"
                                             "border-radius:15px;\n"
                                             "color:white;\n"
                                             "font-family:'Microsoft Yahei';\n"
                                             "font-weight:bold;\n"
                                             "font-size:20px;")
        self.pushButton_login = QPushButton(self.centralwidget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setGeometry(QRect(770, 480, 123, 45))
        self.pushButton_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_login.setStyleSheet(u"background-color:#a0021f;\n"
                                            "border-radius:15px;\n"
                                            "color:white;\n"
                                            "font-family:'Microsoft Yahei';\n"
                                            "font-weight:bold;\n"
                                            "font-size:20px;")
        self.label_smalltext = QLabel(self.centralwidget)
        self.label_smalltext.setObjectName(u"label_smalltext")
        self.label_smalltext.setGeometry(QRect(650, 580, 231, 71))
        self.label_smalltext.setStyleSheet(u"text-align:center;\n"
                                           "font-family:'Microsoft Yahei';\n"
                                           "font-weight:light;\n"
                                           "font-size:14px;\n"
                                           "color:#A9A9A9;")
        self.label_smalltext.setAlignment(Qt.AlignCenter)
        self.lineEdit_student_input = QLineEdit(self.centralwidget)
        self.lineEdit_student_input.setObjectName(u"lineEdit_student_input")
        self.lineEdit_student_input.setGeometry(QRect(700, 320, 181, 26))
        self.lineEdit_student_input.setPlaceholderText("请输入学号")
        self.lineEdit_student_input.setStyleSheet(u"background-color:transparent;\n"
                                                  "border:0px;\n"
                                                  "font-size:20px;\n"
                                                  "selection-color: #cdcdcd;")
        self.lineEdit_password_input = QLineEdit(self.centralwidget)
        self.lineEdit_password_input.setObjectName(u"lineEdit_password_input")
        self.lineEdit_password_input.setEchoMode(QLineEdit.Password)  # 密码框隐藏
        self.lineEdit_password_input.setGeometry(QRect(700, 390, 181, 26))
        self.lineEdit_password_input.setPlaceholderText("请输入密码")
        self.lineEdit_password_input.setStyleSheet(u"background-color:transparent;\n"
                                                   "border:0px;\n"
                                                   "font-size:20px;")
        self.pushButton_shutdown = QPushButton(self.centralwidget)
        self.pushButton_shutdown.setObjectName(u"pushButton_shutdown")
        self.pushButton_shutdown.setGeometry(QRect(880, 60, 35, 35))
        self.pushButton_shutdown.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_shutdown.setStyleSheet(u"image: url(:/icons/icons/\u5173\u95ed.png);\n"
                                               "border:0;\n"
                                               "background-color:transparent;")
        self.pushButton_minimize = QPushButton(self.centralwidget)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setGeometry(QRect(838, 63, 30, 30))
        self.pushButton_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize.setStyleSheet(u"image: url(:/icons/icons/\u6700\u5c0f\u5316.png);\n"
                                               "border:0;\n"
                                               "background-color:transparent;")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.label_backwhite.raise_()
        self.label_bigtitle.raise_()
        self.label_donghualogo.raise_()
        self.leftpic.raise_()
        self.label_student_input_back.raise_()
        self.label_password_input_back.raise_()
        self.label_student_input_label.raise_()
        self.label_password_input_label.raise_()
        self.pushButton_regist.raise_()
        self.pushButton_login.raise_()
        self.label_smalltext.raise_()
        self.lineEdit_student_input.raise_()
        self.lineEdit_password_input.raise_()
        self.pushButton_shutdown.raise_()
        self.pushButton_minimize.raise_()

        # 按钮绑定事件
        # 关闭按钮
        self.pushButton_shutdown.clicked.connect(QCoreApplication.instance().quit)
        # 最小化按钮
        self.pushButton_minimize.clicked.connect(LoginWindow.showMinimized)
        # 登录按钮
        self.pushButton_login.clicked.connect(self.btn_login)
        # 注册按钮
        self.pushButton_regist.clicked.connect(self.btn_regist)
        self.retranslateUi(LoginWindow)
        QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setWindowTitle("登录")

    def btn_regist(self):
        new_windows = regist_ui.My_Window()
        self.regist = regist_ui.Ui_RegistWindow(new_windows)
        self.regist.show()

    def btn_login(self) -> bool:
        inputcode = self.lineEdit_student_input.text()
        userpassword = self.lineEdit_password_input.text()
        if inputcode == '' or userpassword == '':
            self.error = errormessagebox_ui.Ui_ErrorMessageBox("用户名或密码为空！")
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False
        rsaobject = RSA_encrypt()
        proceed_password = rsaobject.encrypt_data(userpassword)
        if login_data.validate_login(inputcode, proceed_password)==0:
            self.error = errormessagebox_ui.Ui_ErrorMessageBox("学号尚未注册！")
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False
        elif login_data.validate_login(inputcode, proceed_password)==1:
            self.error = errormessagebox_ui.Ui_ErrorMessageBox("用户名或密码错误！")
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False
        else:
            return True

    # 添加阴影
    def add_shadow(self):
        # 添加阴影
        self.effect_shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.effect_shadow.setOffset(0, 0)  # 偏移
        self.effect_shadow.setBlurRadius(6)  # 阴影半径
        self.effect_shadow.setColor(Qt.gray)  # 阴影颜色
        self.centralwidget.setGraphicsEffect(self.effect_shadow)  # 将设置套用到widget窗口中

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate(
            "LoginWindow", u"MainWindow", None))
        self.label_backwhite.setText("")
        self.leftpic.setText("")
        self.label_donghualogo.setText("")
        self.label_bigtitle.setText(QCoreApplication.translate(
            "LoginWindow", u"\u75ab\u60c5\u6297\u539f\u6536\u96c6\u7cfb\u7edf", None))
        self.label_student_input_back.setText("")
        self.label_password_input_back.setText("")
        self.label_student_input_label.setText(
            QCoreApplication.translate("LoginWindow", u"\u5b66\u53f7", None))
        self.label_password_input_label.setText(
            QCoreApplication.translate("LoginWindow", u"\u5bc6\u7801", None))
        self.pushButton_regist.setText(QCoreApplication.translate(
            "LoginWindow", u"\u6ce8\u518c", None))
        self.pushButton_login.setText(QCoreApplication.translate(
            "LoginWindow", u"\u767b\u5f55", None))
        self.label_smalltext.setText(
            QCoreApplication.translate("LoginWindow", u"COPYRIGHT@2021-2022 \u5f90\u653f\u6770\n"
                                                      "\u9762\u5411\u5bf9\u8c61\u7a0b\u5e8f\u8bbe\u8ba1\u2014\u8bfe\u7a0b\u8bbe\u8ba1\n"
                                                      "Python PySide6\u5b9e\u73b0", None))
        self.lineEdit_student_input.setText("")
        self.lineEdit_password_input.setText("")
        self.pushButton_shutdown.setText("")
        self.pushButton_minimize.setText("")


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
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  # 移动时间
        if Qt.LeftButton and self.Move:  # 切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPos() - self.Point)  # 移动到鼠标到达的坐标点！
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):  # 结束事件
        self.Move = False

    def closeEvent(self, event):
        # 重写关闭窗口事件，关闭窗口时触发以下事件
        a = QtWidgets.QMessageBox.question(self, '退出', '你确定要退出吗?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                           QtWidgets.QMessageBox.No)  # "退出"代表的是弹出框的标题,"你确认退出.."表示弹出框的内容
        if a == QtWidgets.QMessageBox.Yes:
            event.accept()  # 接受关闭事件
        else:
            event.ignore()  # 忽略关闭事件


class RSA_encrypt(object):
    # 前端加密数据
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
