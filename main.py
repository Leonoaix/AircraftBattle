from tkinter import *
from myGame import *

root = Tk()

btn = Button(root, text="Start", command=aircraft_battle)
btn.pack()

root.mainloop()