# Tk entry demo: show entry text in label upon button press.
# Uses a Tk variable.

import tkinter as Tk

def fun1():
    s.set('You entered: ' + E1.get())

root = Tk.Tk()

# Define Tk string variable
s = Tk.StringVar()

# Define widgets
L1 = Tk.Label(root, text = 'Enter text')
E1 = Tk.Entry(root)
B1 = Tk.Button(root, text = 'Click here', command = fun1)
L2 = Tk.Label(root, textvariable = s)
B2 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place widgets
L1.pack()
E1.pack()
B1.pack()
L2.pack()
B2.pack()

root.mainloop()
