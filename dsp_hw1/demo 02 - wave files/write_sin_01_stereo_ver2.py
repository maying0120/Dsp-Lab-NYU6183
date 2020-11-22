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

# Write a stereo wave file

wf = wave.open('sin_01_stereo_ver2.wav', 'w')
wf.setnchannels(2)			# two channels (stereo)
wf.setsampwidth(2)			# two bytes per sample (16 bits per sample)
wf.setframerate(Fs)			# samples per second
A = 2**15 - 1.0 			# amplitude
f1 = 261.6					# frequency in Hz (middle C)
f2 = 440.0  				# note A4
N = int(0.5*Fs)				# half-second in samples

for n in range(0, N):		# half-second loop 

	# left channel
	x = A * sin(2*pi*f1/Fs*n)
	byte_string_1 = pack('h', int(x))
	# 'h' stands for 'short integer' (16 bits)

	# right channel
	x = A * sin(2*pi*f2/Fs*n)
	byte_string_2 = pack('h', int(x))

	# concatenation
	byte_string = byte_string_1 + byte_string_2
	wf.writeframes(byte_string)

wf.close()
