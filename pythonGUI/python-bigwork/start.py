import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow
import login_package.login_ui as loginui
import os
import sys

if __name__ == "__main__":
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication([])
    window = loginui.My_Window()
    ui = loginui.Ui_LoginWindow(app, window)
    window.show()
    app.exec()
