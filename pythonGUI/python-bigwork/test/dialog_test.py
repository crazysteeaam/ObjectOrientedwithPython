# 窗口之间数据传递（通过属性方式）
from PyQt5.QtWidgets import QDialogButtonBox, QDateTimeEdit, QDialog, QComboBox, QTableView, QAbstractItemView, \
    QHeaderView, QTableWidget, QTableWidgetItem, QMessageBox, QListWidget, QListWidgetItem, QStatusBar, QMenuBar, QMenu, \
    QAction, QLineEdit, QStyle, QFormLayout, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QPushButton, QMainWindow, \
    QGridLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel, QCursor, QFont, QBrush, QColor, QPainter, \
    QMouseEvent, QImage, QTransform
from PyQt5.QtCore import QStringListModel, QAbstractListModel, QModelIndex, QSize, Qt, QObject, pyqtSignal, QTimer, \
    QEvent, QDateTime, QDate

import sys


class Win(QWidget):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.resize(400, 400)

        self.btn = QPushButton("按钮", self)
        self.btn.move(50, 50)
        self.btn.setMinimumWidth(120)
        self.btn.clicked.connect(self.openDialog)

        # 显示子窗口传来的日期字符串或者其他数据
        self.label = QLabel('这里显示信息', self)
        self.label.setMinimumWidth(420)

    # 打开Dialog
    def openDialog(self):
        dialog = Dialog(self)
        # 连接【子窗口内置消息和主窗口的槽函数】
        dialog.datetime.dateChanged.connect(self.slot_inner)
        # 连接【子窗口自定义消息和主窗口槽函数】
        dialog.dialogSignel.connect(self.slot_emit)
        dialog.show()

    def slot_inner(self, date):
        print("主窗口：method_1")
        self.label.setText("①" + str(date) + ">>内置消息获取日期为")

    def slot_emit(self, flag, str):
        print("主窗口：method_2")
        print(flag)
        if flag == "0":  # 点击ok
            self.label.setText("②" + str(str) + ">>自定义消息")
        else:  # 点击cancel
            self.label.setText(str)


# 弹出框对象
class Dialog(QDialog):
    # 自定义消息
    dialogSignel = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())
        self.label.setText("请选择日期")
        layout.addWidget(self.label)
        layout.addWidget(self.datetime)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)  # 点击ok
        buttons.rejected.connect(self.reject)  # 点击cancel
        layout.addWidget(buttons)

    def accept(self):  # 点击ok是发送内置信号
        print("accept")
        self.dialogSignel.emit(0, self.datetime.text())
        self.destroy()

    def reject(self):  # 点击cancel时，发送自定义信号
        print('reject')
        self.dialogSignel.emit(1, "清空")
        self.destroy()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec_())
