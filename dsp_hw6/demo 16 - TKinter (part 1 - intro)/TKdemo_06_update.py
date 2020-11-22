# Tk demo: Use root.update instead of root.mainloop

import tkinter as Tk   	

def fun1():
	print('Hello World')

def fun2():
	print('How are you?')

def fun_quit():
	global PLAY
	print('Good bye')
	PLAY = False

root = Tk.Tk()

# Define buttons
B1 = Tk.Button(root, text = 'Press me', command = fun1)
B2 = Tk.Button(root, text = 'Press me also...', command = fun2)
B3 = Tk.Button(root, text = 'Quit', command = fun_quit)

# Place buttons
B1.pack()
B2.pack()
B3.pack()

# An alternative to root.mainloop() is to use root.update

PLAY = True
while PLAY:
  root.update()
