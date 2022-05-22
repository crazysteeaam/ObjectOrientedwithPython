import wx
import ui_login
import ui_change_password
import ui_user
import ui_good
import ui_shelf
import ui_order
import ui_goodinfo


class MainWindow(wx.Frame):
    def __init__(self, parent, title, userid, username, usertype):
        wx.Frame.__init__(self, parent, title=title, size=(640, 480))
        self.CreateStatusBar()  # 创建状态栏
        self.panel = wx.Panel(self, -1)
        self.userid = userid
        self.username = username
        self.usertype = usertype
        font1 = wx.Font(40, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u'Comic Sans MS')
        # 创建菜单并添加菜单项
        sysmenu = wx.Menu()  # 系统菜单:登录、修改密码、退出
        k_menu = wx.Menu()  # 库存人员菜单:商品管理，货架管理
        x_menu = wx.Menu()  # 销售人员菜单:商品信息，订单管理
        d_menu = wx.Menu()  # 店长菜单:人员管理
        helpmenu = wx.Menu()  # 帮助菜单:关于
        # wX.ID_OPEN、WX.ID_SAVE、x.ID_ABOUT、WX.ID_EXIT是标准菜单ID.
        menuLogin = sysmenu.Append(wx.ID_ANY, "重新登录", "重新登录")
        menuChangePassword = sysmenu.Append(wx.ID_ANY, "修改密码", "修改密码")
        menuExit = sysmenu.Append(wx.ID_EXIT, "退出系统", "退出")

        menuUser = d_menu.Append(wx.ID_ANY, "人员管理", "人员管理")

        menuGood = k_menu.Append(wx.ID_ANY, "商品管理", "商品管理")
        menushelf = k_menu.Append(wx.ID_ANY, "货架管理", "货架管理")

        menugoodinfo = x_menu.Append(wx.ID_ANY, "商品信息", "商品信息")
        menuorder = x_menu.Append(wx.ID_ANY, "订单管理", "订单管理")

        menuAbout = helpmenu.Append(wx.ID_ABOUT, "关于", "关于")

        # 创建菜单栏,根据不同角色,显示不同菜单
        menuBar = wx.MenuBar()
        menuBar.Append(sysmenu, "系统")  # 把菜单"sysmenu"添加到菜单栏
        if self.usertype == "库存人员":
            menuBar.Append(k_menu, "库存信息")  # 把菜单"k_menu"添加到菜单栏
            # 控件
            labelgoodID = wx.StaticText(self.panel, wx.ID_ANY, '   库存管理', size=(400, 350),pos=(100,120))
            labelgoodID.SetFont(font1)
            labelgoodID.SetForegroundColour('pink')
            labelgoodID.SetBackgroundColour('')
            topSizer = wx.BoxSizer(wx.VERTICAL)
            contentSizer = wx.BoxSizer(wx.HORIZONTAL)
            contentSizer.Add(labelgoodID, 1,wx.ALL, 0)
            topSizer.Add(contentSizer, 0,wx.ALIGN_CENTRE_HORIZONTAL, 0)
            self.panel.SetSizer(topSizer)
            topSizer.Fit(self)
        elif self.usertype == "销售人员":
            menuBar.Append(x_menu, "销售信息")  # 把菜单"x_menu"添加到菜单栏
            # 控件
            labelgoodID = wx.StaticText(self.panel, wx.ID_ANY, '    销售系统', size=(400, 350),pos=(100,120))
            labelgoodID.SetFont(font1)
            labelgoodID.SetForegroundColour('pink')
            labelgoodID.SetBackgroundColour('')
            topSizer = wx.BoxSizer(wx.VERTICAL)
            contentSizer = wx.BoxSizer(wx.HORIZONTAL)
            contentSizer.Add(labelgoodID, 0,wx.ALL, 0)
            topSizer.Add(contentSizer, 0,wx.ALIGN_CENTRE_HORIZONTAL, 0)
            self.panel.SetSizer(topSizer)
            topSizer.Fit(self)
        elif self.usertype == "店长":
            menuBar.Append(d_menu, "人员管理")  # 把菜单"d_menu"添加到菜单栏
            # 控件
            labelgoodID = wx.StaticText(self.panel, wx.ID_ANY, '    欢迎店长', size=(400, 350),pos=(100,120))
            labelgoodID.SetFont(font1)
            labelgoodID.SetForegroundColour('pink')
            labelgoodID.SetBackgroundColour('')
            topSizer = wx.BoxSizer(wx.VERTICAL)
            contentSizer = wx.BoxSizer(wx.HORIZONTAL)
            contentSizer.Add(labelgoodID, 0,wx.ALL, 0)
            topSizer.Add(contentSizer, 0,wx.ALIGN_CENTRE_HORIZONTAL, 0)
            self.panel.SetSizer(topSizer)
            topSizer.Fit(self)

        menuBar.Append(helpmenu, "帮助")  # 把菜单"helpmenu"添加到菜单栏
        self.SetMenuBar(menuBar)  # 把菜单栏添加到顶层框架窗口
        # 绑定事件.
        self.Bind(wx.EVT_MENU, self.OnLogin, menuLogin)
        self.Bind(wx.EVT_MENU, self.OnChangePassword, menuChangePassword)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnUser, menuUser)
        self.Bind(wx.EVT_MENU, self.Ongood, menuGood)
        self.Bind(wx.EVT_MENU, self.Onshelf, menushelf)
        self.Bind(wx.EVT_MENU, self.Ongoodinfo, menugoodinfo)
        self.Bind(wx.EVT_MENU, self.Onorder, menuorder)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)

    def OnAbout(self, e):
        # 事件处理函数:显示消息对话框。
        dlg = wx.MessageDialog(self, "库存管理系统V1.0.0\nby", "库存管理系统", wx.OK)
        dlg.ShowModal()  # 显示模式对话框
        dlg.Destroy()  # 销毁对话框


    def OnExit(self, e):
        self.Close(True)  # 关闭窗口

    def OnLogin(self, e):
        # 事件处理函数:重新登录
        self.Close(True)  # 关闭窗口
        loginFrame = ui_login.LoginWindow(parent=None, title="重新登录")
        loginFrame.Show()  # 显示登录窗口
        loginFrame.Center()  # 窗口居中

    def OnChangePassword(self, e):
        # 事件处理函数:保存文件
        changepasswordFrame = ui_change_password.ChangePasswordWindow(parent=None, title="修改密码")
        changepasswordFrame.Show()  # 显示登录窗口
        changepasswordFrame.Center()  # 窗口居中
        changepasswordFrame.userid = self.userid

    def OnUser(self, e):
        # 事件处理函数:用户管理
        userFrame = ui_user.UserWindow(parent=None, title="用户管理")
        userFrame.Show()  # 显示登录窗口
        userFrame.Center()  # 窗口居中

    def Ongood(self, e):
        # 事件处理函数:商品管理
        goodFrame = ui_good.GoodWindow(parent=None, title="商品管理")
        goodFrame.Show()  # 显示登录窗口
        goodFrame.Center()  # 窗口居中

    def Onshelf(self, e):#原教学班
        # 事件处理函数:开课计划"
        shelfFrame = ui_shelf.ShelfWindow(parent=None, title="货架管理")
        shelfFrame.Show()  # 显示登录窗口
        shelfFrame.Center()  # 窗口居中

    def Ongoodinfo(self, e):
        # 事件处理函数:商品信息
        goodinfoFrame = ui_goodinfo.GoodinfoWindow(parent=None, title="商品信息")
        goodinfoFrame.Show()  # 显示登录窗口
        goodinfoFrame.Center()  # 窗口居中

    def Onorder(self, e):
        # 事件处理函数:订单管理
        orderFrame = ui_order.OrderWindow(parent=None, title="订单管理")
        orderFrame.Show()  # 显示登录窗口
        orderFrame.Center()  # 窗口居中


