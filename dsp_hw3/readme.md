1. Single program for mono and stereo. Write a single Python program to play both mono and stereo wave files. The program should determine the number of channels by reading the wave file information.

   Verify that your program can play both mono and stereo wave files encoded with 16-bits per sample.

2. The Python demo program implements the fourth-order difference equation with 8 variables to store past values (i.e., 8 delay units). This is the the direct form implementation. But a fourth-order difference equation can be implemented using just 4 variables to store past values (i.e., 4 delay units). The canonical form can be used for this purpose. See the block diagram in Fig. 7.2.4 on page 274 of the text book ‘Introduction to Signal Processing’ by Orfanidis.

   Modify the Python demo program to implement the difference equation using the canonical form. Instead of 8 delay variables (y1, y2, y3, y4, x1, x2, x3, x4) your new program should have just 4 delay variables. Verify the output produced by this implementation is the same as the output produced by the demo program.

3. Modify the demo program mic_filter.py to process the input signal x(t) so that the output signal is  y(t) = x(t) cos(2πf0t), where f0 = 400 Hz. This is amplitude modulation. The output signal y(t) should both be played to the speaker (or headphones) and saved to a wave file. What is the effect of this on the voice signal? Submit your wave (wav) file of yourself talking, as well as your code.