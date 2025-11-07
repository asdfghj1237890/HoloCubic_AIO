# -*- coding: utf-8 -*-
################################################################################
#
# Author: ClimbSnail(HQ)
# original source is here.
#   https://github.com/ClimbSnail/HoloCubic_AIO_Tool
# 
#
################################################################################

import tkinter as tk
import util.tkutils as tku
from util.i18n import get_i18n


class Helper(object):
    """
    帮助信息页类
    """

    def __init__(self, father, engine, lock=None):
        """
        DownloadDebug初始化
        :param father:父类窗口
        :param engine:引擎对象，用于推送与其他控件的请求
        :param lock:线程锁
        :return:None
        """
        self.m_engine = engine  # 负责各个组件之间数据调度的引擎
        self.m_father = father  # 保存父窗口
        self.i18n = get_i18n()
        self.init_info(self.m_father)

    def init_info(self, father):
        """
        初始化信息打印框
        :param father: 父容器
        :return: None
        """
        info_width = father.winfo_width()
        info_height = father.winfo_height() / 2

        info = self.i18n.t("help_info")

        self.m_project_info = tk.Text(father, height=45, width=140)
        self.m_project_info.tag_configure('bold_italics',
                                          font=('Arial', 12, 'bold', 'italic'))
        self.m_project_info.tag_configure('big', font=('Verdana', 16, 'bold'))
        self.m_project_info.tag_configure('color', foreground='#476042',
                                          font=('Tempus Sans ITC', 12, 'bold'))

        self.m_project_info.pack()
        self.m_project_info.config(state=tk.NORMAL)
        self.m_project_info.insert(tk.END, info, 'big')
        self.m_project_info.config(state=tk.DISABLED)
