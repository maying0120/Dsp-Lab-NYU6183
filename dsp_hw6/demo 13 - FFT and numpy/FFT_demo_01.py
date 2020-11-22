# FFT_demo_01.py

import numpy as np

x = [3, 7, 2, 5, 1]
X = np.fft.fft(x)         # Fourier transform
g = np.fft.ifft(X)        # inverse Fourier transform
err = x - g               # reconstruction error

print('x = ', x)
print('X = ', X)
print('g = ', g)
print('err = ', err)

print('x is of type:', type(x))
print('X is of type:', type(X))
print('g is of type:', type(g))
print('err is of type:', type(err))

print('max(abs(err)) = %f' % np.max(np.abs(err)))

np.set_printoptions(suppress = True)
print('err = ', err)


