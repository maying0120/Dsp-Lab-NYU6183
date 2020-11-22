# Tk entry demo: Minimal demo.
# Does not do anything.

import tkinter as Tk   	# for Python 3

root = Tk.Tk()

# Define label
L1 = Tk.Label(root, text = 'Enter text')

# Define entry widget
E1 = Tk.Entry(root)

# Place widgets
L1.pack()
E1.pack()

root.mainloop()
