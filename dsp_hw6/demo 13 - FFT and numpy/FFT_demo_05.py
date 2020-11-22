# FFT_demo_05.py

# Real FFT

import numpy as np
from matplotlib import pyplot

N = 20
n = np.arange(0, N)     # n = [0, 1, 2, ..., N-1]
f0 = 3.0
x = np.cos(2.0 * np.pi * f0 / N * n)
X = np.fft.rfft(x)
g = np.fft.irfft(X)
err = x - g                 # reconstruction error

print('max(abs(err)) = ', np.max(np.abs(err)))

fig = pyplot.figure(1)

pyplot.subplot(2, 1, 1)
pyplot.stem(n, x)
pyplot.xlim(-1, N)
pyplot.title('Signal')

k = np.arange(len(X))

pyplot.subplot(2, 1, 2)
pyplot.stem(k, np.abs(X))
pyplot.xlim(-1, N)
pyplot.title('Spectrum')

fig.savefig('FFT_demo_05.pdf')
pyplot.show()

