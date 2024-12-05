import tkinter as tk
from tkinter import ttk
from constants import *
from styles import GameStyle
from message_handler import MessageHandler
from database import Database

class AuthFrame(tk.Frame):
    def __init__(self, master, on_auth_success):
        super().__init__(master, bg=BG_COLOR)
        self.db = Database()
        self.on_auth_success = on_auth_success
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        self.title_label = tk.Label(
            self,
            text="Welcome to Tic Tac Toe",
            font=TITLE_FONT,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        self.title_label.pack(pady=20)
        
        # Login/Register Form
        self.form_frame = tk.Frame(self, bg=BG_COLOR)
        self.form_frame.pack(pady=10)
        
        # Username
        tk.Label(
            self.form_frame,
            text="Username:",
            font=('Helvetica', 12),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=5)
        
        self.username_entry = tk.Entry(
            self.form_frame,
            font=('Helvetica', 12),
            bg=BUTTON_BG,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR
        )
        self.username_entry.pack(pady=5)
        
        # Password
        tk.Label(
            self.form_frame,
            text="Password:",
            font=('Helvetica', 12),
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=5)
        
        self.password_entry = tk.Entry(
            self.form_frame,
            show="•",
            font=('Helvetica', 12),
            bg=BUTTON_BG,
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR
        )
        self.password_entry.pack(pady=5)
        
        # Buttons
        self.button_frame = tk.Frame(self, bg=BG_COLOR)
        self.button_frame.pack(pady=20)
        
        self.login_button = tk.Button(
            self.button_frame,
            text="Login",
            command=self.login
        )
        GameStyle.style_mode_button(self.login_button, "Login")
        self.login_button.pack(side=tk.LEFT, padx=10)
        
        self.register_button = tk.Button(
            self.button_frame,
            text="Register",
            command=self.register
        )
        GameStyle.style_mode_button(self.register_button, "Register")
        self.register_button.pack(side=tk.LEFT, padx=10)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            MessageHandler.show_error("Please fill in all fields!")
            return
            
        success, message = self.db.login_user(username, password)
        if success:
            MessageHandler.show_info("Login", message)
            self.on_auth_success(username)
        else:
            MessageHandler.show_error(message)
            
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            MessageHandler.show_error("Please fill in all fields!")
            return
            
        if len(password) < 6:
            MessageHandler.show_error("Password must be at least 6 characters!")
            return
            
        success, message = self.db.register_user(username, password)
        if success:
            MessageHandler.show_info("Registration", message)
            self.login()
        else:
            MessageHandler.show_error(message)