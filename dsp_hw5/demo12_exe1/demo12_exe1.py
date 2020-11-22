import pyaudio
import struct
import math
from matplotlib import pyplot
from myfunctions import clip16


f0 = 500    # Modulation frequency 

BLOCKLEN = 1024      # Number of frames per block
WIDTH = 2           # Number of bytes per signal value
CHANNELS = 1        # mono
RATE = 8000        # Frame rate (frames/second)
RECORD_SECONDS = 15

p = pyaudio.PyAudio()

# Set up plotting...

pyplot.ion()           # Turn on interactive mode so plot gets updated

fig = pyplot.figure(1)

[g1] = pyplot.plot([], [])
[g2] = pyplot.plot([], [])


g1.set_xdata(range(BLOCKLEN))
g1.set_color('blue')
g1.set_label('original signal')
pyplot.ylim(-25000, 25000)
pyplot.xlim(0, BLOCKLEN)
pyplot.xlabel('Time(n)')
g2.set_xdata(range(BLOCKLEN))
g2.set_color('red')
g2.set_label('signal with AM')


pyplot.legend()


stream = p.open(
    format      = p.get_format_from_width(WIDTH),
    channels    = CHANNELS,
    rate        = RATE,
    input       = True,
    output      = True)


output_block = BLOCKLEN * [0]

# Initialize phase
om = 2*math.pi*f0/RATE
theta = 0

# Number of blocks to run for
num_blocks = int(RATE / BLOCKLEN * RECORD_SECONDS)

print('* Recording for %.3f seconds' % RECORD_SECONDS)

# Start loop
for i in range(0, num_blocks):

    # Get frames from audio input stream
    # input_bytes = stream.read(BLOCKLEN)       # BLOCKLEN = number of frames read
    input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)   # BLOCKLEN = number of frames read

    # Convert binary data to tuple of numbers
    input_tuple = struct.unpack('h' * BLOCKLEN, input_bytes)
   
    # Go through block
    for n in range(0, BLOCKLEN):
        # Amplitude modulation:
        theta = theta + om
        output_block[n] = int( clip16(input_tuple[n] * math.cos(theta) ))

        
    g1.set_ydata(input_tuple)
    g2.set_ydata(output_block)
    pyplot.pause(0.0001)
    
    # keep theta betwen -pi and pi
    while theta > math.pi:
        theta = theta - 2*math.pi

    # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *output_block)

    # Write binary data to audio output stream
    stream.write(output_bytes)

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()


pyplot.ioff()           # Turn off interactive mode
pyplot.show()           # Keep plot showing at end of program
