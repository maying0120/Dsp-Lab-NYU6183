# FFT_demo_04.py
# Plot the FFT of a cosine

import numpy as np
from matplotlib import pyplot

N = 16
n = np.arange(0, N)     # n = [0, 1, 2, ..., N-1]
f0 = 3.0 				# Try also f0 = 2.5
x = np.cos(2.0 * np.pi * f0 / N * n)
X = np.fft.fft(x)

fig = pyplot.figure(1)

pyplot.subplot(2, 1, 1)
pyplot.stem(n, x)
pyplot.xlim(-1, N)
pyplot.title('Signal')

pyplot.subplot(2, 1, 2)
pyplot.stem(n, np.abs(X))
# pyplot.stem(n, np.angle(X))  # for phase
pyplot.xlim(-1, N)
pyplot.title('Spectrum')

pyplot.show()
fig.savefig('FFT_demo_04.pdf')


