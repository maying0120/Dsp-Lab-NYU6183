1. For the filter implemented in the demo program, what is the difference equation, transfer function, and impulse response? Use Matlab to plot the pole-zero diagram of the filter.

2. Modify the demo program so the input audio is from the microphone, and the output signal is saved to a wave file. Create a wave file of applying the filter to yourself saying your name; and submit your wave file as part of your work.

3. In the demo program echo_via_circular_buffer.py, change the line: buffer[k]=x0     buffer[k]=y0

   and comment on how this affects the sound of the output. With this change, what is the difference equation, transfer function, and impulse response of the system?

   What happens when the gain for the delayed value is greater than 1?

4. Write a Python program to implement the flanger effect. Use interpolation for an improved result. As described in Chapter 2 of Audio Effects: Theory, Implementation and Application, the flanger effect is Courtesy of CRC Press/Taylor & Francis Group,like the vibrato effect but it additionally has a direct path, as shown in the figure. The input signal should be read from a wave file.