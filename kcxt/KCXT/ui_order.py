import data
import wx


class OrderWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)

        # 创建控件
        lblListAction = ['退货', '修改', '售出']
        self.rboxAction = wx.RadioBox(panel, label='操作', choices=lblListAction)

        self.listorder = wx.ListCtrl(panel, wx.ID_ANY, size=(400, 400), style=wx.LC_REPORT)
        self.listorder.InsertColumn(0, '订单ID', width=50)
        self.listorder.InsertColumn(1, '顾客ID', width=50)
        self.listorder.InsertColumn(2, '商品ID', width=50)
        self.listorder.InsertColumn(3, '数  量', width=50)
        self.listorder.InsertColumn(4, '订单额', width=50)
        labelorderID = wx.StaticText(panel, wx.ID_ANY, '订单ID:')
        self.inputTextorderID = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelcustomerid = wx.StaticText(panel, wx.ID_ANY, '顾客ID:')
        self.inputTextcustomerid = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelgoodid = wx.StaticText(panel, wx.ID_ANY, '商品ID:')
        self.inputTextgoodid = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelordervolume = wx.StaticText(panel, wx.ID_ANY, '数  量:')
        self.inputTextordervolume = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelorderprice = wx.StaticText(panel, wx.ID_ANY, '订单额:')
        self.inputTextorderprice = wx.StaticText(panel, wx.ID_ANY, '')

        self.insertBtn = wx.Button(panel, wx.ID_ANY, '退货')
        self.updateBtn = wx.Button(panel, wx.ID_ANY, '更新')
        self.updateBtn.Disable()
        self.deleteBtn = wx.Button(panel, wx.ID_ANY, '售出')
        self.deleteBtn.Disable()
        self.lookforBtn = wx.Button(panel, wx.ID_ANY, '查询')
        self.shouyeBtn = wx.Button(panel, wx.ID_ANY, '首页')
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        editSizer = wx.BoxSizer(wx.VERTICAL)
        orderidSizer = wx.BoxSizer(wx.HORIZONTAL)
        customeridSizer = wx.BoxSizer(wx.HORIZONTAL)
        goodidSizer = wx.BoxSizer(wx.HORIZONTAL)
        ordervolumeSizer = wx.BoxSizer(wx.HORIZONTAL)
        orderpriceSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(self.rboxAction, 0, wx.ALL, 5)
        listSizer.Add(self.listorder, 0, wx.ALL, 5)

        orderidSizer.Add(labelorderID, 0, wx.ALL, 5)
        orderidSizer.Add(self.inputTextorderID, 0, wx.ALL, 5)
        customeridSizer.Add(labelcustomerid, 0, wx.ALL, 5)
        customeridSizer.Add(self.inputTextcustomerid, 0, wx.ALL, 5)
        goodidSizer.Add(labelgoodid, 0, wx.ALL, 5)
        goodidSizer.Add(self.inputTextgoodid, 0, wx.ALL, 5)
        ordervolumeSizer.Add(labelordervolume, 0, wx.ALL, 5)
        ordervolumeSizer.Add(self.inputTextordervolume, 0, wx.ALL, 5)
        orderpriceSizer.Add(labelorderprice, 0, wx.ALL, 5)
        orderpriceSizer.Add(self.inputTextorderprice, 0, wx.ALL, 5)

        btnSizer.Add(self.insertBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.updateBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.deleteBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.lookforBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.shouyeBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(orderidSizer, 0, wx.ALL, 5)
        editSizer.Add(customeridSizer, 0, wx.ALL, 5)
        editSizer.Add(goodidSizer, 0, wx.ALL, 5)
        editSizer.Add(ordervolumeSizer, 0, wx.ALL, 5)
        editSizer.Add(orderpriceSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.Bind(wx.EVT_RADIOBOX, self.onAction, self.rboxAction)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onorderList, self.listorder)
        self.Bind(wx.EVT_BUTTON, self.onInsert, self.insertBtn)
        self.Bind(wx.EVT_BUTTON, self.onUpdate, self.updateBtn)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.deleteBtn)
        self.Bind(wx.EVT_BUTTON, self.refresh_screen, self.shouyeBtn)
        self.Bind(wx.EVT_BUTTON, self.onlookfor, self.lookforBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)
        self.inputTextordervolume.Bind(wx.EVT_KILL_FOCUS, self.insertprice)

        # 查询课程信息并显示
        self.populate_order_list()

    def populate_order_list(self):
        """查询课程信息并显示"""
        order_list = data.get_order_list()
        self.listorder.DeleteAllItems()
        index = 0
        for order in order_list:
            self.listorder.InsertItem(index, order[0])
            self.listorder.SetItem(index, 1, order[1])
            self.listorder.SetItem(index, 2, order[2])
            self.listorder.SetItem(index, 3, str(order[3]))
            self.listorder.SetItem(index, 4, str(order[4]))
            index += 1

    def onAction(self, e):
        """事情处理函数:根据操作类型(插入、更新、删除)设置不同控件的状态"""
        action = self.rboxAction.GetStringSelection()
        if action == "退货":
            self.inputTextorderID.Enable()
            self.insertBtn.Enable()
            self.updateBtn.Disable()
            self.deleteBtn.Disable()
        elif action == "修改":
            self.inputTextorderID.Disable()
            self.insertBtn.Disable()
            self.updateBtn.Enable()
            self.deleteBtn.Disable()
        elif action == "售出":
            self.inputTextorderID.Enable()
            self.insertBtn.Disable()
            self.updateBtn.Disable()
            self.deleteBtn.Enable()

    def onorderList(self, e):
        """事件处理函数:在列表中选择课程，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        self.inputTextorderID.SetValue(self.listorder.GetItem(index, 0).GetText())
        self.inputTextcustomerid.SetValue(self.listorder.GetItem(index, 1).GetText())
        self.inputTextgoodid.SetValue(self.listorder.GetItem(index, 2).GetText())
        self.inputTextordervolume.SetValue(self.listorder.GetItem(index, 3).GetText())
        self.inputTextorderprice.SetLabel(self.listorder.GetItem(index, 4).GetText())

    # 退货
    def onInsert(self, e):
        """事件处理函数:删除一条记录"""
        orderid = self.inputTextorderID.GetValue()
        customerid = self.inputTextcustomerid.GetValue()
        goodid = self.inputTextgoodid.GetValue()
        ordervolume = int(self.inputTextordervolume.GetValue())
        orderprice = float(self.inputTextorderprice.SetLabel())
        if len(orderid.strip()) == 0:
            wx.MessageBox('请输入订单ID!')
            self.inputTextorderID.SetFocus()
            return None
        if not data.check_order_id(orderid):
            wx.MessageBox('订单不存在!')
        data.tuihuo_order(orderid, ordervolume)
        data.addmore_good(goodid, ordervolume)
        self.refresh_screen(e)

    def refresh_screen(self, e):
        """重新刷新界面"""
        self.inputTextorderID.SetValue('')
        self.inputTextcustomerid.SetValue('')
        self.inputTextgoodid.SetValue('')
        self.inputTextordervolume.SetValue('')
        self.inputTextorderprice.SetLabel('')
        # 查询课程信息并显示
        self.populate_order_list()

    def onUpdate(self, e):
        """事件处理函数: 更新一条记录"""
        orderid = self.inputTextorderID.GetValue()
        customerid = self.inputTextcustomerid.GetValue()
        goodid = self.inputTextgoodid.GetValue()
        ordervolume = int(self.inputTextordervolume.GetValue())
        orderprice = float(self.inputTextorderprice.GetValue())
        if len(orderid.strip()) == 0:
            wx.MessageBox('请输入订单id!')
            self.inputTextorderID.SetFocus()
            return None
        # 更新记录
        data.update_order(orderid, customerid, goodid, ordervolume, orderprice)
        # 初始化界面
        self.refresh_screen(e)

    def onlookfor(self, e):
        orderid = self.inputTextorderID.GetValue()
        if len(orderid.strip()) == 0:
            wx.MessageBox('请输入订单id!')
            self.inputTextorderID.SetFocus()
            return None
        order_lookfor = data.get_order_lookfor(orderid)
        self.listorder.DeleteAllItems()
        index = 0
        for order in order_lookfor:
            self.listorder.InsertItem(index, order[0])
            self.listorder.SetItem(index, 1, order[1])
            self.listorder.SetItem(index, 2, order[2])
            self.listorder.SetItem(index, 3, str(order[3]))
            self.listorder.SetItem(index, 4, str(order[4]))
            index += 1

    # 售出
    def onDelete(self, e):
        """事件处理函数:删除一条记录"""
        orderid = self.inputTextorderID.GetValue()
        customerid = self.inputTextcustomerid.GetValue()
        goodid = self.inputTextgoodid.GetValue()
        ordervolume = int(self.inputTextordervolume.GetValue())
        orderprice = float(self.inputTextorderprice.GetValue())
        if len(orderid.strip()) == 0:
            wx.MessageBox('请输入订单ID!')
            self.inputTextorderID.SetFocus()
            return None
        elif len(goodid.strip()) == 0:
            wx.MessageBox('请输入商品ID!')
            self.inputTextgoodid.SetFocus()
            return None
        elif data.check_order_id(orderid):
            wx.MessageBox('订单已存在!')
        elif data.check_good_id(goodid) and data.check_good_volume(goodid):
            data.insert_order(orderid, customerid, goodid, ordervolume, orderprice)
            data.out_good(goodid, ordervolume)
        else:
            wx.MessageBox('商品不存在!')

        self.refresh_screen(e)

    def onExit(self, e):
        self.Close(True)  # 关闭顶层框架窗口

    def insertprice(self, e):
        goodid = self.inputTextgoodid.GetValue()
        price = data.get_order_goodprice(goodid)
        volume = self.inputTextordervolume.GetValue()
        totalprice = float(price) * int(volume)
        print(totalprice)
        self.inputTextorderprice.SetLabel(str(totalprice))
        e.Skip()
