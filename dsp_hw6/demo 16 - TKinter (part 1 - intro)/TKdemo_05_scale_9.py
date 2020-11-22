# Tk slider demo: Slider and button.
# Uses Tk string variable.

import tkinter as Tk

def myfun():
   string1 = 'Value = ' + str(x.get())
   s.set(string1)

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
s = Tk.StringVar()

# Define widgets
S1 = Tk.Scale(root, variable = x)     
B1 = Tk.Button(root, text = 'Press to display value', command = myfun)
L1 = Tk.Label(root, textvariable = s)

# Place widgets
S1.pack()
B1.pack()
L1.pack()

root.mainloop()
