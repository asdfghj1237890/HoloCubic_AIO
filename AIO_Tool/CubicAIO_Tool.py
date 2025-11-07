# -*- coding: utf-8 -*-
################################################################################
#
# Author: ClimbSnail(HQ)
# original source is here.
#   https://github.com/ClimbSnail/HoloCubic_AIO_Tool
# 
#
################################################################################

from util.common import *
import util.massagehead as mh
from page.videotool import VideoTool
from page.download_debug import DownloadDebug
from page.setting import Setting
from page.help import Helper
from page.images_converter import ImagesConverter 
from page.filemanager import FileManager
from page.tool_settings import ToolSettings
from util.i18n import get_i18n

import os
import sys
import tkinter as tk
import util.tkutils as tku
from tkinter import ttk
from tkinter import messagebox
import requests
import re

# Get the base path for resources (works for both frozen exe and script)
def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Engine(object):
    """
    引擎
    """

    def __init__(self, root):
        """
        Engine initialization
        :param root: Window widget
        """
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        icon_path = get_resource_path("image/holo_256.ico")
        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
        
        # Initialize i18n
        self.i18n = get_i18n()
        
        # Create output directory for file conversion
        try:
            dir_path = os.path.join("OutFile", "Cache")
            os.makedirs(dir_path)
        except Exception as e:
            pass

        self.width = 700
        self.height = 500

        # Tab manager
        self.m_tab_manager = ttk.Notebook(self.root)

        # Download Debug page
        self.m_debug_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_debug_tab, text=self.i18n.t("tab_download_debug"))
        self.m_debug_tab_windows = DownloadDebug(self.m_debug_tab, self)

        # Device Settings page
        self.m_setting_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_setting_tab, text=self.i18n.t("tab_setting"))
        self.m_setting_tab_windows = Setting(self.m_setting_tab, self)

        # File Manager page
        self.m_file_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_file_tab, text=self.i18n.t("tab_file_manager"))
        self.m_file_tab_windows = FileManager(self.m_file_tab, self)

        # Image Converter page
        self.m_image_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_image_tab, text=self.i18n.t("tab_image_converter"))
        self.m_image_tab_windows = ImagesConverter(self.m_image_tab, self)

        # Video Converter page
        self.m_video_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_video_tab, text=self.i18n.t("tab_video_converter"))
        self.m_video_tab_windows = VideoTool(self.m_video_tab, self)

        # Screen Share page
        self.m_srceen_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_srceen_tab, text=self.i18n.t("tab_screen_share"))

        # Help page
        self.m_help_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_help_tab, text=self.i18n.t("tab_help"))
        self.m_help_tab_windows = Helper(self.m_help_tab, self)

        # Tool Settings page (new)
        self.m_tool_settings_tab = tk.Frame(self.m_tab_manager, bg="white")
        self.m_tab_manager.add(self.m_tool_settings_tab, text=self.i18n.t("tab_tool_settings"))
        self.m_tool_settings_tab_windows = ToolSettings(self.m_tool_settings_tab, self)

        self.m_tab_manager.pack(expand=True, fill=tk.BOTH)
    
    def OnThreadMessage(self, fromwho, towho, action, param = None):
        """
        引擎的调度函数 控件利用此函数可间接操作或者获取其他控件的对应资源
        :param fromwho:表示调用者
        :param towho:表示请求操作的控件
        :param action:表示请求操作的操作类型
        :param param:操作请求所携带的参数(根据具体请求来指定参数类型)
        """
        print(fromwho, towho, action, param)
        #info = fromwho+" "+towho+" "+action+" "+param
        #self.OnThreadMessage(mh.M_ENGINE, mh.M_SYSINFO, mh.A_INFO_PRINT, info+"\n")

        if towho == mh.M_DOWNLOAD_DEBUG: # 下载模块操作请求
            self.m_debug_tab_windows.api(action, param)    # 处理消息

        elif towho == mh.M_SETTING: # 设置模块操作请求
            self.m_modelManager.api(action, param)

    def on_closing(self):
        """
        Trigger function when closing main window
        :return: None
        """
        if self.m_file_tab_windows != None:
            self.m_file_tab_windows.__del__()
            del self.m_file_tab_windows
            self.m_file_tab_windows = None

        # if messagebox.askokcancel("Quit", "Do you want to quit?"):
        self.root.destroy()

        if self.m_debug_tab_windows != None:
            del self.m_debug_tab_windows
            self.m_debug_tab_windows = None

        if self.m_setting_tab_windows != None:
            del self.m_setting_tab_windows
            self.m_setting_tab_windows = None
        
        if self.m_tool_settings_tab_windows != None:
            del self.m_tool_settings_tab_windows
            self.m_tool_settings_tab_windows = None

    def OnThreadMessage(self, fromwho, towho, action, param=None):
        """
        引擎的调度函数 控件利用此函数可间接操作或者获取其他控件的对应资源（用函数模拟网络通信模型）
        :param fromwho:表示调用者
        :param towho:表示请求操作的控件
        :param action:表示请求操作的操作类型
        :param param:操作请求所携带的参数(根据具体请求来指定参数类型)
        """
        print(fromwho, towho, action, param)

        if towho == mh.M_ENGINE and action == mh.A_UPDATALANG:  # 更新请求
            self.m_modelManager.api(mh.A_UPDATALANG)  # 按钮语言更新

    def __del__(self):
        """
        Release resources
        """
        # del self.m_debug_tab_windows
        self.m_debug_tab_windows = None

        if self.m_file_tab_windows != None:
            self.m_file_tab_windows.__del__()
            del self.m_file_tab_windows
            self.m_file_tab_windows = None
        
        if self.m_tool_settings_tab_windows != None:
            del self.m_tool_settings_tab_windows
            self.m_tool_settings_tab_windows = None

def get_version():
    TOOL_VERSION_INFO_URL = "http://climbsnail.cn:5001/holocubicAIO/sn/v1/version/tool"
    try:
        response = requests.get(TOOL_VERSION_INFO_URL, timeout=3) # , verify=False
        new_version_info = re.findall(r'AIO_TOOL_VERSION v\d{1,2}\.\d{1,2}\.\d{1,2}', response.text)
        new_version = new_version_info[0].split(" ")[1]
        if TOOL_VERSION == new_version:
            return "[已是最新版本]"
        else:
            return "[推荐升级最新版本 "+ new_version +"]"
    except Exception as err:
        print(err)
        return "[无法获取到最新版本]"


if __name__ == '__main__':
    tool_windows = tk.Tk()  # 创建窗口对象的背景色
    tool_windows.title("HoloCubic_AIO Tools\t  " + TOOL_VERSION)  # 窗口名
    tool_windows.geometry('1000x655+10+10')
    tool_windows.resizable(False, False)  # 设置窗体不可改变大小
    engine = Engine(tool_windows)
    tku.center_window(tool_windows)  # 将窗体移动到屏幕中央
    tool_windows.title("HoloCubic_AIO Tools\t  " + TOOL_VERSION + " " + get_version())  # 窗口名

    # 进入消息循环 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    tool_windows.mainloop()
