import tkinter as tk
from tkinter import ttk
from datas import dd
import json
from tkinter import messagebox


# 子页面
# 添加信息
class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()  # 跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
        self.tel = tk.StringVar()
        self.adress = tk.StringVar()
        self.sex = tk.StringVar()
        self.email = tk.StringVar()
        self.InstantMessaging = tk.StringVar()
        self.status = tk.StringVar()
        self.create_pages()

    def create_pages(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Label(self, text='姓    名   ：').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='电    话   ：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.tel).grid(row=2, column=2, pady=10)
        tk.Label(self, text='工 作 单 位：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.adress).grid(row=3, column=2, pady=10)
        tk.Label(self, text='邮    件   ：').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.email).grid(row=4, column=2, pady=10)
        tk.Label(self, text='即 时  通  ：').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.InstantMessaging).grid(row=5, column=2, pady=10)
        tk.Label(self, text='性    别   ：').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=6, column=2, pady=10)

        tk.Button(self, text='添加', command=self.save_info).grid(row=7, column=5, pady=15)

        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10, stick=tk.E)

    def save_info(self):
        if self.name.get() == '':
            messagebox.showwarning(title='警告', message='名字不可为空')
        elif self.tel.get() == '':
            messagebox.showwarning(title='警告', message='电话不可为空')
        elif self.sex.get() == '':
            messagebox.showwarning(title='警告', message='性别不可为空')
        else:
            s = {
                'name': self.name.get(),
                'tel': self.tel.get(),
                'address': self.adress.get(),
                'sex': self.sex.get(),
                'email': self.email.get(),
                'InstantMessaging': self.InstantMessaging.get()}
            self.name.set('')
            self.tel.set('')
            self.adress.set('')
            self.sex.set('')
            self.email.set('')
            self.InstantMessaging.set('')
            self.status.set("添加成功！")
            dd.Insert(s)
            self.status.set('存储数据成功！')


# 编辑信息
class EditFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tk.StringVar()  # 跟踪变量的值的变化，以保证值的变更随时可以显示在界面上
        self.tel = tk.StringVar()
        self.adress = tk.StringVar()
        self.sex = tk.StringVar()
        self.email = tk.StringVar()
        self.InstantMessaging = tk.StringVar()
        self.status = tk.StringVar()
        self.create_pages()

    def create_pages(self):
        tk.Label(self).grid(row=0, pady=10)

        tk.Label(self, text='姓    名   ：').grid(row=1, column=1, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=2, pady=10)
        tk.Label(self, text='电    话   ：').grid(row=2, column=1, pady=10)
        tk.Entry(self, textvariable=self.tel).grid(row=2, column=2, pady=10)
        tk.Label(self, text='工 作 单 位：').grid(row=3, column=1, pady=10)
        tk.Entry(self, textvariable=self.adress).grid(row=3, column=2, pady=10)
        tk.Label(self, text='邮    件   ：').grid(row=4, column=1, pady=10)
        tk.Entry(self, textvariable=self.email).grid(row=4, column=2, pady=10)
        tk.Label(self, text='即 时  通  ：').grid(row=5, column=1, pady=10)
        tk.Entry(self, textvariable=self.InstantMessaging).grid(row=5, column=2, pady=10)
        tk.Label(self, text='性    别   ：').grid(row=6, column=1, pady=10)
        tk.Entry(self, textvariable=self.sex).grid(row=6, column=2, pady=10)

        tk.Button(self, text='搜索', command=self.Sea_Pp).grid(row=7, column=1, pady=15)
        tk.Button(self, text='编辑', command=self.edit_Pp).grid(row=7, column=2, pady=15)

        tk.Label(self, textvariable=self.status).grid(row=8, column=2, pady=10, stick=tk.E)

    def Sea_Pp(self):
        if self.name.get() == '':
            messagebox.showwarning(title='警告', message='名字不可为空')
        elif self.tel.get() == '':
            messagebox.showwarning(title='警告', message='电话不可为空')
        else:
            f, con = dd.find_data_name(self.tel.get())
            if f:
                for i in con:
                    self.name.set(i['name'])
                    self.tel.set(i['tel'])
                    self.adress.set(i['address'])
                    self.email.set(i['email'])
                    self.InstantMessaging.set(i['InstantMessaging'])
                    self.sex.set(i['sex'])
            else:
                self.name.set('')
                self.tel.set('')
                self.status.set("联系人不存在")

    def edit_Pp(self):
        s = {
            'name': self.name.get(),
            'tel': self.tel.get(),
            'address': self.adress.get(),
            'sex': self.sex.get(),
            'email': self.email.get(),
            'InstantMessaging': self.InstantMessaging.get()}
        self.name.set('')
        self.tel.set('')
        self.adress.set('')
        self.sex.set('')
        self.email.set('')
        self.InstantMessaging.set('')
        dd.Updata(s)
        self.status.set('修改数据成功！')


