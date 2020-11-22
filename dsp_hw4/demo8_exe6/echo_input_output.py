# echo_with_mic_input.py

import pyaudio
import wave
import struct
from myfunctions import clip16

WIDTH       = 2         # Number of bytes per sample
CHANNELS    = 1         # mono
RATE        = 16000     # Sampling rate (frames/second)
DURATION    = 2        # duration of processing (seconds)

N_samples = DURATION * RATE     # N : Number of samples to process


print('The number of channels(s) is %d '            % CHANNELS)
print('The frame rate is %d frames/second.'    % RATE)
print('There are %d bytes per sample.'         % WIDTH)

# Set parameters of delay system
b0 = 1.0            # direct-path gain
G = 0.8             # feed-forward gain
delay_sec = 0.05    # delay in seconds, 50 milliseconds   Try delay_sec = 0.02
N = int( RATE * delay_sec )   # delay in samples

print('The delay of %.3f seconds is %d samples.' %  (delay_sec, N))

# Buffer to store past signal values. Initialize to zero.
BUFFER_LEN = N              # length of buffer
buffer = BUFFER_LEN * [0]   # list of zeros

# Open an output audio stream
p = pyaudio.PyAudio()

stream = p.open(format      = pyaudio.paInt16,
                channels    = 1,
                rate        = RATE,
                input       = True,
                output      = True )


# Initialize buffer index (circular index)
k = 0





# Write to wave file

wf1 = wave.open('output.wav', 'w')		# wf : wave file
num_channels    = 1         # mono
DURATION    = 2         # duration of processing (seconds)
RATE        = 16000     # Sampling rate (frames/second)
N = DURATION * RATE     # N : Number of samples to process


wf1.setnchannels(1)			# one channel (mono)
wf1.setsampwidth(2)			# Two bytes per sample (16 bits per sample)
wf1.setframerate(16000)			# samples per second

print('* Start')

for n in range(0, N_samples):

    # Get one frame from audio input (microphone)
    input_bytes = stream.read(1, exception_on_overflow = False)

    # Convert binary data to tuple of numbers
    input_number = struct.unpack('h', input_bytes)
    print(input_number)
    x0=input_number[0]
    
    # Compute output value
    # y(n) = b0 x(n) + G x(n-N)
    y0 = b0 * x0 + G * buffer[k]

    # Update buffer
    buffer[k] = x0

    # Increment buffer index
    k = k + 1
    if k >= BUFFER_LEN:
        # The index has reached the end of the buffer. Circle the index back to the front.
        k = 0

    
    # Clip and convert output value to binary data
    output_bytes = struct.pack('h', int(clip16(y0)))
    

    wf1.writeframes(output_bytes)

    # Write output value to audio stream
    stream.write(output_bytes)
   

print('* Finished')

stream.stop_stream()
stream.close()
p.terminate()

wf1.close()
