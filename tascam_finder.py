import sounddevice as sd
import numpy as np 

def get_device_indexnumber(device_name='US-16x08', hostapi='MME'):
    '''
    Check for the device name in all of the recognised devices and
    return the index number within the list.

    Parameters
    ----------
    device_name : str, optional
        Name of the device as it appears on sd.query_devices()
        Defaults to 'US-16x08'
    when_manyofsamename: str, optional 
        What to do when >1 devices with the same sounddevice name are
        found. Defaults to 'first', which takes the first device. 
        Alternately if 'last' is given, then the last index is chosen.
    '''
    device_list = sd.query_devices()
    all_hostapis = [each['name']  for each in sd.query_hostapis()]
    
    tgt_ind = False
    for each in device_list:
        name_is_there = device_name in each['name']
        hostapi_is_same = hostapi in all_hostapis[each['hostapi']]
        details_match = np.logical_and(name_is_there, hostapi_is_same) 
        #print(each['name'])
        if details_match:
            tgt_ind = each['index']
        

    if not tgt_ind:
        print (sd.query_devices())

        raise ValueError('The input device \n' + device_name+
        '\n could not be found, please look at the list above'+
                         ' for all the recognised devices'+
                         ' \n Please use sd.query_devices to check the  recognised'
                         +' devices on this computer')

    return tgt_ind