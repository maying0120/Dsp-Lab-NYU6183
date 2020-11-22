%% wave_filter_matlab_HPF.m
% High-pass filtering

%% Load wave file

[x, Fs] = audioread('author.wav');

N = length(x);
n = 1:N;
t = n/Fs;

figure(1)
clf
plot(t, x)
xlabel('Time (sec)')
title('Speech signal')
zoom xon

% sound(x, Fs);

%% Make filter
% high-pass filter

[b, a] = butter(2, 800*2/Fs, 'high')

%% Pole-zero diagram

figure(1)
clf
zplane(b, a)
title('Pole-zero diagram')

%% Frequency response

[H, om] = freqz(b, a);
f = om*Fs/(2*pi);
figure(1)
clf
plot(f, abs(H))
xlabel('Frequency (Hz)')
title('Frequency response')

%% Impulse response
% discrete-time plot

L = 150;
imp = [1 zeros(1, L)];
h = filter(b, a, imp);

figure(1)
clf
stem(0:L, h)
xlabel('Discrete time (n)')
title('Impulse response')
xlim([-10 150])

%% Impulse response
% continuous-time plot

figure(1)
clf
plot((0:L)/Fs, h)
xlabel('Time (sec)')
title('Impulse response')
xlim([-0.001 0.01])

%% Apply filter to speech signal

y = filter(b, a, x);   % implement difference equation

figure(1)
clf
plot(t, x, t, y - 0.5)
xlabel('Time (sec)')
title('Speech signal and filtered speech signal')
zoom xon

%% Write output signal to wave file

audiowrite('output_matlab_hpf.wav', y, Fs);

%%

sound(x, Fs)

%%

sound(y, Fs)

%% Filter coefficients
% Copy these coefficients into Python program to implement
% the same filter. Display in long format for higher accuracy.

format long
b'
a'

