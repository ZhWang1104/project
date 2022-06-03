#  主界面设计
import tkinter as tk
from views import InsertFrame, DeleteFrame, ShowFrame, FindFrame, EditFrame


# 主界面类
class MainPage:
    # 初始化
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.title('通讯录管理系统1.0')
        width = 650
        height = 450
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(size)
        self.menupage()

    # 菜单栏（tkinter的Menu）
    def menupage(self):
        self.insert_frame = InsertFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.find_frame = ShowFrame(self.root)
        self.export_frame = FindFrame(self.root)
        self.edit_frame = EditFrame(self.root)

        MenuBar = tk.Menu(self.root)
        MenuBar.add_command(label='增加', command=self.show_insert)  # 在菜单项中加入子菜单
        MenuBar.add_command(label='展示', command=self.show_data)
        MenuBar.add_command(label='删除', command=self.show_delete)
        MenuBar.add_command(label='查询', command=self.show_export)
        MenuBar.add_command(label='编辑', command=self.show_edit)
        self.root['menu'] = MenuBar

    def show_edit(self):
        self.edit_frame.pack()
        self.find_frame.pack_forget()  # tkinter隐藏控件
        self.export_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.insert_frame.pack_forget()

    def show_insert(self):  # 遇到的问题：无法隐藏其他页面内容
        self.insert_frame.pack()
        self.find_frame.pack_forget()  # tkinter隐藏控件
        self.export_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.edit_frame.pack_forget()

    def show_data(self):
        self.find_frame.pack()
        self.insert_frame.pack_forget()  # tkinter隐藏控件
        self.export_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.edit_frame.pack_forget()

    def show_delete(self):
        self.delete_frame.pack()
        self.find_frame.pack_forget()
        self.insert_frame.pack_forget()  # tkinter隐藏控件
        self.export_frame.pack_forget()
        self.edit_frame.pack_forget()

    def show_export(self):
        self.export_frame.pack()
        self.find_frame.pack_forget()
        self.insert_frame.pack_forget()  # tkinter隐藏控件
        self.delete_frame.pack_forget()
        self.edit_frame.pack_forget()
