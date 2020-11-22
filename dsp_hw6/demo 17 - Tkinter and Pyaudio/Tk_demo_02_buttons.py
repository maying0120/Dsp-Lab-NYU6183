# Tk_demo_02_buttons.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use buttons to adjust the frequency.

from math import cos, pi 
import pyaudio, struct
import tkinter as Tk   	

Fs = 8000           # rate (samples/second)
f1 = 200            # f1 : frequency of sinusoid (Hz)
gain = 0.2 * 2**15

def fun_up():
  global f1
  print('Up')
  f1 = f1 + 20

def fun_dn():
  global f1
  print('Down')
  f1 = f1 - 20

def fun_quit():
  global CONTINUE
  print('Good bye')
  CONTINUE = False

# Define TK root
root = Tk.Tk()

# Define widgets
Label_1 = Tk.Label(root, text = 'Frequency adjustment')
B_up = Tk.Button(root, text = 'Increase', command = fun_up)
B_dn = Tk.Button(root, text = 'Decrease', command = fun_dn)
B_quit = Tk.Button(root, text = 'Quit', command = fun_quit)

# Place widgets
Label_1.pack()
B_up.pack()
B_dn.pack()
B_quit.pack()

# Create Pyaudio object
p = pyaudio.PyAudio()
stream = p.open(
    format = pyaudio.paInt16,  
    channels = 1, 
    rate = Fs,
    input = False, 
    output = True,
    frames_per_buffer = 128)            
    # specify low frames_per_buffer to reduce latency

BLOCKLEN = 512
output_block = [0] * BLOCKLEN  # create 1D array
theta = 0
CONTINUE = True

while CONTINUE:
  root.update()
  om1 = 2.0 * pi * f1 / Fs
  for i in range(0, BLOCKLEN):
    output_block[i] = int( gain * cos(theta) )
    theta = theta + om1
  while theta > pi:
  	theta = theta - 2.0 * pi
  binary_data = struct.pack('h' * BLOCKLEN, *output_block)   # 'h' for 16 bits
  stream.write(binary_data)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
