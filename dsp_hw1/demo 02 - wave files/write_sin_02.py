# write_sin_02
# 
# Make a wave file (.wav) consisting of a sine wave

# 32 bits per sample

from struct import pack
from math import sin, pi
import wave

Fs = 8000

# Write a mono wave file 

wf = wave.open('sin_02_mono.wav', 'w')		# wf : wave file
wf.setnchannels(1)			# one channel (mono)
wf.setsampwidth(4)			# four bytes per sample (32 bits per sample)
wf.setframerate(Fs)			# samples per second
A = 2**31 - 1.0 			# amplitude
f = 220.0					# frequency in Hz (note A3)
N = int(0.5*Fs)				# half-second in samples

for n in range(0, N):	    # half-second loop 
	x = A * sin(2*pi*f/Fs*n)
	byte_string = pack('i', int(x)) 
	# 'i' stands for 'integer' (32 bits)
	wf.writeframesraw(byte_string)
wf.close()
