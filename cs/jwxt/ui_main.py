import wx
import ui_login
import ui_change_password
import ui_user
import ui_course
import ui_jxb
import ui_student
import ui_teacher

class MainWindow(wx.Frame):
    def __init__(self, parent, title, userid, username, usertype):
        wx.Frame.__init__(self, parent, title=title, size=(640, 480))
        self.CreateStatusBar()  # 创建状态栏
        self.userid = userid
        self.username = username
        self.usertype = usertype

        # 创建菜单并添加菜单项
        sysmenu = wx.Menu() #系统菜单：登录、修改密码、退出
        j_menu = wx.Menu() #教务菜单：用户管理、课程管理、开课管理
        s_menu = wx.Menu()  # 系统菜单：选课、查看成绩
        t_menu = wx.Menu()  #系统菜单：登录成绩
        helpmenu = wx.Menu() #帮助菜单：关于
        # wx.ID_OPEN、wx.ID_SAVE、x.ID_ABOUT、wx.ID_EXIT是标准菜单ID.
        menuLogin = sysmenu.Append(wx.ID_ANY, "重新登录", "重新登录")
        menuChangePassword = sysmenu.Append(wx.ID_ANY, "修改密码", "修改密码")
        menuExit = sysmenu.Append(wx.ID_EXIT, "退出系统", "退出")
        menuUser = j_menu.Append(wx.ID_ANY, "用户管理", "用户管理")
        menuCourse = j_menu.Append(wx.ID_ANY, "课程管理", "课程管理")
        menuJXB = j_menu.Append(wx.ID_ANY, "开课计划", "开课计划")
        menuStudent = s_menu.Append(wx.ID_ANY, "学生选课", "学生选课")
        menuTeacher = t_menu.Append(wx.ID_ANY, "成绩登录", "成绩登录")
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "关于", "关于")

        # 创建菜单栏，根据不同角色，显示不同菜单
        menuBar = wx.MenuBar()
        menuBar.Append(sysmenu, "系统") # 把菜单"sysmenu"添加到菜单栏
        if self.usertype == "教务":
            menuBar.Append(j_menu, "教务")  # 把菜单"j_menu"添加到菜单栏
        elif self.usertype == "学生":
            menuBar.Append(s_menu, "学生")  # 把菜单"s_menu"添加到菜单栏
        elif self.usertype == "教师":
            menuBar.Append(t_menu, "教师")  # 把菜单"t_menu"添加到菜单栏
        menuBar.Append(helpmenu, "帮助")  # 把菜单"helpmenu"添加到菜单栏
        self.SetMenuBar(menuBar)  # 把菜单栏添加到顶层框架窗口

        # 绑定事件.
        self.Bind(wx.EVT_MENU, self.OnLogin, menuLogin)
        self.Bind(wx.EVT_MENU, self.OnChangePassword , menuChangePassword )
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnUser, menuUser)
        self.Bind(wx.EVT_MENU, self.OnCourse, menuCourse)
        self.Bind(wx.EVT_MENU, self.OnJXB, menuJXB)
        self.Bind(wx.EVT_MENU, self.OnStudent, menuStudent)
        self.Bind(wx.EVT_MENU, self.OnTeacher, menuTeacher)

        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)


    def OnAbout(self,e):
        """事件处理函数：显示消息对话框"""
        dlg = wx.MessageDialog( self, "简易教务管理系统V1.0.0\nby Hong Jiang", "简易教务管理系统", wx.OK)
        dlg.ShowModal() # 显示模式对话框
        dlg.Destroy() # 销毁对话框

    def OnExit(self,e):
        self.Close(True)  # 关闭窗口

    def OnLogin(self, e):
        """ 事件处理函数：重新登录 """
        self.Close(True)  # 关闭窗口
        loginFrame = ui_login.LoginWindow(parent=None, title='重新登录')
        loginFrame.Show()  # 显示登录窗口
        loginFrame.Center()  # 窗口居中

    def OnChangePassword(self, e):
        """ 事件处理函数：保存文件 """
        changepasswordFrame = ui_change_password.ChangePasswordWindow(parent=None, title='修改密码')
        changepasswordFrame.Show()  # 显示登录窗口
        changepasswordFrame.Center()  # 窗口居中
        changepasswordFrame.userid  =  self.userid

    def OnUser(self, e):
        """ 事件处理函数：用户管理 """
        userFrame = ui_user.UserWindow(parent=None, title='用户管理')
        userFrame.Show()  # 显示登录窗口
        userFrame.Center()  # 窗口居中

    def OnCourse(self, e):
        """ 事件处理函数：课程管理 """
        courseFrame = ui_course.CourseWindow(parent=None, title='课程管理')
        courseFrame.Show()  # 显示登录窗口
        courseFrame.Center()  # 窗口居中

    def OnJXB(self, e):
        """ 事件处理函数：开课计划 """
        jxbFrame = ui_jxb.JXBWindow(parent=None, title='开课计划')
        jxbFrame.Show()  # 显示登录窗口
        jxbFrame.Center()  # 窗口居中

    def OnStudent(self, e):
        """ 事件处理函数：学生选课 """
        studentFrame = ui_student.StudentWindow(parent=None, title='学生选课', userid=self.userid)
        studentFrame.Show()  # 显示登录窗口
        studentFrame.Center()  # 窗口居中

    def OnTeacher(self, e):
        """ 事件处理函数：教师登录成绩 """
        teacherFrame = ui_teacher.TeacherWindow(parent=None, title='教师登录成绩', userid=self.userid)
        teacherFrame.Show()  # 显示登录窗口
        teacherFrame.Center()  # 窗口居中
