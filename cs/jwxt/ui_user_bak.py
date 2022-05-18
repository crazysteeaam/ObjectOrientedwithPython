import data
import wx
class UserWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)

        #创建控件
        # lblListAction = ['新建', '修改']
        # self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)
        # lblListType = ['教务', '教师', '学生']
        # self.rboxUserType = wx.RadioBox(panel, label='角色', choices=lblListType)

        self.listInfo = wx.ListCtrl(panel, wx.ID_ANY, size=(300, 400), style=wx.LC_REPORT)
        self.listInfo.InsertColumn(0, '用户ID', width=100)
        self.listInfo.InsertColumn(1, '姓名',  width=100)
        self.listInfo.InsertColumn(1, '性别', width=100)
        self.listInfo.InsertColumn(1, '系别', width=100)

        labelUserID = wx.StaticText(panel, wx.ID_ANY, '用户 I D:')
        self.inputTextUserID = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelUserName = wx.StaticText(panel, wx.ID_ANY, '用户姓名:')
        self.inputTextUserName = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelBirthday = wx.StaticText(panel, wx.ID_ANY, '出生年月:')
        self.inputTextBirthday = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelDepartment = wx.StaticText(panel, wx.ID_ANY, '所属院系:')
        self.inputTextDepartment = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelPhone = wx.StaticText(panel, wx.ID_ANY, '电话号码:')
        self.inputTextPhone = wx.TextCtrl(panel, wx.ID_ANY, '')
        lblListGender = ['男', '女']
        self.rboxGender = wx.RadioBox(panel, label='性别', choices=lblListGender)

        okBtn = wx.Button(panel, wx.ID_ANY, '确认')
        cancelBtn = wx.Button(panel, wx.ID_ANY, '取消')
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        # optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        useridSizer = wx.BoxSizer(wx.HORIZONTAL)
        usernameSizer = wx.BoxSizer(wx.HORIZONTAL)
        birthdaySizer = wx.BoxSizer(wx.HORIZONTAL)
        departmentSizer = wx.BoxSizer(wx.HORIZONTAL)
        phoneSizer = wx.BoxSizer(wx.HORIZONTAL)
        genderSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        # optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)
        # optionSizer.Add(self.rboxUserType, 0, wx.ALL, 5)

        listSizer.Add(self.listInfo, 0, wx.ALL, 5)

        useridSizer.Add(labelUserID, 0, wx.ALL, 5)
        useridSizer.Add(self.inputTextUserID, 0, wx.ALL, 5)
        usernameSizer.Add(labelUserName, 0, wx.ALL, 5)
        usernameSizer.Add(self.inputTextUserName, 0, wx.ALL, 5)
        birthdaySizer.Add(labelBirthday, 0, wx.ALL, 5)
        birthdaySizer.Add(self.inputTextBirthday, 0, wx.ALL, 5)
        departmentSizer.Add(labelDepartment, 0, wx.ALL, 5)
        departmentSizer.Add(self.inputTextDepartment, 0, wx.ALL, 5)
        phoneSizer.Add(labelPhone, 0, wx.ALL, 5)
        phoneSizer.Add(self.inputTextPhone, 0, wx.ALL, 5)
        genderSizer.Add(self.rboxGender, 0, wx.ALL, 5)
        btnSizer.Add(okBtn, 0, wx.ALL, 5)
        btnSizer.Add(cancelBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(useridSizer, 0, wx.ALL, 5)
        editSizer.Add(usernameSizer, 0, wx.ALL, 5)
        editSizer.Add(birthdaySizer, 0, wx.ALL, 5)
        editSizer.Add(departmentSizer, 0, wx.ALL, 5)
        editSizer.Add(genderSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)

        # topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件.
        self.Bind(wx.EVT_BUTTON, self.onOk, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        #查询百度音乐频道列表并显示
        # self.populate_channel_list()

    def populate_channel_list(self):
        """查询百度音乐频道列表并显示"""
        # self.channel_list = data.get_channel_list()
        # # items = channel_list.items()
        # index = 0
        # for k in self.channel_list:
        #     self.listChannel.InsertItem(index, k)
        #     self.listChannel.SetItem(index, 1, self.channel_list[k])
        #     index += 1
        pass

    def populate_song_list(self,channel_id,channel_name):
        """查询百度音乐指定频道的歌曲列表并显示"""
        # from_no = int(self.inputTextFrom.GetValue())
        # to_no = int(self.inputTextTo.GetValue())
        # self.song_list = data.get_song_list(channel_id,channel_name,from_no,to_no)
        # # items = channel_list.items()
        # index = 0
        # for k in self.song_list:
        #     self.listSong.InsertItem(index, str(k))
        #     self.listSong.SetItem(index, 1, str(self.song_list[k][0]))
        #     self.listSong.SetItem(index, 2, str(self.song_list[k][2]))
        #     index += 1
        pass

    def onOk(self,e):
        """事件处理函数：显示消息对话框"""
        index = self.listChannel.GetFirstSelected()
        channel_id = self.listChannel.GetItemText(index)
        #查询百度音乐指定频道的歌曲列表并显示
        self.populate_song_list(channel_id,self.channel_list[channel_id])

    def onCancel(self, e):
        """ 事件处理函数：打开文件 """
        self.download_list = []
        index = self.listSong.GetFirstSelected()
        while index != -1:
            song_id = self.listSong.GetItemText(index)
            song_url = self.song_list[song_id][1]
            self.download_list.append([song_id, song_url])
            index = self.listSong.GetNextSelected(index)
        print(self.download_list)

    def onExit(self,e):
        self.Close(True)  # 关闭顶层框架窗口

# class App(wx.App):
#     def OnInit(self):
#         frame = MainWindow(parent=None, title='百度音乐批量下载器')
#         frame.Show()
#         return True
#
# app = App()
# app.MainLoop()