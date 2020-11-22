# Tk slider demo: Two sliders.
# Their sum is displayed in a label.
# Uses Tk string variable.

import tkinter as Tk

def update_sum(event):
	z = x.get() + y.get()
	s.set('Sum = ' + str(z))

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
y = Tk.DoubleVar()
s = Tk.StringVar()

# Define widgets
S1 = Tk.Scale(root, variable = x, command = update_sum)
S2 = Tk.Scale(root, variable = y, command = update_sum)
L1 = Tk.Label(root, textvariable = s)

# Place widgets
L1.pack(side = Tk.BOTTOM)
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)

root.mainloop()
