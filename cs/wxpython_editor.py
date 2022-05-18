import os
import wx
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640, 480))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE) #创建多行文本控件
        self.CreateStatusBar()  # 创建状态栏

        # 创建菜单并添加菜单项
        filemenu = wx.Menu()
        helpmenu = wx.Menu()
        # wx.ID_OPEN、wx.ID_SAVE、x.ID_ABOUT、wx.ID_EXIT是标准菜单ID.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "打开")
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "保存")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "退出")
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About", "关于")

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File") # 把菜单"filemenu"添加到菜单栏
        menuBar.Append(helpmenu, "&Help")  # 把菜单"helpmenu"添加到菜单栏
        self.SetMenuBar(menuBar)  # 把菜单栏添加到顶层框架窗口

        # 绑定事件.
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

    def OnAbout(self,e):
        """事件处理函数：显示消息对话框"""
        dlg = wx.MessageDialog( self, "简易文本编辑器V1.0.0\nby Hong Jiang", "简易文本编辑器", wx.OK)
        dlg.ShowModal() # 显示模式对话框
        dlg.Destroy() # 销毁对话框

    def OnExit(self,e):
        self.Close(True)  # 关闭顶层框架窗口

    def OnOpen(self, e):
        """ 事件处理函数：打开文件 """
        self.dirname = ''
        dlg = wx.FileDialog(self, "选择文件", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnSave(self, e):
        """ 事件处理函数：保存文件 """
        self.dirname = ''
        dlg = wx.FileDialog(self, "选择文件", self.dirname, "", "*.*", wx.FD_SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'w')
            f.write(self.control.GetValue())
            f.close()
        dlg.Destroy()

class App(wx.App):
    def OnInit(self):
        frame = MainWindow(parent=None, title='简易文本编辑器')
        frame.Show()
        frame.Center()
        return True

app = App()
app.MainLoop()