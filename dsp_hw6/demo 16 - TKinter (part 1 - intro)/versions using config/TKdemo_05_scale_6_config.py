# Slider demo: Slider with variable.
# The variable is displayed in a label.
# Uses configure method

import tkinter as Tk

root = Tk.Tk()

# Define Tk variable
x = Tk.DoubleVar() 		# floating point value

def update_label(event):
	L1.config(text = str(x.get()))

# Define widgets
S1 = Tk.Scale(root, variable = x, command = update_label)
L1 = Tk.Label(root)

# Place widgets
S1.pack()
L1.pack()

root.mainloop()
