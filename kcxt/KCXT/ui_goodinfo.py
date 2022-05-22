import data
import wx
import ui_good


class GoodinfoWindow(wx.Dialog):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800,600))
        panel = wx.Panel(self, wx.ID_ANY)


        # 创建控件
        self.listgood = wx.ListCtrl(panel, wx.ID_ANY, size = (400, 350), style = wx.LC_REPORT)
        self.listgood.InsertColumn(0, '商品ID', width = 50)
        self.listgood.InsertColumn(1, '商品名称', width=50)
        self.listgood.InsertColumn(2, '单价', width=50)
        self.listgood.InsertColumn(3, '商品描述', width=100)
        self.listgood.InsertColumn(4, '数量', width=50)
        self.listgood.InsertColumn(5, '货架', width=50)
        labelgoodID = wx.StaticText(panel, wx.ID_ANY, '商品ID:')
        self.inputTextgoodID = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelgoodName = wx.StaticText(panel, wx.ID_ANY, '商品名称:')
        self.inputTextgoodName = wx.TextCtrl(panel, wx.ID_ANY, '' )
        labelgoodprice = wx.StaticText(panel, wx.ID_ANY, '单价:')
        self.inputTextgoodprice = wx.TextCtrl(panel, wx.ID_ANY,'')
        labelgoodDescription = wx.StaticText(panel, wx.ID_ANY, '商品描述:')
        self.inputTextgoodDescription = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelgoodvolume = wx.StaticText(panel, wx.ID_ANY, '数量:')
        self.inputTextgoodvolume = wx.TextCtrl(panel, wx.ID_ANY, '')
        labelgoodshelf = wx.StaticText(panel, wx.ID_ANY, '货架:')
        self.inputTextgoodshelf = wx.TextCtrl(panel, wx.ID_ANY, '')

        self.lookforBtn = wx.Button(panel, wx.ID_ANY, '查询')
        self.shouyeBtn = wx.Button(panel, wx.ID_ANY, '首页')
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

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
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)


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
        btnSizer.Add(self.lookforBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.shouyeBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        editSizer.Add(goodidSizer, 0, wx.ALL, 5)
        editSizer.Add(goodnameSizer, 0, wx.ALL, 5)
        editSizer.Add(goodpriceSizer, 0, wx.ALL, 5)
        editSizer.Add(gooddescriptionSizer, 0, wx.ALL, 5)
        editSizer.Add(goodvolumeSizer, 0, wx.ALL, 5)
        editSizer.Add(goodshelfSizer, 0, wx.ALL, 5)
        editSizer.Add(btnSizer, 0, wx.ALL, 5)

        contentSizer.Add(listSizer, 0, wx.ALL, 5)
        contentSizer.Add(editSizer, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(contentSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.onCourseList, self.listgood)
        self.Bind(wx.EVT_BUTTON, self.refresh_screen, self.shouyeBtn)
        self.Bind(wx.EVT_BUTTON, self.onlookfor, self.lookforBtn)

        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        # 查询课程信息并显示
        self.populate_good_list()

    def populate_good_list(self):
        """查询商品信息并显示"""
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


    def onCourseList(self, e):
        """事件处理函数:在列表中选择课程，内容显示在右侧"""
        index = e.GetIndex()  # 获得被激活表项的索引号
        self.inputTextgoodID.SetValue(self.listgood.GetItem(index, 0).GetText())
        self.inputTextgoodName.SetValue(self.listgood.GetItem(index, 1).GetText())
        self.inputTextgoodprice.SetValue(self.listgood.GetItem(index, 2).GetText())
        self.inputTextgoodDescription.SetValue(self.listgood.GetItem(index, 3).GetText())
        self.inputTextgoodvolume.SetValue(self.listgood.GetItem(index, 4).GetText())
        self.inputTextgoodshelf.SetValue(self.listgood.GetItem(index, 5).GetText())


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

    def refresh_screen(self, e):
        """重新刷新界面"""
        self.inputTextgoodID.SetValue('')
        self.inputTextgoodName.SetValue('')
        self.inputTextgoodprice.SetValue('')
        self.inputTextgoodDescription.SetValue('')
        self.inputTextgoodvolume.SetValue('')
        self.inputTextgoodshelf.SetValue('')

        # 查询课程信息并显示
        self.populate_good_list()

    def onExit(self, e):
        self.Close(True)  # 关闭顶层框架窗口



