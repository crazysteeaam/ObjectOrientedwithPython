import data
import wx


class JXBWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)

        # 创建控件
        lblListAction = ['插入', '修改', '删除']
        self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)

        self.listJXB = wx.ListCtrl(panel, wx.ID_ANY, size=(450, 400), style=wx.LC_REPORT)
        self.listJXB.InsertColumn(0, '教学班号', width=50)
        self.listJXB.InsertColumn(1, '课程ID', width=50)
        self.listJXB.InsertColumn(2, '课程名称', width=100)
        self.listJXB.InsertColumn(3, '教师ID', width=50)
        self.listJXB.InsertColumn(4, '教师姓名', width=100)
        self.listJXB.InsertColumn(5, '时间地点', width=100)

        labelJxbID = wx.StaticText(panel, wx.ID_ANY, '教学班号:')
        self.inputTextJxbID = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelCourseID = wx.StaticText(panel, wx.ID_ANY, '课程ID:')
        self.inputTextCourseID = wx.TextCtrl(panel, wx.ID_ANY, '', style=wx.TE_PROCESS_ENTER)
        self.inputTextCourseName = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextCourseName.Disable()
        labelUserID = wx.StaticText(panel, wx.ID_ANY, '教师ID:')
        self.inputTextUserID = wx.TextCtrl(panel, wx.ID_ANY, '', style=wx.TE_PROCESS_ENTER)
        self.inputTextUserName = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextUserName.Disable()
        labelDescription = wx.StaticText(panel, wx.ID_ANY, '时间地点:')
        self.inputTextDescription = wx.TextCtrl(panel, wx.ID_ANY, '')

        self.insertBtn = wx.Button(panel, wx.ID_ANY, '插入')
        self.updateBtn = wx.Button(panel, wx.ID_ANY, '更新')
        self.updateBtn.Disable()
        self.deleteBtn = wx.Button(panel, wx.ID_ANY, '删除')
        self.deleteBtn.Disable()
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        jxbSizer = wx.BoxSizer(wx.HORIZONTAL)
        courseSizer = wx.BoxSizer(wx.HORIZONTAL)
        userSizer = wx.BoxSizer(wx.HORIZONTAL)
        descriptionSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)
        listSizer.Add(self.listJXB, 0, wx.ALL, 5)

        jxbSizer.Add(labelJxbID, 0, wx.ALL, 5)
        jxbSizer.Add(self.inputTextJxbID, 0, wx.ALL, 5)
        courseSizer.Add(labelCourseID, 0, wx.ALL, 5)
        courseSizer.Add(self.inputTextCourseID, 0, wx.ALL, 5)
        courseSizer.Add(self.inputTextCourseName, 0, wx.ALL, 5)
        userSizer.Add(labelUserID, 0, wx.ALL, 5)
        userSizer.Add(self.inputTextUserID, 0, wx.ALL, 5)
        userSizer.Add(self.inputTextUserName, 0, wx.ALL, 5)
        descriptionSizer.Add(labelDescription, 0, wx.ALL, 5)
        descriptionSizer.Add(self.inputTextDescription, 0, wx.ALL, 5)

        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(jxbSizer, 0, wx.ALL, 5)
        editSizer.Add(courseSizer, 0, wx.ALL, 5)
        editSizer.Add(userSizer, 0, wx.ALL, 5)
        editSizer.Add(descriptionSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)
        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(topSizer)
        topSizer.Fit(self)
        # 绑定事件
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onJXBList, self.listJXB)
        self.Bind(wx.EVT_TEXT_ENTER, self.onCourseID, self.inputTextCourseID)
        self.Bind(wx.EVT_TEXT_ENTER, self.onUserID, self.inputTextUserID)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)
        # 查询课程信息并显示
        self.populate_course_list()

    def populate_course_list(self):
        """查询开课信息JXB并显示"""
        jxb_list = data.get_jxb_list()
        self.listJXB.DeleteAllItems()
        index = 0
        for jxb in jxb_list:
            self.listJXB.InsertItem(index, jxb[0])
            self.lisLJXB.SetItem(index, 1, jxb[1])
            self.listJXB.SetItem(index, 2, jxb[2])
            self.listJXB.SetItem(index, 3, jxb[3])
            self.listJXB.SetItem(index, 4, jxb[4])
            self.listJXB.SetItem(index, 5, jxb[5])
            index += 1

    def onAction(self, e):
        """事情处理函数:根据操作类型（插入、更新、删除）设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "插入":
            self.inputTextJxbID.Enable()
            self.insertBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
        elif action == "修改":
            self.inputTextJxbID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "删除":
            self.inputTextJxbID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()

    def onJXBList(self, e):
        """事件处理函数:在列表中选择教学班号课程，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        self.inputTextJxbID.SetValue(self.listJXB.GetItem(index, 0).GetText())
        self.inputTextCourseID.SetValue(self.listJXB.GetItem(index, 1).GetText())
        self.inputTextCourseName.SetValue(self.listJXB.GetItem(index, 2).GetText())
        self.inputTextUserID.SetValue(self.listJXB.GetItem(index, 3).GetText())
        self.inputTextUserName.SetValue(self.listJXB.GetItem(index, 4).GetText())
        self.inputTextDescription.SetValue(self.listJXB.GetItem(index, 5).GetText())

    def onCourseID(self, e):
        """事件处理函数，输入课程ID时检查其存在，并显示名称"""
        courseid = self.inputTextCourseID.GetValue()
        if len(courseid.strip()) == 0:
            return None
        coursename = data.check_course_id(courseid)
        if coursename:
            self.inputTextCourseName.SetValue(coursename)
        else:
            wx.MessageBox("该课程不存在!")
            self.inputTextCourseID.SetFocus()
            return None

    def onUserID(self, e):
        """事件处理函数，输入教师ID时检查其存在，并显示名称"""
        userid = self.inputTextUserID.GetValue()
        if len(userid.strip()) == 0:
            return None
        username = data.check_user_id(userid)
        if username:
            self.inputTextUserName.SetValue(username)
        else:
            wx.MessageBox("该教师不存在! ")
            self.inputTextUserID.SetFocus()
            return None

    def onInsert(self, e):
        """事件处理函数:插入一条记录"""
        jxbid = self.inputTextJxbID.GetValue()
        courseid = self.inputTextCourseID.GetValue()
        userid = self.inputTextUserID.GetValue()
        description = self.inputTextDescription.GetValue()
        if len(jxbid.strip()) == 0:
            wx.MessageBox('请输入教学班号! ')
            self.inputTextJxbID.SetFocus()
            return None
        if len(courseid.strip()) == 0:
            wx.MessageBox('请输入课程ID! ')
            self.inputTextCourseID.SetFocus()
            return None
        if len(userid.strip()) == 0:
            wx.MessageBox('请输入教师ID! ')
            self.inputTextUserID.SetFocus()
            return None
        if data.check_jxb_id(jxbid):
            wx.MessageBox("该教学班号已经存在!")
            self.inputText.JxbID.SetFocus()
            return None
        if not data.check_course_id(courseid):
            wx.MessageBox("该课程不存在! ")
            self.inputTextCourseID.SetFocus()
            return None
        if not data.check_user_id(userid):
            wx.MessageBox("该教师不存在!")
            self.inputTextUserID.SetFocus()
            return None
        # 插入记录
        data.insert_jxb(jxbid, courseid, userid, description)
        # 初始化界面
        self.refresh_screen()

    def refresh_screen(self):
        """重新刷新界面"""
        self.inputTextJxbID.SetValue('')
        self.inputTextCourseID.SetValue('')
        self.inputTextCourseName.SetValue('')
        self.inputTextCourseID.SetValue('')
        self.inputTextUserID.SetValue('')
        self.inputTextUserName.SetValue('')
        self.inputTextDescription.SetValue('')
        # 查询课程信息并显示
        self.populate_course_list()

    def onUpdate(self, e):
        """事件处理函数:更新一条记录"""
        jxbid = self.inputTextJxbID.GetValue()
        courseid = self.inputTextCourseID.GetValue()
        userid = self.inputTextUserID.GetValue()
        description = self.inputTextDescription.GetValue()
        if len(courseid.strip()) == 0:
            wx.MessageBox('请输入课程ID! ')
            self.inputTextCourseID.SetFocus()
            return None
        if len(userid.strip()) == 0:
            wx.MessageBox('请输入教师ID! ')
            self.inputTextUserID.SetFocus()
            return None
        if not data.check_course_id(courseid):
            wx.MessageBox("该课程不存在! ")
            self.inputTextCourseID.SetFocus()
            return None

        if not data.check_user_id(userid):
            wx.MessageBox("该教师不存在!")
            self.inputTextUserID.SetFocus()
            return None
        # 更新记录
        data.update_jxb(jxbid, courseid, userid, description)
        # 初始化界面
        self.refresh_screen()

    def onDelete(self, e):
        """事件处理函数:删除一条记录"""
        jxbid = self.inputTextJxbID.GetValue()
        # 删除记录
        data.delete_jxb(jxbid)
        # 初始化界面
        self.refresh_screen()

    def onExit(self, e):
        self.Close(True)  # 关闭顶层框架窗口
