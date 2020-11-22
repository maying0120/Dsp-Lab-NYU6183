# device_info.py
# print audio device information

import pyaudio

p = pyaudio.PyAudio()

number_of_devices = p.get_device_count()

print('Number of devices:', number_of_devices)

property_list = ['name', 'defaultSampleRate', 'maxInputChannels', 'maxOutputChannels']

for i in range(0, number_of_devices):
    print('Device', i,':')
    for s in property_list:
        print(' ', s, '=', p.get_device_info_by_index(i)[s])

