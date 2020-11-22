# Tk label demo: Minimal demo

import tkinter as Tk   	# for Python 3

root = Tk.Tk()

# Define the label
L1 = Tk.Label(root, text = 'Hello. How are you?')

# Place the label
L1.pack()

root.mainloop()
