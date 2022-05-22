import data
import wx


class ShelfWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)

        # 创建控件
        lblListAction = ['插入', '修改', '删除']
        self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)

        self.listshelf = wx.ListCtrl(panel, wx.ID_ANY, size=(400, 300), style=wx.LC_REPORT)
        self.listshelf.InsertColumn(0, '货架编号', width=150)
        self.listshelf.InsertColumn(1, '货架区域', width=150)
      

        labelshelfid = wx.StaticText(panel, wx.ID_ANY, '货架编号:')
        self.inputTextshelfid = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelshelfplace = wx.StaticText(panel, wx.ID_ANY, '货架区域:')
        self.inputTextlshelfplace= wx.TextCtrl(panel, wx.ID_ANY, '', style=wx.TE_PROCESS_ENTER)
       

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
        shelfidSizer = wx.BoxSizer(wx.HORIZONTAL)
        shelfplaceSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)
        listSizer.Add(self.listshelf, 0, wx.ALL, 5)

        shelfidSizer.Add(labelshelfid, 0, wx.ALL, 5)
        shelfidSizer.Add(self.inputTextshelfid, 0, wx.ALL, 5)
        shelfplaceSizer.Add(labelshelfplace, 0, wx.ALL, 5)
        shelfplaceSizer.Add(self.inputTextlshelfplace, 0, wx.ALL, 5)
     

        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(shelfidSizer, 0, wx.ALL, 5)
        editSizer.Add(shelfplaceSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)
        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(topSizer)
        topSizer.Fit(self)
        # 绑定事件
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onshelfList, self.listshelf)
        self.Bind(wx.EVT_TEXT_ENTER, self.onshelfid, self.inputTextlshelfplace)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)
        # 查询货架信息并显示
        self.populate_shelf_list()

    def populate_shelf_list(self):
        """查询shelf并显示"""
        shelf_list = data.get_shelf_list()
        self.listshelf.DeleteAllItems()
        index = 0
        for shelf in shelf_list:
            self.listshelf.InsertItem(index, shelf[0])
            self.listshelf.SetItem(index, 1, shelf[1])
            index += 1

    def onAction(self, e):
        """事情处理函数:根据操作类型（插入、更新、删除）设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "插入":
            self.inputTextshelfid.Enable()
            self.insertBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
        elif action == "修改":
            self.inputTextshelfid.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "删除":
            self.inputTextshelfid.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()

    def onshelfList(self, e):
        """事件处理函数:在列表中选择货架，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        self.inputTextshelfid.SetValue(self.listshelf.GetItem(index, 0).GetText())
        self.inputTextlshelfplace.SetValue(self.listshelf.GetItem(index, 1).GetText())

    def onshelfid(self, e):
        """事件处理函数，输入货架ID时检查其存在，并显示名称"""
        shelfid = self.inputTextlshelfplace.GetValue()
        if len(shelfid.strip()) == 0:
            return None
        sheldid = data.check_shelf_id(shelfid)
        if sheldid:
            self.inputTextshelfid.SetValue(sheldid)
        else:
            wx.MessageBox("该货架不存在!")
            self.inputTextlshelfplace.SetFocus()
            return None



    def onInsert(self, e):
        """事件处理函数:插入一条记录"""
        shelfid = self.inputTextshelfid.GetValue()
        shelfplace = self.inputTextlshelfplace.GetValue()

        if len(shelfid.strip()) == 0:
            wx.MessageBox('请输入货架id! ')
            self.inputTextshelfid.SetFocus()
            return None
        if data.check_shelf_id(shelfid):
            wx.MessageBox("该货架已经存在!")
            self.inputTextshelfid.SetFocus()
            return None
        # 插入记录
        data.insert_shelf(shelfid,shelfplace)
        # 初始化界面
        self.refresh_screen()

    def refresh_screen(self):
        """重新刷新界面"""
        self.inputTextshelfid.SetValue('')
        self.inputTextlshelfplace.SetValue('')

        # 查询货架信息并显示
        self.populate_shelf_list()

    def onUpdate(self, e):
        """事件处理函数:更新一条记录"""
        shelfid = self.inputTextshelfid.GetValue()
        shelfplace = self.inputTextlshelfplace.GetValue()
        if len(shelfid.strip()) == 0:
            wx.MessageBox('请输入货架ID! ')
            self.inputTextshelfid.SetFocus()
            return None
        # 更新记录
        data.update_shelf(shelfplace,shelfid)
        # 初始化界面
        self.refresh_screen()

    def onDelete(self, e):
        """事件处理函数:删除一条记录"""
        shelfid = self.inputTextshelfid.GetValue()
        # 删除记录
        data.delete_shelf(shelfid)
        # 初始化界面
        self.refresh_screen()

    def onExit(self, e):
        self.Close(True)  # 关闭顶层框架窗口
