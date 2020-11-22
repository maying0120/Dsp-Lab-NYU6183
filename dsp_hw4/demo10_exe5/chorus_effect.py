import pyaudio
import wave
import struct
import math
from myfunctions import clip16

#wavfile = 'decay_cosine_mono.wav'
#wavfile = 'author.wav'
# wavfile = 'cosine_200_hz.wav'
wavfile = 'acoustic.wav'

print('Play the wave file: %s.' % wavfile)

# Open wave file
inf = wave.open( wavfile, 'rb')

# Read wave file properties
RATE        = inf.getframerate()     # Frame rate (frames/second)
WIDTH       = inf.getsampwidth()     # Number of bytes per sample
LEN         = inf.getnframes()       # Signal length
CHANNELS    = inf.getnchannels()     # Number of channels

print('The file has %d channel(s).'         % CHANNELS)
print('The file has %d frames/second.'      % RATE)
print('The file has %d frames.'             % LEN)
print('The file has %d bytes per sample.'   % WIDTH)

# Write a mono wave file

wf = wave.open('output_chorus1.wav', 'w')		# wf : wave file
wf.setnchannels(CHANNELS)			# one channel (mono)
wf.setsampwidth(WIDTH)			# Two bytes per sample (16 bits per sample)
wf.setframerate(RATE)			# samples per second

#chorus coefficient
g=0.8


# Vibrato parameters
f0 = 2
W = 0.2


# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN = int(RATE * 0.03 )         # Set buffer length.

#BUFFER_LEN = 1024  
buffer = BUFFER_LEN * [0]   # list of zeros

# Buffer (delay line) indices
kr =0  # read index
kw = int(0.5 * BUFFER_LEN)  # write index (initialize to middle of buffer)

print('The buffer is %d samples long.' % BUFFER_LEN)

# Open an output audio stream
p = pyaudio.PyAudio()
stream = p.open(format      = pyaudio.paInt16,
                channels    = CHANNELS,
                rate        = RATE,
                input       = False,
                output      = True )

print ('* Playing...')

# Loop through wave file
y=[]
for n in range(0, LEN):

    # Get sample from wave file
    input_bytes = inf.readframes(1)

    # Convert string to number
    x0, = struct.unpack('h', input_bytes)

    # Get previous and next buffer values (since kr is fractional)
    kr_prev = int(math.floor(kr))
    frac = kr - kr_prev    # 0 <= frac < 1
    kr_next = kr_prev + 1
    if kr_next == BUFFER_LEN:
        kr_next = 0

    # Compute output value using interpolation
    #y0 = x0+ g((1-frac) * buffer[kr_prev] + frac * buffer[kr_next])
    y0 = x0+g*((1-frac) * buffer[kr_prev] + frac * buffer[kr_next])
    y.append(y0)
    
    # Update buffer
    buffer[kw] = x0

    # Increment read index
    kr = kr + 1 + W * math.sin( 2 * math.pi * f0 * n / RATE )
        # Note: kr is fractional (not integer!)

    # Ensure that 0 <= kr < BUFFER_LEN
    if kr >= BUFFER_LEN:
        # End of buffer. Circle back to front.
        kr = kr - BUFFER_LEN

    # Increment write index    
    kw = kw + 1
    if kw == BUFFER_LEN:
        # End of buffer. Circle back to front.
        kw = 0

    # Clip and convert output value to binary data
    output_bytes = struct.pack('h', int(clip16(y0)))

    # Write output to audio stream
    stream.write(output_bytes)

print('* Finished')

# save the output signal into a wave file after all data are processed
for n in range(0,LEN):
    output_bytes = struct.pack('h', int(clip16(y[n])))  
    wf.writeframes(output_bytes)

print('* Finished all')

stream.stop_stream()
stream.close()
p.terminate()
wf.close()
