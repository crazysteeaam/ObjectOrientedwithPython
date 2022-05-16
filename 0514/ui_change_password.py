import wx
import data
import ui_main


class ChangePasswordWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)
        # 创建控件
        labelPassword1 = wx.StaticText(panel, wx.ID_ANY, '输入新密码：')
        self.inputTextPassword1 = wx.TextCtrl(panel, wx.ID_ANY, '123456')
        labelPassword2 = wx.StaticText(panel, wx.ID_ANY, '确认新密码：')
        self.inputTextPassword2 = wx.TextCtrl(panel, wx.ID_ANY, '123456')

        okBtn = wx.Button(panel, wx.ID_ANY, '确定')
        cancelBtn = wx.Button(panel, wx.ID_ANY, '取消')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        password1Sizer = wx.BoxSizer(wx.HORIZONTAL)
        password2Sizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        password1Sizer.Add(labelPassword1, 0, wx.ALL, 5)
        password1Sizer.Add(self.inputTextPassword1, 0, wx.ALL, 5)
        password2Sizer.Add(labelPassword2, 0, wx.ALL, 5)
        password2Sizer.Add(self.inputTextPassword2, 0, wx.ALL, 5)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        topSizer.Add(password1Sizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(password2Sizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.onOk, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

    def onOk(self, e):
        """事件处理函数：登陆确认"""
        password1 = self.inputTextPassword1.GetValue()
        password2 = self.inputTextPassword2.GetValue()
        if len(password1.strip()) == 0:
            wx.MessageBox('请输入新密码!')
            self.inputTextPassword1.SetFocus()
            return None
        if password1 != password2:
            wx.MessageBox('两次输入的新密码不一致！')
            self.inputTextPassword2.SetFocus()
            return None
        data.change_password(self.userid, password1)  # 调用data模块的方法，修改密码
        self.Close(True)  # 关闭窗口

    def onCancel(self, e):
        self.Close(True)  # 关闭窗口
