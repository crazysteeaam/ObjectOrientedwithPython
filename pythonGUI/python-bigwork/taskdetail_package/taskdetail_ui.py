# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'taskdetail.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
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
                               QPushButton, QScrollArea, QSizePolicy, QWidget, QMainWindow)
import taskdetail_package.resource_taskdetail as resource_taskdetail
import taskdetail_package.taskdetail_data as taskdetail_data
import piccheck_package.piccheck_ui as piccheck_ui
import confirmmessagebox_package.confirmmessagebox_ui as confirmmessagebox_ui
import errormessagebox_package.errormessagebox_ui as errormessagebox_ui
import functools
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")


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


class Ui_TaskDetail(My_Window):
    def __init__(self, parent, taskid, stcode):
        super().__init__()
        self.taskid = taskid
        self.studentcode = stcode
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(527, 530)
        Form.setWindowIcon(QIcon("./icons/logo.png"))
        Form.setWindowFlags(Qt.FramelessWindowHint)
        Form.setAttribute(Qt.WA_TranslucentBackground)
        # 背景
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 484, 493))
        self.label.setStyleSheet(u"border-image: url(:/images/images/\u5c0f\u4e2d\u578b\u5e95\u5c42\u767d.png);")

        # 标题
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 36, 181, 26))
        self.label_2.setStyleSheet(u"font-weight:bold;\n"
                                   "font-size:20px;")
        # 小标题
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(30, 65, 461, 20))
        self.label_12.setAlignment(Qt.AlignCenter)
        taskcontent = taskdetail_data.get_taskname(self.taskid)
        self.label_12.setText(taskcontent[0])

        complete_situation_list = taskdetail_data.get_roomcompletesitui_fromtask(self.taskid)
        self.scrollArea_4 = QScrollArea(Form)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(50, 90, 431, 401))
        self.scrollArea_4.setStyleSheet(u"background-color:transparent;\n"
                                        " border:none;\n"
                                        "\n"
                                        "QScrollBar::vertical {\n"
                                        "    background-color: transparent;\n"
                                        "    width:5px;\n"
                                        "    border-radius:15px;\n"
                                        "    border-image: url();\n"
                                        "    border:0px;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::handle:vertical {\n"
                                        "    border-radius: 3px;\n"
                                        "	 background: #D8D8D8;;\n"
                                        "}\n"
                                        "\n"
                                        "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                        "    border: 1px solid grey;\n"
                                        "    width: 3px;\n"
                                        "    height: 3px;\n"
                                        "    background: white;\n"
                                        "}\n"
                                        "")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 431, 401))
        self.gridLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 431, 27 * (len(complete_situation_list) + 1)))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        # 表头
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
                                    "border-radius:0px;\n")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_64, 0, 2, 1, 1)

        self.label_65 = QLabel(self.gridLayoutWidget_3)
        self.label_65.setObjectName(u"label_64")
        self.label_65.setStyleSheet(u"background-color:#a0021f;\n"
                                    "border-image: url();\n"
                                    "color:white;\n"
                                    "font-weight:bold;\n"
                                    "border-radius:0px;\n"
                                    "border-bottom-right-radius:5px;\n"
                                    "border-top-right-radius:5px")
        self.label_65.setText("核验")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_65, 0, 3, 1, 1)

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

        # 表格内容
        for i in range(len(complete_situation_list)):
            self.label_5 = QLabel(self.gridLayoutWidget_3)
            self.label_5.setObjectName(u"label_" + str(complete_situation_list[i][0]) + "_1")
            self.label_5.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
            self.label_5.setAlignment(Qt.AlignCenter)
            self.label_5.setText(complete_situation_list[i][1])

            self.gridLayout_4.addWidget(self.label_5, i + 1, 0, 1, 1)

            self.label_6 = QLabel(self.gridLayoutWidget_3)
            self.label_6.setObjectName(u"label_" + str(complete_situation_list[i][0]) + "_2")
            self.label_6.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
            self.label_6.setAlignment(Qt.AlignCenter)
            self.label_6.setText(complete_situation_list[i][2])

            self.gridLayout_4.addWidget(self.label_6, i + 1, 1, 1, 1)

            if complete_situation_list[i][2] != '/':
                self.frame = QFrame(self.gridLayoutWidget_3)
                self.frame.setObjectName(u"frame_" + str(complete_situation_list[i][0]) + "_1")
                self.frame.setStyleSheet(u"QFrame{\n"
                                         "	border-bottom:1px solid #eaeaea;\n"
                                         "};")
                self.frame.setFrameShape(QFrame.StyledPanel)
                self.frame.setFrameShadow(QFrame.Raised)
                self.pushButton = QPushButton(self.frame)
                self.pushButton.setObjectName(u"pushButton_" + str(complete_situation_list[i][0]) + "_1")
                self.pushButton.setGeometry(QRect(20, 3, 51, 21))
                self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushButton.setStyleSheet(u"border-radius:10px;\n"
                                              "background-color:#1890FF;\n"
                                              "color:white;\n"
                                              "font-weight:bold;")
                self.pushButton.clicked.connect(functools.partial(self.pic_check, complete_situation_list[i][0]))

                self.pushButton_2 = QPushButton(self.frame)
                self.pushButton_2.setObjectName(u"pushButton_" + str(complete_situation_list[i][0]) + "_2")
                self.pushButton_2.setGeometry(QRect(80, 3, 51, 21))
                self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
                self.pushButton_2.setStyleSheet(u"border-radius:10px;\n"
                                                "background-color:#EF8113;\n"
                                                "color:white;\n"
                                                "font-weight:bold;")
                self.pushButton_2.clicked.connect(functools.partial(self.delete_mission, complete_situation_list[i][0]))

                self.gridLayout_4.addWidget(self.frame, i + 1, 2, 1, 1)
            else:
                self.label_10 = QLabel(self.gridLayoutWidget_3)
                self.label_10.setObjectName(u"label_" + str(complete_situation_list[i][0]) + "_3")
                self.label_10.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
                self.label_10.setAlignment(Qt.AlignCenter)
                self.label_10.setText("未完成")

                self.gridLayout_4.addWidget(self.label_10, i + 1, 2, 1, 1)

            self.label_66 = QLabel(self.gridLayoutWidget_3)
            self.label_66.setObjectName(u"label_" + str(complete_situation_list[i][0]) + "_4")
            self.label_66.setStyleSheet(u"border-bottom:1px solid #eaeaea;")
            self.label_66.setAlignment(Qt.AlignCenter)
            if complete_situation_list[i][3] == 0.5:
                self.label_66.setText("/")
            elif complete_situation_list[i][3] == 0.0:
                self.label_66.setText("未核验")
            elif complete_situation_list[i][3] == 1.0:
                self.label_66.setText("已核验")

            self.gridLayout_4.addWidget(self.label_66, i + 1, 3, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setColumnStretch(2, 3)
        self.gridLayout_4.setColumnStretch(3, 1)
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

        self.pushButton_9.clicked.connect(Form.close)
        self.pushButton_10.clicked.connect(Form.showMinimized)

        Form.setWindowTitle("任务完成详情")
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    def pic_check(self, roomid):
        # 查看图片按钮
        print(roomid)
        print(self.taskid)
        if taskdetail_data.check_complete(str(self.taskid), str(roomid), self.studentcode):
            self.scrollArea_4.findChild(QLabel,"label_" + str(roomid) + "_4").setText("已核验")
            self.New_Window = piccheck_ui.My_Window()
            self.ui = piccheck_ui.Ui_PicCheck(self.New_Window, self.taskid, roomid)
            self.ui.show()
        else:
            self.error = errormessagebox_ui.Ui_ErrorMessageBox("出现错误，请联系管理员")
            self.error.setupUi(QMainWindow())
            self.error.show()
            return False

    def delete_mission(self, roomid):
        print(roomid)
        self.openDialog(roomid)

    def openDialog(self, roomid):
        # 打开Dialog
        new_window = confirmmessagebox_ui.My_Window()
        self.dialog = confirmmessagebox_ui.Ui_ConfirmMessageBox(new_window, "确认打回图片？")
        self.dialog.show()
        # 连接【子窗口自定义消息和主窗口槽函数】
        self.dialog.dialogSignal.connect(functools.partial(self.slot_emit, roomid))

    def slot_emit(self, roomid, flag, msg):
        # print("主窗口：method_2")
        # print(type(flag))
        # print(taskid)
        # print(str)
        if flag == 0:  # 点击ok
            # 执行数据库删除操作
            if taskdetail_data.delete_complete(self.taskid, roomid):
                print("删除成功")
                # 删除任务
                # w=self.gridLayout_3.takeat(1).widget()
                # w.deleteLater()
                self.scrollArea_4.findChild(QLabel, u"label_" + str(roomid) + "_1").deleteLater()
                self.scrollArea_4.findChild(QLabel, u"label_" + str(roomid) + "_2").deleteLater()
                self.scrollArea_4.findChild(QFrame, u"frame_" + str(roomid) + "_1").deleteLater()
                self.scrollArea_4.findChild(QFrame, u"label_" + str(roomid) + "_4").deleteLater()
            else:
                self.error = errormessagebox_ui.Ui_ErrorMessageBox("删除失败")
                self.error.setupUi(QMainWindow())
                self.error.show()
                return False

        else:  # 点击cancel
            # 不进行其他操作
            print("no")

    def retranslateUi(self, Form):
        # setupUi
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(
            QCoreApplication.translate("Form", u"\u4efb\u52a1\u5b8c\u6210\u60c5\u51b5\u4e00\u89c8\u8868", None))
        self.label_63.setText(QCoreApplication.translate("Form", u"\u6700\u65b0\u63d0\u4ea4\u65f6\u95f4", None))
        self.label_64.setText("完成情况")
        self.label_62.setText(QCoreApplication.translate("Form", u"\u5bdd\u5ba4\u53f7", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u67e5\u770b", None))
        self.pushButton_2.setText("打回")
        self.pushButton_10.setText("")
        self.pushButton_9.setText("")

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
    ui = Ui_TaskDetail(RegistWindow)
    RegistWindow.show()
    app.exec()
