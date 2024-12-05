import tkinter as tk
from constants import (
    BUTTON_FONT, BUTTON_WIDTH, BUTTON_HEIGHT,
    BUTTON_BG, BUTTON_HOVER_BG, TEXT_COLOR,
    X_COLOR, O_COLOR
)

class GameButton(tk.Button):
    def __init__(self, master, row, col, command):
        super().__init__(
            master,
            text="",
            font=BUTTON_FONT,
            width=BUTTON_WIDTH,
            height=BUTTON_HEIGHT,
            bg=BUTTON_BG,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER_BG,
            activeforeground=TEXT_COLOR,
            relief=tk.FLAT,
            borderwidth=1,
            cursor="hand2",
            command=command
        )
        self.row = row
        self.col = col
        
        # Bind hover events
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)
        
    def on_enter(self, event):
        if not self.cget('text'):
            self.configure(bg=BUTTON_HOVER_BG)
            
    def on_leave(self, event):
        if not self.cget('text'):
            self.configure(bg=BUTTON_BG)
            
    def set_symbol(self, symbol):
        self.configure(
            text=symbol,
            fg=X_COLOR if symbol == "X" else O_COLOR if symbol == "O" else TEXT_COLOR,
            bg=BUTTON_BG
        )