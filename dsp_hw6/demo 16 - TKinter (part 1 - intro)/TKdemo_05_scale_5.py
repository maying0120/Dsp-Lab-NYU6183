# Tk slider demo: Slider with variable.
# The slider value is printed to the console.

import tkinter as Tk

root = Tk.Tk()

# Define a Tk variable
x = Tk.DoubleVar()		# floating point value

def myfun1(event):
	print(x.get())

# Define slider
S1 = Tk.Scale(root, variable = x, command = myfun1)

# Place slider
S1.pack()

root.mainloop()
