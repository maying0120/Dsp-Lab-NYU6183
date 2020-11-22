# Tk entry demo: show entry text in label with continuous update.
# Use Tk variable

import tkinter as Tk

root = Tk.Tk()

# Define Tk string variable
s = Tk.StringVar()

# Define widgets
L1 = Tk.Label(root, text = 'Enter text')
E1 = Tk.Entry(root, textvariable = s)
L2 = Tk.Label(root, textvariable = s)

# Place widgets
L1.pack()
E1.pack()
L2.pack()

root.mainloop()
