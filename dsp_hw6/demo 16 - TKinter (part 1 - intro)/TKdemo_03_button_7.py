# Tk button demo: buttons change text displayed in label.
# Uses Tk string variable

import tkinter as Tk   	

def fun1():
	s1.set('The dog is brown')

def fun2():
	s1.set('The cat is red')

root = Tk.Tk()

s1 = Tk.StringVar()
s1.set('I am initialized')

# Define widgets
L1 = Tk.Label(root, textvariable = s1)
B1 = Tk.Button(root, text = 'Press me', command = fun1)
B2 = Tk.Button(root, text = 'Press me also...', command = fun2)
B3 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place widgets
L1.pack()
B1.pack(fill = Tk.X)
B2.pack(fill = Tk.X)
B3.pack(fill = Tk.X)

root.mainloop()
