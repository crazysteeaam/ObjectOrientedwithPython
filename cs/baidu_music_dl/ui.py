import wx
import data

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        panel = wx.Panel(self, wx.ID_ANY)
        #创建控件
        labelFrom = wx.StaticText(panel, wx.ID_ANY, 'From:')
        self.inputTextFrom = wx.TextCtrl(panel, wx.ID_ANY, '0')
        labelTo = wx.StaticText(panel, wx.ID_ANY, 'To:')
        self.inputTextTo = wx.TextCtrl(panel, wx.ID_ANY, '9')
        self.labelMessage = wx.StaticText(panel, wx.ID_ANY, '')
        self.listChannel = wx.ListCtrl(panel, wx.ID_ANY, size=(300, 400), style=wx.LC_REPORT)
        self.listChannel.InsertColumn(0, '频道ID', width=200)
        self.listChannel.InsertColumn(1, '频道名称',  width=100)
        self.listSong = wx.ListCtrl(panel, wx.ID_ANY, size=(300, 400), style=wx.LB_MULTIPLE | wx.LC_REPORT)
        self.listSong.InsertColumn(1, '歌曲ID', width=80)
        self.listSong.InsertColumn(2, '歌曲名称', width=140)
        self.listSong.InsertColumn(3, '歌曲大小', width=80)

        searchBtn = wx.Button(panel, wx.ID_ANY, '搜索')
        downloadBtn = wx.Button(panel, wx.ID_ANY, '下载')
        exitBtn = wx.Button(panel, wx.ID_ANY, '退出')

        topSizer = wx.BoxSizer(wx.VERTICAL)
        optionSizer = wx.BoxSizer(wx.HORIZONTAL)
        messageSizer = wx.BoxSizer(wx.HORIZONTAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        optionSizer.Add(labelFrom, 0, wx.ALL, 5)
        optionSizer.Add(self.inputTextFrom, 0, wx.ALL, 5)
        optionSizer.Add(labelTo, 0, wx.ALL, 5)
        optionSizer.Add(self.inputTextTo, 0, wx.ALL, 5)

        messageSizer.Add(self.labelMessage, 0, wx.ALL, 5)

        listSizer.Add(self.listChannel, 0, wx.ALL, 5)
        listSizer.Add(self.listSong, 0, wx.ALL, 5)

        btnSizer.Add(searchBtn, 0, wx.ALL, 5)
        btnSizer.Add(downloadBtn, 0, wx.ALL, 5)
        btnSizer.Add(exitBtn, 0, wx.ALL, 5)

        topSizer.Add(optionSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(messageSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(listSizer, 0, wx.ALL | wx.CENTER, 5)
        topSizer.Add(btnSizer, 0, wx.ALL | wx.CENTER, 5)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)

        # 绑定事件.
        self.Bind(wx.EVT_BUTTON, self.onSearch, searchBtn)
        self.Bind(wx.EVT_BUTTON, self.onDownload, downloadBtn)
        self.Bind(wx.EVT_BUTTON, self.onExit, exitBtn)

        #查询百度音乐频道列表并显示
        self.populate_channel_list()

    def populate_channel_list(self):
        """查询百度音乐频道列表并显示"""
        self.channel_list = data.get_channel_list()
        # items = channel_list.items()
        index = 0
        for k in self.channel_list:
            self.listChannel.InsertItem(index, k)
            self.listChannel.SetItem(index, 1, self.channel_list[k])
            index += 1

    def populate_song_list(self,channel_id,channel_name):
        """查询百度音乐指定频道的歌曲列表并显示"""
        from_no = int(self.inputTextFrom.GetValue())
        to_no = int(self.inputTextTo.GetValue())
        self.song_list = data.get_song_list(channel_id,channel_name,from_no,to_no)
        index = 0
        for k in self.song_list:
            self.listSong.InsertItem(index, str(k))
            self.listSong.SetItem(index, 1, str(self.song_list[k][0]))
            self.listSong.SetItem(index, 2, str(self.song_list[k][2]))
            index += 1

    def onSearch(self,e):
        """事件处理函数：显示消息对话框"""
        index = self.listChannel.GetFirstSelected()
        channel_id = self.listChannel.GetItemText(index)
        #查询百度音乐指定频道的歌曲列表并显示
        self.populate_song_list(channel_id,self.channel_list[channel_id])

    def onDownload(self, e):
        """ 事件处理函数：打开文件 """
        self.download_list = []
        index = self.listSong.GetFirstSelected()
        while index != -1:
            song_id = self.listSong.GetItemText(index)
            song_name = self.song_list[song_id][0]
            song_url = self.song_list[song_id][1]
            song_size = int(self.song_list[song_id][2])
            #下载歌曲
            self.labelMessage.SetLabelText('正在下载歌曲{0}......'.format(song_name))
            data.down_mp3_by_link(song_name, song_url, song_size)
            index = self.listSong.GetNextSelected(index)
        self.labelMessage.SetLabelText('下载完成，结果请查看log.txt')

    def onExit(self,e):
        self.Close(True)  # 关闭顶层框架窗口
