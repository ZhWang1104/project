import tkinter as tk
from tkinter import messagebox
from datas import dd
from main_page import MainPage
import json


class LoginPage_1:
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

        self.page = tk.Frame(self.root)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='账户：').grid(row=1, column=1, pady=5)
        tk.Entry(self.page, textvariable=self.Username).grid(row=1, column=2, pady=5)

        tk.Label(self.page, text='密码：').grid(row=2, column=1, pady=5)
        tk.Entry(self.page, show='*', textvariable=self.Password).grid(row=2, column=2, pady=5)

        tk.Button(self.page, text='登录', command=self.login).grid(row=3, column=1, pady=10)
        tk.Button(self.page, text='注册', command=self.Reg).grid(row=3, column=2, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=3, pady=10)

    # 登录操作
    def login(self):
        name = self.Username.get()
        password = self.Password.get()
        flag, message = dd.check_login(name, password)
        if flag:
            self.page.destroy()
            print("已完成")
            MainPage(self.root)
        else:
            messagebox.showwarning(title='警告', message=message)

    # 注册操作
    def Reg(self):
        self.page.destroy()
        from RegisterPage import Register_1
        Register_1(self.root)


if __name__ == '__main__':
    root = tk.Tk()
    LoginPage_1(master=root)
    root.mainloop()
