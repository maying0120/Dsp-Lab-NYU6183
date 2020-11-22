# Tk slider demo: Slider with variable
# (but the variable is not used)

import tkinter as Tk

root = Tk.Tk()

# Define a Tk variable
x = Tk.DoubleVar()		# floating point value

# Define slider
S1 = Tk.Scale(root, variable = x)

# Place slider
S1.pack()

root.mainloop()

