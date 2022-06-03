import tkinter as tk
from tkinter import messagebox
from datas import dd
import json


class Register_1:
    def __init__(self, master):

        self.root = master
        width = 300
        height = 300
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(size)
        self.root.title('通讯录系统1.0')

        self.Username = tk.StringVar()
        self.Password = tk.StringVar()
        self.Password_2 = tk.StringVar()

        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='账户：').grid(row=1, column=1, pady=5)
        tk.Entry(self.page, textvariable=self.Username).grid(row=1, column=2, pady=5)

        tk.Label(self.page, text='新密码：').grid(row=2, column=1, pady=5)
        tk.Entry(self.page, show='*', textvariable=self.Password).grid(row=2, column=2, pady=5)

        tk.Label(self.page, text='确认密码：').grid(row=3, column=1, pady=5)
        tk.Entry(self.page, show='*', textvariable=self.Password_2).grid(row=3, column=2, pady=5)

        tk.Button(self.page, text='注册', command=self.Register).grid(row=4, column=1, pady=10)
        tk.Button(self.page, text='返回', command=self.Back).grid(row=4, column=2, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=4, column=3, pady=10)

    # 返回登录界面
    def Back(self):
        self.page.destroy()
        from LoginPage import LoginPage_1
        LoginPage_1(self.root)

    # 注册信息登记
    def Register(self):
        if self.Username.get() == '':
            messagebox.showwarning(title='警告', message='账户不可为空')
        elif self.Password.get() == '':
            messagebox.showwarning(title='警告', message='新密码不可为空')
        elif self.Password_2.get() == '':
            messagebox.showwarning(title='警告', message='确认密码不可为空')
        else:
            name = self.Username.get()
            password = self.Password.get()
            password_2 = self.Password_2.get()
            if password == password_2:
                flag, message = dd.check_login(name, password)
                if flag:
                    messagebox.showwarning(title='警告', message='用户已注册')
                else:
                    con = dd.all_User()
                    i = {"username": name, "password": password}
                    con.append(i)
                    with open('userdatas.json', mode='w+', encoding='utf-8') as f:
                        json.dump(con, f, indent=4)
                    self.page.destroy()
                    from LoginPage import LoginPage_1
                    LoginPage_1(self.root)
            else:
                messagebox.showwarning(title='警告', message='两次密码输入不一致')
