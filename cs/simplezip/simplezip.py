import wx
import ui

class App(wx.App):
    def OnInit(self):
        frame = ui.MainWindow(parent=None, title='简易压缩软件')
        frame.Show()
        frame.Center()  #窗口居中
        return True

app = App()
app.MainLoop()
