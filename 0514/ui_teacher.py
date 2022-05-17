import data
import wx
import wx.lib.mixins.listctrl as listmix


class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.TextEditMixin.__init__(self)
        self.__canEditList = []

    def OpenEditor(self, col, row):
        if col == 4:
            listmix.TextEditMixin.OpenEditor(self, col, row)
        else:
            pass


class TeacherWindow(wx.Dialog):
    def __init__(self, parent, title, userid):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.userid = userid
        panel = wx.Panel(self, wx.ID_ANY)

        # 创建控件
        self.listGrade = EditableListCtrl(panel, wx.ID_ANY, size=(600, 400),
                                          style=wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        self.listGrade.InsertColumn(0, '学生学号', width=100)
        self.listGrade.InsertColumn(1, '学生姓名', width=150)
        self.listGrade.InsertColumn(2, '性别', width=100)
        self.listGrade.InsertColumn(3, '所在院系', width=150)
        self.listGrade.InsertColumn(6, '成绩', width=100)

        labelJxbID = wx.StaticText(panel, wx.ID_ANY, '教学班号:')
        # self.inputTextJxbID = wx.TextCtrl(panel, wx.ID_ANY, '', style=wx.TE_PROCESS_ENTER)
        self.comBoxJxbID = wx.ComboBox(panel, wx.ID_ANY, '', style=wx.CB_READONLY)
        labelCourseID = wx.StaticText(panel, wx.ID_ANY, '课程:')
        self.inputTextCourseID = wx.TextCtrl(panel, wx.ID_ANY, '', size=(50, 25))
        self.inputTextCourseID.Disable()
        self.inputTextCourseName = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextCourseName.Disable()
        labelDescription = wx.StaticText(panel, wx.ID_ANY, '时间地点:')
        self.inputTextDescription = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.inputTextDescription.Disable()

        self.updateBtn = wx.Button(panel, wx.ID_ANY, '成绩登录')
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        listSizer.Add(self.listGrade, 0, wx.ALL, 5)

        editSizer.Add(labelJxbID, 0, wx.ALL, 5)
        editSizer.Add(self.comBoxJxbID, 0, wx.ALL, 5)
        editSizer.Add(labelCourseID, 0, wx.ALL, 5)
        editSizer.Add(self.inputTextCourseID, 0, wx.ALL, 5)
        editSizer.Add(self.inputTextCourseName, 0, wx.ALL, 5)
        editSizer.Add(labelDescription, 0, wx.ALL, 5)
        editSizer.Add(self.inputTextDescription, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        topSizer.Add(editSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(listSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.Bind(wx.EVT_COMBOBOX, self.onJxbID, self.comBoxJxbID)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        jxbId_list = data.get_jxbid_list_by_user(self.userid)
        self.comBoxJxbID.Set(jxbId_list)

    def populate_grade_list(self):
        """查询开课信息并显示"""
        jxbid = self.comBoxJxbID.GetValue()
        grade_list = data.get_grade_list_by_jxbid(jxbid)
        self.listGrade.DeleteAllItems()
        index = 0
        for grade in grade_list:
            self.listGrade.InsertItem(index, grade[0])
            self.listGrade.SetItem(index, 1, grade[1])
            self.listGrade.SetItem(index, 2, grade[2])
            self.listGrade.SetItem(index, 3, grade[3])
            if not grade[4]:
                self.listGrade.SetItem(index, 4, "")
            else:
                self.listGrade.SetItem(index, 4, str(grade[4]))
            index += 1

    def onAction(self, e):
        """事情处理函数:根据操作类型（插入、更新、删除）设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "选课":
            self.inputTextJxbID.Enable()
            self.insertBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "退选":
            self.inputTextJxbID.Disable()
            self.insertBtn.Disable()
            self.deleteBtn.Enable()

    def onJxbID(self, e):
        """事件处理函数，输入课程ID时检查其存在，并显示名称"""
        jxbid = self.comBoxJxbID.GetValue()
        if data.check_jxb_id(jxbid):
            courseid, coursename, userid, username, description = data.check_jxb_id(jxbid)
            self.inputTextCourseID.SetValue(courseid)
            self.inputTextCourseName.SetValue(coursename)
            self.inputTextDescription.SetValue(description)
            self.populate_grade_list()
        else:
            wx.MessageBox("该课程计划不存在!")
            self.inputTextCourseID.SetFocus()
            return None

    def onUpdate(self, e):
        """事件处理函数:更新一条记录"""
        jxbid = self.comBoxJxbID.GetValue()
        if len(jxbid.strip()) == 0:
            wx.MessageBox("请选择教学班号登录成绩!")
            self.comBoxJxbID.SetFocus()
            return None
        grade_list = []
        for index in range(self.listGrade.GetItemCount()):
            userid = self.listGrade.GetItem(index, 0).GetText()
            try:
                score = int(self.listGrade.GetItem(index, 4).GetText())
            except:
                score = 0
            grade_list.append([score, jxbid, userid])
        data.update_grade_score(grade_list)
        wx.MessageBox("成绩登录成功!")

    def onExit(self, e):
        self.Close(True)
