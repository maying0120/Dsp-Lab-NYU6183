# Key stroke demo

import tkinter as Tk    # for Python 3

root = Tk.Tk()

def my_fun(event):
    print(type(event))
    print(type(event.char))
    print('You pressed key %s' % event.char)
    if event.char == 'q':
    	print('Good bye')
    	# root.quit()      
    	root.destroy()
    	# Note: Either root.quit or root.destory work

root.bind("<Key>", my_fun)		# "<Key>" refers to the keyboard

# root.focus_set()				# Might not be necessary

root.mainloop()

