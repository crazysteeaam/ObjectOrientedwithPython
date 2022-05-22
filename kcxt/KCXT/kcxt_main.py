import wx
import ui_login


class App(wx.App):
    def OnInit(self):
        frame = ui_login.LoginWindow(parent=None, title="系统登陆")
        frame.Show()
        frame.Center()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
