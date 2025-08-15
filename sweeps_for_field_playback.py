"""
Sweeps for field playback
=========================

"""

import argparse
import scipy.signal as signal 
import numpy as np 
import matplotlib.pyplot as plt 
import soundfile as sf

help_text = '''
Generate a series of sweeps at 2 Hz.
Th
The mono audio file is 3 minutes.
'''
help_sweepdurn = 'sweep_durn : float>0, sweep duration in seconds. Defaults to 10 ms'
help_startfreq = 'start_freq : float>0, starting frquency in Hz. Defaults to 15 kHz'
help_endfreq = 'end_freq : float>0, end frequency in Hz'
help_samplerate = 'samplerate: float>0, sample rate in Hz. Defaults to 44100 Hz'
parser = argparse.ArgumentParser(description=help_text,)
parser.add_argument('-sweep_durn', type=float, help=help_sweepdurn, default=0.01)
parser.add_argument('-start_freq', type=float, help=help_startfreq, default=15e3)
parser.add_argument('-end_freq', type=float, help=help_endfreq, 
default=200)
parser.add_argument('-samplerate', type=int, help=help_samplerate,
default=44100)

args = parser.parse_args()

if args.sweep_durn >= 0.5:
    raise ValueError(f'The sweep duration must be <= 0.5 s. Current value is {args.durn}')

fs = args.samplerate
t = np.linspace(0, args.sweep_durn, int(fs*args.sweep_durn))
start_f, end_f = args.start_freq, args.end_freq
sweep = signal.chirp(t, start_f, t[-1], end_f)
sweep *= signal.windows.tukey(sweep.size, 0.95)
sweep *= 0.8

# now put the audio into the 0.5 sec chunk
halfsec_chunk = np.zeros(int(fs*0.5))
halfsec_chunk[-sweep.size:] += sweep 

# Make 360 repeats - for 180 seconds
repeat_playbacks = np.tile(halfsec_chunk, 360)
filename = f'linearsweep_{int(args.sweep_durn*1e3)}ms_{fs}Hzsamplerate_{np.around(start_f,10)}_to_{np.around(end_f,1)}Hz.wav'
sf.write(filename, repeat_playbacks, fs)