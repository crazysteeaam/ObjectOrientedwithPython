import os
import wx
import data
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(640, 600))

        panel = wx.Panel(self, wx.ID_ANY)

        self.lTtree = wx.GenericDirCtrl(panel, -1, dir="C:", size=(200, 500), style=0)
        self.rList = wx.ListCtrl(panel, wx.ID_ANY, size=(400, 500), style=wx.LC_REPORT)
        self.rList.InsertColumn(0, '文件名', width=200)
        self.rList.InsertColumn(1, '文件大小', width=100)

        self.compressBtn = wx.Button(panel, wx.ID_ANY, '压缩')
        self.uncompressBtn = wx.Button(panel, wx.ID_ANY, '解压')
        self.exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        self.CreateStatusBar()  # 创建状态栏

        # 布局
        topSizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        contentSizer = wx.BoxSizer(wx.HORIZONTAL)

        btnSizer.Add(self.compressBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.uncompressBtn, 0, wx.ALL, 5)
        btnSizer.Add(self.exitBtn, 0, wx.ALL, 5)

        contentSizer.Add(self.lTtree, 0, wx.ALL, 5)
        contentSizer.Add(self.rList, 0, wx.ALL, 5)

        topSizer.Add(contentSizer, 0, wx.ALL, 5)
        topSizer.Add(btnSizer, 0, wx.ALL, 5)
        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件
        self.lTtree.Bind(wx.EVT_TREE_ITEM_ACTIVATED, self.OnOpen)
        self.compressBtn.Bind(wx.EVT_BUTTON, self.onCompress)
        self.uncompressBtn.Bind(wx.EVT_BUTTON, self.onUncompress)
        self.exitBtn.Bind(wx.EVT_BUTTON, self.onExit)

    def populate_list(self, files):
        """在右侧列表框中显示files信息一览"""
        self.rList.DeleteAllItems()
        index = 0
        for file in files:
            self.rList.InsertItem(index, file[0])
            self.rList.SetItem(index, 1, file[1])
            index += 1

    def OnOpen(self, evt):
        path = self.lTtree.GetPath()
        if os.path.isdir(path):
            """查询目录path中的信息并显示右侧列表框中"""
            files = sorted(data.get_file_list(path), key=lambda x:x[1], reverse=True)
            self.populate_list(files)
            evt.Skip()
        else:
            if path.endswith('.zip'):
                files = sorted(data.get_zipfile_list(path), key=lambda x: x[1], reverse=True)
                self.populate_list(files)

    def onCompress(self, e):
        """压缩按钮事件处理函数"""
        files = [] #待压缩的文件列表
        spath = self.lTtree.GetPath()
        item = self.rList.GetFirstSelected()
        while item != -1:
            filename = self.rList.GetItem(item, 0).GetText()
            filepath = os.path.join(spath, filename)
            files.append(filepath)
            item = self.rList.GetNextSelected(item)
        if len(files) == 0:
            wx.MessageBox('请在右侧选择要压缩的文件！')
        else:
            tpath = spath
            file_wildcard = "Zip files(*.zip)|*.zip|All files(*.*)|*.*"
            dlg = wx.FileDialog(self, u"压缩到文件",
                                spath,
                                # style=wx.SAVE | wx.OVERWRITE_PROMPT,
                                wildcard=file_wildcard
                                )
            if dlg.ShowModal() == wx.ID_OK:
                tpath = dlg.GetPath()  # 解压的目标文件夹
            dlg.Destroy()
            data.compress(files, spath, tpath)

    def onUncompress(self, e):
        """解缩按钮事件处理函数"""
        spath = self.lTtree.GetPath()
        print(spath)
        if os.path.isfile(spath) and spath.endswith('.zip'):
            tpath = spath
            #提示选择目标文件夹
            dlg = wx.DirDialog(self, u"解压到文件夹", style=wx.DD_DEFAULT_STYLE)
            if dlg.ShowModal() == wx.ID_OK:
                tpath = dlg.GetPath()  # 解压的目标文件夹
            dlg.Destroy()
            data.uncompress(spath, tpath) #解压缩spath到目标文件夹tpath
        else:
            wx.MessageBox('请在左侧选择要解压的zip格式的文件！')

    def onExit(self, e):
        self.Close(True)  # 关闭窗口