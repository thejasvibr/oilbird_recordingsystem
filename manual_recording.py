import datetime as dt
import sounddevice as sd
import soundfile as sf
import numpy as np 
import matplotlib.pyplot as plt 
import time
from tascam_finder import get_device_indexnumber   

import argparse
help_text = """

file_prefix : text to add at the beginning of a file

recdurn : duration of recording to be made in seconds.

hostapi: the host API to use for the audio recording. Either MME, WASAPI, or WDM-KS, defaults to MME

device: the name of the device as it appears on sd.query_devices(), Defaults to 'Microphone (US-16x08)'
"""

parser = argparse.ArgumentParser(description=help_text,)
parser.add_argument('-hostapi', type=str, help=help_text, default='MME')
parser.add_argument('-file_prefix', type=str, default='')
parser.add_argument('-rec_durn', type=float, help=help_text, default=3)
parser.add_argument('-devicename', type=str, help=help_text, 
default='Microphone (US-16x08)')
args = parser.parse_args()


device_name = args.devicename
dev_hostapi = args.hostapi
prefix = args.file_prefix

device_index = get_device_indexnumber(device_name=device_name, hostapi=dev_hostapi)
fs = 96000 # sampling rate in Hz
recording_durn = args.rec_durn # seconds
print('......starting recording now...')

audio = sd.rec(int(fs*recording_durn), samplerate=fs,
    channels=16, device=device_index, blocking=True)
endtime = dt.datetime.now()
print('....recording done now....')
# save the end time in LOCAL timesystem
recname = args.file_prefix + '_oilbird_multichaudio_' + f'{dev_hostapi}-API_'+'rec-endtime_'+endtime.strftime("%Y-%m-%d_%H-%M-%S")+'.wav'

print('writing file....')
sf.write(f'{recname}', audio, fs)
print('....Done writing file....')