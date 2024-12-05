from tkinter import messagebox
from constants import WINDOW_TITLE

class MessageHandler:
    @staticmethod
    def show_winner(player):
        title = f"{WINDOW_TITLE} - Game Over"
        if player == "AI":
            messagebox.showinfo(title, "AI wins! 🤖")
        else:
            messagebox.showinfo(title, f"Player {player} wins! 🎉")

    @staticmethod
    def show_tie():
        messagebox.showinfo(f"{WINDOW_TITLE} - Game Over", "It's a tie! 🤝")

    @staticmethod
    def show_error(message):
        messagebox.showerror(f"{WINDOW_TITLE} - Error", message)
        
    @staticmethod
    def show_info(title, message):
        messagebox.showinfo(title, message)