# wave_filter_canonical.py

import pyaudio
import wave
import struct
import math

from myfunctions import clip16

wavefile = 'author.wav'

print('Play the wave file %s.' % wavefile)

# Open wave file (should be mono channel)
wf = wave.open( wavefile, 'rb' )


# Write a mono wave file

wf1 = wave.open('output.wav', 'w')		# wf : wave file
num_channels    = 1         # mono
DURATION    = 2         # duration of processing (seconds)
RATE        = 16000     # Sampling rate (frames/second)
N = DURATION * RATE     # N : Number of samples to process


wf1.setnchannels(1)			# one channel (mono)
wf1.setsampwidth(2)			# Two bytes per sample (16 bits per sample)
wf1.setframerate(16000)			# samples per second






# Read the wave file properties
num_channels    = wf.getnchannels()     # Number of channels
RATE            = wf.getframerate()     # Sampling rate (frames/second)
signal_length   = wf.getnframes()       # Signal length
width           = wf.getsampwidth()     # Number of bytes per sample




print('The file has %d channel(s).'            % num_channels)
print('The frame rate is %d frames/second.'    % RATE)
print('The file has %d frames.'                % signal_length)
print('There are %d bytes per sample.'         % width)

# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829

# Initialization
w1 = 0.0
w2 = 0.0
w3 = 0.0
w4 = 0.0

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = num_channels,
    rate        = RATE,
    input       = False,
    output      = True )


# Get first frame from wave file
input_bytes = wf.readframes(1)

y=[]

while len(input_bytes) > 0:

    # Convert binary data to number
    input_tuple = struct.unpack('h', input_bytes)  # One-element tuple
    input_value = input_tuple[0]                    # Number

    # Set input to difference equation
    x0 = input_value

    # Canonical form
    w0=x0-a1*w1-a2*w2-a3*w3-a4*w4
    y0 = b0*w0 + b2*w2 + b4*w4


    # Delays
    w4 = w3
    w3 = w2
    w2 = w1
    w1 = w0

    # Compute output value
    output_value = int(clip16(y0))    # Integer in allowed range

    # Convert output value to binary data
    output_bytes = struct.pack('h', output_value)  
    


    # Write binary data to audio stream
    stream.write(output_bytes)                     

    # Get next frame from wave file
    input_bytes = wf.readframes(1)
    
    output_bytes = struct.pack('h', output_value)  
    wf1.writeframes(output_bytes)

print('* Finished')

'''wf1 = wave.open('output.wav', 'w')		# wf : wave file
num_channels    = 1         # mono
DURATION    = 2         # duration of processing (seconds)
RATE        = 16000     # Sampling rate (frames/second)
N = DURATION * RATE     # N : Number of samples to process


wf1.setnchannels(1)			# one channel (mono)
wf1.setsampwidth(2)			# Two bytes per sample (16 bits per sample)
wf1.setframerate(16000)			# samples per second

while len(input_bytes) > 0:
    output_bytes = struct.pack('h', y[n])  
    wf1.writeframes(output_bytes)'''



stream.stop_stream()
stream.close()
p.terminate()
wf.close()
