# Tk label demo: Tk string variable

import tkinter as Tk   	# for Python 3

root = Tk.Tk()

# Define a Tk variable (string)
s1 = Tk.StringVar()
s1.set('Hello. How are you?')

# Define label
L1 = Tk.Label(root, textvariable = s1)
L1.pack()

root.mainloop()
