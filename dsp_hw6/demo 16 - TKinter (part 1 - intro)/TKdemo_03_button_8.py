# Tk button demo: buttons to change a value.
# Uses Tk variables.

import tkinter as Tk   	

def fun1():
	x.set(x.get() + 1)
	s.set(str(x.get()))

def fun2():
	x.set(x.get() - 1)
	s.set(str(x.get()))

root = Tk.Tk()

# Define Tk variables
x = Tk.DoubleVar()              # floating point value
s = Tk.StringVar()				# text string

# Initialize TK variables
x.set(10)
s.set(str(x.get()))

# Define widgets
L1 = Tk.Label(root, textvariable = s)
B1 = Tk.Button(root, text = 'Increase', command = fun1)
B2 = Tk.Button(root, text = 'Decrease', command = fun2)
B3 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)

root.mainloop()
