# Tk_demo_03_slider.py
# TKinter demo
# Play a sinusoid using Pyaudio. Use slider to adjust the frequency.

from math import cos, pi 
import pyaudio, struct
import tkinter as Tk   	

def fun_quit():
  global CONTINUE
  print('Good bye')
  CONTINUE = False

Fs = 8000     # rate (samples/second)
gain = 0.2 * 2**15

# Define Tkinter root
root = Tk.Tk()

# Define Tk variable
f1 = Tk.DoubleVar()

# Initialize Tk variable
f1.set(200)   # f1 : frequency of sinusoid (Hz)

# Define widgets
S1 = Tk.Scale(root, label = 'Frequency', variable = f1, from_ = 100, to = 400, tickinterval = 100)
B_quit = Tk.Button(root, text = 'Quit', command = fun_quit)

# Place widgets
S1.pack()
B_quit.pack(fill = Tk.X)

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

BLOCKLEN = 256
output_block = [0] * BLOCKLEN
theta = 0
CONTINUE = True

while CONTINUE:
  root.update()
  om1 = 2.0 * pi * f1.get() / Fs
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
