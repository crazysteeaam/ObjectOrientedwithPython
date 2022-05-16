import data
import wx


class CourseWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        panel = wx.Panel(self, wx.ID_ANY)

        # 创建控件
        lblListAction = ['插入', '修改', '删除']
        self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)

        self.listCourse = wx.ListCtrl(panel, wx.ID_ANY, size = (400, 400), style = wx.LC_REPORT)
        self.listCourse.InsertColumn(0, '课程ID', width = 50)
        self.listCourse.InsertColumn(1, '课程名称', width=100)
        self.listCourse.InsertColumn(2, '学分', width=50)
        self.listCourse.InsertColumn(3, '说明', width=200)
        labelCourseID = wx.StaticText(panel, wx.ID_ANY, '课程ID:')
        self.inputTextCourseID = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelCourseName = wx.StaticText(panel, wx.ID_ANY, '课程名称:')
        self.inputTextCourseName = wx.TextCtrl(panel, wx.ID_ANY, '' )
        labelCredit = wx.StaticText(panel, wx.ID_ANY, '课程学分:')
        self.inputTextCredit = wx.TextCtrl(panel, wx.ID_ANY,'')
        labelDescription = wx.StaticText(panel, wx.ID_ANY, '课程说明:')
        self.inputTextDescription = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.insertBtn = wx.Button(panel, wx.ID_ANY,'插入')
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
        courseidSizer = wx.BoxSizer(wx.HORIZONTAL)
        coursenameSizer = wx.BoxSizer(wx.HORIZONTAL)
        creditSizer = wx.BoxSizer(wx.HORIZONTAL)
        descriptionSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)

        listSizer.Add(self.listCourse, 0, wx.ALL, 5)

        courseidSizer.Add(labelCourseID, 0, wx.ALL, 5)
        courseidSizer.Add(self.inputTextCourseID, 0, wx.ALL, 5)
        coursenameSizer.Add(labelCourseName, 0, wx.ALL, 5)
        coursenameSizer.Add(self.inputTextCourseName, 0, wx.ALL, 5)
        creditSizer.Add(labelCredit, 0, wx.ALL, 5)
        creditSizer.Add(self.inputTextCredit, 0, wx.ALL, 5)
        descriptionSizer.Add(labelDescription, 0, wx.ALL, 5)
        descriptionSizer.Add(self.inputTextDescription, 0, wx.ALL, 5)
        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(courseidSizer, 0, wx.ALL, 5)
        editSizer.Add(coursenameSizer, 0, wx.ALL, 5)
        editSizer.Add(creditSizer, 0, wx.ALL, 5)
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
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onCourseList, self.listCourse)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        # 查询课程信息并显示
        self.populate_course_list()

    def populate_course_list(self):
        """查询课程信息并显示"""
        course_list = data.get_course_list()
        self.listCourse.DeleteAllItems()
        index = 0
        for course in course_list:
            self.listCourse.InsertItem(index, course[0])
            self.listCourse.SetItem(index, 1, course[1])
            self.listCourse.SetItem(index, 2, str(course[2]))
            self.listCourse.SetItem(index, 3, course[3])
            index += 1

    def onAction(self, e):
        """事情处理函数:根据操作类型(插入、更新、删除)设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "插入":
            self.inputTextCourseID.Enable()
            self.insertBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
        elif action == "修改":
            self.inputTextCourseID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "删除":
            self.inputTextCourseID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()

    def onCourseList(self, e):
        """事件处理函数:在列表中选择课程，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        self.inputTextCourseID.SetValue(self.listCourse.GetItem(index, 0).GetText())
        self.inputTextCourseName.SetValue(self.listCourse.GetItem(index, 1).GetText())
        self.inputTextCredit.SetValue(self.listCourse.GetItem(index, 2).GetText())
        self.inputTextDescription.SetValue(self.listCourse.GetItem(index, 3).GetText())

    def onInsert(self, e):
        """事件处理函数: 插入一条记录"""
        courseid = self.inputTextCourseID.GetValue()
        coursename = self.inputTextCourseName.GetValue()
        credit = int(self.inputTextCredit.GetValue())
        description = self.inputTextDescription.GetValue()
        if len(courseid.strip()) == 0:
            wx.MessageBox('请输入课程ID!')
            self.inputTextCourseID.SetFocus()
            return None
        if len(coursename.strip()) == 0:
            wx.MessageBox('请输入课程名称!')
            self.inputTextCourseName.SetFocus()
            return None
        if data.check_course_id(courseid):
            wx.MessageBox("该课程己经存在!")
            self.inputTextCourseID.SetFocus()
            return None
        # 插入记录
        data.insert_course(courseid, coursename, credit, description)
        # 初始化界面
        self.refresh_screen()

    def refresh_screen(self):
        """重新刷新界面"""
        self.inputTextCourseID.SetValue('')
        self.inputTextCourseName.SetValue('')
        self.inputTextCredit.SetValue('')
        self.inputTextDescription.SetValue('')
        # 查询课程信息并显示
        self.populate_course_list()

    def onUpdate(self, e):
        """事件处理函数: 更新一条记录"""
        courseid = self.inputTextCourseID.GetValue()
        coursename = self.inputTextCourseName.GetValue()
        credit = int(self.inputTextCredit.GetValue())
        description = self.inputTextDescription.GetValue()
        if len(coursename.strip()) == 0:
            wx.MessageBox('请输入课程名称!')
            self.inputTextCourseName.SetFocus()
            return None
        # 更新记录
        data.update_course(courseid, coursename, credit, description)
        # 初始化界面
        self.refresh_screen()

    def onDelete(self, e):
        """事件处理函数:删除一条记录"""
        courseid = self.inputTextCourseID.GetValue()
        # 删除记录
        data.delete_course(courseid)
        # 初始化界面
        self.refresh_screen()

    def onExit(self, e):
        self.Close(True)  # 关闭顶层框架窗口



