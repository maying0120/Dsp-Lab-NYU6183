function filter_gui_example_ver1

N = 100;
n = -10:N;
x=zeros(111,1);        
x(11)=1;          % this is Inmpulse signal
figure(1)
subplot(2,1,1)    %first, plot the impulse signal
impulse_response = plot(n, x);
xlabel('Time(sample)')
title('impulse signal')
xlim([-10 50])
ylim([-0.2 1])

subplot(2,1,2)
Nfft = 2^ceil(log2(N))              %plot the frequency response of the impulse response
X = fft(x, Nfft);                   % X will be of length Nfft
fn = (0:Nfft-1)/Nfft;               % fn : normalized frequency
frequency_response=plot(fn, abs(X))
xlabel('Frequency (normalized)')
title('Frequency response')
xlim([0 0.5])
ylim([0 1.1])
box off
drawnow;
uicontrol('Style', 'slider', ...
    'Min', 0.0, 'Max', 0.5,...
    'Value', 0.2, ...
    'SliderStep', [0.01 0.05], ...
    'Position', [5 5 200 20], ...           % [left, bottom, width, height]
    'Callback',  {@fun1, impulse_response, frequency_response, x, Nfft}    );

end

function fun1(hObject, eventdata, impulse_response, frequency_response, x, Nfft)

fc = get(hObject, 'Value');  % fc : cut-off frequency
fc = max(fc, 0.001);
fc = min(fc, 0.499);

subplot(2,1,1)
[b, a] = butter(4, 2*fc);   % Order-4 Butterworth filter (multiply fc by 2 due to non-conventional Matlab convention)
h = filtfilt(b, a, x);
set(impulse_response, 'ydata',  h);        % Update data in figure
title( sprintf('Impulse response of LPF. Cut-off frequency = %.3f', fc),'fontsize', 12)

subplot(2,1,2)
[H,om]=freqz(b,a);
f=om/(2*pi);
set(frequency_response, 'xdata',  f);
set(frequency_response, 'ydata',  abs(H));        % Update data in figure
title( sprintf('Frequency response of LPF. Cut-off frequency = %.3f', fc), 'fontsize', 12 )
end
