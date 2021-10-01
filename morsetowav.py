import wave
morseChart={'A':'.-', 'B':'-...',
            'C':'-.-.', 'D':'-..', 'E':'.',
            'F':'..-.', 'G':'--.', 'H':'....',
            'I':'..', 'J':'.---', 'K':'-.-',
            'L':'.-..', 'M':'--', 'N':'-.',
            'O':'---', 'P':'.--.', 'Q':'--.-',
            'R':'.-.', 'S':'...', 'T':'-',
            'U':'..-', 'V':'...-', 'W':'.--',
            'X':'-..-', 'Y':'-.--', 'Z':'--..',
            '1':'.----', '2':'..---', '3':'...--',
            '4':'....-', '5':'.....', '6':'-....',
            '7':'--...', '8':'---..', '9':'----.',
            '0':'-----', ' ':'____'} # 7 units space between words (1 included per .wav sample, 2 for letter, +4 extra for space = 7)
   
def morseEncode(message, filename, dump_morse_text=False):
    mc = "_"
    message = message.upper()
    for i in message:
        try:
            mc += morseChart[i] + "_" * 2 # 3 units space between letters (1 included per .wav sample)
        except KeyError as e:
            print("Invalid character '" + i + "' skipped.") # Screen out invalid characters and omit them from the data to send
    
    if(dump_morse_text): # Dump morse as text
        print(mc)

    wavFiles = [] # Not technically necessary at the moment but leaves the door open for different encoding speeds
    for i in mc: 
        wavFiles.append(i)
    
    with wave.open(filename+".wav", 'wb') as output: # Stitch audio samples and output
        with wave.open("wav-samples/"+wavFiles[0] + ".wav") as w:
            output.setparams(w.getparams())
        for infile in wavFiles:
            with wave.open("wav-samples/"+infile+".wav") as w:
                output.writeframes(w.readframes(w.getnframes()))

print("KD2WZZ's Morse to WAV Converter")
while True:
    print("Enter message string (A-Z, 0-9, spaces)")
    userMessage = input(":")
    print("Enter output filename (w/o extension)")
    userOutput = input(":")
    print("Encoding...")
    morseEncode(userMessage, userOutput)
    print("Done. (CTRL-C to exit)")
    

