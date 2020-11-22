# TK dialog box demo

import tkinter as Tk   	
import tkinter.messagebox

def fun1():
	tkinter.messagebox.showinfo('Message box title', 'Hello World')

# For Python 2:
# import Tkinter as Tk
# import tkMessageBox
# 
# def fun1():
# 	tkMessageBox.showinfo('Message box title', 'Hello World')


root = Tk.Tk()

# Define buttons
B1 = Tk.Button(root, text = 'Press me', command = fun1)
B2 = Tk.Button(root, text = 'Quit', command = root.quit)

# Place buttons
B1.pack()
B2.pack()

root.mainloop()
