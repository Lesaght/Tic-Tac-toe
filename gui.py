import tkinter as tk
from game_logic import TicTacToe
from ai_player import AIPlayer
from game_button import GameButton
from message_handler import MessageHandler
from styles import GameStyle
from animations import GameAnimations
from auth_gui import AuthFrame
from database import Database
from constants import (
    PLAYER_X, PLAYER_O, EMPTY,
    BG_COLOR, BOARD_BG, PADDING,
    X_COLOR, O_COLOR
)

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        GameStyle.configure_window(self.window)
        
        self.db = Database()
        self.current_user = None
        self.show_auth_screen()
        
    def show_auth_screen(self):
        self.auth_frame = AuthFrame(self.window, self.on_auth_success)
        self.auth_frame.pack(expand=True, fill=tk.BOTH)
        
    def on_auth_success(self, username):
        self.current_user = username
        self.auth_frame.destroy()
        self.setup_game()
        
    def setup_game(self):
        self.game = TicTacToe()
        self.ai_mode = True
        self.buttons = []
        self.setup_ui()
        self.current_player = PLAYER_X
        self.update_mode_buttons()
        
    def setup_ui(self):
        # User info
        self.user_frame = tk.Frame(self.window, bg=BG_COLOR)
        self.user_frame.pack(pady=10)
        
        self.user_label = tk.Label(
            self.user_frame,
            text=f"Player: {self.current_user}",
            font=('Helvetica', 12, 'bold'),
            bg=BG_COLOR
        )
        self.user_label.pack()
        
        stats = self.db.get_stats(self.current_user)
        if stats:
            wins, losses, ties = stats
            stats_text = f"Stats: {wins}W/{losses}L/{ties}T"
            self.stats_label = tk.Label(
                self.user_frame,
                text=stats_text,
                font=('Helvetica', 10),
                bg=BG_COLOR
            )
            self.stats_label.pack()
        
        # Title
        GameStyle.create_title(self.window)
        
        # Rest of the UI setup remains the same
        self.mode_frame = tk.Frame(self.window, bg=BG_COLOR)
        self.mode_frame.pack(pady=PADDING)
        
        self.ai_button = tk.Button(
            self.mode_frame,
            command=self.set_ai_mode
        )
        GameStyle.style_mode_button(self.ai_button, "Play vs AI")
        self.ai_button.pack(side=tk.LEFT, padx=5)
        
        self.pvp_button = tk.Button(
            self.mode_frame,
            command=self.set_pvp_mode
        )
        GameStyle.style_mode_button(self.pvp_button, "Play vs Player")
        self.pvp_button.pack(side=tk.LEFT, padx=5)
        
        # Game board
        self.board_frame = tk.Frame(self.window, bg=BOARD_BG, padx=15, pady=15)
        self.board_frame.pack(padx=PADDING, pady=PADDING)
        
        for i in range(3):
            for j in range(3):
                button = GameButton(
                    self.board_frame,
                    row=i,
                    col=j,
                    command=lambda row=i, col=j: self.button_click(row, col)
                )
                button.grid(row=i, column=j, padx=3, pady=3)
                self.buttons.append(button)
        
        # Reset button
        self.reset_button = tk.Button(
            self.window,
            text="New Game",
            command=self.reset_game
        )
        GameStyle.style_reset_button(self.reset_button)
        self.reset_button.pack(pady=PADDING)
        
        # Logout button
        self.logout_button = tk.Button(
            self.window,
            text="Logout",
            command=self.logout
        )
        GameStyle.style_mode_button(self.logout_button, "Logout")
        self.logout_button.pack(pady=5)

    def logout(self):
        self.window.destroy()
        self.__init__()
        
    def update_stats(self, result):
        self.db.update_stats(self.current_user, result)
        stats = self.db.get_stats(self.current_user)
        if stats:
            wins, losses, ties = stats
            self.stats_label.config(text=f"Stats: {wins}W/{losses}L/{ties}T")
            
    def button_click(self, row, col):
        position = row * 3 + col
        
        if self.game.board[position] == EMPTY and not self.game.current_winner:
            self.game.make_move(position, self.current_player)
            button = self.buttons[position]
            button.set_symbol(self.current_player)
            
            GameAnimations.animate_button_click(
                button,
                self.current_player,
                X_COLOR if self.current_player == PLAYER_X else O_COLOR
            )
            
            if self.game.current_winner:
                MessageHandler.show_winner(self.current_player)
                self.update_stats("win" if self.current_player == PLAYER_X else "loss")
                return
            
            if not self.game.empty_squares():
                MessageHandler.show_tie()
                self.update_stats("tie")
                return
            
            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
            
            if self.ai_mode and self.current_player == PLAYER_O:
                self.window.after(500, self.make_ai_move)

    def make_ai_move(self):
        position = AIPlayer.get_move(self.game)
        self.game.make_move(position, PLAYER_O)
        button = self.buttons[position]
        button.set_symbol(PLAYER_O)
        
        GameAnimations.animate_button_click(button, PLAYER_O, O_COLOR)
        
        if self.game.current_winner:
            self.window.after(300, lambda: MessageHandler.show_winner("AI"))
            self.update_stats("loss")
            return
        
        if not self.game.empty_squares():
            self.window.after(300, MessageHandler.show_tie)
            self.update_stats("tie")
            return
        
        self.current_player = PLAYER_X

    def set_ai_mode(self):
        self.ai_mode = True
        self.reset_game()
        self.update_mode_buttons()

    def set_pvp_mode(self):
        self.ai_mode = False
        self.reset_game()
        self.update_mode_buttons()

    def update_mode_buttons(self):
        if self.ai_mode:
            self.ai_button.configure(bg=O_COLOR)
            self.pvp_button.configure(bg=BOARD_BG)
        else:
            self.ai_button.configure(bg=BOARD_BG)
            self.pvp_button.configure(bg=O_COLOR)

    def reset_game(self):
        self.game.reset()
        self.current_player = PLAYER_X
        for button in self.buttons:
            button.set_symbol("")

    def run(self):
        self.window.mainloop()