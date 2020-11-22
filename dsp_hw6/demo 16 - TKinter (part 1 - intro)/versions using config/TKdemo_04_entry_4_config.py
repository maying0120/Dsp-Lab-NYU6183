# Tk entry demo: show entry text in label upon button press.
# Use configure method.

import tkinter as Tk

def fun1():
    L2.configure(text = 'You entered: ' + E1.get())

root = Tk.Tk()

# Define widgets
L1 = Tk.Label(root, text = 'Enter text')
E1 = Tk.Entry(root)
B1 = Tk.Button(root, text = 'Click here', command = fun1)
L2 = Tk.Label(root)
B2 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place widgets
L1.pack()
E1.pack()
B1.pack()
L2.pack()
B2.pack()

root.mainloop()
