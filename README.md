# morseaudiosuite
morsetowav.py: Generates a .wav file containing your international morse (A-Z, 0-9, spaces) message. Uses 50ms units.
wavtomorse.py: Converts a .wav file containing international morse to its original message. Uses 50ms units.
Ideal application is over radio, as wavtomorse.py is noise-tolerant and has limited but present error-correction capability.
# Important: Please read
Input .wav must be mono 48khz 16bit PCM, with 50ms units international morse A-Z, 0-9, and spaces ONLY. Otherwise, it will error out.
morsetowav.py already generates files at the correct sample rate and bit depth, so I recommend using that. 
Just mind your settings when recording over radio (I recommend using Audacity, as it lets you set your sample rate and bit depth per channel, as well as letting you mix down stereo to mono.
# Planned features:
Most of these will be quality of life improvements, the suite is fully functional as of initial release.
# morsetowav.py:
 - Play encoded morse directly from the command line without writing any files
 - Encode morse at different speeds
# wavtomorse.py:
 - Decode morse directly from an audio input device (ex. VB-Audio Cable and SDR#)
 - Auto-format input files to correct format (48khz, 16 bit PCM, mono)
 - Decode morse at different speeds
