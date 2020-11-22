# Tk slider demo: Slider with variable.
# The variable is displayed in a label.
# Uses a Tk variable.

import tkinter as Tk

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar() 		# floating point value
s = Tk.StringVar()		# text string

def update_label(event):
	s.set( str(x.get()) )

# Define widgets
S1 = Tk.Scale(root, variable = x, command = update_label)
L1 = Tk.Label(root, textvariable = s)

# Place widgets
S1.pack()
L1.pack()

root.mainloop()
