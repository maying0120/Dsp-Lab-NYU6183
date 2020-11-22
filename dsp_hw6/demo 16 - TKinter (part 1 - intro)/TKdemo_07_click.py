# Mouse click demo

import tkinter as Tk    # for Python 3

root = Tk.Tk()

def myfun1(event):
    print('You clicked at position (%d, %d)' % (event.x, event.y))

F1 = Tk.Frame(root, width = 200, height = 100)
F1.bind("<Button-1>",  myfun1)		# "<Button-1>" refers to the mouse
F1.pack()

root.mainloop()
