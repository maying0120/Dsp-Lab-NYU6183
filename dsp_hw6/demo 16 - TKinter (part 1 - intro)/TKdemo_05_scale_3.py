# Tk slider demo: Two sliders and a quit button

import tkinter as Tk

root = Tk.Tk()

# Define widgets
B1 = Tk.Button(root, text = 'Quit', command = root.quit)
S1 = Tk.Scale(root, label = 'Slider 1')
S2 = Tk.Scale(root, label = 'Slider 2')

# Place widgets
B1.pack(side = Tk.BOTTOM, fill = Tk.X)
S1.pack(side = Tk.LEFT)
S2.pack()

root.mainloop()
