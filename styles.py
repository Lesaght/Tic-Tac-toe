from tkinter import ttk
import tkinter as tk
from constants import *

class GameStyle:
    @staticmethod
    def configure_window(window):
        window.geometry(WINDOW_SIZE)
        window.configure(bg=BG_COLOR)
        window.title(WINDOW_TITLE)
        
    @staticmethod
    def create_title(parent):
        title_frame = tk.Frame(parent, bg=BG_COLOR)
        title_frame.pack(pady=20)
        title = tk.Label(
            title_frame,
            text=WINDOW_TITLE,
            font=TITLE_FONT,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        title.pack()
        
    @staticmethod
    def style_mode_button(button, text):
        button.configure(
            text=text,
            font=('Helvetica', 12, 'bold'),
            bg=BUTTON_BG,
            fg=TEXT_COLOR,
            activebackground=BUTTON_ACTIVE_BG,
            activeforeground=TEXT_COLOR,
            bd=0,
            padx=20,
            pady=10,
            cursor="hand2"
        )
        
    @staticmethod
    def style_reset_button(button):
        button.configure(
            bg=BUTTON_ACTIVE_BG,
            fg=TEXT_COLOR,
            font=('Helvetica', 12, 'bold'),
            activebackground=BUTTON_HOVER_BG,
            activeforeground=TEXT_COLOR,
            bd=0,
            padx=30,
            pady=10,
            cursor="hand2"
        )