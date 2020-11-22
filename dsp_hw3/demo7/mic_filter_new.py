# mic_filter.py
# Record from microphone, filter the signal,and play the output signal on the loud speaker.
# save the output signal in wave file

import pyaudio
import struct
from math import cos,pi
import wave

from myfunctions import clip16

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 2         # duration of processing (seconds)

N = DURATION * RATE     # N : Number of samples to process


Fs = 16000

# Write a mono wave file

wf = wave.open('output.wav', 'w')		# wf : wave file
wf.setnchannels(1)			# one channel (mono)
wf.setsampwidth(2)			# Two bytes per sample (16 bits per sample)
wf.setframerate(Fs)			# samples per second

FPB = 32
# Initialization
f0=400

p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True,
    frames_per_buffer = FPB)

print('* Start')

y=[]
for n in range(0, N):

    # Get one frame from audio input (microphone)
    input_bytes = stream.read(1,exception_on_overflow=False)
    # If you get run-time time input overflow errors, try:
    # input_bytes = stream.read(1, exception_on_overflow = False)

    # Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h', input_bytes)

    # Convert one-element tuple to number
    x0 = input_tuple[0]

    # Amplitude modulation
    y0 = x0*cos(2*pi*f0/Fs*n)
    
          
    # Compute output value
    output_value = int(clip16(10*y0))    # Number
    y.append( output_value)

    # Convert output value to binary data
    output_bytes = struct.pack('h', output_value)  

    # Write binary data to audio stream
    stream.write(output_bytes)
    
print('* Finished')

# save the output signal into a wave file after all data are processed
for n in range(0,N):
    output_bytes = struct.pack('h', y[n])  
    wf.writeframes(output_bytes)

print('* Finished saved the wave file')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
