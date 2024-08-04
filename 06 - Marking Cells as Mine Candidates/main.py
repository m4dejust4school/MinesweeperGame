from tkinter import *
from cell import CellPydantic
import constants
import utils


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{constants.WIDTH}x{constants.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=constants.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utils.width_prct(25), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25),
)

for x in range(constants.GRID_SIZE):
    for y in range(constants.GRID_SIZE):
        c = CellPydantic(x=x, y=y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
# Call the label from the Cell class
CellPydantic.create_cell_count_label(left_frame)
CellPydantic.cell_count_label_object.place(
    x=0, y=0
)

CellPydantic.randomize_mines()


# Run the window
root.mainloop()
