# TKinter keyboard demo
# Read characters from the keyboard
# This version uses root.update

import tkinter as Tk    	# for Python 3

def my_fun(event):
	global CONTINUE
	print('You pressed key %s' % event.char)
	if event.char == 'q':
		print('Good bye')
		CONTINUE = False

# Define Tk root
root = Tk.Tk()

# Bind keyboard to root
root.bind("<Key>", my_fun)		# "<Key>" refers to the keyboard

# root.focus_set()				# Might not be necessary

CONTINUE = True
while CONTINUE:
	root.update()

