import pyaudio, struct
import numpy as np
from scipy import signal
from math import sin, cos, pi
import tkinter as Tk    

BLOCKLEN   = 64        # Number of frames per block
WIDTH       = 2         # Bytes per sample
CHANNELS    = 1         # Mono
RATE        = 8000      # Frames per second

MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

# Parameters
Ta = 2      # Decay time (seconds)
f1 = 440            # f1 : frequency of sinusoid (Hz) (440 = 'middle A')
R = 2 ** (1.0/12.0)    # 1.05946309

print('You can press a s d f g h j k l z x c')
#specified frequencies for other notes in this octave
fa = f1 * R
fs = fa * R
fd = fs * R
ff = fd * R
fg = ff * R
fh = fg * R
fj = fh * R
fk = fj * R
fl = fk * R
fz = fl * R
fx = fz * R
fc = fx * R


# Pole radius and angle
r = 0.01**(1.0/(Ta*RATE))       # 0.01 for 1 percent amplitude
oma = 2.0 * pi * float(fa)/RATE
oms = 2.0 * pi * float(fs)/RATE
omd = 2.0 * pi * float(fd)/RATE
omf = 2.0 * pi * float(ff)/RATE
omg = 2.0 * pi * float(fg)/RATE
omh = 2.0 * pi * float(fh)/RATE
omj = 2.0 * pi * float(fj)/RATE
omk = 2.0 * pi * float(fk)/RATE
oml = 2.0 * pi * float(fl)/RATE
omz = 2.0 * pi * float(fz)/RATE
omx = 2.0 * pi * float(fx)/RATE
omc = 2.0 * pi * float(fc)/RATE


# Filter coefficients (second-order IIR)
a_a = [1, -2*r*cos(oma), r**2]
b_a = [r*sin(oma)]
a_s = [1, -2*r*cos(oms), r**2]
b_s = [r*sin(oms)]
a_d = [1, -2*r*cos(omd), r**2]
b_d = [r*sin(omd)]
a_f = [1, -2*r*cos(omf), r**2]
b_f = [r*sin(omf)]
a_g = [1, -2*r*cos(omg), r**2]
b_g = [r*sin(omg)]
a_h = [1, -2*r*cos(omh), r**2]
b_h = [r*sin(omh)]
a_j = [1, -2*r*cos(omj), r**2]
b_j = [r*sin(omj)]
a_k = [1, -2*r*cos(omk), r**2]
b_k = [r*sin(omk)]
a_l = [1, -2*r*cos(oml), r**2]
b_l = [r*sin(oml)]
a_z = [1, -2*r*cos(omz), r**2]
b_z = [r*sin(omz)]
a_x = [1, -2*r*cos(omx), r**2]
b_x = [r*sin(omx)]
a_c = [1, -2*r*cos(omc), r**2]
b_c = [r*sin(omc)]





ORDER = 2   # filter order
#initialize the state for filters
states_a = np.zeros(ORDER)
states_s = np.zeros(ORDER)
states_d = np.zeros(ORDER)
states_f = np.zeros(ORDER)
states_g = np.zeros(ORDER)
states_h = np.zeros(ORDER)
states_j = np.zeros(ORDER)
states_k = np.zeros(ORDER)
states_l = np.zeros(ORDER)
states_z = np.zeros(ORDER)
states_x = np.zeros(ORDER)
states_c = np.zeros(ORDER)

#creat inputs
x_a = np.zeros(BLOCKLEN)
x_s = np.zeros(BLOCKLEN)
x_d = np.zeros(BLOCKLEN)
x_f = np.zeros(BLOCKLEN)
x_g = np.zeros(BLOCKLEN)
x_h = np.zeros(BLOCKLEN)
x_j = np.zeros(BLOCKLEN)
x_k = np.zeros(BLOCKLEN)
x_l = np.zeros(BLOCKLEN)
x_z = np.zeros(BLOCKLEN)
x_x = np.zeros(BLOCKLEN)
x_c = np.zeros(BLOCKLEN)


# Open the audio output stream
p = pyaudio.PyAudio()
PA_FORMAT = pyaudio.paInt16
stream = p.open(
        format      = PA_FORMAT,
        channels    = CHANNELS,
        rate        = RATE,
        input       = False,
        output      = True,
        frames_per_buffer = 128)

#initialize the flags
CONTINUE = True
KEY_a = False
KEY_s = False
KEY_d = False
KEY_f = False
KEY_g = False
KEY_h = False
KEY_j = False
KEY_k = False
KEY_l = False
KEY_z = False
KEY_x = False
KEY_c = False

