import data
import wx
class StudentWindow(wx.Dialog):
    def __init__(self, parent, title, userid):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.userid = userid
        panel = wx.Panel(self, wx.ID_ANY)

        #创建控件
        lblListAction = ['选课', '退选']
        self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)

        self.listGrade = wx.ListCtrl(panel, wx.ID_ANY, size=(550, 400), style=wx.LC_REPORT)
        self.listGrade.InsertColumn(0, '教学班号', width=80)
        self.listGrade.InsertColumn(1, '课程ID',  width=50)
        self.listGrade.InsertColumn(2, '课程名称',  width=100)
        self.listGrade.InsertColumn(3, '教师ID',  width=50)
        self.listGrade.InsertColumn(4, '教师姓名',  width=100)
        self.listGrade.InsertColumn(5, '时间地点',  width=120)
        self.listGrade.InsertColumn(6, '成绩', width=50)

        labelJxbID = wx.StaticText(panel, wx.ID_ANY, '教学班号:')
        self.inputTextJxbID = wx.TextCtrl(panel, wx.ID_ANY, '', style=wx.TE_PROCESS_ENTER)
        labelCourseID = wx.StaticText(panel, wx.ID_ANY, '课程ＩＤ:')
        self.inputTextCourseID = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextCourseID.Disable()
        self.inputTextCourseName = wx.TextCtrl(panel, wx.ID_ANY, '') #课程名称
        self.inputTextCourseName.Disable()
        labelUserID = wx.StaticText(panel, wx.ID_ANY, '教师ＩＤ:')
        self.inputTextUserID = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextUserID.Disable()
        self.inputTextUserName = wx.TextCtrl(panel, wx.ID_ANY, '')  #教师姓名
        self.inputTextUserName.Disable()
        labelDescription = wx.StaticText(panel, wx.ID_ANY, '时间地点:')
        self.inputTextDescription = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextDescription.Disable()
        labelScore = wx.StaticText(panel, wx.ID_ANY, '学生成绩:')
        self.inputTextScore = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextScore.Disable()

        self.insertBtn = wx.Button(panel, wx.ID_ANY, '选课')
        self.deleteBtn = wx.Button(panel, wx.ID_ANY, '退选')
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
        scoreSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)

        listSizer.Add(self.listGrade, 0, wx.ALL, 5)

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
        scoreSizer.Add(labelScore, 0, wx.ALL, 5)
        scoreSizer.Add(self.inputTextScore, 0, wx.ALL, 5)
        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(jxbSizer, 0, wx.ALL, 5)
        editSizer.Add(courseSizer, 0, wx.ALL, 5)
        editSizer.Add(userSizer, 0, wx.ALL, 5)
        editSizer.Add(descriptionSizer, 0, wx.ALL, 5)
        editSizer.Add(scoreSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        #绑定事件.
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onGradeList, self.listGrade)
        self.Bind(wx.EVT_TEXT_ENTER, self.onJxbID, self.inputTextJxbID)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        #查询课程信息并显示
        self.populate_course_list("选课")

    def populate_course_list(self, action):
        """查询选课信息并显示"""
        grade_list = data.get_grade_list_by_student(self.userid, action)
        self.listGrade.DeleteAllItems()
        index = 0
        for grade in grade_list:
            self.listGrade.InsertItem(index, grade[0])
            self.listGrade.SetItem(index, 1, grade[1])
            self.listGrade.SetItem(index, 2, grade[2])
            self.listGrade.SetItem(index, 3, grade[3])
            self.listGrade.SetItem(index, 4, grade[4])
            self.listGrade.SetItem(index, 5, grade[5])
            self.listGrade.SetItem(index, 6, str(grade[6]))
            index += 1

    def onAction(self, e):
        """事情处理函数：根据操作类型（插入、更新、删除）设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "选课":
            self.inputTextJxbID.Enable()
            self.insertBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "退选":
            self.inputTextJxbID.Disable()
            self.insertBtn.Disable()
            self.deleteBtn.Enable()
        self.populate_course_list(action)

    def onGradeList(self,e):
        """事件处理函数：在列表中选择课程，内容显示在右侧"""
        index = e.GetIndex() #获得被激活表项的索引号
        self.inputTextJxbID.SetValue(self.listGrade.GetItem(index, 0).GetText())
        self.inputTextCourseID.SetValue(self.listGrade.GetItem(index, 1).GetText())
        self.inputTextCourseName.SetValue(self.listGrade.GetItem(index, 2).GetText())
        self.inputTextUserID.SetValue(self.listGrade.GetItem(index, 3).GetText())
        self.inputTextUserName.SetValue(self.listGrade.GetItem(index, 4).GetText())
        self.inputTextDescription.SetValue(self.listGrade.GetItem(index, 5).GetText())
        self.inputTextScore.SetValue(self.listGrade.GetItem(index, 6).GetText())

    def onJxbID(self, e):
        """事件处理函数，输入教学班号时检查其存在，并显示相关内容"""
        jxbid = self.inputTextJxbID.GetValue()
        if len(jxbid.strip()) == 0:
            return None
        if data.check_jxb_id(jxbid):
            courseid, coursename, userid, username, description = data.check_jxb_id(jxbid)
            self.inputTextCourseID.SetValue(courseid)
            self.inputTextCourseName.SetValue(coursename)
            self.inputTextUserID.SetValue(userid)
            self.inputTextUserName.SetValue(username)
            self.inputTextDescription.SetValue(description)
        else:
            wx.MessageBox("该课程计划不存在！")
            self.inputTextCourseID.SetFocus()
            return None

    def onInsert(self,e):
        """事件处理函数：插入一条记录"""
        jxbid = self.inputTextJxbID.GetValue()
        if len(jxbid.strip()) == 0:
            wx.MessageBox('请输入教学班号！')
            self.inputTextJxbID.SetFocus()
            return None
        if data.check_grade_id(jxbid, self.userid):
            wx.MessageBox("该课已经选，不能重复选课！")
            self.inputTextJxbID.SetFocus()
            return None
        #插入记录
        data.insert_grade(jxbid, self.userid)
        #初始化界面
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
        action = self.rboxAction.GetStringSelection()
        self.populate_course_list(action)

    def onDelete(self, e):
        """事件处理函数：删除一条记录"""
        jxbid = self.inputTextJxbID.GetValue()
        #删除记录
        data.delete_grade(jxbid, self.userid)
        #初始化界面
        self.refresh_screen()

    def onExit(self,e):
        self.Close(True)  # 关闭顶层框架窗口
