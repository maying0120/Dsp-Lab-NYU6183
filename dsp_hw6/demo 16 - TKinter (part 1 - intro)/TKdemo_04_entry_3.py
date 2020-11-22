# Tk entry demo: entry and button.
# Prints entry text to console upon button press.
# Uses a Tk variable.

import tkinter as Tk

def fun1():
    print('You entered: ' + s.get())

root = Tk.Tk()

# Define Tk variable
s = Tk.StringVar()

# Define widgets
L1 = Tk.Label(root, text = 'Enter text')
E1 = Tk.Entry(root, textvariable = s)
B1 = Tk.Button(root, text = 'Click here', command = fun1)

# Place widgets
L1.pack()
E1.pack()
B1.pack()

root.mainloop()