# 删除信息

class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.delete_name = tk.StringVar()
        self.status = tk.StringVar()

        tk.Label(self, text='请输入名字：').pack(pady=10)
        tk.Entry(self, textvariable=self.delete_name).pack(pady=10)
        tk.Button(self, text='确认删除', command=self.Delete).pack(pady=10)
        tk.Label(self, textvariable=self.status).pack(pady=10)

    def Delete(self):
        if self.delete_name.get() == '':
            messagebox.showwarning(title='警告', message='名字不可为空')
        else:
            delete_name = self.delete_name.get()
            message = dd.Delete_data(delete_name)
            self.delete_name.set('')
            self.status.set(message)


# 展示信息
def save_data():
    with open('contant.json', mode='w+', encoding='utf-8') as f:
        json.dump(dd.all(), f, indent=4)


class ShowFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.tree_view = None
        self.table_view = tk.Frame()
        self.table_view.pack()

        self.create_page()

    def create_page(self):
        col = ("name", "tel", "address", "sex", "email", "InstantMessaging")
        col_value = ("姓名", "电话", "工作单位", "性别", "邮件", "即时通")
        self.tree_view = ttk.Treeview(self, show='headings', columns=col)
        self.tree_view.column('name', width=100, anchor='center')
        self.tree_view.column('tel', width=100, anchor='center')
        self.tree_view.column('address', width=100, anchor='center')
        self.tree_view.column('sex', width=100, anchor='center')
        self.tree_view.column('email', width=100, anchor='center')
        self.tree_view.column('InstantMessaging', width=90, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('tel', text='电话')
        self.tree_view.heading('address', text='工作单位')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('email', text='邮件')
        self.tree_view.heading('InstantMessaging', text='即时通')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.show_data()

        tk.Button(self, text='刷新数据', command=self.show_data).pack(anchor=tk.E, pady=6)
        tk.Button(self, text='导出数据', command=save_data).pack(anchor=tk.E, pady=6)

    def show_data(self):
        # 更新数据
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        con = dd.all()  # 读取通讯录信息
        index = 0
        for i in con:
            print(i)
            self.tree_view.insert('', index + 1, values=(
                i['name'], i['tel'], i['address'], i['sex'], i['email'], i['InstantMessaging']
            ))


# 查询信息
class FindFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.find_name = tk.StringVar()
        self.find_tel = tk.StringVar()
        self.status = tk.StringVar()
        tk.Label(self, text='请输入联系人任意信息：').pack(pady=5)
        tk.Entry(self, textvariable=self.find_name).pack(pady=5)
        tk.Button(self, text='确认', command=self.Find).pack(pady=10)
        tk.Label(self, textvariable=self.status).pack(pady=10)
        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):
        col = ("name", "tel", "address", "sex", "email", "InstantMessaging")
        col_value = ("姓名", "电话", "工作单位", "性别", "邮件", "即时通")
        self.tree_view = ttk.Treeview(self, show='headings', columns=col)
        self.tree_view.column('name', width=100, anchor='center')
        self.tree_view.column('tel', width=100, anchor='center')
        self.tree_view.column('address', width=100, anchor='center')
        self.tree_view.column('sex', width=100, anchor='center')
        self.tree_view.column('email', width=100, anchor='center')
        self.tree_view.column('InstantMessaging', width=90, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('tel', text='电话')
        self.tree_view.heading('address', text='工作单位')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('email', text='邮件')
        self.tree_view.heading('InstantMessaging', text='即时通')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.Find()

    def Find(self):
        find_name = self.find_name.get()
        f, con = dd.find_data_name(find_name)
        index = 0
        self.status.set('')
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        if f:
            for i in con:
                self.tree_view.insert('', index + 1, values=(
                    i['name'], i['tel'], i['address'], i['sex'], i['email'], i['InstantMessaging']
                ))
                self.find_name.set('')
            self.status.set('查询完毕')
        else:
            self.status.set('联系人不存在')
            self.find_name.set('')
