# Tk label demo: Two labels

import tkinter as Tk   	# for Python 3

root = Tk.Tk()

# Define label
L1 = Tk.Label(root, text = 'Hello. How are you?')
L1.pack()

# Define label
L2 = Tk.Label(root, text = 'This is another label')
L2.pack()

root.mainloop()
