# plot_wave_file_and_play.py

import pyaudio
import struct
import wave
from matplotlib import pyplot

'''
# Specify wave file
wavfile = 'author.wav'
print('Name of wave file: %s' % wavfile)

# Open wave file
wf = wave.open( wavfile, 'rb')

# Read wave file properties
RATE        = wf.getframerate()     # Frame rate (frames/second)
WIDTH       = wf.getsampwidth()     # Number of bytes per sample
LEN         = wf.getnframes()       # Signal length
CHANNELS    = wf.getnchannels()     # Number of channels

print('The file has %d channel(s).'         % CHANNELS)
print('The file has %d frames/second.'      % RATE)
print('The file has %d frames.'             % LEN)
print('The file has %d bytes per sample.'   % WIDTH)

'''

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 2        # duration of processing (seconds)
N_samples = DURATION * RATE     # N : Number of samples to process
RECORD_SECONDS = 25


print('The number of channels(s) is %d '            % CHANNELS)
print('The frame rate is %d frames/second.'    % RATE)
print('There are %d bytes per sample.'         % WIDTH)



BLOCKLEN = 1200    # Blocksize
num_blocks = int(RATE / BLOCKLEN * RECORD_SECONDS)

# Set up plotting...

pyplot.ion()           # Turn on interactive mode so plot gets updated

fig = pyplot.figure(1)

[g1] = pyplot.plot([], [])
[g2] = pyplot.plot([], [])


g1.set_xdata(range(BLOCKLEN))
g1.set_color('blue')
pyplot.ylim(-25000, 25000)
pyplot.xlim(0, BLOCKLEN)
pyplot.xlabel('Time(n)')
g2.set_xdata(range(BLOCKLEN))
g2.set_color('red')


g1.set_label('input signal')
g2.set_label('output signal')

pyplot.legend()
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
x1 = 0.0
x2 = 0.0
x3 = 0.0
x4 = 0.0
y1 = 0.0
y2 = 0.0
y3 = 0.0
y4 = 0.0


# Open the audio output stream
p = pyaudio.PyAudio()



stream = p.open(format      = pyaudio.paInt16,
                channels    = CHANNELS,
                rate        = RATE,
                input       = True,
                output      = True )


'''
PA_FORMAT = p.get_format_from_width(WIDTH)
stream = p.open(
    format = PA_FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = False,
    output = True,
    frames_per_buffer = 256)
'''

# Create block (initialize to zero)
output_block = BLOCKLEN * [0]

# Get block of samples from wave file
#input_bytes = wf.readframes(BLOCKLEN)

#input_bytes = stream.read(BLOCKLEN)

#input_bytes = stream.read(1, exception_on_overflow = False)


print('this is num_blocks',num_blocks)
print('this is BLOCKLEN',BLOCKLEN)
for i in range(0, BLOCKLEN):

    # Get one frame from audio input (microphone)
    input_bytes = stream.read(BLOCKLEN, exception_on_overflow = False)

    # Convert binary data to tuple of numbers
    signal_block = struct.unpack('h'* BLOCKLEN, input_bytes)
#while len(input_bytes) >= BLOCKLEN * WIDTH:
    #print(signal_block)
    # Convert binary data to number sequence (tuple)
    #signal_block = struct.unpack('h' * BLOCKLEN, input_bytes)
     # Go through block
    #for n in range(0, BLOCKLEN):
        # filtered with order-6 Butterworth filter
    #x0 = signal_block[0]
    
    for n in range(0, BLOCKLEN):
    	x0 = signal_block[n]
    	output_block[n] = int( b0*x0 + b2*x2 + b4*x4 - a1*y1 - a2*y2 - a3*y3 - a4*y4)

        # Delays
    	x4 = x3
    	x3 = x2
    	x2 = x1
    	x1 = x0
    	y4 = y3
    	y3 = y2
    	y2 = y1
    	y1 = output_block[n]
    	
    	
		  
    #print(output_block)
    g1.set_ydata(signal_block)
    g2.set_ydata(output_block)


    pyplot.pause(0.0001)
    
  # Convert values to binary data
    output_bytes = struct.pack('h' * BLOCKLEN, *output_block)
    
    # Write binary data to audio output stream
    stream.write(output_bytes, BLOCKLEN)
  
  
    # Get block of samples from wave file
    #input_bytes = wf.readframes(BLOCKLEN)
    input_bytes = stream.read(BLOCKLEN)
    

stream.stop_stream()
stream.close()
p.terminate()

wf.close()
pyplot.ioff()           # Turn off interactive mode
pyplot.show()           # Keep plot showing at end of program

audio.terminate()