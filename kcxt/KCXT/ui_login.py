import wx
import data
import ui_main

class LoginWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)
        # 创建控件
        labelUserID = wx.StaticText(panel, wx.ID_ANY, '用户ID:')
        self.inputTextUserID = wx.TextCtrl(panel, wx.ID_ANY, '001')
        labelPassword = wx.StaticText(panel, wx.ID_ANY, "密码:")
        self.inputTextPassword = wx.TextCtrl(panel, wx.ID_ANY, '123456')

        lblList = ["库存人员", "销售人员", "店长"]
        self.rboxUserType = wx.RadioBox(panel, label="角色", choices=lblList)
        self.rboxUserType.SetSelection(2)  # 默认选择店长人员

        okBtn = wx.Button(panel, wx.ID_ANY, "登录")
        cancelBtn = wx.Button(panel, wx.ID_ANY, "取消")

        topSizer = wx.BoxSizer(wx.VERTICAL)
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = wx.BoxSizer(wx.HORIZONTAL)
        usertypeSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        userSizer.Add(labelUserID, 0, wx.ALL, 5)
        userSizer.Add(self.inputTextUserID, 0, wx.ALL, 5)
        passwordSizer.Add(labelPassword, 0, wx.ALL, 5)
        passwordSizer.Add(self.inputTextPassword, 0, wx.ALL, 5)
        usertypeSizer.Add(self.rboxUserType)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        topSizer.Add(userSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(passwordSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(usertypeSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(topSizer)
        topSizer.Fit(self)
        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.onOk, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

    def onOk(self, e):
        # 事件处理函数:登录确认
        userid = self.inputTextUserID.GetValue()
        password = self.inputTextPassword.GetValue()
        usertype = self.rboxUserType.GetStringSelection()
        if len(userid.strip()) == 0:
            wx.MessageBox("请输入用户ID！")
            self.inputTextUserID.SetFocus()
            return None
        if len(password.strip()) == 0:
            wx.MessageBox("请输入登录密码！")
            self.inputTextPassword.SetFocus()
            return None
        username = data.check_login(userid, password, usertype)
        if not username:
            wx.MessageBox('用户名或密码或角色错误,请重新输入！')
            self.inputTextUserID.SetFocus()
        else:
            self.Close(True)  # 关闭窗口
            title = "库存系统(登录:{0}{1}{2})".format(userid, username, usertype)
            mainFrame = ui_main.MainWindow(None, title, userid, username, usertype)
            mainFrame.Show()  # 显示库存系统主窗口
            mainFrame.Center()  # 窗口居中


    def onCancel(self, e):
        self.Close(True)
