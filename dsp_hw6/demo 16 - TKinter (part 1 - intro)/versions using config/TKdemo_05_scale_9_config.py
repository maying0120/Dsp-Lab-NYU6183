# Slider demo: Slider and button.
# Uses configure method.

import tkinter as Tk

def myfun():
   string1 = 'Value = ' + str(x.get())
   L1.config(text = string1)

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()


# Define widgets
S1 = Tk.Scale(root, variable = x)     
B1 = Tk.Button(root, text = 'Press to display value', command = myfun)
L1 = Tk.Label(root)

# Place widgets
S1.pack()
B1.pack()
L1.pack()

root.mainloop()
