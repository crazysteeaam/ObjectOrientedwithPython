from tkinter import *
from tkinter import ttk


class Main(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.dataTreeview = ttk.Treeview(parent, show='headings',
                                    column=('id', 'name', 'sex', 'python_score', 'database_score', 'c_language_score'))
        self.dataTreeview.column('id', width=15, anchor="center")
        self.dataTreeview.column('name', width=20, anchor="center")
        self.dataTreeview.column('sex', width=20, anchor="center")
        self.dataTreeview.column('python_score', width=60, anchor="center")
        self.dataTreeview.column('database_score', width=60, anchor="center")
        self.dataTreeview.column('c_language_score', width=40, anchor="center")

        # 头显示
        self.dataTreeview.heading('id', text='编号')
        self.dataTreeview.heading('name', text='姓名')
        self.dataTreeview.heading('sex', text='性别')
        self.dataTreeview.heading('python_score', text='Python成绩')
        self.dataTreeview.heading('database_score', text='数据库成绩')
        self.dataTreeview.heading('c_language_score', text='C成绩')
        self.dataTreeview.place(x=10, y=245, width=350, height=250)


# 创建窗口

if __name__ == "__main__":
    app = Tk()
    app.title('你好')
    Main(app)
    app.mainloop()
