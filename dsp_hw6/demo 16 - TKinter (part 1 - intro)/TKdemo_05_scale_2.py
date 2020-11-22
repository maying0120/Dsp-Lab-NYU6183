# Tk slider demo: Two sliders

import tkinter as Tk

root = Tk.Tk()

# Define two sliders
S1 = Tk.Scale(root, label = 'Slider 1')
S2 = Tk.Scale(root, label = 'Slider 2')

# Place sliders
# S1.pack()
# S2.pack()

# Alternately
S1.pack(side = Tk.LEFT)
S2.pack()

root.mainloop()

