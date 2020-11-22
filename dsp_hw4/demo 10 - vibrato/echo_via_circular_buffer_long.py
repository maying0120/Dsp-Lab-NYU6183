# echo_via_circular_buffer_long.py
# Reads a specified wave file (mono) and plays it with an echo.
# This implementation uses a circular buffer with two buffer indices.
# The buffer is longer than necessary.

import pyaudio
import wave
import struct
from myfunctions import clip16

wavfile = 'author.wav'
print('Play the wave file %s.' % wavfile)

# Open the wave file
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

# Delay parameters
b0 = 1.0            # direct-path gain
G = 0.8             # feed-forward gain
delay_sec = 0.05    # 50 milliseconds
N = int( RATE * delay_sec )   # delay in samples

# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN =  2048          # Set buffer length.  Must be more than N!
buffer = BUFFER_LEN * [0]   # list of zeros

# Initialize buffer indices
kr = BUFFER_LEN - N     # read index
kw = 0                  # write index

print('The delay of %.3f seconds is %d samples.' %  (delay_sec, N))
print('The buffer is %d samples long.' % BUFFER_LEN)

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(
    format      = pyaudio.paInt16,
    channels    = 1,
    rate        = RATE,
    input       = False,
    output      = True )

# Get first frame
input_bytes = wf.readframes(1)

print('* Start')

# Loop through wave file 
while len(input_bytes) > 0:

    # Convert string to number
    x0, = struct.unpack('h', input_bytes)

    # Compute output value
    # y(n) = b0 x(n) + G x(n-N)
    y0 = b0 * x0 + G * buffer[kr]

    # Update buffer (pure delay)
    buffer[kw] = x0

    # Increment read index
    kr = kr + 1
    if kr == BUFFER_LEN:
        # End of buffer. Circle back to front.
        kr = 0

    # Increment write index    
    kw = kw + 1
    if kw == BUFFER_LEN:
        # End of buffer. Circle back to front.
        kw = 0

    # Clip and convert output value to binary data
    output_bytes = struct.pack('h', int(clip16(y0)))

    # Write output to audio stream
    stream.write(output_bytes)

    # Get next frame
    input_bytes = wf.readframes(1)     

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()