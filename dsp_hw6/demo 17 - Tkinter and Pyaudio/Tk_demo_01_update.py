# Tk_demo_01_update.py
# TKinter demo
# The .update function

import tkinter as Tk   	

def fun_up():
  global x
  x = x + 1
  print('Increased to', x)

def fun_down():
  global x
  x = x - 1
  print('Decreased to', x)

def fun_quit():
  global CONTINUE
  print('Good bye')
  CONTINUE = False

# Define TK root
root = Tk.Tk()

# Define widgets
Label_1 = Tk.Label(root, text = 'Value adjustment')
B_up = Tk.Button(root, text = 'Increase', command = fun_up)
B_down = Tk.Button(root, text = 'Decrease', command = fun_down)
B_quit = Tk.Button(root, text = 'Quit', command = fun_quit)

# Place widgets
Label_1.pack()
B_up.pack()
B_down.pack()
B_quit.pack()

x = 200            # value to be adjusted
print('x = ', x)

CONTINUE = True

while CONTINUE:
  root.update()

print('* Finished')

