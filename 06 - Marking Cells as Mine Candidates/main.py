from cell import CellPydantic
from ui import MineSweeperUI


if __name__ == "__main__":
    app = MineSweeperUI()
    # Call the label from the Cell class
    CellPydantic.assign_cell_count_label(app.cells_left_label)
    CellPydantic.cell_count_label_object.place(x=0, y=0)
    CellPydantic.randomize_mines()
    app.mainloop()
