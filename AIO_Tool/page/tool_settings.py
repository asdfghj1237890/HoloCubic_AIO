# -*- coding: utf-8 -*-
################################################################################
#
# Tool Settings Page
# Allows users to configure tool preferences like language
#
################################################################################

import tkinter as tk
from tkinter import ttk, messagebox
import util.tkutils as tku
from util.i18n import get_i18n


class ToolSettings(object):
    """
    Tool Settings page class
    """

    def __init__(self, father, engine, lock=None):
        """
        ToolSettings initialization
        :param father: Parent window
        :param engine: Engine object for component communication
        :param lock: Thread lock
        :return: None
        """
        self.m_engine = engine
        self.m_father = father
        self.i18n = get_i18n()
        self.current_language = self.i18n.get_language()
        
        self.init_ui(self.m_father)

    def init_ui(self, father):
        """
        Initialize the settings UI
        :param father: Parent container
        :return: None
        """
        # Main container with padding
        main_frame = tk.Frame(father, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text=self.i18n.t("tool_settings_title"),
            font=("Arial", 16, "bold"),
            bg="white",
            fg="#333333"
        )
        title_label.pack(pady=(0, 20))
        
        # Language settings section
        self.create_language_section(main_frame)
        
        # Restart tip
        tip_frame = tk.Frame(main_frame, bg="white")
        tip_frame.pack(fill=tk.X, pady=(20, 0))
        
        tip_label = tk.Label(
            tip_frame,
            text=self.i18n.t("restart_tip"),
            font=("Arial", 9),
            bg="white",
            fg="#666666",
            wraplength=600,
            justify=tk.LEFT
        )
        tip_label.pack(anchor=tk.W)

    def create_language_section(self, parent):
        """
        Create language selection section
        :param parent: Parent container
        :return: None
        """
        # Section frame with border
        section_frame = tk.LabelFrame(
            parent,
            text=self.i18n.t("language_label"),
            font=("Arial", 11, "bold"),
            bg="white",
            fg="#333333",
            padx=15,
            pady=15
        )
        section_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Language tip
        tip_label = tk.Label(
            section_frame,
            text=self.i18n.t("language_tip"),
            font=("Arial", 9),
            bg="white",
            fg="#666666"
        )
        tip_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Radio buttons for language selection
        self.language_var = tk.StringVar(value=self.current_language)
        
        radio_frame = tk.Frame(section_frame, bg="white")
        radio_frame.pack(fill=tk.X)
        
        # Get available languages
        available_languages = self.i18n.get_available_languages()
        
        for lang_code, lang_name in available_languages:
            rb = tk.Radiobutton(
                radio_frame,
                text=lang_name,
                variable=self.language_var,
                value=lang_code,
                font=("Arial", 10),
                bg="white",
                fg="#333333",
                activebackground="white",
                selectcolor="white",
                command=self.on_language_change
            )
            rb.pack(anchor=tk.W, pady=5)
        
        # Apply button
        button_frame = tk.Frame(section_frame, bg="white")
        button_frame.pack(fill=tk.X, pady=(15, 0))
        
        self.apply_button = tk.Button(
            button_frame,
            text=self.i18n.t("apply_button"),
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.apply_language_change
        )
        self.apply_button.pack(side=tk.LEFT)
        
        # Initially disable the apply button
        self.apply_button.config(state=tk.DISABLED)

    def on_language_change(self):
        """
        Called when language selection changes
        Enable/disable apply button based on whether language changed
        """
        selected_language = self.language_var.get()
        if selected_language != self.current_language:
            self.apply_button.config(state=tk.NORMAL)
        else:
            self.apply_button.config(state=tk.DISABLED)

    def apply_language_change(self):
        """
        Apply the language change
        """
        selected_language = self.language_var.get()
        
        if selected_language == self.current_language:
            return
        
        # Save the language preference
        if self.i18n.save_language_preference(selected_language):
            self.i18n.set_language(selected_language)
            self.current_language = selected_language
            
            # Show success message
            messagebox.showinfo(
                self.i18n.t("success_title"),
                self.i18n.t("language_changed")
            )
            
            # Disable apply button
            self.apply_button.config(state=tk.DISABLED)
        else:
            messagebox.showerror(
                "Error",
                "Failed to save language preference"
            )

    def __del__(self):
        """
        Clean up resources
        """
        pass

