# keyboard_demo_05.py
# Play a sinusoid using Pyaudio and Tkinter.
# Adjust the frequency and amplitude of the sinusoid by key strokes.

from math import cos, pi, fabs
import pyaudio, struct
import tkinter as Tk   	

Fs = 8000           # rate (samples/second)
f1 = 440            # f1 : frequency of sinusoid (Hz) (440 = 'middle A')
gain = 0.2 * 2**15
R = 2 ** (1.0/12.0)    # 1.05946309

MAXGAIN = 2**15-1  # Maximum allowed gain (because WIDTH = 2)

def my_function(event):
    global CONTINUE
    global f1, gain
    print('You pressed ' + event.char)
    if event.char == 'q':
      print('Good bye')
      CONTINUE = False
    if event.char == 'i':
      f1 = f1 * R       # increase frequency
    if event.char == 'd':
      f1 = f1 / R       # decrease frequency
    if event.char == 'l':
      gain = gain * 1.3
    if event.char == 's':
      gain = gain / 1.3
    if fabs(gain) > MAXGAIN:     # fabs : floating-point absolute value
      gain = MAXGAIN
      print('Maximum gain attained')
    f1_str.set('Frequency = %.2f' % f1)
    gain_str.set('Gain = %.2f' % gain)

# Define Tkinter root
root = Tk.Tk()
root.bind("<Key>", my_function)

f1_str = Tk.StringVar()
gain_str = Tk.StringVar()

f1_str.set('Frequency = %.2f' % f1)
gain_str.set('Gain = %.2f' % gain)

label_freq = Tk.Label(root, textvariable = f1_str)
label_freq.pack()

label_gain = Tk.Label(root, textvariable = gain_str)
label_gain.pack()

label_explain = Tk.Label(root, text = 'freq (i/d) ; gain (l/s) ; q to quit')
label_explain.pack()

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

print('Switch to Python window.')
print('Use i to increase frequency.')
print('Use d to decrease frequency.')
print('Use l to increase gain (louder).')
print('Use s to decrease gain (softer).')
print('Press q to quit.')

BLOCKLEN = 512
output_block = [0] * BLOCKLEN
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
