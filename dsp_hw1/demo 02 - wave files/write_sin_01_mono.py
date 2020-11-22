# write_sin_01
# 
# Make a wave file (.wav) consisting of a sine wave
# Adapted from http://www.swharden.com/blog/2011-07-08-create-mono-and-stereo-wave-files-with-python/

# 16 bits per sample

# For 'wave' functions, see:
# https://docs.python.org/3/library/wave.html

# For 'pack' function see:
# https://docs.python.org/3/library/struct.html

from struct import pack
from math import sin, pi
import wave

Fs = 8000

# Write a mono wave file

wf = wave.open('sin_01_mono.wav', 'w')		# wf : wave file
wf.setnchannels(1)			# one channel (mono)
wf.setsampwidth(2)			# two bytes per sample (16 bits per sample)
wf.setframerate(Fs)			# samples per second

A = 2**15 - 1.0 			# amplitude
f = 220.0					# frequency in Hz (note A3)
N = int(0.5*Fs)				# half-second in samples

for n in range(0, N):	    # half-second loop 
	x = A * sin(2*pi*f/Fs*n)       	# signal value (float)
	byte_string = pack('h', int(x))   
	# 'h' stands for 'short integer' (16 bits)
	wf.writeframes(byte_string)
wf.close()
