from tkinter import Button, Label, font
import random
import constants
import ctypes
import sys
from pydantic import BaseModel
from typing import List, ClassVar, Optional


class CellPydantic(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    # Class vars
    _objects: ClassVar[List["CellPydantic"]] = []
    cell_count: ClassVar = constants.CELL_COUNT
    cell_count_label_object: ClassVar = None

    # Instance vars
    is_mine: bool = False
    is_opened: bool = False
    is_mine_candidate: bool = False
    cell_btn_object: Optional[Button]
    x: int
    y: int

    @classmethod
    def get_all_instances(cls) -> List["CellPydantic"]:
        return cls._objects

    def assign_button_and_button_events(self, btn: Button):
        btn.bind(constants.LEFT_CLICK_STR, self.left_click_actions)  # Left Click
        btn.bind(constants.RIGHT_CLICK_STR, self.right_click_actions)  # Right Click
        self.cell_btn_object = btn

    def __init__(self, **data):
        super().__init__(**data)
        # Automatically add the instance to the class-level list
        self._objects.append(self)

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If Mines count is equal to the cells left count, player won
            if CellPydantic.cell_count == constants.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(
                    0, "Congratulations! You won the game!", "Game Over", 0
                )

        # Cancel Left and Right click events if cell is already opened:
        self.cell_btn_object.unbind(constants.LEFT_CLICK_STR)
        self.cell_btn_object.unbind(constants.RIGHT_CLICK_STR)

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x,y
        for cell in CellPydantic.get_all_instances():
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            CellPydantic.cell_count -= 1
            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length,
                fg=constants.SURROUNDED_COLORS[self.surrounded_cells_mines_length]
            )
            # Replace the text of cell count label with the newer count
            if CellPydantic.cell_count_label_object:
                CellPydantic.cell_count_label_object.configure(
                    text=f"Cells Left: {CellPydantic.cell_count}"
                )
            # If this was a mine candidate, then for safety, we should
            # configure the background color to SystemButtonFace
            self.cell_btn_object.configure(bg="SystemButtonFace")

        # Mark the cell as opened (Use is as the last line of this method)
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", "Game Over", 0)
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            CellPydantic.get_all_instances(), constants.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
            print(picked_cell)

    @staticmethod
    def assign_cell_count_label(lbl: Label):
        CellPydantic.cell_count_label_object = lbl
