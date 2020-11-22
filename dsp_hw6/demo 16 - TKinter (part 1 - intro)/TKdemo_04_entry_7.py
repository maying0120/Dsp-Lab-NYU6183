# Tk entry demo: horizontal widgets

import tkinter as Tk   	# for Python 3

root = Tk.Tk()

# Define widgets
L1 = Tk.Label(root, text = 'Enter text:')
E1 = Tk.Entry(root)

# Place widgets
L1.pack(side = Tk.LEFT)
E1.pack(side = Tk.RIGHT)

root.mainloop()