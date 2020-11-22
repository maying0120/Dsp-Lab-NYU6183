1. **Exercises**

   **Tkinter and Pyaudio**

   1) In the demo program Tk_demo_04_slider.py, whenever the gain slider is adjusted, a clicking sound can be heard, due to the discontinuity in signal waveform due to a sudden change in amplitude. Modify this program so there is no click (no signal discontinuity).

   2) Implement a real-time echo effect GUI with a slider to control the delay time. Use a circular buffer.

   2) Make a real-time vibrato effect GUI with sliders to control the parameters (LFO, depth).

   3) Make a real-time AM effect GUI with sliders to control the parameters (modulation frequency, gain).

2. Write a program that plays a different note for different keys on the keyboard. The program can be based on keyboard_demo_06.py, but instead of just a single note, it should enable a whole octave of notes (12 notes).
    The notes should play overlappingly (if a note is played before the previous notes have become silent, then both notes should be heard at the same time). There should be a difference equation (filter) to implement each note. Each difference equation should have its own input and output signal. The output signals of the separate filters should be added together to give the total output signal. The total output signal should be written to the output audio device (loudspeaker/headphones).

   For a full octave (twelve notes), adjacent notes on a piano keyboard are related via

   fk = 2^(k/12)f0,  k=0,1,2....

   You can set f0 = 440 Hz which is middle A.