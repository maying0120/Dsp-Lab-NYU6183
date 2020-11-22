# Tk entry demo: entry field and button.
# Prints entry text to console upon button press.

import tkinter as Tk

def fun1():
    print('You entered: ' + E1.get())

root = Tk.Tk()

# Define label
L1 = Tk.Label(root, text = 'Enter text')

# Define entry widget
E1 = Tk.Entry(root)

# Define button
B1 = Tk.Button(root, text = 'Click here', command = fun1)

# Place widgets
L1.pack()
E1.pack()
B1.pack()

root.mainloop()
