import tkinter as tk
from constants import MOVE_DURATION

class GameAnimations:
    @staticmethod
    def animate_button_click(button, symbol, final_color):
        # Flash animation
        original_bg = button.cget('bg')
        button.configure(bg=final_color)
        
        def reset_color():
            button.configure(bg=original_bg)
            
        button.after(100, reset_color)
        
        # Symbol appear animation
        for i in range(0, 101, 20):
            def update_opacity(opacity=i):
                color = final_color if opacity == 100 else f"#{int(opacity/100 * 255):02x}{int(opacity/100 * 255):02x}{int(opacity/100 * 255):02x}"
                button.configure(fg=color)
                
            button.after(int(MOVE_DURATION * (i/100)), update_opacity)
            
    @staticmethod
    def highlight_win(buttons, winning_combo):
        def flash(count=0):
            if count >= 6:  # Flash 3 times (6 state changes)
                return
                
            for idx in winning_combo:
                buttons[idx].configure(
                    bg=BUTTON_ACTIVE_BG if count % 2 == 0 else BUTTON_BG
                )
            
            buttons[0].after(300, lambda: flash(count + 1))
            
        flash()