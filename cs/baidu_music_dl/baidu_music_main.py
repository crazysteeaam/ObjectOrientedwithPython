import wx
import ui
import data

class MusicDownloadApp(wx.App):
    def OnInit(self):
        data.set_logging()  # 配置日志
        frame = ui.MainWindow(parent=None, title='百度音乐批量下载器')
        frame.Show()
        return True

app = MusicDownloadApp()
app.MainLoop()