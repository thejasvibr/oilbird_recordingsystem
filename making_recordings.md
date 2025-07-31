# Performing recordings
After having connecting all the mics and pre-amp cables etc. now we can 'collect' data!

These instructions are assuming you have the software setup (see [software setup](software_setup.md) done correctly. 

* Open up Command Prompt, and type ```conda activate oilbird```

* Start a recording with the default parameters with ```python manual_recording.py``` and inspect the recorded audio with Audacity to see if you pick up any audio on the correct channel. 

* Remember you can change the duration of the recordings. 
* All audio files are saved with 'oilbird_multichannel_<APINAME>-API_rec-endtime_<YYYY-MM-DD_hh-mm-ss>.wav'.
* To change the duration of the recording run ```python manual_recording.py -rec_durn 10``` - for a 10 second recording
* Remember, in Command Prompt you can always use tab-completion and the up/down arrows to use the past few commands again - NO NEED to type repetitive stuff again and again!