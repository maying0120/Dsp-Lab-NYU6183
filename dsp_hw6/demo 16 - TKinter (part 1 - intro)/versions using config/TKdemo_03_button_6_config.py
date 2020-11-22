# Tk button demo: buttons change text displayed in label.
# Uses configure method.

import tkinter as Tk   	

def fun1():
	L1.configure(text = 'The dog is brown')

def fun2():
	L1.configure(text = 'The cat is red')

root = Tk.Tk()

# Define widgets
L1 = Tk.Label(root, text = 'Press the buttons')
B1 = Tk.Button(root, text = 'Press me', command = fun1)
B2 = Tk.Button(root, text = 'Press me also...', command = fun2)
B3 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)

root.mainloop()
