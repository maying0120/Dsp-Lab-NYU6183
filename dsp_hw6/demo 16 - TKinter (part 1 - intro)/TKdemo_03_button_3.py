# Tk button demo: two buttons (horizontally filled).
# Prints text to console.

import tkinter as Tk   	

def fun1():
	print('Hello World')

def fun2():
	print('How are you?')

root = Tk.Tk()

# Define buttons
B1 = Tk.Button(root, text = 'Press me', command = fun1)
B2 = Tk.Button(root, text = 'Press me also...', command = fun2)

# Place buttons
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)

root.mainloop()
