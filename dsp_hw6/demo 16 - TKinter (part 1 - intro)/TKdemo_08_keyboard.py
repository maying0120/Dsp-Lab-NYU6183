# Mouse click and keyboard demo

import tkinter as Tk    # for Python 3

root = Tk.Tk()

def fun1(event):
    print('You clicked at position (%d, %d)' % (event.x, event.y))

def fun2(event):
    print('You pressed key %s' % repr(event.char))

F1 = Tk.Frame(root, width = 200, height = 100)
F1.bind("<Button-1>", fun1)		# "<Button-1>" refers to the mouse
F1.bind("<Key>", fun2)			# "<Key>" refers to the keyboard
F1.pack()
F1.focus_set()				# This activates the keyboard

root.mainloop()

