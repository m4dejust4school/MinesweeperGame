import tkinter as tk
import constants
from cell import CellPydantic
from tkinter import font as tkfont


class MineSweeperUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{constants.WIDTH}x{constants.HEIGHT}")
        self.title("Minesweeper Game")
        self.resizable(False, False)
        self.configure(bg=constants.WINDOW_BG_COLOR)

        self.title_font = tkfont.Font(
            family=constants.FONT_FAMILY, size=24, weight="bold"
        )
        self.label_font = tkfont.Font(family=constants.FONT_FAMILY, size=14)

        # Create title label
        title_label = tk.Label(
            self,
            text="MineSweeper Game",
            font=self.title_font,
            fg="#FFFFFF",
            bg="#2E2E2E",
        )
        title_label.pack(pady=20)

        # Create Cells left label
        self.cells_left_label = tk.Label(
            self,
            text="Select a button to start!",
            font=self.label_font,
            fg="#FFFFFF",
            bg="#2E2E2E",
        )
        self.cells_left_label.pack(side="right", anchor="w")

        # Placeholder for game grid or other widgets
        game_frame = tk.Frame(self, bg="#3E3E3E")
        game_frame.pack(side="right", expand=True, fill="both", padx=20, pady=10)

        for x in range(constants.GRID_SIZE):
            for y in range(constants.GRID_SIZE):
                c = CellPydantic(x=x, y=y)
                btn = tk.Button(game_frame, text="", width=12, height=4)

                c.assign_button_and_button_events(btn)
                btn.grid(row=x, column=y, padx=5, pady=5)
