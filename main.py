from cell import Cell
import random
import settings
from tkinter import *  
import util


# Create the window that the game will be played in.
root = Tk()
root.configure(bg='black')
# root.geometry('WIDTHxHEIGHT')
root.geometry('1440x720')
root.title('Minesweeper Game')
root.resizable(False, False)

# Create 'Frames' to structure display of the game. Divide the window to visualize different elements
top_frame = Frame(
    root,
    bg='black', #change to different color to see the frame
    width=util.width_pct(100),
    height= util.height_pct(25) 
    )
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text='Minesweeper Game',
    font=('Arial', 48)
    )
game_title.place(
    x=util.width_pct(25),
    y=util.height_pct(1)
    )

left_frame = Frame(
    root,
    bg="black",
    width=util.width_pct(25),
    height=util.height_pct(75)
)
left_frame.place(x=0, y=180)

center_frame = Frame(
    root,
    bg="black",
    width=util.width_pct(75),
    height=util.height_pct(75)
)

center_frame.place(
    x=util.width_pct(25),
    y=util.height_pct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)
        
# Call the label from the Cell Class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0,y=0)


        
Cell.randomize_mines()


# Run the window
root.mainloop()