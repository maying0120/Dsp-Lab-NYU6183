import tkinter as TK
from tkinter import *
import tkinter.messagebox

def fun_quit():
    print('Quit successfully!')
    root.quit()


def fun_num(event):
    s2.set(str(x2.get()))


def fun_add():
    c = float(E1.get()) * float(x2.get())
    s.set('The result is : ' + str(c))

def fun_check():
    if CheckVar1.get() == 1:
        print('The result is checked!')
    

   
root = TK.Tk()  


s = TK.StringVar()
s1 = TK.StringVar()
s2 = TK.StringVar()
x2 = TK.DoubleVar()
CheckVar1 = IntVar()

L1 = TK.Label(root, text = 'Multiplication calculator')
L2 = TK.Label(root, text = 'This is the first value : ')
L3 = TK.Label(root, text = 'Choose the second value with scale  : ')
L4 = TK.Label(root, textvariable = s1) #value_1
L5 = TK.Label(root, textvariable = s2)  #value_2
L6 = TK.Label(root, textvariable = s)  #result


B1 = TK.Button(root, text ='Quit', command = fun_quit)#quit
B2 = TK.Button(root, text ='Result', command = fun_add)#add
E1 = TK.Entry(root,textvariable = s1)#entry for value_1
S1 = TK.Scale(root, label = 'Value 2', variable = x2, command = fun_num)#scale for value 2
C1 = Checkbutton(root, text = "Check", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, command = fun_check) #checkbutton




#display
L1.pack()
L2.pack()
E1.pack()
L4.pack()
L3.pack()
S1.pack()
L5.pack()
B2.pack()
L6.pack()
C1.pack()
B1.pack(side = TK.BOTTOM) #quit button

root.mainloop() #start the infinite loop
