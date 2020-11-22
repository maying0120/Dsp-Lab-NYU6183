# plot_microphone_input_spectrum.py

"""
Using Pyaudio, get audio input and plot real-time FFT of blocks.
Ivan Selesnick, October 2015
Based on program by Gerald Schuller
"""

import pyaudio
import struct
from matplotlib import pyplot as plt
import numpy as np

plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 8        # Duration (seconds)

NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')

DBscale = False
# DBscale = True

# Initialize plot window:
plt.figure(1)
if DBscale:
    plt.ylim(0, 150)
else:
    plt.ylim(0, 20*RATE)

# Frequency axis (Hz)
plt.xlim(0, 0.5*RATE)         # set x-axis limits
# plt.xlim(0, 2000)         # set x-axis limits
plt.xlabel('Frequency (Hz)')
f = RATE/BLOCKSIZE * np.arange(0, BLOCKSIZE)

line, = plt.plot([], [], color = 'blue')  # Create empty line
line.set_xdata(f)                         # x-data of plot (frequency)

# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = False)


for i in range(0, NumBlocks):
    input_bytes = stream.read(BLOCKSIZE)                     # Read audio input stream
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_bytes)  # Convert
    X = np.fft.fft(input_tuple)

    # Update y-data of plot
    if DBscale:
        line.set_ydata(20 * np.log10(np.abs(X)))
    else:
        line.set_ydata(np.abs(X))
    plt.pause(0.001)
    # plt.draw()

plt.close()

stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')
