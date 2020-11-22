# Tk slider demo: Two sliders and a button.

import tkinter as Tk

def myfun():
   string1 = 'Sum = ' + str(x.get() + y.get())
   s.set(string1)

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
y = Tk.DoubleVar()
s = Tk.StringVar()

s.set('Click the button')

# Define widgets
S1 = Tk.Scale(root, variable = x)
S2 = Tk.Scale(root, variable = y)
B1 = Tk.Button(root, text = 'Add', command = myfun)
L1 = Tk.Label(root, textvariable = s)

# Place widgets
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)
B1.pack(side = Tk.LEFT)
L1.pack(side = Tk.RIGHT)

root.mainloop()
