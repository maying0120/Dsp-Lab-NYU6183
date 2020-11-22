# FFT_demo_03.py

import numpy as np

N = 10
n = np.arange(0, N)     # n = [0, 1, 2, ..., N-1]
x = np.cos(2.0 * np.pi / N * n)
X = np.fft.fft(x)
g = np.fft.ifft(X)
err = x - g                 # reconstruction error

print('n = ', n)
print('x = ', x)
print('max(abs(err)) = ', np.max(np.abs(err)))

print('X = ', X)
print('abs(X) = ', np.abs(X))

np.set_printoptions(precision = 3)
np.set_printoptions(suppress = True)

print('abs(X) = ', np.abs(X))

