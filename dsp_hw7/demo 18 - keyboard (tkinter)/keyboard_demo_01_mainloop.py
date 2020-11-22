# TKinter keyboard demo
# Read characters from the keyboard
# This version uses root.mainloop

import tkinter as Tk    	# for Python 3

def my_fun(event):
    print(event)
    print(type(event))
    print(type(event.char))
    print('You pressed key %s' % event.char)
    if event.char == 'q':
    	print('Good bye')
    	root.destroy()
    	root.quit()      
    	# Note: root.quit and root.destory may not both be needed

# Define Tk root
root = Tk.Tk()

# Bind keyboard to root
root.bind("<Key>", my_fun)		# "<Key>" refers to the keyboard

# root.focus_set()				# This activates the keyboard

root.mainloop()
