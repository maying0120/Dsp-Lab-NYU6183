# Tk button demo: simple demo.
# Prints text to console.

import tkinter as Tk   	

def fun1():
	print('Hello World')

root = Tk.Tk()

# Define button
B1 = Tk.Button(root, text = 'Press me', command = fun1)

# Place button
B1.pack()

root.mainloop()
