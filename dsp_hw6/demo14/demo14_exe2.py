import pyaudio
import struct
from matplotlib import pyplot as plt
import numpy as np
import math
from myfunctions import clip16
import scipy.signal

plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 15        # Duration (seconds)

NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')


# Difference equation coefficients
b0 =  0.008442692929081
b2 = -0.016885385858161
b4 =  0.008442692929081
b = [b0, 0.0, b2, 0.0, b4]

# a0 =  1.000000000000000
a1 = -3.580673542760982
a2 =  4.942669993770672
a3 = -3.114402101627517
a4 =  0.757546944478829
a = [1.0, a1, a2, a3, a4]

#plt.rcParams["font.family"]="STSong"
# Initialize plot window:
plt.figure(1)


f = np.arange(0, BLOCKSIZE)
plt.subplot(2,1,1)
line, = plt.plot([], [], color = 'blue')  # Create empty line
line.set_xdata(f)                         
line.set_label('input signal')
plt.xlim(0, BLOCKSIZE)
plt.xlabel('Time(sample)')
plt.legend()


plt.subplot(2,1,2)
output, = plt.plot([],[], color = 'red')
output.set_xdata(f)
output.set_label('filtered signal')
plt.xlim(0, BLOCKSIZE)
plt.xlabel('Time')
plt.legend()

# Open audio device:
p = pyaudio.PyAudio()
PA_FORMAT = p.get_format_from_width(WIDTH)

stream = p.open(
    format    = PA_FORMAT,
    channels  = CHANNELS,
    rate      = RATE,
    input     = True,
    output    = True)


# Create block (initialize to zero)
output_block = BLOCKSIZE * [0]

BLOCKLEN = 64
MAXVALUE = 2**15-1  # Maximum allowed output signal value (because WIDTH = 2)

ORDER = 4   # filter is fourth order
states = np.zeros(ORDER)

for i in range(0, NumBlocks):
    input_bytes = stream.read(BLOCKSIZE)                     # Read audio input stream
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_bytes)  # Convert

     
     # filter
    [output_block, states] = scipy.signal.lfilter(b, a, input_tuple, zi = states)
    # clipping
    output_block = np.clip(output_block, -MAXVALUE, MAXVALUE)
    # convert to integer
    output_block = output_block.astype(int)
        
    # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKSIZE, *output_block)

    # Write binary data to audio output stream
    stream.write(output_bytes)

    # Update y-data of plot

    plt.subplot(2,1,1)
    line.set_ydata(input_tuple)
    plt.ylim(-5000, 5000)
    plt.subplot(2,1,2)
    output.set_ydata(output_block)
    plt.ylim(-5000, 5000)
    plt.pause(0.001)
    # plt.draw()

plt.close()

stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')
