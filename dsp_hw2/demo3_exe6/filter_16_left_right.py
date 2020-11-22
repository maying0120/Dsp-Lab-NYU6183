# filter_16_r
# Like filter_16 with adjustable pole radius

from math import cos, pi 
import pyaudio
import struct

# Fs : Sampling frequency (samples/second)
Fs = 8000


T = 2       # T : Duration of audio to play (seconds)
N = T*Fs    # N : Number of samples to play

# Pole location
f1 = 400.0
om1 = 2.0*pi * f1/Fs
r = 0.999

f2 = 200.0
om2 = 2.0*pi * f2/Fs
r = 0.999

# Difference equation coefficients
a1_r= -2*r*cos(om1)
a2_r= r**2

a1_l= -2*r*cos(om2)
a2_l= r**2


print('a1_r = %f' % a1_r)
print('a2_r = %f' % a2_r)
print('a1_l = %f' % a1_l)
print('a2_l = %f' % a2_l)
# Initialization
y1_r = 0.0
y2_r = 0.0
y1_l = 0.0
y2_l = 0.0
gain = 5000.0

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,  
                channels = 2, 
                rate = Fs,
                input = False, 
                output = True)

for n in range(0, N):

    # Use impulse as input signal
    if n == 0:
        x0 = 1.0
    else:
        x0 = 0.0

    # Difference equation
    y0_r = x0 - a1_r * y1_r - a2_r * y2_r
    y0_l = x0 - a1_l * y1_l - a2_l * y2_l
    
    # Delays
    y2_r = y1_r
    y1_r = y0_r
    y2_l = y1_l
    y1_l = y0_l
    # Output
    output_value = [int(gain * y0_r),int(gain * y0_l)]
    output_string = struct.pack('hh', *output_value)     # 'h' for 16 bits
    stream.write(output_string)

print("* Finished *")

stream.stop_stream()
stream.close()
p.terminate()
