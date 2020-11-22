# FFT_demo_02.py

import numpy as np

x = np.array([3, 7, 2, 5, 1])
X = np.fft.fft(x)
g = np.fft.ifft(X)
err = x - g                 # reconstruction error


print('x is of type:', type(x))
print('X is of type:', type(X))
print('g is of type:', type(g))
print('err is of type:', type(err))

print('x = ', x)
print('X = ', X)
print('max(abs(err) = ', np.max(np.abs(err)))
