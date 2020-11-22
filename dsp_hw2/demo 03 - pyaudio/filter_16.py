# filter_16.py
# 
# Implement the second-order recursive difference equation
# y(n) = x(n) - a1 y(n-1) - a2 y(n-2)
# 
# 16 bit/sample

from math import cos, pi 
import pyaudio
import struct


# Fs : Sampling frequency (samples/second)
Fs = 8000
# Also try other values of 'Fs'. What happens? Why?

T = 2       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

f1 = 400.0
om1 = 2.0*pi * f1/Fs
r = 0.999   

# Difference equation coefficients
a0=1
a1 = -2*r*cos(om1)
a2 = r**2
b0=1
b1=-r*cos(om1)
b2=0

# Initialization
y1 = 0.0
y2 = 0.0
gain =2**15-1
# Also try other values of 'gain'. What is the effect?
# gain = 20000.0

#print reuslt
print('a0 = %f' % a0)
print('a1 = %f' % a1)
print('a2 = %f' % a2)
print('b0 = %f' % b0)
print('b1 = %f' % b1)
print('b2 = %f' % b2)

# Create an audio object and open an audio stream for output
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 1, 
                rate = Fs,
                input = False, 
                output = True)

# paInt16 is 16 bits/sample

# Run difference equation
for n in range(0, N):

    # Use impulse as input signal
    if n == 0:
        x0 = 1.0
    else:
        x0 = 0.0
    if n==1:
        x1=1.0
    else:
        x1=0
    # Difference equation
    y0 = x0 - a1 * y1 - a2 * y2

    # Delays
    y2 = y1
    y1 = y0

    # Output
    output_value = gain * y0
    output_string = struct.pack('h', int(output_value))   # 'h' for 16 bits
    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