def my_function(event):
    global CONTINUE
    global KEY_a
    global KEY_s
    global KEY_d
    global KEY_f
    global KEY_g
    global KEY_h
    global KEY_j
    global KEY_k
    global KEY_l
    global KEY_z
    global KEY_x
    global KEY_c
    
    print('You pressed ' + event.char)
    if event.char == 'a':KEY_a = True
    if event.char == 's':KEY_s = True
    if event.char == 'd':KEY_d = True
    if event.char == 'f':KEY_f = True
    if event.char == 'g':KEY_g = True
    if event.char == 'h':KEY_h = True
    if event.char == 'j':KEY_j = True
    if event.char == 'k': KEY_k = True
    if event.char == 'l':KEY_l = True
    if event.char == 'z':KEY_z = True
    if event.char == 'x':KEY_x = True
    if event.char == 'c':KEY_c = True
    
    if event.char == 'q': #for quiting the program
      print('Good bye')
      CONTINUE = False

root = Tk.Tk()
root.bind("<Key>", my_function)

print('Press keys for sound.')
print('Press "q" to quit')

while CONTINUE:
    root.update()

    if KEY_a and CONTINUE:x_a[0] = 10000.0
    if KEY_s and CONTINUE:x_s[0] = 10000.0
    if KEY_d and CONTINUE:x_d[0] = 10000.0
    if KEY_f and CONTINUE: x_f[0] = 10000.0
    if KEY_g and CONTINUE: x_g[0] = 10000.0
    if KEY_h and CONTINUE: x_h[0] = 10000.0
    if KEY_j and CONTINUE:x_j[0] = 10000.0
    if KEY_k and CONTINUE:x_k[0] = 10000.0
    if KEY_l and CONTINUE:x_l[0] = 10000.0
    if KEY_z and CONTINUE:x_z[0] = 10000.0
    if KEY_x and CONTINUE: x_x[0] = 10000.0
    if KEY_c and CONTINUE:x_c[0] = 10000.0
    #play the note
    [a, states_a] = signal.lfilter(b_a, a_a, x_a, zi = states_a)
    [s, states_s] = signal.lfilter(b_s, a_s, x_s, zi = states_s)
    [d, states_d] = signal.lfilter(b_d, a_d, x_d, zi = states_d)
    [f, states_f] = signal.lfilter(b_f, a_f, x_f, zi = states_f)
    [g, states_g] = signal.lfilter(b_g, a_g, x_g, zi = states_g)
    [h, states_h] = signal.lfilter(b_h, a_h, x_h, zi = states_h)
    [j, states_j] = signal.lfilter(b_j, a_j, x_j, zi = states_j)
    [k, states_k] = signal.lfilter(b_k, a_k, x_k, zi = states_k)
    [l, states_l] = signal.lfilter(b_l, a_l, x_l, zi = states_l)
    [z, states_z] = signal.lfilter(b_z, a_z, x_z, zi = states_z)
    [x, states_x] = signal.lfilter(b_x, a_x, x_x, zi = states_x)
    [c, states_c] = signal.lfilter(b_c, a_c, x_c, zi = states_c)
    #clear the input
    x_a[0] = 0.0
    x_s[0] = 0.0 
    x_d[0] = 0.0
    x_f[0] = 0.0 
    x_g[0] = 0.0
    x_h[0] = 0.0 
    x_j[0] = 0.0
    x_k[0] = 0.0
    x_l[0] = 0.0
    x_z[0] = 0.0 
    x_x[0] = 0.0
    x_c[0] = 0.0 

    #clear the flag
    KEY_a = False
    KEY_s = False
    KEY_d = False
    KEY_f = False
    KEY_g = False
    KEY_h = False
    KEY_j = False
    KEY_k = False
    KEY_l = False
    KEY_z = False
    KEY_x = False
    KEY_c = False

    #add up the output of 12 filters
    y = a + s + d + f + g + h + j + k + l + z + x+ c

    
    y = np.clip(y.astype(int), -MAXVALUE, MAXVALUE)     # Clipping

    binary_data = struct.pack('h' * BLOCKLEN, *y);    # Convert to binary binary data
    stream.write(binary_data, BLOCKLEN)               # Write binary binary data to audio output

print('* Done.')

# Close audio stream
stream.stop_stream()
stream.close()
p.terminate()
