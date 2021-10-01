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
# Release 2.0:
 - Ability to encode and decode at different speeds (Planned: 100ms, 50ms, 20ms, and 10ms unit times.)
# Later releases:
 - Play encoded morse directly from morsetowav.py
 - Decode morse directly from an audio input device in wavtomorse.py
 - Auto-format input files to correct sample rate and channel configuration when importing wav files into wavtomorse.py
# Support
If you have any issues, please let me know at the email in my profile.
If you're transmitting over radio, I hope to hear you on the air at some point soon.

73,

Juno (KD2WZZ)
