import pyaudio
import struct
from matplotlib import pyplot as plt
import numpy as np
import math
from myfunctions import clip16

plt.ion()           # Turn on interactive mode so plot gets updated

WIDTH     = 2         # bytes per sample
CHANNELS  = 1         # mono
RATE      = 8000     # Sampling rate (samples/second)
BLOCKSIZE = 1024      # length of block (samples)
DURATION  = 20        # Duration (seconds)

NumBlocks = int( DURATION * RATE / BLOCKSIZE )

print('BLOCKSIZE =', BLOCKSIZE)
print('NumBlocks =', NumBlocks)
print('Running for ', DURATION, 'seconds...')


f0 = 400    # 'Duck' audio

#plt.figure()
# Initialize plot window:
plt.figure(1)


f = RATE/BLOCKSIZE * np.arange(0, BLOCKSIZE)

plt.subplot(2,1,1)
line, = plt.plot([], [], color = 'blue')  # Create empty line
line.set_xdata(f)                         # x-data of plot (frequency)
line.set_label('input signal')
plt.ylim(0, 20*RATE)
plt.xlim(0, RATE)
plt.xlabel('Frequency (Hz)')
plt.legend()


plt.subplot(2,1,2)
output, = plt.plot([],[], color = 'red')
output.set_xdata(f)
output.set_label('output signal')
plt.ylim(0, 20*RATE)
plt.xlim(0, RATE)
plt.xlabel('Frequency (Hz)')
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


# Initialize phase
om = 2 * math.pi * f0 / RATE
theta = 0

# Create block (initialize to zero)
output_block = BLOCKSIZE * [0]

for i in range(0, NumBlocks):
    input_bytes = stream.read(BLOCKSIZE)                     # Read audio input stream
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_bytes)  # Convert
    X = np.fft.fft(input_tuple)
     # Go through block
    for n in range(0, BLOCKSIZE):
        # Amplitude modulation  (frequency f0)
        theta = theta + om
        output_block[n] = int( clip16(input_tuple[n] * math.cos(theta)) )

        # keep theta betwen -pi and pi
        while theta > math.pi:
            theta = theta - 2*math.pi
        
    Y = np.fft.fft(output_block)
    # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKSIZE, *output_block)

    # Write binary data to audio output stream
    stream.write(output_bytes)

    # Update y-data of plot
   
    

    plt.subplot(2,1,1)
    line.set_ydata(np.abs(X))
    plt.subplot(2,1,2)
    output.set_ydata(np.abs(Y))
    plt.pause(0.001)
    # plt.draw()

plt.close()

stream.stop_stream()
stream.close()
p.terminate()

print('* Finished')
