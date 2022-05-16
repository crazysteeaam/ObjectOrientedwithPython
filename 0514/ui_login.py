import data
import ui_main


class LoginWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)
        # 创建控件
        labelUserID = wx.StaticText(panel, wx.ID_ANY, '用户ID:')
        self.inputTextUserID = wx.TextCtrl(panel, wx.ID_ANY, 'S001')
        labelPassword = wx.StaticText(panel, wx.ID_ANY, "密码:")
        self.inputTextPassword = wx.TextCtrl(panel, wx.ID_ANY, '123456')

        lblList = ["教务", "教师", "学生"]
        self.rboxUserType = wx.RadioBox(panel, label="角色", choices=lblList)
        self.rboxUserType.SetSelection(2)  # 默认选择学生

        okBtn = wx.Button(panel, wx.ID_ANY, "登录")
        cancelBtn = wx.Button(panel, wx.ID_ANY, "取消")

        topSizer = wx.BoxSizer(Wx.VERTICAL)
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        passwordSizer = w.BoxSizer(wx.HORIZONTAL)
        usertypeSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        userSizer.Add(labelUserID, 0, wx.ALL, 5)
        userSizer.Add(self.irputTextUserID, O, wx.ALL, 5)
        passwordSizer.Add(labelPassword, 0, wx.ALL, 5)
        passwordSizer.Add(self.irputTextPassword, 0, wx.ALL, 5)
        usertypeSizer.Add(self.rboxluserType)
        btnSizer.Add(okBtn, O, Wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, Wx.ALL, 5)

        topSizer.Add(userSizer, 0, w.ALL | wx.CENTER, 5)
        topSizer.Add(passwordSizer, 0, w.ALL | wx.CENTER, 5)
        topSizer.Add(usertypeSizer, 0, w.ALL | wx.CENTER, 5)
        topSizer.Add(btnsizer, 0, w.ALL | wx.CENTER, 5)
        panel.SetSizer(topSizer)
        topSizer.Fit(self)
        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.onOk, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

    def onOk(self, e):
        # 事件处理函数:登录确认
        userid = self.irputTextUserID.GetValue()
        password = self.inputTextPasswordGetValue()
        usertype = self.rboxUserType.GetStringSelection()
        if len(userid.strip) == 0:
            wx.MessageBox("请输入用户ID！")
            self.inputTextUserID.SetFocus()
            return None
        if len(password.strip()) == 0:
            wx.MessageBox("请输入登录密码！")
            self.inputTextPassword.SetFocus()
            return None
        username = data.check_login(userid, password, usertype)
        if not usermame:
            wx.MessageBox('用户名或密码或角色错误,请重新输入！')
            self.inputTextUserID.SetFocus()
        else:
            self.Close(True)  # 关闭窗口
            title = "教务管理系统(登录:{0]{1}{2])".format(userid, username, usertype)
            mainFrame = ui_main.MainWindow(None, title, userid, username, usertype)
            mainFrame.Show()  # 显示教务管理系统主窗口
            mainFrame.Center()  # 窗口居中
            # mainFrame.userid=userid #保存用户ID到主窗口对象
            # mainFrame.username=username #保存用户姓名到主窗口对象
            # mainFrame.usertype=usertype#保存用户类型到主窗口对象
            # mainFrame.SetTitle(title)

    def onCancel(self, e):
        self.Close(True)
