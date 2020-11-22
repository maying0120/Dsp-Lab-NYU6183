# keyboard_demo_03.py
# Play a sinusoid using Pyaudio and Tkinter.
# Adjust the frequency of the sinusoid by key strokes.

from math import cos, pi
import pyaudio, struct
import tkinter as Tk   	

Fs = 8000           # rate (samples/second)
f1 = 440            # f1 : frequency of sinusoid (Hz) (440 = 'middle A')
gain = 0.2 * 2**15
R = 2 ** (1.0/12.0)    # 1.05946309

def my_function(event):
    global CONTINUE
    global f1
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    if event.char == 'i':
      f1 = f1 * R       # increase frequency
    if event.char == 'd':
      f1 = f1 / R       # decrease frequency
    print('Frequency = %.2f' % f1)

# Define Tkinter root
root = Tk.Tk()
root.bind("<Key>", my_function)

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

# print('Switch to Python window.')
print('Press i to increase frequency.')
print('Press d to decrease frequency.')
print('Press q to quit.')

BLOCKLEN = 512
output_block = [0] * BLOCKLEN
theta = 0
CONTINUE = True

# root.focus_set()        # This activates the keyboard

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
