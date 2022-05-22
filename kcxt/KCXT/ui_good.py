import data
import wx


class GoodWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        self.panel = wx.Panel(self, -1)


        # 创建控件
        lblListAction = ['入库', '修改', '出库','查询']
        self.rboxAction = wx.RadioBox(self.panel, label='操作', choices=lblListAction)

        self.listgood = wx.ListCtrl(self.panel, wx.ID_ANY, size = (400, 350), style = wx.LC_REPORT)
        self.listgood.InsertColumn(0, '商品ID', width = 50)
        self.listgood.InsertColumn(1, '商品名称', width=50)
        self.listgood.InsertColumn(2, '商品单价', width=50)
        self.listgood.InsertColumn(3, '商品描述', width=100)
        self.listgood.InsertColumn(4, '商品数量', width=50)
        self.listgood.InsertColumn(5, '商品货架', width=50)
        labelgoodID = wx.StaticText(self.panel, wx.ID_ANY, '商品ID:')
        self.inputTextgoodID = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        labelgoodName = wx.StaticText(self.panel, wx.ID_ANY, '商品名称:')
        self.inputTextgoodName = wx.TextCtrl(self.panel, wx.ID_ANY, '' )
        labelgoodprice = wx.StaticText(self.panel, wx.ID_ANY, '商品单价:')
        self.inputTextgoodprice = wx.TextCtrl(self.panel, wx.ID_ANY,'')
        labelgoodDescription = wx.StaticText(self.panel, wx.ID_ANY, '商品描述:')
        self.inputTextgoodDescription = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        labelgoodvolume = wx.StaticText(self.panel, wx.ID_ANY, '商品数量:')
        self.inputTextgoodvolume = wx.TextCtrl(self.panel, wx.ID_ANY, '')
        labelgoodshelf = wx.StaticText(self.panel, wx.ID_ANY, '商品货架:')
        self.inputTextgoodshelf = wx.TextCtrl(self.panel, wx.ID_ANY, '')

        self.insertBtn = wx.Button(self.panel, wx.ID_ANY,'入库')
        self.updateBtn = wx.Button(self.panel, wx.ID_ANY, '更新')
        self.updateBtn.Disable()
        self.deleteBtn = wx.Button(self.panel, wx.ID_ANY, '出库')
        self.deleteBtn.Disable()
        self.lookforBtn = wx.Button(self.panel, wx.ID_ANY, '查询')
        self.lookforBtn.Disable()
        self.shouyeBtn = wx.Button(self.panel, wx.ID_ANY, '首页')
        self.shouyeBtn.Enable()
        exitBtn = wx.Button(self.panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        goodidSizer = wx.BoxSizer(wx.HORIZONTAL)
        goodnameSizer = wx.BoxSizer(wx.HORIZONTAL)
        goodpriceSizer = wx.BoxSizer(wx.HORIZONTAL)
        gooddescriptionSizer = wx.BoxSizer(wx.HORIZONTAL)
        goodvolumeSizer= wx.BoxSizer(wx.HORIZONTAL)
        goodshelfSizer= wx.BoxSizer(wx.HORIZONTAL)
        btnSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer2 = wx.BoxSizer(wx.HORIZONTAL)


        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)

        listSizer.Add(self.listgood, 0, wx.ALL, 5)

        goodidSizer.Add(labelgoodID, 0, wx.ALL, 5)
        goodidSizer.Add(self.inputTextgoodID, 0, wx.ALL, 5)
        goodnameSizer.Add(labelgoodName, 0, wx.ALL, 5)
        goodnameSizer.Add(self.inputTextgoodName, 0, wx.ALL, 5)
        goodpriceSizer.Add(labelgoodprice, 0, wx.ALL, 5)
        goodpriceSizer.Add(self.inputTextgoodprice, 0, wx.ALL, 5)
        gooddescriptionSizer.Add(labelgoodDescription, 0, wx.ALL, 5)
        gooddescriptionSizer.Add(self.inputTextgoodDescription, 0, wx.ALL, 5)
        goodvolumeSizer.Add(labelgoodvolume, 0, wx.ALL, 5)
        goodvolumeSizer.Add(self.inputTextgoodvolume, 0, wx.ALL, 5)
        goodshelfSizer.Add(labelgoodshelf, 0, wx.ALL, 5)
        goodshelfSizer.Add(self.inputTextgoodshelf, 0, wx.ALL, 5)

        btnSizer1.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer1.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer1.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer1.Add(self.lookforBtn, 0, wx.ALL, 5)
        btnSizer2.Add(self.shouyeBtn, 0, wx.ALL, 5)
        btnSizer2.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(goodidSizer, 0, wx.ALL, 5)
        editSizer.Add(goodnameSizer, 0, wx.ALL, 5)
        editSizer.Add(goodpriceSizer, 0, wx.ALL, 5)
        editSizer.Add(gooddescriptionSizer, 0, wx.ALL, 5)
        editSizer.Add(goodvolumeSizer, 0, wx.ALL, 5)
        editSizer.Add(goodshelfSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer1, 0, wx.ALL, 5)
        editSizer.Add(btnSizer2, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        self.panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.ongoodList, self.listgood)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.onlookfor, self.lookforBtn)
        self.Bind(wx.EVT_BUTTON, self.refresh_screen, self.shouyeBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        # 查询课程信息并显示
        self.populate_good_list()

    def populate_good_list(self):
        """查询课程信息并显示"""
        good_list = data.get_good_list()
        self.listgood.DeleteAllItems()
        index = 0
        for good in good_list:
            self.listgood.InsertItem(index, good[0])
            self.listgood.SetItem(index, 1, good[1])
            self.listgood.SetItem(index, 2, str(good[2]))
            self.listgood.SetItem(index, 3, good[3])
            self.listgood.SetItem(index, 4, str(good[4]))
            self.listgood.SetItem(index, 5, good[5])
            index += 1

    def onAction(self, e):
        """事情处理函数:根据操作类型(插入、更新、删除)设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "入库":
            self.insertBtn.Enable()
            self.shouyeBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
            self.lookforBtn.Disable()
        elif action == "修改":
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.shouyeBtn.Enable()
            self.deleteBtn.Disable()
            self.lookforBtn.Disable()
        elif action == "出库":
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()
            self.shouyeBtn.Enable()
            self.lookforBtn.Disable()
        elif action == "查询":
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
            self.lookforBtn.Enable()
            self.shouyeBtn.Enable()

    def ongoodList(self, e):
        """事件处理函数:在列表中选择商品，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        self.inputTextgoodID.SetValue(self.listgood.GetItem(index, 0).GetText())
        self.inputTextgoodName.SetValue(self.listgood.GetItem(index, 1).GetText())
        self.inputTextgoodprice.SetValue(self.listgood.GetItem(index, 2).GetText())
        self.inputTextgoodDescription.SetValue(self.listgood.GetItem(index, 3).GetText())
        self.inputTextgoodvolume.SetValue(self.listgood.GetItem(index, 4).GetText())
        self.inputTextgoodshelf.SetValue(self.listgood.GetItem(index, 5).GetText())

    def onInsert(self, e):
        """事件处理函数: 插入一条记录"""
        goodid = self.inputTextgoodID.GetValue()
        goodname = self.inputTextgoodName.GetValue()
        goodprice = self.inputTextgoodprice.GetValue()
        gooddescription = self.inputTextgoodDescription.GetValue()
        goodvolume = int(self.inputTextgoodvolume.GetValue())
        goodshelf = self.inputTextgoodshelf.GetValue()

        if len(goodid.strip()) == 0:
            wx.MessageBox('请输入商品ID!')
            self.inputTextgoodID.SetFocus()
            return None
        elif len(goodname.strip()) == 0:
            wx.MessageBox('请输入商品名称!')
            self.inputTextgoodName.SetFocus()
            return None
        elif data.check_good_id(goodid):
            data.addmore_good(goodid,goodvolume)
        # 插入记录
        else:
            data.insert_good(goodid, goodname,goodprice, gooddescription, goodvolume,goodshelf)
        # 初始化界面
        self.refresh_screen(e)

    def refresh_screen(self,e):
        """重新刷新界面"""
        self.inputTextgoodID.SetValue('')
        self.inputTextgoodName.SetValue('')
        self.inputTextgoodprice.SetValue('')
        self.inputTextgoodDescription.SetValue('')
        self.inputTextgoodvolume.SetValue('')
        self.inputTextgoodshelf.SetValue('')

        # 查询课程信息并显示
        self.populate_good_list()

    def onUpdate(self, e):
        """事件处理函数: 更新一条记录"""
        goodid = self.inputTextgoodID.GetValue()
        goodname = self.inputTextgoodName.GetValue()
        goodprice = self.inputTextgoodprice.GetValue()
        gooddescription = self.inputTextgoodDescription.GetValue()
        goodvolume = self.inputTextgoodvolume.GetValue()
        goodshelf= self.inputTextgoodshelf.GetValue()

        if len(goodname.strip()) == 0:
            wx.MessageBox('请输入商品名称!')
            self.inputTextgoodName.SetFocus()
            return None
        # 更新记录
        data.update_good( goodname,goodprice, gooddescription, goodvolume,goodshelf,goodid)
        # 初始化界面
        self.refresh_screen(e)

    def onlookfor(self,e):
        goodid = self.inputTextgoodID.GetValue()
        if len(goodid.strip()) == 0:
            wx.MessageBox('请输入商品id!')
            self.inputTextgoodID.SetFocus()
            return None
        good_lookfor = data.get_good_lookfor(goodid)
        self.listgood.DeleteAllItems()
        index = 0
        for good in good_lookfor:
            self.listgood.InsertItem(index, good[0])
            self.listgood.SetItem(index, 1, good[1])
            self.listgood.SetItem(index, 2, str(good[2]))
            self.listgood.SetItem(index, 3, good[3])
            self.listgood.SetItem(index, 4, str(good[4]))
            self.listgood.SetItem(index, 5, good[5])
            index += 1

    def onDelete(self, e):
        """事件处理函数: 插入一条记录"""
        goodid = self.inputTextgoodID.GetValue()
        goodname = self.inputTextgoodName.GetValue()
        goodprice = self.inputTextgoodprice.GetValue()
        gooddescription = self.inputTextgoodDescription.GetValue()
        goodvolume = int(self.inputTextgoodvolume.GetValue())
        goodshelf = self.inputTextgoodshelf.GetValue()

        if len(goodid.strip()) == 0:
            wx.MessageBox('请输入商品ID!')
            self.inputTextgoodID.SetFocus()
            return None
        elif len(goodname.strip()) == 0:
            wx.MessageBox('请输入商品名称!')
            self.inputTextgoodName.SetFocus()
            return None
        elif data.check_good_id(goodid):
            data.out_good(goodid,goodvolume)
        # 插入记录
        else:
            wx.MessageBox('不存在该商品')
        # 初始化界面
        self.refresh_screen(e)


    def onExit(self, e):
        self.Close(True)  # 关闭顶层框架窗口



