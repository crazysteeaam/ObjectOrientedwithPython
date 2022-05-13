from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json


class App_Login(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self)
        # Create widgets :)
        master.title("登录")  # 窗口标题
        master.geometry('300x200')
        master.tk.call("source", "Sun-Valley-ttk-theme-master/sun-valley.tcl")
        master.tk.call("set_theme", "light")
        self.accentbutton = None
        self.widgets_frame = None
        self.entry2 = None
        self.label2 = None
        self.entry1 = None
        self.label1 = None
        self.login_page(master)
        master.update()
        master.minsize(root.winfo_width(), root.winfo_height())
        __x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
        __y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
        master.geometry("+{}+{}".format(__x_cordinate, __y_cordinate))

    def login_page(self, parent):
        self.widgets_frame = ttk.LabelFrame(parent, text="登陆信息输入", padding=(20, 10))
        self.widgets_frame.grid(row=0, column=0, padx=35)

        # 用户名输入
        self.label1 = ttk.Label(self.widgets_frame, text="用户名")
        self.label1.grid(row=0, column=0)
        self.label1.configure(font=("Microsoft YaHei", 10))
        self.entry1 = ttk.Entry(self.widgets_frame)
        self.entry1.grid(row=0, column=1, padx=1)

        # 密码输入
        self.label2 = ttk.Label(self.widgets_frame, text="密码")
        self.label2.grid(row=1, column=0, pady=10)
        self.label2.configure(font=("Microsoft YaHei", 10))
        self.entry2 = ttk.Entry(self.widgets_frame)
        self.entry2.grid(row=1, column=1, pady=10, padx=1)

        # 确认按钮
        def button_bind1():
            # 按钮1 事件
            global wrong_time
            input_user = self.entry1.get()
            input_password = self.entry2.get()
            results = Methods.validate_wrongtime(input_user, input_password)
            if results == 'OK':
                self.master.destroy()
                root2 = Tk()
                App_Main(root2, input_user)
            elif results == 'SHUTDOWN':
                self.master.quit()
            elif results == 'WRONG':
                pass

        self.accentbutton = ttk.Button(
            self.widgets_frame, text="确认登陆", style="Accent.TButton", command=button_bind1
        )
        self.accentbutton.grid(row=2, column=0, columnspan=2, padx=5, pady=10)


class App_Main(ttk.Frame):
    def __init__(self, root2, userinfo):
        ttk.Frame.__init__(self)
        self.label3 = None
        self.widgets_frame2 = None
        root2.title("主页面")
        root2.geometry('500x500')
        self.main_page(root2, userinfo)
        root2.update()
        root2.minsize(root2.winfo_width(), root2.winfo_height())
        __x_cordinate = int((root2.winfo_screenwidth() / 2) - (root2.winfo_width() / 2))
        __y_cordinate = int((root2.winfo_screenheight() / 2) - (root2.winfo_height() / 2))
        root2.geometry("+{}+{}".format(__x_cordinate, __y_cordinate))
        root2.mainloop()

    def main_page(self, parent, userinfo):
        self.widgets_frame2 = ttk.LabelFrame(parent, text="登陆信息", padding=(20, 10))
        self.widgets_frame2.grid(row=0, column=0, padx=35)
        self.label3 = ttk.Label(self.widgets_frame2, text="欢迎" + userinfo + "登录")
        self.label3.grid(row=0, column=0)
        self.label3.configure(font=("Microsoft YaHei", 10))


class Methods(object):
    @staticmethod
    def validate_account(input_user: str, input_password: str) -> bool:
        # 验证用户名密码正确
        f = open("account.json", "r", encoding="utf8")
        _account = json.loads(f.read())
        if input_user == _account['user'] and input_password == _account['password']:
            return True
        else:
            messagebox.showinfo("Message", "用户名或密码输入错误!")
            return False

    @staticmethod
    def validate_wrongtime(input_user: str, input_password: str) -> str:
        global wrong_time
        if Methods.validate_account(input_user, input_password):
            return 'OK'
        else:
            wrong_time += 1
            if wrong_time >= 3:
                messagebox.showinfo("Message", "您已错误达到3次，自动退出！")
                return 'SHUTDOWN'
            return 'WRONG'


if __name__ == "__main__":
    wrong_time = 0
    root = Tk()
    App_Login(root)
    root.mainloop()
