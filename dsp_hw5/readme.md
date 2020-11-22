1. Repeat the previous exercise, but take the input audio from the microphone instead of a wave file. (Note, demo 12B might be useful as reference for this exercise.

2. The demo program AM_blocks_from_microphone.py shows how to read the microphone signal in blocks, apply amplitude modulation to this signal, then send the resulting signal in blocks to the output audio device. In a previous demo, we saw how to plot audio signals in real time.

   In this exercise, modify the program AM_blocks_from_microphone.py to plot the output signal on the computer screen at the same time the output signal plays on the loudspeaker. The input signal can also be shown on the computer screen. You can use different colors for input and output signals (and/or offset the two signals) so they are more easily distinguished.

   As part of your submission, submit a video (or a link to a video) using the NYU video streaming tool. The video should be a screen recording of less than one minute, of you introducing yourself with the AM effect applied.

3. The past demo program play_vibrato_interpolation.py does not use blocking (it reads and writes one sample at a time). Write a version of this program that reads, processes, and writes the audio signal in blocks of 64 frames. Verify that the output signal of the new version (using block processing) is the same.