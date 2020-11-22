# Tk slider demo: Two sliders.
# Their sum and product are displayed in two different labels.

import tkinter as Tk

def update(event):
	z1 = x.get() + y.get()
	z2 = x.get() * y.get()
	s1.set( 'Sum = ' + str(z1))
	s2.set('Product = ' + str(z2))

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()
y = Tk.DoubleVar()
s1 = Tk.StringVar()
s2 = Tk.StringVar()

# Define widgets
S1 = Tk.Scale(root, variable = x, command = update)
S2 = Tk.Scale(root, variable = y, command = update)
L1 = Tk.Label(root, textvariable = s1)
L2 = Tk.Label(root, textvariable = s2)
B1 = Tk.Button(root, text = 'Close', command = root.quit)

# Place widgets
S1.pack(side = Tk.LEFT)
S2.pack(side = Tk.LEFT)
L1.pack(side = Tk.TOP)
L2.pack(side = Tk.TOP)
B1.pack(side = Tk.BOTTOM, fill = Tk.X)

root.mainloop()
