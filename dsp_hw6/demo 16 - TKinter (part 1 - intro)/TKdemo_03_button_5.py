# Tk button demo: includes quit button.
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
B3 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place buttons
B1.pack()
B2.pack()
B3.pack()

root.mainloop()
