# -*- coding: utf-8 -*-
import os
import re
import tkinter as tk
from tkinter import *  # 导入 Tkinter 库
from tkinter import ttk, scrolledtext
import threading
import easygui as a


class APKInstaller:
    def __init__(self):
        self.path = r"C:\Users\Administrator\Desktop\APK"  # 存放apk的路径
        #     #木木
        #     cmd = 'adb connect 127.0.0.1:7555'
        #     os.system(cmd)
        #     #逍遥
        #     cmd = 'adb connect 127.0.0.1:21503'
        #     os.system(cmd)
        # except:
        #     print("连接mumu或逍遥有问题")

    def install_and_open(self, device_name, apk_name):
        # 安装软件
        os.system("adb -s " + device_name + " install -r " + self.path + "\\" + apk_name)
        # 启动游戏的指令 shell  am  start -n   包名/主activity , 包名和主activity怎么获得百度一下便知
        # os.system(
        #     "adb -s " + device_name + " shell am start -n com.sanhe.clipclaps/.rebuild.act.MainActivity2")  # 自家包名就不显示了
        # 查看设备已安装的app包名
        appPackageList = os.popen('adb shell pm list packages').read()
        # print('所有包信息' + appPackageList)
        appPackageName = "com.sanhe.clipclaps"
        # 判断是否已经安装
        try:
            if appPackageName in appPackageList:
                a.msgbox(msg='安装成功', title='安装结果', ok_button='确定')
            else:
                a.msgbox(msg='安装中，请稍等！！！', title='安装结果', ok_button='确定')
        except Exception as e:
            print(e)

    def uninstall_apk(self, device_name, apk_name):
        # 卸载软件
        os.system("adb -s" + device_name + "uninstall" + apk_name)
        # 启动游戏的指令 shell  am  start -n   包名/主activity , 包名和主activity怎么获得百度一下便知
        # os.system(
        #     "adb -s " + device_name + " shell am start -n com.sanhe.clipclaps/.rebuild.act.MainActivity2")  # 自家包名就不显示了
        # 查看设备已安装的app包名
        appPackageList = os.popen('adb shell pm list packages').read()
        # print('所有包信息' + appPackageList)
        appPackageName = "com.sanhe.clipclaps"
        # 判断是否已经卸载
        try:
            if appPackageName not in appPackageList:
                a.msgbox(msg='卸载成功', title='卸载结果', ok_button='确定')
            else:
                a.msgbox(msg='卸载失败', title='卸载结果', ok_button='确定')
        except Exception as e:
            print(e)

    def get_device_list(self):
        os.system("adb devices")
        res = os.popen("adb devices").readlines()
        device_list = [sub.split('\t')[0] for sub in res[1:-1]]
        return device_list

    def get_apk_list(self):
        list_name = []
        for file in os.listdir(self.path):
            list_name.append(file)
        return list_name


# 此类用来制作界面
class APKTk(object):
    def __init__(self, APKInstaller):
        self.root = Tk()
        self.root.geometry('551x332')
        self.root.title("APK安装/卸载器")
        self.apk_name = StringVar()
        self.apk_name.set("请输入要安装的包名")
        self.apk_name1 = StringVar()
        self.apk_name1.set("请输入要卸载的包名")
        self.apkInstaller = APKInstaller
        self.select_device_list = []
        self.device_list = self.apkInstaller.get_device_list()
        self.cb_list = []
        # self.root.mainloop()

    def mul_check_box(self):
        print("制作多选框", self.device_list)
        for index, item in enumerate(self.device_list):
            self.select_device_list.append(tk.StringVar())
            cb = Checkbutton(self.root, text=item, variable=self.select_device_list[-1], onvalue=item, offvalue='')
            # cb = Checkbutton(self.root, text=item,onvalue=item,offvalue='')
            self.cb_list.append(cb)
            cb.grid(row=index, column=0, sticky='w')
            cb.select()

    # 刷新设备列表
    def refresh_data(self):
        print("refresh")
        for item in self.cb_list:
            item.grid_remove()
        self.cb_list = []
        self.device_list = self.apkInstaller.get_device_list()
        self.select_device_list = []
        self.mul_check_box()

    # 全选设备列表
    def select_all(self):
        for index, item in enumerate(self.device_list):
            self.device_list[index].set(item)

    # 安装/卸载按钮
    def install_button(self):
        button_install = Button(self.root, text="安装", command=self.install)
        button_install.grid(row=len(self.device_list) + 1, column=1)
        button_uninstall = Button(self.root, text="卸载", command=self.uninstall)
        button_uninstall.grid(row=len(self.device_list) + 2, column=1)

    # 刷新设备列表按钮
    def refresh_button(self):
        button_install = Button(self.root, text="刷新", command=self.refresh_data)
        button_install.grid(row=len(self.device_list) + 1, column=2)
        button_uninstall = Button(self.root, text="刷新", command=self.refresh_data)
        button_uninstall.grid(row=len(self.device_list) + 2, column=2)

    def input_text(self):
        entry_log = Entry(self.root, width=65, textvariable=self.apk_name)
        entry_log.grid(row=len(self.device_list) + 1, column=0, sticky='w')
        entry_logs = Entry(self.root, width=65, textvariable=self.apk_name1)
        entry_logs.grid(row=len(self.device_list) + 2, column=0, sticky='w')

    def get_apk_name(self):
        return self.apk_name.get()

    def get_apk_names(self):
        return self.apk_name1.get()

    def mainloop(self):
        self.root.mainloop()

    def install(self):
        selected_device_list = [i.get() for i in self.select_device_list if i.get()]
        print(selected_device_list)
        apkName = self.get_apk_name()
        print(apkName)

        for device in selected_device_list:
            threading.Thread(target=self.apkInstaller.install_and_open, args=(device, apkName)).start()
            print("启动" + device)

    def uninstall(self):
        selected_device_list = [i.get() for i in self.select_device_list if i.get()]
        print(selected_device_list)
        apkName = self.get_apk_names()
        print(apkName)

        for device in selected_device_list:
            threading.Thread(target=self.apkInstaller.uninstall_apk, args=(device, apkName)).start()
            print("启动" + device)


if __name__ == '__main__':
    apkInstaller = APKInstaller()
    apkTk = APKTk(apkInstaller)
    apkTk.mul_check_box()
    apkTk.input_text()
    apkTk.install_button()
    apkTk.refresh_button()
    apkTk.root.mainloop()
