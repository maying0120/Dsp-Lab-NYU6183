1. Amplitude Modulation. Modify the Python program plot_microphone_input_spectrum so it applies amplitude modulation (AM) to the microphone input audio signal. The program should plot the live frequency spectra (Fourier transform) of both the input and output signals (use two different colors and/or two subplots to distinguish the two signals). The Fourier transform should be computed using the FFT. The program should also play the output (result of AM) to the speaker/headphones. What is the relation between the spectra of the output and input signals?

2. Like the previous exercise. Also plot the input and output signals in real-time in a figure window (use different colors for the input and output signals).

3. Tkinter is a Python library for making graphical user interfaces (GUIs). Tkinter stands for

   ToolKit Interface.
    For documentation and resources about Tkinter, see notes_TKinter.pdf in the folder of

   demo programs.

   **Exercise**

   Make your own original GUI using Tkinter.

   • Your GUI should use all the widgets shown in the demo programs (label, button, entry, scale).

   • Your GUI should also use at least one additional widget: checkbutton, radiobutton, or listbox.

   • Optional: use bind illustrated in the demo programs TKdemo_07_click.py and TKdemo_08_keyboard.py to read information from the keyboard and mouse.

   Your GUI does not need to include any audio functionality. We will combine TKinter and audio later.