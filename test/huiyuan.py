from tkinter import *
import json

# 创建窗口
root = Tk()
root.title('登录')
root.geometry('800x500')
f1 = Frame(root);
f1.pack()
f2 = Frame(root);
f2.pack()
f3 = Frame(root);
f3.pack()
l1 = Label(f1, text='用户名');
l1.pack(side=LEFT)
e1 = Entry(f1);
e1.pack(side=LEFT)
l2 = Label(f2, text='密码');
l2.pack(side=LEFT)
e2 = Entry(f2, show='*');
e2.pack(side=LEFT)
count = 0


# 事件触发
def success_in(self):
    f = open("users.json", "r", encoding='utf-8')
    users_dict = json.loads(f.read())
    global count
    while count > 2:
        root.destroy()
    else:
        if e1.get() not in users_dict:
            print('用户名不存在!')
            count += 1
        else:
            if e2.get() != users_dict[e1.get()]:
                print('密码不正确，请重新输入!')
                count += 1
            else:
                root1 = Tk()
                root1.title('欢迎登录')
                root1.geometry('800x500')
                statusbar = Label(root1, text="登录成功，欢迎您！", bd=1, relief=SUNKEN, anchor=W)
                statusbar.pack(side=BOTTOM, fill=X)
                root1.mainloop()


b1 = Button(f3, text='登录', command=success_in)
b1.pack(side=RIGHT)
b2 = Button(f3, text='取消', command=root.destroy)
b2.pack(side=RIGHT)
root.mainloop()
