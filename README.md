# morseaudiosuite
morsetowav: generates a .wav file containing your international morse (A-Z, 0-9, spaces) message. Uses 50ms units.
wavtomorse: Converts a .wav file containing international morse to its original message. Uses 50ms units.
Ideal application is over radio, as wavtomorse.py is noise-tolerant and has limited but present error-correction capability.
# IMPORTANT
READ: Input .wav must be 48khz 16bit signed, with 50ms units international morse A-Z, 0-9, and spaces ONLY. Otherwise, it will error out.
