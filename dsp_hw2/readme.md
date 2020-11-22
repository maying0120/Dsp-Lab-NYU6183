1. Modify filter_16.py to avoid run-time overflow errors even if gain is very high, by clipping the signal as necessary. To do this, insert an if statement to verify that the sample value is in the allowed range. If it is not, then set the value to its maximum (positive or negative) allowed value, before writing it to the audio stream. Test your program by setting the gain to a high value.

2. Implement the filter in real-time using Python/PyAudio.

3. Modify filter_16.py so that it produces a stereo signal with a different frequency in left and right channels. Use headphones to verify the stereo effect.

4. Modify the Matlab demo program filter_cat.m to use different filters.

   1. (a)  A higher-order Butterworth band-pass filter.
   2. (b)  A Chebyshev Type II band-pass filter (use cheby2 instead of butter in Matlab to design the filter coefficients).
   3. (c)  An elliptic band-pass filter (use ellip in Matlab to design the filter coefficients).
   4. (d)  A Butterworth band-stop filter (instead of a band-pass filter).

   Produce plots showing the filters and the input and output signals, as in the demo file. Comment on your observations.